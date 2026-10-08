# Gia Site Design System

Version: 2.0 (rewritten for gia-site from the Global Reserve design system v1.0)
Scope: the four-page Gia site — Meet Gia, Introducing GLO, Global Connections, How GLO Works — and its shared shell (header, mobile menu, footer).

## 1. Purpose and precedence

This file is the visual and structural source of truth for the Gia site, except for color.

When documents disagree, use this order:

1. The current task prompt controls the scope of the work.
2. `docs/GLONARI_PULSE_COLORS.md` controls every color value and the meaning of each color.
3. This file controls typography, spacing, grid, section rhythm, components, logo use, site shell, motion and responsive behavior.
4. The page wireframes control approved English copy, section order, terminology and required functionality:
   - all wireframes are in `docs/wireframes/`;
   - Meet Gia: `Meet_Gia_Revised_Wireframe_EN.docx`;
   - Introducing GLO, Global Connections, How GLO Works: `*_Revised_Wireframe_EN_v2.docx` (copy and direction) and `*_Simple_Wireframe.docx` (layout drawings).
5. A page or section that is already approved stays unchanged unless the current prompt explicitly changes it.

The wireframe drawings use orange, blue and green only as a legend (main action, Gia/active, retained/ready). On the site these map to the Glonari Pulse palette as described in section 8.4; never copy the drawing colors.

## 2. Design character

The site should feel:

- dark, warm and calm, lit like an evening interior;
- premium and cinematic at the edges of each page (hero and final call to action), concrete and legible in between;
- honest: every promise is shown through real product UI, a status, an approval or a limit;
- spacious but never empty; structured by alignment, contrast and rhythm;
- animated with restrained, purposeful motion.

Gia is the product and the intelligence. Glonari is the company. GLO is a capacity and access layer. Visual hierarchy follows this order on every page: Gia is always visually larger and more prominent than GLO.

Avoid:

- a light theme or light sections (the site is dark-only);
- coin stacks, medals, laurel wreaths, token-price charts, tickers, trading red/green or anything that reads as a crypto exchange or a game;
- gradients as large background fills (the one approved exception is `.section--glow`, see 6.1);
- decoration that means nothing once motion stops (small drawings in cards are allowed when each one conveys its own card's concept and still reads without motion, see 8.1);
- heavy drop shadows and ornamental cards;
- inconsistent section padding.

## 3. Tokens

All tokens live in `css/tokens.css`. Reuse them; never hard-code a value in a component when a token exists.

### 3.1 Color

Color tokens use the `--gp-` prefix and are defined by `docs/GLONARI_PULSE_COLORS.md`. Summary of roles:

| Role | Tokens |
|---|---|
| Page and surfaces | `--gp-black` (deep sections, header, footer), `--gp-bg` (page), `--gp-surface`, `--gp-surface-2`, `--gp-warm-dark` |
| Lines | `--gp-line` (dividers, inactive borders), `--gp-glass-border`, `--gp-glass-border-active` |
| Gold (actions, active states, icons) | `--gp-gold-glow`, `--gp-gold`, `--gp-gold-warm`, `--gp-gold-mid`, `--gp-gold-deep`, `--gp-gold-dark` |
| Editorial gold | `--gp-champagne` (display headlines), `--gp-copper` (eyebrows, labels) |
| Text | `--gp-text`, `--gp-text-2`, `--gp-text-muted`, `--gp-on-gold`, `--gp-white` (rare) |
| Data and status only | `--gp-green`, `--gp-blue`, `--gp-teal`, `--gp-violet`, `--gp-warning` |
| Effects | `--gp-btn-gradient`, `--gp-power-glow`, `--gp-glass` |

Data colors never appear on buttons, links or navigation.

### 3.2 Type, layout and motion

```css
:root {
  --font-display: "Playfair Display", Georgia, "Times New Roman", serif;
  --font-ui: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;

  --container-max: 1200px;
  --page-pad: clamp(24px, 3.5vw, 48px);    /* 24px ≤768, 20px ≤480 */
  --section-pad: clamp(96px, 11vw, 160px);
  --section-pad-compact: clamp(72px, 8vw, 96px);
  --grid-gap: clamp(48px, 6vw, 96px);
  --header-row: 72px;                      /* header level 1; 64px ≤768 */
  --subnav-h: 44px;                        /* header level 2 */
  --header-h: calc(var(--header-row) + var(--subnav-h));  /* total; equals --header-row ≤1100 */
  --ease: cubic-bezier(.22, .61, .36, 1);
}
```

The spacing scale is 8, 16, 24, 32, 48, 64, 96, 128, 160px. Use only these values for gaps and margins unless a component in section 9 defines its own internal value.

## 4. Typography

### 4.1 Font roles

- **Playfair Display** (display serif, champagne): only in these places —
  - the hero headline of each page (on Meet Gia, the scroll-video captions);
  - the final call-to-action headline of each page (`.final__h`);
  - the GLONARI wordmark in the header (section 12.4);
  - Gia's name inside product UI (for example `.phone__title`, `.gia-core__name`).
- **IBM Plex Sans**: everything else — H2 to H4, body, buttons, navigation, cards, product UI text.
- **IBM Plex Mono**: eyebrows, step numbers, status labels, timestamps, compact metadata, the copyright line.

Load all three families in one Google Fonts request.

### 4.2 Type scale

| Role | Class | Size | Weight | Line height | Letter spacing | Color |
|---|---|---:|---:|---:|---:|---|
| Hero headline (display) | page hero | `clamp(34px, 4.4vw, 62px)` | 600 | 1.08 | `-0.01em` | champagne |
| Final CTA headline (display) | `.final__h` | `clamp(36px, 4.5vw, 56px)` | 600 | 1.08 | `-0.01em` | champagne |
| H2 | `.h2` | `clamp(32px, 4vw, 48px)` | 700 | 1.10 | `-0.02em` | text |
| H3 | `.h3` | `clamp(20px, 2vw, 28px)` | 600 | 1.20 | `-0.01em` | text |
| H4 / item title | `.h4` | `18px` | 600 | 1.30 | normal | text |
| Lead | `.lead` | `clamp(18px, 1.8vw, 22px)` | 400 | 1.65 | normal | text-2 |
| Body | `.body` | `clamp(17px, 1.4vw, 20px)` | 400 | 1.70 | normal | text-2 |
| Small body | `.small` | `15px` | 400 | 1.60 | normal | text-2 |
| Eyebrow | `.eyebrow` | `12px` mono | 600 | 1.20 | `0.10em`, uppercase | copper |
| Caption | `.caption` | `13px` | 400 | 1.55 | normal | muted |
| Status label | `.status` | `11px` mono | 500 | — | `0.04em` | data color |

Each page has exactly one `h1` (the hero headline). Section titles are `h2`.

Eyebrows name the section and match the in-page navigation label where one exists. Do not add an eyebrow to a block that already has a heading saying the same thing.

### 4.3 Text width

- Standard text column: 500–560px (`.lead` max-width is 560px).
- Centered heading block: 720px maximum (`.head--center`).
- Final CTA text block and lists: 520px.
- Long body copy never spans the full container.

### 4.4 Vertical relationships

| Relationship | Distance |
|---|---:|
| Eyebrow to heading | 16px |
| Heading to lead or body | 24px |
| Paragraph to paragraph | 16px |
| Body to list, stat or primary component | 32–48px |
| Heading group to major media or grid (`.gap-major`) | 64–96px |
| Item title to item body | 8px |
| Caption to the media it describes | 12px |
| Text block to button row | 32–48px |

Do not position normal content with negative margins. The only approved negative margin is the full-bleed horizontal scroller on mobile (section 11).

## 5. Layout grid

### 5.1 Container

```css
.container { width: min(100%, var(--container-max)); margin-inline: auto; padding-inline: var(--page-pad); }
```

The 1200px maximum includes the side padding. The header inner row uses a wider 1400px track so the navigation has room; page content never exceeds 1200px except the approved 1360px breather on Meet Gia.

### 5.2 Columns

- Standard split (`.split`): `minmax(0, 1fr) minmax(0, 1fr)`, gap `--grid-gap`.
- Text-and-media hero and final CTA: roughly 1fr / 1.1fr, text left, media right.
- 40/60 split: only where a wireframe asks for it (Meet Gia breather).
- Card grids: 2, 3 or 4 equal columns, 24px gap.
- Every direct grid child gets `min-width: 0`.

### 5.3 Alignment

Section headings are left-aligned by default. Center a heading block (`.head--center`) only when the section that follows is itself symmetrical: a centered diagram, a row of equal cards, a single centered panel. The wireframe drawings indicate which sections are centered.

## 6. Sections and rhythm

### 6.1 Section types

| Class | Use | Padding |
|---|---|---|
| `.section` | standard content screen | `--section-pad` (160px desktop, 72–96px mobile) |
| `.section--compact` | short statement or breather | `--section-pad-compact` (96px desktop, 72px mobile) |
| `.section--deep` | alternating darker band, final CTA | background `--gp-black` |
| `.section--glow` | one moment per page where Gia's capability is the subject | soft gold radial glow at the top; at most one per page |

Pinned or scroll-scrubbed sections are exceptional. The Meet Gia hero is the only approved one. New pages use a calm hero composition (section 7.1), not a pinned scroll sequence.

### 6.2 Rhythm

- Alternate `--gp-bg` and `--gp-black` sections. This replaces the grey/white banding in the wireframe drawings.
- Never place two `.section--deep` sections next to each other unless the wireframe groups them.
- Every section owns its top and bottom padding. Do not rely on child margins for the space between screens.
- No borders between sections. The only horizontal hairlines on the page are inside components, under the header and above the footer.

## 7. Common compositions

### 7.1 Page hero (Introducing GLO, Global Connections, How GLO Works)

Approved direction (replaces the half-text, half-media split in the wireframe drawings): the image or video fills the whole first screen, and the text sits over it **on the side**. The image is darkened behind the text so it always reads clearly. Put the text on the side opposite the subject of the media.

- Markup: `section.page-hero` (text left), `.page-hero--right` (text right) or, if ever needed, `.page-hero--center` containing `div.page-hero__media` (an `img` or a `<picture>` made by `tools/optimize-images.py`, or a muted `video[data-play-once]` with a poster; `--focus` sets `object-position`), then `.container > .page-hero__text` with eyebrow, `h1.page-hero__title`, `.lead`, optional `.principle`, `.btn-row.btn-row--stack`. Optional `p.page-hero__tag` marks temporary media.
- Height: the full screen, at least 640px. The media runs behind the fixed header; the text clears it (`--header-h` + 48px) and is vertically centered.
- **Side text** (approved): text block up to 600px on the left (`.page-hero`) or right (`.page-hero--right`); a horizontal darkening from about 94% at the text edge to clear at 80% keeps the subject on the other side visible.
- Current pages: Introducing GLO — video, Gia on the left, text right; Global Connections — image, text left; How GLO Works — text left with the systems diagram on the right half over the dark background.
- How GLO Works hero diagram (`.hgw-stage`, inline SVG, `css/pages/how-glo-works.css`): You → Gia ← GLO capacity, Gia → useful outcome, then Use and Put it to work ("GLO stays with you"), Support (dashed, "defined by terms") and Transfer, drawn from GLO capacity on its own side of a divider ("ownership changes"). It builds once, node by node, each time the hero comes into view (`[data-motion]`, about 5 s), like the play-once video; reduced motion shows it complete. A second, portrait SVG replaces it at 600px and below. At 1280px and below the diagram moves above the text.
- **Centered text** (`--center`, available but not used): text block up to 760px, centered; the image is dimmed evenly with a slightly stronger oval behind the text.
- Both variants add a light darkening under the header and a fade into `--gp-black` at the bottom, so the hero flows into the next (deep) section. Override the fade color with `--hero-fade` if the next section is not deep.
- Phones (≤768px): the image still fills the screen; the text moves to the bottom over a strong vertical fade; buttons stack full width; a temporary-media tag moves to the top.
- Title: Playfair Display 600, `clamp(40px, 5.4vw, 76px)`, line height 1.04, champagne; lead in `--gp-text` for contrast over the image; a soft text shadow helps over busy areas.
- Hero video plays once per visit to the screen (see `video[data-play-once]` in 9.2), never in a loop. Reduced motion: it does not play and the last frame is shown as the complete composition.
- Primary button scrolls to the next section on the page or opens the next page in the sequence, as the wireframe specifies.
- Until real hero media is supplied, pages use temporary images from `assets/images/` (never images with financial charts, percentages or gains), or the dark placeholder `.page-hero__media--placeholder`. Temporary media is recorded in README.md, not tagged on the page.

### 7.2 Centered header plus content

- Header block max-width 720px, centered.
- Heading to lead: 24px. Header to the component below: 64–96px (`.gap-major`).
- Long body text inside a centered block stays left-aligned when that reads better.

### 7.3 Final call to action

- Split: text left, image right (`.final`, shared in `components.css`).
- Display headline (`.final__h`), short list (`.uses`), primary and secondary buttons (`.btn-row--stack`, 40px above), then `figure.media-frame` or `.final__media` with a caption.
- Every page ends with a final CTA before the footer.

### 7.4 Lists and process rows

- Row padding: 16–24px vertical, `1px solid var(--gp-line)` dividers.
- Item title to description: 8px.
- Active or emphasized state: gold marker or gold text, never a large gold fill.
- Numbered markers only for real sequences (steps, workflows, cycles). Do not number unordered sets such as the six resources or the four option cards.

## 8. Surfaces, buttons and media

### 8.1 Cards (marketing content)

- `.card`: background `--gp-surface`, `1px solid var(--gp-line)`, radius 8px, padding 28px (24px ≤560px inside a `.cards` grid).
- No shadow. Gold is never the full card background.
- A gold or champagne border marks the one card the visitor should act on.

#### Card art `.card__art` (optional)

- Placement: the first child of the card, above the badge and the title. The area is 96px high (72px ≤560px); the drawing is aligned left. An empty or missing slot takes no space (no height, no margin).
- Format: inline SVG or `<img>`; SVG is preferred. Line drawing at 1.5px stroke, colored `--gp-gold` / `--gp-champagne` through `currentColor`, transparent background, in the same graphic language as the site's diagrams (8.6).
- The forbidden motifs of section 2 apply here too (coin stacks, growth charts, tickers, medals and the like). Each drawing conveys its own card's concept and reads without motion.
- A decorative drawing gets `aria-hidden="true"` (an `<img>` also gets empty `alt`).
- Use it on: Introducing GLO `#what-it-enables` cards; How GLO Works `#your-options` option cards (one shared set of marks for Use, Put it to work, Support and Transfer, the same on both pages); the role marks in `#three-layer` (for Gia, her photo in a gold ring, as `.gia-core`); small icons in flow nodes (`.flow`).
- Do not use it on: Is / is not, project terms cards, the approval sheet or any other legally significant block.
- Motion: an SVG drawing draws itself each time the card comes into view, and is reset after the card has left the screen completely (1.2s, parts about 0.1s apart; in a `[data-stagger]` grid it starts after its own card has appeared). No attribute is needed; the drawing must read complete without motion and shows complete at once under reduced motion (section 10.1).
- Card art never gets parallax (section 10).

### 8.2 Glass panels (product UI only)

- `.glass`: `--gp-glass` background, 18px backdrop blur, `--gp-glass-border`, radius 16px; `.is-active` uses `--gp-glass-border-active`. A solid `--gp-surface` fallback applies when blur is not supported.
- Use glass only for things that are Gia's interface: chats, workspaces, approval sheets, project cards, memory panels.
- Never use glass for the header, the mobile menu, the footer or plain marketing cards.

### 8.3 Buttons

| Class | Use |
|---|---|
| `.btn--primary` | the one main action in a block; gold gradient, `--gp-on-gold` text |
| `.btn--secondary` | the alternative action; gold outline and text |
| `.btn--ghost` | low-emphasis or negative choices inside product UI ("Not now", "Decline", "Not for me") |
| `.btn--sm` | buttons inside product UI and the header |

- Height 48px (36px small), radius 8px (6px small), 16px gap in a `.btn-row`.
- On mobile, hero and CTA button rows stack at full width (`.btn-row--stack`).
- Button labels say exactly what happens: "Review project", "Authorize Gia", "Explore how GLO works". No arrows appended to labels.
- Product UI never offers a one-click consequential action. "Accept project" does not exist; the flow is "Review project" and then "Authorize Gia".

### 8.4 Status and meaning colors

Status labels are small mono text with a colored dot (`.status`). Mapping from the wireframe legend to the site:

| Meaning | Site treatment |
|---|---|
| Main action (orange in drawings) | gold primary button |
| Gia, active step, selected option (blue in drawings) | gold active border (`--gp-glass-border-active`) and gold text |
| Ready, done, GLO retained (green in drawings) | `--gp-green` status |
| Working, researching, analyzing | `--gp-blue` status |
| Needs review, not reviewed, ownership changes | `--gp-warning` status |
| Conditional or not yet available | dashed `--gp-line` border plus a "Coming next" status |
| Handed off, declined, inactive | `--gp-text-muted` status |

Every option (Use, Put it to work, Support, Transfer) carries a status badge on both Introducing GLO and How GLO Works; the drafts are all Coming next, Support is additionally shown as conditional (dashed). Capability availability uses four labels everywhere on the site: **Available now** (green), **With approval** (blue), **Coming next** (violet), **Vision** (muted). When in doubt, use the more conservative label. Final labels are confirmed by the product team.

### 8.5 Media

- Every image and video has an explicit `aspect-ratio` and `width`/`height` attributes.
- Photography and video use `object-fit: cover`, radius 8px (cards) or 16px (feature media), 1px border.
- Decorative media gets `aria-hidden="true"` or empty `alt`; informative images get a real description.
- Missing media keeps the layout: use a placeholder frame (`.media-frame--placeholder`) whose note says what will go there; no extra caption under it.
- Photos in a media frame use `<picture>`: a WebP `source` and a JPEG (or PNG) fallback `img`, each with a `srcset` of two sizes (about 800px and 1600px on the longer side, or the original if smaller) and `sizes` matching the column, plus `width`/`height`. The image fills the frame with `object-fit: cover`; set `object-position` per photo when the crop must keep a subject in frame. Media near the top of the page: `fetchpriority="high"`, no lazy loading; otherwise `loading="lazy"`. The versions are made with `tools/optimize-images.py`.
- Every new photo goes through `tools/optimize-images.py`, never by hand: drop the original into `assets/images/` and run `python3 tools/optimize-images.py`. It moves the original to `assets/source/` (an existing original is never overwritten) and writes `<name>-800` and `<name>-1600` (the real size if smaller, never upscaled) as WebP (quality 78) and JPEG fallback (`-q:v 4`). Already processed photos are skipped. Do not change these quality settings per photo.
- Optimized files are WebP in `assets/images/` or `assets/video/`; originals stay in `assets/source/`.
- Photos and videos in `.media-frame`, `.final__media` and `.page-hero__media` may use light parallax (`[data-parallax]`); the rule is in section 10.

### 8.6 Diagrams

Diagrams (resource hub, flows, cycles, the ecosystem map) are inline SVG or HTML with real text, not images.

- Nodes: `--gp-surface` fill, `--gp-line` border, radius 8px. The Gia node uses the active gold border and is the largest node. GLO is never larger than Gia and never gets a "brain" or agent treatment.
- Connectors: 1px `--gp-line`; an active path brightens to `--gp-gold-mid`.
- Labels are real text in IBM Plex Sans; every node corresponds to a named concept from the wireframe.
- Ownership indicators ("GLO stays with you", "Ownership changed") are pinned bars under the flow, styled as status, so they stay visible through the whole sequence.
- A static or reduced-motion diagram shows the complete picture.
- Where Gia is the center of a diagram (hub, ecosystem), she is shown as `.gia-core`: her photo (`assets/images/gia.webp`, PNG fallback, `alt="Gia"`) in a circle with a 1px `--gp-gold` ring and a soft gold glow, 180px wide and 140px in the vertical layout. Her name and role sit in a dark plate over the lower edge of the circle, never over her face.

#### Pulse diagrams `[data-pulse]` (hub, ecosystem)

- Wiring: one absolutely positioned SVG over the grid; every route is measured from the cards and the circle, so it starts at a card edge and ends at the circle (or the name plate, for routes from below) and is redrawn on resize. 1px `--gp-gold` at about 25% opacity, rounded corners; arrows where the wireframe has them.
- Pulse: a short glowing comet (bright head, fading tail) runs along a wire; a small glowing dot lights at each junction and end as it passes.
- Card status: a small indicator in the card's top-left corner spins while the pulse travels and turns into a gold check when it arrives.
- Gia's ring flashes once when the work reaches her (ecosystem) or before she sends it out (hub).
- **Playback rule**: when the diagram comes into view, its cycle plays 3 times, then stops on the final state (every check shown, wiring slightly brighter). Hovering the diagram with a mouse plays one more cycle. It pauses when it leaves the screen or the tab is hidden and resumes where it was; once it has finished, leaving the screen completely re-arms it for the next visit. Only transform, opacity and stroke-dashoffset are animated.
- Reduced motion: no animation; the final state is shown at once.
- Vertical layout at the component's breakpoint (hub 960px, ecosystem 860px): the cards above Gia join on a rail along one side, the cards below on the other; the same scenario plays.
- Hub (GLO 02): Gia decides what each task needs, so pulses run out from Gia to the resources in pairs (Compute + Agents, Models + Research, Tools + Execution), about 8 s per cycle.
- Ecosystem (How GLO Works 06): pulses run into Gia from You, Work requests and GLO capacity, Gia flashes, the pulse goes on to Deliverable, then the "After the work" paths light up one by one, about 9 s per cycle. Vertical order: You, Work requests, GLO capacity, Gia, Deliverable, After the work (grid areas only; the HTML order is unchanged).

## 9. Components

### 9.1 Shared now (`css/components.css`)

| Component | Classes | Notes |
|---|---|---|
| Glass panel | `.glass`, `.is-active` | product UI only |
| Chat atoms | `.bubble--user`, `.bubble--gia`, `.gia-tag`, `.gia-dot` | Gia speaks in gold-tinted bubbles |
| Status label | `.status--ready`, `--working`, `--review`, `--muted` | section 8.4 |
| Card | `.card` | section 8.1 |
| Split | `.split` | stacks at 960px |
| Activity history | `.log`, `li.is-new` | every consequential action adds an entry |
| Capability tiers | `.tiers`, `.tier`, `--dot` | Available now / With approval / Coming next |
| Task workspace | `.ws`, `.ws__pane`, `.ws__label`, `.appr`, `.tasks`, `.bar`, `.chips`, `.assume`, `.draft` | request and approvals left, Gia's progress right |
| Entry animation | `.msg-in` | new messages and log entries |

### 9.2 Added in stage 3 (`css/components.css`, `js/components.js`)

Live examples with real wireframe copy: `docs/components.html` (open it through the local server). Pages that use the interactive components load `js/components.js` after `js/site.js`.

| Component | Classes | Where | Notes |
|---|---|---|---|
| Page hero | `.page-hero`, `--right`, `--center`, `__media`, `__media--placeholder`, `__text`, `__title`, `__tag`, `--focus`, `--hero-fade` | hero of pages 2–4 | full-screen media, text on the side or centered over darkening; section 7.1 |
| Principle | `.principle`, `--center` | GLO 01/03, How GLO Works 02/06 | one short line the page wants remembered; Plex Sans 600 champagne |
| Media frame | `figure.media-frame`, `__box`, `--placeholder`, `__note`, `--ratio` | heroes, final CTAs | placeholder keeps the layout and says what will go there |
| Play-once video | `video[data-play-once]`, `data-delay`, `data-still`, `poster` | hero video of every page | plays once each time the hero comes into view, after a short pause (800 ms), from the first frame to the last, no loop; rewinds when it leaves the screen so it can play again on the next visit; poster = first frame; reduced motion: never plays and shows `data-still` (last frame) |
| Gia core | `.gia-core`, `__photo`, `__plate`, `__name`, `__sub` (`__glow` added by script) | GLO 02, How GLO Works 06 | photo of Gia in a gold ring; name plate over the lower edge; section 8.6 |
| Pulse diagram | `[data-pulse="<name>"]`, `.is-final`; script adds `.pulse-wires`, `.pulse-status`, `.pulse-hl` | GLO 02 (`hub`), How GLO Works 06 (`eco`) | wiring, pulses and card status from `js/components.js`; routes and scenario per diagram via `GiaPulse.define()` (hub in `js/components.js`, eco in the page script); playback rule in section 8.6 |
| Ambient motion | `[data-motion]` → `.is-playing` | available for diagrams with slow motion (How GLO Works hero) | CSS animations inside run only while in view and never under reduced motion |
| Badge | `.badge--now`, `--approval`, `--next`, `--vision`, `--plain` | everywhere a capability or option has a status | Available now / With approval / Coming next / Vision; `--plain` for "Illustrative" |
| Card grid | `.cards--2/3/4`, `.card--flex`, `.card__head`, `.card__example`, `.card__link`, `.card--key` | GLO 04 | badge sits above the title; titles stay aligned when only some cards have a badge |
| Flow | `ol.flow > li.flow__node`, `__title`, `__sub`, `.is-key`, `.is-end`, `.flow--numbered` | GLO 03, GC 06, How GLO Works 03/05 | gold arrows; vertical at 768px; `.is-key` (Gia) is wider and gold |
| Pinned bar | `.flow-keep`, `--change` | under a flow | "Member B keeps their GLO the whole time"; `--change` when ownership changes |
| Cycle return | `.flow-return` with `--n`, `__label` | How GLO Works 03 | bracket from the last node back to the first; a text line on mobile |
| Steps line | `ol.steps-line > li.steps-line__item`, `__label`, `__who`, `.is-you` | GLO 07 | numbered circles on a line; champagne circles for the member's own steps |
| Hub | `.hub[data-pulse="hub"]`, `__side--left/--right`, `__node`, `__name`, `__desc`, `__core.gia-core` | GLO 02 | three nodes per side, Gia in the center, pulse-diagram wiring; at 960px one column: Compute, Models, Tools, then Gia, then Agents, Research, Execution (replaces the wireframe's two compact columns) |
| Accordion | `.accordion > details.acc`, `__sum`, `__icon`, `__body` | GLO 06 | native `details`; the same `name` on a group keeps one item open; open item has a gold border |
| Ownership indicator | `.owner--keep`, `--change`, `--terms` | option cards, accordion, flows | always visible, never only in a tooltip |
| Option card | `.options > article.option`, `__head`, `__name`, `__more`, `.option--conditional` | How GLO Works 04 | Use · Put it to work · Support · Transfer; details open on demand; conditional option has a dashed border |
| Terms sheet | `.terms`, `__head`, `__title`, `__list`, `__row`, `__row--total`, `__note` | GC 02/03/07 | put inside `.glass` when it is Gia's interface; one total per project, always with an "Illustrative" badge |
| Approval sheet | `[data-approval]`, `.approval__list/__item/__check/__label`, `[data-state]`, `__actions`, `__confirm`, `__msg`, `[data-approval-*]` | GC 04 | unreviewed terms show "Not reviewed"; Authorize refuses and names the open term; then an explicit confirmation; decline is a normal outcome; `data-log="#id"` writes to an activity history |
| Is / is not | `.isnot`, `__col--is`, `__col--not` | GLO 08 | check marks for what it is, neutral dashes for what it is not |
| Important information | `aside.notice`, `__title`, `__list` | How GLO Works 07 | calm, readable; not fine print |
| Final CTA | `.final`, `.final__h`, `.uses`, `.final__media`, `.final__img` | every page | moved here from the Meet Gia stylesheet |
| Tabs | `.tabs`, `.tab[role=tab][aria-selected]` | Meet Gia 04, Global Connections 05 | moved here from the Meet Gia stylesheet; arrow keys move between tabs in the page script |
| Card art | `.card__art` > inline `svg` or `img` | section 8.1 lists where | 96px area (72px ≤560px), aligned left, `currentColor` gold, 1.5px stroke defaults on the SVG; a slot with no `svg`/`img` is not displayed |
| Parallax | `[data-parallax]` (optional value: a smaller maximum, e.g. `"0.05"`); script adds `.parallax-on`, `.parallax-media` | `.media-frame__box`, `.final__media`, `.page-hero__media` only | section 10.1; the frame gets `overflow: hidden`; on `.final__media` the border and radius move from the media to the frame, so a parallax `.final__media` holds no caption; one rAF update per scroll/resize, only for frames on screen |
| Staggered entry | `[data-stagger]` on a grid; script adds `.stagger-on`, `.is-in`, `--stagger-i` | card grids | children appear 120ms apart (24px rise, blur 4px, 700ms) on every visit; never on an element that is also `.reveal` |
| Spotlight | `[data-spotlight]` on a card; script adds `.spot-on`, `--spot-x/--spot-y` | marketing cards | 360px radial glow of `--gp-gold` at 14% opacity; uses the card's own `::before`, so only on elements without one (free on `.card`); mouse only |
| Line drawing | `[data-draw]` on a container → `.is-drawn`; inside: SVG `path`/`line`/`polyline`/`polygon`/`circle`/`ellipse`/`rect` (script adds `pathLength="1"` and `.draw-path`; `.no-draw` opts out) and `.draw-x` elements; `--draw-delay` per part | flow arrows, timelines, step lines, cycle return (wired in step 5) | stroke-dashoffset in 1.2s, `.draw-x` scaleX from the left in 1s; not around pulse diagrams or already dashed strokes |
| Shine | `[data-shine]` on `.principle` → `.is-shining` during the pass | gold summary lines | one 1.8s pass of light (band 40% / 50% / 60% of the gradient) each time it comes into view (re-armed after it has left the screen completely), then the plain solid color; the text shadow is off during the pass |

The quiet effects share one IntersectionObserver helper in `js/components.js`. Stagger, line drawing (card art included) and shine play each time their block comes into view and re-arm after it has left the screen completely (section 10.1); parallax keeps following the scroll. Their hiding start states apply only after the script has added its class and only under `prefers-reduced-motion: no-preference`, so without JS or with reduced motion the final state shows; switching the setting applies without a reload.

Utility: `[hidden]` always hides, even on elements that set their own `display`.

### 9.3 Page-only

Anything used on a single page lives in `css/pages/<page>.css`. If a second page needs it, move it to `components.css` instead of copying it.

## 10. Motion

- Text reveal (`.reveal`): 600ms, `translateY(24px)` to 0, opacity 0 to 1, `--ease`, once per element.
- Product UI state changes (`.msg-in`): 450ms, 10px rise.
- Hover feedback: 200–300ms, color, border or glow only; no hover transforms.
- One orchestrated motion moment per page hero. Elsewhere, motion answers the visitor's action (choosing a tab, approving, opening an option) or is one of the quiet effects below. Exception: pulse diagrams `[data-pulse]` play their cycle 3 times when they come into view, then rest on the final state (section 8.6).
- Videos never loop: they use `video[data-play-once]` (9.2), play once per visit to the screen, rest on their last frame and look complete at every frame.
- Quiet effects that play on entry (staggered entry, line drawing with card art, shine) follow the same per-visit rule: they play each time their block comes into view and rest on the final state; only after the block has left the screen completely (not a pixel visible) do they quietly return to the start state, ready for the next visit. While any part stays visible they never restart. The text reveal stays once per element.
- No scroll hijacking beyond the approved Meet Gia hero.
- Do not animate layout dimensions that push surrounding content.

### 10.1 Quiet effects

Effects inspired by React Bits are ported to vanilla JS and CSS in `js/components.js` and `css/components.css`. No React, no build step, no new dependencies.

- **Parallax** (`[data-parallax]`): only on photos and videos inside `.media-frame`, `.final__media` and `.page-hero__media`. The media is scaled up to `scale(1.18)` and moves vertically by at most ±8% of the frame height (±4% at 768px and below); the scale leaves 9% on each side, so the frame's edges never show. Only `transform` is animated, through `requestAnimationFrame`, and only while the frame is on screen. Never on: the Meet Gia hero (scroll-scrubbed canvas), Gia's photo in `.gia-core`, card art (`.card__art`), glass panels of the product UI.
- **Staggered card entry**: cards in a grid appear one after another, 120ms apart: `translateY(24px)` to 0, opacity 0 to 1, `blur(4px)` to 0, 700ms, `--ease`; plays on every visit and re-arms after the grid has left the screen completely.
- **Spotlight on hover**: a soft gold radial glow (360px, `--gp-gold` at 14% opacity) follows the pointer inside a card, with no transform. Marketing cards only, and only on devices with a mouse (`@media (hover: hover)`).
- **Line drawing**: flow arrows, timelines, vertical step lines and the cycle return draw each time they come into view (`stroke-dashoffset` or `scaleX`), in 1.2s or less, and re-arm after leaving the screen completely. Every SVG shape is drawn (path, line, polyline, polygon, circle, ellipse, rect). Card art (`.card__art`, 8.1) draws itself the same way without an attribute: each time its card comes into view, parts about 0.1s apart, after the card's own staggered entry when it has one.
- **Shine**: one pass of light (1.8s) across the gold summary lines (`.principle`) each time they come into view; it re-arms only after the line has left the screen completely.

### 10.2 Reduced motion

Under `prefers-reduced-motion: reduce`: no reveal, no entry animation, no transitions, videos do not play, no parallax, no staggered entry, no spotlight, no line drawing, no shine; every element shows its complete final state at once.

## 11. Responsive system

| Range | Rules |
|---|---|
| ≥1200px | container 1200px, page padding 48px, section padding 160px, two-column gap 64–96px |
| 1101–1199px | full desktop header; layouts as desktop with fluid padding |
| ≤1100px | **shell breakpoint**: header navigation collapses into the hamburger menu; 4-column card grids become 2 columns |
| ≤960px | splits, workspaces, control grids and final CTA stack to one column with a 56px gap |
| ≤768px | page padding 24px, section padding 72–96px, header 64px, hero buttons stack full width, footer switches to the stacked logo |
| ≤480px | page padding 20px, H2 never below 30px, nothing overflows the viewport |

- Follow the reading order of the wireframe when stacking: text first, then media, unless a section says otherwise.
- Horizontal card scrollers on mobile show part of the next card (`flex: 0 0 82%`) and bleed to the viewport edge.
- Never compress a text column below about 360px; stack instead.

## 12. Brand and logo

### 12.1 Assets

All logo files are in `assets/logo/`. Originals as supplied are in `assets/source/logo/`.

| File | What it is | Where it is used |
|---|---|---|
| `glonari-mark.webp` / `.png` (192 × 192) | the globe "G" mark, cut from the horizontal lockup | header brand, favicons |
| `glonari-lockup-horizontal.webp` / `.png` (840 × 222) | mark, divider, GLONARI wordmark, "Experience more." | footer above 768px |
| `glonari-lockup-stacked.webp` / `.png` (760 × 359) | mark above wordmark, "Experience more" | footer at 768px and below; large brand moments |
| `favicon-32.png`, `favicon-180.png` | the mark at favicon sizes | `<link rel="icon">`, `apple-touch-icon` |

All logo files have transparent backgrounds and are rendered gold on dark. The globe interior is transparent, so the logo works only on dark surfaces (`--gp-black`, `--gp-bg`, `--gp-surface`). On a light background the globe reads as an empty cloud; do not use it there.

### 12.2 Sizes

| Asset | Minimum | Standard |
|---|---|---|
| Mark | 24px | 32px in the header |
| Horizontal lockup | 240px wide | 320px in the footer; at most 420px |
| Stacked lockup | 200px wide | 240px in the mobile footer; at most 380px |

The tagline becomes illegible below the minimum widths; use the mark alone instead.

### 12.3 Clear space and placement

- Keep clear space around any lockup of at least one quarter of the mark's height on every side.
- Never place the logo over photography or video; put it on a flat dark surface.
- Display the logo lockups from the image files only; never recolor them, add shadows or glows, stretch or rotate them. The one approved live-text wordmark is the header brand (12.4); do not set GLONARI as text anywhere else.

### 12.4 Header brand

The header brand is the mark (36px; 32px ≤480px) followed by the live-text wordmark **GLONARI**: Playfair Display 700, 24px (21px ≤480px), uppercase, letter spacing 0.02em, color `--gp-gold-mid`, 12px gap. It follows the approved reference lockup (round mark plus serif uppercase wordmark in bronze-gold). This is the only place GLONARI is set as text; elsewhere use the image lockups. The full lockup image is not used in the header because its tagline is unreadable at header height. In the markup the word is written "Glonari" and uppercased by CSS so screen readers pronounce it correctly; the link is labeled "Glonari, Meet Gia" (on Meet Gia, "Glonari, back to top").

### 12.5 To confirm with the brand team

The two supplied lockups differ: the horizontal one reads "Experience more." with a period, the stacked one "Experience more" without. Use them as supplied until the brand team chooses one.

## 13. Site shell

The shell is the same on every page. Styles: `css/shell.css`. Behavior: `js/site.js`.

### 13.1 Header

- `position: fixed`, solid `--gp-black` background, 1px `--gp-glass-border` bottom hairline, no blur, no shadow. Total height is `--header-h`; use that token for anything that must clear the header (scroll padding, sticky offsets, hero top padding).
- **Level 1, site navigation** (`--header-row`, 72px): the brand (mark plus GLONARI wordmark, 12.4), the four pages in sequence order — Meet Gia · Introducing GLO · Global Connections · How GLO Works — then "Join the waitlist" (`.btn--primary.btn--sm`). Page links are 15px IBM Plex Sans 500 in `--gp-text-2`; the current page has `aria-current="page"`, gold text and a 2px gold bar on the bottom edge of the row.
- **Level 2, in-page navigation** (`--subnav-h`, 44px): one row with the current page's sections, separated from level 1 by a 1px `--gp-line` rule and left-aligned with the brand. Links are 13px in `--gp-text-muted`; the active section has `aria-current="true"` and gold text. If the row is wider than the window it scrolls sideways (no scrollbar) and keeps the active item in view.
- The active section is the section crossing a line at 45% of the viewport height. The hero and final CTA are not in the list; while they are in view nothing is marked (on Meet Gia the hero is "What is Gia"). A section can hand its highlight to another item with `data-nav="id"`.
- The 2px gold scroll-progress bar sits on the bottom edge of the header.
- The "Join the waitlist" button links to `#join` on Meet Gia and to `index.html#join` on the other pages.
- On Meet Gia, the header overlays the scroll-video hero without changing its geometry.
- Section lists and their anchor ids (defined in `tools/build-shell.py`):

| Page | Sections (id) |
|---|---|
| Meet Gia | What is Gia (`what`) · How it works (`how`) · How people use Gia (`people`) · In action (`in-action`) · Memory (`memory`) · Control (`control`) · Work (`work`) · More power (`more-power`) |
| Introducing GLO | Why capacity (`why-capacity`) · What GLO is (`what-glo-is`) · What it enables (`what-it-enables`) · How it works (`how-it-works`) · Your options (`your-options`) · Global Connections (`global-connections`) · Limits (`limits`) |
| Global Connections | How work starts (`work-starts`) · Gia finds projects (`gia-finds`) · Review & authorize (`authorize`) · Gia works (`gia-works`) · Deliverable (`deliverable`) · Compensation (`compensation`) · Project end (`project-end`) |
| How GLO Works | Three-layer model (`three-layer`) · Reusable capacity (`reusable-capacity`) · Your options (`your-options`) · Global Connections vs market (`gc-vs-market`) · Ecosystem (`ecosystem`) · Important information (`important-info`) |

The hero of pages 2–4 uses the id `intro`; the final CTA uses `final` (Meet Gia keeps `join`, the waitlist target).

### 13.2 Mobile menu (≤1100px)

- At 1100px and below both navigation rows and the header button are replaced by a 44px hamburger button; the header is one 72px row (64px ≤768px). The scroll-progress bar stays.
- The menu opens below the header on a solid `--gp-black` surface and scrolls on its own if it is taller than the screen. It lists the four pages (18px); under the current page, its sections (15px, `--gp-text-2`) are indented behind a 1px `--gp-gold-dark` rule. A full-width "Join the waitlist" button ends the menu.
- The button turns into a close icon while the menu is open. Choosing a link, pressing Escape (focus returns to the button) or widening the window past 1100px closes it. No open/close animation.

### 13.3 Footer

- Solid `--gp-black`, 1px `--gp-glass-border` top hairline, padding 72px top and 40px bottom (56/32px ≤768px).
- Top row, a grid of the brand block (1.6fr) plus one 1fr column per link column (`--footer-cols`, set by the build script): the Glonari horizontal lockup (stacked at ≤768px) with one line "Gia is your personal AI agent by Glonari."; "The site" — the four pages, current page in gold; "Membership" — Join the waitlist, Learn about membership; "Legal" — Privacy, Terms. Column headings are 13px IBM Plex Sans 600, links 15px `--gp-text-2`, gold on hover.
- Links whose page is not built yet are not shown (no dead links, no service notes): Learn about membership, Privacy and Terms are switched on in `tools/build-shell.py` (MEMBERSHIP_PAGE, PRIVACY_PAGE, TERMS_PAGE). A column with no links is left out. Privacy and Terms must exist before the waitlist form sends data.
- Below a 1px `--gp-line` rule: the important-information paragraph (caption size, max 880px wide) built only from statements approved in the wireframes.
- Last line: «© 2026 Glonari.» in IBM Plex Mono.
- At ≤960px the brand block spans the full width above the link columns; at ≤560px the links form two columns.

### 13.4 One source for the shell markup

The header, mobile menu and footer are identical on every page except for the marks of the current page and its section list. The site has no build step, so this markup is written into each HTML file between `<!-- shell:header -->` / `<!-- /shell:header -->` and `<!-- shell:footer -->` / `<!-- /shell:footer -->` by `tools/build-shell.py`. Change the shell only in that script (page list, section lists, footer links and wording), then run `python3 tools/build-shell.py`. Never edit the markup between the markers by hand.

## 14. Multi-page structure

### 14.1 Files

```
index.html                    Meet Gia
glo.html                      Introducing GLO
global-connections.html       Global Connections
how-glo-works.html            How GLO Works

css/tokens.css                tokens (section 3)
css/base.css                  reset, type, sections, buttons, reveal
css/components.css            shared components (section 9)
docs/components.html          live reference of every shared component
css/shell.css                 header, mobile menu, progress, footer, logo
css/pages/<page>.css          page-only sections

js/site.js                    shell behavior; exposes window.GiaSite = { reduce, clamp, lerp }
js/components.js              shared component behavior (approval sheet, play-once video, ambient motion, quiet effects, pulse diagrams)
js/pages/<page>.js            page behavior
js/pages/meet-gia-frames.js   Meet Gia hero frame list

tools/build-shell.py          writes header, mobile menu and footer into all four pages (13.4)
```

Page slugs: `meet-gia`, `glo`, `global-connections`, `how-glo-works`. Each page sets `<body class="no-js" data-page="<slug>">`.

### 14.2 Loading order

Stylesheets: `tokens.css`, `base.css`, `components.css`, `shell.css`, then the page file. Scripts at the end of `body`: `site.js`, then `components.js` (pages 2–4, and any page using interactive components), then the page's own scripts. A page never loads another page's CSS or JS.

### 14.3 Page sequence

Calls to action move the visitor forward: Meet Gia → Introducing GLO → Global Connections → How GLO Works. A CTA never skips a page or points back to the page before it; the header is the way back.

The shell navigation (header, mobile menu, footer) always lists all four pages. While a page is still being built it shows placeholder sections with their final ids and headings.

Calls to action inside page content use their final destinations from the wireframe, even when the target page is still in progress during the draft; the target then shows its placeholder sections. Before launch every CTA target must be built. A destination that is not built yet (for example "Learn about membership") is hidden with the `hidden` attribute on the final link until the page exists, never shown as an inactive button, a link to `#` or a link to an unrelated page. The site shows no service notes for the team; open items are recorded in README.md.

## 15. Cross-page content rules

These come from the wireframes and apply to every page:

- **Hierarchy**: Gia is the intelligence; GLO is capacity and access. "GLO isn't the intelligence. Gia is."
- **One options model**: Use, Put it to work, Support, Transfer — these names, this order, on every page. Reuse after a project is a property of the options, not a fifth option.
- **Two mechanisms, never mixed**: in Global Connections the work moves and the member keeps their GLO; in a secondary-market transfer the GLO moves and ownership changes. Never show compensation and market price in the same component.
- **Compensation**: only on the Global Connections page, only as one illustrative total for one defined project, labeled "Illustrative". No rate per GLO, percentages, annual figures, payout frequency or GLO's offering price anywhere.
- **No investment framing**: no promises of income, yield, appreciation, liquidity, resale or project availability.
- **Member's role**: show the member reviewing, authorizing and taking part; never sell participation as doing nothing.
- **Status labels**: every capability shows Available now, With approval, Coming next or Vision.
- **Trademarks**: GLO™, Glonari Life Optimizers™, Global Connections®, Human Intelligence™ — mark the first prominent use on a page.

## 16. Implementation rules

1. Reuse tokens and shared classes; do not repeat spacing or color values per section.
2. Use `clamp()` for fluid type and major spacing.
3. Lay out with Grid or Flexbox; absolute positioning only for overlays, decorative layers and animation internals.
4. `box-sizing: border-box` globally; `min-width: 0` on grid and flex children.
5. No fixed heights on content sections.
6. Page scripts check that their elements exist before using them; a missing element must never throw.
7. Interactive product UI uses real buttons, native `details`/`summary` for accordions and correct ARIA for tabs, with visible keyboard focus (2px gold outline).
8. Calls to action use their final destinations; a CTA whose page is not built yet stays `hidden` (14.3).
9. Change only the files the current task needs; never change an approved page as a side effect.
10. All repository content (copy, comments, docs) is in English.

## 17. Visual QA checklist

Before reporting a page or section complete:

- Section padding, heading spacing and component spacing follow sections 4.4 and 6.
- Text aligns to the container; no paragraph wider than 560px unless it sits in a 720px centered block.
- Fonts follow 4.1: Playfair only in the hero headline, final CTA headline and the Gia name.
- Colors come from tokens; data colors appear only in status and data.
- Gia is visually larger than GLO in every diagram.
- No content is clipped and nothing scrolls sideways at 1440, 1024, 768 and 375px.
- Header and mobile menu work at 1101px and 1100px; the current page and section are marked.
- Reduced-motion mode shows complete static compositions: parallax, staggered entry, spotlight, line drawing and shine are all off (10.2).
- An empty or missing `.card__art` leaves no gap above the badge or title.
- Keyboard: every control is reachable, focus is visible, Escape closes the menu.
- Content rules in section 15 hold.
- Other pages are unchanged; the browser console has no errors.

## 18. Instruction for future tasks

Start every implementation prompt with:

> Read `docs/GIA-SITE-DESIGN-SYSTEM.md` and `docs/GLONARI_PULSE_COLORS.md`, and the wireframe for the page being changed, before changing files. The wireframe controls copy, section order, terminology and functionality. The color file controls color. The design system controls everything else visual and structural. Do not change approved pages or sections unless this prompt explicitly authorizes it.

Then specify one page, one section or one bounded system task.
