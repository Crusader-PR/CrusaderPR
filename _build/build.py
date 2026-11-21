"""Builds the site pages from one shared header/footer. Run: python3 _build/build.py"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = "https://irp.cdn-website.com/555274c7/dms3rep/multi/opt/Untitled+design+-+2024-12-01T231554.836-1920w.png"
PHOTO = "https://irp.cdn-website.com/555274c7/dms3rep/multi/opt/pexels-photo-5673510-1920w.jpeg"

NAV = [("index.html", "Home"), ("index.html#services", "Services"), ("index.html#work", "Our Work"),
       ("about.html", "About"), ("testimonials.html", "Testimonials"), ("contact.html", "Contact")]

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
<link rel="stylesheet" href="styles.css">
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
      <p class="social">YouTube · TikTok · Instagram · Facebook <em>(links to come)</em></p>
    </div>
    <nav><a href="index.html#services">Services</a><a href="about.html">About</a><a href="testimonials.html">Testimonials</a><a href="contact.html">Contact</a></nav>
  </div>
  <div class="wrap legal">© <span id="yr"></span> Crusader Public Relations, LLC</div>
</footer>

<script>
  document.getElementById('yr').textContent = new Date().getFullYear();
  const btn = document.querySelector('.menu-btn'), menu = document.getElementById('menu');
  const setMenu = open => {{ menu.hidden = !open; btn.setAttribute('aria-expanded', open); btn.classList.toggle('open', open); }};
  btn.addEventListener('click', () => setMenu(menu.hidden));
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', e => {{ if (e.key === 'Escape') setMenu(false); }});
  // Service boxes start open on wide screens, collapsed on phones
  if (window.matchMedia('(min-width: 861px)').matches) document.querySelectorAll('details.svc').forEach(d => d.open = true);
</script>
</body>
</html>
"""

SERVICES = [
    ("Text Messaging", "Targeted, compliant SMS and picture texts that drive engagement, turnout and fundraising.",
     ["4¢ per message", "Federal 10DLC approval handled for you", "Free list scrubbing", "Full analytics on every send"]),
    ("Digital Advertising", "Precision-targeted ads across search, social and display.",
     ["Audience targeting by district and demographic", "Search, social and display placements", "Performance reporting"]),
    ("Website Design and Development", "Mobile-friendly sites that inform, inspire and drive action.",
     ["Campaign and business websites", "Domains, DNS and Google Workspace setup", "Email sends and tracked links"]),
    ("OTT Television Commercials", "Audience-targeted video on streaming TV platforms.",
     ["Spots produced in-house", "Targeted by geography and audience", "Delivery reporting"]),
    ("Social Media", "Campaigns that keep your message in front of voters and customers.",
     ["Content calendars and posting", "Platform setup and management", "Paid social"]),
    ("Video Studio Filming and Editing", "Professional, high-quality video from our in-house studio.",
     ["Filming on location or in studio", "Editing for TV, streaming and social", "Explainer and testimonial videos"]),
    ("Graphic Design", "Eye-catching visuals from logos to mailers.",
     ["Logos and brand kits", "Flyers, signs and mailers", "Digital and social assets"]),
    ("Print and Direct Mail Services", "Persuasive, high-quality materials delivered to voters' hands.",
     ["Design, print and mail in one place", "Targeted mail lists", "Door hangers, postcards and more"]),
    ("Campaign Strategy", "A clear, results-driven plan that turns goals into action.",
     ["Message and audience strategy", "Budget and timeline planning", "Election Day war room"]),
]

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
        <p class="eyebrow">Crusader Public Relations</p>
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
      <p class="section-lede">Everything a campaign, cause or business needs to reach people. Tap a service to see what's included.</p>
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
        <figure class="work-item work-wide">
          <div class="work-media" data-kind="Video">OTT Commercial</div>
          <figcaption><strong>Streaming TV Spot</strong> Sample caption</figcaption>
        </figure>
        <figure class="work-item">
          <div class="work-media tall" data-kind="Picture text">Picture Text</div>
          <figcaption><strong>Get-Out-The-Vote Text</strong> Sample caption</figcaption>
        </figure>
        <figure class="work-item">
          <div class="work-media" data-kind="Print">Direct Mail Piece</div>
          <figcaption><strong>Direct Mail</strong> Sample caption</figcaption>
        </figure>
        <figure class="work-item">
          <div class="work-media" data-kind="Social">Social Graphic</div>
          <figcaption><strong>Social Campaign</strong> Sample caption</figcaption>
        </figure>
        <figure class="work-item">
          <div class="work-media" data-kind="Web">Campaign Website</div>
          <figcaption><strong>Website</strong> Sample caption</figcaption>
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
""" + "".join(f"            <option>{s[0]}</option>\n" for s in SERVICES) + """            <option>Not sure yet</option>
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

if __name__ == "__main__":
    for fn, (t, d, b) in PAGES.items():
        with open(os.path.join(ROOT, fn), "w") as f:
            f.write(page(t, d, b, fn))
    print("built", ", ".join(PAGES))
