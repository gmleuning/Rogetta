# Roget's Thesaurus (1911) — Self-Hosted Interface

A single-file, zero-dependency web interface to **Roget's Thesaurus of English Words and Phrases** (1911 edition, Peter Mark Roget), as digitised by [Project Gutenberg](https://www.gutenberg.org/ebooks/10681). The full 1,000-entry corpus is embedded directly in `index.html` — no build step, no server-side code, no database, no network calls. Open the file in a browser and it works.

## What it does

- **Full-corpus search.** Type a word or phrase and every entry containing it is listed, with matching lines highlighted. Headword matches are listed first; body matches follow in Roget's original order.
- **Entry numbers as addresses.** Typing `494` opens entry 494 directly. Results and cross-references are clickable anchors (`#e=494`), so entries can be bookmarked and linked.
- **Intact entry structure.** Each entry shows its full path through Roget's hierarchy (Class › Section › Group), part-of-speech groupings (N., V., Adj., Adv., Phr.), synonym lists, and glosses.
- **Roget's cross-references are live.** The `&c 197`, `&c 350`-style pointers throughout the text are rendered as clickable links to the referenced entry. Obsolete terms are marked with a dagger (†).
- **Whole-word or partial matching.** Whole-word by default; a checkbox switches to substring matching. Accents are folded, so *naive* finds *naïve*.
- **"Show full entry".** In search results, only matching lines are shown by default. A button expands an entry to its full text without leaving the results page.
- **Keyboard-driven.** <kbd>/</kbd> focuses the search box, <kbd>Esc</kbd> clears it, <kbd>Alt</kbd>+click on any word or phrase runs a new search for it.
- **Preferences persist.** The partial-match, full-entry, hide-obsolete, and light/dark settings are stored in `localStorage` and restored on the next visit.
- **Light and dark themes.** Follows the system preference by default; the toggle overrides it.

## Files

| File | Purpose |
|---|---|
| `index.html` | The entire application — markup, styles, data, and logic in one file. |
| `rogets1911.txt` | The source text (Project Gutenberg eBook #10681). Reference only; the interface does not read it at runtime. |

`index.html` is self-contained. The corpus is embedded as a JavaScript array literal (`const D = [...]`), and all styling and behaviour live in `<style>` and `<script>` blocks. Copy it anywhere and it runs.

## Hosting

Because there is nothing to build and nothing to serve dynamically, any static host works:

- **GitHub Pages** — drop `index.html` at the repo root, enable Pages, done. This is the simplest option for a repo of this kind.
- **Local file** — `file:///path/to/index.html` works as-is. No CORS issues, no fetch, no module loading.
- **Any static file server** — nginx, Caddy, `python -m http.server`, a Raspberry Pi, whatever you already run.

No configuration, no environment variables, no reverse proxy rules beyond serving one file. Hash-based routing (`#q=…`, `#e=…`) means deep links work without any server-side rewrite rules.

## Adding an Omnibox shortcut in Chrome (or any Chromium browser)

Chrome's omnibox supports **custom search engines** — keyword shortcuts that send whatever you type in the address bar to a URL of your choosing. This makes the thesaurus reachable without opening a bookmark or a new tab first: type a keyword, a space, the word, and Enter.

### Setup

1. Open `chrome://settings/searchEngines` (Edge: `edge://settings/searchEngines`, Brave: `brave://settings/searchEngines`).
2. Scroll to the **Site search** section and click **Add**.
3. Fill in the three fields:

   | Field | Value |
   |---|---|
   | **Search engine** | `Roget` (any name you'll recognise in the list) |
   | **Shortcut** | `rog` (or any keyword without spaces; must not clash with an existing one) |
   | **URL** | `https://your-host.example/index.html#q=%s` |

4. Click **Save**.

Replace `https://your-host.example/index.html` with wherever you host the file — a GitHub Pages URL, a LAN address, or a `file:///` path if you run it locally.

### Use

Type `rog`, press <kbd>Space</kbd> (the omnibox shows "Search Roget"), type a word or phrase, and press <kbd>Enter</kbd>:

```

rog taciturn

```

…opens the interface with that search already running. The `#q=` fragment is exactly what the page's own router reads, so the omnibox shortcut uses the same code path as typing into the search box — nothing special is needed on the page side.

### Notes

- The `%s` placeholder is where Chrome substitutes the typed query. It is URL-encoded automatically, so spaces and punctuation are safe.
- To open a specific entry number instead of searching, use `…#e=%s` and type `rog 494`. Entry numbers are matched before search terms, so a bare number jumps straight to that entry.
- If you host the interface on a domain you visit often and want the shortcut to feel native, Chrome also lists it under "Inactive shortcuts" once you've used the site's own search box — but the manual entry above is more reliable and works for `file://` and LAN hosts too.
- Firefox does the same thing via **Bookmarks → Manage Bookmarks → New Bookmark**, setting a **Keyword** and using `%s` in the location. Safari has no equivalent.

## Notes on the corpus

The embedded data is a lightly normalised transcription of the Gutenberg text: entries are indexed by their Roget numbers (including the `16a`, `59a`, `604a`-style sub-entries), senses are split on commas and semicolons outside brackets, and the trailing numeric cross-references are preserved as numbers for linking. The text itself is unchanged — including the occasional
