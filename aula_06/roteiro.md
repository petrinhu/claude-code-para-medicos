# Aula 06 — Pôster de Congresso + Análise de Dados

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~41 min  
**Tom:** Colega com humor leve e didático  

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Direto, conectando com aula_05, elevando o nível

"Na semana passada você criou o carrossel sobre a tríade obesidade-inflamação-depressão
e a newsletter da semana. Você tem Instagram agora.

Aí um colega viu o seu conteúdo e perguntou:
'Você tem esse dado publicado em algum congresso?'

Não ainda.

Hoje você publica.

Você vai pegar os dados reais do seu consultório — anonimizados —
e sair daqui com análise estatística, dois gráficos para publicação
e o texto completo do pôster pronto para diagramar.

Vamos lá."

---

## SEÇÃO 2: O CENÁRIO (3 min)

**Tom:** Situação real, pressão de prazo, dois obstáculos claros

"Cenário.

Mesma metabologista da semana passada. Ela tem 50 pacientes no consultório —
todos com IMC, HbA1c e PHQ-9 registrados na planilha.

Há tempos ela suspeita que os pacientes com depressão mais grave têm
pior controle glicêmico. É uma hipótese clínica que qualquer metabologista consideraria.

Problema 1: ela nunca formalizou isso estatisticamente.
Não sabe R, não sabe Python, não sabe SPSS.

Problema 2: tem um congresso de endocrinologia em 3 meses.
O prazo de submissão de pôsteres é semana que vem.

O Claude resolve os dois.

Não precisa saber programar para fazer estatística.
Não precisa saber escrever paper para escrever um pôster científico.

Você descreve o problema, o Claude executa.

Vamos começar pelos dados."

---

## SEÇÃO 3: DEMO — GERAR + ANALISAR O CSV (10 min)

**Tom:** Focado, dois prompts em sequência, explicando o que cada um faz

"Primeiro: os dados.

Na vida real, você já teria a planilha salva. Mas pra fins de demo,
vou pedir pro Claude gerar uma planilha simulada — e depois usar ela
como se fossem os dados reais do consultório.

Esse fluxo é idêntico se você usar dados próprios anonimizados.

Prompt 1 — gerar a planilha:

```
Gere uma planilha CSV simulada com 50 pacientes anonimizados
de um consultório de metabolologia.

Colunas:
- ID: P001 a P050
- Idade: entre 30 e 65 anos
- Sexo: M ou F (distribuição realista)
- Peso_kg: entre 80 e 140 kg
- Altura_cm: entre 155 e 185 cm
- IMC: calculado a partir do peso e altura
- HbA1c_pct: entre 5.5 e 11.0 (pacientes com risco metabólico)
- PHQ9_score: entre 0 e 27

Importante: gere uma correlação moderada positiva entre PHQ-9 e IMC,
e entre PHQ-9 e HbA1c — refletindo o que a literatura já aponta.

Salve em dados_pacientes.csv.
```

[executar e mostrar o arquivo gerado]

Ótimo. Temos 50 linhas, 8 colunas, tudo anonimizado — só ID e variáveis clínicas.
Sem nome, sem data de nascimento, sem CPF. LGPD OK.

Agora a análise:

```
Analise o arquivo dados_pacientes.csv e me gere:

1. Estatísticas descritivas de todas as variáveis numéricas:
   média, desvio-padrão, mínimo, máximo, mediana
2. Correlação de Pearson entre PHQ-9 e IMC (com valor-p)
3. Correlação de Pearson entre PHQ-9 e HbA1c (com valor-p)
4. Apresente tudo em tabela formatada, pronta para copiar no Word
```

[executar e mostrar resultado]

Olha o que saiu.

Temos as correlações, os valores-p, as estatísticas descritivas.
Se p < 0,05 — o achado é estatisticamente significativo.

Isso é o que vai para a seção de Resultados do pôster.

Guarda esses números na cabeça — a gente vai usá-los daqui a pouco."

---

## SEÇÃO 4: DEMO — GRÁFICOS PARA PUBLICAÇÃO (10 min)

**Tom:** Focado, mostrando a entrega visual — dois gráficos prontos

"Agora os gráficos.

Pôster de congresso sem gráfico não existe. E gráfico bem feito
conta a história dos dados melhor do que qualquer tabela.

Prompt:

```
Com base em dados_pacientes.csv, gere dois gráficos prontos para publicação científica:

GRÁFICO 1 — Scatter plot:
- Eixo X: IMC (kg/m²), Eixo Y: PHQ-9 score
- Adicione linha de tendência com regressão linear
- Mostre a equação da reta e o valor de R²
- Título: 'Correlação entre IMC e Escore PHQ-9'
- Legenda dos eixos em português
- Estilo: fundo branco, pontos em cinza-escuro, linha em preto
  (padrão de publicação científica — sem cores desnecessárias)

GRÁFICO 2 — Boxplot:
- Divida os pacientes em quartis de PHQ-9 (Q1, Q2, Q3, Q4)
- Eixo Y: HbA1c (%)
- Título: 'Distribuição de HbA1c por Quartil de PHQ-9'
- Mostre outliers como pontos individuais
- Mesmo estilo: preto e cinza, fundo branco

Salve como scatter_phq9_imc.png e boxplot_hba1c_phq9.png na pasta atual.
```

[executar e mostrar os dois gráficos gerados]

Veja o scatter: você consegue ver visualmente a tendência positiva —
quanto maior o IMC, maior o PHQ-9. A linha de tendência confirma.

O boxplot conta outra história: no Q4 — os mais deprimidos —
a HbA1c mediana é visivelmente mais alta do que no Q1.

São dois gráficos prontos para inserir direto no PowerPoint ou no Canva.

Perceba: o Claude escreveu o código Python internamente, rodou a análise
e entregou os arquivos. Você não viu uma linha de código.
Só os resultados.

Isso é o que eu chamo de estatística sem sofrimento."

---

## SEÇÃO 5: DEMO — TEXTO DO PÔSTER (12 min)

**Tom:** Metódico, ensinando a estrutura acadêmica e o prompt

"Agora vem a parte mais trabalhosa do pôster — o texto.

Introdução, objetivo, métodos, resultados, conclusão.
Em inglês ou português, dependendo do congresso.
Em ABNT ou Vancouver, dependendo da norma.

Vou gerar tudo em português, formato ABNT, para um congresso brasileiro.

Prompt:

```
Com base na análise que fizemos do arquivo dados_pacientes.csv,
escreva o texto completo de um pôster científico para submissão em
congresso brasileiro de endocrinologia e metabolismo.

Estrutura obrigatória:

1. TÍTULO
   Impactante e descritivo. Máx. 2 linhas.
   Exemplo de estrutura: 'Associação entre [variável A] e [variável B]
   em pacientes com [condição]: estudo transversal observacional'

2. AUTORES
   Dra. [Nome da Pesquisadora], Ambulatório de Metabolologia, [Cidade]

3. INTRODUÇÃO (3-4 frases)
   Contexto da tríade obesidade-inflamação-depressão.
   Lacuna na literatura que este estudo preenche.
   Justificativa clínica.

4. OBJETIVO
   Uma frase objetiva.

5. MÉTODOS
   Desenho do estudo (transversal observacional retrospectivo).
   População: n=50 pacientes com obesidade (IMC ≥30).
   Variáveis coletadas: IMC, HbA1c, PHQ-9.
   Análise estatística: estatísticas descritivas e correlação de Pearson.

6. RESULTADOS
   Inclua os valores REAIS que obtivemos: médias, desvios-padrão,
   correlações de Pearson e valores-p encontrados na análise.
   Mencione os dois gráficos gerados.

7. CONCLUSÃO (2-3 frases)
   O que os dados sugerem clinicamente.
   Limitações do estudo (cross-sectional, n pequeno).
   Perspectivas futuras.

8. REFERÊNCIAS
   3 referências reais e relevantes sobre a tríade obesidade-inflamação-depressão,
   no formato ABNT.

Tom: acadêmico e preciso. Sem especulação além do que os dados mostram.
```

[executar e mostrar resultado]

Olha o que saiu.

Título objetivo e descritivo.
Introdução com contexto e justificativa.
Métodos com o que você realmente fez.
Resultados com os números reais da análise.
Conclusão honesta — reconhece as limitações do estudo.
Três referências ABNT.

Isso é o corpo do pôster. Você copia para o template no Word ou no Canva,
insere os dois gráficos nas posições certas, ajusta o layout, e submete.

Uma observação importante: o Claude está gerando o texto com base nos dados simulados.
Se os seus dados reais mostrarem correlação diferente — ou não mostrarem correlação —
o texto muda. O Claude vai escrever o que os dados dizem, não o que você quer que eles digam.

Isso é pesquisa honesta."

---

## SEÇÃO 6: ENCERRAMENTO + DEVER DE CASA (4 min)

**Tom:** Motivador, resumo do fluxo completo, desafio concreto

"Resumo do que a gente fez hoje.

A metabologista saiu daqui com:
— Uma planilha de 50 pacientes anonimizados analisada estatisticamente
— Dois gráficos prontos para publicação: scatter e boxplot
— O texto completo do pôster no formato ABNT
— Tudo isso sem escrever uma linha de código e sem abrir o SPSS

O fluxo foi:
1. Gerar dados simulados — na vida real: usar os dados reais anonimizados
2. Análise descritiva + correlação de Pearson
3. Gráficos no padrão de publicação científica
4. Texto do pôster usando os resultados reais

Agora o dever de casa.

Pense em uma hipótese clínica que você tem no seu consultório.
Duas variáveis que você suspeita que estão correlacionadas.
E faça isso:

```
Gere uma planilha simulada com 30 pacientes da minha especialidade.
Colunas: [variáveis relevantes para o seu caso].
Analise e me mostre a correlação entre [variável A] e [variável B].
```

Não precisa submeter em congresso essa semana. Mas entenda o fluxo.
Porque quando você tiver dados reais — e você vai ter —
você já sabe o que fazer.

Na aula_07 a gente fecha o M3 com gestão do consultório:
indicadores de produção, faturamento por convênio, taxa de no-show.
Você vai sair com um dashboard de métricas do consultório funcionando.

Até lá."

---

**FIM DO ROTEIRO**
