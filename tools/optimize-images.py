#!/usr/bin/env python3
"""Make the optimized versions of every new photo for the site.

Every new photo goes through this script. Drop the original into assets/images/ (or pass its path) and run,
from the site folder (needs ffmpeg and ffprobe on PATH):

    python3 tools/optimize-images.py                         # all new photos in assets/images/
    python3 tools/optimize-images.py assets/images/photo.png # one file (also accepts a file in assets/source/)
    python3 tools/optimize-images.py photo.png --name final-photo
    python3 tools/optimize-images.py --check                 # rebuild all photos in a temp folder, compare
                                                             # with the files in assets/images/, write nothing

For each photo the script:
  1. moves the original to assets/source/ (an original that is already there is never overwritten);
  2. writes WebP + JPEG fallback in two sizes to assets/images/, never upscaled:
         <name>-800.webp / .jpg     about 800px on the longer side
         <name>-1600.webp / .jpg    about 1600px on the longer side (or the original size if it is smaller;
                                    the suffix is then the real longer side, e.g. -1448)
     Quality: WebP 78, JPEG -q:v 4 (no visible loss at these sizes);
  3. prints the files, their sizes, the <picture> srcset values and width/height.

New photo = a PNG/JPEG/TIFF/BMP/HEIC/AVIF file in assets/images/ that is not itself an output (<name>-<number>)
and has no WebP of the same name next to it (that pair is an optimized file with its fallback, e.g. gia.webp +
gia.png). A photo whose <name>-800.webp already exists is skipped as processed; --force rebuilds its versions
(the original is still never touched). WebP files in assets/images/ are treated as already optimized.
Rules: docs/GIA-SITE-DESIGN-SYSTEM.md, section on photography.
"""
import argparse
import filecmp
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMAGES = ROOT / "assets" / "images"
SOURCE = ROOT / "assets" / "source"
SIZES = (800, 1600)  # longer side
WEBP_QUALITY = 78
JPEG_QSCALE = 4  # ffmpeg -q:v, lower is better
ORIGINAL_EXTS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".heic", ".avif"}
OUTPUT_RE = re.compile(r"-\d+$")


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height", "-of", "json", str(path)],
        check=True, capture_output=True, text=True).stdout
    s = json.loads(out)["streams"][0]
    return s["width"], s["height"]


def ffmpeg(src, scale, extra, dest):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", f"scale={scale}:flags=lanczos{extra[0]}",
                    *extra[1], str(dest)], check=True)


def is_processed(name):
    return (IMAGES / f"{name}-{SIZES[0]}.webp").exists()


def find_new():
    """Originals waiting in assets/images/."""
    found = []
    for p in sorted(IMAGES.iterdir()):
        if not p.is_file() or p.suffix.lower() not in ORIGINAL_EXTS or OUTPUT_RE.search(p.stem):
            continue
        if (IMAGES / f"{p.stem}.webp").exists():  # optimized WebP + its fallback
            continue
        found.append(p)
    return found


def adopt(src):
    """Move an original from assets/images/ to assets/source/. Returns the path in assets/source/."""
    dest = SOURCE / src.name
    if dest.exists():
        if filecmp.cmp(src, dest, shallow=False):
            src.unlink()  # identical copy already kept as the original
            print(f"{src.relative_to(ROOT)}: same as {dest.relative_to(ROOT)}, removed the copy")
            return dest
        sys.exit(f"{dest.relative_to(ROOT)} already exists and differs from {src.relative_to(ROOT)}; "
                 f"rename the new file (originals are never overwritten)")
    SOURCE.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dest))
    print(f"moved {src.relative_to(ROOT)} -> {dest.relative_to(ROOT)}")
    return dest


def build(src, name, out):
    """Write the versions of src to out. Returns the list of written files."""
    w, h = probe(src)
    longer = max(w, h)
    written = []
    srcset = {"webp": [], "jpg": []}
    for target in SIZES:
        side = min(target, longer)
        k = side / longer
        sw, sh = round(w * k / 2) * 2, round(h * k / 2) * 2
        for ext, extra in (("webp", ("", ["-c:v", "libwebp", "-quality", str(WEBP_QUALITY), "-compression_level", "6"])),
                           ("jpg", (",format=yuvj420p", ["-q:v", str(JPEG_QSCALE)]))):
            dest = out / f"{name}-{side}.{ext}"
            ffmpeg(src, f"{sw}:{sh}", extra, dest)
            written.append(dest)
            srcset[ext].append(f"assets/images/{dest.name} {sw}w")
            if out == IMAGES:
                print(f"  {dest.relative_to(ROOT)}  {sw}x{sh}  {dest.stat().st_size // 1024} KB")
        if side == longer:
            break
    if out == IMAGES:
        for ext, items in srcset.items():
            print(f'  srcset ({ext}): "{", ".join(items)}"')
        print(f'  width/height of the largest version: width="{sw}" height="{sh}"')
    return written


def process(src, name, force):
    if src.resolve().parent == IMAGES.resolve():
        if is_processed(name) and not force:
            print(f"{src.relative_to(ROOT)}: {name} is already processed, skipped (the file stays where it is)")
            return
        src = adopt(src)
    elif is_processed(name) and not force:
        print(f"{name}: already processed, skipped (use --force to rebuild)")
        return
    print(f"{name}  (from {src.relative_to(ROOT) if src.is_relative_to(ROOT) else src})")
    build(src, name, IMAGES)


def check():
    """Rebuild every processed photo whose original is in assets/source/ and compare with assets/images/."""
    pairs = [(p, p.stem) for p in sorted(SOURCE.iterdir())
             if p.is_file() and p.suffix.lower() in ORIGINAL_EXTS and is_processed(p.stem)]
    if not pairs:
        sys.exit("nothing to check")
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        for src, name in pairs:
            for f in build(src, name, pathlib.Path(tmp)):
                ref = IMAGES / f.name
                same = ref.exists() and filecmp.cmp(f, ref, shallow=False)
                bad += not same
                print(f"{'same     ' if same else 'DIFFERENT'}  assets/images/{f.name}")
    sys.exit(1 if bad else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("source", nargs="?", help="one original (default: every new photo in assets/images/)")
    ap.add_argument("--name", help="output base name (default: the source file name)")
    ap.add_argument("--force", action="store_true", help="rebuild the versions of an already processed photo")
    ap.add_argument("--check", action="store_true", help="rebuild in a temp folder and compare, write nothing")
    args = ap.parse_args()

    if args.check:
        check()
    if args.source:
        src = pathlib.Path(args.source).resolve()
        if not src.is_file():
            sys.exit(f"not found: {args.source}")
        process(src, args.name or src.stem, args.force)
        return
    if args.name:
        sys.exit("--name needs a source file")
    new = find_new()
    if not new:
        print("no new photos in assets/images/")
    for src in new:
        process(src, src.stem, args.force)


if __name__ == "__main__":
    main()
