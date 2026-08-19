# Material impresso — encontro de 22 de agosto de 2026

Três PDFs, prontos para impressão em A4 — dois para os padres, um só para quem conduz.
Todos diagramados para sair direto da impressora da diocese, sem ajuste.

> Estas mesmas instruções estão em `como-imprimir.pdf` (2 páginas A4), para entregar
> a quem for imprimir.

| Arquivo | O que é | Páginas | Onde entra no roteiro |
|---|---|---|---|
| `enciclica-recorte-cap3-cap4.pdf` | Recorte de leitura da encíclica, §90 a §153 | 26 (A4) | Blocos 2, 3 e 4 |
| `cartoes-tres-compromissos.pdf` | Cartão dos três compromissos, 4 por folha | 2 (frente e verso) | Bloco 5 |
| `guia-do-facilitador.pdf` | Roteiro de condução, o mural sem flip chart, medo → §, véspera e dia | 4 (A4) | Só o facilitador |

---

## 1. Recorte da encíclica — um por padre

**Conteúdo:** capa · página de uso e índice das 24 passagens citadas no encontro ·
Capítulo III inteiro e início do Capítulo IV (§90–§153, pp. 33–51 do PDF oficial) ·
página de anotações.

O texto é o oficial, conferido palavra por palavra contra o PDF da Santa Sé; muda apenas
a diagramação. A numeração dos parágrafos fica na margem esquerda e uma barrinha discreta
(`|35`) marca onde começa cada página do PDF oficial — é o que permite ao padre achar
em segundos uma citação anunciada como "§ 99, p. 35".

**Impressão**

- Frente e verso, **virando na borda longa** (é o padrão; as margens são espelhadas para isso:
  26 mm do lado da encadernação, 18 mm do lado de fora).
- **Escala 100% / "tamanho real"** — nunca "ajustar à página", que encolhe o texto e come a margem.
- Preto e branco resolve; os detalhes em marrom saem em cinza e continuam legíveis.
- **13 folhas por exemplar.** Dois grampos na margem esquerda.
- Tiragem de **40 exemplares ≈ 520 folhas A4**.

> Se a lista da secretaria mudar, cada exemplar a mais custa 13 folhas A4 e ¼ de folha de
> papel-cartão. Rode os dois materiais na mesma tiragem, para ninguém ficar com o caderno e sem o cartão.

## 2. Cartões dos três compromissos — um por padre

**Frente:** os três compromissos para escrever à mão (um uso, um limite, uma pessoa),
com linhas, nome, paróquia e a data de releitura em 60 dias.
**Verso:** as duas perguntas de discernimento — §129 ("mais humana? mais digna do homem?")
e §140 ("é uma situação em que eu deveria *não* usar?") — mais a frase do jejum da IA
e os quatro verbos do §236.

**Impressão**

- Frente e verso, **escala 100%**. Como os quatro cartões da folha são iguais, não existe
  risco de desalinhamento entre frente e verso: qualquer sentido de virada funciona.
- Papel de gramatura alta (**180–250 g**) — o cartão precisa sobreviver 60 dias no breviário.
- **4 cartões por folha** (100 × 140 mm cada). Corte nas linhas indicadas pelas marcas nas
  bordas da folha: um corte vertical no meio e dois horizontais.
- Para 40 cartões, **10 folhas**.

## 2b. Guia do facilitador — um exemplar só

Quatro páginas A4, frente e verso em duas folhas, para o senhor levar no púlpito junto com o caderno da
encíclica. Traz os 120 minutos bloco a bloco, as cinco decisões de tom, os cinco silêncios, o que fazer
sem flip chart, a tabela de medo → § e os checklists da véspera e do dia.

## 3. Conferência na entrega

Vale abrir um exemplar de cada antes de sair da gráfica ou da secretaria.

- [ ] Saíram os **40 exemplares** de cada material — 40 cadernos grampeados e 40 cartões
      cortados — mais as duas cópias do documento de estudo para o bispo e a secretaria.
- [ ] O miolo do recorte está grampeado à esquerda e **nenhuma linha de texto entrou no grampo** —
      é o que a margem de 26 mm garante quando a escala foi mantida em 100%.
- [ ] Frente e verso do recorte estão na mesma orientação: virando a folha pela borda longa,
      o texto do verso fica de cabeça para cima.
- [ ] Os cartões saíram em 100 × 140 mm, com as duas perguntas no verso e o papel firme o
      bastante para escrever à mão sem apoio.

## 4. O que não vai impresso

- **Flip chart e pincel** — não é impresso, mas é do mesmo checklist e é estrutural: o quadro
  de medos do Bloco 0 volta no Bloco 4.
- **Documento de estudo** (`magnifica-humanitas-estudo.md`) — entregue digital; 2 ou 3 cópias
  impressas bastam, para o bispo e a secretaria.
- **Tabela de ferramentas do Bloco 3** — deliberadamente fora do material impresso: contém
  datas (Sora, Microsoft Lens, Suno) que o roteiro manda reconferir na véspera.

## 5. Para regerar os PDFs

```bash
cd impressos/fonte && ./build.sh
```

Requer `poppler-utils`, `python3` e `google-chrome`. O script relê o PDF oficial da encíclica
na raiz do projeto, remonta o texto e regrava os três PDFs.
