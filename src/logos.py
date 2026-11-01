import os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
import json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

def text_path(fontfile, text, x0, baseline, cap_px, tracking=0.0, target_w=None):
    f=TTFont(fontfile); gs=f.getGlyphSet(); cmap=f.getBestCmap(); hmtx=f['hmtx']
    cap=f['OS/2'].sCapHeight; s=cap_px/cap
    names=[cmap[ord(c)] for c in text]
    adv=[hmtx[n][0] for n in names]
    # kerning ignored (simple); compute tracking to fit target width
    def total(tr): return sum(adv)*s + tr*(len(text)-1)
    if target_w is not None:
        last=names[-1]; g=gs[last]
        from fontTools.pens.boundsPen import BoundsPen
        bp=BoundsPen(gs); g.draw(bp); rb=bp.bounds[2]
        nat=(sum(adv[:-1])+rb)*s
        tracking=(target_w-nat)/(len(text)-1)
    out=[]; x=x0
    for n,a in zip(names,adv):
        sp=SVGPathPen(gs); tp=TransformPen(sp,(s,0,0,-s,x,baseline)); gs[n].draw(tp)
        out.append(sp.getCommands()); x+=a*s+tracking
    return out

f=json.load(open(os.path.join(HERE, 'faces_final.json')))
def P(rings): return ' '.join('M'+' L'.join(f'{x:.0f} {y:.0f}' for x,y in r)+'Z' for r in rings)

def filledP(c):  # c: (light, mid, dark)
    return ''.join(f'<path d="{P(f[k])}" fill="{col}" stroke="{col}" stroke-width="2" stroke-linejoin="round" fill-rule="evenodd"/>' for k,col in zip(['light','mid','dark'],c))
def outlineP(stroke, bg):
    return ''.join(f'<path d="{P(f[k])}" fill="{bg}" stroke="{stroke}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" fill-rule="evenodd"/>' for k in ['light','mid','dark'])

PED=text_path(os.path.join(HERE,'m600.ttf'),'Ped',1560,804,492)
PER=None
# full word to fit width, then split colors
word=text_path(os.path.join(HERE,'m600.ttf'),'PedPer',1560,804,492,target_w=2232)
pub=text_path(os.path.join(HERE,'m500.ttf'),'PUBLISHING',1584,1086,138,target_w=2208)

THEMES={
 'renkli':  dict(f=('#8C7BC4','#6E52A3','#4A2E83'), o='#6E52A3', obg='#FFFFFF', ped='#4A2E83', per='#8C7BC4', pub='#8C7BC4', div='#A68CC8'),
 'beyaz':   dict(f=('#FFFFFF','#D9D0F5','#B3A3E3'), o='#FFFFFF', obg='none', ped='#FFFFFF', per='#C9BEEF', pub='#C9BEEF', div='#8C7BC4'),
 'siyah':   dict(f=('#6B6B73','#3A3A40','#141416'), o='#3A3A40', obg='#FFFFFF', ped='#141416', per='#6B6B73', pub='#6B6B73', div='#9A9AA3'),
 'mor':     dict(f=('#6E52A3','#6E52A3','#4A2E83'), o='#6E52A3', obg='#FFFFFF', ped='#6E52A3', per='#6E52A3', pub='#6E52A3', div='#6E52A3'),
}
OUT_DX=648
def symbol(t):
    # outline P on dark bg: fill none would show hidden lines; use transparent-safe approach: fill with bg if given
    obg=t['obg'] if t['obg']!='none' else 'BG'
    return f'<g>{filledP(t["f"])}</g><g transform="translate({OUT_DX} 0)">{outlineP(t["o"], obg)}</g>'
def wordmark(t):
    return (f'<rect x="1341" y="144" width="18" height="1092" rx="9" fill="{t["div"]}"/>'
            f'<path d="{" ".join(word[:3])}" fill="{t["ped"]}"/><path d="{" ".join(word[3:])}" fill="{t["per"]}"/>'
            f'<path d="{" ".join(pub)}" fill="{t["pub"]}"/>')
def svg(vb,body,bg=None):
    r=f'<rect x="{vb[0]}" y="{vb[1]}" width="{vb[2]}" height="{vb[3]}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]} {vb[1]} {vb[2]} {vb[3]}">{r}{body}</svg>'

files={}
PAD=120
H_VB=(60-PAD,144-PAD,3792-60+2*PAD,1238-144+2*PAD)   # horizontal
S_VB=(60-PAD,237-PAD,1180-60+2*PAD,1238-237+2*PAD)   # symbol
for name,t in THEMES.items():
    bg = None
    body_h=symbol(t)+wordmark(t); body_s=symbol(t)
    if name=='beyaz':
        body_h=body_h.replace('fill="BG"','fill="#281A52"'); body_s=body_s.replace('fill="BG"','fill="#281A52"')
    files[f'pedper-logo-yatay-{name}.svg']=svg(H_VB,body_h,bg)
    files[f'pedper-sembol-{name}.svg']=svg(S_VB,body_s,bg)
    # vertical: symbol centered above wordmark
    sw=1180-60; ww=3792-1560; cx=ww/2
    vbody=(f'<g transform="translate({1560+cx-60-sw/2-60+60} 0)">' )  # placeholder
    # place symbol centered over wordmark block (x 1560..3792), wordmark moved down
    tx_sym=1560+ww/2-(60+sw/2)
    v=(f'<g transform="translate({tx_sym:.0f} 0)">{body_s}</g>'
       f'<g transform="translate(0 1180)"><path d="{" ".join(word[:3])}" fill="{t["ped"]}"/><path d="{" ".join(word[3:])}" fill="{t["per"]}"/><path d="{" ".join(pub)}" fill="{t["pub"]}"/></g>')
    V_VB=(1560-PAD,237-PAD,ww+2*PAD,(1086+1180)-237+2*PAD)
    files[f'pedper-logo-dikey-{name}.svg']=svg(V_VB,v,bg)
for n,s in files.items(): open(os.path.join(ROOT,'brand','logo',n),'w').write(s)

print(len(files))
