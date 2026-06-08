# Aula 02 — Assistente de Produtividade

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~56 min  
**Tom:** Colega com humor leve e didático  

---

## SEÇÃO 1: ABERTURA (3 min)

**Tom:** Pessoal, direto, conectando com a aula anterior

"Na aula de abertura a gente instalou o Claude Code, tirou o medo de terminal,
e eu mostrei pra vocês que 95% deste curso foi feito com IA.

Hoje a gente começa a usar de verdade.

Sem teoria. Sem enrolação. Sem slides explicando o que é IA.

A gente vai pegar um problema clínico real, do tipo que vocês têm toda semana,
e resolver do início ao fim usando o Claude Code.

Pera — antes de começar, uma pergunta: vocês já viram aquela situação
em que o residente chega na sexta às 16h e fala 'professor, eu apresento
aquela aula segunda de manhã'?

É. Hoje vocês vão ser o residente. Mas com uma diferença."

---

## SEÇÃO 2: O CENÁRIO (2 min)

**Tom:** Situação real, urgente, com humor

"Imaginem esse cenário.

É sexta-feira. 17h. Vocês acabaram a última consulta.
O coordenador da residência manda mensagem:
'Doutor, o palestrante da segunda foi cancelado.
Você consegue apresentar uma aula sobre depressão pra turma? Às 8h.'

Pânico normal.

[pausa]

Mas vocês têm Claude Code.

E eu vou mostrar que em menos de 1 hora vocês saem dessa reunião com:
— Uma guideline de depressão resumida
— Uma planilha de dados organizada
— Slides prontos pra apresentar
— Um folheto de orientação pra distribuir pros pacientes

Tudo feito ao vivo. Agora.

Vamos lá."

---

## SEÇÃO 3: DEMO — RESUMIR GUIDELINE DE DEPRESSÃO (12 min)

**Tom:** Pausado, didático, mostrando cada passo na tela

"Primeira tarefa: a gente precisa de conteúdo. E conteúdo de qualidade vem
de guideline. Vou usar aqui o guideline da APA — American Psychiatric Association —
sobre tratamento de depressão. É documento público, está em PDF.

[mostrar o PDF baixado na pasta]

Abro o Claude Code. Primeiro: vou anexar o PDF.
No Claude Code, basta arrastar o arquivo ou usar o comando de anexar.

[mostrar como anexar o PDF]

Agora o prompt. Preste atenção como eu escrevo — não é um comando técnico,
é linguagem natural:

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

[executar e mostrar o resultado]

Viu o que aconteceu?

O Claude leu o documento inteiro — que tem quantas páginas? [mostrar] —
e devolveu tópicos estruturados, prontos pra virar slide.

Repara: eu não pedi 'faça um resumo'. Eu dei contexto clínico —
quem sou, para quem apresento, qual a estrutura que preciso.
Isso faz diferença enorme na qualidade da resposta.

Uma coisa importante antes de continuar.

Se você está assistindo isso em casa e tentou fazer o mesmo prompt —
a resposta que apareceu pra você provavelmente foi diferente da minha.
Talvez a ordem dos tópicos mudou. Talvez o texto ficou mais longo, ou mais curto.
Talvez as palavras foram outras.

Isso é normal. Isso é esperado. E isso não é erro.

O Claude não é uma calculadora — ele não devolve sempre o mesmo resultado.
Ele é como um especialista que você consulta: se você perguntar a mesma coisa
pra dois psiquiatras diferentes, eles vão te dar respostas com nuances diferentes.
Ambas corretas. Ambas úteis.

Essa não-determinismo — essa variação criativa — é exatamente uma das belezas da IA.
Você não precisa chegar no mesmo resultado que eu.
Você precisa chegar num resultado bom pro seu contexto.

Então: não tente copiar minha tela. Use como referência de processo —
o que perguntar, como estruturar o prompt, o que esperar como retorno.
O conteúdo vai ser seu, adaptado pra você.

Antes de ir pra próxima demo, para um segundo.
Preciso te contar algo sobre os modelos do Claude."

---

## SEÇÃO 4: MODELOS + TOKENS (8 min)

**Tom:** Explicativo, com analogia clínica, leve

"Pra você usar Claude Code com inteligência — e gastar menos —
você precisa entender que o Claude não é um modelo único.
São três modelos diferentes. E você escolhe qual usar.

Pensa assim:

**Haiku — o Residente**
Rápido, entusiasmado, resolve casos simples muito bem.
Se você mandar um caso complexo de hepatite autoimune com manifestação incomum,
ele pode simplificar demais ou errar. Mas pra tarefa simples? É ótimo.

**Sonnet — o Especialista**
É o seu residente sênior que já fez especialização.
Rápido o suficiente, raciocínio confiável, resolve 95% das coisas.
É o modelo padrão. Começa sempre com ele.

**Opus — o Chefe do Departamento**
Pensa mais devagar, mas pensa melhor. Para casos raros, complexos,
onde você precisa de raciocínio profundo. Mais caro, mais lento.
Só chame quando o Sonnet não foi suficiente.

Agora: o que são tokens?

Token é o 'custo' de cada palavra que você manda e recebe.
Aproximadamente: 1 token = 4 caracteres. Uma frase dessas tem umas 20 tokens.
Um artigo inteiro de 10 páginas? Uns 8.000 tokens.

Por que isso importa?

Porque cada modelo tem um preço por token. Haiku é bem barato.
Sonnet custa um pouco mais. Opus é o mais caro.

Na prática, pra uso médico normal — 10 conversas ricas por dia —
você vai gastar menos de 5 reais por mês no Sonnet.
Não é o que vai quebrar seu consultório.

Mas se você tiver uma tarefa simples — limpar uma planilha, 
renomear arquivos, extrair um número de uma tabela —
use Haiku. Resultado igual, custo menor, mais rápido.

Como trocar de modelo no Claude Code?

[mostrar na tela como selecionar o modelo — botão ou comando /model]

Simples assim. Vou mostrar isso agora na próxima demo."

---

## SEÇÃO 5: DEMO — PLANILHA DE DADOS DE PESQUISA (8 min)

**Tom:** Prático, mostrando comparação Haiku x Sonnet

"Segunda tarefa: organizar dados de pesquisa.

Vamos supor que você tem uma planilha bagunçada de um estudo piloto
que você fez com pacientes deprimidos — escores MADRS em quatro visitas.
Os dados chegaram sujos. Vejam:

[mostrar planilha com dados simulados — pode ser no editor de texto ou CSV]

```
nome , visita1 , visita2 , visita3 , visita4
João  , 18 ,  14 , 9 , 5
maria,  22  , 19, 15,  9
Pedro , 16, 12 , 8 ,4
ana luiza, 20 , 17, 12 ,7
```

Tarefa simples: limpar espaços, padronizar nomes, calcular média de melhora.

Olha — essa é uma tarefa simples. Não preciso do especialista.
Vou trocar pra Haiku.

[mostrar troca de modelo na interface]

Prompt:

```
Limpe esta planilha de dados MADRS: padronize os nomes (primeira letra maiúscula),
remova espaços extras, adicione uma coluna 'reducao_total' que é visita1 menos visita4,
e ordene por maior redução. Me devolva a planilha limpa em formato CSV.
```

[executar e mostrar resultado]

Rápido. Resultado perfeito. E gastou uma fração do custo do Sonnet.

Regra prática:
— Tarefa simples, direta → Haiku
— Análise, síntese, raciocínio → Sonnet
— Raciocínio profundo, caso complexo → Opus

Agora vamos montar os slides."

---

## SEÇÃO 6: DEMO — SLIDES DA AULA (12 min)

**Tom:** Empolgado, mostrando a transformação dos bullets em aula

"Lembra do resumo que a gente fez do guideline lá atrás?

Aqueles bullets que o Claude gerou — vamos transformar em slides.

Volto pro Sonnet — essa tarefa exige criatividade e estrutura.

[mostrar troca de modelo se necessário]

Vou copiar os bullets gerados na seção anterior e usar como base.
Prompt:

```
Você é um especialista em educação médica. Com base nos tópicos abaixo
sobre depressão (extraídos do guideline da APA), crie uma aula em formato
de slides para residentes de psiquiatria com as seguintes regras:
- Slide de abertura: título da aula, nome do apresentador, data
- Um slide por tópico principal (6 tópicos)
- Cada slide: título + 4 bullets concisos + 1 pérola clínica (dica prática)
- Slide de encerramento: 3 mensagens-chave para levar pra casa
- Tom: didático, sem jargão desnecessário

[colar os bullets do guideline aqui]
```

[executar e mostrar resultado]

Olha o que saiu.

Slide de abertura. Título. Seis slides de conteúdo, cada um com a pérola clínica.
Encerramento com mensagens-chave.

Você pega isso, copia pro PowerPoint ou Google Slides,
ajusta a fonte, coloca logo da instituição, e está pronto.

O que você economizou? Umas 3 horas de trabalho manual.
O que você pagou? Menos de 1 real em tokens.

Vale o trade? Sem dúvida.

Última tarefa: o folheto pra paciente."

---

## SEÇÃO 7: DEMO — FOLHETO PÓS-CONSULTA (8 min)

**Tom:** Cuidadoso, ressaltando a importância da comunicação com o paciente

"Última entrega do dia: um folheto de orientação pra paciente
que acabou de receber diagnóstico de depressão.

Isso é algo que todo psiquiatra e clínico geral precisa ter.
E raramente tem tempo de fazer bem feito.

Sonnet de volta — quero qualidade na linguagem.

Prompt:

```
Crie um folheto de orientação para paciente recém-diagnosticado com depressão.
Requisitos:
- Linguagem simples, sem jargão médico — como se você explicasse para um familiar
- Seções: O que é depressão, Por que acontece, Como é o tratamento, 
  O que esperar das primeiras semanas, Quando ligar para o médico
- Tom: acolhedor, esperançoso, sem minimizar a doença
- Máximo 1 página A4
- Incluir ao final: 'CVV — Centro de Valorização da Vida: 188'
```

[executar e mostrar resultado]

Pronto.

Um folheto que qualquer paciente consegue ler e entender.
Sem jargão. Com acolhimento. Com o número do CVV.

Você pode imprimir isso hoje e distribuir na sua próxima consulta.

E perceba: em nenhum momento colocamos dado de paciente real.
Criamos um documento genérico — isso é LGPD na prática.
O Claude ajudou, mas o dado sensível ficou no seu consultório."

---

## SEÇÃO 8: ENCERRAMENTO + DEVER DE CASA (3 min)

**Tom:** Motivador, resumo rápido, desafio claro

"Deixa eu resumir o que a gente fez hoje.

Chegamos com um problema real: aula de depressão, segunda de manhã, sem preparação.

E saímos com:
1. Guideline resumida em tópicos estruturados — Sonnet
2. Planilha de pesquisa limpa e organizada — Haiku
3. Slides completos com pérolas clínicas — Sonnet
4. Folheto de orientação pro paciente — Sonnet

Sem programar. Sem saber de IA. Só descrevendo o problema em linguagem natural.

E você aprendeu que existem 3 modelos — Haiku, Sonnet, Opus —
e que a escolha certa economiza tempo e dinheiro sem perder qualidade.

Agora o dever de casa.

Antes da próxima aula, quero que você faça isso:

Pegue um PDF da sua especialidade — um artigo, uma diretriz, um protocolo
que você tem engavetado — e mande para o Claude Code com o prompt:

```
Resuma este documento em 6 bullets principais.
Use linguagem para especialista da área.
```

Só isso. Simples. Veja o que sai.

Se travar em alguma parte, anota onde travou — a gente resolve na próxima aula.

Na aula 03: a gente vai buscar artigos diretamente no PubMed
sem sair do Claude Code. Vai mudar o jeito que vocês se atualizam.

Até lá."

---

**FIM DO ROTEIRO**
