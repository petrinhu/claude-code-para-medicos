# Aula 26 — Dashboard Financeiro: KPIs e Gráficos

**Formato:** Gravada no OBS Studio, editada no Kdenlive
**Duração:** ~48 min
**Tom:** Ortopedista que já tem os dados e agora quer ler a curva
**Módulo:** S06.02 — Dashboard Financeiro

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Já preparado em `resources/` (é só usar):**

- [ ] `resources/dados_6_meses_bastidor.csv` : os seis meses fictícios do ortopedista (março a agosto de 2025). Use como cola para cadastrar os meses ANTES de gravar (esta aula começa com o banco já cheio).
- [ ] `resources/gabarito_kpis_bastidor.csv` : o gabarito dos KPIs (receita líquida, taxa de glosa, ticket médio) mês a mês. Confira contra a tela na Seção 5 e 6: agosto deve dar líquida R$ 22.400, glosa 18,5%, ticket R$ 246,15.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] App com o módulo financeiro da aula_25 funcionando (formulário + tabela + banco em `data/clinmd.db`).
- [ ] Banco `data/clinmd.db` JÁ POPULADO com os SEIS meses (março a agosto), não só os três da aula_25. Cadastre março, abril e maio pelo formulário antes de gravar, usando a cola `dados_6_meses_bastidor.csv`.

**Confira antes de gravar:**

- [ ] `uv run python main.py` abre o app e o formulário da aula_25 lista os seis meses na tabela.
- [ ] Os seis meses na tabela batem com a cola (março 32000/3200/112 ... agosto 27500/5100/91).
- [ ] Você consegue calcular os KPIs de agosto na cabeça/calculadora na Seção 2 e bater com o gabarito (líquida 22.400; glosa 18,5%; ticket 246,15).

**Navegador:** nenhum site é necessário nesta aula. O navegador só abre para exibir o dashboard Flet (via `uv run python main.py`).

---

## SEÇÃO 1: ABERTURA — 4 min

**Tom:** Retrieval — puxar o que foi feito na aula_25 antes de avançar

**[Aviso rápido dos óculos, antes de mergulhar]**

"Recadinho de sempre: hoje a gente vai ler gráfico e número pequeno na tela, e eixo de gráfico não perdoa vista cansada. Coloca os óculos de perto, ajusta o foco, que a curva de hoje merece ser vista nítida."

"Na aula passada você construiu a memória do consultório.

O app salva. O app lembra. O arquivo mora em `data/clinmd.db`.

E desde então a memória encheu: agora são seis meses de dados, março a agosto de 2025, todos cadastrados pelo mesmo formulário.

Mas agora você tem uma tabela de números.

| Mês | Receita bruta | Glosas | Consultas |
|---|---|---|---|
| Março | R$ 32.000 | R$ 3.200 | 112 |
| Abril | R$ 30.500 | R$ 3.660 | 105 |
| Maio | R$ 34.000 | R$ 3.400 | 118 |
| Junho | R$ 28.000 | R$ 4.200 | 95 |
| Julho | R$ 31.000 | R$ 3.800 | 108 |
| Agosto | R$ 27.500 | R$ 5.100 | 91 |

Você consegue ver a tendência olhando para esses números?

---

Talvez sim. Talvez não.

Na medicina você não olha um exame isolado.
Você olha a curva de evolução.

HbA1c de 8,2% não diz nada sozinha.
HbA1c de 9,1 → 8,7 → 8,2 diz que o paciente está respondendo.

Receita do consultório é a mesma leitura.
Agosto não diz nada sozinho.
Agosto dentro de uma curva de seis meses diz tudo.

Hoje os números viram gráfico."

---

## SEÇÃO 2: KPIS COMO ESPECIFICAÇÃO — 6 min

**Tom:** Clínico e técnico — transformar receita e glosa em indicadores antes de escrever o prompt

"Três KPIs.

O primeiro você já conhece: receita líquida.

```
receita_liquida = receita_bruta - glosas
```

O que sobra depois que o convênio devolveu.

---

O segundo: taxa de glosa.

```
taxa_glosa = glosas / receita_bruta
```

Qual porcentagem da receita bruta foi negada.

Um consultório com 10% de glosa está no controle.
Com 15%, está no limite.
Com 18%, tem um problema.

---

O terceiro: ticket médio.

```
ticket_medio = receita_liquida / n_consultas
```

Quanto cada consulta efetivamente trouxe, depois das glosas.
O rendimento por atendimento.

---

Agora o cálculo de agosto.

[calcular ao vivo]

Receita líquida = 27.500 - 5.100 = **R$ 22.400**
Taxa de glosa = 5.100 / 27.500 = **18,5%**
Ticket médio = 22.400 / 91 = **R$ 246,15**

Taxa de glosa 18,5%.
Acima de 15%.
Agosto vai aparecer em vermelho no dashboard.

Esse é o gabarito.
O app vai ter que bater esses números."

---

## SEÇÃO 3: PROMPT DASHBOARD — 5 min

**Tom:** Professor conduz — destaque para guard de divisão por zero e gráficos nativos do Flet

"Dois destaques antes de digitar.

Primeiro: divisão por zero.

Se o médico cadastrar um mês de férias — receita zero, consultas zero —
o cálculo de taxa de glosa vai tentar dividir por zero.
O app quebra.

O prompt precisa pedir que o Claude proteja os dois cálculos:
se receita_bruta for zero, taxa_glosa é zero.
Se n_consultas for zero, ticket_medio é zero.

Segundo: gráficos nativos do Flet.

Flet tem `ft.BarChart` e `ft.LineChart` nativos.
Você não precisa instalar matplotlib nem nenhuma outra biblioteca.
Os gráficos ficam dentro do app — não são imagens externas."

---

[digitar no terminal — ler cada parte em voz alta]

```
Implemente o dashboard financeiro do ClinMd-Tribe:

domain/financeiro/registro_mensal.py
  - Adicionar método calcular_kpis() -> dict
    receita_liquida = receita_bruta - glosas
    taxa_glosa = glosas / receita_bruta (se receita_bruta > 0, senão 0.0)
    ticket_medio = receita_liquida / n_consultas (se n_consultas > 0, senão 0.0)

application/servicos/financeiro_service.py
  - Adicionar calcular_kpis_periodo(registros: list[dict]) -> list[dict]
    Retorna cada registro com os KPIs calculados adicionados

presentation/telas/dashboard_financeiro.py
  - 3 cards KPI (valores do último mês registrado):
    Receita Líquida (R$) | Taxa de Glosa (%) | Ticket Médio (R$)
  - Card de Taxa de Glosa: fundo vermelho se taxa_glosa > 0.15
  - ft.BarChart: receita líquida dos últimos 12 meses
    (eixo x = mês/ano, eixo y = R$)
  - ft.LineChart: taxa de glosa (%) dos últimos 12 meses
    (linha vermelha tracejada acima de 15%)
```

---

[enviar o prompt ao Claude Code]

---

## SEÇÃO 4: CLAUDE IMPLEMENTA + LEITURA SUPERVISIONADA — 10 min

**Tom:** Aguardar + auditar — três perguntas, primeira é crítica

[aguardar o Claude Code processar]

[mostrar na tela os arquivos sendo criados e modificados]

"Um arquivo novo.
Dois modificados.

`presentation/telas/dashboard_financeiro.py` — criado.
`domain/financeiro/registro_mensal.py` — modificado.
`application/servicos/financeiro_service.py` — modificado.

Três perguntas."

---

**Pergunta 1:** ← crítica

"Abra `domain/financeiro/registro_mensal.py`.

O método `calcular_kpis()` tem guard para divisão por zero?

Você está procurando as duas condições:

```python
taxa_glosa = self.glosas / self.receita_bruta if self.receita_bruta > 0 else 0.0
ticket_medio = receita_liquida / self.n_consultas if self.n_consultas > 0 else 0.0
```

Se o `if` não estiver lá, um mês de férias quebra o app.

[mostrar o método]

Correto — ambos os guards presentes."

---

**Pergunta 2:**

"O BarChart mostra receita líquida — não receita bruta?

Procure onde o BarChart recebe os dados.
Deve estar usando `receita_liquida` — não `receita_bruta`.

A diferença: receita bruta inclui as glosas.
Receita líquida é o que o médico efetivamente recebeu.
O gráfico deve mostrar o que entrou, não o que foi cobrado.

[mostrar o dado que alimenta o BarChart]

Correto — usando receita líquida."

---

**Pergunta 3:**

"A cor de alerta do card de taxa de glosa está na tela — não no domínio?

Abra `presentation/telas/dashboard_financeiro.py`.

O código que muda a cor do card para vermelho quando taxa_glosa > 15% deve estar aqui.

Não no `calcular_kpis()`.
Não no serviço.

Por quê? Porque a cor é uma decisão de exibição — não uma regra clínica.
O domínio calcula o valor. A tela decide como mostrar.

[confirmar onde está a lógica de cor]

Correto — na tela."

---

**Frase-âncora:**

"Você não olha um exame isolado.
Você olha a curva.

Receita mês a mês é o mesmo raciocínio que acompanhar HbA1c ao longo do tempo."

---

## SEÇÃO 5: APP AO VIVO — BARCHART E LINECHART — 6 min

**Tom:** Payoff visual — os dados de seis meses viram curva

[no terminal — o app já está rodando com os dados dos seis meses pré-carregados]

[navegar para a tela do dashboard]

---

"Aqui está o dashboard.

Três cards no topo.

[mostrar os cards do último mês — agosto]

Receita Líquida: R$ 22.400
Taxa de Glosa: 18,5%
Ticket Médio: R$ 246,15

O card de Taxa de Glosa está em vermelho.
Acima de 15%.

---

Abaixo dos cards: o BarChart.

[mostrar o gráfico de barras]

Seis barras. Março a agosto.
Eixo x: mês e ano.
Eixo y: receita líquida em reais.

Maio foi o melhor mês: R$ 30.600 líquidos.
Agosto foi o pior: R$ 22.400.

Você já via isso na tabela — mas agora você vê de uma vez.

---

E abaixo: o LineChart da taxa de glosa.

[mostrar o gráfico de linha]

Linha subindo.
Março: 10%.
Abril: 12%.
Junho: 15%.
Agosto: 18,5%.

Não é coincidência.
É tendência.

Agosto não é um mês ruim.
É o último ponto de uma curva que está subindo há quatro meses.

---

Isso é o que os dados dizem.
O app calculou.
O médico decide o que fazer."

---

## SEÇÃO 6: CARD DE ALERTA — AGOSTO EM VERMELHO — 4 min

**Tom:** Payoff clínico — o alerta visual serve o raciocínio médico

"Olhe para o card de Taxa de Glosa.

Vermelho.

Não porque o app acha que agosto foi ruim.
Porque você definiu que acima de 15% o consultório precisa de atenção.

O app não decide nada.
Ele mostra o que os dados dizem, na cor que você pediu.

---

Qual plano está glosando mais?

O app não sabe — você não cadastrou essa informação.
É o próximo passo, quando você quiser ir além.

Por enquanto, o app fez a pergunta mais importante:
'O problema está crescendo?'

E a resposta está na curva.

Sim. Está crescendo.

Agora é decisão clínica — conversar com o convênio, revisar os laudos, contratar auditoria.

O app não resolve.
O app informa.
Você resolve."

---

## SEÇÃO 7: ENCERRAMENTO + BRIDGE S07 — 4 min

**Tom:** Fechamento do módulo S06 + abertura do S07 com curiosidade

"Vamos fechar o módulo S06.

O ClinMd-Tribe agora tem dois módulos funcionando.

O módulo de calculadoras: seis instrumentos clínicos.
O módulo financeiro: memória + curva do consultório.

---

O que você aprendeu neste módulo:

Persistência.
O dado mora num arquivo. O arquivo sobrevive ao fechar o app.
O banco fica em `data/`. Nunca vai ao Git. Nunca sobe pra nuvem.

KPIs.
Receita líquida. Taxa de glosa. Ticket médio.
Calculados no domínio. Exibidos na tela. Cada um no lugar certo.

Gráficos nativos.
BarChart para volume. LineChart para tendência.
Sem biblioteca extra. Dentro do Flet.

---

Na próxima aula: memória clínica.

O módulo financeiro guarda números do consultório.
O próximo módulo vai guardar conhecimento médico.

RAG — Retrieval-Augmented Generation.

Você vai indexar PDFs: guidelines, artigos, protocolos.
E o app vai responder perguntas clínicas com base nesses documentos.

Não na internet. Nos seus documentos. Na sua máquina.

O ClinMd-Tribe vai começar a falar como você.

Até lá."

---

**FIM DO ROTEIRO**
