"""Builds the site pages from one shared header/footer. Run: python3 _build/build.py"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = "https://irp.cdn-website.com/555274c7/dms3rep/multi/opt/Untitled+design+-+2024-12-01T231554.836-1920w.png"
PHOTO = "https://irp.cdn-website.com/555274c7/dms3rep/multi/opt/pexels-photo-5673510-1920w.jpeg"

NAV = [("index.html", "Home"), ("index.html#services", "Services"), ("index.html#work", "Our Work"),
       ("about.html", "About"), ("testimonials.html", "Testimonials"), ("contact.html", "Contact")]

import hashlib
CSS_V = hashlib.md5(open(os.path.join(ROOT, "styles.css"), "rb").read()).hexdigest()[:8]

def page(title, desc, body, current):
    links = "\n".join(
        f'        <a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Preview build: keep out of search engines until this replaces the live site -->
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css?v={CSS_V}">
</head>
<body>

<div class="preview-bar">Preview build. Not the live site.</div>

<header class="site-header">
  <div class="wrap header-inner">
    <a href="index.html" class="brand">
      <img src="{LOGO}" alt="Crusader Public Relations logo" width="76" height="76">
      <span class="wordmark"><span>Crusader</span><small>Public Relations</small></span>
    </a>
    <div class="header-actions">
      <a href="contact.html" class="btn btn-primary btn-cta">Book a Consultation</a>
      <button class="menu-btn" aria-expanded="false" aria-controls="menu" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
  <nav id="menu" class="menu" hidden>
    <div class="wrap menu-inner">
{links}
    </div>
  </nav>
</header>

<main>
{body}
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div>
      <p class="footer-brand">Crusader Public Relations, LLC</p>
      <p class="legal-line">© <span id="yr"></span> Crusader Public Relations, LLC. All rights reserved.</p>
    </div>
    <div class="social-icons">
        <a href="#" aria-label="YouTube"><svg viewBox="0 0 24 24"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.7 15.1V8.9l5.8 3.1-5.8 3.1z"/></svg></a>
        <a href="#" aria-label="TikTok"><svg viewBox="0 0 24 24"><path d="M16.6 2h-3.4v13.4a2.9 2.9 0 1 1-2.9-2.9c.3 0 .6 0 .9.1V9.1a6.4 6.4 0 1 0 5.4 6.3V8.6a8 8 0 0 0 4.7 1.5V6.7a4.7 4.7 0 0 1-4.7-4.7z"/></svg></a>
        <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zM12 1.5c-2.9 0-3.2 0-4.3.1C3.4 1.8 1.8 3.4 1.6 7.7 1.5 8.8 1.5 9.1 1.5 12s0 3.2.1 4.3c.2 4.3 1.8 5.9 6.1 6.1 1.1.1 1.4.1 4.3.1s3.2 0 4.3-.1c4.3-.2 5.9-1.8 6.1-6.1.1-1.1.1-1.4.1-4.3s0-3.2-.1-4.3c-.2-4.3-1.8-5.9-6.1-6.1-1.1-.1-1.4-.1-4.3-.1zm0 1.9c2.8 0 3.2 0 4.3.1 3.1.1 4.1 1.2 4.3 4.3.1 1.1.1 1.4.1 4.2s0 3.2-.1 4.3c-.1 3.1-1.2 4.1-4.3 4.3-1.1.1-1.4.1-4.3.1s-3.2 0-4.2-.1c-3.1-.1-4.2-1.2-4.3-4.3-.1-1.1-.1-1.4-.1-4.3s0-3.1.1-4.2c.1-3.1 1.2-4.2 4.3-4.3 1-.1 1.4-.1 4.2-.1z"/></svg></a>
        <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg></a>
    </div>
  </div>
</footer>

<script>
  document.getElementById('yr').textContent = new Date().getFullYear();
  const btn = document.querySelector('.menu-btn'), menu = document.getElementById('menu');
  const setMenu = open => {{ menu.hidden = !open; btn.setAttribute('aria-expanded', open); btn.classList.toggle('open', open); }};
  btn.addEventListener('click', () => setMenu(menu.hidden));
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', e => {{ if (e.key === 'Escape') setMenu(false); }});
  // Service boxes start open on wide screens, collapsed on phones
  const io = 'IntersectionObserver' in window && new IntersectionObserver(es => es.forEach(e => {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }}), {{ threshold: .12 }});
  document.querySelectorAll('.section .wrap, .proof-inner').forEach(el => {{ if (io) {{ el.classList.add('reveal'); io.observe(el); }} }});
  if (window.matchMedia('(min-width: 861px)').matches) document.querySelectorAll('details.svc').forEach(d => d.open = true);
</script>
</body>
</html>
"""

SERVICES = [
    ("Voter & Customer Outreach", "Reach people directly and measure what lands.",
     ["Text messaging: SMS and picture texts at 4¢ per message, with 10DLC approval, free list scrubbing and full analytics",
      "Digital advertising across search, social and display",
      "OTT and streaming TV commercials",
      "Print and direct mail"]),
    ("Creative & Content", "Professional work produced in-house.",
     ["Video studio: filming and editing",
      "Graphic design, from logos to mailers",
      "Social media content and management"]),
    ("Strategy & Digital", "The plan and the infrastructure behind it.",
     ["Campaign strategy and Election Day war room",
      "Website design and development",
      "Domains, DNS, Google Workspace and email setup"]),
]

CONTACT_OPTIONS = ["Text Messaging", "Digital Advertising", "OTT Television Commercials", "Print and Direct Mail",
                   "Video, Design or Social Media", "Website, Domains or Email", "Campaign Strategy"]

def services_html():
    out = []
    for name, lede, items in SERVICES:
        lis = "".join(f"<li>{i}</li>" for i in items)
        out.append(f"""        <details class="svc">
          <summary>{name}</summary>
          <div class="svc-body"><p>{lede}</p><ul>{lis}</ul></div>
        </details>""")
    return "\n".join(out)

HOME = f"""  <section class="hero">
    <div class="wrap hero-grid">
      <div class="hero-inner">
        <p class="eyebrow">Trailblazers In Campaign Communication</p>
        <h1>Leading The Charge In Political Campaign Communication</h1>
        <p class="lede">From strategy to execution, we build the outreach, creative and digital presence that help candidates, causes and businesses connect, engage and win.</p>
        <div class="hero-actions">
          <a href="contact.html" class="btn btn-light">Book a Consultation</a>
          <a href="#services" class="btn btn-ghost">See Our Services</a>
        </div>
      </div>
      <div class="hero-crest">
        <img src="{LOGO}" alt="" width="360" height="360">
        <span class="motto">Non Exidet</span>
      </div>
    </div>
  </section>

  <section class="proof" aria-label="Track record">
    <div class="wrap proof-inner">
      <div class="stat"><span class="num">30+</span><span class="label">Federal Campaigns</span></div>
      <div class="stat"><span class="num">100+</span><span class="label">State &amp; Local Campaigns</span></div>
      <div class="stat tbd"><span class="num">#M</span><span class="label">Messages Delivered</span></div>
      <div class="stat tbd"><span class="num">#</span><span class="label">States Served</span></div>
      <div class="stat tbd"><span class="num">#</span><span class="label">Years In Business</span></div>
    </div>
    <p class="wrap tbd-note">Dashed figures are placeholders. Real numbers needed from Brian.</p>
  </section>

  <section id="services" class="section">
    <div class="wrap">
      <h2>What We Do</h2>
      <p class="section-lede">Everything a campaign, cause or business needs to reach people. Tap a category to see what's included.</p>
      <div class="svc-grid">
{services_html()}
      </div>
    </div>
  </section>

  <section id="work" class="section section-tint">
    <div class="wrap">
      <h2>Our Work</h2>
      <p class="section-lede">A sample of what we've produced for campaigns and organizations. Client names are removed.</p>
      <div class="work-grid">
        <figure class="work-item">
          <div class="work-media" data-kind="Video">OTT Commercial</div>
          <figcaption><strong>Streaming TV Spot</strong> Sample caption</figcaption>
        </figure>
        <figure class="work-item">
          <div class="work-media" data-kind="Picture text">Picture Text</div>
          <figcaption><strong>Get-Out-The-Vote Text</strong> Sample caption</figcaption>
        </figure>
        <figure class="work-item">
          <div class="work-media" data-kind="Print">Direct Mail</div>
          <figcaption><strong>Mailer</strong> Sample caption</figcaption>
        </figure>
      </div>
      <p class="placeholder small">Placeholder tiles. Swap in anonymized videos and visuals, with names, faces and phone numbers blurred.</p>
    </div>
  </section>

  <section class="cta-band">
    <div class="wrap cta-inner">
      <div>
        <h2>Ready To Make An Impact?</h2>
        <p>Tell us about your campaign or business and we'll set up a consultation.</p>
      </div>
      <a href="contact.html" class="btn btn-light">Book a Consultation</a>
    </div>
  </section>"""

def page_hero(eyebrow, h1, lede):
    return f"""  <section class="page-hero">
    <div class="wrap">
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
    </div>
  </section>"""

CTA = """  <section class="cta-band">
    <div class="wrap cta-inner">
      <div><h2>Let's Win Together</h2><p>Book a consultation to talk through your goals.</p></div>
      <a href="contact.html" class="btn btn-light">Book a Consultation</a>
    </div>
  </section>"""

member = """        <div class="member">
          <div class="avatar"></div>
          <h3>Name</h3>
          <p class="role">Title</p>
          <p>Short bio.</p>
        </div>"""

ABOUT = page_hero("About", "Who We Are", "Crusader Public Relations has supported more than 30 federal and 100 state and local campaigns.") + f"""
  <section class="section">
    <div class="wrap about">
      <h2>Our Story</h2>
      <p class="placeholder">Placeholder: how Crusader started, how long you've done this work, and what sets you apart. Content needed from Brian.</p>
    </div>
  </section>
  <section class="section section-tint">
    <div class="wrap">
      <h2>Our Team</h2>
      <p class="section-lede">The people behind your campaign.</p>
      <div class="team-grid">
{member}
{member}
{member}
      </div>
      <p class="placeholder small">Placeholder: team photos, names, titles and short bios.</p>
    </div>
  </section>
""" + CTA

quote = """        <figure class="quote">
          <blockquote>"Testimonial quote goes here."</blockquote>
          <figcaption><strong>Name</strong> Role, campaign or organization</figcaption>
        </figure>"""

TESTIMONIALS = page_hero("Testimonials", "What Our Clients Say", "Results from the campaigns, causes and businesses we've worked with.") + f"""
  <section class="section">
    <div class="wrap">
      <div class="quote-grid">
{quote}
{quote}
{quote}
{quote}
      </div>
      <p class="placeholder small">Placeholder quotes. Collect testimonials with permission to publish names, or use roles only (for example, "State House candidate, Pennsylvania").</p>
    </div>
  </section>
""" + CTA

CONTACT = page_hero("Contact", "Let's Talk About Your Goals", "Share a few details and we'll reach out to set up a consultation.") + """
  <section class="section">
    <div class="wrap split">
      <div class="contact-aside">
        <h2>What Happens Next</h2>
        <ol class="steps">
          <li><strong>We review your note</strong> and look at your race, cause or business.</li>
          <li><strong>We set up a call</strong> to talk through goals, timing and budget.</li>
          <li><strong>You get a plan</strong> with the services that fit and clear pricing.</li>
        </ol>
      </div>
      <form class="contact-form" onsubmit="event.preventDefault(); this.querySelector('.form-note').hidden=false;">
        <label>Name <input name="name" required autocomplete="name"></label>
        <label>Email <input name="email" type="email" required autocomplete="email"></label>
        <label>Phone <input name="phone" type="tel" autocomplete="tel"></label>
        <label>Campaign, Organization or Business <input name="org" autocomplete="organization"></label>
        <label>What Do You Need Help With?
          <select name="interest">
""" + "".join(f"            <option>{o}</option>\n" for o in CONTACT_OPTIONS) + """            <option>Not sure yet</option>
          </select>
        </label>
        <label>Message <textarea name="message" rows="4"></textarea></label>
        <button class="btn btn-primary" type="submit">Send</button>
        <p class="form-note" hidden>Preview only. This form isn't connected yet.</p>
      </form>
    </div>
  </section>"""

PAGES = {
    "index.html": ("Crusader Public Relations | Political Campaign Communication",
                   "Voter contact, creative and digital strategy for campaigns, causes and businesses.", HOME),
    "about.html": ("About | Crusader Public Relations", "Who is behind Crusader Public Relations.", ABOUT),
    "testimonials.html": ("Testimonials | Crusader Public Relations", "What clients say about Crusader Public Relations.", TESTIMONIALS),
    "contact.html": ("Contact | Crusader Public Relations", "Book a consultation with Crusader Public Relations.", CONTACT),
}

def preview(out_path):
    """One self-contained file holding every page, for previewing without a web server."""
    css = open(os.path.join(ROOT, "styles.css")).read()
    ids = {"index.html": "home", "about.html": "about", "testimonials.html": "testimonials", "contact.html": "contact"}
    bodies = "".join(f'<div class="pv-page" id="page-{ids[fn]}">\n{b}\n</div>\n' for fn, (t, d, b) in PAGES.items())
    html = page("Preview | Crusader Public Relations", "", bodies, "")
    html = html.replace(f'<link rel="stylesheet" href="styles.css?v={CSS_V}">', "<style>\n" + css + "\n.pv-page{display:none}.pv-page.on{display:block}\n</style>")
    html = html.replace('href="index.html#', 'href="#').replace('href="index.html"', 'href="#page-home"')
    for fn, i in ids.items():
        html = html.replace(f'href="{fn}"', f'href="#page-{i}"')
    router = """<script>
  function route() {
    const h = location.hash || '#page-home';
    const target = document.querySelector(h);
    const pg = h.startsWith('#page-') ? target : (target ? target.closest('.pv-page') : null) || document.getElementById('page-home');
    document.querySelectorAll('.pv-page').forEach(p => p.classList.toggle('on', p === pg));
    if (h.startsWith('#page-')) window.scrollTo(0, 0); else if (target) target.scrollIntoView();
  }
  addEventListener('hashchange', route); route();
</script>
</body>"""
    html = html.replace("</body>", router)
    open(out_path, "w").write(html)

if __name__ == "__main__":
    for fn, (t, d, b) in PAGES.items():
        with open(os.path.join(ROOT, fn), "w") as f:
            f.write(page(t, d, b, fn))
    if len(os.sys.argv) > 1:
        preview(os.sys.argv[1])
    print("built", ", ".join(PAGES))
