# Glonari Pulse — Website Color System

> **For Claude Code.** This file is the single source of truth for color on the glonaripulse.com marketing website. Use the tokens in section 10 for all color values. Do not introduce new colors without a clear reason, and never hard-code a hex value in a component when a token exists.

Sources: the website strategy ("Visual Design System" section), the Gia Power brochure, and four UI mockups (Pulse Connect, Gia Power, Daily Briefing, Life Capacity). Values marked **measured** were sampled from those images. Values marked **proposed** fill roles the source materials do not cover.

---

## 1. Rules from the strategy (non-negotiable)

1. **Base:** near-black / charcoal environment. The site is dark-only. Do not build a light theme.
2. **Primary accent:** warm metallic Glonari gold.
3. **Gold always means Glonari, Gia, Power, and primary actions** (Meet Gia, Ask Gia, Connect, Increase My Power). Nothing else is gold-filled.
4. **Blue, green and violet are used sparingly and only to distinguish information types** (data, charts, category labels). Never on buttons or navigation.
5. **Materials:** smoked glass, dark translucent panels, fine gold borders, soft reflections, warm environmental lighting, subtle depth.
6. **Never look like a crypto exchange or a game.** No neon, no red/green trading colors, no full-screen saturated gradients, no token-price styling.

---

## 2. Reconciling the two golds

The source materials use two different golds:

| | Brochure (PDF) | App mockups (PNG) |
|---|---|---|
| Character | copper / champagne / bronze; restrained, private-banking | saturated amber gold with glow |
| Key values | `#C78D61`, `#EBC99E` | `#FAB95A`, `#F1A74D`, `#C58E42` |
| Background | pure black `#000000` | warm charcoal `#0F0F0E` with photography and light |

**Resolution — apply this consistently:**

- **Amber gold** (`--gp-gold*`) → actions, key numbers, icons, active states, glow.
- **Champagne & copper** (`--gp-champagne`, `--gp-copper`) → editorial typography: large serif headlines, uppercase eyebrow labels, pull quotes, page numbers.

---

## 3. Background & surfaces

| Token | HEX | Use | Source |
|---|---|---|---|
| `--gp-black` | `#050402` | deepest areas, final "Meet Your Gia" screen | measured |
| `--gp-bg` | `#0F0F0E` | page background | measured |
| `--gp-surface` | `#171514` | cards, panels, blocks | measured |
| `--gp-surface-2` | `#1D1712` | raised cards, diagram circles | brochure |
| `--gp-warm-dark` | `#251D16` | under-layers for gold, warm shadows | measured |
| `--gp-line` | `#3F2A1D` | dividers, borders of inactive elements | brochure |

**Glass panels** (the default panel style, as in the mockups):

```css
.glass {
  background: var(--gp-glass);                 /* rgba(20,17,14,0.62) */
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border: 1px solid var(--gp-glass-border);    /* gold at 22% */
  border-radius: 16px;
}
.glass.is-active { border-color: var(--gp-glass-border-active); } /* gold at 55% */
```

Provide a solid fallback (`--gp-surface`) where `backdrop-filter` is unsupported.

---

## 4. Glonari gold (primary accent)

| Token | HEX | Use | Source |
|---|---|---|---|
| `--gp-gold-glow` | `#FAB95A` | primary button fill (top), big numbers, highlights | measured |
| `--gp-gold` | `#F2B35A` | **core brand color**: icons, active nav item, outline buttons, links | measured (averaged) |
| `--gp-gold-warm` | `#F1A74D` | button gradient middle, glow falloff | measured |
| `--gp-gold-mid` | `#C58E42` | secondary gold elements, outlines | measured |
| `--gp-gold-deep` | `#966B32` | button shadow, gradient bottom; **decorative only** (see contrast) | measured |
| `--gp-gold-dark` | `#604119` | active tab background, dimmed gold | measured |
| `--gp-champagne` | `#EBC99E` | large serif headlines ("Possibilities.", "Your Life. Powered by Gia.") | brochure |
| `--gp-copper` | `#C78D61` | uppercase eyebrow labels ("PULSE CONNECT", "INTRODUCING GIA POWER™") | brochure |

**Primary button** (Meet Gia, Connect, Increase My Power):

```css
.btn-primary {
  background: var(--gp-btn-gradient);
  color: var(--gp-on-gold);
  box-shadow: 0 6px 20px rgba(150, 107, 50, 0.35);
}
.btn-primary:hover { box-shadow: var(--gp-power-glow); }
```

**Secondary button** (Ask Gia Why, Read Full Article, Explore Glonari Pulse): transparent background, `1px solid var(--gp-gold)`, text `var(--gp-gold)` or `var(--gp-text)`.

**Power motif.** The strategy asks for a visual shift into an "illuminated Power motif" when the Gia Power section appears. Use the same gold, add glow (`--gp-power-glow`) and thin glowing network lines. Do not introduce a new color for Power.

---

## 5. Text

| Token | HEX | Use |
|---|---|---|
| `--gp-text` | `#F6F0E7` | headings and body text (warm off-white from the brochure) |
| `--gp-white` | `#FFFFFF` | only very large numbers and hero headings |
| `--gp-text-2` | `#C7C0B6` | descriptions, subtitles |
| `--gp-text-muted` | `#8A847B` | timestamps ("2h ago"), footnotes, compliance/disclaimer copy (proposed) |
| `--gp-on-gold` | `#1A1206` | text on gold buttons |

Do not use pure white for long body text on the dark background.

---

## 6. Data colors (information types only)

Use **only inside data**: charts, metric icons, category labels, progress indicators. Never on buttons, links, or navigation.

| Token | HEX | Meaning | Seen in mockups |
|---|---|---|---|
| `--gp-green` | `#2EDB8C` | saved, covered, growth, online status | "Money Saved $1,240", "84% Covered" bar, "↑28%" |
| `--gp-blue` | `#2F8CF0` | earned, data, Global Economy category | "Value Earned $602", blue chart bars |
| `--gp-teal` | `#1EC8E0` | transition color in chart gradients | "Gia Power Results" bars |
| `--gp-violet` | `#A35CE0` | time, AI & Technology / Travel categories | "Time Saved 14.6 hrs", clock icon |
| `--gp-warning` | `#C3734E` | soft warning, used rarely (proposed) | — |

These are slightly desaturated versions of the measured values (`#1EE28D`, `#0487E3`, `#00B4D6`, `#9B34CC`) so they do not compete with gold.

**Fix from the mockups:** the online-status dot in the Pulse Connect mockup is neon green (`#01ED02`). Use `--gp-green` instead.

**No red.** Do not use red for negative values. If a warning state is truly needed, use `--gp-warning`.

---

## 7. Gradients

**Life Capacity ring (84%)** — the hero visual of the Life Capacity section:

```css
.capacity-ring { background: var(--gp-capacity-ring); }
/* conic-gradient(#2F8CF0, #1EC8E0, #2EDB8C, #F2B35A) */
```

Animate the fill from 62% to 84% when the section enters the viewport (per the strategy's motion notes).

**Covered / out-of-pocket bar:** covered part `#2EDB8C → #08E698`, out-of-pocket part `#FDBF57`.

**Stacked chart bars:** bottom-to-top blue `--gp-blue` → green `--gp-green` → gold `--gp-gold` (as in "Value Over Time").

**Section atmosphere:** warm sunset glow over the page background:

```css
.section-glow {
  background:
    radial-gradient(ellipse at 70% 0%, rgba(241, 167, 77, 0.18), transparent 60%),
    var(--gp-bg);
}
```

---

## 8. Don'ts

- Don't use gold for secondary or informational elements; gold must keep meaning "Glonari / primary action".
- Don't color buttons blue, green, or violet.
- Don't use red/green "trading" semantics, price tickers, or candlestick styling anywhere, including the G-Power and Global Reserve sections.
- Don't build a light theme.
- Don't use pure `#FFFFFF` for long text.
- Don't use `--gp-gold-deep` (`#966B32`) or darker for small text.

---

## 9. Contrast (WCAG)

Measured against `--gp-bg` (`#0F0F0E`). Target ≥ 4.5 for body text, ≥ 3 for large text.

| Color | Ratio | Allowed for |
|---|---|---|
| `#F6F0E7` text | 16.9 | all text |
| `#C7C0B6` text-2 | 10.6 | all text |
| `#8A847B` text-muted | 5.2 | small text |
| `#F2B35A` gold | 10.4 | all text |
| `#C58E42` gold-mid | 6.7 | all text |
| `#966B32` gold-deep | 4.1 | **large text / decoration only** |
| `#2EDB8C` green | 10.6 | all text |
| `#2F8CF0` blue | 5.6 | all text |
| `#A35CE0` violet | 4.7 | prefer icons and large numbers |
| `#1A1206` on gold button | 10.0 | button labels |

---

## 10. Tokens

```css
:root {
  color-scheme: dark;

  /* Background & surfaces */
  --gp-black:               #050402;
  --gp-bg:                  #0F0F0E;
  --gp-surface:             #171514;
  --gp-surface-2:           #1D1712;
  --gp-warm-dark:           #251D16;
  --gp-line:                #3F2A1D;
  --gp-glass:               rgba(20, 17, 14, 0.62);
  --gp-glass-border:        rgba(242, 179, 90, 0.22);
  --gp-glass-border-active: rgba(242, 179, 90, 0.55);

  /* Glonari gold */
  --gp-gold-glow:   #FAB95A;
  --gp-gold:        #F2B35A;
  --gp-gold-warm:   #F1A74D;
  --gp-gold-mid:    #C58E42;
  --gp-gold-deep:   #966B32;
  --gp-gold-dark:   #604119;
  --gp-champagne:   #EBC99E;
  --gp-copper:      #C78D61;

  /* Text */
  --gp-text:        #F6F0E7;
  --gp-white:       #FFFFFF;
  --gp-text-2:      #C7C0B6;
  --gp-text-muted:  #8A847B;
  --gp-on-gold:     #1A1206;

  /* Data colors */
  --gp-green:       #2EDB8C;
  --gp-blue:        #2F8CF0;
  --gp-teal:        #1EC8E0;
  --gp-violet:      #A35CE0;
  --gp-warning:     #C3734E;

  /* Gradients & effects */
  --gp-btn-gradient:  linear-gradient(180deg, #FAB95A 0%, #F1A74D 55%, #C58E42 100%);
  --gp-capacity-ring: conic-gradient(#2F8CF0, #1EC8E0, #2EDB8C, #F2B35A);
  --gp-power-glow:    0 0 40px rgba(250, 185, 90, 0.35);
}
```

### Tailwind (if the project uses Tailwind)

```js
// tailwind.config.js → theme.extend.colors
gp: {
  black: '#050402', bg: '#0F0F0E', surface: '#171514', 'surface-2': '#1D1712',
  'warm-dark': '#251D16', line: '#3F2A1D',
  'gold-glow': '#FAB95A', gold: '#F2B35A', 'gold-warm': '#F1A74D',
  'gold-mid': '#C58E42', 'gold-deep': '#966B32', 'gold-dark': '#604119',
  champagne: '#EBC99E', copper: '#C78D61',
  text: '#F6F0E7', 'text-2': '#C7C0B6', 'text-muted': '#8A847B', 'on-gold': '#1A1206',
  green: '#2EDB8C', blue: '#2F8CF0', teal: '#1EC8E0', violet: '#A35CE0', warning: '#C3734E',
}
```

---

## Summary

Charcoal-black background. Warm gold as the only voice of the brand and of primary actions. Champagne and copper for editorial typography. Three quiet data colors (green, blue, violet) used only for numbers and charts.
