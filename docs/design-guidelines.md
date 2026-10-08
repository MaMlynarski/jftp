# Sygnity Design Guidelines

This reference records the visible design of the Sygnity homepage as inspected on 2026-10-07. It is a point-in-time reference for visual alignment, not a claim that Sygnity's brand assets are licensed for reuse.

## Assets

Paths in this table are relative to `docs/`.

| Asset | File | Notes |
|---|---|---|
| Homepage screenshot | [../assets/homepage.png](../assets/homepage.png) | Full-page capture after closing the cookie notice. |
| Sygnity wordmark | [../assets/logo.svg](../assets/logo.svg) | SVG fetched from the visible header logo URL. Verify usage and redistribution rights before use. |
| Favicon | [../assets/favicon.png](../assets/favicon.png) | Fetched from the page's declared favicon URL. Verify usage rights before reuse. |
| Design tokens | [../assets/design-tokens.json](../assets/design-tokens.json) | Machine-readable colors, type, spacing, and component values. |

## Colors

| Token | Value | Observed use |
|---|---|---|
| Brand primary | `#00AEEF` | Filled calls to action, selected accents, and section details. |
| Wordmark blue | `#009DDE` | Fill used in the downloaded SVG wordmark. |
| Link blue | `#1E73BE` | Default link color in the rendered page. |
| Text primary | `#3A3A3A` | Body copy. |
| Text secondary | `#666666` | Form field text and secondary copy. |
| Text muted | `#69727D` | Muted supporting labels observed on the page. |
| Light background | `#F9F9F9` | Alternating section background. |
| Field border | `#CCCCCC` | Contact form input and textarea borders. |
| Overlay | `rgba(0, 0, 0, 0.3)` | Carousel controls. |

The hero combines dark blue imagery with white text at 80% opacity. Its background is image-driven, so no single hero background color is specified as a token. Error and success colors were not visible in the captured page and are intentionally unspecified.

## Typography

The browser reported `Montserrat, sans-serif` for body text, controls, and headings. The observed body size is 16px with a 24px line height. The hero heading is 32px, weight 500, with a 38.4px line height. Primary calls to action use 14px text at weight 400. The section and widget headings vary by context; inspect the reference screenshot before choosing a size.

| Role | Size | Weight | Evidence |
|---|---:|---:|---|
| Body | 16px | 400 | Computed body style. |
| Button | 14px | 400 | Computed visible `Czytaj więcej` action. |
| Hero heading | 32px | 500 | Computed visible carousel heading. |
| Widget heading | 14px | 500 | Computed `Kurs akcji` heading. |

No local Montserrat text font was saved. The browser exposed self-hosted icon fonts as well, but they were temporary extraction results and are not part of this design system. If implementing this look, use an appropriately licensed Montserrat source or an approved fallback; do not copy font files from the site without checking their license.

## Spacing

The rendered contact form uses `10px 15px` field padding. The primary action uses `8px 12px`; another observed content action uses `6px 12px`. The spacing values in the token file provide a practical 4px-based scale for new layouts, but page gutters and section gaps vary with the responsive layout and should be checked against the screenshot.

## Border radius

The contact form fields use a 3px radius. Primary action links use a 3px radius; another content action uses 2px. Cards and carousel indicators include larger or circular shapes, with 5px and 50% radii observed in the page styles. Use small radii for controls and reserve circular shapes for indicators or icon controls.

## Components

### Header and navigation

The desktop header is white, approximately 101px high in the captured viewport, and places the blue wordmark at the left with compact gray navigation, language links, market information, and social links across the row. Keep the header visually light and avoid adding heavy borders or shadows unless the reference changes.

### Buttons

Primary actions use a bright cyan blue fill (`#00AEEF`), white 14px text, `8px 12px` padding, and a 3px radius. On the hero, the action sits over a dark image; maintain enough contrast for the label to remain legible.

### Inputs and textareas

The contact form uses white fields, 16px Montserrat text, `10px 15px` padding, a 1px `#CCCCCC` border, and a 3px radius. Keep labels small and muted above each field. The textarea is substantially taller than a single-line input.

### Content sections and cards

The homepage alternates white and very light gray sections, uses generous vertical whitespace, and separates some section titles with a short centered rule. News cards use a light surface, restrained shadows, image-led content, and cyan links or actions. Carousel imagery carries most of the visual weight in the hero.

## Logo usage

Use the supplied SVG only where reuse is permitted. It contains the blue wordmark (`#009DDE`) and should sit on a light, uncluttered surface. The inspected page did not expose an inverted logo variant; do not recolor the mark or invent a dark-background variant without an approved asset. Confirm logo and favicon rights before distributing them.

## Visual style summary

The page presents a restrained corporate technology identity built around white space, Montserrat typography, and a bright cyan accent. Dark, image-led hero content introduces the brand, while the rest of the page uses alternating light sections and compact gray copy. Controls have modest corner rounding and avoid decorative effects beyond subtle card shadows. Partner and customer imagery adds color without changing the consistent blue-and-neutral interface palette.

## Capture notes

- Source: <https://www.sygnity.pl/>
- Inspected: 2026-10-07 using a rendered desktop page at a 1280px viewport width.
- The delayed cookie notice was closed using its close button; no consent choice was made.
- The screenshot was visually checked after capture and contains no cookie notice or other overlay.
- Computed styles were captured from visible page elements. Values described as a practical scale or visual observation are inferred from the rendered layout, not explicit brand specifications.
