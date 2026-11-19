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
            dd = "".join(f'<li><a href="{SVC_URL[sid]}"><span class="dd__icon">{icon(ic)}</span>{name}</a></li>' for sid, ic, name, _, _ in SERVICES)
            lis.append(f'        <li class="has-dd"><a href="{h}"{cur}>{t} <span class="caret">{icon("chev")}</span></a>\n          <ul class="dropdown">{dd}</ul></li>')
        else:
            lis.append(f'        <li><a href="{h}"{cur}>{t}</a></li>')
    links = "\n".join(lis)
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container topbar">
    <a href="index.html" class="brand" aria-label="Webratron home"><img src="assets/img/logo-light.webp" alt="Webratron" width="441" height="80"></a>
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
        <a href="index.html" aria-label="Webratron home"><img src="assets/img/logo-dark.webp" alt="Webratron" width="593" height="104" class="footer__logo"></a>
        <p>Webratron is a results-driven web development company focused on building high-performance digital experiences. We create custom websites that not only look exceptional but also help businesses grow, engage, and convert.</p>
        <img src="assets/img/pay.webp" alt="We accept PayPal, Mastercard, Visa and American Express" width="340" height="53" class="footer__pay" loading="lazy">
      </div>
      <div class="footer__badges">
        <img src="assets/img/badges.webp" alt="Top 10 ranked, Verified by 10Best, DesignRush accredited agency, Appfutura top web design company, GoodFirms, Trustpilot, Google reviews, McAfee Secure, DMCA protected" width="755" height="200" loading="lazy">
      </div>
    </div>
    <div class="footer__links">
      <div><h2 class="footer__h">Quick Links</h2><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="portfolio.html">Portfolio</a></li><li><a href="blog.html">Blogs</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div><h2 class="footer__h">Services</h2><ul>{"".join(f'<li><a href="{SVC_URL[sid]}">{name}</a></li>' for sid, ic, name, _, _ in SERVICES)}</ul></div>
    </div>
    <div class="footer__locations">
      <h2 class="footer__loc">Our Locations</h2>
      <div class="loc-grid">
        <div><h3 class="footer__h">USA Address:</h3><p>80 Broad St 5th floor, New York, NY 10004, United States</p></div>
        <div><h3 class="footer__h">AU Address:</h3><p>{AU_ADDRESS}</p></div>
        <div><h3 class="footer__h">Email:</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><h3 class="footer__h">Phone:</h3><p><a href="tel:{PHONE_TEL}">{PHONE}</a></p></div>
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

import json as _json
# ---- Tracking (fill these in to activate; leave empty to disable) ----
GTM_ID = ""        # e.g. "GTM-XXXXXXX"  (Google Tag Manager — recommended for Google Ads / GA4)
GA4_ID = ""        # e.g. "G-XXXXXXXXXX" (only if not using GTM)
FORM_ENDPOINT = "" # e.g. "https://formspree.io/f/xxxx" — receives leads directly

SVC_URL = {"web-design": "website-design.html", "development": "web-development.html", "mobile": "mobile-app-development.html",
           "branding": "logo-design.html", "ecommerce": "ecommerce-website-development.html", "seo": "seo-services.html",
           "video": "video-animation.html", "maintenance": "website-maintenance.html"}
SITEMAP = []  # (url, priority)

def org_graph():
    org = {
      "@type": ["Organization", "ProfessionalService"], "@id": SITE + "/#org", "name": "Webratron", "url": SITE + "/",
      "logo": SITE + "/assets/img/logo-dark.webp", "image": SITE + "/assets/img/og-image.jpg",
      "description": "Webratron is a results-driven web design and development company in New York offering custom websites, Shopify and e-commerce stores, mobile apps, logo design, SEO and video animation.",
      "email": EMAIL, "telephone": "+1-917-924-6809", "priceRange": "$75 - $10,998",
      "address": {"@type": "PostalAddress", "streetAddress": "80 Broad Street, 5th Floor", "addressLocality": "New York", "addressRegion": "NY", "postalCode": "10004", "addressCountry": "US"},
      "department": [{"@type": "LocalBusiness", "name": "Webratron Australia", "address": {"@type": "PostalAddress", "streetAddress": "308 Sussex St", "addressLocality": "Sydney", "addressRegion": "NSW", "postalCode": "2000", "addressCountry": "AU"}, "telephone": "+1-917-924-6809"}],
      "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "telephone": "+1-917-924-6809", "email": EMAIL, "areaServed": "Worldwide", "availableLanguage": ["English"]},
                       {"@type": "ContactPoint", "contactType": "customer support", "telephone": "+1-864-671-0341", "email": EMAIL}],
      "areaServed": "Worldwide",
      "knowsAbout": ["Website design", "Web development", "WordPress", "Shopify", "E-commerce", "Mobile app development", "Flutter", "Logo design", "Branding", "Search engine optimization", "2D animation", "Whiteboard animation"],
      "sameAs": [TRUSTPILOT, PROVEN],
    }
    site = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Webratron", "publisher": {"@id": SITE + "/#org"}, "inLanguage": "en"}
    return [org, site]

def ld(*nodes):
    return '\n  <script type="application/ld+json">' + _json.dumps({"@context": "https://schema.org", "@graph": list(nodes)}, ensure_ascii=False) + '</script>'

def breadcrumbs(crumbs):
    items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + (u if u != "index.html" else "")} for i, (n, u) in enumerate(crumbs)]
    return {"@type": "BreadcrumbList", "itemListElement": items}

def faq_node(pairs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}

def tracking_head():
    out = '\n  <script>window.dataLayer=window.dataLayer||[];</script>'
    if GTM_ID:
        out += f"\n  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>"
    elif GA4_ID:
        out += f"\n  <script async src=\"https://www.googletagmanager.com/gtag/js?id={GA4_ID}\"></script>\n  <script>function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA4_ID}');</script>"
    return out

def tracking_body():
    return f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>\n' if GTM_ID else ""

def lp_header():
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header lp-header">
  <div class="container topbar">
    <a href="index.html" class="brand" aria-label="Webratron home"><img src="assets/img/logo-light.webp" alt="Webratron" width="441" height="80"></a>
    <a href="tel:{PHONE_TEL}" class="lp-call" data-track="click_call">{icon("phone")}<span><small>Call now — free consultation</small>{PHONE}</span></a>
    <a href="#lead" class="btn btn--quote">Get a Free Quote</a>
  </div>
</header>"""

def lp_footer():
    return f"""<footer class="lp-footer">
  <div class="container">
    <img src="assets/img/badges.webp" alt="Top 10 ranked, Verified, DesignRush accredited agency, Appfutura, GoodFirms, Trustpilot, Google reviews, McAfee Secure, DMCA protected" width="755" height="200" loading="lazy" class="lp-footer__badges">
    <p>Webratron · 80 Broad St 5th Floor, New York, NY 10004 · 308 Sussex St, Sydney NSW 2000 · <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="tel:{PHONE_TEL}">{PHONE}</a></p>
    <p>&copy; Webratron <span data-year>2026</span> · <a href="privacy.html">Privacy Policy</a> · <a href="terms.html">Terms &amp; Condition</a></p>
  </div>
</footer>
<div class="lp-bar"><a href="tel:{PHONE_TEL}" data-track="click_call">{icon("phone")} Call</a><a href="#lead">{icon("chat")} Free Quote</a></div>"""

def page(fname, title, desc, body, active=None, schema="", noindex=False, crumbs=None, lp=False, extra_nodes=(), priority=None):
    canonical = SITE + "/" + ("" if fname == "index.html" else fname)
    nodes = org_graph() + list(extra_nodes)
    if crumbs: nodes.append(breadcrumbs(crumbs))
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    if not noindex: SITEMAP.append((canonical, priority or (1.0 if fname == "index.html" else 0.7)))
    html = f'''<!doctype html>
<html lang="en" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#050826">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_US">
  <meta property="og:site_name" content="Webratron">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="alternate" type="text/plain" href="{SITE}/llms.txt" title="LLM summary">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/v3.css">{'<link rel="preload" as="image" href="assets/img/hero-visual.webp" fetchpriority="high">' if fname == "index.html" else ""}{tracking_head()}{ld(*nodes)}{schema}
</head>
<body{' class="is-lp"' if lp else ''} data-form-endpoint="{FORM_ENDPOINT}">
{tracking_body()}{lp_header() if lp else header(active)}
<main id="main">
{textwrap.dedent(body).strip()}
</main>
{lp_footer() if lp else footer()}
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
        link = f'<a href="{SVC_URL[sid]}" class="card__link">Learn more<span class="sr-only"> about {name}</span> {ARROW}</a>' if links else ""
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

# ================= ILLUSTRATIONS (inline SVG scenes) =================
_SCENE_N = [0]
def scene(kind):
    _SCENE_N[0] += 1
    u = f"s{_SCENE_N[0]}"
    defs = f'''<defs>
  <linearGradient id="{u}g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8b5cf6"/><stop offset=".55" stop-color="#ec4899"/><stop offset="1" stop-color="#fb923c"/></linearGradient>
  <linearGradient id="{u}c" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6366f1"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
  <linearGradient id="{u}o" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fb923c"/><stop offset="1" stop-color="#facc15"/></linearGradient>
  <linearGradient id="{u}m" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#34d399"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
  <filter id="{u}s" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#000" flood-opacity=".55"/></filter>
</defs>'''
    G, C, O, M, S = f"url(#{u}g)", f"url(#{u}c)", f"url(#{u}o)", f"url(#{u}m)", f"url(#{u}s)"
    P, L, T = "#15122e", "#2a2552", "#e9e8ff"
    def win(x, y, w, h, extra=""):
        return (f'<g filter="{S}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{P}" stroke="#3a3470"/>'
                f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="12" fill="#1d1940"/><rect x="{x}" y="{y+14}" width="{w}" height="12" fill="#1d1940"/>'
                f'<circle cx="{x+16}" cy="{y+13}" r="4" fill="#ff5f57"/><circle cx="{x+30}" cy="{y+13}" r="4" fill="#febc2e"/><circle cx="{x+44}" cy="{y+13}" r="4" fill="#28c840"/>{extra}</g>')
    def bar(x, y, w, h=7, fill=None, op=.5):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{fill or T}" opacity="{op}"/>'
    body = ""
    if kind == "web-design":
        body = win(40, 36, 300, 210,
            f'<rect x="58" y="80" width="264" height="74" rx="10" fill="{G}"/>' + bar(74, 98, 120, 10, "#fff", .95) + bar(74, 116, 170, 6, "#fff", .7) +
            f'<rect x="74" y="130" width="60" height="16" rx="8" fill="#fff"/>' +
            "".join(f'<rect x="{58+i*90}" y="166" width="84" height="62" rx="9" fill="{L}"/><rect x="{68+i*90}" y="176" width="22" height="22" rx="6" fill="{[C,O,M][i]}"/>' + bar(68+i*90, 206, 60, 5) + bar(68+i*90, 216, 40, 5, op=.3) for i in range(3)))
        body += "".join(f'<circle cx="{354}" cy="{70+i*34}" r="13" fill="{c}" filter="{S}"/>' for i, c in enumerate([G, C, O, M]))
        body += '<path d="M268 196l26 10-11 4-4 11z" fill="#fff" stroke="#15122e" stroke-width="2"/>'
    elif kind == "development":
        lines = [(0, 90, G), (1, 140, C), (1, 110, O), (2, 150, M), (2, 90, C), (1, 70, G), (0, 40, T)]
        code = "".join(f'<rect x="{80+ind*18}" y="{78+i*20}" width="{w}" height="8" rx="4" fill="{c}" opacity="{.6 if c==T else .95}"/><text x="58" y="{86+i*20}" fill="#6e6a9e" font-size="10" font-family="monospace">{i+1}</text>' for i, (ind, w, c) in enumerate(lines))
        body = win(30, 34, 280, 200, code)
        body += (f'<g filter="{S}"><rect x="200" y="160" width="170" height="100" rx="12" fill="#0b0a1f" stroke="#3a3470"/>'
                 f'<text x="214" y="186" fill="#34d399" font-size="12" font-family="monospace">$ npm run build</text>'
                 f'<text x="214" y="206" fill="#e9e8ff" font-size="11" font-family="monospace" opacity=".7">✓ compiled in 1.2s</text>'
                 f'<text x="214" y="226" fill="#f9a8d4" font-size="11" font-family="monospace">⚡ score: 100</text></g>')
        body += f'<text x="318" y="70" fill="{G}" font-size="54" font-weight="700" font-family="monospace">&lt;/&gt;</text>'
    elif kind == "mobile":
        def phone(x, y, s, accent):
            return (f'<g filter="{S}" transform="translate({x} {y}) scale({s})"><rect width="120" height="230" rx="22" fill="#0b0a1f" stroke="#3a3470" stroke-width="2"/>'
                    f'<rect x="8" y="10" width="104" height="210" rx="16" fill="{P}"/><rect x="44" y="16" width="32" height="6" rx="3" fill="#3a3470"/>'
                    f'<rect x="16" y="32" width="88" height="62" rx="12" fill="{accent}"/>' + bar(24, 46, 50, 7, "#fff", .95) + bar(24, 60, 36, 5, "#fff", .7) +
                    "".join(f'<rect x="16" y="{104+i*36}" width="88" height="28" rx="8" fill="{L}"/><circle cx="31" cy="{118+i*36}" r="8" fill="{[C,O,M][i]}"/>' + bar(45, 112+i*36, 46, 5) + bar(45, 122+i*36, 30, 4, op=.3) for i in range(3)) +
                    '</g>')
        body = phone(70, 40, 1, G) + phone(210, 64, .9, C)
        body += f'<g filter="{S}"><rect x="300" y="44" width="70" height="38" rx="10" fill="{P}" stroke="#3a3470"/><text x="335" y="68" text-anchor="middle" fill="#fff" font-size="13" font-weight="700" font-family="sans-serif">iOS ✓</text></g>'
        body += f'<g filter="{S}"><rect x="22" y="214" width="88" height="38" rx="10" fill="{P}" stroke="#3a3470"/><text x="66" y="238" text-anchor="middle" fill="#fff" font-size="13" font-weight="700" font-family="sans-serif">Android ✓</text></g>'
    elif kind == "branding":
        tiles = [(G, '<circle cx="0" cy="0" r="26" fill="none" stroke="#fff" stroke-width="7"/><circle cx="0" cy="0" r="9" fill="#fff"/>'),
                 (C, '<path d="M-26 22L0-26 26 22z" fill="#fff"/><path d="M-12 22L0 0 12 22z" fill="#6366f1"/>'),
                 (O, '<rect x="-22" y="-22" width="44" height="44" rx="10" fill="none" stroke="#fff" stroke-width="7" transform="rotate(45)"/>'),
                 (M, '<path d="M-28-14l10 32 10-24 10 24 10-32" fill="none" stroke="#fff" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>')]
        body = "".join(f'<g filter="{S}"><rect x="{60+(i%2)*130}" y="{36+(i//2)*120}" width="116" height="106" rx="16" fill="{c}"/><g transform="translate({118+(i%2)*130} {89+(i//2)*120})">{shape}</g></g>' for i, (c, shape) in enumerate(tiles))
        body += f'<g filter="{S}"><rect x="316" y="60" width="64" height="180" rx="12" fill="{P}" stroke="#3a3470"/>' + "".join(f'<circle cx="348" cy="{88+i*36}" r="12" fill="{c}"/>' for i, c in enumerate(["#8b5cf6", "#ec4899", "#fb923c", "#22d3ee", "#34d399"])) + '</g>'
        body += '<path d="M300 250c-20-30-60-10-80-30" fill="none" stroke="#f9a8d4" stroke-width="3" stroke-dasharray="6 6"/><circle cx="300" cy="250" r="6" fill="#fff"/><circle cx="220" cy="220" r="6" fill="#fff"/>'
    elif kind == "ecommerce":
        prods = "".join(f'<rect x="{56+i*92}" y="74" width="80" height="120" rx="10" fill="{L}"/><rect x="{64+i*92}" y="82" width="64" height="56" rx="8" fill="{[G,C,O][i]}"/>' + bar(64+i*92, 148, 50, 6) + f'<text x="{64+i*92}" y="176" fill="#fbbf77" font-size="13" font-weight="700" font-family="sans-serif">${[49,89,29][i]}</text><rect x="{102+i*92}" y="164" width="26" height="18" rx="6" fill="#ec4899"/>' for i in range(3))
        body = win(40, 40, 300, 200, prods + bar(56, 210, 120, 8, op=.3) + f'<rect x="250" y="204" width="74" height="22" rx="11" fill="{G}"/><text x="287" y="219" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="sans-serif">Checkout</text>')
        body += (f'<g filter="{S}" transform="translate(318 34)"><circle r="30" fill="{G}"/><path d="M-14-8h4l4 16h14l4-12h-20" fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round"/><circle cx="-4" cy="14" r="2.5" fill="#fff"/><circle cx="8" cy="14" r="2.5" fill="#fff"/>'
                 '<circle cx="20" cy="-20" r="11" fill="#34d399"/><text x="20" y="-16" text-anchor="middle" fill="#fff" font-size="12" font-weight="700" font-family="sans-serif">3</text></g>')
        body += f'<g filter="{S}"><rect x="20" y="210" width="110" height="46" rx="12" fill="{P}" stroke="#3a3470"/><text x="34" y="230" fill="#9b98c4" font-size="10" font-family="sans-serif">Sales today</text><text x="34" y="248" fill="#34d399" font-size="15" font-weight="700" font-family="sans-serif">+$2,480</text></g>'
    elif kind == "seo":
        res = "".join(f'<rect x="{56}" y="{108+i*40}" width="268" height="32" rx="8" fill="{G if i==0 else L}" opacity="{1 if i==0 else .9}"/><text x="68" y="{129+i*40}" fill="#fff" font-size="13" font-weight="700" font-family="sans-serif">#{i+1}</text>' + bar(96, 116+i*40, [150,120,140][i], 6, "#fff", .9 if i==0 else .5) + bar(96, 126+i*40, [100,90,70][i], 5, "#fff", .6 if i==0 else .3) for i in range(3))
        body = win(40, 36, 300, 210, f'<rect x="56" y="74" width="268" height="24" rx="12" fill="{L}"/><circle cx="72" cy="86" r="5" fill="none" stroke="#e9e8ff" stroke-width="2"/>' + bar(86, 83, 110, 6) + res)
        body += (f'<g filter="{S}"><rect x="262" y="160" width="120" height="96" rx="12" fill="{P}" stroke="#3a3470"/>'
                 f'<path d="M276 236l22-18 18 10 22-26 26-14" fill="none" stroke="{M}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
                 f'<text x="276" y="182" fill="#34d399" font-size="14" font-weight="700" font-family="sans-serif">↑ 312%</text></g>')
    elif kind == "video":
        frames = "".join(f'<rect x="{58+i*68}" y="196" width="60" height="34" rx="6" fill="{[G,C,O,M][i]}" opacity=".9"/>' for i in range(4))
        body = win(40, 30, 300, 220, f'<rect x="56" y="70" width="268" height="112" rx="10" fill="{G}"/><circle cx="190" cy="126" r="26" fill="#fff" opacity=".95"/><path d="M182 112l22 14-22 14z" fill="#ec4899"/>'
                   + bar(56, 186, 268, 4, op=.25) + f'<rect x="56" y="186" width="150" height="4" rx="2" fill="#fff"/><circle cx="206" cy="188" r="6" fill="#fff"/>' + frames)
        body += f'<g filter="{S}"><rect x="300" y="40" width="80" height="40" rx="10" fill="{P}" stroke="#3a3470"/><text x="340" y="65" text-anchor="middle" fill="#fff" font-size="13" font-weight="700" font-family="sans-serif">0:30–2:00</text></g>'
        body += f'<g filter="{S}" transform="translate(356 230)"><circle r="22" fill="{O}"/><path d="M-6-10v14a5 5 0 1 1-3-4.5V-12l14-3v12a5 5 0 1 1-3-4.5V-11z" fill="#fff"/></g>'
    elif kind == "maintenance":
        bars_ = "".join(f'<rect x="{62+i*22}" y="{200-h}" width="14" height="{h}" rx="4" fill="{M if i%3 else C}"/>' for i, h in enumerate([60, 80, 70, 95, 85, 110, 100, 120, 105, 115]))
        body = win(30, 36, 290, 210, bar(52, 72, 90, 8, op=.6) + f'<text x="52" y="102" fill="#34d399" font-size="22" font-weight="700" font-family="sans-serif">99.9% uptime</text>' + bars_ +
                   "".join(f'<rect x="{52+i*88}" y="214" width="78" height="22" rx="11" fill="{L}"/><circle cx="{64+i*88}" cy="225" r="6" fill="#34d399"/>' + bar(74+i*88, 222, 44, 6) for i in range(3)))
        body += (f'<g filter="{S}" transform="translate(330 110)"><path d="M0-50l42 16v30c0 32-24 52-42 60-18-8-42-28-42-60v-30z" fill="{G}"/>'
                 '<path d="M-16 4l11 11 22-24" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>')
    return f'<svg class="scene" viewBox="0 0 400 290" role="img" aria-hidden="true">{defs}{body}</svg>'

WORK_SCENE = {"Custom Websites": "web-design", "Mobile Apps": "mobile", "Logo & Mascot": "branding",
              "Shopify Stores": "ecommerce", "2D Animation": "video", "WordPress": "development"}


def work_cards(limit=None):
    out = []
    for i, (cat, art, name, kind, short, text) in enumerate(WORK[:limit] if limit else WORK):
        out.append(f'''      <article class="work reveal" data-cat="{cat}" data-delay="{i % 3}">
        <div class="work__thumb"><div class="art {art}"></div>{scene(WORK_SCENE.get(name, "web-design"))}</div>
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
 ("How much does a website cost?", "Website packages start at $469 (Startup) and go up to $5,499 for a customized web portal. Logo design starts at $75, animation videos at $499 and SEO at $3,500 for a 6-month plan. Our Business Starter combo (logo, stationery, social media and a 15-page website) is $1,999. Contact us for a quote tailored to your needs."),
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

PLATFORMS = '<span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#7AB55C"><path d="M15.337 23.979l7.216-1.561s-2.604-17.613-2.625-17.73c-.018-.116-.114-.192-.211-.192s-1.929-.136-1.929-.136-1.275-1.274-1.439-1.411c-.045-.037-.075-.057-.121-.074l-.914 21.104h.023zM11.71 11.305s-.81-.424-1.774-.424c-1.447 0-1.504.906-1.504 1.141 0 1.232 3.24 1.715 3.24 4.629 0 2.295-1.44 3.76-3.406 3.76-2.354 0-3.54-1.465-3.54-1.465l.646-2.086s1.245 1.066 2.28 1.066c.675 0 .975-.545.975-.932 0-1.619-2.654-1.694-2.654-4.359-.034-2.237 1.571-4.416 4.827-4.416 1.257 0 1.875.361 1.875.361l-.945 2.715-.02.01zM11.17.83c.136 0 .271.038.405.135-.984.465-2.064 1.639-2.508 3.992-.656.213-1.293.405-1.889.578C7.697 3.75 8.951.84 11.17.84V.83zm1.235 2.949v.135c-.754.232-1.583.484-2.394.736.466-1.777 1.333-2.645 2.085-2.971.193.501.309 1.176.309 2.1zm.539-2.234c.694.074 1.141.867 1.429 1.755-.349.114-.735.231-1.158.366v-.252c0-.752-.096-1.371-.271-1.871v.002zm2.992 1.289c-.02 0-.06.021-.078.021s-.289.075-.714.21c-.423-1.233-1.176-2.37-2.508-2.37h-.115C12.135.209 11.669 0 11.265 0 8.159 0 6.675 3.877 6.21 5.846c-1.194.365-2.063.636-2.16.674-.675.213-.694.232-.772.87-.075.462-1.83 14.063-1.83 14.063L15.009 24l.927-21.166z"/></svg><b style="color:#7AB55C">Shopify</b></span><span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#1BDBDB"><path d="M20.702 2.29c-2.494-1.554-5.778-1.187-8.706.654C9.076 1.104 5.79.736 3.3 2.29c-3.941 2.463-4.42 8.806-1.07 14.167 2.47 3.954 6.333 6.269 9.77 6.226 3.439.043 7.301-2.273 9.771-6.226 3.347-5.361 2.872-11.704-1.069-14.167zM4.042 15.328a12.838 12.838 0 01-1.546-3.541 10.12 10.12 0 01-.336-3.338c.15-1.98.956-3.524 2.27-4.345 1.315-.822 3.052-.87 4.903-.137.281.113.556.24.825.382A15.11 15.11 0 007.5 7.54c-2.035 3.255-2.655 6.878-1.945 9.765a13.247 13.247 0 01-1.514-1.98zm17.465-3.541a12.866 12.866 0 01-1.547 3.54 13.25 13.25 0 01-1.513 1.984c.635-2.589.203-5.76-1.353-8.734a.39.39 0 00-.563-.153l-4.852 3.032a.397.397 0 00-.126.546l.712 1.139a.395.395 0 00.547.126l3.145-1.965c.101.306.203.606.28.916.296 1.086.41 2.214.335 3.337-.15 1.982-.956 3.525-2.27 4.347a4.437 4.437 0 01-2.25.65h-.101a4.432 4.432 0 01-2.25-.65c-1.314-.822-2.121-2.365-2.27-4.347-.074-1.123.039-2.251.335-3.337a13.212 13.212 0 014.05-6.482 10.148 10.148 0 012.849-1.765c1.845-.733 3.586-.685 4.9.137 1.316.822 2.122 2.365 2.271 4.345a10.146 10.146 0 01-.33 3.334z"/></svg><b style="color:#0B7F80">GoDaddy</b></span><span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#FF9900"><path d="M.045 18.02c.072-.116.187-.124.348-.022 3.636 2.11 7.594 3.166 11.87 3.166 2.852 0 5.668-.533 8.447-1.595l.315-.14c.138-.06.234-.1.293-.13.226-.088.39-.046.525.13.12.174.09.336-.12.48-.256.19-.6.41-1.006.654-1.244.743-2.64 1.316-4.185 1.726a17.617 17.617 0 01-10.951-.577 17.88 17.88 0 01-5.43-3.35c-.1-.074-.151-.15-.151-.22 0-.047.021-.09.051-.13zm6.565-6.218c0-1.005.247-1.863.743-2.577.495-.71 1.17-1.25 2.04-1.615.796-.335 1.756-.575 2.912-.72.39-.046 1.033-.103 1.92-.174v-.37c0-.93-.105-1.558-.3-1.875-.302-.43-.78-.65-1.44-.65h-.182c-.48.046-.896.196-1.246.46-.35.27-.575.63-.675 1.096-.06.3-.206.465-.435.51l-2.52-.315c-.248-.06-.372-.18-.372-.39 0-.046.007-.09.022-.15.247-1.29.855-2.25 1.82-2.88.976-.616 2.1-.975 3.39-1.05h.54c1.65 0 2.957.434 3.888 1.29.135.15.27.3.405.48.12.165.224.314.283.45.075.134.15.33.195.57.06.254.105.42.135.51.03.104.062.3.076.615.01.313.02.493.02.553v5.28c0 .376.06.72.165 1.036.105.313.21.54.315.674l.51.674c.09.136.136.256.136.36 0 .12-.06.226-.18.314-1.2 1.05-1.86 1.62-1.963 1.71-.165.135-.375.15-.63.045a6.062 6.062 0 01-.526-.496l-.31-.347a9.391 9.391 0 01-.317-.42l-.3-.435c-.81.886-1.603 1.44-2.4 1.665-.494.15-1.093.227-1.83.227-1.11 0-2.04-.343-2.76-1.034-.72-.69-1.08-1.665-1.08-2.94l-.05-.076zm3.753-.438c0 .566.14 1.02.425 1.364.285.34.675.512 1.155.512.045 0 .106-.007.195-.02.09-.016.134-.023.166-.023.614-.16 1.08-.553 1.424-1.178.165-.28.285-.58.36-.91.09-.32.12-.59.135-.8.015-.195.015-.54.015-1.005v-.54c-.84 0-1.484.06-1.92.18-1.275.36-1.92 1.17-1.92 2.43l-.035-.02zm9.162 7.027c.03-.06.075-.11.132-.17.362-.243.714-.41 1.05-.5a8.094 8.094 0 011.612-.24c.14-.012.28 0 .41.03.65.06 1.05.168 1.172.33.063.09.099.228.099.39v.15c0 .51-.149 1.11-.424 1.8-.278.69-.664 1.248-1.156 1.68-.073.06-.14.09-.197.09-.03 0-.06 0-.09-.012-.09-.044-.107-.12-.064-.24.54-1.26.806-2.143.806-2.64 0-.15-.03-.27-.087-.344-.145-.166-.55-.257-1.224-.257-.243 0-.533.016-.87.046-.363.045-.7.09-1 .135-.09 0-.148-.014-.18-.044-.03-.03-.036-.047-.02-.077 0-.017.006-.03.02-.063v-.06z"/></svg><b style="color:#111111">Amazon</b></span><span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#21759B"><path d="M21.469 6.825c.84 1.537 1.318 3.3 1.318 5.175 0 3.979-2.156 7.456-5.363 9.325l3.295-9.527c.615-1.54.82-2.771.82-3.864 0-.405-.026-.78-.07-1.11m-7.981.105c.647-.03 1.232-.105 1.232-.105.582-.075.514-.93-.067-.899 0 0-1.755.135-2.88.135-1.064 0-2.85-.15-2.85-.15-.585-.03-.661.855-.075.885 0 0 .54.061 1.125.09l1.68 4.605-2.37 7.08L5.354 6.9c.649-.03 1.234-.1 1.234-.1.585-.075.516-.93-.065-.896 0 0-1.746.138-2.874.138-.2 0-.438-.008-.69-.015C4.911 3.15 8.235 1.215 12 1.215c2.809 0 5.365 1.072 7.286 2.833-.046-.003-.091-.009-.141-.009-1.06 0-1.812.923-1.812 1.914 0 .89.513 1.643 1.06 2.531.411.72.89 1.643.89 2.977 0 .915-.354 1.994-.821 3.479l-1.075 3.585-3.9-11.61.001.014zM12 22.784c-1.059 0-2.081-.153-3.048-.437l3.237-9.406 3.315 9.087c.024.053.05.101.078.149-1.12.393-2.325.609-3.582.609M1.211 12c0-1.564.336-3.05.935-4.39L7.29 21.709C3.694 19.96 1.212 16.271 1.211 12M12 0C5.385 0 0 5.385 0 12s5.385 12 12 12 12-5.385 12-12S18.615 0 12 0"/></svg><b style="color:#21759B">WordPress</b></span><span class="platform platform--wide" role="img" aria-label="Wix"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#0C6EFC"><path d="m0 7.354 2.113 9.292h.801a1.54 1.54 0 0 0 1.506-1.218l1.351-6.34a.171.171 0 0 1 .167-.137c.08 0 .15.058.167.137l1.352 6.34a1.54 1.54 0 0 0 1.506 1.218h.805l2.113-9.292h-.565c-.62 0-1.159.43-1.296 1.035l-1.26 5.545-1.106-5.176a1.76 1.76 0 0 0-2.19-1.324c-.639.176-1.113.716-1.251 1.365l-1.094 5.127-1.26-5.537A1.33 1.33 0 0 0 .563 7.354H0zm13.992 0a.951.951 0 0 0-.951.95v8.342h.635a.952.952 0 0 0 .951-.95V7.353h-.635zm1.778 0 3.158 4.66-3.14 4.632h1.325c.368 0 .712-.181.918-.486l1.756-2.59a.12.12 0 0 1 .197 0l1.754 2.59c.206.305.55.486.918.486h1.326l-3.14-4.632L24 7.354h-1.326c-.368 0-.712.181-.918.486l-1.772 2.617a.12.12 0 0 1-.197 0L18.014 7.84a1.108 1.108 0 0 0-.918-.486H15.77z"/></svg></span><span class="platform platform--img"><img src="assets/img/weebly.png" alt="Weebly" width="90" height="70" loading="lazy"></span><span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#111111"><path d="M22.655 8.719c-1.802-1.801-4.726-1.801-6.564 0l-7.351 7.35c-.45.45-.45 1.2 0 1.65.45.449 1.2.449 1.65 0l7.351-7.351c.899-.899 2.362-.899 3.264 0 .9.9.9 2.364 0 3.264l-7.239 7.239c.9.899 2.362.899 3.263 0l5.589-5.589c1.836-1.838 1.836-4.763.037-6.563zm-2.475 2.437c-.451-.45-1.201-.45-1.65 0l-7.354 7.389c-.9.899-2.361.899-3.262 0-.45-.45-1.2-.45-1.65 0s-.45 1.2 0 1.649c1.801 1.801 4.726 1.801 6.564 0l7.351-7.35c.449-.487.449-1.239.001-1.688zm-2.439-7.35c-1.801-1.801-4.726-1.801-6.564 0l-7.351 7.351c-.45.449-.45 1.199 0 1.649s1.2.45 1.65 0l7.395-7.351c.9-.899 2.371-.899 3.27 0 .451.45 1.201.45 1.65 0 .421-.487.421-1.199-.029-1.649h-.021zm-2.475 2.437c-.45-.45-1.2-.45-1.65 0l-7.351 7.389c-.899.9-2.363.9-3.265 0-.9-.899-.9-2.363 0-3.264l7.239-7.239c-.9-.9-2.362-.9-3.263 0L1.35 8.719c-1.8 1.8-1.8 4.725 0 6.563 1.801 1.801 4.725 1.801 6.564 0l7.35-7.351c.451-.488.451-1.238 0-1.688h.002z"/></svg><b style="color:#111111">Squarespace</b></span><span class="platform platform--wide" role="img" aria-label="WooCommerce"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#96588A"><path d="M.754 9.58a.754.754 0 00-.754.758v2.525c0 .42.339.758.758.758h3.135l1.431.799-.326-.799h2.373a.757.757 0 00.758-.758v-2.525a.757.757 0 00-.758-.758H.754zm2.709.445h.03c.065.001.124.023.179.067a.26.26 0 01.103.19.29.29 0 01-.033.16c-.13.239-.236.64-.322 1.199-.083.541-.114.965-.094 1.267a.392.392 0 01-.039.219.213.213 0 01-.176.12c-.086.006-.177-.034-.263-.124-.31-.316-.555-.788-.735-1.416-.216.425-.375.744-.478.957-.196.376-.363.568-.502.578-.09.007-.166-.069-.233-.228-.17-.436-.352-1.277-.548-2.524a.297.297 0 01.054-.222c.047-.064.116-.095.21-.102.169-.013.265.065.288.238.103.695.217 1.284.336 1.766l.727-1.387c.066-.126.15-.192.25-.199.146-.01.237.083.273.28.083.441.188.817.315 1.136.086-.844.233-1.453.44-1.828a.255.255 0 01.218-.147zm1.293.36c.056 0 .116.006.18.02.232.05.411.177.53.386.107.18.161.395.161.654 0 .343-.087.654-.26.94-.2.332-.459.5-.781.5a.88.88 0 01-.18-.022.763.763 0 01-.531-.384 1.287 1.287 0 01-.158-.659c0-.342.085-.655.258-.937.202-.333.462-.498.78-.498zm2.084 0c.056 0 .116.006.18.02.236.05.411.177.53.386.107.18.16.395.16.654 0 .343-.086.654-.259.94-.2.332-.459.5-.781.5a.88.88 0 01-.18-.022.763.763 0 01-.531-.384 1.287 1.287 0 01-.16-.659c0-.342.087-.655.26-.937.202-.333.462-.498.78-.498zm4.437.047c-.305 0-.546.102-.718.304-.173.203-.256.49-.256.856 0 .395.086.697.256.906.17.21.418.316.744.316.315 0 .559-.107.728-.316.17-.21.256-.504.256-.883s-.087-.673-.26-.879c-.176-.202-.424-.304-.75-.304zm-1.466.002a1.13 1.13 0 00-.84.326c-.223.22-.332.499-.332.838 0 .362.108.658.328.88.22.223.505.336.861.336.103 0 .22-.016.346-.052v-.54c-.117.034-.216.051-.303.051a.545.545 0 01-.422-.177c-.106-.12-.16-.278-.16-.48 0-.19.053-.348.156-.468a.498.498 0 01.397-.181c.103 0 .212.015.332.049v-.537a1.394 1.394 0 00-.363-.045zm12.414 0a1.135 1.135 0 00-.84.326c-.223.22-.332.499-.332.838 0 .362.108.658.328.88.22.223.506.336.861.336.103 0 .22-.016.346-.052v-.54c-.116.034-.216.051-.303.051a.545.545 0 01-.422-.177c-.106-.12-.16-.278-.16-.48 0-.19.053-.348.156-.468a.498.498 0 01.397-.181c.103 0 .212.015.332.049v-.537a1.394 1.394 0 00-.363-.045zm-9.598.06l-.29 2.264h.579l.156-1.559.395 1.559h.412l.379-1.555.164 1.555h.603l-.304-2.264h-.791l-.12.508c-.03.13-.06.264-.087.4l-.067.352a29.97 29.97 0 00-.258-1.26h-.771zm2.768 0l-.29 2.264h.579l.156-1.559.396 1.559h.412l.375-1.555.165 1.555h.603l-.305-2.264h-.789l-.119.508c-.03.13-.06.264-.086.4l-.066.352c-.063-.352-.15-.771-.26-1.26h-.771zm3.988 0v2.264h.611v-1.031h.012l.494 1.03h.645l-.489-1.019a.61.61 0 00.37-.552.598.598 0 00-.25-.506c-.167-.123-.394-.186-.68-.186h-.713zm3.377 0v2.264H24v-.483h-.63v-.414h.54v-.468h-.54v-.416h.626v-.483H22.76zm-4.793.004v2.264h1.24v-.483h-.627v-.416h.541v-.468h-.54v-.415h.622v-.482h-1.236zm2.025.432c.146.003.25.025.313.072.063.046.091.12.091.227 0 .156-.135.236-.404.24v-.54zm-15.22.011c-.104 0-.205.069-.301.211a1.078 1.078 0 00-.2.639c0 .096.02.2.06.303.049.13.117.198.196.215.083.016.173-.02.27-.106.123-.11.205-.273.252-.492.016-.077.023-.16.023-.246 0-.097-.02-.2-.06-.303-.05-.13-.116-.198-.196-.215a.246.246 0 00-.045-.006zm2.083 0c-.103 0-.204.069-.3.211a1.078 1.078 0 00-.2.639c0 .096.02.2.06.303.049.13.117.198.196.215.083.016.173-.02.27-.106.123-.11.205-.273.252-.492.013-.077.023-.16.023-.246 0-.097-.02-.2-.06-.303-.05-.13-.116-.198-.196-.215a.246.246 0 00-.045-.006zm4.428.006c.233 0 .354.218.354.66-.004.273-.038.46-.098.553a.293.293 0 01-.262.139.266.266 0 01-.242-.139c-.056-.093-.084-.28-.084-.562 0-.436.11-.65.332-.65Z"/></svg></span><span class="platform"><svg viewBox="0 0 24 24" aria-hidden="true" style="fill:#146EF5"><path d="m24 4.515-7.658 14.97H9.149l3.205-6.204h-.144C9.566 16.713 5.621 18.973 0 19.485v-6.118s3.596-.213 5.71-2.435H0V4.515h6.417v5.278l.144-.001 2.622-5.277h4.854v5.244h.144l2.72-5.244H24Z"/></svg><b style="color:#146EF5">Webflow</b></span>'

# ================= PACKAGES (tabbed pricing) =================
import re as _re
SUIT = "Suitable for potential super-startups and brand revamps for companies."
SUIT2 = "Suitable for startups and brand revamps for companies."
ANIM = "Get animations made for your business — custom-made and affordable animation plans."
SEO6 = "(6 months plan)"
VECTOR = "Vector Formats (AI, PSD, EPS, PNG, GIF, JPG, PDF)"
SEO_BASE = ["Prior Analysis", "Business Analysis", "Consumer Analysis", "Competitor Analysis"]
SEO_TAIL = ["Webpage Optimization", "Meta Tags Creation"]

PACKAGES = {
 "website": {
   "label": "Website",
   "title": "Flexible Website Development Packages for Every Business",
   "intro": "Whether you're launching a new brand or scaling an existing one, Webratron offers custom website development packages tailored to your goals. Our solutions are built for performance, scalability, and conversion, ensuring your website works as hard as you do.",
   "sub": {
     "website": ("Website", [
       ("Startup Website Package", "$469.00", "$938.00", SUIT, ["3 Page", "5 Stock Images", "1 jQuery Slider Banner", "3 Banner Design", "Contact/Query Form", "Social Media Integration", "Complete W3C Certified HTML", "48 to 72 hours TAT"]),
       ("Standard Website Package", "$869.00", "$1938.00", SUIT, ["5 Page", "10 Stock Images", "1 jQuery Slider Banner", "5 Banner Design", "Contact/Query Form", "Social Media Integration", "Complete W3C Certified HTML", "48 to 72 hours TAT"]),
       ("Professional Package", "$1269.00", "$2938.00", SUIT, ["10 Page", "15 Premium Stock Images", "5 Banner Design", "Social Media Integration", "Contact/Query Form", "Complete W3C Certified HTML", "48 to 72 hours TAT", "Complete Deployment"]),
       ("Business Package", "$1969.00", "$4938.00", SUIT, ["20 Page", "15 Premium Stock Images", "1 jQuery Slider Banner", "5 Banner Design", "Social Media Integration", "Industry Specified Team of Expert Designers and Developers", "Contact/Query Form"]),
       ("Customized Web Portal", "$5499.00", "$10,998.00", SUIT, ["Complete Custom Design & Development", "Dating Portal, Job Portal, Professional Network Portal, Social Network Portal, Restaurant Portal, Medical Portal, Enterprise Portal (Any One)", "Unique, User Friendly, Interactive, Dynamic, High End UI Design"]),
     ]),
     "ecommerce": ("Ecommerce", [
       ("Basic Ecommerce Package", "$669.00", "$1338.00", SUIT, ["Up to 10 Products", "5 Stock Images", "1 jQuery Slider Banner", "3 Banner Design", "Contact/Query Form", "Social Media Integration", "Complete W3C Certified HTML", "48 to 72 hours TAT", "Mobile Responsive", "Free Google Friendly Sitemap", "Ownership Rights & Unique Design", "Moneyback Guarantee"]),
       ("Standard Ecommerce Package", "$1769.00", "$3538.00", SUIT, ["Up to 50 Products", "15 Premium Stock Images", "1 jQuery Slider Banner", "5 Banner Design", "CMS / Admin Panel Support", "Custom Forms", "Special Hover Effects", "Online Reservation/Appointment Tool", "Lead Capturing Forms", "Contact/Query Form", "Social Media Integration", "Complete Deployment", "Free Google Friendly Sitemap", "Ownership Rights & Unique Design"]),
       ("Professional Ecommerce Package", "$2969.00", "$5938.00", SUIT, ["Up to 100 Products", "CMS / Admin Panel Support", "Payment Gateway Integration", "Shopping Cart Integration", "Customer Login Area", "Custom Forms", "Special Hover Effects", "Social Media Integration", "Complete Deployment", "Free Google Friendly Sitemap", "Ownership Rights & Unique Design"]),
       ("Business Ecommerce Package", "$4969.00", "$9938.00", SUIT, ["500+ Products", "Client Dashboard", "Search Engine Indexing Setup", "CMS / Admin Panel Support", "Payment Gateway Integration", "Shopping Cart Integration", "Customer Login Area", "Custom Forms", "Social Media Integration", "Complete Deployment", "Free Google Friendly Sitemap", "Ownership Rights & Unique Design"]),
     ]),
     "shopify": ("Shopify", [
       ("Basic Shopify Package", "$699.00", "$1399.00", SUIT, ["Custom Designed Homepage (1x Concept)", "5 Inner Pages", "Up to 50 Products", "Up to 7 Categories", "Content Management System", "Payment Gateway Integration", "Mobile Responsive", "30 Days Free Maintenance (Post-launch Support)", "Live Chat Integration (add-on $249)"]),
       ("Standard Shopify Package", "$2299.00", "$4599.00", SUIT, ["Up to 1,000 Products", "Up to 20 Categories", "20 Inner Pages", "Customer Login", "Shopping Cart & Guest Checkout", "Product Ratings & Reviews", "Promotional Banners", "Product Offers System", "Product Sorting (Newest, Featured, Popular, Best Seller)", "1 Year Free Hosting", "1 Year Free Domain"]),
       ("Professional Shopify Package", "$2799.00", "$5599.00", SUIT, ["Unlimited Products", "Unlimited Categories", "Unlimited Inner Pages", "Unlimited Promotional Banners", "Custom Coding", "Product Return Management System", "Reward Points System", "Bulk CSV Products Upload", "Automated Emails", "Professional Content Writing (extra cost)"]),
     ]),
     "webapp": ("Web App Development", None),
   },
 },
 "logo": {
   "label": "Logo Design",
   "title": "Our Logo Design Packages",
   "intro": "Your visions can become a reality thanks to our talented team of graphic designers. We design logos that are distinctive in style and consistent with the objectives of your business.",
   "cards": [
     ("Startup Package", "$75", "$99", SUIT, ["4 Design Concepts", "2 Revisions", "2 Dedicated Designers", "Jpeg PNG Format", "Ownership Rights & Unique Design", "Moneyback Guarantee"]),
     ("Standard Package", "$149", "$199", SUIT, ["8 Design Concepts", "Unlimited Revisions", "2 Dedicated Designer", VECTOR, "Icon Design", "Banner Design", "Ownership Rights & Unique Design"]),
     ("Professional Package", "$199", "$249", SUIT, ["12 Design Concepts", "3 Dedicated Designer", VECTOR, "Unlimited Revisions", "Business Card Design", "Letterhead Design", "Envelope Design", "Icon Design"]),
     ("Business Package", "$360.00", "$738.00", SUIT, ["Unlimited Original Logo Concepts", "4 Dedicated Designer", VECTOR, "Unlimited Revisions", "Business Card Design", "Letterhead Design", "Envelope Design"]),
     ("Premium Package", "$425.00", "$938.00", SUIT2, ["Unlimited Original Logo Concepts", "4 Dedicated Designer", VECTOR, "Unlimited Revisions", "Business Card Design", "Letterhead Design", "Envelope Design"]),
     ("3D Logo Design Package", "$499.00", "$2338.00", SUIT2, ["3 Unique 3D Logo Concepts", "Light Effects and VFX", "Fully Rendered", "Multiple 3D Angles", "3 Dedicated Designers", "72 Business Hours Turn Around Time", "Unlimited Revisions"]),
   ],
 },
 "seo": {
   "label": "SEO",
   "title": "Our SEO Packages",
   "intro": "By providing a range of packages, we give clients the information they need to improve their visibility, reach, and organic search rankings on search engines.",
   "cards": [
     ("Basic SEO Package", "$3500", "$7000", SEO6, SEO_BASE + ["15 Selected Keywords Targeting", "15 Pages Keyword Targeted"] + SEO_TAIL),
     ("Premium SEO Package", "$6000", "$12000", SEO6, SEO_BASE + ["30 Selected Keywords Targeting", "30 Pages Keyword Targeted"] + SEO_TAIL),
     ("Platinum SEO Package", "$8000", "$16000", SEO6, SEO_BASE + ["30 Selected Keywords Targeting", "30 Pages Keyword Targeted"] + SEO_TAIL),
   ],
 },
 "mobile": {"label": "Mobile App", "title": "Our App Development Packages", "intro": "Cross-platform iOS and Android apps built with Flutter — from concept and UI/UX design to launch on the app stores.", "cards": None},
 "branding": {"label": "Branding", "title": "Our Branding Packages", "intro": "Logos, stationery and social media design that give your business a consistent, professional identity everywhere.", "cards": None},
 "animation": {
   "label": "Animations",
   "title": "Our Animations Packages",
   "intro": "Our animated videos have the ability to captivate viewers and keep them watching, which benefits businesses by increasing website traffic and generating income.",
   "cards": [
     ("Basic Animation Package", "$499", "$1598", ANIM, ["30 Second Video", "Professional Script", "Storyboard", "Animation", "Voice-Over & Sound Effects", "4 Weeks Delivery", "Unlimited Revisions", "Dedicated Project Manager"]),
     ("Classic Animation Package", "$999", "$2198", ANIM, ["60 Second Video", "Professional Script", "Sample Theme", "Storyboard", "Animation", "Voice-Over & Sound Effects", "5 Weeks Delivery", "Dedicated Project Manager"]),
     ("Premium Animation Package", "$1499", "$2998", ANIM, ["90 Second Video", "Professional Script", "Sample Theme", "Storyboard", "Animation", "Voice-Over & Sound Effects", "6 Weeks Delivery", "Dedicated Project Manager"]),
     ("Unlimited Animation Package", "$2299", "$4590", ANIM, ["120 Second Video", "Professional Script", "Sample Theme", "Storyboard", "Animation", "Voice-Over & Sound Effects", "Dedicated Project Manager", "Ownership Rights & Unique Design"]),
   ],
 },
}

def _slug(t): return _re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def pkg_card(name, price, was, desc, feats):
    lis = "".join(f"<li>{f}</li>" for f in feats)
    q = _slug(name)
    return f'''<article class="pkg">
          <h3 class="pkg__name">{name}</h3>
          <div class="pkg__price"><strong>{price}</strong><s>{was}</s></div>
          <p class="pkg__desc">{desc}</p>
          <ul class="pkg__list">{lis}</ul>
          <div class="pkg__actions"><a href="contact.html?package={q}" class="pkg__btn pkg__btn--order">Order Now</a><button type="button" class="pkg__btn pkg__btn--details" aria-expanded="false">View Details</button></div>
        </article>'''

def pkg_quote(label):
    return f'''<div class="pkg-quote">
          <h3>Custom {label} packages</h3>
          <p>Every {label.lower()} project is different. Tell us what you need and we'll send you a tailored package and price.</p>
          <div class="hero__actions" style="justify-content:center;margin:0"><a href="contact.html" class="pkg__btn pkg__btn--details">Get a Custom Quote</a><a href="tel:{PHONE_TEL}" class="pkg__btn pkg__btn--order">Call {PHONE}</a></div>
        </div>'''

def pkg_grid(cards, label):
    if not cards: return pkg_quote(label)
    return '<div class="pkg-grid">' + "\n        ".join(pkg_card(*c) for c in cards) + '</div>'

def packages_section(uid="pk"):
    tabs, panels = [], []
    for i, (key, d) in enumerate(PACKAGES.items()):
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button type="button" role="tab" class="pk-tab{" is-active" if i == 0 else ""}" id="{uid}-tab-{key}" aria-controls="{uid}-{key}" aria-selected="{sel}" data-tab="{uid}-{key}">{d["label"]}</button>')
        if "sub" in d:
            stabs, spanels = [], []
            for j, (sk, (sl, cards)) in enumerate(d["sub"].items()):
                ssel = "true" if j == 0 else "false"
                stabs.append(f'<button type="button" role="tab" class="pk-tab pk-tab--sub{" is-active" if j == 0 else ""}" aria-controls="{uid}-{key}-{sk}" aria-selected="{ssel}" data-tab="{uid}-{key}-{sk}">{sl}</button>')
                spanels.append(f'<div class="pk-panel pk-panel--sub" id="{uid}-{key}-{sk}" role="tabpanel"{"" if j == 0 else " hidden"}>{pkg_grid(cards, sl)}</div>')
            body = f'<div class="pk-tabs pk-tabs--sub" role="tablist" aria-label="{d["label"]} package types">{"".join(stabs)}</div>' + "".join(spanels)
        else:
            body = pkg_grid(d["cards"], d["label"])
        panels.append(f'''<div class="pk-panel" id="{uid}-{key}" role="tabpanel" aria-labelledby="{uid}-tab-{key}"{"" if i == 0 else " hidden"}>
        <div class="pk-head"><h2>{d["title"]}</h2><p>{d["intro"]}</p></div>
        {body}
      </div>''')
    return f'''
<section class="packages" id="packages">
  <div class="container">
    <div class="pk-tabs" role="tablist" aria-label="Package categories">{"".join(tabs)}</div>
    {"".join(panels)}
  </div>
</section>'''

COMBO = [
 ("Logo Design", ["8 Custom Logo Design Concepts", "By 2 Expert Designers", "Icon Design", "All File Formats (PSD, PDF, AI, JPEG, PNG)"]),
 ("Stationery", ["Business Card, Letterhead, Envelope, Fax Template", "MS Word Letterhead", "Electronic Invoice Template"]),
 ("Social Media", ["Facebook Page Design", "Instagram Page Design", "LinkedIn Page Design", "YouTube Page Design"]),
 ("Website", ["15 Pages Website", "Custom Made, Interactive, Dynamic & High End Design", "Custom WP (or) Custom PHP Development", "6 jQuery Slider Banner", "Up to 10 Custom Made Banner Designs", "20 Stock Images", "Unlimited Revisions", "Special Hover Effects", "CMS / Admin Panel Support", "Online Appointment/Scheduling/Online Ordering Integration", "Online Payment Integration", "Custom Dynamic Forms", "Newsletter Subscription", "Newsfeed Integration", "Signup Area (For Newsletters, Offers etc.)", "Search Bar", "Free Google Friendly Sitemap", "Social Media Integration", "Search Engine Submission", "Complete W3C Certified HTML", "Industry Specified Team of Expert Designers and Developers", "Cross Browser Compatible", "Complete Designing", "Facebook Page Design", "Instagram Page Design", "YouTube Page Design", "Complete Deployment", "24 to 48 Hours Turnaround Time"]),
 ("Value Added Services", ["All Final File Formats", "Dedicated Account Manager", "Ownership Rights & Unique Design", "Moneyback Guarantee"]),
]
def combo_section():
    groups = {g: "".join(f"<li>{x}</li>" for x in items) for g, items in COMBO}
    return f'''
<section class="packages packages--combo">
  <div class="container">
    <div class="combo">
      <div class="combo__sale" aria-hidden="true"><small>Up to 50%</small><b>SUPER<br>SALE</b></div>
      <span class="combo__kicker">Combo Package</span>
      <h2 class="combo__title">Business Starter Package</h2>
      <div class="combo__cols">
        <div>
          <h3>Logo Design</h3><ul>{groups["Logo Design"]}</ul>
          <h3>Stationery</h3><ul>{groups["Stationery"]}</ul>
          <h3>Social Media</h3><ul>{groups["Social Media"]}</ul>
        </div>
        <div class="combo__web">
          <h3>Website</h3><ul class="combo__webl">{groups["Website"]}</ul>
          <h3>Value Added Services</h3><ul class="combo__webl">{groups["Value Added Services"]}</ul>
        </div>
      </div>
      <div class="combo__foot">
        <div class="combo__contact"><a href="tel:{PHONE_TEL}">{icon("phone")} {PHONE}</a><a href="contact.html">{icon("chat")} Live Chat</a><small>For more information speak with us</small></div>
        <div class="combo__price"><s>$3,999.00</s><strong>$1999.00</strong></div>
        <a href="contact.html?package=business-starter-package" class="pkg__btn pkg__btn--details combo__cta">Activate Now</a>
      </div>
    </div>
  </div>
</section>'''

PACKAGES_HTML = packages_section("hp")
COMBO_HTML = combo_section()


# ================= HOME =================
import json

# ================= HOME v3 (new creative layout) =================
def _num(p): return float(p.replace("$", "").replace(",", ""))

def calc_config():
    W = {n: (p, w, f) for (n, p, w, d, f) in PACKAGES["website"]["sub"]["website"][1]}
    E = {n: (p, w, f) for (n, p, w, d, f) in PACKAGES["website"]["sub"]["ecommerce"][1]}
    S = {n: (p, w, f) for (n, p, w, d, f) in PACKAGES["website"]["sub"]["shopify"][1]}
    def pk(src, name, upto):
        p, w, f = src[name]
        return {"name": name, "price": _num(p), "was": _num(w), "feats": f[:6], "upto": upto}
    return {
      "website": {"label": "How many pages do you need?", "unit": "pages",
                  "steps": [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25], "plusLast": True,
                  "tiers": [pk(W, "Startup Website Package", 3), pk(W, "Standard Website Package", 5), pk(W, "Professional Package", 10),
                            pk(W, "Business Package", 20), pk(W, "Customized Web Portal", 10**9)]},
      "ecommerce": {"label": "How many products will you sell?", "unit": "products",
                    "steps": [10, 25, 50, 100, 250, 500], "plusLast": True,
                    "tiers": [pk(E, "Basic Ecommerce Package", 10), pk(E, "Standard Ecommerce Package", 50),
                              pk(E, "Professional Ecommerce Package", 100), pk(E, "Business Ecommerce Package", 10**9)]},
      "shopify": {"label": "How many products in your Shopify store?", "unit": "products",
                  "steps": [25, 50, 200, 500, 1000, 5000], "plusLast": True,
                  "tiers": [pk(S, "Basic Shopify Package", 50), pk(S, "Standard Shopify Package", 1000), pk(S, "Professional Shopify Package", 10**9)]},
      "addons": [{"id": "logo", "name": "Logo Design (Standard)", "price": 149},
                 {"id": "video", "name": "30-sec Animation Video", "price": 499},
                 {"id": "seo", "name": "Basic SEO (6 months)", "price": 3500}],
    }

def calculator():
    cfg = json.dumps(calc_config()).replace("'", "&#39;")
    return f'''
<section class="section calc-sec" id="calculator">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow reveal">Instant estimate</span>
      <h2 class="reveal">Build your package <span class="grad-text">in seconds</span></h2>
      <p class="reveal">Pick what you need and we'll match you with the right Webratron package — no forms, no waiting.</p>
    </div>
    <div class="calc reveal" data-config='{cfg}'>
      <div class="calc__controls">
        <fieldset class="calc__step">
          <legend><span class="calc__n">1</span>What are we building?</legend>
          <div class="calc__types" role="radiogroup">
            <label><input type="radio" name="calc-type" value="website" checked><span>{icon("web")}Website</span></label>
            <label><input type="radio" name="calc-type" value="ecommerce"><span>{icon("cart")}E-commerce</span></label>
            <label><input type="radio" name="calc-type" value="shopify"><span>{icon("bolt")}Shopify</span></label>
          </div>
        </fieldset>
        <div class="calc__step">
          <label for="calc-range" class="calc__legend"><span class="calc__n">2</span><span data-calc-label>How many pages do you need?</span></label>
          <div class="calc__range">
            <input type="range" id="calc-range" min="0" max="11" value="2" step="1">
            <output for="calc-range" data-calc-out>3 pages</output>
          </div>
        </div>
        <fieldset class="calc__step">
          <legend><span class="calc__n">3</span>Add extras</legend>
          <div class="calc__addons" data-calc-addons></div>
        </fieldset>
      </div>
      <aside class="calc__summary" aria-live="polite">
        <small>Recommended for you</small>
        <h3 data-calc-name>Startup Website Package</h3>
        <div class="calc__price"><strong data-calc-price>$469</strong><s data-calc-was>$938</s></div>
        <ul data-calc-feats></ul>
        <div class="calc__lines" data-calc-lines></div>
        <div class="calc__total"><span>Estimated total</span><strong data-calc-total>$469</strong></div>
        <p class="calc__save" data-calc-save>You save $469</p>
        <a href="contact.html" class="btn btn--primary btn--block" data-calc-cta>Get this quote {ARROW}</a>
        <p class="calc__note">Estimate based on our published packages. Final quote confirmed after a free consultation.</p>
      </aside>
    </div>
  </div>
</section>'''

def bento():
    tiles = []
    layout = {"web-design": "big", "branding": "wide", "video": "wide"}
    for sid, ic, name, text, tags in SERVICES:
        kind = layout.get(sid, "")
        art = scene(sid) if kind else ""
        tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
        tiles.append(f'''<a href="{SVC_URL[sid]}" class="tile tile--{kind or "sm"} reveal">
        <div class="tile__body"><div class="icon">{icon(ic)}</div><h3>{name}</h3><p>{text}</p><div class="tags">{tag_html}</div><span class="tile__go" aria-hidden="true">{ARROW}</span></div>
        {f'<div class="tile__art">{art}</div>' if art else ""}
      </a>''')
    tiles.insert(4, f'''<a href="{TRUSTPILOT}" target="_blank" rel="noopener" class="tile tile--stat reveal"><strong>4.7<span>★</span></strong><p>Rated on Trustpilot<br>5.0 on ProvenExpert</p></a>''')
    tiles.append(f'''<a href="contact.html" class="tile tile--cta reveal"><div><h3>Not sure what you need?</h3><p>Get a free consultation and a clear plan for your brand.</p></div><span class="btn btn--primary">Talk to us {ARROW}</span></a>''')
    return "\n      ".join(tiles)

def stack():
    out = []
    for i, (t, d) in enumerate(PROCESS):
        out.append(f'''<article class="stack__card" style="--i:{i}">
        <span class="stack__num">0{i+1}</span>
        <div><h3>{t}</h3><p>{d}</p></div>
        <div class="stack__art">{scene(["web-design", "branding", "development", "seo"][i])}</div>
      </article>''')
    return "\n      ".join(out)

def tslider():
    slides = "".join(f'''<figure class="tslide{" is-active" if i == 0 else ""}" data-slide="{i}"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div><blockquote>“{q}”</blockquote><figcaption>Trustpilot review · {role}</figcaption></figure>''' for i, (role, q) in enumerate(TESTIMONIALS))
    dots = "".join(f'<button type="button" class="tdot{" is-active" if i == 0 else ""}" data-go="{i}" aria-label="Show review {i+1}"></button>' for i in range(len(TESTIMONIALS)))
    return f'<div class="tslider" data-slider>{slides}<div class="tdots">{dots}</div></div>'

KINETIC = "".join(f'<span>{w}</span><i>✦</i>' for w in ["Web Design", "Shopify Stores", "Mobile Apps", "Logo Design", "SEO", "2D Animation", "Branding", "E-commerce"])

home = f'''
<section class="hero hero--v2 hero--inset">
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
        <a href="contact.html" class="btn btn--primary btn--lg magnetic">Get Your Website in 24 Hours {ARROW}</a>
        <a href="#calculator" class="btn btn--ghost btn--lg">Estimate my price</a>
      </div>
      <div class="hero__reviews reveal" data-delay="3">
        <img src="assets/img/trust-logos.webp" alt="Reviewed on Bark, Clutch, Google and Trustpilot" width="946" height="92">
      </div>
    </div>
    <div class="hero__art reveal" data-delay="2" data-parallax>
      <div class="hero__ring"></div>
      <img src="assets/img/hero-visual.webp" alt="Classical statue stepping out of a smartphone in front of a glowing planet" width="740" height="785" fetchpriority="high">
      <div class="float-chip float-chip--1" data-depth="18"><span class="dot">★</span><div><strong>4.7 / 5</strong><small>Trustpilot rating</small></div></div>
      <div class="float-chip float-chip--2" data-depth="28"><span class="dot dot--orange">⚡</span><div><strong>24 Hours</strong><small>Fast delivery</small></div></div>
      <div class="float-chip float-chip--3" data-depth="12"><span class="dot dot--cyan">$</span><div><strong>From $469</strong><small>Business websites</small></div></div>
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

<section class="kinetic" aria-hidden="true">
  <div class="kinetic__track">{KINETIC}{KINETIC}</div>
  <div class="kinetic__track kinetic__track--rev">{KINETIC}{KINETIC}</div>
</section>

<section class="section">
  <div class="container">
    <div class="split-head">
      <div><span class="eyebrow reveal">What we do</span>
      <h2 class="reveal">Everything you need to <span class="grad-text">win online</span></h2></div>
      <p class="reveal">From your first logo to a full-scale web platform — one team, one vision, end-to-end. Tap any service to explore.</p>
    </div>
    <div class="bento">
      {bento()}
    </div>
  </div>
</section>

{PACKAGES_HTML}
{COMBO_HTML}
{calculator()}

<section class="section stack-sec">
  <div class="container stack-wrap">
    <div class="stack-intro">
      <span class="eyebrow reveal">How we work</span>
      <h2 class="reveal">A simple, proven <span class="grad-text">process</span></h2>
      <p class="reveal">Clear steps, no surprises — you're involved and informed from day one.</p>
      <a href="contact.html" class="btn btn--primary reveal">Start your project {ARROW}</a>
    </div>
    <div class="stack">
      {stack()}
    </div>
  </div>
</section>

<section class="section section--alt work-sec">
  <div class="container">
    <div class="split-head">
      <div><span class="eyebrow reveal">What we create</span>
      <h2 class="reveal">Work across <span class="grad-text">every channel</span></h2></div>
      <div class="hs-nav"><button type="button" class="hs-btn" data-hs="-1" aria-label="Scroll left">←</button><button type="button" class="hs-btn" data-hs="1" aria-label="Scroll right">→</button></div>
    </div>
  </div>
  <div class="hscroll" tabindex="0" aria-label="Our work">
{work_cards()}
  </div>
</section>

<section class="section">
  <div class="container testi-wrap">
    <div class="testi-stats">
      <div class="stat reveal"><strong class="grad-text">4.7★</strong><span>Trustpilot rating</span></div>
      <div class="stat reveal" data-delay="1"><strong class="grad-text">5.0★</strong><span>ProvenExpert score</span></div>
      <div class="stat reveal" data-delay="2"><strong class="grad-text">24h</strong><span>Fastest delivery</span></div>
      <div class="stat reveal" data-delay="3"><strong class="grad-text">100%</strong><span>Design ownership</span></div>
    </div>
    <div class="testi-card reveal">
      <span class="eyebrow">Client love</span>
      {tslider()}
      <a href="{TRUSTPILOT}" target="_blank" rel="noopener" class="card__link">Read all reviews on Trustpilot {ARROW}</a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container faq-split">
    <div class="faq-split__head">
      <span class="eyebrow reveal">FAQ</span>
      <h2 class="reveal">Questions? <span class="grad-text">Answered.</span></h2>
      <p class="reveal">Can't find what you're looking for? Our team is one message away.</p>
      <a href="contact.html" class="btn btn--ghost reveal">Ask a question {ARROW}</a>
    </div>
    <div class="faq">
{faqs()}
    </div>
  </div>
</section>

<section class="mega-cta">
  <div class="container">
    <div class="mega-cta__box">
      <div class="starfield"></div>
      <p class="mega-cta__kicker">Ready when you are</p>
      <h2>Let's build something <span class="grad-text">remarkable.</span></h2>
      <div class="mega-cta__row">
        <a href="contact.html" class="mega-btn magnetic"><span>Start a project</span>{ARROW}</a>
        <div class="mega-cta__contact"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE_TEL}">{PHONE}</a></div>
      </div>
    </div>
  </div>
</section>
'''

page("index.html", "Website Design & Development Company in New York | Webratron",
     "Custom website design from $469, Shopify & e-commerce stores, mobile apps, logo design, SEO and explainer videos. Rated 4.7/5 on Trustpilot. Get a free quote.",
     home, "index.html", extra_nodes=[faq_node(FAQS)])

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
      <div class="hero__actions" style="margin:0"><a href="contact.html?service={sid}" class="btn btn--primary reveal">Start your project {ARROW}</a><a href="{SVC_URL[sid]}" class="btn btn--ghost reveal">{name} details</a></div>
    </div>
    <div class="visual-panel reveal" data-delay="1" aria-hidden="true">
      <div class="bg-grid"></div>
      {scene(sid)}
    </div>
  </div>
</section>''')
services = page_hero("Services", "Our services", 'Digital services that <span class="grad-text">drive results</span>',
    "Strategy, design, development and growth — everything your brand needs online, delivered by one dedicated team.") + f'''
<section class="section" style="padding-top:20px">
  <div class="container">
    <h2 class="sr-only">All services</h2>
    <div class="grid grid--4">
{service_cards()}
    </div>
  </div>
</section>''' + "".join(blocks) + f'''
<section class="section section--light">
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
     services, "services.html", crumbs=[("Home", "index.html"), ("Services", "services.html")])

# ================= PORTFOLIO =================
portfolio = page_hero("Work", "Portfolio", 'Work that <span class="grad-text">speaks for itself</span>',
    "Websites, apps, logos and videos — explore the kinds of projects we build for our clients.") + f'''
<section class="section" style="padding-top:20px">
  <div class="container">
    <h2 class="sr-only">Our work</h2>
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
<section class="section section--light">
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
     portfolio, "portfolio.html", crumbs=[("Home", "index.html"), ("Portfolio", "portfolio.html")])

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
<section class="section section--light" style="padding-top:20px">
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
<section class="section section--light">
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
     about, "about.html", crumbs=[("Home", "index.html"), ("About", "about.html")])

# ================= PRICING =================
pricing = page_hero("Pricing", "Pricing", 'Packages for <span class="grad-text">every business</span>',
    "Packages for websites, logos, SEO and animation — with full ownership of your design.") + f'''
{packages_section("pp")}
{COMBO_HTML}
<section class="section section--light">
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
     pricing, "pricing.html", faq_schema(), crumbs=[("Home", "index.html"), ("Pricing", "pricing.html")])

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
        <h2 style="font-size:1.1rem">What happens next?</h2>
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
     contact, "contact.html", crumbs=[("Home", "index.html"), ("Contact", "contact.html")])

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
    <h2 class="sr-only">Latest articles</h2>
    <div class="grid grid--3">
{cards}
    </div>
  </div>
</section>''' + cta()
page("blog.html", "Blogs — Web Design & Marketing Tips | Webratron",
     "Web design, development, e-commerce and digital marketing tips from the Webratron team.", blog, "blog.html", crumbs=[("Home", "index.html"), ("Blogs", "blog.html")])

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
    iso = {"Nov 2026": "2026-11-01", "Oct 2026": "2026-10-01", "Sep 2026": "2026-09-01"}.get(date, "2026-11-01")
    post_node = {"@type": "BlogPosting", "headline": title, "description": excerpt, "datePublished": iso, "dateModified": "2026-11-19",
                 "author": {"@id": SITE + "/#org"}, "publisher": {"@id": SITE + "/#org"}, "image": SITE + "/assets/img/og-image.jpg",
                 "mainEntityOfPage": f"{SITE}/blog-{slug}.html", "inLanguage": "en"}
    page(f"blog-{slug}.html", f"{title} | Webratron Blog", excerpt, html, "blog.html",
         crumbs=[("Home", "index.html"), ("Blogs", "blog.html"), (title, f"blog-{slug}.html")], extra_nodes=[post_node], priority=0.6)


# ================= SEO SERVICE PAGES + PPC LANDING PAGES =================
def _pk(sub=None, key=None):
    if sub: return PACKAGES["website"]["sub"][sub][1]
    return PACKAGES[key]["cards"]

def _range(cards):
    ps = [_num(c[1]) for c in cards]
    return min(ps), max(ps)

SVC = {
 "web-design": dict(
   title="Custom Website Design Services | From $469 | Webratron",
   desc="Custom, mobile-first website design for startups and small businesses. Packages from $469, delivered in 48–72 hours, with full design ownership.",
   h1='Custom Website Design <span class="grad-text">That Converts</span>',
   kw="website design", lead="Webratron designs custom, mobile-first websites for startups and growing businesses. Packages start at $469 for a 3-page Startup Website and standard packages are delivered in 48 to 72 hours — with full ownership of your design.",
   cards=lambda: _pk(sub="website"), stype="Website design",
   facts=[("Starting price", "$469 (Startup Website, 3 pages)"), ("Delivery", "48–72 hours for standard packages"), ("Ownership", "100% ownership rights to your design"), ("Platforms", "WordPress, custom HTML/PHP, Shopify")],
   faqs=[("How much does a custom website design cost?", "At Webratron, website design packages start at $469 for a 3-page Startup Website. Standard (5 pages) is $869, Professional (10 pages) is $1,269, Business (20 pages) is $1,969, and a customized web portal starts at $5,499."),
         ("How long does it take to design a website?", "Standard website packages are delivered in 48 to 72 hours after we receive your content. Larger or custom projects are scheduled with clear milestones before work begins."),
         ("Will my website be mobile-friendly and SEO-ready?", "Yes. Every website is fully responsive across devices and browsers, uses W3C-certified HTML, and includes on-page SEO basics such as clean structure, meta tags and a Google-friendly sitemap."),
         ("Do I own my website design?", "Yes. All Webratron packages include full ownership rights to your unique design once the project is complete.")]),
 "development": dict(
   title="Web Development Company | WordPress & Custom Websites | Webratron",
   desc="Fast, secure, scalable web development — WordPress, custom PHP and web apps. Website packages from $469 with complete deployment and CMS options.",
   h1='Web Development <span class="grad-text">Built to Perform</span>',
   kw="web development", lead="Webratron builds fast, secure and scalable websites and web applications using WordPress, custom PHP, React and Next.js. Website packages start at $469, and Professional packages include CMS support and complete deployment.",
   cards=lambda: _pk(sub="website"), stype="Web development",
   facts=[("Technologies", "WordPress, custom PHP, React, Next.js, Shopify"), ("Starting price", "$469"), ("Includes", "W3C-certified HTML, deployment, CMS options"), ("Custom portals", "From $5,499")],
   faqs=[("Should I choose WordPress or a custom-built website?", "WordPress is ideal if you want to edit content yourself and launch quickly. A custom build suits unique features, portals or integrations. We recommend the right option after a free consultation."),
         ("Can you redesign or rebuild my existing website?", "Yes. We can redesign, rebuild or migrate an existing website while keeping your content and protecting the SEO value you have already built."),
         ("Do you handle deployment and launch?", "Yes. Our Professional package and above include complete deployment, so your site goes live without you needing to deal with servers."),
         ("Can you build web applications and portals?", "Yes. Our Customized Web Portal package starts at $5,499 and covers job, dating, social network, restaurant, medical and enterprise portals.")]),
 "mobile": dict(
   title="Mobile App Development Company | Flutter iOS & Android | Webratron",
   desc="Cross-platform mobile app development with Flutter for iOS and Android — UI/UX design, backend, push notifications and app store publishing.",
   h1='Mobile App Development <span class="grad-text">for iOS &amp; Android</span>',
   kw="mobile app development", lead="Webratron develops cross-platform mobile apps with Flutter, so one codebase runs on both iOS and Android. We handle UI/UX design, development, backend integration and App Store and Google Play publishing. Every app is quoted to your exact requirements.",
   cards=lambda: None, stype="Mobile app development",
   facts=[("Framework", "Flutter (one codebase for iOS & Android)"), ("Includes", "UI/UX, development, backend, store publishing"), ("Pricing", "Custom quote based on features"), ("Reviews", "Clients praise on-time delivery and communication")],
   faqs=[("How much does it cost to build a mobile app?", "App cost depends on features, screens and integrations. Webratron provides a free consultation and a fixed custom quote before development begins."),
         ("Why use Flutter for app development?", "Flutter lets us build one codebase that runs natively on both iOS and Android, which reduces cost and development time while keeping performance high."),
         ("Do you publish apps to the App Store and Google Play?", "Yes. We handle store listings and publishing for both the Apple App Store and Google Play."),
         ("Can you design the app UI as well?", "Yes. Our team designs the app's UI/UX before development so you can review screens and flows early.")]),
 "branding": dict(
   title="Professional Logo Design Services | From $75 | Webratron",
   desc="Custom logo design from $75 with 4–12 concepts, unlimited revisions on most packages, vector files and full ownership. 3D logos from $499.",
   h1='Professional Logo Design <span class="grad-text">From $75</span>',
   kw="logo design", lead="Webratron creates custom logos that are distinctive and consistent with your business goals. Logo packages start at $75 for 4 design concepts, the Standard package at $149 includes 8 concepts with unlimited revisions, and 3D logo design starts at $499.",
   cards=lambda: _pk(key="logo"), stype="Logo design",
   facts=[("Starting price", "$75 (4 concepts)"), ("Most popular", "$149 — 8 concepts, unlimited revisions"), ("File formats", "AI, PSD, EPS, PNG, GIF, JPG, PDF"), ("Ownership", "Full ownership rights to your logo")],
   faqs=[("How much does a professional logo cost?", "Webratron logo packages are $75 (Startup), $149 (Standard), $199 (Professional), $360 (Business), $425 (Premium) and $499 for 3D logo design."),
         ("How many logo concepts will I get?", "Between 4 and 12 initial concepts depending on the package, and unlimited original concepts on the Business and Premium packages."),
         ("What file formats are included?", "Standard and higher packages include vector formats: AI, PSD, EPS, PNG, GIF, JPG and PDF."),
         ("Do I own the final logo?", "Yes. You receive full ownership rights to your unique logo design.")]),
 "ecommerce": dict(
   title="Shopify & E-commerce Website Development | From $669 | Webratron",
   desc="Shopify stores from $699 and custom e-commerce websites from $669 — payment gateways, product catalogues, carts and mobile-friendly checkout.",
   h1='Shopify &amp; E-commerce <span class="grad-text">Stores That Sell</span>',
   kw="ecommerce website development", lead="Webratron builds Shopify stores and custom e-commerce websites with product catalogues, payment gateways, shopping carts and fast mobile checkout. Custom e-commerce packages start at $669 and Shopify packages start at $699.",
   cards=lambda: _pk(sub="ecommerce") + _pk(sub="shopify"), stype="E-commerce website development",
   facts=[("Shopify", "$699 – $2,799"), ("Custom e-commerce", "$669 – $4,969"), ("Products", "From 10 up to unlimited"), ("Includes", "Payments, cart, CMS, mobile-responsive")],
   faqs=[("Should I build my store on Shopify or WooCommerce?", "Choose Shopify for a fast, hosted store with minimal maintenance. Choose WordPress with WooCommerce for maximum flexibility and content-heavy marketing. Read our Shopify vs WordPress guide for a full comparison."),
         ("How much does an e-commerce website cost?", "Custom e-commerce packages are $669, $1,769, $2,969 and $4,969. Shopify packages are $699, $2,299 and $2,799, depending on products, pages and features."),
         ("How many products can my store have?", "From up to 10 products on the Basic e-commerce package to 500+ on Business, and unlimited products on the Professional Shopify package."),
         ("Do you set up payment gateways?", "Yes. We integrate payment gateways and shopping carts so customers can check out securely on any device.")]),
 "seo": dict(
   title="SEO Services | 6-Month SEO Plans from $3,500 | Webratron",
   desc="Results-focused SEO services: business, consumer and competitor analysis, keyword targeting, on-page optimisation and meta tags. 6-month plans from $3,500.",
   h1='SEO Services <span class="grad-text">That Get You Found</span>',
   kw="SEO services", lead="Webratron's SEO services improve your visibility and organic rankings through business, consumer and competitor analysis, keyword targeting and on-page optimisation. Plans run for 6 months: Basic $3,500, Premium $6,000 and Platinum $8,000.",
   cards=lambda: _pk(key="seo"), stype="Search engine optimization",
   facts=[("Plan length", "6 months"), ("Pricing", "$3,500 / $6,000 / $8,000"), ("Keywords", "15–30 targeted keywords"), ("Includes", "Analysis, on-page optimisation, meta tags")],
   faqs=[("How long does SEO take to show results?", "SEO is a long-term investment; meaningful ranking improvements usually build over several months, which is why our plans run for 6 months."),
         ("What is included in your SEO packages?", "Prior, business, consumer and competitor analysis, 15–30 selected target keywords, keyword-targeted pages, webpage optimisation and meta tag creation."),
         ("How much do SEO services cost?", "Our 6-month SEO plans are Basic at $3,500, Premium at $6,000 and Platinum at $8,000."),
         ("Do you offer local SEO?", "Yes. We optimise for local search, including Google Business Profile and location-based keywords.")]),
 "video": dict(
   title="Explainer & 2D Animation Video Services | From $499 | Webratron",
   desc="Whiteboard, 2D explainer and brand-intro animation videos from $499 — professional script, storyboard, voice-over and sound effects included.",
   h1='Animated Explainer Videos <span class="grad-text">From $499</span>',
   kw="animation video", lead="Webratron produces whiteboard, 2D explainer and brand-intro animation videos that keep viewers watching. Packages start at $499 for a 30-second video and include a professional script, storyboard, animation, voice-over and sound effects.",
   cards=lambda: _pk(key="animation"), stype="Video animation",
   facts=[("Starting price", "$499 (30-second video)"), ("Lengths", "30, 60, 90 or 120 seconds"), ("Includes", "Script, storyboard, voice-over, sound effects"), ("Delivery", "4–6 weeks depending on package")],
   faqs=[("How much does an animated explainer video cost?", "Webratron animation packages are $499 (30 seconds), $999 (60 seconds), $1,499 (90 seconds) and $2,299 (120 seconds)."),
         ("What is included in an animation package?", "Every package includes a professional script, storyboard, animation, voice-over and sound effects, plus a dedicated project manager."),
         ("How long does it take to make an animated video?", "Delivery is 4 weeks for the Basic package, 5 weeks for Classic and 6 weeks for Premium."),
         ("What animation styles do you offer?", "Whiteboard animation, 2D explainer videos, 2D brand intros and motion graphics.")]),
 "maintenance": dict(
   title="Website Maintenance Services | Updates, Security & Support | Webratron",
   desc="Website maintenance: plugin, theme and core updates, bug fixes, security hardening and content updates — so your site stays fast and secure.",
   h1='Website Maintenance <span class="grad-text">&amp; Support</span>',
   kw="website maintenance", lead="Webratron keeps your website fast, secure and up to date with plugin, theme and core updates, bug fixes, security hardening and content changes on request. Maintenance is quoted based on your website and needs.",
   cards=lambda: None, stype="Website maintenance",
   facts=[("Covers", "Updates, fixes, security, content changes"), ("Platforms", "WordPress, Shopify, custom sites"), ("Pricing", "Custom quote"), ("Post-launch", "Basic Shopify includes 30 days free maintenance")],
   faqs=[("What does website maintenance include?", "Plugin, theme and core updates, bug fixes and troubleshooting, security hardening and content updates on request."),
         ("Why does my website need maintenance?", "Regular updates keep your site secure, compatible and fast. Outdated plugins and software are a common cause of hacks and broken pages."),
         ("Do you maintain websites you didn't build?", "Yes. We can review and maintain existing WordPress, Shopify and custom websites."),
         ("How much does website maintenance cost?", "Maintenance is quoted to your website's size and needs. Contact us for a free quote.")]),
}

def svc_page(sid):
    d = SVC[sid]; ic, name = [(i, n) for s, i, n, _, _ in SERVICES if s == sid][0]
    fname = SVC_URL[sid]; cards = d["cards"]()
    facts = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in d["facts"])
    feats = "".join(f"<li>{x}</li>" for x in DETAILS[sid])
    faq_html = "\n".join(f'      <details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in d["faqs"])
    others = "".join(f'<a href="{SVC_URL[s]}" class="chip-link">{n}</a>' for s, i2, n, _, _ in SERVICES if s != sid)
    pk_html = pkg_grid(cards, name) if cards else pkg_quote(name)
    body = f'''
<section class="page-hero svc-hero">
  <div class="starfield"></div><div class="orb orb--1"></div><div class="orb orb--2"></div>
  <div class="container svc-hero__grid">
    <div>
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><a href="services.html">Services</a><span aria-hidden="true">/</span><span>{name}</span></nav>
      <h1>{d["h1"]}</h1>
      <p class="svc-hero__lead">{d["lead"]}</p>
      <div class="hero__actions"><a href="contact.html?service={sid}" class="btn btn--primary btn--lg" data-track="cta_click">Get a Free Quote {ARROW}</a><a href="tel:{PHONE_TEL}" class="btn btn--ghost btn--lg" data-track="click_call">Call {PHONE}</a></div>
    </div>
    <div class="svc-hero__art">{scene(sid)}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="container answer-grid">
    <div class="answer reveal">
      <span class="eyebrow">Quick answer</span>
      <h2>What do Webratron's {d["kw"]} services include?</h2>
      <p>{d["lead"]}</p>
      <ul class="checklist">{feats}</ul>
    </div>
    <aside class="facts reveal" aria-label="Key facts">
      <h2>Key facts</h2>
      <dl>{facts}</dl>
      <p class="facts__rating"><span class="stars">★★★★★</span> Rated 4.7/5 on <a href="{TRUSTPILOT}" target="_blank" rel="noopener">Trustpilot</a></p>
    </aside>
  </div>
</section>

<section class="packages" id="packages">
  <div class="container">
    <div class="pk-head"><h2>{name} packages &amp; pricing</h2><p>Transparent packages with full ownership of your work. Not sure which fits? <a href="contact.html?service={sid}">Ask for a free recommendation</a>.</p></div>
    {pk_html}
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head"><span class="eyebrow reveal">How it works</span><h2 class="reveal">Our {d["kw"]} <span class="grad-text">process</span></h2></div>
    <div class="process">
{process()}
    </div>
  </div>
</section>

<section class="section">
  <div class="container faq-split">
    <div class="faq-split__head">
      <span class="eyebrow reveal">FAQ</span>
      <h2 class="reveal">{name}: <span class="grad-text">your questions answered</span></h2>
      <p class="reveal">Still have questions? Call <a href="tel:{PHONE_TEL}">{PHONE}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
    <div class="faq">
{faq_html}
    </div>
  </div>
</section>

<section class="section section--alt section--tight">
  <div class="container text-center">
    <h2 class="related-h">Explore more services</h2>
    <div class="chip-links">{others}</div>
  </div>
</section>
''' + cta()
    lo_hi = _range(cards) if cards else None
    svc_node = {"@type": "Service", "@id": f"{SITE}/{fname}#service", "name": name, "serviceType": d["stype"], "description": d["desc"],
                "provider": {"@id": SITE + "/#org"}, "areaServed": "Worldwide", "url": f"{SITE}/{fname}"}
    if lo_hi:
        svc_node["offers"] = {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": f"{lo_hi[0]:.2f}", "highPrice": f"{lo_hi[1]:.2f}", "offerCount": len(cards)}
        svc_node["hasOfferCatalog"] = {"@type": "OfferCatalog", "name": f"{name} packages", "itemListElement": [
            {"@type": "Offer", "name": c[0], "price": f"{_num(c[1]):.2f}", "priceCurrency": "USD", "url": f"{SITE}/{fname}#packages"} for c in cards]}
    page(fname, d["title"], d["desc"], body, "services.html", crumbs=[("Home", "index.html"), ("Services", "services.html"), (name, fname)],
         extra_nodes=[svc_node, faq_node(d["faqs"])], priority=0.9)

for _sid in SVC: svc_page(_sid)

# ---------- PPC landing pages ----------
def lead_form(service_value, cta_label):
    chips = "".join(f'<option value="{n}"{" selected" if s == service_value else ""}>{n}</option>' for s, i, n, _, _ in SERVICES)
    return f'''<div class="form lp-form" id="lead">
      <form novalidate data-email="{EMAIL}" data-lead-form>
        <p class="lp-form__title">Get your free quote</p>
        <p class="lp-form__sub">Free consultation · No obligation</p>
        <div class="field"><label for="lp-name">Full name *</label><input id="lp-name" name="name" type="text" autocomplete="name" required><span class="error">Please enter your name.</span></div>
        <div class="field"><label for="lp-email">Email *</label><input id="lp-email" name="email" type="email" autocomplete="email" required><span class="error">Please enter a valid email.</span></div>
        <div class="field"><label for="lp-phone">Phone *</label><input id="lp-phone" name="phone" type="tel" autocomplete="tel" required><span class="error">Please enter your phone number.</span></div>
        <div class="field"><label for="lp-service">Service</label><select id="lp-service" name="service">{chips}</select></div>
        <div class="field"><label for="lp-message">Project details *</label><textarea id="lp-message" name="message" rows="3" required placeholder="A few words about your business and goals"></textarea><span class="error">Please tell us a little about your project.</span></div>
        <div style="position:absolute;left:-9999px" aria-hidden="true"><input type="text" name="company_website" tabindex="-1" autocomplete="off"></div>
        <button type="submit" class="btn btn--primary btn--block">{cta_label} {ARROW}</button>
        <p class="form__note">🔒 Your details are safe with us. Prefer to talk? <a href="tel:{PHONE_TEL}" data-track="click_call">{PHONE}</a></p>
      </form>
      <div class="form-success" role="status"><div class="icon">{icon("check")}</div><h3>Thank you!</h3><p>We'll be in touch shortly.</p></div>
    </div>'''

LPS = [
 ("lp-website-design.html", "web-design", "Professional Website Design — From $469 | Webratron",
  "Get a custom, mobile-first business website from $469. Delivered in 48–72 hours with full ownership. Free quote today.",
  "Limited offer · Up to 50% off", 'Get a Professional Website <span class="grad-text">From $469</span>',
  ["Custom design — no templates", "Delivered in 48–72 hours", "Mobile-friendly &amp; SEO-ready", "100% ownership · Money-back guarantee on eligible packages"], "Get My Free Quote"),
 ("lp-logo-design.html", "branding", "Custom Logo Design From $75 | Webratron",
  "Professional custom logo design from $75 — up to 12 concepts, unlimited revisions on most packages, vector files and full ownership.",
  "Logo packages from $75", 'Stand Out With a <span class="grad-text">Custom Logo</span>',
  ["4–12 original concepts", "Unlimited revisions (Standard &amp; up)", "Vector files: AI, EPS, PDF, PNG", "Full ownership · Moneyback guarantee"], "Start My Logo"),
 ("lp-ecommerce.html", "ecommerce", "Shopify & E-commerce Stores From $669 | Webratron",
  "Launch a Shopify or custom online store from $669 — payments, cart, product setup and mobile checkout. Free consultation.",
  "Shopify &amp; custom stores", 'Launch an Online Store <span class="grad-text">That Sells</span>',
  ["Shopify from $699 · Custom from $669", "Payment gateway &amp; cart setup", "Mobile-friendly fast checkout", "Up to unlimited products"], "Get My Store Quote"),
 ("lp-video-animation.html", "video", "Animated Explainer Videos From $499 | Webratron",
  "2D and whiteboard explainer videos from $499 — script, storyboard, voice-over and sound effects included.",
  "Explainer videos from $499", 'Explain Your Business in <span class="grad-text">60 Seconds</span>',
  ["Professional script &amp; storyboard", "Voice-over &amp; sound effects", "30 to 120-second videos", "Dedicated project manager"], "Get My Video Quote"),
]
for fname, sid, title, desc, badge, h1, points, cta_label in LPS:
    d = SVC[sid]; cards = d["cards"]()
    pts = "".join(f"<li>{p}</li>" for p in points)
    faq_html = "\n".join(f'      <details><summary>{q}</summary><p>{a}</p></details>' for q, a in d["faqs"])
    body = f'''
<section class="hero hero--v2 hero--inset lp-hero">
  <div class="starfield"></div><div class="orb orb--1"></div><div class="orb orb--2"></div>
  <div class="container lp-hero__grid">
    <div>
      <span class="lp-badge">{badge}</span>
      <h1>{h1}</h1>
      <p class="lp-lead">{d["lead"]}</p>
      <ul class="hero__points lp-points">{pts}</ul>
      <div class="lp-proof"><span class="stars">★★★★★</span><span>Rated <strong>4.7/5</strong> on Trustpilot · <strong>5.0</strong> on ProvenExpert</span></div>
      <img src="assets/img/trust-logos.webp" alt="Reviewed on Bark, Clutch, Google and Trustpilot" width="946" height="92" class="lp-trust">
    </div>
    {lead_form(sid, cta_label)}
  </div>
</section>
<section class="packages">
  <div class="container">
    <div class="pk-head"><h2>Choose your package</h2><p>Clear prices. Full ownership. Free consultation before you pay.</p></div>
    {pkg_grid(cards, d["kw"]) if cards else ""}
  </div>
</section>
<section class="section section--alt section--tight">
  <div class="container">
    <div class="section-head"><h2>How it works</h2></div>
    <div class="process">
{process()}
    </div>
  </div>
</section>
<section class="section section--tight">
  <div class="container">
    <div class="section-head"><h2>What our clients say</h2></div>
    <div class="grid grid--3">
{testimonials()}
    </div>
  </div>
</section>
<section class="section section--alt section--tight">
  <div class="container faq-split">
    <div class="faq-split__head"><h2>Frequently asked questions</h2><a href="#lead" class="btn btn--primary">{cta_label} {ARROW}</a></div>
    <div class="faq">
{faq_html}
    </div>
  </div>
</section>'''
    page(fname, title, desc, body, None, noindex=True, lp=True, extra_nodes=[faq_node(d["faqs"])])

# ---------- Thank-you (conversion) page ----------
thanks = f'''
<section class="page-hero">
  <div class="starfield"></div><div class="orb orb--1"></div><div class="orb orb--2"></div>
  <div class="container">
    <span class="eyebrow">Request received</span>
    <h1>Thank you — <span class="grad-text">we're on it!</span></h1>
    <p>Our team will review your request and get back to you shortly. Need us sooner? Call <a href="tel:{PHONE_TEL}" style="color:#fff;text-decoration:underline">{PHONE}</a>.</p>
    <div class="hero__actions" style="justify-content:center"><a href="index.html" class="btn btn--primary">Back to home {ARROW}</a><a href="portfolio.html" class="btn btn--ghost">See our work</a></div>
  </div>
</section>
<script>window.dataLayer=window.dataLayer||[];window.dataLayer.push({{event:"conversion_thank_you"}});</script>'''
page("thank-you.html", "Thank You | Webratron", "Thanks for contacting Webratron.", thanks, noindex=True)

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
page("privacy.html", "Privacy Policy | Webratron", "Webratron privacy policy.", privacy, priority=0.3)

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
page("terms.html", "Terms of Service | Webratron", "Webratron terms of service.", terms, priority=0.3)

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
page("404.html", "Page not found | Webratron", "The page you are looking for could not be found.", nf, noindex=True)
print("built")

# ================= LLM / CRAWLER FILES =================
def _money(x): return "${:,.0f}".format(x)
lines = ["# Webratron", "",
 "> Webratron is a results-driven web design and development company headquartered in New York (80 Broad Street, 5th Floor, New York, NY 10004) with an office in Sydney, Australia. It builds custom websites, Shopify and e-commerce stores, mobile apps, logos and brand identities, SEO campaigns and animated explainer videos for startups and growing businesses worldwide.", "",
 "## Key facts",
 f"- Website: {SITE}/",
 f"- Email: {EMAIL}",
 f"- Phone: {PHONE} (sales), {PHONE2}",
 "- Locations: 80 Broad St 5th Floor, New York, NY 10004, USA; 308 Sussex St, Sydney NSW 2000, Australia",
 "- Ratings: 4.7/5 on Trustpilot; 5.0 on ProvenExpert",
 "- Website packages start at $469; standard website packages are delivered in 48–72 hours",
 "- All packages include full ownership rights to the client's unique design", "",
 "## Services"]
for sid, ic, name, text, tags in SERVICES:
    lines.append(f"- [{name}]({SITE}/{SVC_URL[sid]}): {SVC[sid]['lead']}")
lines += ["", "## Packages and prices (USD)"]
def _cards(title, cards, note=""):
    lines.append(f"### {title}{note}")
    for c in cards: lines.append(f"- {c[0]}: {c[1]} (regular {c[2]}) — " + "; ".join(c[4][:5]))
_cards("Website", PACKAGES["website"]["sub"]["website"][1])
_cards("E-commerce", PACKAGES["website"]["sub"]["ecommerce"][1])
_cards("Shopify", PACKAGES["website"]["sub"]["shopify"][1])
_cards("Logo design", PACKAGES["logo"]["cards"])
_cards("SEO", PACKAGES["seo"]["cards"], " (6-month plans)")
_cards("Animation", PACKAGES["animation"]["cards"])
lines.append("### Business Starter combo\n- Business Starter Package: $1,999 (regular $3,999) — logo design, stationery, social media pages and a 15-page website")
lines.append("- Mobile app, branding, web app development and website maintenance: custom quote")
lines += ["", "## Frequently asked questions"]
for sid in SVC:
    for q, a in SVC[sid]["faqs"][:2]: lines.append(f"- Q: {q}\n  A: {a}")
lines += ["", "## Pages",
 f"- [Home]({SITE}/)", f"- [Services]({SITE}/services.html)", f"- [Pricing]({SITE}/pricing.html)", f"- [Portfolio]({SITE}/portfolio.html)",
 f"- [About]({SITE}/about.html)", f"- [Blog]({SITE}/blog.html)", f"- [Contact]({SITE}/contact.html)", ""]
open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(lines))

open(os.path.join(ROOT, "robots.txt"), "w").write(f"""# Webratron robots.txt
User-agent: *
Allow: /
Disallow: /thank-you.html

# AI / answer-engine crawlers are welcome
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Bingbot
Allow: /

Sitemap: {SITE}/sitemap.xml
""")

sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url, pr in SITEMAP:
    if url.endswith("/404.html"): continue
    sm.append(f"  <url><loc>{url}</loc><lastmod>2026-11-19</lastmod><priority>{pr:.1f}</priority></url>")
sm.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
