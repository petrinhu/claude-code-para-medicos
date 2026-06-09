# Aula 02 — Roteiro Refatorado — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Substituir `aula_02/roteiro.md` com roteiro correto cobrindo M1.01–04 em abordagem demo encadeada (~46 min).

**Architecture:** Arquivo único `aula_02/roteiro.md` em formato Markdown canônico do curso (seções numeradas, Tom, falas entre aspas, blocos copiáveis). Segue spec aprovado em `docs/superpowers/specs/2026-06-08-aula02-design.md`. Acompanhado de `roteiro.html` gerado via pandoc.

**Tech Stack:** Markdown, pandoc (HTML export), Git.

---

## Referência rápida do spec

| Seção | Conteúdo | Duração |
|---|---|---|
| 1 | Âncora + Cenário: callback aula_01 + "sexta 17h" + preview entregável | 4 min |
| 2 | PDF — Resumir (M1.01 parte 1): guideline APA + prompt com contexto clínico | 8 min |
| 3 | PDF — Comparar + Extrair tabela (M1.01 partes 2+3): versão antiga vs nova → CSV | 6 min |
| 4 | Planilha (M1.04): tabela extraída + MADRS suja → limpa; 1 min modelos | 7 min |
| 5 | Slides (M1.03): bullets da S2 → slides com pérola clínica | 10 min |
| 6 | Folheto pós-consulta (M1.02): folheto para paciente + LGPD reforçado | 8 min |
| 7 | Fechamento + Dever de casa: antes/depois + dever + ponte aula_03 | 3 min |

**Demo encadeada:** S2 gera bullets → S5 usa como input | S3 extrai tabela → S4 usa como input  
**Tema:** Depressão (guideline APA, planilha MADRS) — válido para toda especialidade médica

---

## Task 1: Escrever `aula_02/roteiro.md`

**Files:**
- Modify: `aula_02/roteiro.md` (sobrescrever conteúdo atual)

- [ ] **Step 1: Escrever o roteiro completo**

Conteúdo completo do arquivo:

```markdown
# Aula 02 — Claude Code com Arquivos Reais

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~46-50 min  
**Tom:** Colega com humor leve e didático — "hoje você para de conversar e começa a trabalhar"  
**Fio narrativo:** Sexta 17h, palestrante de depressão cancelado, aula segunda às 8h  

---

## SEÇÃO 1: ÂNCORA + CENÁRIO — 4 min

**Tom:** Callback direto da aula_01, cenário de urgência clínica real

"Na aula_01 você aprendeu a conversar com o Claude.

Sabe pedir. Sabe anexar. Sabe revisar. Sabe iterar.

Hoje você para de conversar e começa a trabalhar.

---

Imaginem esse cenário.

É sexta-feira. 17h. Você acabou a última consulta.
O coordenador da residência manda mensagem:

'Doutor, o palestrante de segunda foi cancelado.
Você consegue apresentar uma aula sobre depressão pra turma? Às 8h da manhã.'

Pânico normal.

[pausa de um segundo]

Mas você tem o Claude Code.

---

Vou mostrar que quando a gente terminar essa aula,
você vai sair com quatro coisas prontas:

[mostrar na tela — abrir uma lista]

Um: guideline da APA resumida em tópicos estruturados.
Dois: comparação com versões anteriores — o que mudou na conduta.
Três: slides completos, prontos para abrir no PowerPoint.
Quatro: folheto de orientação para distribuir aos pacientes.

Tudo feito na mesma sessão.
Tudo sem dado identificável de paciente — LGPD do começo ao fim.

Vamos lá."

---

## SEÇÃO 2: PDF — RESUMIR (M1.01 PARTE 1) — 8 min

**Tom:** Didático, mostrando cada passo — prompt construído em tempo real na tela

"Primeira tarefa: conteúdo de qualidade vem de guideline.

Vou usar o guideline da American Psychiatric Association —
documento público, disponível online, sem dado de paciente.

[mostrar o PDF baixado na pasta]

Abro o Claude Code. Primeiro: vou anexar o PDF.

[mostrar como anexar o arquivo na sessão]

Agora o prompt. Preste atenção em como eu escrevo —
não é comando técnico, é linguagem natural com contexto clínico:

[digitar no terminal]

```
Você é um psiquiatra experiente. Acabei de receber um convite de última hora
para apresentar uma aula sobre depressão para residentes na segunda-feira de manhã.
Preciso que você resuma este guideline da APA nos seguintes tópicos:
1. Epidemiologia
2. Etiopatogenia e neurobiologia
3. Quadro clínico e critérios diagnósticos (DSM-5/CID-11)
4. Diagnóstico diferencial
5. Tratamento (farmacológico, psicoterápico, ECT, estimulação magnética)
6. Casos especiais e depressão refratária

Para cada tópico: 4 a 6 bullets concisos. Linguagem para residentes de psiquiatria.
```

[aguardar e mostrar a resposta]

---

Olha o que saiu.

Seis tópicos. Bullets concisos. Linguagem clínica.
O Claude leu o documento inteiro e devolveu o esqueleto da aula.

Uma coisa importante:

Se você está assistindo isso em casa e o seu resultado ficou diferente do meu —
texto mais longo, outra ordem, outras palavras —
isso é normal. É esperado. Não é erro.

O Claude não é calculadora. Ele não devolve sempre o mesmo resultado.
É como dois especialistas respondendo a mesma pergunta:
ambos corretos, nuances diferentes.

Você não precisa chegar no mesmo resultado que eu.
Você precisa chegar num resultado bom para o seu contexto.

---

Esses bullets que acabaram de aparecer na tela —
não feche essa janela. Vamos usar eles daqui a pouco para montar os slides."

---

## SEÇÃO 3: PDF — COMPARAR + EXTRAIR TABELA (M1.01 PARTES 2 E 3) — 6 min

**Tom:** Revelar dois casos de uso do mesmo arquivo — sem reabrir, sem repassar o PDF

"O PDF ainda está na sessão. Não precisamos reabrir nada.

Segundo pedido — um caso de uso que você vai usar toda vez que sair um guideline novo:

[digitar no terminal]

```
Compare este guideline com as recomendações de diretrizes anteriores sobre depressão.
O que mudou nos critérios diagnósticos e nas recomendações de tratamento?
Liste as principais diferenças em bullets.
```

[aguardar e mostrar a resposta]

---

Isso é o que eu chamo de 'inteligência de guideline'.

Você não precisa ler os 80 páginas da versão nova e lembrar o que a versão antiga dizia.
Você pergunta: o que mudou? O Claude compara.

Na prática clínica isso vale ouro —
quando sai uma diretriz nova de hipertensão, de diabetes, de anticoagulação,
você sabe em dois minutos o que muda na sua conduta.

---

Agora terceiro pedido. Mesmo PDF, ainda na sessão:

[digitar no terminal]

```
Extraia do documento a tabela de critérios diagnósticos do DSM-5 para depressão maior.
Formate como lista estruturada, uma linha por critério.
```

[aguardar e mostrar a resposta]

---

Essa lista que acabou de aparecer —
vamos jogar ela numa planilha agora."

---

## SEÇÃO 4: PLANILHA (M1.04) — 7 min

**Tom:** Prático, dois insumos diferentes, mostrar limpeza de dados clínicos reais

"Segunda tarefa: dados de pesquisa.

Tenho dois insumos agora:
a lista de critérios que acabamos de extrair,
e uma planilha de dados MADRS que veio suja de um estudo piloto.

[mostrar o arquivo de planilha na tela]

Olha como chegou:

```
nome , visita1 , visita2 , visita3 , visita4
João  , 18 ,  14 , 9 , 5
maria,  22  , 19, 15,  9
Pedro , 16, 12 , 8 ,4
ana luiza, 20 , 17, 12 ,7
```

Nomes inconsistentes. Espaços sobrando em todo lugar.
Sem coluna de redução total.

Tarefa para o Claude:

[digitar no terminal — com o arquivo de planilha anexado]

```
Limpe esta planilha de dados MADRS:
- Padronize os nomes (primeira letra maiúscula, resto minúsculo)
- Remova todos os espaços extras
- Adicione uma coluna 'reducao_total' que é visita1 menos visita4
- Ordene por maior redução (decrescente)
Me devolva a planilha limpa em formato CSV.
```

[aguardar e mostrar a resposta]

---

Limpa. Organizada. Ordenada. Em CSV pronto para importar.

Uma nota rápida sobre modelos:

Existem versões diferentes do Claude — Haiku, Sonnet, Opus.
Para esta aula, o Sonnet — que é o padrão — serve para tudo.
Vamos aprofundar essa escolha quando você tiver mais fluência.

E gráficos? Para gerar gráficos o Claude precisaria de Python.
Isso fica para a fase avançada do curso — por enquanto, planilha limpa e organizada já resolve 80% dos casos."

---

## SEÇÃO 5: SLIDES (M1.03) — 10 min

**Tom:** Revelar que o contexto da sessão está preservado — não precisou repassar nada

"Terceira tarefa: os slides.

Lembra dos bullets que o Claude gerou no começo da aula?

O contexto ainda está aqui. Não preciso repassar o PDF.
Não preciso copiar e colar nada.

[mostrar que a sessão continua aberta]

Só dizer onde os bullets estão:

[digitar no terminal]

```
Com base nos tópicos sobre depressão que você gerou no início desta sessão,
crie uma estrutura de slides para residentes de psiquiatria com as seguintes regras:
- Slide de abertura: título da aula, nome do apresentador, data
- Um slide por tópico principal (6 tópicos)
- Cada slide: título + 4 bullets concisos + 1 pérola clínica (dica prática)
- Slide de encerramento: 3 mensagens-chave para levar pra casa
- Tom: didático, sem jargão desnecessário
```

[aguardar e mostrar a resposta]

---

Olha o que saiu.

Slide de abertura. Seis slides de conteúdo, cada um com a pérola clínica.
Encerramento com mensagens-chave.

Você copia isso pro PowerPoint ou Google Slides,
ajusta a fonte, coloca o logo da instituição, e está pronto.

O que você economizou? Umas três horas de trabalho manual.
O que você pagou? Menos de um real em tokens.

---

E repara numa coisa:

O Claude não esqueceu o que resumiu lá atrás.
Você não precisou repassar o PDF. Não precisou recopiar os tópicos.
O contexto da sessão estava preservado.

Isso é o prontuário funcionando — memória de tudo que aconteceu,
do início ao fim da sessão."

---

## SEÇÃO 6: FOLHETO PÓS-CONSULTA (M1.02) — 8 min

**Tom:** Cuidadoso com a linguagem — produto final que o paciente vai ler; LGPD explícito no fechamento

"Última entrega.

Um folheto de orientação para o paciente que acabou de receber diagnóstico de depressão.

Isso é algo que todo psiquiatra e clínico geral precisa ter.
E raramente tem tempo de fazer bem feito.

[digitar no terminal]

```
Crie um folheto de orientação para paciente recém-diagnosticado com depressão.
Requisitos:
- Linguagem simples, sem jargão médico — como se você explicasse para um familiar
- Seções: O que é depressão / Por que acontece / Como é o tratamento /
  O que esperar das primeiras semanas / Quando ligar para o médico
- Tom: acolhedor, esperançoso, sem minimizar a doença
- Máximo 1 página A4
- Incluir ao final: 'CVV — Centro de Valorização da Vida: 188'
```

[aguardar e mostrar a resposta]

---

Pronto.

Um folheto que qualquer paciente consegue ler e entender.
Sem jargão. Com acolhimento. Com o número do CVV.

Você imprime isso hoje e distribui na próxima consulta.

---

Agora para.

Olha as quatro demos que a gente fez hoje.

PDF de guideline. Comparação de versões. Planilha de dados. Slides. Folheto.

Em nenhum momento apareceu:
nome de paciente. RG. Data de nascimento. Número de prontuário.

Tudo que o Claude precisou foi do quadro clínico —
o que é a doença, quais são os critérios, como é o tratamento.

Isso é LGPD na prática.

Dado de paciente não entra no Claude Code.
Vou repetir isso em toda aula deste curso
até vocês repetirem no sonho."

---

## SEÇÃO 7: FECHAMENTO + DEVER DE CASA — 3 min

**Tom:** Antes/depois concreto, dever de casa com fluxo completo, ponte para aula_03

"Sexta 17h: zero preparação. Aula na segunda às 8h.

[mostrar o que foi produzido]

Agora você tem:
1. Guideline resumida em tópicos prontos para apresentar
2. Comparação com versões anteriores — o que mudou na conduta
3. Tabela de critérios extraída do documento
4. Planilha de dados limpa e organizada
5. Slides completos com pérolas clínicas
6. Folheto de orientação para o paciente

Seis entregáveis. Uma sessão. Sem saber programar. Sem copiar e colar manualmente.

---

**Dever de casa:**

Antes da aula_03, faça isso:

Pegue um documento real da sua especialidade —
PDF de protocolo, artigo, diretriz, qualquer coisa que você tem engavetada —
e percorra o fluxo completo:

Passo 1: resuma em tópicos.
Passo 2: extraia uma tabela ou lista de critérios.
Passo 3: crie um entregável — slide, folheto, ou resumo estruturado.

Não precisa usar depressão. Use a sua área.
O cirurgião usa protocolo de profilaxia.
O cardiologista usa diretriz de anticoagulação.
O pediatra usa calendário vacinal atualizado.

Traga o que você fez para a aula_03.

---

**Na próxima aula:**

Você não vai precisar trazer PDF de casa.

O Claude vai buscar os artigos direto no PubMed por você —
pesquisa bibliográfica, filtros por data e nível de evidência,
fichamento automático.

Você já sabe trabalhar com arquivos.
Na aula_03 você começa a pesquisar.

Até lá."

---

**FIM DO ROTEIRO**
```

- [ ] **Step 2: Verificar contra o spec**

Abrir `docs/superpowers/specs/2026-06-08-aula02-design.md` e confirmar cobertura:

| Item do spec | Presente no roteiro? |
|---|---|
| M1.01: resumir PDF com prompt estruturado | ✓ Seção 2 |
| M1.01: comparar dois documentos / versões | ✓ Seção 3 |
| M1.01: extrair tabela como lista estruturada | ✓ Seção 3 |
| M1.02: folheto para paciente | ✓ Seção 6 |
| M1.03: slides com pérola clínica por tópico | ✓ Seção 5 |
| M1.04: planilha limpar + calcular redução | ✓ Seção 4 |
| Demo encadeada: S2 bullets → S5 slides | ✓ Seção 5 referencia S2 |
| Demo encadeada: S3 tabela → S4 planilha | ✓ Seção 3→4 bridge explícito |
| Modelos: 1 min embutido em S4 | ✓ Seção 4 |
| Gráfico omitido com menção fase avançada | ✓ Seção 4 |
| LGPD reforçado em S6 + nenhum dado nas demos | ✓ Seção 6 |
| Variação natural do Claude explicada | ✓ Seção 2 |
| Cenário "sexta 17h" | ✓ Seção 1 |
| Preview entregável no início | ✓ Seção 1 |
| Ponte para aula_03 (PubMed) | ✓ Seção 7 |
| Duração ~46 min | ✓ (4+8+6+7+10+8+3=46 min) |

- [ ] **Step 3: Commitar o roteiro**

```bash
git add aula_02/roteiro.md
git commit -m "feat: aula_02 roteiro refatorado — M1.01-04 demo encadeada (~46min)

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Task 2: Gerar `aula_02/roteiro.html`

**Files:**
- Create: `aula_02/roteiro.html`

- [ ] **Step 1: Gerar HTML via pandoc**

```bash
cd /home/petrus/IDrive/Vídeos/Dieckmann/aulas_claude_dieckmann/aula_02
pandoc roteiro.md -o roteiro.html --standalone --metadata title="Aula 02 — Claude Code com Arquivos Reais"
```

Expected: arquivo `roteiro.html` criado sem erros.

- [ ] **Step 2: Verificar que o HTML foi gerado**

```bash
ls -lh roteiro.html
```

Expected: arquivo com tamanho > 0.

- [ ] **Step 3: Commitar o HTML**

```bash
git add aula_02/roteiro.html
git commit -m "feat: aula_02 roteiro.html gerado

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Checklist de self-review do plano

- [x] Spec coverage: todos os 16 itens do spec cobertos nas tasks
- [x] Placeholder scan: sem TBDs, sem "similar to task N", sem "handle edge cases"
- [x] Conteúdo de demo inclui prompts reais (não genéricos)
- [x] Duração calculada: 4+8+6+7+10+8+3 = 46 min dentro do alvo 45-55 min
- [x] Demo encadeada explícita: S2→S5 (bullets→slides) e S3→S4 (tabela→planilha)
- [x] LGPD reforçado em S6 com enumeration explícita das quatro demos
- [x] Modelos+tokens: 1 min embutido em S4 (não seção própria)
- [x] Gráfico: omitido com menção controlada à fase avançada
- [x] Ponte para aula_03: PubMed mencionado em S7
- [x] Nenhuma nova analogia central — reservado para aula_17 ("residente de plantão")
