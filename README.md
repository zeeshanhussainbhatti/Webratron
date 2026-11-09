# Webratron — Agency Website

A fast, responsive static website for Webratron (website design, development, mobile apps, branding, SEO and video).

## Pages
`index.html` · `about.html` · `portfolio.html` · `services.html` · `blog.html` (+ 3 `blog-*.html` articles) · `pricing.html` · `contact.html` · `privacy.html` · `terms.html` · `404.html`

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
