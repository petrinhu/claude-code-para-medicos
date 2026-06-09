# Aula 23 — PHQ-9 + GAD-7 — Roteiro Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produzir `aula_23/roteiro.md` (~55 min, 8 seções) e `aula_23/roteiro.html` para o módulo S05.03 do curso Claude Code para Médicos.

**Architecture:** Roteiro narrativo no formato canônico do curso — seções numeradas, Tom, falas do professor entre aspas, blocos copiáveis. Spec aprovado em `docs/superpowers/specs/2026-06-09-aula23-design.md`.

**Tech Stack:** Markdown, pandoc (HTML), git.

---

## Arquivos

- **Criar:** `aula_23/roteiro.md`
- **Criar:** `aula_23/roteiro.html` (pandoc a partir do .md)
- **Modificar:** `TODO.md` (S05.03 ✅, contadores 33✅/20⏳)

---

### Task 1: Escrever `aula_23/roteiro.md`

**Files:**
- Create: `aula_23/roteiro.md`

- [ ] **Step 1: Criar pasta e arquivo**

```bash
mkdir -p aula_23
```

- [ ] **Step 2: Escrever roteiro completo**

Conteúdo completo conforme spec `docs/superpowers/specs/2026-06-09-aula23-design.md`:

```markdown
# Aula 23 — PHQ-9 e GAD-7: O Paradigma Likert

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~55 min  
**Tom:** Médico de família — prático, acolhedor, sabe que a paciente disse mais do que parecia  
**Módulo:** S05.03 — Calculadoras Médicas  
**Persona:** Médico de família / clínico geral  

---

## SEÇÃO 1: ABERTURA + PARADIGMA LIKERT — 5 min

**Tom:** Narrativo — a frase que muda a consulta

"Tô meio triste, doutor."

Ela disse de passagem.
No final da consulta.
Enquanto você ainda estava digitando o ajuste da insulina.

Paciente de 45 anos.
Consulta de rotina para diabetes.
Sem queixa principal de humor.
Mas essa frase ficou no ar.

---

Você sabe o que ela quis dizer.
Todo médico de família sabe.

O problema é que 'meio triste' não entra em prontuário.
Não tem CID.
Não tem conduta automática.

O PHQ-9 existe para transformar essa frase em dado.

---

Nas últimas duas aulas, você trabalhou com calculadoras binárias.
Hipertenso ou não.
AVC prévio ou não.
Checkboxes — sim ou não.

Hoje o paradigma muda.

Não é mais 'tem ou não tem'.
É 'com que frequência'.

---

Você já viu isso antes — só não chamava de Likert.

Pense na EVA de dor.
Quando você pergunta 'de zero a dez, qual é a sua dor?',
você não está perguntando se o paciente tem dor.
Você está perguntando com que intensidade.

O PHQ-9 faz o mesmo com humor — mas com frequência.

Quatro opções para cada item:

- 0 = Nunca
- 1 = Alguns dias
- 2 = Mais da metade dos dias
- 3 = Quase todo dia

Cada item tem um peso.
A soma decide a faixa.

Esse é o paradigma Likert.
Vai aparecer em dezenas de calculadoras que você vai implementar.
Hoje você aprende o padrão uma vez."

---

## SEÇÃO 2: PHQ-9 COMO ESPECIFICAÇÃO — 8 min

**Tom:** Clínico e técnico — transformar o instrumento em dado antes de escrever o prompt

"Você já sabe o score. Vamos transformar o que você sabe em especificação."

---

[mostrar na tela]

PHQ-9 — Patient Health Questionnaire.
Rastreio de depressão.
Frequência nos últimos 14 dias.

Nove itens:

| # | Critério | Campo |
|---|---|---|
| 1 | Pouco interesse ou prazer em fazer as coisas | interesse |
| 2 | Sentir-se deprimido(a), sem esperança | deprimido |
| 3 | Dificuldade para adormecer, manter sono ou dormir demais | sono |
| 4 | Sentir-se cansado(a) ou com pouca energia | energia |
| 5 | Falta de apetite ou comer em excesso | apetite |
| 6 | Sentir-se mal consigo mesmo(a) / fracasso / decepção | autoestima |
| 7 | Dificuldade de concentração | concentracao |
| 8 | Lentidão ou agitação percebida pelos outros | agitacao |
| **9** | **Pensamentos de se machucar ou de que seria melhor estar morto** | **item_9** |

Cada item: 0, 1, 2 ou 3.
Score total: 0 a 27.

---

"Cinco faixas:

| Score | Faixa |
|---|---|
| 0 a 4 | Mínimo |
| 5 a 9 | Leve |
| 10 a 14 | Moderado |
| 15 a 19 | Moderadamente grave |
| 20 a 27 | Grave |

Cutoff de ação clínica: 10.
Abaixo de 10 — monitorar.
A partir de 10 — intervir.

---

[pausar]

Mas antes de continuar.

O item 9 é diferente.

Leia de novo:
'Pensamentos de se machucar ou de que seria melhor estar morto.'

Esse item não é mais um critério a somar.
Ele é uma pergunta à parte.

Qualquer resposta acima de zero — mesmo 'alguns dias' —
muda a conduta imediatamente.
Independente do score total.

Um paciente com score 3 e item 9 igual a 1
não é 'Mínimo'.
É risco a avaliar agora.

O alerta de suicídio existe fora da faixa.
O app vai implementar isso como método separado.

---

Agora: nosso caso âncora.

Paciente de 45 anos, mulher.
Consulta de rotina para DM.
'Tô meio triste, doutor.'

Você aplica o PHQ-9.

Respostas:

- Pouco interesse: 1
- Deprimida: 1
- Sono: 2
- Energia: 2
- Concentração: 1
- Todos os outros: 0
- Item 9: 0

[calcular ao vivo]

1 + 1 + 2 + 2 + 1 = **7**

Score 7 → Leve.
Item 9 = 0 → sem alerta.

Esse é o gabarito.
O app vai ter que bater esse número."

---

## SEÇÃO 3: PROMPT PHQ-9 — 7 min

**Tom:** Professor conduz — lê cada parte em voz alta, pausa no item_9 e no alerta_suicidio()

"Na aula_21 e na aula_22, você aprendeu o padrão.
Hoje ele aparece com uma diferença nova:
em vez de campos booleanos, campos inteiros.
E um método que não depende da soma."

---

[digitar no terminal — ler cada parte em voz alta]

```
Implemente a calculadora PHQ-9 no ClinMd-Tribe
respeitando a Clean Architecture das 4 camadas:

domain/calculadoras/phq9.py
  - Classe Phq9 com 9 campos inteiros (0 a 3):
    interesse, deprimido, sono, energia, apetite,
    autoestima, concentracao, agitacao, item_9
  - Método calcular() → retorna score inteiro 0-27
  - Método interpretar(score) → str
    - 0 a 4: "Mínimo"
    - 5 a 9: "Leve"
    - 10 a 14: "Moderado"
    - 15 a 19: "Moderadamente grave"
    - 20 a 27: "Grave"
  - Método alerta_suicidio() → bool
    - Retorna True se item_9 >= 1
    - Independente do score total

application/servicos/calculadora_service.py
  - Adicionar função calcular_phq9(dados: dict) → dict
    Retorna: {"score": int, "faixa": str, "alerta_suicidio": bool}

presentation/telas/calculadora_phq9.py
  - Tela Flet com:
    - 9 dropdowns, cada um com opções:
      0 = Nunca
      1 = Alguns dias
      2 = Mais da metade dos dias
      3 = Quase todo dia
    - Botão "Calcular PHQ-9"
    - Exibir score em destaque
    - Exibir faixa com cor:
      Mínimo/Leve: verde · Moderado: amarelo
      Moderadamente grave/Grave: vermelho
    - Se alerta_suicidio = True:
      Exibir caixa vermelha em destaque:
      "⚠ Avaliar risco de suicídio imediatamente"
      (independente do score total)
```

---

[pausar antes de enviar]

"Perceba três diferenças em relação às aulas anteriores.

Primeiro: os campos não são booleanos.
São inteiros — de 0 a 3.

Segundo: a tela usa dropdowns, não checkboxes.
Porque a resposta não é sim ou não — é uma frequência.

Terceiro: `alerta_suicidio()` é um método separado.
Não faz parte de `interpretar()`.
Não depende do score.
Depende apenas do item_9.

Essa separação é a decisão clínica mais importante deste prompt."

---

[enviar o prompt ao Claude Code]

---

## SEÇÃO 4: CLAUDE IMPLEMENTA + LEITURA SUPERVISIONADA — 12 min

**Tom:** Aguardar + auditar — cinco perguntas clínicas em ritmo pausado

[aguardar o Claude Code processar]

[mostrar na tela os arquivos sendo criados e modificados]

"Dois arquivos novos.
Um modificado.

`domain/calculadoras/phq9.py` — criado.
`presentation/telas/calculadora_phq9.py` — criado.
`application/servicos/calculadora_service.py` — modificado, função adicionada.

Agora você lê antes de rodar."

---

**Pergunta 1:**

"Abra `domain/calculadoras/phq9.py`.

Cada campo aceita valores de 0 a 3 — não é booleano?

Você está procurando campos declarados como inteiros.
Se aparecerem como bool, a calculadora está errada.

[mostrar o código]

Correto — inteiros, não booleanos."

---

**Pergunta 2:**

"A soma máxima é 27 — nove campos vezes três?

Procure o método `calcular()`.
Ele deve somar os nove campos.
Se algum campo estiver faltando na soma, o score vai ser menor do que deveria.

[mostrar o método]

Correto — nove campos somados, máximo 27."

---

**Pergunta 3:**

"O cutoff de Moderado começa em 10, não em 9?

Procure o método `interpretar()`.
A faixa Leve vai até 9.
A faixa Moderado começa em 10.

Se o limite estiver em 9, a faixa está deslocada — um ponto de diferença na conduta.

[mostrar as condições]

Correto — Leve encerra em 9, Moderado começa em 10."

---

**Pergunta 4:** ← crítica

"O método `alerta_suicidio()` existe e verifica `item_9 >= 1` separado do score total?

Essa é a pergunta mais importante.

Procure um método chamado `alerta_suicidio` — separado de `calcular` e de `interpretar`.
Ele deve olhar apenas para `item_9`.
Não deve depender do score total.

Se não existir como método separado — o app está errado e não pode ser usado.

[mostrar o método]

Está lá. Separado. Independente do score. Correto."

---

**Pergunta 5:**

"A tela chama o serviço — não calcula direto?

Abra `presentation/telas/calculadora_phq9.py`.

Quando o botão 'Calcular PHQ-9' é clicado,
o código deve chamar `calcular_phq9` do `calculadora_service`.
Não deve fazer a soma diretamente na tela.

[mostrar a chamada ao serviço]

Está chamando o serviço. A arquitetura está respeitada.

---

Cinco perguntas. Cinco confirmações.

Você pode assinar."

---

**Frase-âncora:**

"O item 9 não é mais um critério.
Ele é uma pergunta à parte.
Qualquer resposta acima de zero muda a conduta —
independente do score total."

---

## SEÇÃO 5: APP AO VIVO PHQ-9 + VALIDAÇÃO — 7 min

**Tom:** Payoff — dois casos: leve sem alerta e grave com alerta simultâneos

[no terminal]

```
uv run python main.py
```

[aguardar o Flet abrir no browser]

---

**Caso 1 — âncora (score 7, Leve, sem alerta):**

"Aqui está a tela do PHQ-9.

Nove dropdowns.
Um botão.

Vamos preencher o caso da nossa paciente.

[selecionar nos dropdowns]

- Pouco interesse: 1 = Alguns dias
- Deprimida: 1 = Alguns dias
- Sono: 2 = Mais da metade dos dias
- Energia: 2 = Mais da metade dos dias
- Apetite: 0 = Nunca
- Autoestima: 0 = Nunca
- Concentração: 1 = Alguns dias
- Agitação: 0 = Nunca
- Item 9: 0 = Nunca

[clicar Calcular PHQ-9]

Score: 7.
Faixa: Leve — em verde.
Sem alerta.

Bateu o gabarito."

---

**Caso 2 — grave (score 20, Grave, alerta ativo):**

"Agora o caso mais importante desta aula.

Paciente de 58 anos, homem.
Isolamento há dois meses.
Anedonia completa.
Queixas em quase todos os itens.

[preencher nos dropdowns]

- Pouco interesse: 3 = Quase todo dia
- Deprimido: 3 = Quase todo dia
- Sono: 3 = Quase todo dia
- Energia: 3 = Quase todo dia
- Apetite: 2 = Mais da metade dos dias
- Autoestima: 2 = Mais da metade dos dias
- Concentração: 2 = Mais da metade dos dias
- Agitação: 1 = Alguns dias
- Item 9: 1 = Alguns dias

[clicar Calcular PHQ-9]

[mostrar na tela]

Score: 20.
Faixa: Grave — em vermelho.

E abaixo do score:

⚠ Avaliar risco de suicídio imediatamente.

---

Dois resultados na tela ao mesmo tempo.

A faixa Grave diz o que o score significa.
A caixa vermelha diz o que fazer agora —
independente do score.

Isso é o que diferencia o item 9 de todos os outros.

Não é mais um critério.
É uma pergunta à parte.

Qualquer resposta acima de zero — a conduta muda."

---

## SEÇÃO 6: GAD-7 — TRANSFERÊNCIA DELIBERADA — 8 min

**Tom:** Professor recua — é a vez do aluno escrever o prompt

"Agora é sua vez.

O GAD-7 tem a mesma estrutura do PHQ-9.
Sete itens.
Escala 0-3.
Lógica Likert.

A diferença:
- 7 itens, não 9
- Score máximo: 21, não 27
- Quatro faixas, não cinco
- Sem item equivalente ao item 9

Você vai adaptar o prompt do PHQ-9.
Não vou escrever por você.

---

O que muda:

- Nome da classe: `Gad7`
- Arquivo: `domain/calculadoras/gad7.py`
- 7 campos inteiros (0 a 3):
  nervoso, preocupacao_incontrolavel, preocupacao_excessiva,
  relaxar, inquietacao, irritabilidade, medo
- `calcular()` → score inteiro 0-21
- `interpretar(score)`:
  - 0 a 4: 'Mínimo'
  - 5 a 9: 'Leve'
  - 10 a 14: 'Moderado'
  - 15 a 21: 'Grave'
- Função no service: `calcular_gad7(dados: dict) → {"score": int, "faixa": str}`
- Tela: `presentation/telas/calculadora_gad7.py`
  - 7 dropdowns (mesmas opções: Nunca / Alguns dias / Mais da metade / Quase todo dia)
  - Faixa colorida: Mínimo/Leve verde · Moderado amarelo · Grave vermelho
  - Sem caixa de alerta especial
- Sem método `alerta_suicidio`

---

Adapte o prompt.
Digite no terminal.

[aguardar o aluno escrever — professor não intervém a não ser que haja erro estrutural,
como esquecer as 4 faixas ou usar 5 campos em vez de 7]"

---

[aguardar o Claude processar o prompt do aluno]

[mostrar os arquivos gerados]

---

"**Pergunta-relâmpago:**

Quantas faixas o Claude gerou?
Bate com 4?

[mostrar o método `interpretar()` do GAD-7]

Quatro faixas: Mínimo, Leve, Moderado, Grave.
Correto.

Você escreveu o prompt.
Você verificou o resultado.
Essa é a transferência."

---

## SEÇÃO 7: APP AO VIVO GAD-7 — 4 min

**Tom:** Rápido — confirmar que a transferência funcionou com o caso 3

"[navegar para a tela GAD-7]

Caso clínico: 32 anos, masculino.
Queixa de ansiedade e palpitações.

[selecionar nos dropdowns]

- Nervoso: 2 = Mais da metade dos dias
- Preocupação incontrolável: 2 = Mais da metade dos dias
- Preocupação excessiva: 2 = Mais da metade dos dias
- Dificuldade de relaxar: 2 = Mais da metade dos dias
- Inquietação: 1 = Alguns dias
- Irritabilidade: 1 = Alguns dias
- Medo: 1 = Alguns dias

[clicar Calcular GAD-7]

4 × 2 + 3 × 1 = 8 + 3 = 11.
Faixa: Moderado.

Transferência confirmada.

O padrão que você aprendeu com o PHQ-9
funcionou quando você usou sozinho no GAD-7."

---

## SEÇÃO 8: ENCERRAMENTO + DEVER — 4 min

**Tom:** Consolidar + bridge S05.04

"Resumo do que ficou pronto hoje.

O paradigma Likert — escala 0-3, frequência, não presença.
O PHQ-9: nove itens, cinco faixas, cutoff em 10.
O item 9: pergunta à parte, alerta independente do score.
O GAD-7: você escreveu o prompt. Funcionou.

O ClinMd-Tribe agora tem quatro calculadoras.
Duas binárias. Duas Likert.
E você conhece os dois padrões.

---

Dever de casa.

Abra o ClinMd-Tribe.
Pense num paciente que se queixou de tristeza, ansiedade ou fadiga.

Des-identifica antes de digitar qualquer coisa.
Nome: Paciente 001.
CPF, data de nascimento, endereço: apaga.
Mantém só: sexo, faixa etária, as respostas aos itens.

Calcule o PHQ-9 e o GAD-7.
Compare os dois scores com a sua impressão clínica.

Se o item 9 for maior que zero:
anota que o alerta apareceu.
Registra a conduta que você tomou.

---

Na próxima aula: o padrão continua — mas com variações.

HAM-D e YMRS são escalas Likert com estrutura diferente.
AUDIT e CAGE voltam ao padrão booleano.

Você já conhece os dois padrões.
Na aula_24, você vai identificar qual é qual antes de escrever o prompt.

Até lá."

---

**FIM DO ROTEIRO**
```

- [ ] **Step 3: Verificar spec coverage (self-review inline)**

Checklist contra `docs/superpowers/specs/2026-06-09-aula23-design.md`:

| Item de spec | Presente no roteiro? |
|---|---|
| Abertura "Tô meio triste doutor" | ✅ S1 |
| Analogia EVA de dor | ✅ S1 |
| Escala 0=Nunca / 3=Quase todo dia | ✅ S1 |
| Tabela 9 itens com nomes de campo | ✅ S2 |
| 5 faixas com scores | ✅ S2 |
| Cutoff ação clínica = 10 | ✅ S2 |
| Pausa no item 9 + explicação "pergunta à parte" | ✅ S2 |
| Cálculo caso âncora ao vivo → 7 Leve | ✅ S2 |
| Prompt PHQ-9 completo copiável | ✅ S3 |
| 3 diferenças booleano→Likert explicadas | ✅ S3 |
| Claude gera 3 arquivos | ✅ S4 |
| 5 perguntas leitura supervisionada | ✅ S4 (P1–P5) |
| Pergunta 4 marcada como crítica | ✅ S4 |
| Frase-âncora item 9 | ✅ S4 |
| Caso 1 âncora score 7 Leve sem alerta | ✅ S5 |
| Caso 2 grave score 20 + alerta ativo simultâneo | ✅ S5 |
| Instrução transferência GAD-7 | ✅ S6 |
| 7 campos GAD-7 listados | ✅ S6 |
| 4 faixas GAD-7 sem item especial | ✅ S6 |
| Pergunta-relâmpago "quantas faixas?" | ✅ S6 |
| Caso 3 GAD-7 score 11 Moderado | ✅ S7 |
| Valores individuais caso 3 explicitados | ✅ S7 |
| Dever de casa + des-identificação + item 9 | ✅ S8 |
| Bridge aula_24 HAM-D/YMRS/AUDIT/CAGE | ✅ S8 |

---

### Task 2: Gerar `aula_23/roteiro.html`

**Files:**
- Create: `aula_23/roteiro.html`

- [ ] **Step 1: Gerar HTML com pandoc**

```bash
pandoc aula_23/roteiro.md -o aula_23/roteiro.html --standalone --metadata title="Aula 23 — PHQ-9 e GAD-7: O Paradigma Likert"
```

Expected: arquivo `aula_23/roteiro.html` criado sem erros.

---

### Task 3: Commit + atualizar TODO.md

**Files:**
- Modify: `TODO.md`

- [ ] **Step 1: Commit dos arquivos da aula_23**

```bash
git add aula_23/
git commit -m "feat: aula_23 roteiro.md + roteiro.html — PHQ-9 + GAD-7 paradigma Likert"
```

- [ ] **Step 2: Atualizar TODO.md**

Mover S05.03 de ⏳ para ✅ e atualizar contadores para 33✅/20⏳.

- [ ] **Step 3: Commit TODO.md**

```bash
git add TODO.md
git commit -m "chore: TODO.md — S05.03 ✅, contadores 33✅/20⏳"
```
