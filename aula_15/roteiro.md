# Aula 15 — Clean Architecture: Quem Decide o Quê no Plantão

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~46 min  
**Tom:** Colega com humor leve e didático — o conceito que organiza tudo que vem depois

---

## SEÇÃO 1: ABERTURA — O CÓDIGO EMBOLADO (5 min)

**Tom:** Gancho da dor — mostrar o problema antes de nomear a solução

"Você tem uma calculadora de IMC funcionando.
Botão roxo, campos de peso e altura, resultado na tela.

Agora imagina que saiu uma diretriz nova da ABESO:
obesidade grau 2 agora começa em IMC > 35, e grau 3 em IMC > 40.

Fácil, certo? Você pede ao Claude Code:

```
No main.py da calculadora de IMC, muda o critério de obesidade grau 2
para IMC > 35 e adiciona obesidade grau 3 para IMC > 40.
```

[aguardar o Claude atualizar]

[mostrar o código modificado]

Olha o que aconteceu.

O Claude mexeu num bloco de código. Mas esse bloco fica onde?
No meio do handler do botão. Junto com o código que verifica se o campo
está vazio. Junto com o código que decide a cor do texto de resultado.

Você quer mudar uma regra clínica — e precisa navegar por código de interface.

---

Isso tem um nome: código embolado.

É o equivalente a um prontuário onde a anamnese, a prescrição e a
conta do hospital estão escritas no mesmo parágrafo.

Você quer mudar a prescrição. Mas pra achar ela, precisa ler o prontuário inteiro.
E se você editar no lugar errado, a conta sai com dados da anamnese.

Desenvolvimento de software com código embolado é exatamente isso.
Funciona. Mas é frágil. Cada mudança é um risco.

Existe uma solução para isso.
Ela tem um nome.
E é o que a gente vai aprender hoje."

---

## SEÇÃO 2: PONTE DA ANALOGIA — DO CORPO AO PLANTÃO (3 min)

**Tom:** Transição narrada — upgrade pedagógico, não contradição

"Lá na aula de setup eu dei a foto rápida de como o ClinMd-Tribe vai se organizar.

Apresentação, Aplicação, Domínio, Infraestrutura.
E eu usei a analogia do corpo: pele, tecido, músculo, osso.

Essa analogia foi boa pra mostrar que existem camadas empilhadas.
Serviu pra isso.

Hoje a gente troca ela.

Porque arquitetura não é sobre empilhamento — é sobre FLUXO.
Quem chama quem. Quem decide o quê. Quem pode mudar sem quebrar o resto.

E para fluxo, a melhor analogia não é o corpo.

É o plantão hospitalar.

---

Plantão hospitalar tem papéis. Cada papel tem responsabilidade definida.
O fluxo é direcional: o paciente entra, percorre o sistema, sai com diagnóstico e conduta.

É exatamente como o código vai funcionar no ClinMd-Tribe.

| Camada | Plantão | O que faz |
|--------|---------|-----------|
| **Apresentação** | Recepção / balcão | Recebe o paciente, mostra a tela, coleta o que foi digitado. Não decide nada clínico. |
| **Aplicação** | Enfermagem de triagem | Orquestra: pega o pedido, aciona quem precisa, organiza a ordem. Não é dona da regra. |
| **Domínio** | O médico / protocolo clínico | A regra de decisão pura: o escore, o critério. Não sabe se há tela ou banco de dados. |
| **Infraestrutura** | Laboratório / arquivo / farmácia | Guarda no disco, busca no banco, lê PDFs. Executa pedidos, não pensa. |

A regra de ouro da arquitetura: a dependência aponta para dentro.

O protocolo clínico — o Domínio — existe independente de tela ou banco.
Você pode trocar a recepção sem mudar o protocolo.
Você pode trocar o laboratório sem mudar o diagnóstico.

Isso é a Clean Architecture."

---

## SEÇÃO 3: AS 4 CAMADAS NO PLANTÃO — UM FIO NARRATIVO (9 min)

**Tom:** Didático — um único caso percorrendo as 4 camadas do início ao fim

"Vamos seguir um caso clínico real pelo sistema.

O caso: calcular o CHA2DS2-VASc de um paciente com fibrilação atrial.

---

**Passo 1 — O paciente chega na Recepção (Apresentação).**

O formulário aparece na tela.
Campos: idade, fibrilação atrial, AVC prévio, HAS, diabetes, ICC, sexo feminino.

A Recepção coleta os dados. Não calcula nada.
Não sabe o que é um escore. Não sabe onde os dados vão ser salvos.
Só recebe e exibe.

---

**Passo 2 — A Triagem recebe os dados (Aplicação).**

O botão 'Calcular' é clicado. A Triagem acorda.

Ela pega os dados do formulário, chama o protocolo CHA2DS2-VASc,
pede para o Laboratório salvar o resultado depois.

A Triagem orquestra. Ela não sabe calcular o escore.
Ela sabe quem sabe — e aciona.

---

**Passo 3 — O Médico calcula (Domínio).**

O protocolo CHA2DS2-VASc entra em ação.

Idade > 75 anos: 2 pontos.
AVC ou TIA prévio: 2 pontos.
Idade entre 65 e 74: 1 ponto.
HAS, diabetes, ICC, sexo feminino: 1 ponto cada.

O Médico calcula. Devolve o escore para a Triagem.

Ele não sabe se há uma janela bonita ou um terminal feio.
Não sabe se o resultado vai para um arquivo ou para um banco de dados.
Só sabe medicina.

---

**Passo 4 — O Laboratório guarda (Infraestrutura).**

A Triagem pede: 'salva esse resultado'.
O Laboratório abre o arquivo local, salva, confirma.

Ele não sabe calcular escore.
Não sabe o que é fibrilação atrial.
Só executa o pedido.

---

Agora: voltando ao problema da diretriz nova.

Mudou a diretriz: idade > 75 agora vale 2 pontos em vez de 1.

Onde você mexe?

Só no Médico — no Domínio.

A Recepção não sabe que existiu mudança.
A Triagem continua orquestrando do mesmo jeito.
O Laboratório continua salvando do mesmo jeito.

Apenas o protocolo clínico mudou.

Isso é o que a arquitetura em camadas compra para você."

---

## SEÇÃO 4: MAPA DE ARQUITETURAS — DO MONÓLITO AO MICROSSERVIÇO (9 min)

**Tom:** Contextual — situar o Clean Architecture no landscape, não decorar definições

"Antes de seguir, deixa eu mostrar o mapa completo.

Porque Clean Architecture não é a única forma de organizar código.
É uma entre várias. E cada uma faz sentido num contexto diferente.

---

**Monolítico — o consultório solo.**

O médico faz tudo: atende, receita, cobra, arquiva.
Funciona quando há poucos pacientes. Quando cresce, vira caos.

No código: tudo num único arquivo ou projeto.
Funciona? Sim. Mas mudar uma coisa pode quebrar outra.

Ainda faz sentido hoje? Sim — scripts de automação interna,
ferramentas de uso próprio, MVPs de validação rápida.
O problema não é o monólito. É usar monólito num projeto que vai crescer.

---

**3 camadas — a clínica simples.**

Recepção, consultório, farmácia.
Separação básica, mas a regra clínica ainda fica misturada no 'consultório'.

No código: front-end, back-end, banco de dados.
O padrão mais comum na web. Funciona bem para sistemas de tamanho médio.

---

**4 camadas + Foundation — o hospital completo.**

Balcão, triagem, médico, laboratório.
É o que usamos. Apresentação, Aplicação, Domínio, Infraestrutura.

Clean Architecture é o refinamento desse modelo:
coloca o Domínio no centro, torna explícito que as dependências
apontam sempre para dentro.

---

**Hexagonal — o hospital com múltiplas entradas.**

O mesmo hospital, mas com pronto-socorro, ambulatório e telemedicina
como entradas intercambiáveis.

No código: você pode trocar a interface Flet por uma API REST
sem mudar uma linha do Domínio.
Mais poderoso — e mais abstrato. Dificulta para iniciantes.

---

**Microsserviços — a rede hospitalar.**

Oncologia, cardiologia e ortopedia como hospitais separados
que se comunicam por protocolos.

No código: cada parte do sistema é um serviço independente.
Necessário para sistemas de grande escala com múltiplos times.

Para o ClinMd-Tribe? Over-engineering.
A complexidade de coordenação seria maior que o benefício.

---

Por que Clean Architecture para o ClinMd-Tribe?

Porque os protocolos clínicos — CHA2DS2-VASc, PHQ-9, GAD-7 —
precisam ser isolados, testáveis e independentes de interface.

Quando a diretriz muda, só o protocolo muda.
Quando o layout muda, o protocolo não sabe.

Essa independência é o que torna o app seguro de manter."

---

## SEÇÃO 5: RECUPERAÇÃO ATIVA (3 min)

**Tom:** Consolidação — o aluno verbaliza antes de aplicar

"Fecha a tela por um momento.

Três perguntas rápidas.

**Primeira: o que faz a Triagem — a camada de Aplicação?**

[pausa]

Orquestra o fluxo. Pega os dados da tela, aciona o protocolo,
pede para salvar. Não decide a conduta clínica.

**Segunda: o que o Médico — o Domínio — sabe fazer?**

[pausa]

O protocolo clínico puro. O cálculo do escore.
Não sabe se há interface gráfica ou terminal.
Não sabe onde os dados vão ser salvos.

**Terceira: o Laboratório — a Infraestrutura — calcula o CHA2DS2-VASc?**

[pausa]

Não. O Laboratório só executa pedidos de armazenamento e busca.
Calcular escore é trabalho do Médico.

---

Três respostas. Você acabou de descrever Clean Architecture
sem precisar de definição formal."

---

## SEÇÃO 6: JOGO — EM QUE CAMADA EU MEXO? (10 min)

**Tom:** Prática ativa — o aluno classifica antes de ver a resposta

"Agora a parte mais importante da aula.

Cinco pedidos clínicos reais. Para cada um você vai dizer:
em que camada eu mexo — e por quê?

Classifique antes de eu revelar.

---

**Pedido 1:** 'Quero o botão Calcular em roxo escuro em vez de roxo claro.'

[pausa para o aluno classificar]

**Apresentação.** A cor do botão é responsabilidade do balcão — da recepção.
O protocolo clínico não sabe que o botão existe.

---

**Pedido 2:** 'Saiu nova diretriz: no CHA2DS2-VASc, idade > 75 agora vale 2 pontos.'

[pausa]

**Domínio.** É exatamente a dor do gancho desta aula.
A regra clínica mudou — só o Médico precisa saber disso.
Recepção, Triagem e Laboratório não mudam uma linha.

---

**Pedido 3:** 'Quero que o resultado do cálculo seja salvo num arquivo TXT no Desktop.'

[pausa]

**Infraestrutura.** Onde e como salvar é responsabilidade do Laboratório.
O Médico não precisa saber se é TXT, SQLite ou PDF.

---

**Pedido 4:** 'Ao salvar o resultado, quero que apareça uma mensagem de confirmação na tela.'

[pausa — este é propositalmente ambíguo]

**Aplicação + Apresentação.**

A Triagem orquestra: 'ao salvar com sucesso, peça à Recepção para exibir a confirmação.'
A Recepção exibe o texto de confirmação.

Dois papéis. Um fluxo.

Não existe resposta errada aqui — o importante é entender que
salvar e exibir confirmação são responsabilidades separadas que se coordenam.

---

**Pedido 5:** 'Quero adicionar o PHQ-9 ao app, do lado do CHA2DS2-VASc.'

[pausa]

**Atravessa tudo.**

Apresentação: novo formulário com os campos do PHQ-9.
Aplicação: nova orquestração para o fluxo do PHQ-9.
Domínio: o protocolo do PHQ-9 com seus critérios e pontuação.
Infraestrutura: salvar o resultado do PHQ-9 junto com o do CHA2DS2-VASc.

Features grandes tocam o sistema inteiro. E tá tudo bem.
Cada camada sabe o que é sua responsabilidade.

---

Uma saída honesta para quando você não sabe a camada certa:

Descreva a feature em linguagem clínica e pergunte diretamente ao Claude Code:

```
Em que camada da Clean Architecture fica a feature de [descreva aqui]?
Por que essa camada e não outra?
```

O Claude explica. Você valida. Você aprende.
Não saber a camada de cabeça é normal — saber como descobrir é o skill."

---

## SEÇÃO 7: MINI-DEMO — PROMPT AO CLAUDE CODE (5 min)

**Tom:** Conectar conceito ao uso real — o mapa de referência do projeto

"Agora vamos registrar essa estrutura no projeto.

No Claude Code:

```
Cria um arquivo chamado arquitetura.txt mostrando a estrutura de pastas
do ClinMd-Tribe com as 4 camadas da Clean Architecture.
Para cada pasta, adiciona um comentário explicando o que vai ali.
Use nomes em inglês com comentários em português.
```

[aguardar o Claude gerar o arquivo]

[mostrar o conteúdo do arquitetura.txt]

O Claude gerou algo parecido com isso:

```
clinmd-tribe/
  presentation/     # telas Flet: botões, campos, janelas, AppBar
  application/      # orquestração: lê tela, chama domínio, pede pra salvar
  domain/           # regras clínicas: CHA2DS2-VASc, PHQ-9, critérios diagnósticos
  infrastructure/   # arquivos, banco de dados SQLite, indexação de PDFs
```

Guarde esse arquivo.

Na próxima aula, esse mapa vai se tornar código real.
O Claude Code vai gerar o scaffold completo do ClinMd-Tribe —
as pastas, os arquivos-base de cada camada, a estrutura que vai
sustentar todas as calculadoras, o anotador e o RAG.

---

Veja as pendências do projeto:

```
/tab_pendencias
```

[mostrar a tabela — Clean Architecture conceitual como concluído,
scaffold do ClinMd-Tribe como próxima tarefa]

E consulte o Caetano para validar a escolha arquitetural:

```
@caetano-cto, vamos usar Clean Architecture com 4 camadas
(presentation, application, domain, infrastructure) para o ClinMd-Tribe.
Essa estrutura é adequada para um app clínico local em Python + Flet?
```

[mostrar a validação do Caetano]"

---

## SEÇÃO 8: ENCERRAMENTO (2 min)

**Tom:** Síntese pelo aluno, motivação e dever de casa

"Resumo do que ficou pronto hoje.

Você entendeu por que separar o código em camadas —
não como teoria, mas como solução para um problema que você viu acontecer.

Você conheceu a analogia do plantão:
recepção, triagem, médico, laboratório.

Você posicionou o Clean Architecture no mapa de seis abordagens —
do monólito ao microsserviço.

E você jogou o jogo das cinco features — classificando onde cada mudança mexe.

---

Dever de casa.

Pensa numa feature que você quer no ClinMd-Tribe —
não precisa ser técnica, pode ser clínica.

Escreve no papel ou num arquivo de texto:
em qual das quatro camadas essa feature mexe, e por quê.

Depois escreve o prompt que você daria ao Claude Code
para pedir essa feature sabendo a camada.

Na próxima aula: o scaffold real.
O Claude Code vai gerar a estrutura completa de pastas e arquivos
do ClinMd-Tribe — e você vai ver o arquitetura.txt desta aula
se tornar código vivo.

Até lá."

---

**FIM DO ROTEIRO**
