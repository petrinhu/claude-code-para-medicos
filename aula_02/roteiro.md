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

Isso é o que eu chamo de inteligência de guideline.

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

Existem versões diferentes do Claude — pensa nelas como uma equipe de níveis diferentes.
O Haiku é o residente rápido: resolve o simples num instante.
O Sonnet é o clínico geral competente — dá conta de quase tudo, e é o padrão.
O Opus é o especialista, que você chama nos casos mais difíceis.
E o mais novo e mais forte de todos é o Fable 5: o professor titular, que aguenta os casos
mais longos e complexos sem perder o fio do raciocínio — daqueles que levam horas de
trabalho seguido. Ele tem até um cuidado de segurança embutido: em temas sensíveis, passa
o caso sozinho para o Opus.

Para esta aula — limpar uma planilha, gerar bullets — o Sonnet, que é o padrão, serve para
tudo. Você não chama o professor titular para medir uma pressão.

E tem mais um controle que vale conhecer desde já: o esforço — em inglês, o 'effort'.
É quanto o Claude pensa antes de responder. É igual ao seu raciocínio clínico: num resfriado
você decide rápido; num caso difícil, você para, revisa e pensa com calma. Você pode pedir
ao Claude mais esforço para um problema cabeludo — ele pensa mais fundo, demora um pouco
mais — ou menos esforço para uma tarefa boba e rápida. No dia a dia desta aula, o esforço
padrão dá conta.

Regra de bolso: comece sempre com o padrão — Sonnet, esforço normal. Conforme o curso
avançar e os seus pedidos ficarem mais complexos, aí você sobe o modelo (Opus ou Fable 5)
e o esforço. Vamos aprofundar essa escolha quando você tiver mais fluência.

E gráficos? Para gerar gráficos o Claude precisaria de Python.
Isso fica para a fase avançada do curso — por enquanto,
planilha limpa e organizada já resolve 80% dos casos."

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

Olha as demos que a gente fez hoje.

PDF de guideline. Comparação de versões. Extração de tabela. Planilha de dados. Slides. Folheto.

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

Seis entregáveis. Uma sessão. Sem programar. Sem copiar e colar manualmente.

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
