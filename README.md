# Gia site — draft

Static HTML/CSS/JS, no build step. Open `index.html` in a browser, or serve the folder:

    python3 -m http.server 8000   # then open http://localhost:8000

## Meet Gia sections (see docs/wireframes/Meet_Gia_Revised_Wireframe_EN.docx)

    01  Hero, scroll video                 #what
    02  How it works                       #how
    03  A Gia that works with you          #with-you   (short breather, 40/60 text + video that plays once)
    04  How people use Gia                 #people
    05  See Gia in action                  #in-action
    06  She gets to know you (Memory)      #memory
    07  Control, privacy & limits          #control
    08  She can work with you              #work
    09  More power, more tools             #more-power
    10  Final CTA                          #join

## Site

Four pages, in this order. Calls to action move the visitor forward through the sequence:
Meet Gia (the GLO card in More power) -> Introducing GLO -> Global Connections -> How GLO Works.
Introducing GLO also links straight to How GLO Works from its options section, as its wireframe asks.

    index.html                 Meet Gia            (built)
    glo.html                   Introducing GLO     (built)
    global-connections.html    Global Connections  (built)
    how-glo-works.html         How GLO Works       (built)

## Structure

    css/tokens.css             design tokens (colors from Glonari Pulse)
    css/base.css               reset, type, sections, buttons, reveal
    css/components.css         shared components: glass UI, chat atoms, status, card, split, log, tiers, task workspace,
                               final CTA, and (stage 3) page hero, badge, flow, steps line, hub, accordion,
                               option card, ownership indicator, terms sheet, approval sheet, is/is not, notice,
                               Gia core (photo in a gold ring), pulse diagram, card art (.card__art), quiet effects
    css/shell.css              header, mobile menu, scroll progress, footer, logo
    css/pages/<page>.css       page-only sections (meet-gia, glo, global-connections, how-glo-works)
    js/components.js           shared component behavior: approval sheet, play-once hero video (pages 2-4),
                               pulse diagrams [data-pulse] (wiring, pulses, card status; the hub's routes and scenario),
                               quiet effects switched on by attributes: [data-parallax], [data-stagger], [data-spotlight],
                               [data-draw], [data-shine]; card art (.card__art) and small line icons (svg.draw-icon)
                               draw themselves (design system 9.2 and 10.1; demos in docs/components.html)
    js/site.js                 shared shell: menu, scroll progress, active section, reveal; exposes window.GiaSite
    js/pages/meet-gia.js       Meet Gia: hero scroll video, section 03 video, In action, Memory, permissions, approval, waitlist
    js/pages/meet-gia-frames.js  list of Meet Gia hero video frames
    js/pages/<page>.js         page scripts for the other pages (how-glo-works.js: the ecosystem pulse diagram)
    assets/logo/               Glonari mark, horizontal and stacked lockups, favicons
    assets/hero-frames/        96 WebP frames of the Meet Gia hero video (scroll-scrubbed on a canvas)
    assets/video/              works-with-you.mp4, the Meet Gia section 03 video (plays once per visit)
    assets/images/             optimized photos (gia.webp + gia.png fallback, 400x400 face crop of
                               assets/source/gia-original.png) and the section 03 first/last frames
    assets/art/                source SVGs of the card line drawings (.card__art); pages inline the same SVG so
                               currentColor works (glo-uses-*: Introducing GLO #what-it-enables; hgw-option-*: How GLO Works
                               #your-options; hgw-layer-*: role marks in How GLO Works #three-layer, Gia's mark is her photo)
    assets/source/             originals: videos, persona photos, logos as supplied
    docs/                      design system, color system, wireframes
    docs/components.html       live reference of every shared component (open via the local server)
    tools/build-shell.py       writes the shared header, mobile menu and footer into all four pages
    tools/optimize-images.py   every new photo goes through it: moves the original to assets/source/, makes WebP + JPEG
                               versions (about 800 and 1600px, never upscaled) in assets/images/

Every page loads tokens, base, components, shell and its own page CSS, then js/site.js and its own page script.

## Site shell (header, mobile menu, footer)

The shell markup sits in each page between `<!-- shell:header -->` and `<!-- shell:footer -->` markers.
Do not edit it by hand: change `tools/build-shell.py` (pages, section lists, footer links and wording), then run

    python3 tools/build-shell.py

Header: level 1 lists the four pages, level 2 lists the sections of the current page, with a scroll-progress bar.
At 1100px and below both collapse into the menu button.

## Photos

Rule: every new photo goes through `tools/optimize-images.py` (needs ffmpeg and ffprobe). Put the original
(PNG, JPEG, ...) into assets/images/ and run

    python3 tools/optimize-images.py            # every new photo in assets/images/
    python3 tools/optimize-images.py <file>     # one file; --name <base> sets the output name

It moves the original to assets/source/ (never overwrites an original already there), writes
`<name>-800` and `<name>-1600` (or the real size if smaller) as WebP (quality 78) and JPEG (-q:v 4), and prints the
srcset and width/height to use in the page. Photos already processed are skipped (`--force` rebuilds their versions).
`--check` rebuilds everything in a temp folder and compares it with assets/images/ without writing.

## Notes

- Colors: docs/GLONARI_PULSE_COLORS.md has priority. Everything else visual and structural (type, spacing, grid, components, logo, site shell, motion): docs/GIA-SITE-DESIGN-SYSTEM.md.
- Hero video: the canvas starts below the header and frames are anchored near the top (FOCUS_Y in
  js/pages/meet-gia.js), so Gia's head stays visible; plays over the first 85% of the hero scroll; the last 15% holds the final frame with the CTA.
  To replace it, re-export frames:
  `ffmpeg -i new.mp4 -an -vf "select='not(mod(n\,2))',scale=1280:-1" -vsync vfr -c:v libwebp -quality 70 assets/hero-frames/f%03d.webp`
  and update the count in js/pages/meet-gia-frames.js.
- Section 03 video: plays once each time the visitor reaches the screen (when 40% of it is visible), then stops
  on its last frame. When the screen is scrolled fully out of view it rewinds, so it plays again on the next visit.
  Muted, no audio track, no loop. Before playing it shows the first frame (works-with-you-start.webp).
  To replace it: `ffmpeg -i new.mp4 -an -c:v libx264 -crf 23 -pix_fmt yuv420p -movflags +faststart assets/video/works-with-you.mp4`
  and re-export the first and last frames as WebP.
- Reduced motion: the hero shows its final frame immediately; section 03 shows the video's last frame as a still.
- The waitlist form does not send data yet. Launch condition: the Privacy and Terms pages must exist BEFORE the form starts
  sending data.
- Hidden until their pages exist (no service notes are shown on the site):
  "Learn about membership" buttons on Introducing GLO, Global Connections and How GLO Works (`hidden` attribute on the
  link, which already points to membership.html: remove `hidden` to show it; check the file name when the page is built);
  footer links Learn about membership, Privacy and Terms (set MEMBERSHIP_PAGE, PRIVACY_PAGE, TERMS_PAGE in
  tools/build-shell.py and run it; a footer column with no links is left out).
- The important-information wording in the footer is a draft for product and legal review.
- Meet Gia final CTA: video assets/video/final-gia.mp4 (plays once; poster final-gia-poster.webp, still final-gia-still.webp).
- Placeholders, Meet Gia: the FAQ question "Where is my data stored,
  and how do I delete it?" is hidden (`hidden` on its `details` in index.html) and waits for the answer from the product
  and legal teams: write the answer and remove `hidden`.
- Final photos (originals in assets/source/, optimized WebP + JPEG fallback in two sizes in assets/images/):
  Global Connections: gc-hero-workspace-800/-1600; How GLO Works: hgw-choice-panel-800 (600x800) / -1448 (full size).
  Introducing GLO final CTA: final-glo-800/-1600. The bar-chart tile on the panel is blurred (it could read as a
  growth chart, which the content rules forbid); the unblurred original is assets/source/final-glo-unblurred.png.
- Hero of pages 2-4: full-screen media with the text on the side.
  Introducing GLO: assets/video/hero-glo.mp4 (8 s, no audio; original in assets/source/hero-glo-original.mp4),
  text on the right; the video starts below the header (`.page-hero--below-header`, `--focus: 30% 10%`) so Gia's head
  is never hidden on short laptop screens, and page heroes have no parallax. Hero videos play once each time the hero comes into view (after 0.8 s), no loop;
  poster = first frame (hero-glo-poster.webp), reduced motion shows the last frame (hero-glo-still.webp).
  Global Connections: final image hero-gc-800/-1600 (master with the blur: assets/source/hero-gc.png; unblurred original:
  assets/source/hero-gc-original.jpg), text on the left.
  The "$48 per GLO" figure on the monitor in the photo is blurred: the content rules forbid a rate per GLO.
  Any replacement image must not show compensation figures either.
  How GLO Works: animated systems diagram (inline SVG) on the right, text on the left; it builds once per visit.
- Placeholders, How GLO Works: "Learn about membership" destination, option status labels (drafts).
- Placeholders, Global Connections: the illustrative project total
  (the terms card says "Defined in the project terms" until a value is set with the legal team), "Learn about membership"
  destination, status label (Coming next, draft).
  The example project (logistics market briefing) is invented for illustration and used consistently in sections 02-08.
- Placeholders, Introducing GLO:
  "Learn about membership" destination, capability status labels (drafts, conservative), example values in the workspace.
- Pulse diagrams (Introducing GLO 02 hub, How GLO Works 06 ecosystem): Gia's photo in the center, wiring drawn in one SVG
  from the measured cards, pulses and card status driven by js/components.js. The cycle plays 3 times when the diagram
  comes into view, then rests on the final state; mouse hover plays it once more; it pauses off screen and in a hidden tab.
  Rules: docs/GIA-SITE-DESIGN-SYSTEM.md, section 8.6. reference/ holds design references only, is not part of the site and is ignored by git (.gitignore).
