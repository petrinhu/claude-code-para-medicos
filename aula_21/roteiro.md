# Aula 21 — CHA₂DS₂-VASc: Sua Primeira Calculadora Clínica

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~55 min  
**Tom:** Colega com humor leve e didático — "de hoje em diante você constrói ferramentas que outros usam"  
**Módulo:** S05.01 — Calculadoras Médicas  
**Persona:** Cardiologista  

---

## SEÇÃO 1: ABERTURA DO MÓDULO S05 — 3 min

**Tom:** Virada de marco — fechar o arco de setup e abrir o arco de produto real

"Vamos fazer um balanço rápido.

Nas últimas dez aulas você montou o laboratório.

Instalou o uv. Aprendeu Python com analogias clínicas.
Criou a interface com Flet. Organizou tudo em quatro camadas.
Recebeu um residente de plantão, equipou ele,
montou o time da bigtech virtual, aprendeu a priorizar o trabalho.

Tudo isso foi setup.

---

A partir de hoje muda o jogo.

Você vai parar de construir a estrutura
e vai começar a construir funcionalidades reais.

Funcionalidades que você vai usar na clínica.
Que colegas seus vão usar.
Que um dia podem entrar em produção.

---

Módulo 5: Calculadoras Médicas.

Quatro aulas. Quatro calculadoras.
Começando hoje com a que você mais vai usar
se você tem pacientes com fibrilação atrial.

Mas antes de falar de código — me conta um caso."

---

## SEÇÃO 2: CLÍNICA COMO ESPECIFICAÇÃO — 10 min

**Tom:** Didático com propósito — a clínica gera o gabarito, não a revisão

"Paciente. 68 anos. Masculino.

Checkup de rotina. ECG de repouso. FA paroxística — descoberta agora.
Hipertenso em tratamento. Diabético tipo 2.
Sem AVC prévio. Sem insuficiência cardíaca. Sem doença vascular conhecida.

A pergunta que você vai fazer — que todo cardiologista faz nesse momento:

Anticoagulo?

---

Para responder isso existe o CHA₂DS₂-VASc.

Não vou te ensinar cardiologia.
Você já sabe o que é esse score — você usa todo dia.

O que eu vou fazer é diferente:
vou te mostrar como transformar o que você já sabe
em uma especificação que o Claude entende.

---

O score tem oito critérios.

[mostrar na tela]

C — Insuficiência cardíaca congestiva: 1 ponto
H — Hipertensão arterial: 1 ponto
A₂ — Idade igual ou maior que 75 anos: 2 pontos
D — Diabetes mellitus: 1 ponto
S₂ — AVC, AIT ou tromboembolismo prévio: 2 pontos
V — Doença vascular: 1 ponto
A — Idade entre 65 e 74 anos: 1 ponto
Sc — Sexo feminino: 1 ponto

Dois critérios valem 2 pontos: o A₂ e o S₂.
Os outros valem 1.

Score máximo: 9 pontos se for mulher, 8 se for homem.

---

Cutoff para anticoagular:

Homem com score maior ou igual a 2: anticoagular.
Mulher com score maior ou igual a 3: anticoagular.

---

Agora: o caso do nosso paciente.

[calcular ao vivo]

C: não tem insuficiência cardíaca → 0
H: hipertenso → 1
A₂: 68 anos, não tem 75 ainda → 0
D: diabético → 1
S₂: sem AVC prévio → 0
V: sem doença vascular → 0
A: 68 anos, está na faixa 65-74 → 1
Sc: masculino → 0

Total: 3 pontos.

Homem com score 3. Cutoff é 2.

Anticoagula.

---

Anote esse número: 3.

É o gabarito.

Quando o app estiver pronto, você vai digitar esses mesmos dados
e o app vai ter que responder: 3 — Anticoagular.

Se não bater, tem erro na implementação.
Se bater, você pode assinar."

---

## SEÇÃO 3: O PROMPT DESCRITIVO — 8 min

**Tom:** Revelar que o prompt é o protocolo, não o código

"Agora vem a parte que você ainda não fez neste curso.

Nas aulas anteriores o Claude Code ajudava você a entender código
que já existia — o scaffold, a estrutura, os arquivos.

Hoje você vai pedir para o Claude Code criar algo novo do zero.

E o segredo é simples: você não escreve código.
Você escreve um protocolo.

---

[mostrar na tela]

O prompt que vou usar agora foi preparado antes da aula.
Você não vai decorá-lo — vai entendê-lo.
E na sua especialidade você vai escrever o equivalente.

[digitar no terminal — o professor lê cada parte enquanto digita]

```
Implemente a calculadora CHA₂DS₂-VASc no ClinMd-Tribe
respeitando a Clean Architecture das 4 camadas:

domain/calculadoras/cha2ds2vasc.py
  - Classe Cha2ds2Vasc com campos:
    chf, has, idade (int), dm, avc_previo,
    doenca_vascular, sexo_feminino (bool)
  - Método calcular() → retorna score inteiro 0–9
    Regras:
    - idade >= 75: 2 pts
    - idade entre 65 e 74: 1 pt
    - avc_previo: 2 pts
    - chf, has, dm, doenca_vascular: 1 pt cada
    - sexo_feminino: 1 pt
  - Método interpretar(score, sexo_feminino) → str
    - Homem: score >= 2 → "Anticoagular"
    - Homem: score < 2 → "Sem indicação no momento"
    - Mulher: score >= 3 → "Anticoagular"
    - Mulher: score < 3 → "Sem indicação no momento"

application/servicos/calculadora_service.py
  - Função calcular_cha2ds2vasc(dados: dict) → dict
    Retorna: {"score": int, "recomendacao": str}

presentation/telas/calculadora_cha2ds2vasc.py
  - Tela Flet com:
    - Checkbox para: CHF, HAS, DM, AVC prévio, doença vascular
    - Campo numérico para idade
    - Radio para sexo (Masculino / Feminino)
    - Botão "Calcular"
    - Exibir score em destaque (número grande)
    - Exibir recomendação:
      "Sem indicação" em verde
      "Anticoagular" em laranja
```

---

Olha o que esse prompt é.

É um protocolo clínico na linguagem do sistema.

Você descreveu as regras do score — que você já conhecia.
Você descreveu onde cada parte vai morar — que você aprendeu na aula_15.
Você descreveu como a tela deve aparecer — que você viu na aula_13.

Você não escreveu uma linha de Python.
Você escreveu uma prescrição.

O Claude vai executar a prescrição."

---

## SEÇÃO 4: CLAUDE IMPLEMENTA — 5 min

**Tom:** Mostrar os arquivos criados — não explicar cada linha ainda

"[aguardar o Claude Code processar o prompt]

[mostrar na tela os arquivos sendo criados]

Três arquivos novos.

`domain/calculadoras/cha2ds2vasc.py` — a lógica do score.
`application/servicos/calculadora_service.py` — o serviço que conecta.
`presentation/telas/calculadora_cha2ds2vasc.py` — a tela no Flet.

---

Agora uma coisa importante.

O Claude gerou o código. Mas você ainda não pode confiar nele.

Não porque o Claude erra sempre — ele erra às vezes.
Não porque Python seja complicado — você não precisa entender Python.

Mas porque você é o médico.
E score médico errado em silêncio é risco para o paciente.

Você não assina um laudo sem ler.
Você não usa um app sem validar.

Próxima seção: leitura clínica do código."

---

## SEÇÃO 5: LEITURA SUPERVISIONADA — 12 min

**Tom:** Clínico fazendo auditoria — verificar regras, não sintaxe

"Vamos abrir o arquivo de domínio primeiro.

[abrir domain/calculadoras/cha2ds2vasc.py]

Você não precisa entender cada linha.
Você precisa responder cinco perguntas.

---

Pergunta 1: o campo de idade está calculando A₂ e A separados?

A₂ vale 2 pontos para quem tem 75 ou mais.
A vale 1 ponto para quem tem entre 65 e 74.

Procure no código uma linha que testa `idade >= 75`
e outra que testa `65 <= idade <= 74` ou equivalente.

[mostrar as linhas correspondentes]

Está lá? Sim.

---

Pergunta 2: o `avc_previo` está valendo 2 pontos?

Esse é o erro mais comum em implementações de CHA₂DS₂-VASc.
Alguém confunde S₂ com S e coloca 1 ponto.

Procure no código onde `avc_previo` contribui para o score.
Confirme que soma 2, não 1.

[mostrar a linha]

Correto.

---

Pergunta 3: o sexo feminino está adicionando 1 ponto ao score?

[mostrar a linha com sexo_feminino]

Sim.

---

Pergunta 4: o cutoff para mulher está em 3, não em 2?

Abra o método `interpretar`.
Procure onde ele verifica `sexo_feminino`.
O número que aparece deve ser 3, não 2.

[mostrar a condição]

Correto.

---

Pergunta 5: a tela está associada ao serviço?

Abra `presentation/telas/calculadora_cha2ds2vasc.py`.

O botão Calcular chama a função de `calculadora_service`?
Ou o cálculo está direto na tela — fora da arquitetura?

[mostrar a chamada]

Está chamando o serviço. A camada está respeitada.

---

Cinco perguntas. Todas respondidas.

Você leu o código como médico, não como programador.
Verificou as regras clínicas, não a sintaxe Python.

Isso é o que significa supervisionar.

Frase que vai aparecer várias vezes neste curso:

Você não lê para entender Python.
Você lê para assinar o laudo."

---

## SEÇÃO 6: APP AO VIVO — 7 min

**Tom:** Payoff — o cardiologista vê o score na tela que construiu

"Agora a parte que você esperava desde a abertura.

Vamos rodar o app.

[no terminal]

```
uv run python main.py
```

[aguardar o Flet abrir no browser]

---

[mostrar a tela da calculadora na tela do professor]

Está aqui.

A calculadora CHA₂DS₂-VASc.
No seu app. No ClinMd-Tribe.
Que você vai usar na clínica.

---

Agora: o caso do nosso paciente.

68 anos. Masculino.
HAS: sim.
DM: sim.
Os outros critérios: não.

[preencher cada campo ao vivo]

[clicar Calcular]

---

Score: 3.

Recomendação: Anticoagular.

---

Bate com o gabarito que calculamos à mão no começo da aula.

Esse é o momento de confiar.
Não porque o app é bonito.
Não porque o código ficou limpo.

Mas porque o número bateu com o que você calcularia à mão."

---

## SEÇÃO 7: VALIDAÇÃO CRUZADA — 5 min

**Tom:** Rigoroso — um caso não é suficiente para confiar num instrumento clínico

"Um caso não é suficiente.

Você não valida um aparelho de PA com uma medida só.
Você não valida uma calculadora com um paciente só.

Vamos testar mais dois.

---

Caso 2: paciente de 55 anos, masculino, sem nenhum fator de risco.

[preencher na tela: todos os campos desmarcados, idade 55, masculino]

[clicar Calcular]

Score: 0.
Sem indicação no momento.

Correto. Nenhum critério preenchido, nenhum ponto.

---

Caso 3: paciente de 77 anos, feminina.
Insuficiência cardíaca. Hipertensa. AVC prévio.

[preencher: CHF marcado, HAS marcado, AVC prévio marcado, idade 77, feminino]

[clicar Calcular]

Score: 7.

Vamos conferir à mão:
C: 1 + H: 1 + A₂: 2 (tem 77 anos) + S₂: 2 (AVC prévio) + Sc: 1 (feminino) = 7.

Bate.

Recomendação: Anticoagular. Evidentemente.

---

Três casos. Três acertos.

Agora você tem razão para confiar.

Esse processo — testar com casos que você conhece a resposta —
é o processo de validação de qualquer instrumento clínico.

Termômetro, glicômetro, aparelho de PA, app de calculadora.
A lógica é a mesma.

Você não confia num aparelho de PA só porque ele apitou.
Você compara com pacientes que você conhece.
Com o app é igual."

---

## SEÇÃO 8: ENCERRAMENTO + DEVER — 5 min

**Tom:** Consolidar + motivar + ponte para a próxima calculadora

"Resumo do que ficou pronto hoje.

Você escreveu um prompt descritivo em linguagem natural.
O Claude implementou a calculadora CHA₂DS₂-VASc nas 4 camadas certas.
Você leu o código com olho clínico — verificou as regras, não a sintaxe.
Rodou o app ao vivo e viu o score aparecer na tela.
Validou com três casos clínicos conhecidos.

O ClinMd-Tribe agora tem a sua primeira funcionalidade real.

---

Uma observação sobre o que aconteceu aqui.

Você é cardiologista — ou clínico com pacientes de FA.
Você sabe as regras do CHA₂DS₂-VASc de cor.

E foi exatamente por isso que você conseguiu fazer isso.

O conhecimento clínico que você tem
é o que transforma um prompt vago em uma especificação precisa.
É o que permite que você valide o resultado.
É o que separa uma calculadora que funciona de uma que mente.

A ferramenta é do médico. Não do programador.

---

Dever de casa.

Abra o ClinMd-Tribe.
Pense em um paciente com FA que você está acompanhando.

Antes de digitar qualquer coisa: des-identifica.
Nome: Paciente 001.
CPF, data de nascimento, endereço: apaga.
Mantém só: sexo, faixa etária, os critérios clínicos.

Preencha a calculadora com os dados des-identificados.
Compare o score do app com o score que você calcularia à mão.

Se bater: você tem uma ferramenta validada.
Se não bater: me manda o caso des-identificado e a gente investiga juntos.

---

Na próxima aula: o outro lado da balança.

O CHA₂DS₂-VASc calcula o risco de AVC.
Mas anticoagular tem um custo: o risco de sangramento.

Na aula_22 você implementa o HAS-BLED —
e aí você tem os dois lados.
Com os dois scores em mão, a decisão de anticoagular
deixa de ser intuição e vira dado.

Até lá."

---

**FIM DO ROTEIRO**
