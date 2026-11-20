/* Bimayr çerez izni + Microsoft Clarity (yalnızca izinle yüklenir) */
(function(){
var CLARITY_ID="zgn5gpjw9l";
var KEY="bimayr-izin-v1",d=document;
function oku(){try{return localStorage.getItem(KEY)}catch(e){return null}}
function yaz(v){try{localStorage.setItem(KEY,v)}catch(e){}}
function clarityYukle(){
 if(!CLARITY_ID||CLARITY_ID.indexOf("__")===0||window.clarity)return;
 (function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y)})(window,d,"clarity","script",CLARITY_ID);
 window.clarity("consentv2",{ad_Storage:"denied",analytics_Storage:"granted"});
}
function kok(){var p=location.pathname;return p.indexOf("/projeler/")>-1?"../":""}
function kutu(){
 var s=d.createElement("style");
 s.textContent=".izn{position:fixed;right:16px;bottom:16px;z-index:90;max-width:380px;background:#140a0d;color:#F4EDE0;border:1px solid #3a1d25;border-radius:18px;padding:18px 18px 16px;box-shadow:0 20px 50px -12px rgba(0,0,0,.55);font:400 .85rem/1.55 Manrope,system-ui,sans-serif;opacity:0;transform:translateY(16px);transition:opacity .4s,transform .5s cubic-bezier(.2,.8,.2,1)}"
 +".izn.on{opacity:1;transform:none}.izn b{display:block;font:600 1rem 'Inter Tight',system-ui,sans-serif;margin-bottom:4px}.izn p{margin:0;color:#B9A9A0}.izn a{color:#F4EDE0;text-underline-offset:3px}"
 +".izn .bt{display:flex;gap:8px;margin-top:14px}.izn button{flex:1;font:700 .85rem Manrope,system-ui,sans-serif;border-radius:999px;padding:10px 14px;cursor:pointer;border:1.5px solid #F4EDE0;background:transparent;color:#F4EDE0;transition:background .3s,color .3s}"
 +".izn button.ok{background:#A62644;border-color:#A62644;color:#fff}.izn button:hover{background:#F4EDE0;color:#140a0d}.izn button.ok:hover{background:#7A1730;border-color:#7A1730;color:#fff}"
 +"@media (max-width:520px){.izn{left:12px;right:12px;bottom:12px;max-width:none}}";
 d.head.appendChild(s);
 var k=d.createElement("div");k.className="izn";k.setAttribute("role","dialog");k.setAttribute("aria-label","Çerez tercihi");
 k.innerHTML="<b>Çerez tercihiniz</b><p>Deneyiminizi iyileştirmek için sitenin nasıl kullanıldığını ölçmek istiyoruz. Adınız ve form bilgileriniz kaydedilmez. <a href='"+kok()+"kvkk.html#cerezler'>Ayrıntılar</a></p><div class='bt'><button type='button' class='no'>Hayır, teşekkürler</button><button type='button' class='ok'>Kabul et</button></div>";
 d.body.appendChild(k);
 requestAnimationFrame(function(){requestAnimationFrame(function(){k.classList.add("on")})});
 function kapat(v){yaz(v);k.classList.remove("on");setTimeout(function(){k.remove()},450);if(v==="evet")clarityYukle()}
 k.querySelector(".ok").addEventListener("click",function(){kapat("evet")});
 k.querySelector(".no").addEventListener("click",function(){kapat("hayir")});
}
/* çerez tercihini değiştirme bağlantısı: href="#cerez-tercihi" */
d.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest("a[href='#cerez-tercihi']");if(a){e.preventDefault();try{localStorage.removeItem(KEY)}catch(x){}if(!d.querySelector(".izn"))kutu()}});
var v=oku();
if(v==="evet"){addEventListener("load",function(){setTimeout(clarityYukle,1500)})}
else if(v!=="hayir"){addEventListener("load",function(){setTimeout(kutu,2200)})}
})();
