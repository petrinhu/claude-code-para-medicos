# Aula 17 — Claude Code: Seu Residente de Plantão 24h

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~44 min  
**Tom:** Colega com humor leve e didático — aprofundar o que o aluno já usa sem perceber que usa errado

---

## SEÇÃO 1: ABERTURA — ORÁCULO VS RESIDENTE (3 min)

**Tom:** Dissonância produtiva — revelar o erro antes de ensinar o modelo certo

"Desde a aula_01 você usa o Claude Code.

Você pediu textos, criou código Python, montou interfaces Flet,
gerou a arquitetura completa do ClinMd-Tribe.

Mas deixa eu te fazer uma pergunta honesta:

Como você trata o Claude Code?

Como um oráculo — uma entidade que tem todas as respostas
e que você consulta esperando a verdade?

Ou como um residente — um profissional competente, treinado,
que executa o que você pede, comete erros e precisa de supervisão?

---

[abrir o Claude Code numa sessão nova]

Deixa eu mostrar a diferença.

Prompt:

```
Faz uma calculadora de escore clínico
```

[aguardar e mostrar o resultado]

O Claude entregou algo. Funciona? Talvez.
Está certo clinicamente? Não sei.

Ele não perguntou qual escore.
Não perguntou os critérios.
Não perguntou os pesos de cada item.

Mas respondeu com confiança, como se soubesse exatamente o que você queria.

Isso é o comportamento de oráculo.
E é o comportamento que vai te dar dor de cabeça.

---

Hoje a gente corrige isso.

Você vai entender o que o Claude Code é por dentro,
por que ele erra, o que ele lembra e o que esquece —
e como usar esse residente brilhante do jeito que ele foi feito pra ser usado."

---

## SEÇÃO 2: O QUE É UM LLM — ANALOGIA MÉDICA (7 min)

**Tom:** Conceitual — explicar o mecanismo sem tecnicalismo

"LLM. Large Language Model. Modelo de linguagem de grande escala.

Esse nome não ajuda muito. Então deixa eu traduzir.

---

Pensa num radiologista que leu 100 milhões de laudos.

Ele reconhece padrões com uma precisão que nenhum humano sozinho consegue.
Nódulo pulmonar com essa densidade, essa borda, esse tamanho —
ele já viu esse padrão dezenas de milhares de vezes.

Mas tem um detalhe importante:

Ele não tem um livro de respostas.
Ele tem padrões.

O laudo que ele escreve é a resposta mais provável
dado tudo que ele já viu.

---

O Claude Code funciona exatamente assim.

Ele foi treinado num volume imenso de texto —
código, documentação, artigos médicos, livros, fóruns.

Quando você escreve um prompt, ele não consulta um banco de dados de verdades.
Ele prevê: qual seria a próxima palavra mais provável?
Qual seria o próximo bloco de código mais provável?

Por isso ele 'sabe medicina' — leu o suficiente para reconhecer padrões.
Mas também pode inventar uma dose de remédio
que não existe em nenhuma diretriz.

Não é malícia. Não é descuido.
É o mecanismo.

---

O radiologista brilhante pode errar num caso atípico.
O Claude brilhante pode errar num pedido impreciso.

A diferença entre os dois e os que erram mais?
O contexto que você fornece.

Laudo bom vem de clínica boa.
Código bom vem de prompt bom."

---

## SEÇÃO 3: CONTEXTO E MEMÓRIA — TROCA DE PLANTÃO (6 min)

**Tom:** Prático — explicar o que persiste e o que some

"Segunda coisa que você precisa entender: o que o Claude lembra.

---

Pensa na memória de trabalho de um plantonista.

Você entra às 7h. Recebe 12 pacientes.
Durante aquele plantão, você lembra de tudo:
o paciente do leito 4 que teve febre às 10h,
a evolução do pós-operatório do leito 7,
o resultado de gasometria que veio às 14h.

Às 19h o plantão passa.
O plantonista que entra sabe o quê?

Só o que está escrito no prontuário.

---

O Claude Code funciona exatamente igual.

Dentro de uma sessão — enquanto você está no mesmo terminal, no mesmo chat —
ele lembra tudo que foi dito.
Cada arquivo que você mostrou. Cada código que ele gerou. Cada correção.

Quando a sessão termina ou você abre uma nova janela,
o plantonista novo entra.

Ele não sabe nada do plantão anterior.

O que ele sabe? O que está escrito nos arquivos do projeto.
O CLAUDE.md, o main.py, os arquivos da Clean Architecture.
Esse é o prontuário.

---

Por isso o CLAUDE.md existe no projeto.

Ele é o resumo de admissão. O que o próximo plantonista precisa saber
antes de começar a trabalhar.

E existe um comando para chamar um plantonista novo
no meio do turno:

```
/clear
```

[executar /clear no terminal]

Contexto limpo. O Claude não lembra mais de nada do que foi dito nesta sessão.
Útil quando a conversa ficou longa e confusa,
quando você quer recomeçar sem vieses do histórico."

---

## SEÇÃO 4: POR QUE O CLAUDE ERRA (5 min)

**Tom:** Calibrar expectativa sem minar confiança — você é o atestante final

"Você já conhece um colega assim.

Aquele que quando você pergunta qualquer coisa,
responde imediatamente, com segurança absoluta.

Às vezes está certo.
Às vezes está completamente errado.
Mas o tom é sempre o mesmo.

---

O Claude tem esse comportamento.

Ele não sabe que não sabe.
Não existe incerteza explícita na resposta dele
a não ser que você peça.

Ele não vai dizer 'olha, não tenho certeza sobre essa dose'.
Vai responder com a mesma confiança que usa quando sabe com certeza.

---

Isso não é um defeito que vai ser corrigido.
É uma característica do mecanismo.

Então como lidar?

A mesma regra que você aplica no trabalho:
você não assina um laudo sem revisar.

O Claude é o aparelho que gerou o resultado.
Você é o médico que assina.

---

E quando você suspeitar que tem algo errado, use isso:

```
Revise a resposta anterior. Algum dado clínico pode estar incorreto?
```

[mostrar o Claude revisando e encontrando um erro]

Peça a revisão antes de aceitar.
Especialmente para qualquer coisa com dado numérico clínico:
dose, escore, critério diagnóstico.

O residente bom é o que você treina para ter dúvida.
E o treino começa no seu prompt."

---

## SEÇÃO 5: DEMO A/B — PROMPT RUIM VS BOM (8 min)

**Tom:** Demonstrar — o delta visível entre os dois resultados é o professor

"Agora o momento mais importante da aula.

Vou fazer o mesmo pedido clínico duas vezes.
Você vai ver a diferença.

[abrir sessão nova no Claude Code — fora da pasta do ClinMd-Tribe]

---

Prompt ruim:

```
faz uma calculadora de escore cardíaco
```

[aguardar e mostrar o resultado]

O Claude entregou alguma coisa.
Olha o que ele fez: inventou os itens, inventou os pesos,
pode ter misturado critérios de escores diferentes.

Funciona? Provavelmente.
Está clinicamente correto? Não dá pra saber sem revisar tudo.

---

Agora o mesmo pedido, do jeito certo.

Prompt bom:

```
Cria uma função Python chamada calcular_cha2ds2vasc.
Ela recebe os seguintes parâmetros:
- fibrilacao_atrial: booleano
- avc_previo: booleano
- has: booleano
- diabetes: booleano
- icc: booleano
- sexo_feminino: booleano
- idade: inteiro

Retorna o escore total com esta pontuação:
- avc_previo: 2 pontos
- idade maior que 75: 2 pontos
- idade entre 65 e 74: 1 ponto
- has, diabetes, icc, sexo_feminino: 1 ponto cada

Inclua um exemplo de chamada com valores fictícios.
Sem interface gráfica — só a função.
```

[aguardar e mostrar o resultado]

---

Olha a diferença.

O segundo tem os itens certos. Os pesos certos.
É testável — você sabe exatamente o que entra e o que sai.

O que mudou?

Você descreveu o resultado clínico, não o código.
Você especificou os tipos de dado.
Você disse o que não queria: 'sem interface'.

Você foi o médico que passou o caso.
O residente executou o protocolo.

Esse é o padrão para qualquer prompt de código clínico:
descreva o resultado que você quer ver,
não a solução que você imagina."

---

## SEÇÃO 6: DEMO CLI VS WEB — LENDO ARQUIVOS (5 min)

**Tom:** Revelar o diferencial concreto do Claude Code sobre o Claude.ai web

"Uma coisa que o Claude.ai no navegador não consegue fazer.

[entrar na pasta do ClinMd-Tribe e abrir o Claude Code]

```
cd Documents\projetos\clinmd-tribe
claude
```

Prompt:

```
Leia os arquivos presentation/tela_inicial.py, application/orquestrador.py,
domain/calculadoras.py e infrastructure/armazenamento.py.
Me diga qual camada ainda não tem nenhuma lógica clínica implementada.
```

[aguardar e mostrar o resultado]

O Claude leu os 4 arquivos. Cruzou o conteúdo. Respondeu com precisão.

No Claude.ai web isso é impossível —
ele não tem acesso aos arquivos do seu computador.

O Claude Code CLI lê, escreve e navega no projeto inteiro.
Esse é o diferencial que justifica usar o terminal.

---

Conforme o ClinMd-Tribe crescer — mais arquivos, mais camadas,
mais calculadoras implementadas —
você vai usar esse padrão constantemente:

```
Leia [arquivo X] e [arquivo Y] e me diga [o que você quer saber]
```

O residente que lê o prontuário antes de fazer a visita
é infinitamente mais útil do que o que entra no quarto sem contexto."

---

## SEÇÃO 7: LGPD COMO SKILL DE PROMPT (4 min)

**Tom:** Prático — ensinar a anonimizar como técnica, não como palestra

"LGPD.

Em toda aula você ouviu: dado de paciente não entra no Claude Code.

Hoje você aprende como fazer isso na prática.

---

Existe uma técnica simples que resolve o problema
e preserva todo o contexto clínico que você precisa.

O padrão de anonimização.

Em vez de:

```
Paciente João Silva, 64 anos, CPF 123.456.789-00,
internado em 15/03, com FA e HAS. Dr. Petrus, CRM 12345.
```

Use:

```
Paciente fictício: 64 anos, sexo masculino, FA + HAS.
Sem nome real, sem CPF, sem data real.
```

O contexto clínico está inteiro.
A identidade está protegida.

---

[mostrar os dois prompts lado a lado no Claude Code]

Prompt com dado real — resultado idêntico ao anonimizado.
A qualidade do código não muda.
O risco clínico e legal é completamente diferente.

---

Incorpore esse padrão como reflexo.
Antes de qualquer prompt clínico, uma pergunta:

'Tem algum dado que identifica uma pessoa real aqui?'

Se sim, substitua por dado fictício equivalente.

O Claude não precisa saber que o paciente é o João.
Ele precisa saber que é um homem de 64 anos com FA e HAS.
Isso é suficiente para um prompt excelente."

---

## SEÇÃO 8: /CLEAR E /HELP (3 min)

**Tom:** Referência prática — dois comandos de higiene de sessão

"/clear você já viu — troca de plantonista no meio do turno.

Quando usar:
— a conversa ficou longa e confusa
— você quer começar um assunto novo sem o contexto anterior interferindo
— o Claude começou a repetir soluções que não funcionaram

```
/clear
```

[executar e mostrar que o histórico some]

---

/help é o manual do residente.

```
/help
```

[mostrar o output]

Lista o que o Claude Code consegue fazer nesta sessão:
comandos disponíveis, capacidades, atalhos.

Consulte quando não souber se existe um comando para o que você quer.

---

Esses dois fazem parte da higiene de sessão.
Como lavar as mãos antes de um procedimento —
não são obrigatórios em cada momento,
mas quando você precisa, precisa."

---

## SEÇÃO 9: /TAB_PENDENCIAS + ENCERRAMENTO (3 min)

**Tom:** Registro canônico e ponte para a aula_18

"Atualize as pendências:

```
/tab_pendencias
```

[mostrar a tabela — aula_17 concluída, aula_18 MCP/Skills/Hooks/Plugins como próxima]

---

Resumo do que ficou claro hoje.

O Claude Code é um residente brilhante e incansável.
Lê rápido, escreve rápido, nunca reclama do plantão duplo.
Mas chuta com confiança — e você assina o laudo.

LLM é o radiologista de 100 milhões de laudos: padrões, não verdades.

Contexto é a memória do plantão: some quando a sessão termina,
persiste só no que está escrito nos arquivos.

Prompt bom descreve o resultado clínico — não o código.

LGPD é uma skill de prompt: dado fictício, contexto clínico preservado.

---

Dever de casa.

Escolha um pedido clínico que você faria ao Claude Code.
Escreva três versões:

A primeira do jeito que você escreveria hoje — sem pensar.
A segunda um pouco mais específica.
A terceira com todos os elementos: resultado descrito,
tipos de dado, sem dado real, sem ambiguidade.

Execute as três e compare os resultados.

Não é exercício de código — é exercício de comunicação com o residente.

---

Na próxima aula: MCP, Skills, Hooks e Plugins.
Você vai entender como estender o bisturi do Claude Code —
como ele se conecta a ferramentas externas,
como as skills do curso funcionam por dentro,
e como os hooks automatizam ações no seu projeto.

Até lá."

---

**FIM DO ROTEIRO**
