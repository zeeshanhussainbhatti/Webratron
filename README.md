# Webratron — Agency Website

A fast, responsive static website for Webratron (website design, development, mobile apps, branding, SEO and video).

## Pages
`index.html` · `about.html` · `portfolio.html` · `services.html` + 8 service pages · `blog.html` (+ 3 articles) · `pricing.html` · `contact.html` · 4 PPC landing pages (`lp-*.html`, noindex) · `thank-you.html` · `privacy.html` · `terms.html` · `404.html`

## Editing
All pages are generated from `tools/build.py`, which holds the shared header/footer and all content (services, portfolio, testimonials, pricing, FAQ, contact details).

```bash
python3 tools/build.py
```

Styles: `assets/css/style.css` · Scripts: `assets/js/main.js`

## Contact form
By default the form opens the visitor's email app pre-filled to `support@webratron.com`.
To receive submissions directly, create a free form endpoint (e.g. Formspree) and set
`data-endpoint="https://formspree.io/f/XXXX"` on the `<form>` in `tools/build.py`, then rebuild.

## Deploy
No build step is needed for hosting. Upload the folder to any static host (Netlify, Vercel, GitHub Pages, cPanel/Hostinger `public_html`).

## SEO / AEO / GEO / PPC setup
- **Tracking:** set `GTM_ID` (recommended) or `GA4_ID` at the top of the SEO section in `tools/build.py`, then rebuild. The site pushes these dataLayer events: `generate_lead`, `form_start`, `click_call`, `click_email`, `select_package`, `calculator_quote`, `cta_click`, `conversion_thank_you`.
- **Google Ads conversions:** use the `/thank-you.html` page view (or the `generate_lead` event) as the conversion.
- **Lead capture:** set `FORM_ENDPOINT` (e.g. Formspree) so leads arrive by email and are stored. Each lead includes UTM, gclid and landing-page data. Without an endpoint, the form opens the visitor's email app.
- **PPC landing pages:** `lp-website-design.html`, `lp-logo-design.html`, `lp-ecommerce.html`, `lp-video-animation.html`. They have no navigation, put the form at the top, show a sticky call bar on mobile, and are noindexed.
- **LLM / answer engines:** `llms.txt`, AI crawlers allowed in `robots.txt`, JSON-LD (Organization, Service, Offers, FAQ, Breadcrumb, BlogPosting), and "Quick answer" + "Key facts" blocks on service pages.
