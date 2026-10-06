#!/usr/bin/env python3
"""Write the shared site shell (header, mobile menu, footer) into every page.

The site has no build step, so the shell markup lives in each HTML file between
marker comments:

    <!-- shell:header -->  ...  <!-- /shell:header -->
    <!-- shell:footer -->  ...  <!-- /shell:footer -->

Edit PAGES or the templates below, then run from the site folder:

    python3 tools/build-shell.py

Everything between the markers is replaced; nothing else in the page is touched.
Rules for the shell: docs/GIA-SITE-DESIGN-SYSTEM.md, section 13.
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Site sequence. Section lists come from each page's wireframe ("secondary in-page navigation").
# Each entry: (anchor id on the page, label in the navigation).
PAGES = [
    {
        "file": "index.html",
        "title": "Meet Gia",
        "top": "what",
        "sections": [
            ("what", "What is Gia"),
            ("how", "How it works"),
            ("people", "How people use Gia"),
            ("in-action", "In action"),
            ("memory", "Memory"),
            ("control", "Control"),
            ("work", "Work"),
            ("more-power", "More power"),
        ],
    },
    {
        "file": "glo.html",
        "title": "Introducing GLO",
        "top": "intro",
        "sections": [
            ("why-capacity", "Why capacity"),
            ("what-glo-is", "What GLO is"),
            ("what-it-enables", "What it enables"),
            ("how-it-works", "How it works"),
            ("your-options", "Your options"),
            ("global-connections", "Global Connections"),
            ("limits", "Limits"),
        ],
    },
    {
        "file": "global-connections.html",
        "title": "Global Connections",
        "top": "intro",
        "sections": [
            ("work-starts", "How work starts"),
            ("gia-finds", "Gia finds projects"),
            ("authorize", "Review & authorize"),
            ("gia-works", "Gia works"),
            ("deliverable", "Deliverable"),
            ("compensation", "Compensation"),
            ("project-end", "Project end"),
        ],
    },
    {
        "file": "how-glo-works.html",
        "title": "How GLO Works",
        "top": "intro",
        "sections": [
            ("three-layer", "Three-layer model"),
            ("reusable-capacity", "Reusable capacity"),
            ("your-options", "Your options"),
            ("gc-vs-market", "Global Connections vs market"),
            ("ecosystem", "Ecosystem"),
            ("important-info", "Important information"),
        ],
    },
]

WAITLIST = "index.html#join"  # the waitlist form lives on Meet Gia

IMPORTANT = (
    "GLO&trade; is Glonari&rsquo;s Membership &amp; Access Token. Qualifying GLO can give Gia access to "
    "additional resources under applicable program terms. GLO itself does not pay income, interest or yield, "
    "and does not guarantee appreciation, liquidity or resale. Not every capability described on this site "
    "is available today; each one is labeled with its current status."
)


def e(s):
    return html.escape(s, quote=True)


def page_links(current, cls_current):
    out = []
    for p in PAGES:
        cur = p["file"] == current["file"]
        attr = ' aria-current="page"' if cur else ""
        out.append(f'<a href="{p["file"]}"{attr}>{e(p["title"])}</a>')
    return out


def header(page):
    here = page["file"]
    on_home = here == "index.html"
    brand_href = f'#{page["top"]}' if on_home else "index.html"
    brand_label = "Glonari, back to top" if on_home else "Glonari, Meet Gia"
    cta = "#join" if on_home else WAITLIST
    pages = "\n        ".join(page_links(page, "is-current"))
    sections = "\n        ".join(f'<a href="#{i}">{e(t)}</a>' for i, t in page["sections"])

    mm = []
    for p in PAGES:
        if p["file"] == here:
            subs = "\n          ".join(f'<li><a href="#{i}">{e(t)}</a></li>' for i, t in p["sections"])
            mm.append(
                f'<li class="mm__page is-current"><a href="{p["file"]}" aria-current="page">{e(p["title"])}</a>\n'
                f'        <ul class="mm__sections" aria-label="On this page">\n          {subs}\n        </ul>\n      </li>'
            )
        else:
            mm.append(f'<li class="mm__page"><a href="{p["file"]}">{e(p["title"])}</a></li>')
    mm = "\n      ".join(mm)

    return f'''<!-- shell:header -->
<header class="site-header">
  <div class="site-header__row">
    <a class="brand" href="{brand_href}" aria-label="{brand_label}">
      <img class="brand__mark" src="assets/logo/glonari-mark.webp" width="192" height="192" alt="">
      <span class="brand__name">Glonari</span>
    </a>
    <nav class="site-nav" aria-label="Site">
        {pages}
    </nav>
    <a class="btn btn--primary btn--sm header-cta" href="{cta}">Join the waitlist</a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu"><span></span></button>
  </div>
  <div class="subnav">
    <nav class="subnav__inner" aria-label="On this page">
        {sections}
    </nav>
  </div>
  <div class="progress" aria-hidden="true"></div>
</header>
<div class="mobile-menu" id="mobile-menu">
  <nav aria-label="Site">
    <ul class="mm">
      {mm}
    </ul>
  </nav>
  <a class="btn btn--primary" href="{cta}">Join the waitlist</a>
</div>
<!-- /shell:header -->'''


def footer(page):
    here = page["file"]
    on_home = here == "index.html"
    logo_href = f'#{page["top"]}' if on_home else "index.html"
    logo_label = "Glonari, back to top" if on_home else "Glonari, Meet Gia"
    cta = "#join" if on_home else WAITLIST
    pages = "\n          ".join(f"<li>{a}</li>" for a in page_links(page, ""))
    return f'''<!-- shell:footer -->
<footer class="site-footer">
  <div class="container">
    <div class="footer__top">
      <div class="footer__brand">
        <a class="footer-logo" href="{logo_href}" aria-label="{logo_label}">
          <picture>
            <source media="(max-width: 768px)" srcset="assets/logo/glonari-lockup-stacked.webp" width="760" height="359">
            <img src="assets/logo/glonari-lockup-horizontal.webp" width="840" height="222" alt="Glonari. Experience more.">
          </picture>
        </a>
        <p class="small footer__about">Gia is your personal AI agent by Glonari.</p>
      </div>
      <nav class="footer__col" aria-label="Footer: site">
        <p class="footer__head">The site</p>
        <ul>
          {pages}
        </ul>
      </nav>
      <div class="footer__col">
        <p class="footer__head">Membership</p>
        <ul>
          <li><a href="{cta}">Join the waitlist</a></li>
          <li><span class="footer__todo">Learn about membership <span class="footer__tbc">link to be confirmed</span></span></li>
        </ul>
      </div>
      <div class="footer__col">
        <p class="footer__head">Legal</p>
        <ul>
          <li><span class="footer__todo">Privacy <span class="footer__tbc">page to come</span></span></li>
          <li><span class="footer__todo">Terms <span class="footer__tbc">page to come</span></span></li>
        </ul>
      </div>
    </div>
    <div class="footer__info">
      <p class="caption"><strong>Important information.</strong> {IMPORTANT}</p>
      <p class="caption placeholder-note">Draft wording, to be confirmed by the product and legal teams.</p>
    </div>
    <p class="caption mono footer__legal">© 2026 Glonari. Draft for content and design development.</p>
  </div>
</footer>
<!-- /shell:footer -->'''


def replace_block(text, name, new):
    pat = re.compile(rf"<!-- shell:{name} -->.*?<!-- /shell:{name} -->", re.S)
    if not pat.search(text):
        sys.exit(f"missing <!-- shell:{name} --> markers")
    return pat.sub(lambda _: new, text, count=1)


def main():
    for page in PAGES:
        path = ROOT / page["file"]
        text = path.read_text(encoding="utf-8")
        text = replace_block(text, "header", header(page))
        text = replace_block(text, "footer", footer(page))
        path.write_text(text, encoding="utf-8")
        print("updated", page["file"])


if __name__ == "__main__":
    main()
