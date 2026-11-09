import os, textwrap
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://webratron.com"
EMAIL = "support@webratron.com"
PHONE = "(917) 924-6809"
PHONE_TEL = "+19179246809"
TRUSTPILOT = "https://www.trustpilot.com/review/webratron.com"
PROVEN = "https://www.provenexpert.com/en-us/webratron/"
ADDRESS = "80 Broad Street, 5th Floor, New York, NY 10004, USA"

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg>'

LOGO = '''<svg viewBox="0 0 40 40" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8b5cf6"/><stop offset="1" stop-color="#ec4899"/></linearGradient></defs><rect width="40" height="40" rx="11" fill="url(#lg)"/><path d="M9 12l4.2 16h1.6L20 16.5 25.2 28h1.6L31 12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

ICONS = {
 "web": '<path d="M3 5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M3 9h18M9 21V9"/>',
 "code": '<path d="m16 18 6-6-6-6M8 6l-6 6 6 6"/>',
 "mobile": '<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/>',
 "brand": '<path d="M12 2l3 7h7l-5.5 4.5L18.5 21 12 16.5 5.5 21l2-7.5L2 9h7z"/>',
 "video": '<rect x="2" y="5" width="15" height="14" rx="2"/><path d="m17 10 5-3v10l-5-3z"/>',
 "seo": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3M8 11h6M11 8v6"/>',
 "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 7H6"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "chart": '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>',
 "pin": '<path d="M12 22s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="10" r="2.5"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
 "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21.2l8.8-8.8a5.5 5.5 0 0 0 0-7.8z"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
}
def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

SOCIAL = {
 "Facebook": '<path fill="currentColor" d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H8v4h2v8h4v-8h3l1-4h-4V8z"/>',
 "Instagram": '<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/>',
 "LinkedIn": '<path fill="currentColor" d="M4 9h4v12H4zM6 3a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM10 9h4v1.7c.6-1 1.9-2 4-2 4 0 4.5 2.6 4.5 6V21h-4v-5.5c0-1.4 0-3.2-2-3.2s-2.3 1.5-2.3 3.1V21h-4z"/>',
 "X": '<path fill="currentColor" d="M17.8 3h3.1l-6.8 7.7L22 21h-6.2l-4.9-6.3L5.3 21H2.2l7.3-8.3L2 3h6.4l4.4 5.8L17.8 3zm-1.1 16.2h1.7L7.4 4.7H5.6l11.1 14.5z"/>',
}
SOCIAL_URL = {"Facebook": "https://facebook.com/", "Instagram": "https://instagram.com/", "LinkedIn": "https://linkedin.com/", "X": "https://x.com/"}

NAV = [("index.html", "Home"), ("services.html", "Services"), ("portfolio.html", "Work"), ("about.html", "About"), ("pricing.html", "Pricing"), ("contact.html", "Contact")]

def header(active):
    links = "\n".join(
        f'        <li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container nav">
    <a href="index.html" class="logo" aria-label="Webratron home">{LOGO}<span>Webratron</span></a>
    <nav aria-label="Primary">
      <ul class="nav__links" id="nav-links">
{links}
        <li class="nav__mobile-cta"><a href="contact.html" class="btn btn--primary btn--block">Start a project</a></li>
      </ul>
    </nav>
    <div class="nav__cta">
      <a href="contact.html" class="btn btn--primary">Start a project {ARROW}</a>
      <button class="nav__toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links"><span></span></button>
    </div>
  </div>
</header>'''

def footer():
    soc = "".join(f'<a href="{SOCIAL_URL[n]}" target="_blank" rel="noopener" aria-label="{n}"><svg viewBox="0 0 24 24" aria-hidden="true">{p}</svg></a>' for n, p in SOCIAL.items())
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__about">
        <a href="index.html" class="logo" aria-label="Webratron home">{LOGO}<span>Webratron</span></a>
        <p>A hub of custom website design — crafting websites, apps, logos and videos that help businesses grow.</p>
        <p style="margin:0"><a href="{TRUSTPILOT}" target="_blank" rel="noopener"><span class="stars">★★★★★</span> 4.7 on Trustpilot</a></p>
      </div>
      <div class="footer__col">
        <h4>Services</h4>
        <ul>
          <li><a href="services.html#web-design">Website Design</a></li>
          <li><a href="services.html#development">Web Development</a></li>
          <li><a href="services.html#mobile">Mobile Apps</a></li>
          <li><a href="services.html#branding">Logo Design &amp; Branding</a></li>
          <li><a href="services.html#ecommerce">Shopify &amp; E-commerce</a></li>
          <li><a href="services.html#video">Video Animation</a></li>
          <li><a href="services.html#seo">SEO &amp; Marketing</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="portfolio.html">Our work</a></li>
          <li><a href="pricing.html">Pricing</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>Get in touch</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{ADDRESS}</li>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span data-year>2026</span> Webratron. All rights reserved.</span>
      <nav aria-label="Legal"><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a></nav>
    </div>
  </div>
</footer>'''

def page(fname, title, desc, body, active=None, schema=""):
    canonical = SITE + "/" + ("" if fname == "index.html" else fname)
    html = f'''<!doctype html>
<html lang="en" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#080716">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Webratron">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/assets/img/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">{schema}
</head>
<body>
{header(active)}
<main id="main">
{textwrap.dedent(body).strip()}
</main>
{footer()}
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, fname), "w") as f:
        f.write(html)

def cta(title="Ready to build something remarkable?", text="Tell us about your project and get a free consultation and quote."):
    return f'''
<section class="section">
  <div class="container">
    <div class="cta-band reveal">
      <h2>{title}</h2>
      <p>{text}</p>
      <div class="hero__actions">
        <a href="contact.html" class="btn btn--primary">Get a free quote {ARROW}</a>
        <a href="mailto:{EMAIL}" class="btn btn--ghost">{EMAIL}</a>
      </div>
    </div>
  </div>
</section>'''

SERVICES = [
 ("web-design", "web", "Website Design", "Custom, conversion-focused designs that make your brand unforgettable on every screen.", ["UI/UX", "Figma", "Responsive"]),
 ("development", "code", "Web Development", "Fast, secure, scalable websites and web apps built with WordPress, Shopify, React and Next.js.", ["WordPress", "React", "Next.js"]),
 ("mobile", "mobile", "Mobile App Development", "Beautiful cross-platform iOS & Android apps built with Flutter and React Native.", ["Flutter", "iOS", "Android"]),
 ("branding", "brand", "Logo Design & Branding", "Custom logos, mascots and stationery that give your business a clear, confident identity.", ["Logo", "Mascot", "Stationery"]),
 ("ecommerce", "cart", "Shopify & E-commerce", "Online stores that sell — Shopify and custom e-commerce, from product pages to checkout.", ["Shopify", "WooCommerce", "Payments"]),
 ("seo", "seo", "SEO & Digital Marketing", "Rank higher and get found with SEO, content marketing and social media marketing.", ["SEO", "Content", "Social Media"]),
 ("video", "video", "Video Animation", "Explainer, whiteboard and 2D brand-intro videos — from 30 to 120 seconds — that tell your story fast.", ["2D Animation", "Whiteboard", "Explainers"]),
 ("maintenance", "shield", "Website Maintenance", "Updates, fixes, security and content changes to keep your website running smoothly.", ["Updates", "Security", "Support"]),
]

def service_cards(limit=None, links=True):
    out = []
    for i, (sid, ic, name, text, tags) in enumerate(SERVICES[:limit] if limit else SERVICES):
        tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
        link = f'<a href="services.html#{sid}" class="card__link">Learn more {ARROW}</a>' if links else ""
        out.append(f'''      <article class="card reveal" data-delay="{i % 4}">
        <div class="icon">{icon(ic)}</div>
        <h3>{name}</h3>
        <p>{text}</p>
        <div class="tags">{tag_html}</div>
        {link}
      </article>''')
    return "\n".join(out)

WORK = [
 ("web", "art--1", "Custom Websites", "Web Design · Development", "Business & corporate websites", "Custom-designed, mobile-responsive websites with CMS so you can update content yourself."),
 ("mobile", "art--2", "Mobile Apps", "Mobile App · Flutter", "Cross-platform mobile apps", "Concepts turned into sleek, fully functional iOS & Android apps built with Flutter."),
 ("branding", "art--3", "Logo & Mascot", "Branding · Logo", "Logos & mascot design", "Unique logos and mascots built from 8 initial concepts, refined with unlimited revisions."),
 ("ecommerce web", "art--4", "Shopify Stores", "E-commerce · Shopify", "Online stores", "Shopify and e-commerce stores with product catalogues, payments and mobile-friendly checkout."),
 ("video", "art--5", "2D Animation", "Animation · Video", "Explainer & brand-intro videos", "Whiteboard and 2D animated videos that explain your product or introduce your brand."),
 ("web", "art--6", "WordPress", "WordPress · SEO", "WordPress websites", "WordPress builds with SEO foundations, ongoing maintenance and easy content editing."),
]

def work_cards(limit=None):
    out = []
    for i, (cat, art, name, kind, short, text) in enumerate(WORK[:limit] if limit else WORK):
        out.append(f'''      <article class="work reveal" data-cat="{cat}" data-delay="{i % 3}">
        <div class="work__thumb"><div class="art {art}"></div><span class="label">{name}</span></div>
        <div class="work__body">
          <small>{kind}</small>
          <h3>{short}</h3>
          <p>{text}</p>
        </div>
      </article>''')
    return "\n".join(out)

TESTIMONIALS = [
 ("Mobile app project", "Webratron built our Flutter app on time and kept us in the loop throughout the project."),
 ("Mascot logo project", "The final mascot logo turned out better than I imagined."),
 ("2D animation project", "The 2D brand intro they created for us was outstanding."),
]
def testimonials():
    out = []
    for i, (role, q) in enumerate(TESTIMONIALS):
        out.append(f'''      <figure class="card quote reveal" data-delay="{i}">
        <div class="stars" aria-label="5 out of 5 stars">★★★★★</div>
        <blockquote>“{q}”</blockquote>
        <figcaption><span class="avatar">★</span><div><strong>Trustpilot review</strong><span>{role}</span></div></figcaption>
      </figure>''')
    return "\n".join(out)

PROCESS = [
 ("Discover", "We dive into your business, goals and audience to define a clear strategy and scope."),
 ("Design", "Wireframes and pixel-perfect designs you review and refine until they feel just right."),
 ("Develop", "Clean, fast, SEO-ready code — built, tested and optimised across every device."),
 ("Launch & Grow", "We launch, monitor and keep improving with support, analytics and marketing."),
]
def process():
    return "\n".join(f'      <div class="step reveal" data-delay="{i}"><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(PROCESS))

FAQS = [
 ("How long does it take to build a website?", "It depends on the size of the project. A small business website is much quicker than a custom web portal or e-commerce store. We share a clear timeline with you before work begins."),
 ("How much does a website cost?", "Our Startup Website Package starts at $469, the Professional package at $1,269 and custom web portals at $5,499. Logo design starts at $149 and video animation at $499. Contact us for a quote tailored to your needs."),
 ("Will my website be mobile-friendly and SEO-ready?", "Yes. Every site we build is fully responsive, fast-loading and follows SEO best practices out of the box, including meta tags, clean structure, sitemaps and performance optimisation."),
 ("Can I update the website myself?", "Absolutely. We build on easy-to-use platforms like WordPress or Shopify (or a custom CMS) and provide a walkthrough so you can edit content, images and products yourself."),
 ("Do you offer support after launch?", "Yes. We offer website maintenance covering updates, fixes, security and content changes. Ask us about support options for your package."),
 ("Do I own the final design?", "Yes. Our packages include full ownership rights to your unique design."),
 ("Do you work with clients outside the USA?", "Yes. We are based in New York and work with clients remotely through calls, email and regular progress updates."),
]
def faqs(n=None):
    items = FAQS[:n] if n else FAQS
    return "\n".join(f'      <details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in items)

def faq_schema():
    import json
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return '\n  <script type="application/ld+json">' + json.dumps(data) + '</script>'

ORG_SCHEMA = '''
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"Webratron","url":"%s","logo":"%s/assets/img/favicon.svg","email":"%s","telephone":"+1-917-924-6809","description":"A hub of custom website design: web design, development, Shopify, mobile apps, logo design, branding, SEO and video animation.","address":{"@type":"PostalAddress","streetAddress":"80 Broad Street, 5th Floor","addressLocality":"New York","addressRegion":"NY","postalCode":"10004","addressCountry":"US"},"areaServed":"Worldwide"}</script>''' % (SITE, SITE, EMAIL)

def page_hero(crumb, eyebrow, h1, text):
    return f'''
<section class="page-hero">
  <div class="bg-grid"></div><div class="orb orb--1"></div><div class="orb orb--2"></div>
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>{crumb}</span></nav>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p>{text}</p>
  </div>
</section>'''

# ================= HOME =================
home = f'''
<section class="hero">
  <div class="bg-grid"></div><div class="orb orb--1"></div><div class="orb orb--2"></div><div class="orb orb--3"></div>
  <div class="container hero__inner">
    <div>
      <span class="eyebrow reveal">Digital agency · New York</span>
      <h1 class="reveal" data-delay="1">We build websites that <span class="grad-text">grow your business.</span></h1>
      <p class="hero__lead reveal" data-delay="2">Webratron is a hub of custom website design. We create websites, Shopify stores, mobile apps, logos and animated videos for startups and growing businesses.</p>
      <div class="hero__actions reveal" data-delay="3">
        <a href="contact.html" class="btn btn--primary">Get a free quote {ARROW}</a>
        <a href="portfolio.html" class="btn btn--ghost">View our work</a>
      </div>
      <div class="hero__trust reveal" data-delay="3">
        <a href="{TRUSTPILOT}" target="_blank" rel="noopener"><small><span class="stars">★★★★★</span><br>Rated 4.7/5 on Trustpilot · 5.0 on ProvenExpert</small></a>
      </div>
    </div>
    <div class="hero__visual reveal" data-delay="2" aria-hidden="true">
      <div class="mock mock--browser">
        <div class="mock__bar"><i></i><i></i><i></i></div>
        <div class="mock__body">
          <div class="sk sk--title"></div><div class="sk sk--w80"></div><div class="sk sk--w60"></div>
          <div class="mock__cards"><div></div><div></div><div></div></div>
          <div class="sk sk--w40"></div>
        </div>
      </div>
      <div class="mock mock--phone"><div class="notch"></div><div class="ph-hero"></div><div class="sk" style="margin-bottom:8px"></div><div class="sk sk--w60"></div></div>
      <div class="mock mock--chip"><span class="dot">{icon("check")}</span><div><strong>4.7 ★</strong><small>Trustpilot rating</small></div></div>
    </div>
  </div>
</section>

<section class="logos" aria-label="Technologies we work with">
  <p>Technologies we master</p>
  <div class="marquee" aria-hidden="true">
    <span>WordPress</span><span>Shopify</span><span>React</span><span>Next.js</span><span>Flutter</span><span>PHP</span><span>Laravel</span><span>Figma</span><span>WooCommerce</span><span>Adobe</span>
    <span>WordPress</span><span>Shopify</span><span>React</span><span>Next.js</span><span>Flutter</span><span>PHP</span><span>Laravel</span><span>Figma</span><span>WooCommerce</span><span>Adobe</span>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">What we do</span>
      <h2 class="reveal">Everything you need to <span class="grad-text">win online</span></h2>
      <p class="reveal">From your first logo to a full-scale web platform — one team, one vision, end-to-end.</p>
    </div>
    <div class="grid grid--4">
{service_cards()}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container split">
    <div>
      <span class="eyebrow reveal">Why Webratron</span>
      <h2 class="reveal">Design that impresses. <span class="grad-text">Code that performs.</span></h2>
      <p class="reveal">We combine creative design with solid engineering so your website doesn't just look great — it loads fast, ranks well and turns visitors into customers.</p>
      <ul class="checklist reveal">
        <li>100% custom design — no cookie-cutter templates</li>
        <li>Mobile-first, lightning-fast and SEO-optimised</li>
        <li>Unlimited revisions on logo design</li>
        <li>100% ownership rights to your unique design</li>
        <li>Money-back guarantee on eligible packages</li>
      </ul>
      <a href="about.html" class="btn btn--ghost reveal">More about us {ARROW}</a>
    </div>
    <div class="visual-panel reveal" data-delay="1" aria-hidden="true">
      <div class="bg-grid"></div>
      <div class="code-card">
<span class="c">// webratron.config.js</span><br>
<span class="k">export default</span> {{<br>
&nbsp;&nbsp;design: <span class="s">"pixel-perfect"</span>,<br>
&nbsp;&nbsp;performance: <span class="f">100</span>,<br>
&nbsp;&nbsp;seo: <span class="s">"optimised"</span>,<br>
&nbsp;&nbsp;responsive: <span class="k">true</span>,<br>
&nbsp;&nbsp;goal: <span class="s">"grow your business"</span><br>
}};
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="stats">
      <div class="stat reveal"><strong class="grad-text">4.7★</strong><span>Trustpilot rating</span></div>
      <div class="stat reveal" data-delay="1"><strong class="grad-text">5.0★</strong><span>ProvenExpert score</span></div>
      <div class="stat reveal" data-delay="2"><strong class="grad-text" data-count="8" data-suffix="">8</strong><span>Logo concepts per project</span></div>
      <div class="stat reveal" data-delay="3"><strong class="grad-text">100%</strong><span>Design ownership</span></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">What we create</span>
      <h2 class="reveal">Work across <span class="grad-text">every channel</span></h2>
      <p class="reveal">Websites, apps, logos and videos — everything your brand needs, under one roof.</p>
    </div>
    <div class="grid grid--3">
{work_cards(3)}
    </div>
    <div class="text-center" style="margin-top:44px"><a href="portfolio.html" class="btn btn--ghost">Explore our work {ARROW}</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">How we work</span>
      <h2 class="reveal">A simple, proven <span class="grad-text">process</span></h2>
      <p class="reveal">Clear steps, no surprises — you're involved and informed from day one.</p>
    </div>
    <div class="process">
{process()}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">Testimonials</span>
      <h2 class="reveal">What our clients <span class="grad-text">say</span></h2>
      <p class="reveal">From our reviews on <a href="{TRUSTPILOT}" target="_blank" rel="noopener" class="grad-text" style="font-weight:600">Trustpilot</a> — rated 4.7 out of 5.</p>
    </div>
    <div class="grid grid--3">
{testimonials()}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">FAQ</span>
      <h2 class="reveal">Questions? <span class="grad-text">Answered.</span></h2>
    </div>
    <div class="faq">
{faqs(4)}
    </div>
  </div>
</section>
{cta()}
'''
page("index.html", "Webratron — Website Design, Development & Digital Agency",
     "Webratron is a full-service digital agency building custom websites, mobile apps, brands and SEO strategies that help businesses grow.",
     home, "index.html", ORG_SCHEMA)

# ================= SERVICES =================
DETAILS = {
 "web-design": ["Custom UI/UX design in Figma", "Landing pages & multi-page sites", "Conversion-focused layouts", "Interactive prototypes"],
 "development": ["WordPress & headless CMS", "React / Next.js web apps", "API & third-party integrations", "Speed & Core Web Vitals optimisation"],
 "mobile": ["Flutter & React Native apps", "iOS & Android store publishing", "Backend, auth & push notifications", "App UI/UX design"],
 "branding": ["8 unique logo concepts", "Unlimited revisions", "2 dedicated designers", "Mascot logos & stationery design"],
 "ecommerce": ["Shopify & WooCommerce stores", "Payment gateway setup", "Product, inventory & shipping", "Conversion rate optimisation"],
 "seo": ["Technical & on-page SEO", "Local SEO & Google Business", "Content marketing", "Social media marketing"],
 "video": ["Whiteboard animation", "2D explainer videos", "2D brand intros", "30 to 120-second videos"],
 "maintenance": ["Plugin, theme & core updates", "Bug fixes & troubleshooting", "Security hardening", "Content updates on request"],
}
blocks = []
for i, (sid, ic, name, text, tags) in enumerate(SERVICES):
    rev = " split--reverse" if i % 2 else ""
    alt = " section--alt" if i % 2 else ""
    lis = "".join(f"<li>{d}</li>" for d in DETAILS[sid])
    art = f"art--{(i % 6) + 1}"
    blocks.append(f'''
<section class="section{alt}" id="{sid}">
  <div class="container split{rev}">
    <div>
      <div class="icon reveal">{icon(ic)}</div>
      <h2 class="reveal">{name}</h2>
      <p class="reveal">{text}</p>
      <ul class="checklist reveal">{lis}</ul>
      <a href="contact.html?service={sid}" class="btn btn--primary reveal">Start your project {ARROW}</a>
    </div>
    <div class="visual-panel reveal" data-delay="1" aria-hidden="true">
      <div class="art {art}" style="position:absolute;inset:0;opacity:.35"></div>
      <div class="bg-grid"></div>
      <div class="icon" style="position:relative;z-index:1;width:120px;height:120px;border-radius:32px;margin:0"><span style="width:56px;height:56px;display:block">{icon(ic)}</span></div>
    </div>
  </div>
</section>''')
services = page_hero("Services", "Our services", 'Digital services that <span class="grad-text">drive results</span>',
    "Strategy, design, development and growth — everything your brand needs online, delivered by one dedicated team.") + f'''
<section class="section" style="padding-top:20px">
  <div class="container">
    <div class="grid grid--4">
{service_cards()}
    </div>
  </div>
</section>''' + "".join(blocks) + f'''
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">Our process</span>
      <h2 class="reveal">From idea to <span class="grad-text">launch</span></h2>
    </div>
    <div class="process">
{process()}
    </div>
  </div>
</section>''' + cta()
page("services.html", "Services — Web Design, Development, Apps & SEO | Webratron",
     "Explore Webratron's services: website design, web development, mobile apps, logo & branding, e-commerce, SEO, animation videos and website maintenance.",
     services, "services.html")

# ================= PORTFOLIO =================
portfolio = page_hero("Work", "Portfolio", 'Work that <span class="grad-text">speaks for itself</span>',
    "Websites, apps, logos and videos — explore the kinds of projects we build for our clients.") + f'''
<section class="section" style="padding-top:20px">
  <div class="container">
    <div class="filters" role="group" aria-label="Filter projects">
      <button class="filter is-active" data-filter="all" aria-pressed="true">All</button>
      <button class="filter" data-filter="web" aria-pressed="false">Websites</button>
      <button class="filter" data-filter="mobile" aria-pressed="false">Mobile Apps</button>
      <button class="filter" data-filter="ecommerce" aria-pressed="false">E-commerce</button>
      <button class="filter" data-filter="branding" aria-pressed="false">Branding</button>
      <button class="filter" data-filter="video" aria-pressed="false">Video</button>
    </div>
    <div class="grid grid--3">
{work_cards()}
    </div>
  </div>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">Client love</span>
      <h2 class="reveal">Results our clients <span class="grad-text">talk about</span></h2>
      <p class="reveal">Read all our reviews on <a href="{TRUSTPILOT}" target="_blank" rel="noopener" class="grad-text" style="font-weight:600">Trustpilot</a>.</p>
    </div>
    <div class="grid grid--3">
{testimonials()}
    </div>
  </div>
</section>''' + cta("Your project could be next.", "Let's create something you're proud to show the world.")
page("portfolio.html", "Portfolio — Our Work | Webratron",
     "See websites, mobile apps, e-commerce stores, brand identities and animation videos designed and built by Webratron.",
     portfolio, "portfolio.html")

# ================= ABOUT =================
VALUES = [("target", "Results-driven", "Every pixel and line of code serves one purpose: growing your business."),
          ("users", "Client-first", "Honest advice, clear communication and a partnership that lasts beyond launch."),
          ("bolt", "Fast & reliable", "Agile workflows and clear milestones mean we deliver on time, every time."),
          ("heart", "Crafted with care", "We sweat the details so your brand looks and feels premium everywhere.")]
TEAM = [("DS", "Design Team", "Web, UI/UX & Logo Design", "#7c5cff"), ("DV", "Development Team", "Web, Shopify & Mobile Apps", "#00a8cc"),
        ("AN", "Animation Team", "Whiteboard & 2D Video", "#d63fb5"), ("GM", "Growth Team", "SEO & Social Media", "#1fae78")]
vals = "\n".join(f'      <article class="card reveal" data-delay="{i}"><div class="icon">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></article>' for i, (ic, t, d) in enumerate(VALUES))
team = "\n".join(f'      <article class="card member reveal" data-delay="{i}"><div class="avatar-lg" style="background:{c}">{ini}</div><h3>{n}</h3><span>{r}</span></article>' for i, (ini, n, r, c) in enumerate(TEAM))
about = page_hero("About", "About Webratron", 'We turn ideas into <span class="grad-text">digital growth</span>',
    "Designers, developers, animators and marketers helping businesses stand out and grow online.") + f'''
<section class="section" style="padding-top:20px">
  <div class="container split">
    <div>
      <span class="eyebrow reveal">Our story</span>
      <h2 class="reveal">Built for businesses that <span class="grad-text">aim higher</span></h2>
      <p class="reveal">Webratron is a hub of custom website design, built on a simple belief: every business deserves a website and brand that work as hard as they do.</p>
      <p class="reveal">From our office at 80 Broad Street in New York, we design and develop websites, Shopify stores, mobile apps, logos and animated videos — and help clients get found through SEO and social media marketing.</p>
      <a href="contact.html" class="btn btn--primary reveal">Work with us {ARROW}</a>
    </div>
    <div class="stats reveal" data-delay="1" style="grid-template-columns:repeat(2,1fr)">
      <div class="stat"><strong class="grad-text">4.7★</strong><span>Trustpilot rating</span></div>
      <div class="stat"><strong class="grad-text">5.0★</strong><span>ProvenExpert score</span></div>
      <div class="stat"><strong class="grad-text" data-count="8" data-suffix="">8</strong><span>Core services</span></div>
      <div class="stat"><strong class="grad-text">NYC</strong><span>Headquarters</span></div>
    </div>
  </div>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">Our values</span>
      <h2 class="reveal">What we <span class="grad-text">stand for</span></h2>
    </div>
    <div class="grid grid--4">
{vals}
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">Our team</span>
      <h2 class="reveal">The people behind <span class="grad-text">Webratron</span></h2>
      <p class="reveal">Specialists in design, engineering and growth — working together as one team for you.</p>
    </div>
    <div class="grid grid--4">
{team}
    </div>
  </div>
</section>''' + cta()
page("about.html", "About Us | Webratron Digital Agency",
     "Learn about Webratron — a New York-based digital agency of designers, developers and marketers helping businesses grow online.",
     about, "about.html")

# ================= PRICING =================
PLANS = [
 ("starter", "Startup Website", "$469", "$938", "A clean, professional website to get your business online.", ["3-page website", "5 stock images", "3 banner designs", "1 jQuery slider banner", "Contact form", "Social media integration", "Mobile responsive", "100% ownership rights"], False),
 ("growth", "Professional Website", "$1,269", "$2,938", "A complete website for growing businesses.", ["10-page website", "15 premium stock images", "5 banner designs", "CMS / admin panel", "Contact form", "Mobile responsive", "100% ownership rights", "Money-back guarantee"], True),
 ("enterprise", "Web Portal", "$5,499", "$10,998", "A fully custom web portal for established businesses.", ["Custom design & development", "Content management system", "Dedicated project manager", "Mobile responsive", "100% ownership rights", "Money-back guarantee"], False),
]
plans = []
for i, (pid, name, price, was, desc, feats, featured) in enumerate(PLANS):
    badge = '<span class="plan__badge">Recommended</span>' if featured else ""
    cls = " plan--featured" if featured else ""
    btn = "btn--primary" if featured else "btn--ghost"
    lis = "".join(f"<li>{f}</li>" for f in feats)
    plans.append(f'''      <article class="card plan{cls} reveal" data-delay="{i}">
        {badge}
        <h3>{name}</h3>
        <p>{desc}</p>
        <div class="plan__price">{price} <small><s>{was}</s></small></div>
        <ul class="checklist">{lis}</ul>
        <a href="contact.html?plan={pid}" class="btn {btn} btn--block">Get started</a>
      </article>''')
ADDONS = [("brand", "Logo Design", "from $149"), ("video", "Video Animation", "from $499"), ("cart", "Shopify Store", "from $99"),
          ("seo", "SEO Packages", "from $3,500"), ("mobile", "Mobile App", "custom quote"), ("shield", "Website Maintenance", "custom quote")]
addons = "\n".join(f'      <article class="card reveal" data-delay="{i % 3}" style="display:flex;gap:18px;align-items:center;padding:24px"><div class="icon" style="margin:0;flex:0 0 56px">{icon(ic)}</div><div><h3 style="margin:0 0 2px;font-size:1.1rem">{n}</h3><p style="margin:0;color:var(--primary-2);font-weight:600">{p}</p></div></article>' for i, (ic, n, p) in enumerate(ADDONS))
pricing = page_hero("Pricing", "Pricing", 'Simple, <span class="grad-text">transparent</span> pricing',
    "Website packages for every stage of business, with full ownership of your design.") + f'''
<section class="section" style="padding-top:20px">
  <div class="container">
    <div class="grid grid--3 pricing">
{chr(10).join(plans)}
    </div>
    <p class="text-center" style="margin-top:32px;font-size:.95rem">Prices in USD. E-commerce, Shopify and other website packages are also available. Need something different? <a href="contact.html" class="grad-text" style="font-weight:600">Request a custom quote</a>.</p>
  </div>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">Add-ons</span>
      <h2 class="reveal">More <span class="grad-text">services</span></h2>
    </div>
    <div class="grid grid--3">
{addons}
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">FAQ</span>
      <h2 class="reveal">Frequently asked <span class="grad-text">questions</span></h2>
    </div>
    <div class="faq">
{faqs()}
    </div>
  </div>
</section>''' + cta()
page("pricing.html", "Pricing — Website & App Packages | Webratron",
     "Transparent website design and development packages from Webratron. Starter, Business and E-commerce plans plus add-ons for branding, apps, SEO and maintenance.",
     pricing, "pricing.html", faq_schema())

# ================= CONTACT =================
chips = "".join(f'<label><input type="checkbox" name="services" value="{sid}"><span>{name}</span></label>' for sid, ic, name, t, tg in SERVICES)
contact = page_hero("Contact", "Contact us", "Let's build something <span class=\"grad-text\">great together</span>",
    "Tell us about your project and we'll get back to you with ideas and a free quote.") + f'''
<section class="section" style="padding-top:20px">
  <div class="container contact-grid">
    <div class="contact-info">
      <div class="contact-item reveal"><div class="icon">{icon("mail")}</div><div><strong>Email us</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
      <div class="contact-item reveal" data-delay="1"><div class="icon">{icon("pin")}</div><div><strong>Visit us</strong><span>{ADDRESS}</span></div></div>
      <div class="contact-item reveal" data-delay="2"><div class="icon">{icon("phone")}</div><div><strong>Call us</strong><a href="tel:{PHONE_TEL}">{PHONE}</a></div></div>
      <div class="card reveal" data-delay="3" style="padding:26px">
        <h3 style="font-size:1.1rem">What happens next?</h3>
        <ul class="checklist" style="margin:12px 0 0">
          <li>Our team reviews your project brief</li>
          <li>Free discovery call to understand your goals</li>
          <li>You receive a clear proposal &amp; fixed quote</li>
        </ul>
      </div>
    </div>
    <div class="form reveal" data-delay="1">
      <!-- To receive messages directly, set data-endpoint to a form service URL (e.g. Formspree). Without it, the form opens the visitor's email app. -->
      <form novalidate data-endpoint="" data-email="{EMAIL}">
        <div class="form__row">
          <div class="field"><label for="name">Full name *</label><input id="name" name="name" type="text" autocomplete="name" required><span class="error">Please enter your name.</span></div>
          <div class="field"><label for="email">Email *</label><input id="email" name="email" type="email" autocomplete="email" required><span class="error">Please enter a valid email.</span></div>
        </div>
        <div class="form__row">
          <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field"><label for="budget">Budget</label>
            <select id="budget" name="budget">
              <option value="">Select a range</option>
              <option value="<1k">Under $1,000</option>
              <option value="1k-3k">$1,000 – $3,000</option>
              <option value="3k-8k">$3,000 – $8,000</option>
              <option value="8k+">$8,000+</option>
            </select>
          </div>
        </div>
        <div class="field"><span style="font-size:.9rem;font-weight:600">I'm interested in</span><div class="chips">{chips}</div></div>
        <div class="field"><label for="message">Project details *</label><textarea id="message" name="message" placeholder="Tell us about your business, goals and timeline…" required></textarea><span class="error">Please tell us a little about your project.</span></div>
        <div style="position:absolute;left:-9999px" aria-hidden="true"><input type="text" name="company_website" tabindex="-1" autocomplete="off"></div>
        <button type="submit" class="btn btn--primary btn--block">Send message {ARROW}</button>
        <p class="form__note">We respect your privacy. Your details are never shared.</p>
      </form>
      <div class="form-success" role="status">
        <div class="icon">{icon("check")}</div>
        <h3>Thank you!</h3>
        <p>Your message is on its way. We'll get back to you soon.</p>
      </div>
    </div>
  </div>
</section>'''
page("contact.html", "Contact Us — Get a Free Quote | Webratron",
     "Contact Webratron for a free consultation and quote on your website, mobile app, branding or SEO project.",
     contact, "contact.html")

# ================= LEGAL =================
privacy = page_hero("Privacy Policy", "Legal", "Privacy Policy", "How we collect, use and protect your information.") + f'''
<section class="section" style="padding-top:20px">
  <div class="container prose">
    <p><em>Last updated: November 2026</em></p>
    <h2>Information we collect</h2>
    <p>When you contact us through our website, we collect the information you provide such as your name, email address, phone number, budget and project details. We may also collect anonymous usage data (such as pages visited) to improve our website.</p>
    <h2>How we use your information</h2>
    <ul><li>To respond to your enquiries and provide quotes</li><li>To deliver and support the services you request</li><li>To improve our website and services</li></ul>
    <h2>Sharing</h2>
    <p>We do not sell or rent your personal information. We only share it with trusted service providers who help us operate our business, under confidentiality obligations.</p>
    <h2>Your rights</h2>
    <p>You may request access to, correction of, or deletion of your personal data at any time by emailing <a href="mailto:{EMAIL}" class="grad-text">{EMAIL}</a>.</p>
    <h2>Contact</h2>
    <p>Webratron, {ADDRESS}.</p>
  </div>
</section>'''
page("privacy.html", "Privacy Policy | Webratron", "Webratron privacy policy.", privacy)

terms = page_hero("Terms of Service", "Legal", "Terms of Service", "The terms that govern our work together.") + f'''
<section class="section" style="padding-top:20px">
  <div class="container prose">
    <p><em>Last updated: November 2026</em></p>
    <h2>Projects &amp; proposals</h2>
    <p>Each project is defined by a written proposal outlining scope, deliverables, timeline and fees. Work begins once the proposal is accepted and the initial payment is received.</p>
    <h2>Payments</h2>
    <p>Unless otherwise agreed, projects are billed in milestones. Final files and website launch are released upon full payment.</p>
    <h2>Revisions</h2>
    <p>Revision rounds are included as described in your package. Requests outside the agreed scope may be quoted separately.</p>
    <h2>Ownership</h2>
    <p>Upon full payment, you own the final designs and website content created for you. Third-party assets (fonts, plugins, stock media) remain subject to their own licences.</p>
    <h2>Refunds</h2>
    <p>Refund eligibility depends on your package. Packages that include a money-back guarantee are refunded according to the conditions stated in your package details. Contact us with any refund questions.</p>
    <h2>Contact</h2>
    <p>Questions about these terms? Email <a href="mailto:{EMAIL}" class="grad-text">{EMAIL}</a>.</p>
  </div>
</section>'''
page("terms.html", "Terms of Service | Webratron", "Webratron terms of service.", terms)

# ================= 404 =================
nf = f'''
<section class="notfound">
  <div class="bg-grid"></div><div class="orb orb--1"></div><div class="orb orb--2"></div>
  <div style="position:relative;z-index:1">
    <h1 class="grad-text">404</h1>
    <h2>This page got lost in cyberspace.</h2>
    <p>The page you're looking for doesn't exist or has moved.</p>
    <a href="index.html" class="btn btn--primary">Back to home {ARROW}</a>
  </div>
</section>'''
page("404.html", "Page not found | Webratron", "The page you are looking for could not be found.", nf)
print("built")
