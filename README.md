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
                               Gia core (photo in a gold ring), pulse diagram
    css/shell.css              header, mobile menu, scroll progress, footer, logo
    css/pages/<page>.css       page-only sections (meet-gia, glo, global-connections, how-glo-works)
    js/components.js           shared component behavior: approval sheet, play-once hero video (pages 2-4),
                               pulse diagrams [data-pulse] (wiring, pulses, card status; the hub's routes and scenario)
    js/site.js                 shared shell: menu, scroll progress, active section, reveal; exposes window.GiaSite
    js/pages/meet-gia.js       Meet Gia: hero scroll video, section 03 video, In action, Memory, permissions, approval, waitlist
    js/pages/meet-gia-frames.js  list of Meet Gia hero video frames
    js/pages/<page>.js         page scripts for the other pages (how-glo-works.js: the ecosystem pulse diagram)
    assets/logo/               Glonari mark, horizontal and stacked lockups, favicons
    assets/hero-frames/        96 WebP frames of the Meet Gia hero video (scroll-scrubbed on a canvas)
    assets/video/              works-with-you.mp4, the Meet Gia section 03 video (plays once per visit)
    assets/images/             optimized photos (gia.webp + gia.png fallback, 400x400 face crop of
                               assets/source/gia-original.png) and the section 03 first/last frames
    assets/source/             originals: videos, persona photos, logos as supplied
    docs/                      design system, color system, wireframes
    docs/components.html       live reference of every shared component (open via the local server)
    tools/build-shell.py       writes the shared header, mobile menu and footer into all four pages

Every page loads tokens, base, components, shell and its own page CSS, then js/site.js and its own page script.

## Site shell (header, mobile menu, footer)

The shell markup sits in each page between `<!-- shell:header -->` and `<!-- shell:footer -->` markers.
Do not edit it by hand: change `tools/build-shell.py` (pages, section lists, footer links and wording), then run

    python3 tools/build-shell.py

Header: level 1 lists the four pages, level 2 lists the sections of the current page, with a scroll-progress bar.
At 1100px and below both collapse into the menu button.

## Notes

- Colors: docs/GLONARI_PULSE_COLORS.md has priority. Everything else visual and structural (type, spacing, grid, components, logo, site shell, motion): docs/GIA-SITE-DESIGN-SYSTEM.md.
- Hero video: plays over the first 85% of the hero scroll; the last 15% holds the final frame with the CTA.
  To replace it, re-export frames:
  `ffmpeg -i new.mp4 -an -vf "select='not(mod(n\,2))',scale=1280:-1" -vsync vfr -c:v libwebp -quality 70 assets/hero-frames/f%03d.webp`
  and update the count in js/pages/meet-gia-frames.js.
- Section 03 video: plays once each time the visitor reaches the screen (when 40% of it is visible), then stops
  on its last frame. When the screen is scrolled fully out of view it rewinds, so it plays again on the next visit.
  Muted, no audio track, no loop. Before playing it shows the first frame (works-with-you-start.webp).
  To replace it: `ffmpeg -i new.mp4 -an -c:v libx264 -crf 23 -pix_fmt yuv420p -movflags +faststart assets/video/works-with-you.mp4`
  and re-export the first and last frames as WebP.
- Reduced motion: the hero shows its final frame immediately; section 03 shows the video's last frame as a still.
- The waitlist form does not send data yet.
- Footer placeholders: "Learn about membership", Privacy and Terms have no destination yet; the important-information wording is a draft for product and legal review.
- Placeholders, Meet Gia: final CTA image (temporary frame from the hero video), privacy/storage FAQ answer.
- Hero of pages 2-4: full-screen media with the text on the side.
  Introducing GLO: assets/video/hero-glo.mp4 (8 s, no audio; original in assets/source/hero-glo-original.mp4),
  text on the right. Hero videos play once each time the hero comes into view (after 0.8 s), no loop;
  poster = first frame (hero-glo-poster.webp), reduced motion shows the last frame (hero-glo-still.webp).
  Global Connections: temporary image assets/images/hero-gc-temp.webp (original: assets/source/hero-gc-original.jpg), text on the left.
  The "$48 per GLO" figure on the monitor in the photo is blurred: the content rules forbid a rate per GLO.
  The final image must not show compensation figures.
  How GLO Works: animated systems diagram (inline SVG) on the right, text on the left; it builds once per visit.
- Placeholders, How GLO Works: final photo (member and Gia reviewing the four options), "Learn about membership"
  destination, option status labels (drafts).
- Placeholders, Global Connections: hero loop (temporary image), final CTA photo, the illustrative project total
  (to be set with the legal team), "Learn about membership" destination, status label (Coming next, draft).
  The example project (logistics market briefing) is invented for illustration and used consistently in sections 02-08.
- Placeholders, Introducing GLO: final CTA photo,
  "Learn about membership" destination, capability status labels (drafts, conservative), example values in the workspace.
- Pulse diagrams (Introducing GLO 02 hub, How GLO Works 06 ecosystem): Gia's photo in the center, wiring drawn in one SVG
  from the measured cards, pulses and card status driven by js/components.js. The cycle plays 3 times when the diagram
  comes into view, then rests on the final state; mouse hover plays it once more; it pauses off screen and in a hidden tab.
  Rules: docs/GIA-SITE-DESIGN-SYSTEM.md, section 8.6. reference/ holds design references only and is not part of the site.
