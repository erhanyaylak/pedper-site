"""Instagram profil fotoğrafı (1080x1080) — izometrik çift P sembolü.

Çalıştır: python3 src/instagram.py  →  brand/instagram/*.svg + *.png
Sembol geometrisi faces_final.json'dan gelir; koordinatlar doğrudan
dönüştürülür, böylece kontur P'nin yüz dolguları arka plan degradesiyle
piksel piksel örtüşür (gizli çizgiler görünmez).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'brand', 'instagram')
F = json.load(open(os.path.join(HERE, 'faces_final.json')))

N = 1080                 # tuval
OUT_DX = 648             # kontur P'nin kaydırması (logos.py ile aynı)
CX, CY = 625, 731        # sembol sınır kutusunun merkezi (79..1171, 242..1220)
S = 0.60                 # ölçek → sembol ~655 px genişlik, daire içinde rahat

def tf(x, y, dx=0):
    return (x + dx - CX) * S + N / 2, (y - CY) * S + N / 2

def path(rings, dx=0):
    return ' '.join('M' + ' L'.join('%.1f %.1f' % tf(x, y, dx) for x, y in r) + 'Z' for r in rings)

def symbol(fill3, stroke, face_bg):
    sw_f, sw_o = 2 * S, 14   # kontur küçük boyutta da okunsun diye kalın
    g = ''.join(f'<path d="{path(F[k])}" fill="{c}" stroke="{c}" stroke-width="{sw_f:.2f}" '
                f'stroke-linejoin="round" fill-rule="evenodd"/>'
                for k, c in zip(('light', 'mid', 'dark'), fill3))
    g += ''.join(f'<path d="{path(F[k], OUT_DX)}" fill="{face_bg}" stroke="{stroke}" '
                 f'stroke-width="{sw_o:.2f}" stroke-linejoin="round" stroke-linecap="round" fill-rule="evenodd"/>'
                 for k in ('light', 'mid', 'dark'))
    return g

VARIANTS = {
    # Koyu: Gece Moru → Koyu Mor radyal degrade, beyaz sembol (önerilen)
    'koyu': dict(
        defs='<radialGradient id="bg" gradientUnits="userSpaceOnUse" cx="540" cy="470" r="760">'
             '<stop offset="0" stop-color="#4A2E83"/><stop offset="1" stop-color="#281A52"/></radialGradient>',
        fill3=('#FFFFFF', '#D9D0F5', '#B3A3E3'), stroke='#FFFFFF'),
    # Açık: beyaz → Açık Lavanta, renkli sembol (kapaktaki görünüm)
    'acik': dict(
        defs='<radialGradient id="bg" gradientUnits="userSpaceOnUse" cx="540" cy="470" r="760">'
             '<stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#E6DEFA"/></radialGradient>',
        fill3=('#8C7BC4', '#6E52A3', '#4A2E83'), stroke='#6E52A3'),
}

os.makedirs(OUT, exist_ok=True)
for name, v in VARIANTS.items():
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{N}" height="{N}" viewBox="0 0 {N} {N}">'
           f'<defs>{v["defs"]}</defs><rect width="{N}" height="{N}" fill="url(#bg)"/>'
           f'{symbol(v["fill3"], v["stroke"], "url(#bg)")}</svg>')
    p = os.path.join(OUT, f'pedper-instagram-{name}.svg')
    open(p, 'w').write(svg)

# PNG çıktısı (Node Playwright + önceden kurulu Chromium)
import subprocess
JS = """const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:%d,height:%d}});
for(const n of process.argv.slice(1)){await p.goto('file://'+n+'.svg');await p.screenshot({path:n+'.png'});}
await b.close();})();""" % (N, N)
subprocess.run(['node', '-e', JS] + [os.path.join(OUT, f'pedper-instagram-{n}') for n in VARIANTS], check=True)
print('ok:', ', '.join(VARIANTS))
