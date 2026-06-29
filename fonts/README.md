# Your handwriting font

This folder holds the **master copy** of your handwriting font. `setup.sh` copies any
`.woff2 / .woff / .ttf / .otf` from here into `template/css/fonts/`, and from there
every new talk inherits it.

## 1. Create it on the iPad

- **iFontMaker** (one-time ~$7.99) — draw each glyph with the Apple Pencil and export a
  TrueType (`.ttf`); it also supports web-font export. Easiest Pencil-native option.
- **Calligraphr** (free) — print a template, write on it, scan/photograph, upload. Free
  tier caps at ~75 glyphs; Pro raises the limit. Good if you don't have iFontMaker.

Aim to cover: A–Z, a–z, 0–9, and the punctuation you actually use on slides
(`. , : ; ( ) [ ] + - = / % $ ` and so on).

## 2. Convert to WOFF2 (smaller, faster)

From a `.ttf`:

```
npx ttf2woff2 < myhand.ttf > myhand.woff2
```

(Or any TTF→WOFF2 converter.) Keep the `.ttf` too as a fallback.

## 3. Name and place the files

Put them here as `myhand.woff2` (and optionally `myhand.ttf`). The name must match the
`@font-face` rule in `template/css/custom.css` — if you use a different name, update
that rule.

## 4. Propagate

```
./setup.sh        # copies the font into template/css/fonts/
```

New talks created with `./new-talk.sh` will include it automatically. For talks you
already created, copy the font into that talk's `css/fonts/` folder as well.

## Note on equations

By default, equations render in KaTeX's standard math fonts for legibility. If you want
them in your handwriting too, uncomment the `.reveal .katex` rule in `custom.css` and
test your real equations first — letter/number shapes follow the font, but accent and
operator metrics can drift.
