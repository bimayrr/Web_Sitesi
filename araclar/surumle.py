"""CSS/JS bağlantılarına içerik özetinden sürüm ekler (?v=...), böylece uzun önbellek güvenle kullanılır.
Kullanım (depo klasöründe): python araclar/surumle.py .
Site dosyalarında (css/js/proje.css) her değişiklikten sonra çalıştırın."""
import sys, re, hashlib, pathlib
R = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
pat = re.compile(r'((?:href|src)=")((?:\.\./)?(?:css/style\.css|js/main\.js)|proje\.css)(?:\?v=[0-9a-f]+)?(")')
n = 0
for h in [R / "index.html", R / "kvkk.html", *sorted((R / "projeler").glob("*.html"))]:
    if not h.exists(): continue
    s = h.read_text(encoding="utf-8")
    def sub(m):
        hedef = (h.parent / m.group(2)).resolve()
        v = hashlib.md5(hedef.read_bytes()).hexdigest()[:10]
        return f'{m.group(1)}{m.group(2)}?v={v}{m.group(3)}'
    t = pat.sub(sub, s)
    if t != s: h.write_text(t, encoding="utf-8"); n += 1
print(f"surum guncellendi: {n} dosya")
