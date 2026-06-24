# Aula 20 — /tab_pendencias: A Escala Cirúrgica do Projeto

**Formato:** Gravada no OBS Studio, editada no Kdenlive  
**Duração:** ~35 min  
**Tom:** Colega com humor leve e didático — fechar o bloco de agents como quem fecha um plantão bem coordenado

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Já preparado em `resources/` (é só usar):**

- [ ] `resources/prompts_aula20.md` : cola com `/tab_pendencias --create`, o texto pronto das seis calculadoras a fornecer quando a skill pedir os itens, e `/tab_pendencias`. Apoio das Seções 4 e 7.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] A skill `/tab_pendencias` disponível (deve aparecer ao digitar `/`); o ADR-001 da aula_19 já no projeto, pois a tabela referencia decisões já tomadas.

**Confira antes de gravar:**

- [ ] Digite `/` e confirme que `/tab_pendencias` aparece na lista de skills.
- [ ] O `TODO.md` é gerado/atualizado ao vivo; saiba onde ele cai para mostrar o topo da tabela na tela.
- [ ] Após o `--create`, o CHA₂DS₂-VASc deve sair na primeira linha (alto custo de atraso, baixo esforço). Se não subir, refaça o `--create` conferindo a descrição dos itens.

**Navegador:** nenhum site é necessário nesta aula.

---

## SEÇÃO 1: RECONEXÃO — O CHEFE DE EQUIPE QUE VOCÊ SE TORNOU (3 min)

**Tom:** Callback narrativo — fechar o arco do submódulo com satisfação

**[Aviso rápido dos óculos, antes de mergulhar]**

"Rapidinho: ajeita os óculos. A tabela de pendências de hoje tem nove colunas espremidas no terminal, e ler isso de longe é igual tentar bater um martelo na ponta do dedão sem olhar: dói e ainda erra a linha. Aproxima e foca, que vale a pena."

"Vamos fazer um balanço rápido do que aconteceu nas últimas quatro aulas.

aula_17: você recebeu um residente.
Competente, incansável, sem reclamar do plantão duplo.
Mas que chuta com confiança e você assina o laudo.

aula_18: você equipou esse residente.
Maleta com skills, MCPs para conectar ferramentas, hooks para o checklist automático.

aula_19: você descobriu o hospital inteiro.
Narciso na segurança, Caetano na tecnologia, Cósimo que convoca a junta certa.
E você usou o /bigtech para montar o time do ClinMd-Tribe.

---

Hoje: a última peça.

Você tem um residente equipado.
Você tem um hospital de especialistas para interconsulta.

O que falta é o quadro de gestão — o que cada um vai fazer, em que ordem, e por quê.

Hoje você aprende a priorizar o trabalho do seu time
do mesmo jeito que você prioriza a escala cirúrgica do dia."

---

## SEÇÃO 2: A ESCALA CIRÚRGICA DO PROJETO (6 min)

**Tom:** Construir a intuição clínica antes de qualquer sigla

"Você já conhece esse problema.

Terça-feira de manhã. Cinco cirurgias na escala.
Paciente do leito 3: revascularização de miocárdio, coronária comprometida, FA em curso.
Paciente do leito 7: colecistectomia laparoscópica eletiva, calculosa assintomática.
Paciente do leito 11: artroscopia de joelho, dor crônica, paciente estável.
Paciente do leito 14: apendicectomia, irritação peritoneal leve, temperatura 37.8.
Paciente do leito 2: cataratas bilateral, sem impacto em atividade funcional.

Qual sobe na escala?

---

Você não precisou de planilha para responder.

Você avaliou três critérios:

Urgência — o que piora se eu adiar?
O paciente do leito 3 tem FA ativa e coronária comprometida.
O custo de atraso é alto: risco de desfecho ruim.

Complexidade — quanto tempo e recurso o procedimento exige?
A revascularização é o mais complexo, mas o risco de atraso supera qualquer outro.
A artroscopia é simples, mas não urgente — o WSJF dela é baixo.

Sequência obrigatória — o que não posso operar sem antes resolver?
Não opero sem tipagem, ECG, consentimento.
Essas são as dependências — os pré-requisitos.

---

[mostrar a tabela na tela]

| Escala cirúrgica | /tab_pendencias |
|---|---|
| Urgência do procedimento | Custo de atraso — o que piora se adiar |
| Complexidade da cirurgia | Tamanho do trabalho — esforço para implementar |
| Exame obrigatório antes de operar | Pré-requisito — dependência técnica |
| Duas salas ao mesmo tempo | Onda — o que pode rodar em paralelo |

A `/tab_pendencias` faz triagem de sala cirúrgica para as tarefas do seu projeto.
O mais urgente e o mais rápido de resolver sobe ao topo.
O que depende de outra coisa espera a vez."

---

## SEÇÃO 3: WSJF — O NOME QUE A ENGENHARIA DEU PARA A TRIAGEM (4 min)

**Tom:** Revelar o nome como recompensa — o aluno já sabe o conceito

"Esse critério que você acabou de usar tem um nome em engenharia de software.

WSJF. Weighted Shortest Job First.

Tradução direta: o trabalho mais curto e mais custoso de atrasar vai primeiro.

Fórmula:

```
WSJF = Custo de Atraso ÷ Tamanho do Trabalho
```

Custo de Atraso é o quanto você perde esperando.
Tamanho do Trabalho é o esforço para entregar.

Alto custo de atraso, baixo esforço: sobe ao topo.
Baixo custo, alto esforço: espera na fila.

---

Você viu isso na `/tab_pendencias` desde a aula_10.

Só que nunca tinha o nome.

E se você lembra da aula_18, quando a gente abriu o arquivo da skill —
era exatamente esse o método de ordenação que estava escrito lá dentro.

WSJF é a triagem de sala cirúrgica que a skill aplica automaticamente
toda vez que você chama `/tab_pendencias --create` ou `--reorder`.

E a coluna Onda — as tarefas que podem correr em paralelo —
é o equivalente das salas cirúrgicas disponíveis ao mesmo tempo:
sem conflito, sem dependência mútua, podem avançar juntas."

---

## SEÇÃO 4: DEMO — /TAB_PENDENCIAS --CREATE (10 min)

**Tom:** Revelar — o aluno vê a triagem funcionando no projeto real

"Agora vamos criar a primeira tabela real do ClinMd-Tribe.

[entrar no projeto]

```
cd Documents\projetos\clinmd-tribe
claude
```

Prompt:

```
/tab_pendencias --create
```

[a skill vai pedir os itens — fornecer as 5 calculadoras]

---

Quando a skill pedir os itens, vou fornecer as seis calculadoras
que estão no próximo módulo do curso:

CHA₂DS₂-VASc, escore de risco de AVC em fibrilação atrial
HAS-BLED, escore de risco de sangramento na anticoagulação
PHQ-9, escala de rastreio de depressão (Patient Health Questionnaire)
GAD-7, escala de rastreio de ansiedade generalizada
MELD, fórmula de gravidade da doença hepática terminal
MMSE, mini-exame do estado mental

[aguardar o Claude processar e mostrar a tabela]

---

Olha o que apareceu.

Noves colunas. ID, Onda, Grupo, Descrição, Prioridade, Pré-requisito,
Dificuldade, Status, Estado Auditado.

E a tabela já saiu ordenada.

Não foi o Claude chutando.
Foi o WSJF aplicando a triagem cirúrgica nos seus dados."

---

## SEÇÃO 5: DISSECAR A TABELA — POR QUE FICOU NESSA ORDEM? (5 min)

**Tom:** Analisar — o aluno entende o critério que gerou a ordem

"Vamos dissecar a primeira linha.

[mostrar o CHA₂DS₂-VASc no topo]

Por que o CHA₂DS₂-VASc ficou primeiro?

Custo de Atraso: alto.
FA é a arritmia mais prevalente em consultório. O risco tromboembólico é real e urgente.
De todas as calculadoras, essa é a que você mais usa — e a que mais impacto tem se não existir.

Tamanho do Trabalho: baixo.
A regra do score já está definida e consolidada na literatura, você conhece de cor.
Sete parâmetros booleanos, um inteiro de idade, retorna um número. Sem pré-requisito.

WSJF alto ÷ esforço baixo = sobe ao topo.
A triagem cirúrgica foi exata.

---

Agora olha a coluna Onda.

Algumas calculadoras estão na mesma Onda.
Isso significa que podem ser implementadas em paralelo —
como dois procedimentos em salas cirúrgicas diferentes,
sem que um precise esperar o outro terminar.

Você não precisa fazer uma por vez.
A tabela já te disse o que pode rodar junto.

---

É isso que a `/tab_pendencias` entrega:
não só uma lista — uma sequência de execução que minimiza retrabalho
e maximiza o que você consegue avançar em paralelo."

---

## SEÇÃO 6: QUIZ RELÂMPAGO DO MÓDULO 04 + PONTE (4 min)

**Tom:** Recuperação ativa — fechar o arco com o aluno respondendo, não só ouvindo

"Quatro perguntas rápidas do módulo inteiro.
Responda antes de eu falar.

---

O residente de plantão tem quanto de memória quando você abre uma sessão nova no Claude Code?

[pausa]

Zero. O que persiste é o que está escrito nos arquivos do projeto.
O plantonista novo só sabe o que está no prontuário.

---

O que o `/bigtech` faz?

[pausa]

Chama o Cósimo, que classifica o porte do projeto
e convoca o time certo para aquele tamanho.

---

O que é a coluna Onda na tabela?

[pausa]

O que pode rodar em paralelo sem conflito —
como procedimentos em salas cirúrgicas diferentes ao mesmo tempo.

---

O que é WSJF?

[pausa]

Custo de Atraso dividido pelo Tamanho do Trabalho.
A triagem de sala cirúrgica aplicada às tarefas do projeto.

---

Agora olha a primeira linha do TODO.md.

[mostrar o topo da tabela]

CHA₂DS₂-VASc.

Não fui eu que escolhi a próxima aula.
Foi o WSJF do seu projeto.

A triagem fez o trabalho.
Você só precisa executar."

---

## SEÇÃO 7: /TAB_PENDENCIAS + ENCERRAMENTO (3 min)

**Tom:** Fechamento de bloco — sensação de controle e clareza antes do próximo módulo

"Atualiza as pendências:

```
/tab_pendencias
```

[mostrar a tabela — aula_20 concluída, submódulo 04 fechado, submódulo 05 calculadoras como próximo]

---

Resumo do submódulo 04.

Você entrou com um residente.
Saiu como chefe de equipe.

O residente é o Claude Code — brilhante, incansável, erra com confiança, você assina o laudo.
A maleta é a stack de extensões — skills, MCPs, hooks, plugins.
O hospital é a BigTech Virtual — interconsulta com o especialista certo via `/bigtech`.
E a escala cirúrgica é a `/tab_pendencias` — WSJF ordenando o trabalho do time.

Você não precisa mais improviso.
Você tem protocolo.

---

Dever de casa.

A triagem da semana.

Abra o ClinMd-Tribe, rode `/tab_pendencias`
e olhe os dois itens no topo da tabela.

Responda em uma frase cada: por que esse subiu?
Qual foi o custo de atraso? Qual foi o tamanho do trabalho?

Não execute código. Só explique a triagem.

---

Na próxima aula: a primeira calculadora.

Você vai implementar o CHA₂DS₂-VASc no ClinMd-Tribe —
escore de risco de AVC em fibrilação atrial.

O WSJF escolheu.
O protocolo está pronto.
Na próxima aula você opera.

Até lá."

---

**FIM DO ROTEIRO**
