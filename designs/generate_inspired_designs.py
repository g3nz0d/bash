from __future__ import annotations

import math
import os
from dataclasses import dataclass


WIDTH = 1024
HEIGHT = 576
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "generated")


@dataclass(frozen=True)
class Design:
    slug: str
    quote: str
    accent: str
    text: str
    hair_left: str
    hair_right: str
    top_left: tuple[int, int]
    top_right: tuple[int, int]
    pants_left: str
    top_left_clothing: str
    pants_right: str


DESIGNS = [
    Design(
        slug="design-01-firewall-smile",
        quote="His firewall looked strong\nuntil she logged in with a smile.",
        accent="#A5792B",
        text="#855A16",
        hair_left="#5E412D",
        hair_right="#6B4338",
        top_left=(245, 190, 95),
        top_right=(225, 182, 74),
        pants_left="#BBD2D4",
        top_left_clothing="#F2EFE8",
        pants_right="#F1C4B3",
    ),
    Design(
        slug="design-02-password-policy",
        quote="Their connection is stronger\nthan his password policy.",
        accent="#AF8740",
        text="#8A5D18",
        hair_left="#4C3224",
        hair_right="#543327",
        top_left=(221, 181, 151),
        top_right=(131, 92, 104),
        pants_left="#D9C9B8",
        top_left_clothing="#E8F0EE",
        pants_right="#E8B39B",
    ),
    Design(
        slug="design-03-encryption",
        quote="Even his encryption could not hide\nthat he fell first.",
        accent="#A88E52",
        text="#785623",
        hair_left="#553A2A",
        hair_right="#3F2C24",
        top_left=(198, 206, 214),
        top_right=(177, 142, 102),
        pants_left="#BFD9D0",
        top_left_clothing="#F4F3EC",
        pants_right="#E5C3B2",
    ),
    Design(
        slug="design-04-guard-down",
        quote="She did not break his guard.\nHe set it down for her.",
        accent="#AC8042",
        text="#7B5120",
        hair_left="#634230",
        hair_right="#4D3025",
        top_left=(236, 204, 112),
        top_right=(104, 77, 98),
        pants_left="#C5D7DA",
        top_left_clothing="#F1EDE4",
        pants_right="#F0C0A9",
    ),
    Design(
        slug="design-05-latency-heart",
        quote="No lag, no latency -\nher heart synced with his instantly.",
        accent="#B18A47",
        text="#7A5419",
        hair_left="#5B382B",
        hair_right="#563428",
        top_left=(230, 192, 134),
        top_right=(158, 111, 121),
        pants_left="#C1D4CF",
        top_left_clothing="#EFF2E8",
        pants_right="#F1C7B8",
    ),
]


def svg_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def draw_corner(x: int, y: int, accent: str, flip_x: bool = False, flip_y: bool = False) -> str:
    sx = -1 if flip_x else 1
    sy = -1 if flip_y else 1
    tx = x + (180 if flip_x else 0)
    ty = y + (180 if flip_y else 0)
    return f"""
    <g transform="translate({tx} {ty}) scale({sx} {sy})" stroke="{accent}" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M22 114 C18 83, 22 53, 38 29" stroke-width="3.2" opacity="0.85"/>
      <path d="M23 24 L48 24 L48 49 L23 49 Z" stroke-width="3"/>
      <path d="M31 31 L39 24 L48 32" stroke-width="2.2" opacity="0.9"/>
      <path d="M24 39 L31 48 L24 56" stroke-width="2.2" opacity="0.9"/>
      <path d="M39 49 L48 56 L40 64" stroke-width="2.2" opacity="0.9"/>
      <path d="M48 24 C69 18, 94 20, 109 31 C121 39, 129 52, 131 67" stroke-width="3.1"/>
      <path d="M64 23 C72 39, 68 57, 51 61 C38 64, 27 53, 29 40 C31 25, 48 18, 60 28" stroke-width="2.7" opacity="0.95"/>
      <path d="M73 41 C85 24, 108 25, 119 41 C128 55, 121 74, 104 77 C87 79, 73 66, 77 51" stroke-width="2.7" opacity="0.95"/>
      <path d="M97 28 C118 21, 143 24, 161 38" stroke-width="3" opacity="0.9"/>
      <path d="M117 41 C126 33, 142 32, 151 40 C160 49, 160 64, 149 72 C138 80, 122 77, 115 66 C109 57, 110 47, 117 41" stroke-width="2.6"/>
      <path d="M138 33 C154 28, 168 29, 177 36" stroke-width="2.8" opacity="0.8"/>
    </g>
    """


def draw_side_motif(x: int, y: int, accent: str) -> str:
    return f"""
    <g transform="translate({x} {y})" fill="none" stroke="{accent}" stroke-width="2.2" stroke-linejoin="round" opacity="0.78">
      <path d="M0 26 L14 0 L28 26 L14 52 Z"/>
      <path d="M8 26 L14 14 L20 26 L14 38 Z"/>
      <path d="M14 0 L28 13 L14 26 L0 13 Z" opacity="0.8"/>
    </g>
    """


def draw_mug(x: float, y: float, fill: str, accent: str, rotate: float = 0) -> str:
    return f"""
    <g transform="translate({x} {y}) rotate({rotate})">
      <rect x="-10" y="-14" width="20" height="18" rx="3" fill="{fill}" stroke="{accent}" stroke-width="2"/>
      <path d="M10 -10 C18 -10, 18 0, 10 0" fill="none" stroke="{accent}" stroke-width="2"/>
      <path d="M-4 -18 C-7 -24, -3 -28, -1 -32" fill="none" stroke="{accent}" stroke-width="1.7" opacity="0.65"/>
      <path d="M4 -18 C1 -25, 5 -29, 7 -33" fill="none" stroke="{accent}" stroke-width="1.7" opacity="0.65"/>
    </g>
    """


def draw_couple(design: Design) -> str:
    r1, g1, b1 = design.top_left
    r2, g2, b2 = design.top_right
    return f"""
    <g transform="translate(0 -2)">
      <ellipse cx="408" cy="343" rx="112" ry="34" fill="#EFE8DE" opacity="0.72"/>
      <ellipse cx="619" cy="352" rx="108" ry="30" fill="#EFE8DE" opacity="0.68"/>

      <path d="M377 178 C361 188, 351 202, 350 222 C349 250, 365 272, 391 279 C418 286, 443 269, 448 243 C452 222, 444 198, 428 184 C416 173, 392 169, 377 178 Z"
            fill="{design.hair_left}" opacity="0.98"/>
      <circle cx="395" cy="225" r="40" fill="#F4C9AD"/>
      <path d="M363 219 C368 196, 380 181, 400 178 C414 176, 429 183, 438 194 C429 190, 421 193, 413 198 C401 206, 395 208, 386 209 C379 210, 372 212, 363 219 Z"
            fill="{design.hair_left}"/>
      <path d="M408 250 C412 260, 419 268, 427 273" fill="none" stroke="#52392D" stroke-width="2" stroke-linecap="round"/>
      <path d="M402 236 C409 238, 418 237, 424 232" fill="none" stroke="#52392D" stroke-width="2" stroke-linecap="round"/>
      <path d="M425 220 C432 220, 437 223, 440 228" fill="none" stroke="#52392D" stroke-width="2" stroke-linecap="round" opacity="0.7"/>
      <path d="M393 221 C387 220, 380 223, 376 227" fill="none" stroke="#52392D" stroke-width="2" stroke-linecap="round" opacity="0.7"/>
      <path d="M408 243 C416 249, 426 252, 435 250" fill="none" stroke="#8D5B4B" stroke-width="2.2" stroke-linecap="round"/>

      <path d="M359 272 C379 265, 407 265, 429 275 C445 282, 457 295, 462 321 C466 341, 466 357, 463 377 L335 377 C335 349, 338 327, 346 307 C350 296, 354 283, 359 272 Z"
            fill="{design.top_left_clothing}"/>
      <path d="M460 327 C446 318, 432 311, 416 304 C401 296, 387 291, 373 287" fill="none" stroke="#D5C8B6" stroke-width="4" stroke-linecap="round"/>
      <path d="M341 309 C350 339, 359 365, 381 390 C405 416, 431 430, 461 441"
            fill="none" stroke="{design.pants_left}" stroke-width="34" stroke-linecap="round"/>
      <path d="M434 384 C407 403, 378 410, 348 411" fill="none" stroke="{design.pants_left}" stroke-width="34" stroke-linecap="round"/>
      <path d="M343 414 C335 421, 336 433, 348 436 C360 439, 373 437, 381 431" fill="#F4C9AD"/>
      <path d="M456 441 C451 451, 456 460, 467 460 C478 460, 488 453, 491 443" fill="#F4C9AD"/>
      <path d="M443 314 C450 336, 454 356, 454 373" fill="none" stroke="#F4C9AD" stroke-width="22" stroke-linecap="round"/>
      <path d="M337 311 C350 330, 366 338, 390 339" fill="none" stroke="#F4C9AD" stroke-width="20" stroke-linecap="round"/>
      <path d="M422 313 C432 321, 440 325, 451 328" fill="none" stroke="#F4C9AD" stroke-width="16" stroke-linecap="round"/>
      {draw_mug(449, 323, "#E4B640", design.accent, -4)}

      <path d="M600 177 C583 193, 577 214, 580 237 C583 257, 596 274, 617 281 C644 289, 671 272, 678 247 C685 224, 675 200, 658 185 C644 173, 616 167, 600 177 Z"
            fill="{design.hair_right}" opacity="0.98"/>
      <circle cx="630" cy="226" r="39" fill="#F3C6A8"/>
      <path d="M649 173 C663 182, 670 194, 671 207 C670 223, 663 236, 651 242 C651 229, 643 221, 632 215 C619 208, 607 204, 594 202 C598 188, 608 177, 620 173 C629 170, 640 170, 649 173 Z"
            fill="{design.hair_right}"/>
      <path d="M654 175 C667 168, 680 175, 686 188 C691 201, 687 215, 675 222 C673 208, 670 195, 654 175 Z"
            fill="{design.hair_right}"/>
      <path d="M611 220 C606 220, 600 223, 596 227" fill="none" stroke="#52392D" stroke-width="2" stroke-linecap="round" opacity="0.7"/>
      <path d="M639 220 C646 220, 652 224, 655 229" fill="none" stroke="#52392D" stroke-width="2" stroke-linecap="round" opacity="0.7"/>
      <path d="M624 239 C631 246, 642 249, 651 246" fill="none" stroke="#8D5B4B" stroke-width="2.2" stroke-linecap="round"/>

      <path d="M580 274 C600 262, 635 261, 663 271 C683 278, 695 297, 696 330 L694 379 L557 379 C559 349, 561 321, 565 300 C567 288, 571 280, 580 274 Z"
            fill="rgb({r2},{g2},{b2})"/>
      <path d="M593 259 C610 249, 648 248, 666 259 C677 266, 682 280, 684 296 C663 290, 641 287, 619 287 C602 287, 585 290, 568 296 C570 281, 577 268, 593 259 Z"
            fill="rgb({max(r2 - 24, 0)},{max(g2 - 22, 0)},{max(b2 - 18, 0)})"/>
      <path d="M586 315 C596 337, 607 361, 637 387 C656 403, 671 415, 678 423" fill="none" stroke="{design.pants_right}" stroke-width="32" stroke-linecap="round"/>
      <path d="M653 383 C625 402, 601 411, 572 411" fill="none" stroke="{design.pants_right}" stroke-width="32" stroke-linecap="round"/>
      <path d="M675 421 C671 432, 676 442, 688 442 C699 442, 707 434, 709 424" fill="#F3C6A8"/>
      <path d="M569 414 C560 420, 560 433, 571 436 C582 439, 595 437, 602 431" fill="#F3C6A8"/>
      <path d="M572 312 C584 332, 595 337, 617 337" fill="none" stroke="#F3C6A8" stroke-width="18" stroke-linecap="round"/>
      <path d="M611 307 C608 325, 611 348, 617 364" fill="none" stroke="#F3C6A8" stroke-width="18" stroke-linecap="round"/>
      {draw_mug(615, 307, "#D7A93A", design.accent, 4)}
    </g>
    """


def draw_text_block(quote: str, color: str) -> str:
    lines = quote.split("\n")
    start_y = 424
    spacing = 50
    tspans = []
    for index, line in enumerate(lines):
        dy = 0 if index == 0 else spacing
        tspans.append(
            f'<tspan x="{WIDTH / 2}" dy="{dy}">{svg_escape(line)}</tspan>'
        )
    return f"""
    <text x="{WIDTH / 2}" y="{start_y}" text-anchor="middle"
          font-family="'Georgia', 'Times New Roman', serif"
          font-size="34" font-weight="700" fill="{color}" letter-spacing="0.2">
      {''.join(tspans)}
    </text>
    """


def build_svg(design: Design) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="{design.slug}-title {design.slug}-desc">
  <title id="{design.slug}-title">{svg_escape(design.quote.replace(chr(10), ' '))}</title>
  <desc id="{design.slug}-desc">Romantic coffee-inspired quote card with decorative gold corners and a seated couple illustration.</desc>
  <rect width="100%" height="100%" fill="#FBF8F3"/>
  <rect x="18" y="18" width="{WIDTH - 36}" height="{HEIGHT - 36}" rx="22" fill="none" stroke="#F0E5D2" stroke-width="1.4"/>
  {draw_corner(10, 6, design.accent)}
  {draw_corner(WIDTH - 190, 6, design.accent, flip_x=True)}
  {draw_corner(10, HEIGHT - 186, design.accent, flip_y=True)}
  {draw_corner(WIDTH - 190, HEIGHT - 186, design.accent, flip_x=True, flip_y=True)}
  {draw_side_motif(29, 253, design.accent)}
  {draw_side_motif(967, 253, design.accent)}
  {draw_couple(design)}
  {draw_text_block(design.quote, design.text)}
  <path d="M496 544 L504 529 L512 544" fill="none" stroke="{design.accent}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M506 544 L514 529 L522 544" fill="none" stroke="{design.accent}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""


def build_index(designs: list[Design]) -> str:
    bullets = "\n".join(
        f"- **{design.slug}.svg** - {design.quote.replace(chr(10), ' ')}"
        for design in designs
    )
    return f"""# Inspired poster set

Five original SVG designs inspired by the provided romantic coffee-card aesthetic.

## Files

{bullets}

## Notes

- Vector format for easy editing in Figma, Illustrator, Inkscape, or a code editor.
- Shared visual language: soft neutral background, gold ornamental corners, centered seated couple, and decorative serif quote treatment.
- Generated by `designs/generate_inspired_designs.py`.
"""


def build_gallery(designs: list[Design]) -> str:
    cards = "\n".join(
        f"""
        <article class="card">
          <h2>{svg_escape(design.slug)}</h2>
          <p>{svg_escape(design.quote.replace(chr(10), ' '))}</p>
          <img src="generated/{svg_escape(design.slug)}.svg" alt="{svg_escape(design.quote.replace(chr(10), ' '))}">
        </article>
        """
        for design in designs
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Inspired poster gallery</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f7f1e8;
      --panel: #fffdf9;
      --ink: #6e4b1c;
      --line: #ddc9ab;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      background: linear-gradient(180deg, #f9f4ec 0%, var(--bg) 100%);
      color: var(--ink);
    }}
    main {{
      max-width: 1380px;
      margin: 0 auto;
      padding: 32px 24px 48px;
    }}
    h1 {{
      text-align: center;
      font-size: 2.1rem;
      margin: 0 0 10px;
    }}
    .intro {{
      text-align: center;
      margin: 0 auto 28px;
      max-width: 760px;
      line-height: 1.5;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 22px;
    }}
    .card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 18px;
      box-shadow: 0 10px 30px rgba(110, 75, 28, 0.08);
    }}
    .card h2 {{
      font-size: 1.1rem;
      margin: 0 0 8px;
    }}
    .card p {{
      margin: 0 0 14px;
      min-height: 3em;
      line-height: 1.4;
    }}
    .card img {{
      width: 100%;
      height: auto;
      display: block;
      border-radius: 12px;
      border: 1px solid #eadbc3;
      background: #fbf8f3;
    }}
  </style>
</head>
<body>
  <main>
    <h1>Inspired poster gallery</h1>
    <p class="intro">Five original SVG designs created from the supplied romantic coffee-card aesthetic, each keeping the ornate frame, warm palette, and playful security-themed copy direction.</p>
    <section class="grid">
      {cards}
    </section>
  </main>
</body>
</html>
"""


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for design in DESIGNS:
        output_path = os.path.join(OUTPUT_DIR, f"{design.slug}.svg")
        with open(output_path, "w", encoding="utf-8") as handle:
            handle.write(build_svg(design))

    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(readme_path, "w", encoding="utf-8") as handle:
        handle.write(build_index(DESIGNS))

    gallery_path = os.path.join(os.path.dirname(__file__), "gallery.html")
    with open(gallery_path, "w", encoding="utf-8") as handle:
        handle.write(build_gallery(DESIGNS))


if __name__ == "__main__":
    main()
