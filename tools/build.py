import os, textwrap
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://webratron.com"
EMAIL = "support@webratron.com"
PHONE = "(917) 924-6809"
PHONE_TEL = "+19179246809"
PHONE2 = "(864) 671-0341"
PHONE2_TEL = "+18646710341"
AU_ADDRESS = "308 Sussex St, Sydney NSW 2000, Australia"
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
 "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/>',
 "chev": '<path d="m6 9 6 6 6-6"/>',
 "help": '<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>',
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

NAV = [("index.html", "Home"), ("about.html", "About"), ("portfolio.html", "Portfolio"), ("services.html", "Services"), ("blog.html", "Blogs"), ("pricing.html", "Pricing"), ("contact.html", "Contact")]

def header(active):
    lis = []
    for h, t in NAV:
        cur = ' aria-current="page"' if h == active else ""
        if h == "services.html":
            dd = "".join(f'<li><a href="services.html#{sid}"><span class="dd__icon">{icon(ic)}</span>{name}</a></li>' for sid, ic, name, _, _ in SERVICES)
            lis.append(f'        <li class="has-dd"><a href="{h}"{cur}>{t} <span class="caret">{icon("chev")}</span></a>\n          <ul class="dropdown">{dd}</ul></li>')
        else:
            lis.append(f'        <li><a href="{h}"{cur}>{t}</a></li>')
    links = "\n".join(lis)
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container topbar">
    <a href="index.html" class="brand" aria-label="Webratron home"><img src="assets/img/logo-light.png" alt="Webratron" width="320" height="56"></a>
    <a href="contact.html" class="topbar__offer">{icon("chat")}<span>Chat to avail <strong>50% off</strong></span></a>
    <a href="contact.html" class="btn btn--quote">Get a Quote</a>
    <a href="mailto:{EMAIL}" class="topbar__mail">{icon("mail")}<span>{EMAIL}</span></a>
    <div class="topbar__phones"><a href="tel:{PHONE_TEL}">{PHONE}</a><a href="tel:{PHONE2_TEL}">{PHONE2}</a></div>
    <button class="nav__toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links"><span></span></button>
  </div>
  <div class="navrow">
    <div class="container">
      <nav aria-label="Primary">
        <ul class="nav__links" id="nav-links">
{links}
          <li class="nav__mobile-cta">
            <a href="contact.html" class="btn btn--primary btn--block">Get a Quote</a>
            <p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="tel:{PHONE2_TEL}">{PHONE2}</a></p>
          </li>
        </ul>
      </nav>
      <a href="contact.html" class="navrow__offer"><span class="pulse"></span>Limited offer: <strong>50% off</strong> — chat now</a>
    </div>
  </div>
</header>"""

def footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer__top">
      <div class="footer__brand">
        <a href="index.html" aria-label="Webratron home"><img src="assets/img/logo-dark.png" alt="Webratron" width="320" height="56" class="footer__logo"></a>
        <p>Webratron is a results-driven web development company focused on building high-performance digital experiences. We create custom websites that not only look exceptional but also help businesses grow, engage, and convert.</p>
        <img src="assets/img/pay.webp" alt="We accept PayPal, Mastercard, Visa and American Express" width="340" height="53" class="footer__pay" loading="lazy">
      </div>
      <div class="footer__badges">
        <img src="assets/img/badges.webp" alt="Top 10 ranked, Verified by 10Best, DesignRush accredited agency, Appfutura top web design company, GoodFirms, Trustpilot, Google reviews, McAfee Secure, DMCA protected" width="755" height="200" loading="lazy">
      </div>
    </div>
    <div class="footer__links">
      <div><h4>Quick Links</h4><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="portfolio.html">Portfolio</a></li><li><a href="blog.html">Blogs</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div><h4>Services</h4><ul>{"".join(f'<li><a href="services.html#{sid}">{name}</a></li>' for sid, ic, name, _, _ in SERVICES)}</ul></div>
    </div>
    <div class="footer__locations">
      <h3>Our Locations</h3>
      <div class="loc-grid">
        <div><h4>USA Address:</h4><p>80 Broad St 5th floor, New York, NY 10004, United States</p></div>
        <div><h4>AU Address:</h4><p>{AU_ADDRESS}</p></div>
        <div><h4>Email:</h4><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><h4>Phone:</h4><p><a href="tel:{PHONE_TEL}">{PHONE}</a></p></div>
      </div>
    </div>
  </div>
  <div class="footer__bar">
    <div class="container">
      <span>&copy; Webratron <span data-year>2026</span>. All Rights Reserved</span>
      <nav aria-label="Legal"><a href="terms.html">Terms &amp; Condition</a><a href="privacy.html">Privacy Policy</a></nav>
    </div>
  </div>
</footer>
<a href="contact.html" class="help-btn">{icon("help")}<span>Help</span></a>"""

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
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
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
  <div class="starfield"></div><div class="orb orb--1"></div><div class="orb orb--2"></div>
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>{crumb}</span></nav>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p>{text}</p>
  </div>
</section>'''

PLATFORMS = '<span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#7AB55C"><path d="M15.337 23.979l7.216-1.561s-2.604-17.613-2.625-17.73c-.018-.116-.114-.192-.211-.192s-1.929-.136-1.929-.136-1.275-1.274-1.439-1.411c-.045-.037-.075-.057-.121-.074l-.914 21.104h.023zM11.71 11.305s-.81-.424-1.774-.424c-1.447 0-1.504.906-1.504 1.141 0 1.232 3.24 1.715 3.24 4.629 0 2.295-1.44 3.76-3.406 3.76-2.354 0-3.54-1.465-3.54-1.465l.646-2.086s1.245 1.066 2.28 1.066c.675 0 .975-.545.975-.932 0-1.619-2.654-1.694-2.654-4.359-.034-2.237 1.571-4.416 4.827-4.416 1.257 0 1.875.361 1.875.361l-.945 2.715-.02.01zM11.17.83c.136 0 .271.038.405.135-.984.465-2.064 1.639-2.508 3.992-.656.213-1.293.405-1.889.578C7.697 3.75 8.951.84 11.17.84V.83zm1.235 2.949v.135c-.754.232-1.583.484-2.394.736.466-1.777 1.333-2.645 2.085-2.971.193.501.309 1.176.309 2.1zm.539-2.234c.694.074 1.141.867 1.429 1.755-.349.114-.735.231-1.158.366v-.252c0-.752-.096-1.371-.271-1.871v.002zm2.992 1.289c-.02 0-.06.021-.078.021s-.289.075-.714.21c-.423-1.233-1.176-2.37-2.508-2.37h-.115C12.135.209 11.669 0 11.265 0 8.159 0 6.675 3.877 6.21 5.846c-1.194.365-2.063.636-2.16.674-.675.213-.694.232-.772.87-.075.462-1.83 14.063-1.83 14.063L15.009 24l.927-21.166z"/></svg><b style="color:#7AB55C">Shopify</b></span><span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#1BDBDB"><path d="M20.702 2.29c-2.494-1.554-5.778-1.187-8.706.654C9.076 1.104 5.79.736 3.3 2.29c-3.941 2.463-4.42 8.806-1.07 14.167 2.47 3.954 6.333 6.269 9.77 6.226 3.439.043 7.301-2.273 9.771-6.226 3.347-5.361 2.872-11.704-1.069-14.167zM4.042 15.328a12.838 12.838 0 01-1.546-3.541 10.12 10.12 0 01-.336-3.338c.15-1.98.956-3.524 2.27-4.345 1.315-.822 3.052-.87 4.903-.137.281.113.556.24.825.382A15.11 15.11 0 007.5 7.54c-2.035 3.255-2.655 6.878-1.945 9.765a13.247 13.247 0 01-1.514-1.98zm17.465-3.541a12.866 12.866 0 01-1.547 3.54 13.25 13.25 0 01-1.513 1.984c.635-2.589.203-5.76-1.353-8.734a.39.39 0 00-.563-.153l-4.852 3.032a.397.397 0 00-.126.546l.712 1.139a.395.395 0 00.547.126l3.145-1.965c.101.306.203.606.28.916.296 1.086.41 2.214.335 3.337-.15 1.982-.956 3.525-2.27 4.347a4.437 4.437 0 01-2.25.65h-.101a4.432 4.432 0 01-2.25-.65c-1.314-.822-2.121-2.365-2.27-4.347-.074-1.123.039-2.251.335-3.337a13.212 13.212 0 014.05-6.482 10.148 10.148 0 012.849-1.765c1.845-.733 3.586-.685 4.9.137 1.316.822 2.122 2.365 2.271 4.345a10.146 10.146 0 01-.33 3.334z"/></svg><b style="color:#1BDBDB">GoDaddy</b></span><span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#FF9900"><path d="M.045 18.02c.072-.116.187-.124.348-.022 3.636 2.11 7.594 3.166 11.87 3.166 2.852 0 5.668-.533 8.447-1.595l.315-.14c.138-.06.234-.1.293-.13.226-.088.39-.046.525.13.12.174.09.336-.12.48-.256.19-.6.41-1.006.654-1.244.743-2.64 1.316-4.185 1.726a17.617 17.617 0 01-10.951-.577 17.88 17.88 0 01-5.43-3.35c-.1-.074-.151-.15-.151-.22 0-.047.021-.09.051-.13zm6.565-6.218c0-1.005.247-1.863.743-2.577.495-.71 1.17-1.25 2.04-1.615.796-.335 1.756-.575 2.912-.72.39-.046 1.033-.103 1.92-.174v-.37c0-.93-.105-1.558-.3-1.875-.302-.43-.78-.65-1.44-.65h-.182c-.48.046-.896.196-1.246.46-.35.27-.575.63-.675 1.096-.06.3-.206.465-.435.51l-2.52-.315c-.248-.06-.372-.18-.372-.39 0-.046.007-.09.022-.15.247-1.29.855-2.25 1.82-2.88.976-.616 2.1-.975 3.39-1.05h.54c1.65 0 2.957.434 3.888 1.29.135.15.27.3.405.48.12.165.224.314.283.45.075.134.15.33.195.57.06.254.105.42.135.51.03.104.062.3.076.615.01.313.02.493.02.553v5.28c0 .376.06.72.165 1.036.105.313.21.54.315.674l.51.674c.09.136.136.256.136.36 0 .12-.06.226-.18.314-1.2 1.05-1.86 1.62-1.963 1.71-.165.135-.375.15-.63.045a6.062 6.062 0 01-.526-.496l-.31-.347a9.391 9.391 0 01-.317-.42l-.3-.435c-.81.886-1.603 1.44-2.4 1.665-.494.15-1.093.227-1.83.227-1.11 0-2.04-.343-2.76-1.034-.72-.69-1.08-1.665-1.08-2.94l-.05-.076zm3.753-.438c0 .566.14 1.02.425 1.364.285.34.675.512 1.155.512.045 0 .106-.007.195-.02.09-.016.134-.023.166-.023.614-.16 1.08-.553 1.424-1.178.165-.28.285-.58.36-.91.09-.32.12-.59.135-.8.015-.195.015-.54.015-1.005v-.54c-.84 0-1.484.06-1.92.18-1.275.36-1.92 1.17-1.92 2.43l-.035-.02zm9.162 7.027c.03-.06.075-.11.132-.17.362-.243.714-.41 1.05-.5a8.094 8.094 0 011.612-.24c.14-.012.28 0 .41.03.65.06 1.05.168 1.172.33.063.09.099.228.099.39v.15c0 .51-.149 1.11-.424 1.8-.278.69-.664 1.248-1.156 1.68-.073.06-.14.09-.197.09-.03 0-.06 0-.09-.012-.09-.044-.107-.12-.064-.24.54-1.26.806-2.143.806-2.64 0-.15-.03-.27-.087-.344-.145-.166-.55-.257-1.224-.257-.243 0-.533.016-.87.046-.363.045-.7.09-1 .135-.09 0-.148-.014-.18-.044-.03-.03-.036-.047-.02-.077 0-.017.006-.03.02-.063v-.06z"/></svg><b style="color:#FF9900">Amazon</b></span><span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#21759B"><path d="M21.469 6.825c.84 1.537 1.318 3.3 1.318 5.175 0 3.979-2.156 7.456-5.363 9.325l3.295-9.527c.615-1.54.82-2.771.82-3.864 0-.405-.026-.78-.07-1.11m-7.981.105c.647-.03 1.232-.105 1.232-.105.582-.075.514-.93-.067-.899 0 0-1.755.135-2.88.135-1.064 0-2.85-.15-2.85-.15-.585-.03-.661.855-.075.885 0 0 .54.061 1.125.09l1.68 4.605-2.37 7.08L5.354 6.9c.649-.03 1.234-.1 1.234-.1.585-.075.516-.93-.065-.896 0 0-1.746.138-2.874.138-.2 0-.438-.008-.69-.015C4.911 3.15 8.235 1.215 12 1.215c2.809 0 5.365 1.072 7.286 2.833-.046-.003-.091-.009-.141-.009-1.06 0-1.812.923-1.812 1.914 0 .89.513 1.643 1.06 2.531.411.72.89 1.643.89 2.977 0 .915-.354 1.994-.821 3.479l-1.075 3.585-3.9-11.61.001.014zM12 22.784c-1.059 0-2.081-.153-3.048-.437l3.237-9.406 3.315 9.087c.024.053.05.101.078.149-1.12.393-2.325.609-3.582.609M1.211 12c0-1.564.336-3.05.935-4.39L7.29 21.709C3.694 19.96 1.212 16.271 1.211 12M12 0C5.385 0 0 5.385 0 12s5.385 12 12 12 12-5.385 12-12S18.615 0 12 0"/></svg><b style="color:#21759B">WordPress</b></span><span class="platform platform--wide" aria-label="Wix"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#0C6EFC"><path d="m0 7.354 2.113 9.292h.801a1.54 1.54 0 0 0 1.506-1.218l1.351-6.34a.171.171 0 0 1 .167-.137c.08 0 .15.058.167.137l1.352 6.34a1.54 1.54 0 0 0 1.506 1.218h.805l2.113-9.292h-.565c-.62 0-1.159.43-1.296 1.035l-1.26 5.545-1.106-5.176a1.76 1.76 0 0 0-2.19-1.324c-.639.176-1.113.716-1.251 1.365l-1.094 5.127-1.26-5.537A1.33 1.33 0 0 0 .563 7.354H0zm13.992 0a.951.951 0 0 0-.951.95v8.342h.635a.952.952 0 0 0 .951-.95V7.353h-.635zm1.778 0 3.158 4.66-3.14 4.632h1.325c.368 0 .712-.181.918-.486l1.756-2.59a.12.12 0 0 1 .197 0l1.754 2.59c.206.305.55.486.918.486h1.326l-3.14-4.632L24 7.354h-1.326c-.368 0-.712.181-.918.486l-1.772 2.617a.12.12 0 0 1-.197 0L18.014 7.84a1.108 1.108 0 0 0-.918-.486H15.77z"/></svg></span><span class="platform platform--img"><img src="assets/img/weebly.png" alt="Weebly" width="90" height="70"></span><span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#111111"><path d="M22.655 8.719c-1.802-1.801-4.726-1.801-6.564 0l-7.351 7.35c-.45.45-.45 1.2 0 1.65.45.449 1.2.449 1.65 0l7.351-7.351c.899-.899 2.362-.899 3.264 0 .9.9.9 2.364 0 3.264l-7.239 7.239c.9.899 2.362.899 3.263 0l5.589-5.589c1.836-1.838 1.836-4.763.037-6.563zm-2.475 2.437c-.451-.45-1.201-.45-1.65 0l-7.354 7.389c-.9.899-2.361.899-3.262 0-.45-.45-1.2-.45-1.65 0s-.45 1.2 0 1.649c1.801 1.801 4.726 1.801 6.564 0l7.351-7.35c.449-.487.449-1.239.001-1.688zm-2.439-7.35c-1.801-1.801-4.726-1.801-6.564 0l-7.351 7.351c-.45.449-.45 1.199 0 1.649s1.2.45 1.65 0l7.395-7.351c.9-.899 2.371-.899 3.27 0 .451.45 1.201.45 1.65 0 .421-.487.421-1.199-.029-1.649h-.021zm-2.475 2.437c-.45-.45-1.2-.45-1.65 0l-7.351 7.389c-.899.9-2.363.9-3.265 0-.9-.899-.9-2.363 0-3.264l7.239-7.239c-.9-.9-2.362-.9-3.263 0L1.35 8.719c-1.8 1.8-1.8 4.725 0 6.563 1.801 1.801 4.725 1.801 6.564 0l7.35-7.351c.451-.488.451-1.238 0-1.688h.002z"/></svg><b style="color:#111111">Squarespace</b></span><span class="platform platform--wide" aria-label="WooCommerce"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#96588A"><path d="M.754 9.58a.754.754 0 00-.754.758v2.525c0 .42.339.758.758.758h3.135l1.431.799-.326-.799h2.373a.757.757 0 00.758-.758v-2.525a.757.757 0 00-.758-.758H.754zm2.709.445h.03c.065.001.124.023.179.067a.26.26 0 01.103.19.29.29 0 01-.033.16c-.13.239-.236.64-.322 1.199-.083.541-.114.965-.094 1.267a.392.392 0 01-.039.219.213.213 0 01-.176.12c-.086.006-.177-.034-.263-.124-.31-.316-.555-.788-.735-1.416-.216.425-.375.744-.478.957-.196.376-.363.568-.502.578-.09.007-.166-.069-.233-.228-.17-.436-.352-1.277-.548-2.524a.297.297 0 01.054-.222c.047-.064.116-.095.21-.102.169-.013.265.065.288.238.103.695.217 1.284.336 1.766l.727-1.387c.066-.126.15-.192.25-.199.146-.01.237.083.273.28.083.441.188.817.315 1.136.086-.844.233-1.453.44-1.828a.255.255 0 01.218-.147zm1.293.36c.056 0 .116.006.18.02.232.05.411.177.53.386.107.18.161.395.161.654 0 .343-.087.654-.26.94-.2.332-.459.5-.781.5a.88.88 0 01-.18-.022.763.763 0 01-.531-.384 1.287 1.287 0 01-.158-.659c0-.342.085-.655.258-.937.202-.333.462-.498.78-.498zm2.084 0c.056 0 .116.006.18.02.236.05.411.177.53.386.107.18.16.395.16.654 0 .343-.086.654-.259.94-.2.332-.459.5-.781.5a.88.88 0 01-.18-.022.763.763 0 01-.531-.384 1.287 1.287 0 01-.16-.659c0-.342.087-.655.26-.937.202-.333.462-.498.78-.498zm4.437.047c-.305 0-.546.102-.718.304-.173.203-.256.49-.256.856 0 .395.086.697.256.906.17.21.418.316.744.316.315 0 .559-.107.728-.316.17-.21.256-.504.256-.883s-.087-.673-.26-.879c-.176-.202-.424-.304-.75-.304zm-1.466.002a1.13 1.13 0 00-.84.326c-.223.22-.332.499-.332.838 0 .362.108.658.328.88.22.223.505.336.861.336.103 0 .22-.016.346-.052v-.54c-.117.034-.216.051-.303.051a.545.545 0 01-.422-.177c-.106-.12-.16-.278-.16-.48 0-.19.053-.348.156-.468a.498.498 0 01.397-.181c.103 0 .212.015.332.049v-.537a1.394 1.394 0 00-.363-.045zm12.414 0a1.135 1.135 0 00-.84.326c-.223.22-.332.499-.332.838 0 .362.108.658.328.88.22.223.506.336.861.336.103 0 .22-.016.346-.052v-.54c-.116.034-.216.051-.303.051a.545.545 0 01-.422-.177c-.106-.12-.16-.278-.16-.48 0-.19.053-.348.156-.468a.498.498 0 01.397-.181c.103 0 .212.015.332.049v-.537a1.394 1.394 0 00-.363-.045zm-9.598.06l-.29 2.264h.579l.156-1.559.395 1.559h.412l.379-1.555.164 1.555h.603l-.304-2.264h-.791l-.12.508c-.03.13-.06.264-.087.4l-.067.352a29.97 29.97 0 00-.258-1.26h-.771zm2.768 0l-.29 2.264h.579l.156-1.559.396 1.559h.412l.375-1.555.165 1.555h.603l-.305-2.264h-.789l-.119.508c-.03.13-.06.264-.086.4l-.066.352c-.063-.352-.15-.771-.26-1.26h-.771zm3.988 0v2.264h.611v-1.031h.012l.494 1.03h.645l-.489-1.019a.61.61 0 00.37-.552.598.598 0 00-.25-.506c-.167-.123-.394-.186-.68-.186h-.713zm3.377 0v2.264H24v-.483h-.63v-.414h.54v-.468h-.54v-.416h.626v-.483H22.76zm-4.793.004v2.264h1.24v-.483h-.627v-.416h.541v-.468h-.54v-.415h.622v-.482h-1.236zm2.025.432c.146.003.25.025.313.072.063.046.091.12.091.227 0 .156-.135.236-.404.24v-.54zm-15.22.011c-.104 0-.205.069-.301.211a1.078 1.078 0 00-.2.639c0 .096.02.2.06.303.049.13.117.198.196.215.083.016.173-.02.27-.106.123-.11.205-.273.252-.492.016-.077.023-.16.023-.246 0-.097-.02-.2-.06-.303-.05-.13-.116-.198-.196-.215a.246.246 0 00-.045-.006zm2.083 0c-.103 0-.204.069-.3.211a1.078 1.078 0 00-.2.639c0 .096.02.2.06.303.049.13.117.198.196.215.083.016.173-.02.27-.106.123-.11.205-.273.252-.492.013-.077.023-.16.023-.246 0-.097-.02-.2-.06-.303-.05-.13-.116-.198-.196-.215a.246.246 0 00-.045-.006zm4.428.006c.233 0 .354.218.354.66-.004.273-.038.46-.098.553a.293.293 0 01-.262.139.266.266 0 01-.242-.139c-.056-.093-.084-.28-.084-.562 0-.436.11-.65.332-.65Z"/></svg></span><span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#146EF5"><path d="m24 4.515-7.658 14.97H9.149l3.205-6.204h-.144C9.566 16.713 5.621 18.973 0 19.485v-6.118s3.596-.213 5.71-2.435H0V4.515h6.417v5.278l.144-.001 2.622-5.277h4.854v5.244h.144l2.72-5.244H24Z"/></svg><b style="color:#146EF5">Webflow</b></span>'

# ================= HOME =================
home = f'''
<section class="hero hero--v2">
  <div class="starfield"></div><div class="orb orb--1"></div><div class="orb orb--2"></div>
  <div class="container hero__inner">
    <div>
      <p class="hero__kicker reveal">Build a website that actually converts – with Webratron</p>
      <h1 class="reveal" data-delay="1">High-Performance Websites <span class="grad-text">Delivered Fast</span></h1>
      <p class="hero__lead reveal" data-delay="2">Launch your custom website in as little as 24 hours. Webratron combines strategy, design and performance to create websites that not only look great but also drive real results for your business.</p>
      <ul class="hero__points reveal" data-delay="2">
        <li>Conversion-focused, user-friendly design</li>
        <li>Fully responsive across all devices</li>
        <li>Business websites starting from <strong>$469</strong></li>
        <li>Cross-browser &amp; OS compatibility</li>
        <li>Modern UI/UX that engages and converts</li>
        <li>Proven track record of client satisfaction</li>
        <li>Growth-driven strategies from industry experts</li>
        <li>Tailor-made website development solutions</li>
      </ul>
      <div class="hero__actions reveal" data-delay="3">
        <a href="contact.html" class="btn btn--primary btn--lg">Get Your Website in 24 Hours {ARROW}</a>
        <a href="pricing.html" class="btn btn--ghost btn--lg">View Packages</a>
      </div>
      <div class="hero__reviews reveal" data-delay="3">
        <img src="assets/img/trust-logos.png" alt="Reviewed on Bark, Clutch, Google and Trustpilot" width="720" height="70">
      </div>
    </div>
    <div class="hero__art reveal" data-delay="2">
      <div class="hero__ring"></div>
      <img src="assets/img/hero-visual.webp" alt="Classical statue stepping out of a smartphone in front of a glowing planet" width="740" height="785" fetchpriority="high">
      <div class="float-chip float-chip--1"><span class="dot">★</span><div><strong>4.7 / 5</strong><small>Trustpilot rating</small></div></div>
      <div class="float-chip float-chip--2"><span class="dot dot--orange">⚡</span><div><strong>24 Hours</strong><small>Fast delivery</small></div></div>
      <div class="float-chip float-chip--3"><span class="dot dot--cyan">$</span><div><strong>From $469</strong><small>Business websites</small></div></div>
    </div>
  </div>
</section>

<section class="platforms" aria-label="Platforms we build on">
  <p class="platforms__title">We build on the platforms you trust</p>
  <div class="platforms__track">
    <div class="platforms__row">{PLATFORMS}</div>
    <div class="platforms__row" aria-hidden="true">{PLATFORMS}</div>
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

import json
# ================= BLOG =================
POSTS = [
 ("website-cost-2026", "How Much Does a Website Cost in 2026?", "Pricing", "art--1", "Nov 2026", "5 min read",
  "A clear breakdown of what you actually pay for when you build a business website — and how to choose the right package.",
  [("p", "One of the first questions every business owner asks is: how much will a website cost? The honest answer is that it depends on what your website needs to do. A simple brochure site and a fully custom web portal are very different projects."),
   ("h2", "What affects the price?"),
   ("ul", ["Number of pages — a 3-page site takes far less time than a 20-page one.",
           "Custom design vs. templates — unique design work takes more time but sets your brand apart.",
           "Functionality — e-commerce, booking systems, member areas and integrations add development time.",
           "Content — copywriting, stock images, banners and video all add to the scope.",
           "Ongoing needs — hosting, maintenance, SEO and updates after launch."]),
   ("h2", "Typical price ranges"),
   ("p", "At Webratron, a Startup Website (3 pages, banners, contact form and mobile-responsive design) starts at $469. Our Professional Website package — 10 pages with a CMS so you can update content yourself — starts at $1,269. Fully custom web portals with a dedicated project manager start at $5,499."),
   ("h2", "Cheap vs. valuable"),
   ("p", "A website is a sales tool, not just an expense. A fast, mobile-friendly, conversion-focused site pays for itself by turning visitors into leads and customers. When comparing quotes, look at what is included: design ownership, revisions, responsiveness and support."),
   ("p", "Not sure which package fits? Contact us for a free consultation and we will recommend the right option for your goals and budget.")]),
 ("signs-you-need-a-redesign", "7 Signs Your Business Needs a Website Redesign", "Web Design", "art--3", "Oct 2026", "4 min read",
  "Is your website quietly costing you customers? Here are seven warning signs that it is time for a refresh.",
  [("p", "Your website is often the first impression a customer has of your business. If it looks outdated or is hard to use, visitors leave — usually for a competitor. Here are seven signs it is time for a redesign."),
   ("ol", ["It does not work well on mobile phones. Most visitors now browse on a phone; a site that is not responsive loses them instantly.",
           "It loads slowly. Every extra second of loading time increases the chance a visitor gives up.",
           "It looks outdated. Old fonts, cluttered layouts and low-quality images make a business look out of touch.",
           "Visitors do not convert. If people visit but rarely call, buy or fill in a form, your design may be getting in the way.",
           "You cannot update it yourself. A modern CMS lets you edit text, images and products without a developer.",
           "It does not reflect your brand. If your business has grown or rebranded, your website should too.",
           "It ranks poorly on Google. Poor structure, slow speed and missing SEO basics hold back your visibility."]),
   ("h2", "What a redesign should deliver"),
   ("p", "A good redesign is not just a new coat of paint. It should make your site faster, easier to use, mobile-friendly and focused on turning visitors into customers — while keeping the SEO value you have already built."),
   ("p", "If you recognise two or more of these signs, talk to our team about a redesign that is built to convert.")]),
 ("shopify-vs-wordpress", "Shopify vs WordPress: Which Is Right for Your Online Store?", "E-commerce", "art--4", "Sep 2026", "6 min read",
  "Both platforms power millions of stores. Here is how to decide which one suits your products, budget and growth plans.",
  [("p", "If you are planning to sell online, two names come up again and again: Shopify and WordPress (with WooCommerce). Both are excellent — but they suit different businesses."),
   ("h2", "Shopify: simple, hosted and built for selling"),
   ("ul", ["Hosting, security and updates are handled for you.",
           "Fast setup with a polished checkout and built-in payments.",
           "Large app store for reviews, upsells, subscriptions and more.",
           "Monthly subscription plus transaction or app fees."]),
   ("h2", "WordPress + WooCommerce: flexible and fully yours"),
   ("ul", ["Complete control over design, features and data.",
           "Ideal if content and blogging are a big part of your marketing.",
           "Thousands of plugins for almost any feature.",
           "You manage hosting, updates and security (or have a partner do it)."]),
   ("h2", "Which should you choose?"),
   ("p", "Choose Shopify if you want to launch quickly, focus on selling and avoid technical maintenance. Choose WordPress with WooCommerce if you want maximum flexibility, a content-heavy site or deeper customisation."),
   ("p", "Webratron builds on both platforms. Tell us about your products and goals and we will recommend — and build — the best fit for your store.")]),
]

def render_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == "p": out.append(f"<p>{val}</p>")
        elif kind == "h2": out.append(f"<h2>{val}</h2>")
        else: out.append(f"<{kind}>" + "".join(f"<li>{x}</li>" for x in val) + f"</{kind}>")
    return "\n    ".join(out)

def post_card(slug, title, cat, art, date, mins, excerpt, i):
    return f'''      <article class="work reveal" data-delay="{i % 3}">
        <a href="blog-{slug}.html" class="post-link">
        <div class="work__thumb"><div class="art {art}"></div><span class="label">{cat}</span></div>
        <div class="work__body">
          <small>{cat} · {date} · {mins}</small>
          <h3>{title}</h3>
          <p>{excerpt}</p>
          <span class="card__link">Read article {ARROW}</span>
        </div></a>
      </article>'''

cards = "\n".join(post_card(slug, t, c, a, d, m, e, i) for i, (slug, t, c, a, d, m, e, _) in enumerate(POSTS))
blog = page_hero("Blogs", "Blogs", 'Insights to <span class="grad-text">grow online</span>',
    "Practical tips on web design, development, e-commerce and digital marketing from the Webratron team.") + f'''
<section class="section" style="padding-top:20px">
  <div class="container">
    <div class="grid grid--3">
{cards}
    </div>
  </div>
</section>''' + cta()
page("blog.html", "Blogs — Web Design & Marketing Tips | Webratron",
     "Web design, development, e-commerce and digital marketing tips from the Webratron team.", blog, "blog.html")

for i, (slug, title, cat, art, date, mins, excerpt, body) in enumerate(POSTS):
    others = "\n".join(post_card(s2, t2, c2, a2, d2, m2, e2, j) for j, (s2, t2, c2, a2, d2, m2, e2, _) in enumerate(POSTS) if s2 != slug)
    html = f'''
<section class="page-hero">
  <div class="starfield"></div><div class="orb orb--1"></div><div class="orb orb--2"></div>
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><a href="blog.html">Blogs</a></nav>
    <span class="eyebrow">{cat}</span>
    <h1 style="font-size:clamp(2rem,4.5vw,3.4rem)">{title}</h1>
    <p>{date} · {mins}</p>
  </div>
</section>
<section class="section" style="padding-top:10px">
  <article class="container prose post">
    <p class="post__lead">{excerpt}</p>
    {render_body(body)}
    <div class="post__cta"><a href="contact.html" class="btn btn--primary">Get a free quote {ARROW}</a></div>
  </article>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="section-head"><h2>More <span class="grad-text">articles</span></h2></div>
    <div class="grid grid--2">
{others}
    </div>
  </div>
</section>'''
    schema = '\n  <script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "BlogPosting", "headline": title, "description": excerpt, "author": {"@type": "Organization", "name": "Webratron"}, "publisher": {"@type": "Organization", "name": "Webratron"}}) + '</script>'
    page(f"blog-{slug}.html", f"{title} | Webratron Blog", excerpt, html, "blog.html", schema)


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
  <div class="starfield"></div><div class="orb orb--1"></div><div class="orb orb--2"></div>
  <div style="position:relative;z-index:1">
    <h1 class="grad-text">404</h1>
    <h2>This page got lost in cyberspace.</h2>
    <p>The page you're looking for doesn't exist or has moved.</p>
    <a href="index.html" class="btn btn--primary">Back to home {ARROW}</a>
  </div>
</section>'''
page("404.html", "Page not found | Webratron", "The page you are looking for could not be found.", nf)
print("built")
