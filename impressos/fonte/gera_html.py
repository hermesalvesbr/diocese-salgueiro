# -*- coding: utf-8 -*-
import os, json, re, html, sys

S = os.path.dirname(os.path.abspath(__file__))
blocos = json.load(open(S + '/blocos.json'))

ITALICOS = ['Laudato si’', 'Rerum novarum', 'Magnifica Humanitas', 'Antiqua et nova']
SIGLA = re.compile(r'\b(Gn|Ex|Ne|Sl|Pr|Is|Mt|Mc|Lc|Jo|At|Rm|1 Cor|2 Cor|Gl|Ef|Fl|Cl|Hb|Tg|Ap) (\d)')

def fmt(t):
    t = html.escape(t)
    t = re.sub(r'\x00(\d+)\x00', r'<span class="pg">\1</span>', t)
    t = re.sub(r'\[(\d{2,3})\]', r'<span class="nota">[\1]</span>', t)
    for it in ITALICOS:
        t = t.replace(html.escape(it), '<em>%s</em>' % html.escape(it))
    t = SIGLA.sub(r'<em>\1</em> \2', t)
    return t

# índice de citações-chave do roteiro (só o que cai neste recorte)
INDICE = [
 (90,33,'“o que estamos a construir?” — a pergunta que abre o Capítulo III'),
 (93,34,'“Mais poderoso não significa necessariamente melhor” · Guardini'),
 (98,35,'IAs “cultivadas”, não “construídas”'),
 (99,35,'o que a IA não é · “adaptação estatística”, sem crescimento interior'),
 (100,36,'as três armadilhas · “palavra simulada, mas não encarnada”'),
 (101,36,'custo ambiental e cuidado da Casa comum'),
 (102,36,'sem compaixão, misericórdia, perdão'),
 (103,37,'“a injustiça torna-se silenciosa”'),
 (104,37,'“não podemos considerar a IA moralmente neutra”'),
 (110,39,'“Desarmar a IA”'),
 (111,39,'os programadores e o peso ético do projeto'),
 (112,39,'a pessoa como “projeto a otimizar”'),
 (128,44,'“Para um algoritmo, o erro é algo a corrigir…”'),
 (129,44,'nem entusiasmo, nem medo · “mais humana? mais digna do homem?”'),
 (130,44,'Agostinho · os dois amores, as duas cidades'),
 (132,45,'desinformação · a IA como “poderoso multiplicador”'),
 (137,47,'ecologia da comunicação · proteger os dados pessoais'),
 (140,48,'“Devemos educar-nos ao jejum da IA”'),
 (141,48,'menores, celular precoce, riscos na rede'),
 (142,48,'não delegar às famílias o ónus da limitação'),
 (146,49,'“higiene da atenção”'),
 (147,50,'“tempo partilhado para aprender e relações de confiança”'),
 (150,50,'automação, robótica e IA na estrutura do trabalho'),
 (153,51,'“reservatórios de mão de obra precária… migrações forçadas”'),
]

corpo = []
for b in blocos:
    if b['pg'] and b['kind'] != 'center':
        corpo.append('<div class="marcapg">p.&thinsp;%d</div>' % b['pg'])
    if b['kind'] == 'center':
        cls = 'cap' if b['text'].startswith('CAPÍTULO') else 'captit'
        corpo.append('<h2 class="%s">%s</h2>' % (cls, fmt(b['text'])))
    elif b['kind'] == 'sub':
        corpo.append('<h3>%s</h3>' % fmt(b['text']))
    else:
        n = '<span class="num">%d</span>' % b['num'] if b['num'] else ''
        corpo.append('<p class="par">%s%s</p>' % (n, fmt(b['text'].strip())))

linhas_indice = '\n'.join(
 '<tr><td class="ip">§&thinsp;%d</td><td class="ig">p.&thinsp;%d</td><td>%s</td></tr>' % (n, p, html.escape(d).replace('&quot;','"'))
 for n, p, d in INDICE)

CSS = """
@page { size: A4; margin: 20mm 18mm 20mm 26mm; }
@page :left  { margin-left: 18mm; margin-right: 26mm; }
@page :right { margin-left: 26mm; margin-right: 18mm; }
@page :first { margin: 30mm 24mm 24mm 24mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Noto Serif", Georgia, serif; font-size: 11.4pt; line-height: 1.58;
       color: #1a1a1a; margin: 0; text-align: justify; hyphens: auto; -webkit-hyphens: auto; }
p, h2, h3 { orphans: 3; widows: 3; }

/* ---------- capa ---------- */
.capa { height: 232mm; display: flex; flex-direction: column; text-align: left; page-break-after: always; }
.capa .topo { font-family: "Noto Sans", sans-serif; font-size: 8.6pt; letter-spacing: .16em;
              text-transform: uppercase; color: #7a5c2e; border-bottom: .6pt solid #c9b895; padding-bottom: 5mm; }
.capa h1 { font-family: "Noto Serif Display", "Noto Serif", serif; font-size: 34pt; font-weight: 600;
           line-height: 1.08; margin: 26mm 0 0; letter-spacing: -.01em; }
.capa .sub { font-size: 12pt; line-height: 1.5; color: #4a4a4a; margin: 7mm 0 0; max-width: 118mm; }
.capa .faixa { margin: 20mm 0 0; padding: 6mm 7mm; background: #f6f1e7; border-left: 2.4pt solid #7a5c2e; }
.capa .faixa .big { font-family: "Noto Sans", sans-serif; font-size: 14pt; font-weight: 700; color: #4a3411; }
.capa .faixa .small { font-size: 9.6pt; color: #5d5346; margin-top: 2.5mm; line-height: 1.5; }
.capa .rodape { margin-top: auto; font-size: 8.8pt; color: #6b6b6b; line-height: 1.55; }
.capa .nome { margin: 0 0 9mm; font-family: "Noto Sans", sans-serif; font-size: 10pt; color: #333; }
.capa .nome span { display: inline-block; width: 92mm; border-bottom: .8pt solid #9a9a9a; margin-left: 3mm; }

/* ---------- página de uso + índice ---------- */
.guia { page-break-after: always; }
.guia h2 { font-family: "Noto Sans", sans-serif; font-size: 11.5pt; letter-spacing: .04em; margin: 0 0 4mm; color: #4a3411; }
.guia h2.seg { margin-top: 5mm; }
.guia p { font-size: 10pt; color: #333; margin: 0 0 3.5mm; }
.guia .amostra { background: #f6f1e7; padding: 3.5mm 5mm; margin: 0 0 4mm; font-size: 9.2pt; text-align: left; line-height: 1.7; }
.guia table { width: 100%; border-collapse: collapse; font-size: 8.9pt; text-align: left; }
.guia td { padding: .88mm 2mm .88mm 0; border-bottom: .4pt solid #e3dccd; vertical-align: baseline; }
.guia .ip { font-family: "Noto Sans", sans-serif; font-weight: 700; color: #7a5c2e; white-space: nowrap; width: 13mm; }
.guia .ig { font-family: "Noto Sans", sans-serif; color: #8c8c8c; white-space: nowrap; width: 13mm; font-size: 8.6pt; }

/* ---------- corpo ---------- */
h2.cap { font-family: "Noto Sans", sans-serif; font-size: 11pt; font-weight: 700; letter-spacing: .22em;
         text-align: center; text-transform: uppercase; color: #7a5c2e; margin: 0 0 6mm; page-break-before: always; }
h2.captit { font-family: "Noto Serif Display", serif; font-size: 15pt; font-weight: 600; text-align: center;
            line-height: 1.35; margin: 0 auto 11mm; max-width: 130mm; }
h3 { font-family: "Noto Sans", sans-serif; font-size: 10.4pt; font-weight: 700; color: #4a3411;
     margin: 8mm 0 3.5mm; text-align: left; page-break-after: avoid; }
p.par { position: relative; padding-left: 12mm; margin: 0 0 3.6mm; }
p.par .num { position: absolute; left: 0; top: .1em; width: 9mm; text-align: right;
             font-family: "Noto Sans", sans-serif; font-size: 8.6pt; font-weight: 700; color: #7a5c2e; }
.nota { font-size: .74em; color: #a08a63; vertical-align: .28em; letter-spacing: -.02em; }
.pg { font-family: "Noto Sans", sans-serif; font-size: .58em; color: #b09a72; vertical-align: .32em;
      white-space: nowrap; padding-left: .18em; margin-left: .1em; border-left: .8pt solid #ddcfb2; }
.marcapg { float: right; margin: .15em 0 0 5mm; font-family: "Noto Sans", sans-serif;
            font-size: 8pt; color: #b09a72; letter-spacing: .02em; }
em { font-style: italic; }
.fim { margin-top: 9mm; }
.fim .regra { width: 28mm; height: 1.2pt; background: #c9b895; margin-bottom: 4mm; }
.fim p { font-size: 9pt; line-height: 1.55; color: #6b6255; text-align: left; }
.anot { page-break-before: always; }
.anot h2 { font-family: "Noto Sans", sans-serif; font-size: 11pt; font-weight: 700; color: #4a3411;
           letter-spacing: .06em; text-transform: uppercase; margin: 0 0 6mm; }
.anot .l { height: 10.9mm; border-bottom: .5pt solid #ddd6c6; }
"""

HTML = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Magnifica Humanitas — recorte Cap. III–IV</title><style>%s</style></head><body>

<section class="capa">
  <div class="topo">Diocese de Salgueiro &middot; Formação do presbitério &middot; 22 de agosto de 2026</div>
  <h1>Magnifica<br>Humanitas</h1>
  <div class="sub">Carta Encíclica do Papa Leão XIV sobre a salvaguarda da pessoa humana na era da inteligência artificial. Roma, junto de São Pedro, 15 de maio de 2026.</div>
  <div class="faixa">
    <div class="big">Capítulo III e início do Capítulo IV</div>
    <div class="small">§&thinsp;90 a §&thinsp;153 &middot; páginas 33 a 51 do PDF oficial<br>
    Técnica e domínio &middot; A grandeza da pessoa humana perante as promessas da IA &middot; Verdade, trabalho, liberdade</div>
  </div>
  <div class="rodape">
    <div class="nome">Este exemplar é de <span></span></div>
    Recorte de leitura para o encontro de formação. O texto é reproduzido sem qualquer alteração a partir do
    PDF oficial publicado pela Santa Sé; muda apenas a diagramação, para leitura e anotação.
    A numeração dos parágrafos (§) e as marcas de página do original foram preservadas.<br>
    Texto integral em vatican.va &middot; Leão XIV, Carta Encíclica <i>Magnifica Humanitas</i>, 245 parágrafos e 224 notas.
  </div>
</section>

<section class="guia">
  <h2>Como usar este caderno</h2>
  <p>Este recorte traz os dois capítulos que o encontro percorre. O que ficou de fora está no documento
  de estudo entregue à diocese.</p>
  <div class="amostra">
    <b>99</b> &nbsp;→ o número à esquerda de cada parágrafo é o § da encíclica.<br>
    <span style="font-family:'Noto Sans';font-size:7.6pt;color:#b09a72;border-left:.8pt solid #ddcfb2;padding-left:.2em">35</span> &nbsp;→ a barrinha marca onde começa a página do PDF oficial. Assim, uma citação
    anunciada como “§&thinsp;99, p.&thinsp;35” é encontrada em segundos.<br>
    <span style="font-size:8pt;color:#a08a63">[116]</span> &nbsp;→ nota de rodapé do original. As 224 notas estão nas pp. 79–93 do PDF e não foram reproduzidas.
  </div>
  <h2 class="seg">As passagens citadas no encontro</h2>
  <table>%s</table>
</section>

%s

<div class="fim">
  <div class="regra"></div>
  <p><b>Aqui termina o recorte.</b> O texto da encíclica continua no §&thinsp;154 e vai até o §&thinsp;245,
  na p.&thinsp;78 do PDF oficial; as pp. 79–93 trazem as 224 notas. O restante — Capítulos I, II e V,
  a conclusão e o <i>Magnificat</i> dos §§&thinsp;243–245 — está no documento de estudo entregue à diocese
  e no texto integral em vatican.va.</p>
</div>

<section class="anot">
  <h2>Anotações</h2>
  <div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div><div class="l"></div>
</section>

</body></html>""" % (CSS, linhas_indice, '\n'.join(corpo))

open(sys.argv[1], 'w').write(HTML)
print('html ok:', sys.argv[1], len(HTML), 'bytes')
