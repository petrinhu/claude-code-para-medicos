# Aula 22 — HAS-BLED: O Outro Lado da Balança

**Formato:** Gravada no OBS Studio, editada no Kdenlive  
**Duração:** ~45 min  
**Tom:** Colega com humor leve e didático — "agora você tem os dois lados"  
**Módulo:** S05.02 — Calculadoras Médicas  
**Persona:** Cardiologista  

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Já preparado em `resources/` (é só usar):**

- [ ] `resources/casos_teste_hasbled.md` : os dois casos clínicos fictícios com gabarito (HAS-BLED 1 com Decisão FA "Anticoagular"; HAS-BLED 7 com Decisão FA "individualizada"). Apoio das Seções 6 e 7. Só o instrutor vê; não aparece na aula.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] O ClinMd-Tribe já com a calculadora CHA₂DS₂-VASc da aula_21 funcionando (esta aula adiciona o HAS-BLED e o painel Decisão FA). O `uv run python main.py` deve subir o app no navegador.

**Confira antes de gravar:**

- [ ] Tenha o prompt descritivo da Seção 3 à mão (está no roteiro) para colar de uma vez no terminal.
- [ ] Dois arquivos novos e um modificado são gerados ao vivo (`domain/calculadoras/hasbled.py`, `presentation/telas/calculadora_hasbled.py`, e o `application/servicos/calculadora_service.py` ganha uma função). Saiba em que pastas caem para abri-los na leitura supervisionada.
- [ ] Rode `uv run python main.py` uma vez antes de gravar para confirmar que o app abre sem erro.

**Navegador:** o app Flet abre no navegador local (`uv run python main.py`); nenhum site externo é necessário.

---

## SEÇÃO 1: ABERTURA — 2 min

**Tom:** Continuação direta da aula_21 — retomar o caso, não começar do zero

**[Aviso rápido dos óculos, antes de mergulhar]**

"Antes da balança virar: óculos no nariz. Hoje a gente cruza dois scores na mesma tela, e confundir um 3 com um 8 por causa da fonte pequena é o tipo de erro que muda anticoagulação. Foca a tela, que aqui cada dígito pesa."

"Na aula passada você ficou com metade da resposta.

O paciente: 68 anos, masculino, FA paroxística,
hipertenso em tratamento, diabético.

O CHA₂DS₂-VASc: score 3. Anticoagulação indicada.

Mas você não anticoagulou ainda.

Por quê?

Porque anticoagular tem um custo.
Você reduziu o risco de AVC — mas expôs o paciente ao risco de sangramento.

Hoje você calcula o outro lado da balança.

Ao final desta aula, você vai ver os dois scores na tela ao mesmo tempo.
E a decisão vai deixar de ser intuição."

---

## SEÇÃO 2: HAS-BLED COMO ESPECIFICAÇÃO — 7 min

**Tom:** Mais rápido que na aula_21 — aluno já sabe o método, o foco é a clínica

"O HAS-BLED foi desenvolvido para estimar o risco de sangramento
em pacientes com FA em uso de anticoagulante.

[mostrar na tela]

Sete critérios:

H — Hipertensão não controlada (PAS acima de 160): 1 ponto
A — Disfunção renal ou hepática: 1 ponto
S — AVC ou AIT prévio: 1 ponto
B — Sangramento prévio ou predisposição: 1 ponto
L — INR lábil: 1 ponto
E — Idade acima de 65 anos: 1 ponto
D — Drogas antiagregantes, AINEs ou álcool: 1 ponto

Score máximo: 7.

> [CONFERIR CLÍNICO: 7 critérios HAS-BLED, 1 ponto cada, score máximo 7. Nota: o HAS-BLED original tem componentes que podem somar até 9 (função renal e hepática contam separado; drogas e álcool contam separado). Esta aula adota a versão simplificada de 7 itens / 7 pontos, coerente com o resource. Validar se essa simplificação é aceitável para o uso clínico pretendido.]

---

Interpretação:

Score menor que 3: baixo risco de sangramento.
Score igual a 3: risco moderado.
Score maior que 3: alto risco.

> [CONFERIR CLÍNICO: faixas de risco de sangramento (< 3 baixo, = 3 moderado, > 3 alto). Bate com o resource.]

---

Um detalhe importante: o critério L.

INR lábil significa que o paciente anticoagulado com warfarina
fica menos de 60% do tempo dentro da faixa terapêutica.

É o critério mais frequentemente esquecido nas implementações.
Vamos prestar atenção nele quando ler o código.

---

Agora: nosso paciente.

[calcular ao vivo]

H: hipertenso, mas em tratamento e controlado — PAS dentro do alvo → 0
A: sem disfunção renal ou hepática → 0
S: sem AVC ou AIT prévio → 0
B: sem sangramento prévio → 0
L: não está em uso de warfarina ainda → 0
E: 68 anos, acima de 65 → 1
D: sem AAS, AINE ou álcool → 0

Total: 1 ponto.

HAS-BLED de 1: baixo risco de sangramento.

> [CONFERIR CLÍNICO: caso âncora 68a masculino, HAS controlada, só idade > 65 = HAS-BLED 1, baixo risco. Bate com o resource (Caso 1).]

---

Anote: HAS-BLED = 1.

Esse é o gabarito.

Na aula passada você anotou CHA₂DS₂-VASc = 3.

Ao final desta aula, os dois vão aparecer na mesma tela.
E a decisão vai estar lá."

---

## SEÇÃO 3: O PROMPT DESCRITIVO — 7 min

**Tom:** Mostrar que fica mais fácil na segunda vez — o padrão está internalizado

"Na aula_21 você precisou que eu lesse cada parte do prompt
e explicasse o que cada trecho fazia.

Hoje vai ser diferente.

Você já sabe o que é Clean Architecture.
Você já sabe o que é domain, application, presentation.
Você já sabe que o médico escreve o protocolo — e o Claude executa.

O prompt desta vez vai ser mais curto.
Não porque a calculadora é mais simples —
mas porque você ficou mais rápido.

---

[digitar no terminal — o professor lê em ritmo mais acelerado]

```
Implemente a calculadora HAS-BLED no ClinMd-Tribe
respeitando a Clean Architecture das 4 camadas:

domain/calculadoras/hasbled.py
  - Classe HasBled com 7 campos booleanos:
    has_descontrolada, disfuncao_renal_hepatica, avc_previo,
    sangramento_previo, inr_labial, idoso, drogas_alcool
  - Método calcular() → score inteiro 0-7
  - Método interpretar(score) → str
    - score < 3 → "Baixo risco de sangramento"
    - score == 3 → "Risco moderado de sangramento"
    - score > 3 → "Alto risco de sangramento"

application/servicos/calculadora_service.py
  - Adicionar função calcular_hasbled(dados: dict) → dict
    Retorna: {"score": int, "interpretacao": str}

presentation/telas/calculadora_hasbled.py
  - Tela Flet com:
    - 7 checkboxes para os critérios HAS-BLED
    - Botão "Calcular HAS-BLED"
    - Exibir score em destaque
    - Exibir interpretação: verde se score < 3, amarelo se = 3, vermelho se > 3
    - Seção "Decisão FA":
      - Campo numérico: "CHA₂DS₂-VASc (da calculadora anterior)"
      - Radio: sexo do paciente (Masculino / Feminino)
      - Botão "Ver decisão"
      - Exibir recomendação combinada:
        · CHA₂DS₂-VASc maior ou igual ao cutoff E HAS-BLED menor que 3:
          "Anticoagular — baixo risco de sangramento" em verde
        · CHA₂DS₂-VASc maior ou igual ao cutoff E HAS-BLED maior ou igual a 3:
          "Decisão individualizada — discutir risco/benefício" em laranja
        · CHA₂DS₂-VASc menor que o cutoff:
          "Sem indicação de anticoagulação" em cinza
      (cutoff: homem ≥ 2 · mulher ≥ 3)
```

> [NOTA: o campo do critério L está nomeado `inr_labial` no prompt e na leitura da Seção 5; o termo clínico correto é "INR lábil". Nome de variável é interno (não aparece na tela do médico) e está consistente entre prompt e leitura, então a demo funciona. Padronizar para `inr_labil` numa rodada futura se quiser rigor terminológico.]

---

Percebe o que ficou diferente?

Você digitou mais rápido.
Você não precisou pausar para pensar onde cada coisa vai.

Isso é o padrão sendo internalizado.

Daqui a quatro aulas, quando você implementar a décima calculadora,
vai ser mais rápido ainda."

---

## SEÇÃO 4: CLAUDE IMPLEMENTA — 4 min

**Tom:** Rápido — confirmação, não explicação

"[aguardar o Claude Code processar o prompt]

[mostrar na tela os arquivos sendo criados e modificados]

Dois arquivos novos.
Um arquivo modificado.

`domain/calculadoras/hasbled.py` — criado.
`presentation/telas/calculadora_hasbled.py` — criado.
`application/servicos/calculadora_service.py` — modificado, função adicionada.

---

O padrão é o mesmo da aula_21.
Mas desta vez você sabia o que esperar antes de o Claude gerar.

Essa antecipação — saber o que vai aparecer antes de aparecer —
é o sinal de que você está entendendo a arquitetura.

Não decorando. Entendendo."

---

## SEÇÃO 5: LEITURA SUPERVISIONADA — 8 min

**Tom:** Auditoria clínica — três perguntas, ritmo mais rápido que na aula_21

"Desta vez: três perguntas.

Na aula_21 foram cinco.
Você já sabe onde olhar — o andaime ficou menor.

---

Pergunta 1: o critério L está no domínio?

Abra `domain/calculadoras/hasbled.py`.

Procure o campo `inr_labial`.

É o critério mais esquecido.
Se não estiver lá — o app está errado e você não pode assinar.

[mostrar o campo]

Está. Correto.

---

Pergunta 2: o método `interpretar()` usa o cutoff de 3, não de 2?

Procure onde o código decide entre baixo, moderado e alto risco.

O número que aparece como limite deve ser 3.
Se for 2, a calculadora vai superestimar o risco — e pode fazer o médico
evitar anticoagulação em quem se beneficiaria dela.

[mostrar a condição]

Correto.

---

Pergunta 3: a seção Decisão FA chama o serviço?

Abra `presentation/telas/calculadora_hasbled.py`.

Quando o botão 'Ver decisão' é clicado,
o código chama `calcular_hasbled` do `calculadora_service`?

Ou o cálculo está feito direto na tela, fora da arquitetura?

[mostrar a chamada]

Está chamando o serviço. A camada está respeitada.

---

Três perguntas. Três confirmações.

Você pode assinar."

---

## SEÇÃO 6: APP AO VIVO + CLIMAX — 8 min

**Tom:** Payoff — os dois lados da balança na mesma tela

"[no terminal]

```
uv run python main.py
```

[aguardar o Flet abrir no browser]

---

[mostrar a tela da calculadora HAS-BLED]

Aqui está.

Sete checkboxes. Um botão. O score.

Vamos preencher o nosso paciente.

---

68 anos. Masculino. Hipertenso controlado. Diabético.
Sem disfunção renal ou hepática.
Sem AVC ou AIT.
Sem sangramento prévio.
Sem warfarina ainda — INR não se aplica.
Sem AAS, AINE ou álcool.

[preencher cada campo ao vivo — apenas E marcado]

[clicar Calcular HAS-BLED]

---

Score: 1.

Baixo risco de sangramento.

---

Agora: a seção Decisão FA.

CHA₂DS₂-VASc: digito 3.
Sexo: masculino.

[clicar Ver decisão]

---

[mostrar o resultado em destaque]

Anticoagular — baixo risco de sangramento.

---

Os dois lados da balança.

CHA₂DS₂-VASc de 3: a indicação está lá.
HAS-BLED de 1: o risco de sangramento é baixo.

A decisão virou dado.

Não é intuição. Não é experiência clínica sozinha.
É o protocolo — calculado, verificado, documentado.

E você construiu a ferramenta que faz esse cálculo."

---

## SEÇÃO 7: VALIDAÇÃO CRUZADA — 4 min

**Tom:** Rigoroso — e introduzindo o limite da calculadora

"Um segundo caso. Diferente do primeiro.

Paciente de 78 anos, feminina.
Hipertensa, pressão não controlada.
Doença renal crônica estágio 4.
AVC isquêmico há dois anos.
Sangramento gastrointestinal prévio.
INR lábil — menos de 60% do tempo em faixa.
Em uso de AAS.

[preencher: todos os critérios marcados, sem exceção]

[clicar Calcular HAS-BLED]

Score: 7.

Alto risco de sangramento.

---

Agora: a seção Decisão FA.

Para essa paciente, o CHA₂DS₂-VASc seria alto —
AVC prévio vale 2, idade acima de 75 vale 2, HAS vale 1, sexo feminino vale 1:
score de 6, pelo menos.

CHA₂DS₂-VASc: digito 6.
Sexo: feminino.

[clicar Ver decisão]

---

Decisão individualizada — discutir risco/benefício.

> [CONFERIR CLÍNICO: Caso 2 - 78a feminina, todos os 7 critérios = HAS-BLED 7 (alto risco); CHA₂DS₂-VASc 6 (AVC 2 + idade>=75 2 + HAS 1 + feminino 1). Combinação alto+alto = "Decisão individualizada". Bate com o resource (Caso 2).]

---

Aqui está o limite da calculadora.

Quando os dois scores são altos,
o app não decide por você.

Ele diz: essa decisão precisa de uma conversa.
Com o paciente, com a família, com o especialista se necessário.

Isso não é uma falha da ferramenta.
É honestidade clínica embutida no código.

A calculadora não é oráculo.
É andaime para o raciocínio.

Você construiu uma ferramenta que sabe o que não sabe."

---

## SEÇÃO 8: ENCERRAMENTO + DEVER — 5 min

**Tom:** Consolidar + motivar + sinalizar a virada de paradigma na aula_23

"Resumo do que ficou pronto hoje.

Você implementou o HAS-BLED — sete critérios, cutoff de 3.
Você verificou o código com três perguntas clínicas.
Você rodou o app e viu os dois scores juntos pela primeira vez.
Você testou o caso mais difícil — e o app respondeu com honestidade.

O ClinMd-Tribe agora tem duas calculadoras.
E um painel de decisão que integra as duas.

---

Dever de casa.

Abra o ClinMd-Tribe.
Pense num paciente com FA que você está acompanhando.

Des-identifica antes de digitar qualquer coisa.
Nome: Paciente 001.
CPF, data de nascimento, endereço: apaga.
Mantém só: sexo, faixa etária, os critérios clínicos.

Calcule o HAS-BLED.
Coloque o CHA₂DS₂-VASc que você calcularia à mão.
Veja o que o Painel de Decisão FA mostra.

Compare com o que você faria clinicamente.
Se divergir — me manda o caso des-identificado.

---

Na próxima aula: o paradigma muda.

Até agora todas as calculadoras trabalharam com sim e não.
Hipertenso ou não. AVC prévio ou não.

Na aula_23, a pergunta vai ser diferente:

Com que frequência?

PHQ-9 e GAD-7 — rastreio de depressão e ansiedade.
Cada item tem quatro opções: nunca, alguns dias, mais da metade dos dias, quase todo dia.
Cada opção tem um valor numérico. A soma decide.

É um padrão novo.
E ele vai aparecer em dezenas de calculadoras que você vai implementar depois.

Até lá."

---

**FIM DO ROTEIRO**
