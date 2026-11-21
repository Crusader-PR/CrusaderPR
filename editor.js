/* Crusader PR page editor.
   Open any page with #edit at the end of its address to edit it. Visitors never load this file.
   Publish saves the page straight to GitHub using an access key kept in this browser only. */
(function () {
  "use strict";
  const REPO = "Crusader-PR/CrusaderPR";
  const BRANCH = "main";
  const KEY_STORE = "crusader-editor-key";

  const TEXT = "main h1, main h2, main h3, main p, main li, main figcaption, main blockquote, main summary, main .num, main .label, main .more, main .motto";
  const REPEAT = "main .member, main .quote, main .work-item, main details.svc, main .stat, main .chips li, main .svc-body li, main .steps li, main .card li";
  const REMOVABLE = REPEAT + ", main .placeholder, main .tbd-note";
  const UI = "[data-ed-ui]";

  const getKey = () => { try { return localStorage.getItem(KEY_STORE) || ""; } catch (e) { return ""; } };
  const setKey = v => { try { v ? localStorage.setItem(KEY_STORE, v) : localStorage.removeItem(KEY_STORE); } catch (e) {} };

  let editing = false, dirty = false, linkTarget = null;

  /* ---------- styles for the editor UI ---------- */
  const css = document.createElement("style");
  css.setAttribute("data-ed-ui", "");
  css.textContent = `
  .ed-bar{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);z-index:1000;display:flex;gap:.5rem;align-items:center;background:#1a0a0e;color:#fff;padding:.55rem .6rem .55rem 1rem;border-radius:999px;box-shadow:0 10px 30px rgba(0,0,0,.35);font:600 14px Sora,system-ui,sans-serif;max-width:94vw;flex-wrap:wrap;justify-content:center}
  .ed-bar button{font:inherit;border:0;border-radius:999px;padding:.55rem 1rem;cursor:pointer;background:#fff;color:#1a0a0e}
  .ed-bar .ed-primary{background:#c6012b;color:#fff}
  .ed-bar .ed-ghost{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.35)}
  .ed-status{opacity:.8;font-weight:400;padding:0 .4rem}
  body.ed-on [contenteditable]{outline:1px dashed rgba(198,1,43,.55);outline-offset:3px;border-radius:3px;cursor:text}
  body.ed-on .hero [contenteditable],body.ed-on .page-hero [contenteditable],body.ed-on .cta-band [contenteditable],body.ed-on .site-footer [contenteditable]{outline-color:rgba(255,255,255,.7)}
  body.ed-on [contenteditable]:focus{outline:2px solid #c6012b;background:rgba(255,255,255,.08)}
  .ed-x{position:absolute;top:-10px;right:-10px;width:24px;height:24px;border-radius:50%;border:0;background:#c6012b;color:#fff;font:700 14px/24px Sora,sans-serif;cursor:pointer;z-index:5;box-shadow:0 2px 6px rgba(0,0,0,.25)}
  .ed-add{display:inline-block;margin:.6rem 0;font:600 13px Sora,sans-serif;border:1px dashed #c6012b;color:#c6012b;background:#fff;border-radius:999px;padding:.35rem .9rem;cursor:pointer}
  .ed-panel{position:fixed;z-index:1001;left:50%;bottom:84px;transform:translateX(-50%);width:min(440px,92vw);background:#fff;color:#1d2230;border-radius:14px;box-shadow:0 18px 50px rgba(0,0,0,.3);padding:1.2rem;font:14px/1.5 Sora,sans-serif}
  .ed-panel h4{margin:0 0 .5rem;font-size:15px}
  .ed-panel input{width:100%;font:inherit;padding:.6rem;border:1px solid #cfd3dc;border-radius:8px;margin:.3rem 0 .8rem;box-sizing:border-box}
  .ed-panel .ed-row{display:flex;gap:.5rem;justify-content:flex-end;flex-wrap:wrap}
  .ed-panel button{font:600 13px Sora,sans-serif;border:0;border-radius:999px;padding:.5rem 1rem;cursor:pointer;background:#eee}
  .ed-panel .ed-primary{background:#c6012b;color:#fff}
  .ed-panel small{color:#545b6e}
  `;
  document.head.appendChild(css);

  /* ---------- bar ---------- */
  const bar = el(`<div class="ed-bar" data-ed-ui>
      <button class="ed-toggle">Edit This Page</button>
      <button class="ed-publish ed-primary" hidden>Publish</button>
      <button class="ed-cancel ed-ghost" hidden>Discard</button>
      <button class="ed-key ed-ghost">Access Key</button>
      <span class="ed-status"></span></div>`);
  document.body.appendChild(bar);
  const $ = s => bar.querySelector(s);
  const status = t => { $(".ed-status").textContent = t || ""; };
  status(getKey() ? "" : "Add your access key to publish");

  $(".ed-toggle").onclick = () => (editing ? stop() : start());
  $(".ed-cancel").onclick = () => { if (!dirty || confirmInline()) location.reload(); };
  $(".ed-publish").onclick = publish;
  $(".ed-key").onclick = keyPanel;

  function confirmInline() { return window.confirm("Discard your unpublished changes?"); }

  /* ---------- edit mode ---------- */
  function start() {
    editing = true;
    document.body.classList.add("ed-on");
    // show everything so it can be edited
    document.querySelectorAll(".reveal").forEach(n => n.classList.add("in"));
    document.querySelectorAll(TEXT).forEach(n => {
      if (n.closest(UI) || n.closest("form")) return;
      n.setAttribute("contenteditable", "true");
    });
    addControls();
    $(".ed-toggle").textContent = "Done Editing";
    $(".ed-publish").hidden = false;
    $(".ed-cancel").hidden = false;
    status("Click text to edit. Click a link or button to change where it goes.");
  }
  function stop() {
    editing = false;
    document.body.classList.remove("ed-on");
    document.querySelectorAll("[contenteditable]").forEach(n => n.removeAttribute("contenteditable"));
    document.querySelectorAll(".ed-x, .ed-add").forEach(n => n.remove());
    closePanel();
    $(".ed-toggle").textContent = "Edit This Page";
    $(".ed-cancel").hidden = !dirty;
    status(dirty ? "Unpublished changes" : "");
  }

  function addControls() {
    document.querySelectorAll(".ed-x, .ed-add").forEach(n => n.remove());
    document.querySelectorAll(REMOVABLE).forEach(item => {
      if (getComputedStyle(item).position === "static") item.style.position = "relative";
      const x = el(`<button class="ed-x" data-ed-ui title="Remove">×</button>`);
      x.onclick = e => { e.preventDefault(); e.stopPropagation(); item.remove(); dirty = true; addControls(); };
      item.appendChild(x);
    });
    // one Add button per group of repeatable items
    const groups = new Set();
    document.querySelectorAll(REPEAT).forEach(item => groups.add(item.parentElement));
    groups.forEach(g => {
      const items = [...g.children].filter(c => c.matches(REPEAT));
      const last = items[items.length - 1];
      const add = el(`<button class="ed-add" data-ed-ui>+ Add</button>`);
      add.onclick = e => {
        e.preventDefault();
        const copy = last.cloneNode(true);
        copy.querySelectorAll(UI).forEach(n => n.remove());
        last.after(copy);
        dirty = true;
        start();
      };
      const holder = g.tagName === "UL" || g.tagName === "OL" ? g.parentElement : g;
      if (g.tagName === "UL" || g.tagName === "OL") g.after(add); else holder.after(add);
    });
  }

  document.addEventListener("input", e => { if (editing && e.target.closest("[contenteditable]")) { dirty = true; clearTbd(e.target); } });
  // plain-text paste so formatting can't break the design
  document.addEventListener("paste", e => {
    if (!editing || !e.target.closest("[contenteditable]")) return;
    e.preventDefault();
    document.execCommand("insertText", false, (e.clipboardData || window.clipboardData).getData("text/plain"));
  });
  // Enter finishes a line instead of inserting junk markup
  document.addEventListener("keydown", e => {
    if (editing && e.key === "Enter" && e.target.closest("[contenteditable]")) { e.preventDefault(); e.target.blur(); }
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "s" && editing) { e.preventDefault(); publish(); }
  });
  // clicking links/buttons while editing opens the link panel instead of navigating
  document.addEventListener("click", e => {
    if (!editing || e.target.closest(UI)) return;
    const a = e.target.closest("a");
    if (a && !a.closest(".ed-panel")) { e.preventDefault(); linkPanel(a); return; }
    const sum = e.target.closest("summary");
    if (sum) e.preventDefault(); // keep service boxes from toggling while typing
  }, true);

  function clearTbd(node) {
    const stat = node.closest(".stat.tbd");
    if (stat) stat.classList.remove("tbd");
  }

  /* ---------- panels ---------- */
  function closePanel() { document.querySelectorAll(".ed-panel").forEach(p => p.remove()); }
  function panel(html) { closePanel(); const p = el(`<div class="ed-panel" data-ed-ui>${html}</div>`); document.body.appendChild(p); return p; }

  function linkPanel(a) {
    linkTarget = a;
    const p = panel(`<h4>Link</h4>
      <label>Button or link text<input class="ed-lt"></label>
      <label>Goes to<input class="ed-lh" placeholder="https://... or contact.html"></label>
      <div class="ed-row"><button class="ed-close">Cancel</button><button class="ed-primary ed-ok">Update Link</button></div>`);
    p.querySelector(".ed-lt").value = a.textContent.trim();
    p.querySelector(".ed-lh").value = a.getAttribute("href") || "";
    p.querySelector(".ed-close").onclick = closePanel;
    p.querySelector(".ed-ok").onclick = () => {
      const t = p.querySelector(".ed-lt").value.trim(), h = p.querySelector(".ed-lh").value.trim();
      if (t && !a.querySelector("img, svg")) a.textContent = t;
      if (h) a.setAttribute("href", h);
      dirty = true; closePanel();
    };
  }

  function keyPanel() {
    const has = !!getKey();
    const p = panel(`<h4>GitHub access key</h4>
      <small>Paste the fine-grained access key for the ${REPO} repository. It's stored only in this browser, so only set it up on your own computer.</small>
      <input class="ed-k" type="password" placeholder="${has ? "Saved. Paste a new key to replace it" : "github_pat_..."}" autocomplete="off">
      <div class="ed-row">${has ? '<button class="ed-forget">Remove Key</button>' : ""}<button class="ed-close">Cancel</button><button class="ed-primary ed-ok">Save Key</button></div>`);
    p.querySelector(".ed-close").onclick = closePanel;
    const f = p.querySelector(".ed-forget");
    if (f) f.onclick = () => { setKey(""); closePanel(); status("Access key removed"); };
    p.querySelector(".ed-ok").onclick = () => {
      const v = p.querySelector(".ed-k").value.trim();
      if (v) { setKey(v); status("Access key saved"); }
      closePanel();
    };
  }

  /* ---------- publish ---------- */
  function cleanHtml() {
    const doc = document.documentElement.cloneNode(true);
    doc.querySelectorAll(UI).forEach(n => n.remove());
    doc.querySelectorAll("[contenteditable]").forEach(n => n.removeAttribute("contenteditable"));
    doc.querySelectorAll(".reveal").forEach(n => n.classList.remove("reveal", "in"));
    doc.querySelectorAll("details[open]").forEach(n => n.removeAttribute("open"));
    doc.querySelectorAll("[style]").forEach(n => { n.style.removeProperty("position"); if (!n.getAttribute("style")) n.removeAttribute("style"); });
    const menu = doc.querySelector("#menu"); if (menu) menu.setAttribute("hidden", "");
    const mb = doc.querySelector(".menu-btn"); if (mb) { mb.classList.remove("open"); mb.setAttribute("aria-expanded", "false"); }
    doc.querySelectorAll(".ed-on").forEach(n => n.classList.remove("ed-on"));
    doc.querySelectorAll('[class=""]').forEach(n => n.removeAttribute("class"));
    const yr = doc.querySelector("#yr"); if (yr) yr.textContent = "";
    return "<!DOCTYPE html>\n" + doc.outerHTML + "\n";
  }

  function pagePath() {
    let p = location.pathname.split("/").pop();
    return p && p.endsWith(".html") ? p : "index.html";
  }

  const b64 = s => { const bytes = new TextEncoder().encode(s); let bin = ""; bytes.forEach(b => bin += String.fromCharCode(b)); return btoa(bin); };

  async function publish() {
    const key = getKey();
    if (!key) { keyPanel(); status("Add your access key first"); return; }
    if (!dirty) { status("No changes to publish"); return; }
    const btn = $(".ed-publish"); btn.disabled = true; status("Publishing…");
    const path = pagePath();
    const api = `https://api.github.com/repos/${REPO}/contents/${path}`;
    const headers = { Authorization: `Bearer ${key}`, Accept: "application/vnd.github+json" };
    try {
      const cur = await fetch(`${api}?ref=${BRANCH}&t=${Date.now()}`, { headers });
      if (cur.status === 401) throw new Error("The access key didn't work. Check it hasn't expired.");
      if (!cur.ok) throw new Error(`Couldn't read the page from GitHub (${cur.status}).`);
      const { sha } = await cur.json();
      const html = cleanHtml();
      const res = await fetch(api, { method: "PUT", headers, body: JSON.stringify({
        message: `Update ${path} from the page editor`, content: b64(html), sha, branch: BRANCH }) });
      if (res.status === 403 || res.status === 404) throw new Error("This key can't write to the site. It needs Contents: Read and write on this repository.");
      if (res.status === 409) throw new Error("Someone else just published this page. Reload, then make your change again.");
      if (!res.ok) throw new Error(`Publishing failed (${res.status}).`);
      dirty = false;
      stop();
      status("Published. The live page updates in about a minute.");
    } catch (err) {
      status(err.message || "Publishing failed.");
    } finally { btn.disabled = false; }
  }

  window.addEventListener("beforeunload", e => { if (dirty) { e.preventDefault(); e.returnValue = ""; } });

  function el(html) { const t = document.createElement("template"); t.innerHTML = html.trim(); return t.content.firstElementChild; }
})();
