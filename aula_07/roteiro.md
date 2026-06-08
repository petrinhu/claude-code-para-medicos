# Aula 07 — Gestão do Consultório: Dashboard Cirúrgico

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~37 min  
**Tom:** Colega com humor leve e didático  

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Direto, virando a página do M3, nova perspectiva

"Nas últimas duas aulas você criou conteúdo para o Instagram
e submeteu um pôster de congresso.

Hoje a gente fecha o M3 com um problema diferente.

Não é sobre comunicar. Não é sobre pesquisar.
É sobre entender o próprio negócio.

Você é cirurgião.

A pergunta de hoje é simples e brutal:
onde está o seu dinheiro?

Vamos descobrir."

---

## SEÇÃO 2: O CENÁRIO (3 min)

**Tom:** Situação real, identificação imediata, dois problemas concretos

"Cenário.

Você é cirurgião geral. Consultório próprio, six anos de carreira.
Faz 8 a 12 procedimentos por semana — colecistectomia, herniorrafia,
apendicectomia de urgência, às vezes bariátrica.

Três convênios no seu CNPJ mais particular.

Problema 1: você não sabe qual procedimento é mais lucrativo.
Você acha que bariátrica paga mais, mas não tem certeza.
Você só sabe quando o extrato chega no fim do mês — e nem entende o extrato.

Problema 2: a sua taxa de no-show está alta mas você não sabe em qual dia da semana.
Você desconfia que é segunda — e provavelmente está certo — mas sem dado, é chute.

Hoje você vai ter os dados. Tudo em uma tela, em um arquivo.
Que você manda pro contador e ele entende.

Vamos começar."

---

## SEÇÃO 3: DEMO — GERAR O CSV DE PROCEDIMENTOS (8 min)

**Tom:** Prático, rápido, explicando o que cada coluna representa

"Primeiro: os dados.

Na vida real, você exportaria uma planilha do sistema do consultório.
Mas vamos gerar um CSV simulado — o fluxo é exatamente o mesmo.

Prompt:

```
Gere uma planilha CSV simulada com 120 procedimentos cirúrgicos
dos últimos 6 meses (janeiro a junho de 2025).

Colunas:
- Data: distribuída entre jan e jun 2025
- Dia_semana: segunda a sábado
- Procedimento: colecistectomia videolaparoscópica, herniorrafia inguinal,
  apendicectomia, cirurgia bariátrica (proporções realistas —
  colecistectomia e herniorrafia são os mais frequentes)
- Convenio: PlanoSol, PlanoNorte, PlanoCentro, Particular
  (nomes fictícios — distribua de forma realista)
- Valor_recebido_R$: valores realistas por procedimento e convênio
  (bariátrica mais cara, apendicectomia de urgência com variação)
- Status: realizado, no-show, cancelado
- Tempo_cirurgia_min: tempo médio realista por procedimento

Salve como procedimentos.csv.
```

[executar e mostrar o arquivo]

Pronto. 120 linhas, 7 colunas.

Veja a coluna Status — tem 'realizado', 'no-show', 'cancelado'.
Veja a coluna Valor_recebido_R$ — cada convênio paga diferente pelo mesmo procedimento.

Isso é a realidade do consultório. E agora vamos enxergar ela com clareza."

---

## SEÇÃO 4: DEMO — ANÁLISE DE INDICADORES (8 min)

**Tom:** Didático, mostrando cada indicador com reação clínica

"Com a planilha criada, vamos pedir a análise completa.

Prompt:

```
Analise o arquivo procedimentos.csv e me entregue um relatório
de indicadores de gestão do consultório:

1. Faturamento total dos 6 meses
2. Faturamento por convênio — ranking do maior para o menor pagador
3. Faturamento por tipo de procedimento — qual é o mais lucrativo?
4. Taxa de no-show geral (%) e por dia da semana
   — em qual dia tenho mais falta?
5. Tempo médio de cirurgia por tipo de procedimento
6. Tendência de faturamento mês a mês (jan a jun)
   — estou crescendo ou caindo?

Para cada indicador: um parágrafo curto de interpretação
mais uma tabela quando relevante.
```

[executar e mostrar resultado]

Olha o que saiu.

Faturamento total — você sabe pela primeira vez exatamente quanto entrou.

Ranking de convênios — o PlanoSol paga mais que o PlanoCentro pelo mesmo procedimento?
Isso muda decisão de credenciamento.

No-show por dia — segunda realmente lidera? Confirme e já ajuste a agenda.

Tendência mensal — fevereiro caiu? Provavelmente por causa do carnaval.
Abril subiu? Talvez porque você contratou um secretário novo.

Esses números contam a história do consultório. Agora você vai colocar ela numa tela."

---

## SEÇÃO 5: DEMO — DASHBOARD HTML AUTÔNOMO (12 min)

**Tom:** Revelação, mostrando o resultado ao abrir no navegador

"Agora a cereja do bolo.

Tudo que analisamos vai virar um dashboard — uma tela com gráficos e indicadores —
em um único arquivo que você abre no navegador.

Sem instalar nada. Sem login. Sem servidor. Funciona no Windows, no Mac, no celular.
Você manda por e-mail pro contador e ele abre no computador dele.

Prompt:

```
Com base nos dados de procedimentos.csv, crie um dashboard de gestão
do consultório cirúrgico.

O resultado deve ser um único arquivo HTML que funciona no navegador
sem precisar de internet ou servidor.

Conteúdo do dashboard:

Linha superior — 4 cards de resumo:
- Faturamento total (6 meses)
- Total de procedimentos realizados
- Taxa de no-show (%)
- Procedimento mais rentável

Gráficos:
1. Barras: faturamento por convênio (PlanoSol, PlanoNorte, PlanoCentro, Particular)
2. Linha: faturamento mensal (janeiro a junho)
3. Barras horizontais: faturamento por tipo de procedimento

Tabela:
- No-show por dia da semana (contagem e percentual)

Estilo: limpo, fundo branco, cores sóbrias. Todos os dados embutidos
no próprio arquivo — nada de arquivo CSV separado.

Salve como dashboard_cirurgico.html.
```

[executar e aguardar]

[abrir o arquivo no navegador]

Olha isso.

Cards de resumo no topo — uma olhada e você sabe o mês.
Gráfico de barras — em dois segundos você vê qual convênio paga mais.
Gráfico de linha — a tendência dos 6 meses na frente dos seus olhos.
Tabela de no-show — segunda realmente é o pior dia.

Este arquivo tem 400, 500 linhas de código por dentro.
Você não viu nenhuma delas. Você só descreveu o que queria.

É exatamente assim que o Claude Code funciona:
você descreve o resultado, ele constrói os meios."

---

## SEÇÃO 6: ENCERRAMENTO + FECHAMENTO DO M3 (4 min)

**Tom:** Motivador, dois níveis de encerramento — aula e módulo

"Resumo do que a gente fez hoje.

O cirurgião saiu daqui com:
— CSV com 6 meses de procedimentos analisado estatisticamente
— Ranking de convênios, ranking de procedimentos, no-show por dia
— Dashboard HTML pronto, offline, para mandar ao contador

Em menos de 30 minutos. Sem planilha de Excel complexa. Sem Power BI. Sem programar.

Agora o dever de casa.

Pegue uma planilha real do seu consultório — pode ser de agendamentos,
de faturamento, de qualquer coisa.
Anonimize: troque nomes de pacientes por ID, remova CPF e data de nascimento.
E peça ao Claude os mesmos indicadores que a gente gerou hoje.

Só isso. Dado real, mesma lógica.

---

E com isso a gente fecha o Módulo 3.

Pensa no que vocês fizeram neste módulo:

**Aula 05:** Instagram com carrossel sobre uma tópico clínico sofisticado,
newsletter da semana pronta para o Substack.

**Aula 06:** Estudo observacional com 50 pacientes, análise de correlação,
dois gráficos para publicação, pôster completo no formato ABNT.

**Aula 07:** Dashboard de gestão do consultório, indicadores claros,
arquivo HTML pronto para o contador.

Tudo sem programar. Tudo sem saber estatística computacional.
Só descrevendo o problema em linguagem natural.

Isso é Claude Code para Médicos.

---

Agora a pergunta: você quer ir além?

A fase avançada é opcional. Mas se você quer entender como construir apps clínicos reais —
com interface gráfica, banco de dados local, busca por inteligência artificial em PDFs —
a próxima aula começa essa jornada.

É uma fase diferente. Vai ter um pouco de código. Mas vai ser guiado, passo a passo,
do jeito que você aprendeu um novo protocolo clínico.

Se quiser continuar: até a aula_08.
Se preferir parar aqui: você já tem mais do que a maioria dos médicos.

Nos dois casos: obrigado por chegar até aqui."

---

**FIM DO ROTEIRO**
