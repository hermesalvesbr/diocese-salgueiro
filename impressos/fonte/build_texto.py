import os, re, html, xml.etree.ElementTree as ET, json, sys

SRC = sys.argv[1]; OUT = sys.argv[2]
tree = ET.parse(SRC); root = tree.getroot()

def eltext(e):
    # concatena texto + filhos (<a>, <b>, <i>)
    s = e.text or ''
    for c in e:
        s += (c.text or '') + (c.tail or '')
    return s

items = []          # blocos: dict(kind, num, text)
pending_pg = None   # marca de página a inserir
for page in root.findall('page'):
    pno = int(page.get('number'))
    lines = []      # (top, left, right, texto)
    buf = {}
    for t in page.findall('text'):
        top = int(t.get('top')); left = int(t.get('left')); w = int(t.get('width'))
        txt = eltext(t)
        if not txt.strip(): continue
        key = min((k for k in buf if abs(k-top) <= 4), default=None)
        if key is None: buf[top] = [(left, w, txt)]
        else: buf[key].append((left, w, txt))
    for top in sorted(buf):
        runs = sorted(buf[top])
        txt = ''.join(r[2] for r in runs)
        left = runs[0][0]; right = runs[-1][0] + runs[-1][1]
        if re.fullmatch(r'\s*\d{1,3}\s*', txt) and left > 700:   # número de página do original
            continue
        lines.append((top, left, right, txt))
    pending_pg = pno
    prev_top = None
    for top, left, right, txt in lines:
        gap = None if prev_top is None else top - prev_top
        centered = abs((left + right)/2 - 446) < 45 and (right-left) < 700
        m = re.match(r'^(\d{1,3})\.\s', txt)
        is_num = bool(m and 88 <= int(m.group(1)) <= 250)
        short = (right - left) < 620 and not re.search(r'[.:;»]$', txt.strip())
        first_of_page = gap is None
        newblock = is_num or (gap is not None and gap > 40) or (first_of_page and (centered or short))
        if newblock:
            if is_num:
                kind, num, body = 'par', int(m.group(1)), txt[m.end():]
            elif centered:
                kind, num, body = 'center', None, txt
            else:
                kind, num, body = 'sub', None, txt
            items.append({'kind': kind, 'num': num, 'text': body, 'pg': pending_pg})
            pending_pg = None
        else:
            if not items:            # cauda do §89, antes do CAPÍTULO III — fora do recorte
                prev_top = top; continue
            it = items[-1]
            if pending_pg:                       # página nova no meio do parágrafo
                it['text'] += ' \x00%d\x00' % pending_pg
                pending_pg = None
            it['text'] += ('' if it['text'].rstrip().endswith('-') else ' ') + txt
        prev_top = top

# corta no fim do §153
end = next(i for i, it in enumerate(items) if it['kind'] == 'par' and it['num'] == 154)
items = items[:end]
json.dump(items, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('blocos:', len(items), '| §:', sum(1 for i in items if i['kind']=='par' and i['num']))
print('headings:', [i['text'][:60] for i in items if i['kind'] in ('center','sub')])
