/* Webratron v2 ("Midnight Aurora") extras — loaded only on /v2/ pages */
(function () {
  "use strict";
  var fine = window.matchMedia && window.matchMedia("(pointer: fine)").matches;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!fine || reduce) return;
  var g = document.createElement("div");
  g.className = "cursor-glow";
  g.setAttribute("aria-hidden", "true");
  document.body.appendChild(g);
  var x = 0, y = 0, tx = 0, ty = 0, raf = null;
  function loop() {
    x += (tx - x) * 0.14; y += (ty - y) * 0.14;
    g.style.transform = "translate3d(" + x + "px," + y + "px,0)";
    raf = Math.abs(tx - x) + Math.abs(ty - y) > 0.5 ? requestAnimationFrame(loop) : null;
  }
  window.addEventListener("pointermove", function (e) {
    tx = e.clientX; ty = e.clientY; g.classList.add("on");
    if (!raf) raf = requestAnimationFrame(loop);
  }, { passive: true });
  document.addEventListener("pointerleave", function () { g.classList.remove("on"); });
})();
