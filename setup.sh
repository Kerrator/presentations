#!/usr/bin/env bash
# Vendors every third-party asset into template/lib so decks run fully offline.
# Re-run any time you bump a version in package.json.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIB="$ROOT/template/lib"
TMP="$ROOT/.vendor-tmp"

echo "==> Installing pinned packages (reveal.js, katex, chalkboard, menu)..."
rm -rf "$TMP"; mkdir -p "$TMP"
cp "$ROOT/package.json" "$TMP/package.json"
( cd "$TMP" && npm install --no-audit --no-fund --silent )

echo "==> Vendoring into template/lib ..."
rm -rf "$LIB"
mkdir -p "$LIB/reveal/plugin/highlight" "$LIB/katex" \
         "$LIB/plugins/chalkboard" "$LIB/plugins/menu"

# --- reveal.js core (v6 layout: flat dist/plugin/*.js) ---
cp "$TMP/node_modules/reveal.js/dist/reveal.css" "$LIB/reveal/"
cp "$TMP/node_modules/reveal.js/dist/reset.css"  "$LIB/reveal/"
cp "$TMP/node_modules/reveal.js/dist/reveal.js"  "$LIB/reveal/"
cp -r "$TMP/node_modules/reveal.js/dist/theme"   "$LIB/reveal/theme"
for p in markdown highlight notes math search zoom; do
  cp "$TMP/node_modules/reveal.js/dist/plugin/$p.js" "$LIB/reveal/plugin/"
done
cp "$TMP/node_modules/reveal.js/dist/plugin/highlight/monokai.css" "$LIB/reveal/plugin/highlight/"
cp "$TMP/node_modules/reveal.js/dist/plugin/highlight/zenburn.css" "$LIB/reveal/plugin/highlight/"

# Make EVERY bundled theme offline-safe: strip the remote @import(Google Fonts) that
# ships in beige/blood/league/moon/night/simple/sky/solarized. Without this, switching
# to one of those themes silently fetches fonts at runtime and breaks the "runs with the
# Wi-Fi off" guarantee. custom.css sets the house font anyway, so the local fallback is fine.
for css in "$LIB"/reveal/theme/*.css; do
  perl -0777 -pi -e 's/\@import\s+(?:url\()?["\x27]?https?:\/\/fonts\.googleapis\.com[^;]*;//g' "$css"
done

# --- KaTeX (math plugin loads <local>/dist/katex.min.* + contrib/mhchem for \ce{}) ---
cp -r "$TMP/node_modules/katex/dist" "$LIB/katex/dist"

# --- chalkboard plugin (rajgoel): needs plugin.js + style.css + img/ ---
cp "$TMP/node_modules/reveal.js-plugins/chalkboard/plugin.js" "$LIB/plugins/chalkboard/"
cp "$TMP/node_modules/reveal.js-plugins/chalkboard/style.css" "$LIB/plugins/chalkboard/"
cp -r "$TMP/node_modules/reveal.js-plugins/chalkboard/img"    "$LIB/plugins/chalkboard/img"

# --- slide menu plugin (denehyg): jump anywhere, helps non-linear navigation ---
cp "$TMP/node_modules/reveal.js-menu/menu.js"       "$LIB/plugins/menu/"
cp "$TMP/node_modules/reveal.js-menu/menu.css"      "$LIB/plugins/menu/"
cp -r "$TMP/node_modules/reveal.js-menu/font-awesome" "$LIB/plugins/menu/font-awesome"

# --- copy your handwriting font(s) from the master fonts/ folder into the template ---
mkdir -p "$ROOT/template/css/fonts"
shopt -s nullglob
for f in "$ROOT"/fonts/*.woff2 "$ROOT"/fonts/*.woff "$ROOT"/fonts/*.ttf "$ROOT"/fonts/*.otf; do
  cp "$f" "$ROOT/template/css/fonts/"
  echo "    copied font: $(basename "$f")"
done
shopt -u nullglob

rm -rf "$TMP"
echo "==> Done. template/lib is populated and runs offline."
echo "    Start a talk:   ./new-talk.sh 2026-my-talk"
