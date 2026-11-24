document.addEventListener("click",function(e){
  var b=e.target.closest("[data-filter]");
  if(!b)return;
  var g=b.closest("[data-filter-group]");
  if(!g)return;
  var target=b.getAttribute("data-filter");
  g.querySelectorAll("[data-filter]").forEach(function(btn){
    btn.classList.toggle("is-active",btn===b);
    btn.setAttribute("aria-pressed",btn===b?"true":"false");
  });
  var scope=document.querySelector(g.getAttribute("data-target")||"main");
  if(!scope)return;
  scope.querySelectorAll("[data-cat]").forEach(function(el){
    var cats=(el.getAttribute("data-cat")||"").split(/\s+/);
    var show=target==="all"||cats.indexOf(target)!==-1;
    el.classList.toggle("is-hidden",!show);
  });
});
