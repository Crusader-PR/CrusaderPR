# crusaderpr.com rebuild

Preview build of the redesigned Crusader Public Relations site. The live site on River Avenue Digital is untouched.

- `index.html` and `styles.css`: a single static page, no build step.
- Published to GitHub Pages from `main` for preview. The page carries `noindex` so search engines skip it.

Still needed before launch: About content from Brian, a working contact form endpoint, and the logo and photos copied into the repo instead of linked from the current host.

## Editing the site

- **Brian (no git):** open any page with `#edit` at the end of the address, for example `https://crusader-pr.github.io/CrusaderPR/about.html#edit`. Click Edit This Page, change text or links, then Publish. The first time, click Access Key and paste a fine-grained GitHub token limited to this repo with Contents: Read and write.
- **Structural changes:** `python3 _build/build.py` regenerates the shared head, header and footer on every page while keeping each page's published `<main>` content. Add `--reset` only to rebuild pages from the template (this discards edits made in the browser).
