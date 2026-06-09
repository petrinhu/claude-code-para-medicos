# Aula 24 — MELD + MMSE: Fórmula e Subtestes

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~58 min  
**Tom:** Dois especialistas — hepatologista diante de um fígado que está falhando; geriatra diante de uma memória que está partindo  
**Módulo:** S05.04 — Calculadoras Médicas  
**Personas:** Hepatologista (MELD) + Geriatra (MMSE)  

---

## SEÇÃO 1: ABERTURA — 3 min

**Tom:** Retrospectivo e provocativo — dois paradigmas, dois saltos

"Nas últimas três aulas você implementou quatro calculadoras.

Todas elas somavam coisas.
Binárias ou Likert — no final, sempre uma soma.

Hoje são dois padrões genuinamente novos.

O MELD não soma.
O MELD calcula.

Fórmula contínua.
Três variáveis laboratoriais.
Logaritmos.
O resultado não é uma soma de checkboxes —
é um número que o seu software vai calcular com `math.log`.

O MMSE também é diferente do que você viu.
Não são itens com o mesmo peso.
São subtestes — cada um com um teto próprio.
Orientação temporal vai de zero a cinco.
Linguagem e praxia vai de zero a nove.

---

Dois arcos hoje.

Primeiro: o hepatologista e o MELD.
Depois: a geriatra e o MMSE.

Cada arco é completo — prompt, leitura, validação.

Ao final, você terá seis calculadoras funcionando
e vai conhecer os três paradigmas do módulo S05:
booleano, Likert e fórmula contínua com subtestes."

---

## SEÇÃO 2: MELD COMO ESPECIFICAÇÃO — 7 min

**Tom:** Clínico e técnico — transformar a fórmula em dado antes de escrever o prompt

"Hepatologista.

Paciente de 58 anos, homem.
Cirrose alcoólica.
Internado por descompensação aguda.
Você precisa priorizar na lista de transplante.

O instrumento é o MELD — Model for End-Stage Liver Disease.

Não é uma escala clínica.
É uma fórmula matemática."

---

[mostrar na tela]

**Fórmula MELD:**

```
MELD = 3,78 × ln(bilirrubina) + 11,2 × ln(INR) + 9,57 × ln(creatinina) + 6,43
```

Três variáveis laboratoriais.
Três logaritmos naturais.
O resultado é arredondado para o inteiro mais próximo.

| Campo | Tipo | Restrição clínica |
|---|---|---|
| Bilirrubina (mg/dL) | número decimal | mínimo 1,0 |
| INR | número decimal | mínimo 1,0 |
| Creatinina (mg/dL) | número decimal | mínimo 1,0 |

---

"Por que mínimo 1,0?

Logaritmo de um número menor que 1 é negativo.
Um paciente com bilirrubina de 0,8 não tem bilirrubina anormalmente baixa —
ela está dentro do normal.
A convenção do MELD diz: se o valor for menor que 1,0, usar 1,0.
Isso garante que o logaritmo não produza um score negativo sem sentido clínico.

Essa regra não é da tela.
É do domínio — faz parte da definição do score.
Vamos ver isso de perto quando o Claude implementar."

---

[mostrar na tela]

**Faixas de mortalidade em 90 dias:**

| Score MELD | Mortalidade em 90 dias |
|---|---|
| < 10 | 3,7% |
| 10 a 19 | 6,0% |
| 20 a 29 | 19,6% |
| 30 a 39 | 52,6% |
| ≥ 40 | 71,3% |

---

"Agora o caso âncora.

Bilirrubina: 4,5.
INR: 1,8.
Creatinina: 1,2.

Todos os valores são maiores que 1,0 — a convenção não entra em ação.

[calcular ao vivo]

3,78 × ln(4,5) = 3,78 × 1,504 = **5,685**
11,2 × ln(1,8) = 11,2 × 0,588 = **6,583**
9,57 × ln(1,2) = 9,57 × 0,182 = **1,745**

Somando com 6,43:

5,685 + 6,583 + 1,745 + 6,43 = **20,44 → arredonda para 20**

Score 20 → Mortalidade em 90 dias: 19,6%.

Esse é o gabarito.
O app vai ter que bater esse número."

---

## SEÇÃO 3: PROMPT MELD — 6 min

**Tom:** Professor conduz — lê cada parte em voz alta, pausa nos três destaques: float, min=1.0, math.log

"Vamos escrever o prompt.

Três destaques antes de digitar.

Primeiro: os campos são `float`, não `int`.
Bilirrubina pode ser 4,5 ou 1,2 — não são inteiros.

Segundo: `min=1.0` mora no domínio.
Não na tela.
A regra clínica está dentro da classe — a tela não precisa saber disso.

Terceiro: `math.log` — logaritmo natural.
Não `math.log10`.
São funções diferentes.
O Python tem as duas — você vai especificar qual usar."

---

[digitar no terminal — ler cada parte em voz alta]

```
Implemente a calculadora MELD no ClinMd-Tribe
respeitando a Clean Architecture das 4 camadas:

domain/calculadoras/meld.py
  - Classe Meld com 3 campos float:
    bilirrubina_mg_dl, inr, creatinina_mg_dl
  - Método calcular() → score inteiro
    Fórmula: round(3.78*ln(bili) + 11.2*ln(INR) + 9.57*ln(crea) + 6.43)
    Antes de calcular: aplicar min=1.0 em cada campo
    (ex: bilirrubina_efetiva = max(bilirrubina_mg_dl, 1.0))
    Usar math.log (logaritmo natural)
  - Método interpretar(score) → str com faixa + mortalidade
    - score < 10:  "Mortalidade em 90 dias: 3.7%"
    - 10 a 19:     "Mortalidade em 90 dias: 6.0%"
    - 20 a 29:     "Mortalidade em 90 dias: 19.6%"
    - 30 a 39:     "Mortalidade em 90 dias: 52.6%"
    - >= 40:       "Mortalidade em 90 dias: 71.3%"

application/servicos/calculadora_service.py
  - Adicionar função calcular_meld(dados: dict) → dict
    Retorna: {"score": int, "mortalidade_90d": str}

presentation/telas/calculadora_meld.py
  - Tela Flet com:
    - 3 campos numéricos float (bilirrubina, INR, creatinina)
    - Botão "Calcular MELD"
    - Exibir score inteiro em destaque
    - Exibir mortalidade em 90 dias
    - Cor por faixa: <10 verde · 10-19 amarelo claro ·
      20-29 amarelo · 30-39 laranja · >=40 vermelho
```

---

[pausar antes de enviar]

"Perceba o que está no domínio e o que está na tela.

O `max(valor, 1.0)` está em `calcular()` — dentro da classe Meld.
A tela não sabe que essa regra existe.
A tela só passa os valores que o médico digitou.
O domínio aplica a convenção.

Essa separação é o princípio que você aprendeu na aula_15:
as regras do domínio ficam no domínio.
A tela não decide nada clínico."

---

[enviar o prompt ao Claude Code]

---

## SEÇÃO 4: CLAUDE IMPLEMENTA MELD + LEITURA SUPERVISIONADA — 10 min

**Tom:** Aguardar + auditar — quatro perguntas, terceira é crítica

[aguardar o Claude Code processar]

[mostrar na tela os arquivos sendo criados e modificados]

"Dois arquivos novos.
Um modificado.

`domain/calculadoras/meld.py` — criado.
`presentation/telas/calculadora_meld.py` — criado.
`application/servicos/calculadora_service.py` — modificado.

Agora você lê antes de rodar.

Quatro perguntas."

---

**Pergunta 1:**

"Abra `domain/calculadoras/meld.py`.

Os campos são declarados como `float`, não `int`?

Você está procurando os três atributos da classe Meld.
Se aparecerem como `int`, o campo vai recortar a parte decimal —
bilirrubina 4,5 vira 4, e o score fica errado.

[mostrar o código]

Correto — `float` nos três campos."

---

**Pergunta 2:**

"O `calcular()` usa `math.log` — logaritmo natural — não `math.log10`?

Procure a importação no topo do arquivo.
Deve estar `import math`.

Depois procure a fórmula dentro de `calcular()`.
Deve estar `math.log(bilirrubina_efetiva)`.
Não `math.log10`.

`math.log10(4.5)` é 0,653.
`math.log(4.5)` é 1,504.
O MELD usa o logaritmo natural.
Se o Claude usou `log10`, o score vai ser completamente diferente.

[mostrar a fórmula no código]

Correto — `math.log`, logaritmo natural."

---

**Pergunta 3:** ← crítica

"O `min=1.0` está aplicado no domínio antes do `math.log` — não na tela?

Essa é a pergunta mais importante do arco MELD.

Procure dentro do método `calcular()`.
Você deve ver algo como:

```python
bilirrubina_efetiva = max(self.bilirrubina_mg_dl, 1.0)
inr_efetivo = max(self.inr, 1.0)
creatinina_efetiva = max(self.creatinina_mg_dl, 1.0)
```

Esses três `max()` devem aparecer antes do `math.log`.

Agora abra `presentation/telas/calculadora_meld.py`.
A tela não deve ter nenhum `max()`.
A tela recebe o valor digitado e passa direto para o serviço.

Se o `max()` estiver só na tela — a regra clínica está no lugar errado.
Um médico que chame o serviço sem passar pela tela vai receber um logaritmo inválido.

[mostrar o domínio]

Correto — os três `max()` estão no domínio, antes do logaritmo.

[confirmar que a tela não tem max()]

Correto — a tela está limpa."

---

**Pergunta 4:**

"A tela chama o serviço — não calcula direto?

Abra `presentation/telas/calculadora_meld.py`.

Quando o botão 'Calcular MELD' é clicado,
o código deve chamar `calcular_meld` do `calculadora_service`.
Não deve conter `math.log` nem `round()`.

[mostrar a chamada ao serviço]

Está chamando o serviço. A arquitetura está respeitada."

---

**Frase-âncora MELD:**

"O médico não digita logaritmo.
Ele descreve a fórmula em português.
O Claude codifica.

Mas a regra clínica do `min=1.0` mora no domínio —
não na tela."

---

## SEÇÃO 5: APP AO VIVO MELD + VALIDAÇÃO — 5 min

**Tom:** Payoff — dois casos com escalas de gravidade bem distintas

[no terminal]

```
uv run python main.py
```

[aguardar o Flet abrir no browser]

---

**Caso 1 — âncora (score 20, mortalidade 19,6%):**

"Aqui está a tela do MELD.

Três campos decimais.
Um botão.

Nosso paciente de 58 anos.

[preencher os campos]

- Bilirrubina: 4,5
- INR: 1,8
- Creatinina: 1,2

[clicar Calcular MELD]

Score: **20**.
Mortalidade em 90 dias: **19,6%**.

Bateu o gabarito."

---

**Caso 2 — grave (score 31, mortalidade 52,6%):**

"Agora o caso grave.

Cirrose descompensada severa.
Todos os marcadores elevados.

[preencher os campos]

- Bilirrubina: 8,0
- INR: 2,5
- Creatinina: 2,0

[clicar Calcular MELD]

Score: **31**.
Mortalidade em 90 dias: **52,6%**.

---

Veja a diferença entre os dois casos.

Score 20 — esse paciente está em risco moderado-alto.
Score 31 — esse paciente tem mais de 50% de mortalidade em 90 dias.

A mesma fórmula. Os mesmos logaritmos.
O app calcula. O médico decide.

---

O arco MELD está fechado.

Agora: o segundo paradigma."

---

## SEÇÃO 6: MMSE COMO ESPECIFICAÇÃO — 6 min

**Tom:** Clínico e afetivo — a perda de memória tem gradações

"Geriatra.

Paciente de 72 anos, mulher.
Viúva há dois anos.
A filha traz para a consulta.
Esquecimento crescente nos últimos seis meses.
Às vezes não lembra o dia.
Às vezes não lembra o que foi buscar no quarto.

Você precisa quantificar o quanto de cognição está preservado.

O instrumento é o MMSE — Mini-Mental State Examination."

---

[mostrar na tela]

"O MMSE não é uma soma de itens iguais.
É uma soma de **subtestes** — cada um com um teto diferente.

Seis subtestes:

| Subteste | Campo | Máximo |
|---|---|---|
| Orientação temporal | orientacao_temporal | 5 |
| Orientação espacial | orientacao_espacial | 5 |
| Registro (memória imediata) | registro | 3 |
| Atenção e cálculo | atencao_calculo | 5 |
| Evocação (memória tardia) | evocacao | 3 |
| Linguagem e praxia | linguagem_praxia | 9 |

Score total: 0 a 30.

---

Linguagem e praxia tem o maior peso — 9 pontos.
Inclui nomear objetos, repetir frase, seguir comando, ler, escrever e copiar figura.

A figura é a dos pentágonos sobrepostos — você vai ver na tela.
O médico avalia presencialmente e registra o score do subteste inteiro.

---

Quatro faixas:

| Score | Resultado |
|---|---|
| ≥ 24 | Normal |
| 18 a 23 | Comprometimento leve |
| 10 a 17 | Comprometimento moderado |
| < 10 | Comprometimento grave |

---

Agora o caso âncora.

Paciente de 72 anos.

[calcular ao vivo]

- Orientação temporal: 3 de 5 — não sabe o dia nem o mês
- Orientação espacial: 4 de 5 — sabe o hospital, não sabe o andar
- Registro: 2 de 3 — lembrou 2 das 3 palavras
- Atenção e cálculo: 3 de 5 — errou 2 das subtrações
- Evocação: 1 de 3 — lembrou 1 palavra após 5 min
- Linguagem e praxia: 7 de 9 — dificuldade em copiar a figura e em seguir comando complexo

3 + 4 + 2 + 3 + 1 + 7 = **20**

Score 20 → Comprometimento leve.

Esse é o gabarito."

---

## SEÇÃO 7: PROMPT MMSE — 5 min

**Tom:** Professor conduz — destaques: limites heterogêneos por subteste e o tooltip dos pentágonos

"O MMSE tem uma diferença estrutural em relação a tudo que você viu.

Cada campo tem um limite diferente.
O app precisa saber que `orientacao_temporal` vai de 0 a 5
e `linguagem_praxia` vai de 0 a 9 —
e não pode aceitar valores além do limite de cada subteste.

Outra diferença: o subteste de linguagem e praxia inclui a figura dos pentágonos.
Você não consegue fazer o médico desenhar no app.
O que você faz: coloca um ícone de configuração ao lado do campo
com uma imagem de referência dos pentágonos sobrepostos.
O médico avalia presencialmente e digita o score do subteste inteiro."

---

[digitar no terminal — ler cada parte em voz alta]

```
Implemente a calculadora MMSE no ClinMd-Tribe
respeitando a Clean Architecture das 4 camadas:

domain/calculadoras/mmse.py
  - Classe Mmse com 6 campos inteiros e seus limites máximos:
    orientacao_temporal (0-5)
    orientacao_espacial (0-5)
    registro (0-3)
    atencao_calculo (0-5)
    evocacao (0-3)
    linguagem_praxia (0-9)
  - Método calcular() → score inteiro 0-30
    (soma dos 6 subtestes)
  - Método interpretar(score) → str
    - >= 24:    "Normal"
    - 18 a 23:  "Comprometimento leve"
    - 10 a 17:  "Comprometimento moderado"
    - < 10:     "Comprometimento grave"

application/servicos/calculadora_service.py
  - Adicionar função calcular_mmse(dados: dict) → dict
    Retorna: {"score": int, "faixa": str}

presentation/telas/calculadora_mmse.py
  - Tela Flet com:
    - 6 campos numéricos, cada um com seu máximo visível:
      Orientação temporal (0-5)
      Orientação espacial (0-5)
      Registro (0-3)
      Atenção e cálculo (0-5)
      Evocação (0-3)
      Linguagem + praxia (0-9) — com ícone ⚙ tooltip
        mostrando imagem de referência dos pentágonos sobrepostos
    - Botão "Calcular MMSE"
    - Exibir score total em destaque
    - Cor por faixa: Normal verde · Leve amarelo ·
      Moderado laranja · Grave vermelho
```

---

[pausar antes de enviar]

"Note o que o prompt especifica sobre os limites.

Cada campo tem o seu máximo escrito — não apenas como label na tela,
mas como dado que o domínio vai respeitar.

Se o médico digitar 10 em `orientacao_temporal`, que tem máximo 5,
o app não pode aceitar.
O domínio protege a integridade do score."

---

[enviar o prompt ao Claude Code]

---

## SEÇÃO 8: CLAUDE IMPLEMENTA MMSE + LEITURA SUPERVISIONADA — 8 min

**Tom:** Aguardar + auditar — três perguntas, sequência mais rápida que o MELD

[aguardar o Claude Code processar]

[mostrar na tela os arquivos sendo criados e modificados]

"Dois arquivos novos.
Um modificado.

`domain/calculadoras/mmse.py` — criado.
`presentation/telas/calculadora_mmse.py` — criado.
`application/servicos/calculadora_service.py` — modificado novamente.

Três perguntas."

---

**Pergunta 1:**

"Abra `domain/calculadoras/mmse.py`.

Cada subteste recusa valor acima do seu máximo?

Você está procurando uma validação por campo.
Pode ser `min(valor, maximo)` dentro do `calcular()`,
ou validação no momento de atribuição.

O importante é que `linguagem_praxia=10` não deve ser aceito —
o máximo é 9.
Um subteste que aceita valores além do teto vai inflar o score total.

[mostrar o código]

Correto — cada subteste tem seu limite aplicado."

---

**Pergunta 2:**

"O cutoff de Normal é 24 — não 25?

Procure o método `interpretar()`.

A primeira condição deve ser `score >= 24`.
Se estiver `score >= 25`, um paciente com score 24 vai ser classificado como Leve
quando deveria ser Normal.

Um ponto de diferença na conduta diagnóstica.

[mostrar as condições]

Correto — Normal começa em 24."

---

**Pergunta 3:**

"A tela chama o serviço — não calcula direto?

Abra `presentation/telas/calculadora_mmse.py`.

Quando o botão 'Calcular MMSE' é clicado,
o código deve chamar `calcular_mmse` do `calculadora_service`.
Não deve fazer a soma diretamente na tela.

[mostrar a chamada ao serviço]

Está chamando o serviço. A arquitetura está respeitada.

---

Três perguntas. Três confirmações."

---

**Frase-âncora MMSE:**

"Cada subteste tem um teto.
O domínio sabe.
A tela só registra."

---

## SEÇÃO 9: APP AO VIVO MMSE + VALIDAÇÃO — 4 min

**Tom:** Payoff — dois casos: comprometimento leve e grave

[no terminal — o app já está rodando]

[navegar para a tela MMSE]

---

**Caso 3 — âncora (72F, score 20, comprometimento leve):**

"Aqui está a tela do MMSE.

Seis campos.
Cada um com seu máximo visível.

Nossa paciente de 72 anos.

[preencher os campos]

- Orientação temporal: 3
- Orientação espacial: 4
- Registro: 2
- Atenção e cálculo: 3
- Evocação: 1
- Linguagem + praxia: 7

[clicar Calcular MMSE]

Score: **20**.
Faixa: **Comprometimento leve** — em amarelo.

Bateu o gabarito."

---

**Caso 4 — grave (score 7, comprometimento grave):**

"Agora o caso grave.

Idoso, desorientado.
Sem recordação das palavras.
Linguagem comprometida.

[preencher os campos]

- Orientação temporal: 1
- Orientação espacial: 1
- Registro: 0
- Atenção e cálculo: 1
- Evocação: 0
- Linguagem + praxia: 4

[clicar Calcular MMSE]

Score: **7**.
Faixa: **Comprometimento grave** — em vermelho.

---

Veja os dois casos.

Score 20: a cognição está comprometida, mas há preservação significativa.
Score 7: abaixo de 10 — comprometimento grave.

O app registra.
O médico interpreta.
A família que está na sala do lado aguarda."

---

## SEÇÃO 10: ENCERRAMENTO + BRIDGE S06 — 4 min

**Tom:** Fechamento de ciclo — consolidar os três paradigmas e abrir o próximo módulo

"Vamos fechar o módulo S05.

Você começou com a FA de um paciente em risco de AVC.
Terminou com o fígado falhando de um paciente cirrótico
e a memória partindo de uma paciente de 72 anos.

Seis calculadoras.
Três paradigmas.

---

**Paradigma 1: booleano.**
CHA₂DS₂-VASc e HAS-BLED.
Cada critério é presente ou ausente.
O app soma zeros e uns.

**Paradigma 2: Likert.**
PHQ-9 e GAD-7.
Cada item tem frequência — nunca, alguns dias, quase todo dia.
O app soma de zero a três por item.

**Paradigma 3: fórmula e subtestes.**
MELD: logaritmos de três variáveis laboratoriais.
MMSE: seis subtestes com tetos diferentes.

---

A próxima vez que você receber uma calculadora clínica nova,
você vai olhar para ela e reconhecer: qual é o paradigma?

Booleano — checkboxes, soma simples.
Likert — dropdowns 0-3, tem item especial?
Fórmula — float, logaritmo, convenção numérica?
Subtestes heterogêneos — limites diferentes por campo?

Você tem os três padrões.
O código vai seguir.

---

Na próxima aula: o dinheiro do consultório.

O ClinMd-Tribe tem as calculadoras clínicas.
Agora vai ganhar uma nova funcionalidade:
registrar receitas, glosas e consultas mês a mês.

O módulo S06 é o dashboard financeiro —
KPIs, gráficos, visão do consultório.

Até lá."

---

**FIM DO ROTEIRO**
