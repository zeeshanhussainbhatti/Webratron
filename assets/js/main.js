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
    var extras = params.get("extras");
    msg.value = "Hi, I'm interested in the " + nice + (extras ? " with " + extras.replace(/[<>]/g, "") : "") + ". Please share the next steps.";
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
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = window.matchMedia && window.matchMedia("(pointer: fine)").matches;

  /* ---- Scroll progress bar ---- */
  var bar = document.createElement("div");
  bar.className = "progress"; bar.setAttribute("aria-hidden", "true");
  document.body.appendChild(bar);
  function prog() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.transform = "scaleX(" + (h > 0 ? window.scrollY / h : 0) + ")";
  }
  prog(); window.addEventListener("scroll", prog, { passive: true });

  /* ---- Spotlight hover ---- */
  if (fine) {
    document.querySelectorAll(".card, .tile, .work, .stack__card, .calc__step").forEach(function (el) {
      el.classList.add("spot");
      el.addEventListener("pointermove", function (e) {
        var r = el.getBoundingClientRect();
        el.style.setProperty("--mx", (e.clientX - r.left) + "px");
        el.style.setProperty("--my", (e.clientY - r.top) + "px");
      });
    });
  }

  /* ---- Hero parallax ---- */
  var par = document.querySelector("[data-parallax]");
  if (par && fine && !reduce) {
    var img = par.querySelector("img");
    var chips = par.querySelectorAll("[data-depth]");
    document.querySelector(".hero").addEventListener("pointermove", function (e) {
      var x = e.clientX / window.innerWidth - 0.5, y = e.clientY / window.innerHeight - 0.5;
      if (img) img.style.transform = "translate(" + (x * -14) + "px," + (y * -14) + "px)";
      chips.forEach(function (c) {
        var d = +c.getAttribute("data-depth");
        c.style.transform = "translate(" + (x * d) + "px," + (y * d) + "px)";
      });
    });
  }

  /* ---- Magnetic buttons ---- */
  if (fine && !reduce) {
    document.querySelectorAll(".magnetic").forEach(function (b) {
      b.addEventListener("pointermove", function (e) {
        var r = b.getBoundingClientRect();
        b.style.transform = "translate(" + (e.clientX - r.left - r.width / 2) * 0.18 + "px," + (e.clientY - r.top - r.height / 2) * 0.3 + "px)";
      });
      b.addEventListener("pointerleave", function () { b.style.transform = ""; });
    });
  }

  /* ---- Testimonial slider ---- */
  document.querySelectorAll("[data-slider]").forEach(function (sl) {
    var slides = sl.querySelectorAll(".tslide"), dots = sl.querySelectorAll(".tdot"), cur = 0, timer;
    function go(n) {
      cur = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) { s.classList.toggle("is-active", i === cur); });
      dots.forEach(function (d, i) { d.classList.toggle("is-active", i === cur); });
    }
    function auto() { if (!reduce) { clearInterval(timer); timer = setInterval(function () { go(cur + 1); }, 6000); } }
    dots.forEach(function (d) { d.addEventListener("click", function () { go(+d.getAttribute("data-go")); auto(); }); });
    auto();
  });

  /* ---- Horizontal gallery buttons ---- */
  var hs = document.querySelector(".hscroll");
  document.querySelectorAll("[data-hs]").forEach(function (b) {
    b.addEventListener("click", function () {
      if (hs) hs.scrollBy({ left: +b.getAttribute("data-hs") * (hs.clientWidth * 0.8), behavior: reduce ? "auto" : "smooth" });
    });
  });

  /* ---- Price calculator ---- */
  var calc = document.querySelector(".calc");
  if (calc) {
    var cfg = JSON.parse(calc.getAttribute("data-config"));
    var range = calc.querySelector("#calc-range");
    var $ = function (sel) { return calc.querySelector(sel); };
    var money = function (n) { return "$" + Math.round(n).toLocaleString("en-US"); };
    var addonsBox = $("[data-calc-addons]");
    cfg.addons.forEach(function (a) {
      var l = document.createElement("label");
      l.innerHTML = '<input type="checkbox" value="' + a.id + '"><span>' + a.name + "<b>+" + money(a.price) + "</b></span>";
      addonsBox.appendChild(l);
    });
    function type() { return calc.querySelector('input[name="calc-type"]:checked').value; }
    function render(bump) {
      var t = cfg[type()], idx = +range.value, qty = t.steps[idx];
      var tier = t.tiers.filter(function (x) { return qty <= x.upto; })[0] || t.tiers[t.tiers.length - 1];
      var plus = t.plusLast && idx === t.steps.length - 1 ? "+" : "";
      $("[data-calc-label]").textContent = t.label;
      $("[data-calc-out]").textContent = qty.toLocaleString("en-US") + plus + " " + t.unit;
      range.style.setProperty("--fill", (idx / (t.steps.length - 1) * 100) + "%");
      $("[data-calc-name]").textContent = tier.name;
      $("[data-calc-price]").textContent = money(tier.price);
      $("[data-calc-was]").textContent = money(tier.was);
      $("[data-calc-feats]").innerHTML = tier.feats.map(function (f) { return "<li>" + f + "</li>"; }).join("");
      var total = tier.price, was = tier.was, lines = "", picked = [];
      addonsBox.querySelectorAll("input:checked").forEach(function (c) {
        var a = cfg.addons.filter(function (x) { return x.id === c.value; })[0];
        total += a.price; was += a.price; picked.push(a.name);
        lines += "<div><span>+ " + a.name + "</span><span>" + money(a.price) + "</span></div>";
      });
      $("[data-calc-lines]").innerHTML = lines;
      $("[data-calc-total]").textContent = money(total);
      $("[data-calc-save]").textContent = "You save " + money(was - total) + " vs. regular price";
      var slug = tier.name.toLowerCase().replace(/[^a-z0-9]+/g, "-");
      $("[data-calc-cta]").href = "contact.html?package=" + slug + (picked.length ? "&extras=" + encodeURIComponent(picked.join(", ")) : "");
      if (bump && !reduce) { var s = $(".calc__summary"); s.classList.remove("bump"); void s.offsetWidth; s.classList.add("bump"); }
    }
    calc.querySelectorAll('input[name="calc-type"]').forEach(function (r) {
      r.addEventListener("change", function () {
        var t = cfg[type()];
        range.max = t.steps.length - 1; range.value = Math.min(+range.value, t.steps.length - 1);
        render(true);
      });
    });
    range.addEventListener("input", function () { render(false); });
    range.addEventListener("change", function () { render(true); });
    addonsBox.addEventListener("change", function () { render(true); });
    render(false);
  }
})();
