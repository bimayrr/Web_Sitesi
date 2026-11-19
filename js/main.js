(function(){
var b=document.body;
function go(){b.classList.add("ready")}
var t0=Date.now();function soon(){setTimeout(go,Math.max(0,650-(Date.now()-t0)))}
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(soon);else soon();
setTimeout(go,1200);
var hd=document.getElementById("hd");
function sc(){hd.classList.toggle("solid",window.scrollY>40)}
window.addEventListener("scroll",sc,{passive:true});sc();
var bar=document.getElementById("bar"),hero=document.querySelector(".hero");
function pg(){var h=document.documentElement.scrollHeight-innerHeight;bar.style.transform="scaleX("+(h>0?scrollY/h:0)+")"}
addEventListener("scroll",pg,{passive:true});pg();
var rm=matchMedia("(prefers-reduced-motion:reduce)").matches;
if(!rm){
hero.addEventListener("mousemove",function(e){var r=hero.getBoundingClientRect();hero.style.setProperty("--px",((e.clientX-r.left)/r.width-.5).toFixed(3));hero.style.setProperty("--py",((e.clientY-r.top)/r.height-.5).toFixed(3))});
document.querySelectorAll(".work,.card").forEach(function(c){
c.addEventListener("mousemove",function(e){var r=c.getBoundingClientRect();c.style.setProperty("--ry",(((e.clientX-r.left)/r.width-.5)*8).toFixed(2)+"deg");c.style.setProperty("--rx",(-((e.clientY-r.top)/r.height-.5)*8).toFixed(2)+"deg")});
c.addEventListener("mouseleave",function(){c.style.setProperty("--rx","0deg");c.style.setProperty("--ry","0deg")})});
document.querySelectorAll(".btn").forEach(function(btn){
btn.addEventListener("mousemove",function(e){var r=btn.getBoundingClientRect();btn.style.setProperty("--mx",((e.clientX-r.left-r.width/2)*.25).toFixed(1)+"px");btn.style.setProperty("--my",((e.clientY-r.top-r.height/2)*.35).toFixed(1)+"px")});
btn.addEventListener("mouseleave",function(){btn.style.setProperty("--mx","0px");btn.style.setProperty("--my","0px")})})}
var els=document.querySelectorAll(".rv");
if("IntersectionObserver" in window){
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{threshold:.15});
els.forEach(function(el){io.observe(el)});
}else{els.forEach(function(el){el.classList.add("in")})}
var f=document.getElementById("qf");
if(f)f.addEventListener("submit",function(e){e.preventDefault();var d=new FormData(f);
var body="Ad: "+d.get("ad")+"\nE-posta: "+d.get("mail")+"\nHizmet: "+d.get("hizmet")+"\n\n"+d.get("mesaj");
location.href="mailto:bimayrr@gmail.com?subject="+encodeURIComponent("Teklif talebi: "+d.get("hizmet"))+"&body="+encodeURIComponent(body)});
})();
