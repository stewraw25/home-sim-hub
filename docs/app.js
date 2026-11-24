document.addEventListener("click",function(e){
  var b=e.target.closest("[data-filter]");
  if(b){
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
  }
  var p=e.target.closest("[data-room-preset]");
  if(p){
    var vals=p.getAttribute("data-room-preset").split(",");
    var h=document.getElementById("rm-h"),w=document.getElementById("rm-w"),d=document.getElementById("rm-d");
    if(h&&w&&d){h.value=vals[0];w.value=vals[1];d.value=vals[2];updateRoomFit();}
  }
});

function updateRoomFit(){
  var box=document.getElementById("room-fit-results");
  if(!box)return;
  var h=parseFloat((document.getElementById("rm-h")||{}).value)||0;
  var w=parseFloat((document.getElementById("rm-w")||{}).value)||0;
  var d=parseFloat((document.getElementById("rm-d")||{}).value)||0;
  var ceilNote,ceilCls;
  if(h>=3.05){ceilCls="fit-ok";ceilNote="Meets SkyTrak's 10 ft (3.05 m) ample clearance figure for full driver swings.";}
  else if(h>=2.74){ceilCls="fit-warn";ceilNote="Meets the 9 ft (2.74 m) figure cited by Rapsodo for players ~5 ft 8 in and under; taller players may need 3.05 m+. Do the slow driver swing test.";}
  else{ceilCls="fit-no";ceilNote="Under 2.74 m (9 ft): full driver swings may hit the ceiling or beams. Check iron/wedge clearance only, or use an outdoor garden net.";}

  var radarCls,radarNote;
  if(d>=4.8 && w>=3.0){radarCls="fit-ok";radarNote="Depth meets Garmin R10 (1.8–2.4 m behind + 2.4 m+ ball flight) and Rapsodo MLM2PRO (~4.3 m+ total).";}
  else if(d>=4.3 && w>=2.7){radarCls="fit-warn";radarNote="Close to the ~4.3 m (14 ft+) Rapsodo MLM2PRO minimum; check exact net clearance before ordering a behind-the-ball unit.";}
  else{radarCls="fit-no";radarNote="Under 4.3 m depth: tight for behind-the-ball radar units indoors. Beside-the-ball camera units save behind-golfer depth.";}

  var camCls,camNote;
  if(d>=3.6 && w>=3.05){camCls="fit-ok";camNote="Clears SkyTrak's 10 ft x 10 ft (3.05 x 3.05 m) minimum unobstructed area and Shop Indoor Golf's 12 ft (3.66 m) Square Omni depth.";}
  else if(d>=3.05 && w>=2.8){camCls="fit-warn";camNote="Tight width or depth for a full enclosure; measure swing width carefully (especially if sharing left/right-handed).";}
  else{camCls="fit-no";camNote="Under 3.05 m unobstructed length/width: check whether a full iron swing clears walls before installing.";}

  var bayCls,bayNote;
  if(d>=4.9 && w>=3.65 && h>=2.74){bayCls="fit-ok";bayNote="Fits SkyTrak's suggested 16–17 ft depth and 12 ft width for a spacious projected bay.";}
  else{bayCls="fit-warn";bayNote="Smaller than SkyTrak's 16–17 ft x 12 ft comfortable enclosure guidance; consider a compact net + beside-the-ball unit.";}

  box.innerHTML=
    '<div class="fit-card '+ceilCls+'"><strong>Ceiling ('+h.toFixed(2)+' m)</strong>'+ceilNote+'</div>'+
    '<div class="fit-card '+radarCls+'"><strong>Behind-ball radar (R10 / MLM2PRO / Mevo+)</strong>'+radarNote+'</div>'+
    '<div class="fit-card '+camCls+'"><strong>Beside-ball camera (R50 / SkyTrak / Square / Uneekor)</strong>'+camNote+'</div>'+
    '<div class="fit-card '+bayCls+'"><strong>Full projected enclosure</strong>'+bayNote+'</div>';
}
document.addEventListener("input",function(e){
  if(e.target && (e.target.id==="rm-h"||e.target.id==="rm-w"||e.target.id==="rm-d"))updateRoomFit();
});
if(document.getElementById("room-fit-results"))updateRoomFit();
