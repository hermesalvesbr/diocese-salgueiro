import os, sys
S = os.path.dirname(os.path.abspath(__file__))
h = open(S + '/cartoes.html').read()

FRENTE = """
    <div class="card">
      <div class="eyebrow">Diocese de Salgueiro &middot; 22 de agosto de 2026</div>
      <h1>Três compromissos</h1>
      <div class="lead">Escritos por mim, no encontro sobre a <i>Magnifica Humanitas</i>.</div>

      <div class="campo">
        <div class="rot"><b>1</b>Um uso que vou testar nos próximos 30 dias</div>
        <div class="lin"></div><div class="lin sec"></div>
      </div>
      <div class="campo">
        <div class="rot"><b>2</b>Um limite que vou respeitar</div>
        <div class="lin"></div><div class="lin sec"></div>
      </div>
      <div class="campo">
        <div class="rot"><b>3</b>Uma pessoa da minha paróquia que vou formar</div>
        <div class="hint">“artesãos em educar” &middot; §&thinsp;238</div>
        <div class="lin"></div><div class="lin"></div>
      </div>

      <div class="rodape">
        Pe. <span class="lg" style="width:37mm"></span>&nbsp;&nbsp;Paróquia <span class="lg" style="width:28mm"></span><br>
        <span style="display:inline-block;margin-top:1.6mm">Reler este cartão em <span class="lg" style="width:22mm"></span> &nbsp;(60 dias)</span>
      </div>
    </div>"""

VERSO = """
    <div class="card verso">
      <div class="marca">Antes de usar, pergunte</div>
      <h2>Duas perguntas que funcionam sem saber nada de tecnologia</h2>

      <div class="painel">
        <div class="perg">
          <p>Isto torna a vida das pessoas <b>&ldquo;mais humana&rdquo;</b>? Torna-a <b>&ldquo;mais digna do homem&rdquo;</b>?</p>
          <div class="ref">&sect;&thinsp;129 &middot; p.&thinsp;44 &mdash; Le&atilde;o XIV citando S&atilde;o Jo&atilde;o Paulo II</div>
        </div>
        <div class="perg">
          <p>Esta &eacute; uma situa&ccedil;&atilde;o em que eu deveria <b>n&atilde;o usar</b>?</p>
          <div class="ref">&sect;&thinsp;140 &middot; p.&thinsp;48</div>
        </div>
      </div>

      <div class="jejum">
        <div class="q">&ldquo;Devemos educar-nos ao jejum da IA e proteger os nossos jovens das promessas da m&aacute;quina perfeita.&rdquo; &sect;&thinsp;140</div>
        <div class="verbos">FI&Eacute;IS &Agrave; VERDADE &middot; INVESTIR NA EDUCA&Ccedil;&Atilde;O &middot; CUIDAR DAS RELA&Ccedil;&Otilde;ES &middot; AMAR A JUSTI&Ccedil;A E A PAZ &middot; &sect;&thinsp;236</div>
      </div>
    </div>"""

# marcas de corte: nas bordas da folha, alinhadas às linhas de corte
ticks = []
for x in (5, 105, 205):                       # linhas verticais de corte
    ticks.append('<div class="tick tv" style="left:%smm;top:2.5mm"></div>' % x)
    ticks.append('<div class="tick tv" style="left:%smm;top:289.5mm"></div>' % x)
for y in (8.5, 148.5, 288.5):                 # linhas horizontais de corte
    ticks.append('<div class="tick th" style="top:%smm;left:0"></div>' % y)
    ticks.append('<div class="tick th" style="top:%smm;right:0"></div>' % y)
T = '\n'.join(ticks)

h = h.replace('<!--CARDS_FRENTE-->', FRENTE * 4)
h = h.replace('<!--CARDS_VERSO-->', VERSO * 4)
h = h.replace('<!--TICKS-->', T)
open(sys.argv[1], 'w').write(h)
print('cartoes html ok')
