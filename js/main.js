(function(){
var b=document.body,hd=document.getElementById("hd"),bar=document.getElementById("bar"),hero=document.querySelector(".hero");
var t0=Date.now();function go(){b.classList.add("ready")}function soon(){setTimeout(go,Math.max(0,650-(Date.now()-t0)))}
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(soon);else soon();setTimeout(go,1200);
/* kaydırma: ölçümler önbellekte, yazmalar tek karede */
var maxS=1,tick=false;
function olc(){maxS=Math.max(1,document.documentElement.scrollHeight-innerHeight)}
function ciz(){tick=false;var y=scrollY;hd.classList.toggle("solid",y>40);bar.style.transform="scaleX("+Math.min(1,y/maxS)+")"}
function kay(){if(!tick){tick=true;requestAnimationFrame(ciz)}}
addEventListener("scroll",kay,{passive:true});
addEventListener("resize",function(){olc();kay()},{passive:true});
if("ResizeObserver" in window)new ResizeObserver(function(){olc();kay()}).observe(b);
addEventListener("load",function(){olc();kay()});
requestAnimationFrame(function(){olc();ciz()});
/* hero paralaks: dikdörtgen sadece fare girince ölçülür */
if(!matchMedia("(prefers-reduced-motion:reduce)").matches&&matchMedia("(hover:hover)").matches&&hero){
var r=null,mx=0,my=0,pt=false;
hero.addEventListener("mouseenter",function(){r=hero.getBoundingClientRect()});
hero.addEventListener("mousemove",function(e){if(!r)r=hero.getBoundingClientRect();mx=(e.clientX-r.left)/r.width-.5;my=(e.clientY-r.top)/r.height-.5;
if(!pt){pt=true;requestAnimationFrame(function(){pt=false;hero.style.setProperty("--px",mx.toFixed(3));hero.style.setProperty("--py",my.toFixed(3))})}});
addEventListener("resize",function(){r=null},{passive:true});addEventListener("scroll",function(){r=null},{passive:true})}
/* görünür olunca beliren bölümler */
var els=document.querySelectorAll(".rv");
if("IntersectionObserver" in window){
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{threshold:.15});
els.forEach(function(el){io.observe(el)});
}else{els.forEach(function(el){el.classList.add("in")})}
/* mobil menü */
var mb=document.querySelector(".mnu"),mm=document.getElementById("mm");
function mset(o){b.classList.toggle("mo",o);mb.setAttribute("aria-expanded",o);mb.setAttribute("aria-label",o?"Menüyü kapat":"Menüyü aç")}
if(mb){mb.addEventListener("click",function(){mset(!b.classList.contains("mo"))});
mm.querySelectorAll("a").forEach(function(a){a.addEventListener("click",function(){mset(false)})});
addEventListener("keydown",function(e){if(e.key==="Escape")mset(false)})}
/* teklif formu */
var f=document.getElementById("qf");
if(f)f.addEventListener("submit",function(e){e.preventDefault();var d=new FormData(f);
var body="Ad: "+d.get("ad")+"\nE-posta: "+d.get("mail")+"\nHizmet: "+d.get("hizmet")+"\n\n"+d.get("mesaj");
location.href="mailto:bimayrr@gmail.com?subject="+encodeURIComponent("Teklif talebi: "+d.get("hizmet"))+"&body="+encodeURIComponent(body)});
})();
