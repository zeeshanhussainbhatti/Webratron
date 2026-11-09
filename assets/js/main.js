/* =========================================================
   Webratron — Site scripts
   ========================================================= */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");

  /* ---- Sticky header ---- */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 20);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---- Mobile nav ---- */
  var toggle = document.querySelector(".nav__toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    document.querySelectorAll(".nav__links a").forEach(function (a) {
      a.addEventListener("click", function () {
        document.body.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.body.classList.contains("nav-open")) {
        document.body.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* ---- Reveal on scroll ---- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---- Animated counters ---- */
  var counters = document.querySelectorAll("[data-count]");
  function animateCount(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    var duration = 1600;
    var start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window && counters.length) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { animateCount(entry.target); cio.unobserve(entry.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach(function (c) { cio.observe(c); });
  }

  /* ---- Portfolio filter ---- */
  var filters = document.querySelectorAll(".filter");
  filters.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var f = btn.getAttribute("data-filter");
      filters.forEach(function (b) {
        b.classList.toggle("is-active", b === btn);
        b.setAttribute("aria-pressed", String(b === btn));
      });
      document.querySelectorAll(".work").forEach(function (w) {
        var cats = (w.getAttribute("data-cat") || "").split(" ");
        w.classList.toggle("is-hidden", f !== "all" && cats.indexOf(f) === -1);
      });
    });
  });

  /* ---- Pre-select service from URL (?service=web) ---- */
  var params = new URLSearchParams(window.location.search);
  var svc = params.get("service");
  if (svc) {
    var chip = document.querySelector('.chips input[value="' + svc.replace(/[^a-z-]/gi, "") + '"]');
    if (chip) chip.checked = true;
  }
  var plan = params.get("plan");
  var budget = document.getElementById("budget");
  if (plan && budget) {
    var map = { starter: "1k-3k", growth: "3k-8k", enterprise: "8k+" };
    if (map[plan]) budget.value = map[plan];
  }

  /* ---- Package tabs ---- */
  document.querySelectorAll(".pk-tabs").forEach(function (list) {
    var tabs = Array.prototype.filter.call(list.children, function (c) { return c.classList.contains("pk-tab"); });
    tabs.forEach(function (tab, idx) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (t) {
          var on = t === tab;
          t.classList.toggle("is-active", on);
          t.setAttribute("aria-selected", String(on));
          var panel = document.getElementById(t.getAttribute("data-tab"));
          if (panel) panel.hidden = !on;
        });
      });
      tab.addEventListener("keydown", function (e) {
        var n = null;
        if (e.key === "ArrowRight") n = tabs[(idx + 1) % tabs.length];
        if (e.key === "ArrowLeft") n = tabs[(idx - 1 + tabs.length) % tabs.length];
        if (n) { e.preventDefault(); n.focus(); n.click(); }
      });
    });
  });

  /* ---- Package "View Details" expands the full feature list ---- */
  document.querySelectorAll(".pkg__btn--details[aria-expanded]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var card = btn.closest(".pkg");
      var open = card.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", String(open));
      btn.textContent = open ? "Hide Details" : "View Details";
    });
  });

  /* ---- Pre-fill contact form from ?package= ---- */
  var pkg = params.get("package");
  var msg = document.getElementById("message");
  if (pkg && msg && !msg.value) {
    var nice = pkg.replace(/[^a-z0-9-]/gi, "").replace(/-/g, " ").replace(/\b\w/g, function (c) { return c.toUpperCase(); });
    msg.value = "Hi, I'm interested in the " + nice + ". Please share the next steps.";
  }

  /* ---- Contact form ---- */
  var wrap = document.querySelector(".form");
  var form = wrap && wrap.querySelector("form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var valid = true;
      form.querySelectorAll("[required]").forEach(function (input) {
        var field = input.closest(".field");
        var ok = input.value.trim() !== "";
        if (ok && input.type === "email") ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim());
        if (field) field.classList.toggle("has-error", !ok);
        if (!ok) valid = false;
      });
      if (!valid) {
        var firstErr = form.querySelector(".has-error input, .has-error textarea, .has-error select");
        if (firstErr) firstErr.focus();
        return;
      }

      var data = new FormData(form);
      var services = data.getAll("services").join(", ");
      var endpoint = form.getAttribute("data-endpoint");
      var btn = form.querySelector("button[type=submit]");

      // Honeypot spam check
      if (data.get("company_website")) { wrap.classList.add("is-sent"); return; }

      if (endpoint) {
        btn.disabled = true;
        btn.textContent = "Sending…";
        fetch(endpoint, { method: "POST", body: data, headers: { Accept: "application/json" } })
          .then(function (r) {
            if (!r.ok) throw new Error("Request failed");
            wrap.classList.add("is-sent");
          })
          .catch(function () {
            btn.disabled = false;
            btn.textContent = "Send message";
            alert("Sorry, something went wrong. Please email us directly at " + form.getAttribute("data-email"));
          });
      } else {
        // Fallback: open the visitor's email app with the message pre-filled
        var body =
          "Name: " + data.get("name") + "\n" +
          "Email: " + data.get("email") + "\n" +
          "Phone: " + (data.get("phone") || "-") + "\n" +
          "Services: " + (services || "-") + "\n" +
          "Budget: " + (data.get("budget") || "-") + "\n\n" +
          data.get("message");
        window.location.href = "mailto:" + form.getAttribute("data-email") +
          "?subject=" + encodeURIComponent("New project enquiry — " + data.get("name")) +
          "&body=" + encodeURIComponent(body);
        wrap.classList.add("is-sent");
      }
    });
    form.querySelectorAll("input, textarea, select").forEach(function (input) {
      input.addEventListener("input", function () {
        var field = input.closest(".field");
        if (field) field.classList.remove("has-error");
      });
    });
  }

  /* ---- Footer year ---- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
