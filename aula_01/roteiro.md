# Aula 01 — O que é o Claude Code

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~50-55 min  
**Tom:** Colega com humor leve e didático — primeiro dia, criar confiança sem assustar  
**Analogia central:** CC = prontuário eletrônico | Web UI = post-it  

---

## SEÇÃO 1: ÂNCORA + O QUE É O CLAUDE CODE (M0.01) — 10 min

**Tom:** Abre com a dor real do médico — 60 segundos antes de qualquer tecnologia

"Você já ficou até meia-noite reformatando um relatório
que podia ter feito em 10 minutos?

Ou procurando aquela referência que sumiu do slide —
a que você tinha certeza que tinha salvo, mas sumiu?

Esta aula é sobre uma ferramenta que vai mudar isso.

E não precisa saber nada de computação para usar.

---

Antes de começar: eu uso Linux. Vocês usam Windows.

Isso é como dialeto de idioma — terminal é terminal,
Claude Code funciona igual nos dois sistemas.

Dito isso. Assunto encerrado. Nunca mais voltamos nesse tema.

---

Agora: o que é o Claude Code?

Vocês já conhecem o Claude.ai — aquele que você abre no navegador,
faz uma pergunta, ele responde.

Quero que vocês pensem nele como um post-it.

Você escreve uma coisa, ele responde, você fecha.
Post-it. Funciona pra uma pergunta rápida.

Mas post-it não tem memória. Post-it não sabe quem você é.
Post-it não sabe nada do seu projeto.
Toda conversa começa do zero.

---

O Claude Code é diferente.

O Claude Code é o prontuário eletrônico do seu projeto.

Tem histórico. Tem contexto. Você fecha às 23h,
abre no dia seguinte às 7h — ele sabe exatamente onde estava.
Sabe o que foi feito, o que está pendente, o que você pediu ontem.

E não só isso.

Claude Code **vê toda a estrutura do projeto**.
Você tem um app com 50 arquivos? Claude Code lê todos,
entende a relação entre eles, monta o quebra-cabeça.

Claude.ai Web? Não. Ele vê um arquivo por vez, como conversa isolada.

---

[mostrar na tela: Claude.ai aberto no navegador | Claude Code no terminal]

Mesma pergunta. Dois contextos diferentes.

Web UI: responde sua pergunta, fecha, sumiu.
Claude Code: responde sua pergunta, lembra, continua.

Post-it vs prontuário.

É por isso que este curso é Claude Code, não Web UI."

---

## SEÇÃO 2: PRIMEIRO CONTATO AO VIVO (M0.02) — 8 min

**Tom:** Prático, "vamos confirmar que está funcionando" — sem drama

"Na aula de abertura a gente instalou o Claude Code no computador.

Vamos confirmar que está tudo certo com um comando simples.

[abrir o terminal]

```
claude --version
```

[mostrar a versão aparecendo na tela]

Apareceu a versão? Perfeito. Instalação confirmada.

---

Agora: primeira conversa real.

[digitar no terminal]

```
claude
```

[aguardar o prompt aparecer]

Vou fazer uma pergunta clínica real — do tipo que você usaria no consultório.

[digitar o prompt]

```
Qual a diferença entre FA paroxística e persistente em termos de manejo?
```

[aguardar e mostrar a resposta]

---

Olha o que aconteceu.

Resposta estruturada, linguagem clínica, critérios de manejo.

Agora vou abrir o Claude.ai no navegador — a mesma pergunta.

[mostrar Web UI lado a lado na tela]

[digitar a mesma pergunta no Web UI]

O resultado é parecido. É o mesmo cérebro.

A diferença não está na resposta desta pergunta isolada.

A diferença está no que acontece quando você tem um projeto:
quando você tem arquivos, contexto, histórico.

Aí o prontuário bate o post-it por KO."

---

## SEÇÃO 3: O CICLO DE CONVERSA (M0.03) — 12 min

**Tom:** Didático com demo — cada passo demonstrado, não só explicado

"Agora que você viu o Claude Code respondendo,
precisa aprender a conversar com ele de forma eficiente.

O ciclo tem quatro passos.

Pedir. Anexar. Revisar. Iterar.

Cada um tem um propósito específico. Vou mostrar cada um ao vivo.

---

**Passo 1: Pedir.**

Você descreve o que quer em linguagem natural.
Não é código. Não é comando técnico.
É como você falaria com um colega.

[digitar no terminal]

```
Liste as principais causas de síncope no adulto
em ordem de probabilidade para o pronto-socorro,
com o sinal clínico diferenciador de cada uma.
```

[mostrar a resposta]

Pedido claro, resposta útil.

---

**Passo 2: Anexar.**

Quando você tem um arquivo — PDF, texto, planilha —
você passa para o Claude antes de pedir.

Vou usar um trecho de guideline público que preparei.

[mostrar o arquivo texto.txt na tela]

[anexar o arquivo na sessão]

```
Resumo este texto em 3 bullets para alunos de medicina.
```

[mostrar a resposta]

Claude leu o arquivo e resumiu com base no conteúdo dele.
Não inventou. Usou o que estava no arquivo.

---

**Passo 3: Revisar.**

Você avalia a resposta com olho clínico.

Está correto? Está completo? Está no tom certo?

Você é o responsável pelo laudo. Claude é o residente.
O residente faz — você assina.

[avaliar a resposta em voz alta]

'Aqui está bom. Aqui eu quero mais detalhe. Esse tom está formal demais.'

---

**Passo 4: Iterar.**

Se não ficou do jeito que você queria, você não desiste.
Você reformula o pedido.

[digitar no terminal]

```
Mais conciso. Foco em aplicação clínica no consultório.
Máximo 3 linhas por bullet.
```

[mostrar a nova resposta]

Compara antes e depois.

O Claude não mudou de opinião — você reformulou a instrução.

---

Frase que vou repetir várias vezes neste curso:

Você não troca de colega quando ele entendeu errado.
Você reformula o pedido.

Pedir. Anexar. Revisar. Iterar.
Esse ciclo é o núcleo de tudo que você vai fazer."

---

## SEÇÃO 4: BONS HÁBITOS + KATA DE PROMPT (M0.04) — 12 min

**Tom:** Revelar regras depois do aluno já ter visto o ciclo funcionando — mais concreto

"Você já viu o ciclo funcionando.

Agora: três regras que fazem a diferença entre uma resposta mediana
e uma resposta que você realmente usa.

---

**Regra 1: Dê contexto clínico sempre.**

Deixa eu mostrar a diferença.

[digitar no terminal]

```
Me fala sobre depressão.
```

[mostrar a resposta]

Genérico. Poderia ser para qualquer pessoa.
Você como psiquiatra com residentes na frente não usaria isso.

---

Agora com contexto:

[digitar no terminal]

```
Sou psiquiatra. Preciso preparar uma aula de 30 minutos
sobre diagnóstico de depressão para residentes de clínica médica.
Foco em critérios DSM-5 e quando encaminhar para psiquiatria.
Linguagem acessível para não especialistas.
```

[mostrar a resposta]

Compara.

A segunda resposta é o que você usaria. A primeira, não.

A diferença? Você deu contexto: quem você é, para quem é,
qual é o objetivo, qual é o nível do público.

O Claude não sabe nada disso até você falar.
É como pedir conduta sem dar anamnese.
Sem anamnese, a conduta vai ser genérica.

---

**Regra 2: Dado de paciente não entra. Nunca.**

Isso é LGPD. É ética médica. É bom senso.

Deixa eu mostrar o que NÃO fazer:

[mostrar na tela — não digitar no Claude]

```
João da Silva, 45 anos, RG 123456, nascido em 12/03/1980,
queixa de dor torácica há 2 horas...
```

Para. Nome, RG, data de nascimento — dados identificáveis.

Isso viola a LGPD e vai contra os termos de uso da ferramenta.

A versão correta:

[digitar no terminal]

```
Paciente do sexo masculino, 45 anos,
sem comorbidades conhecidas,
queixa de dor torácica há 2 horas com irradiação para membro superior esquerdo.
Qual o protocolo de triagem inicial no pronto-socorro?
```

[mostrar a resposta]

Mesmo resultado clínico. Zero dado identificável.

Isso vai aparecer em toda aula deste curso.
Vou repetir até vocês sonharem.

---

**Regra 3: Seja específico.**

O Claude é tão específico quanto você for.

Prompt vago: resposta vaga.
Prompt específico: resposta utilizável.

É lei de qualquer sistema médico: garbage in, garbage out.

[mostrar contraste rápido — prompt curto vs prompt com critérios]

---

Três regras. Contexto clínico. Zero dado de paciente. Seja específico.

**Dever de casa desta seção:**

Escreva 3 prompts sobre situações do seu dia a dia clínico.
Para cada um: a versão ruim e a versão melhorada.
Não precisa rodar. Só escrever.

Traga para a aula_02."

---

## SEÇÃO 5: CLAUDE CODE NO CELULAR + FECHAMENTO (M0.05) — 8 min

**Tom:** Prático, "isso vai mudar sua rotina entre consultas"

"Última parte.

Você está trabalhando num projeto. Projeto andando, contexto acumulado.
Aí você precisa sair — uma consulta, uma viagem, um deslocamento.

Não vai levar o notebook.

Você abre o Claude.ai no celular? Pode. Mas perdeu o contexto.
Nova conversa, sem os arquivos, sem o histórico.

Existe uma solução melhor.

---

[no terminal, digitar]

```
/remote
```

[mostrar o link gerado na tela]

Ele gerou um link temporário.

[abrir o link no celular, mostrar na câmera ou espelhar a tela]

Vou abrir no meu celular agora.

[acessar e mostrar a interface]

É o mesmo projeto. O mesmo contexto.
A sessão que estava rodando no computador.
De qualquer lugar, sem instalar nada no celular.

Isso é especialmente útil quando você está entre consultas
e quer continuar de onde parou.

---

**Resumo da aula_01:**

1. CC = prontuário eletrônico | Web UI = post-it
2. Ciclo: pedir → anexar → revisar → iterar
3. Três regras: contexto clínico / zero dado de paciente / seja específico
4. /remote: mesmo projeto, de qualquer lugar

Quatro coisas. Simples.

---

**Na próxima aula:**

Você vai usar o Claude Code com arquivos reais.

PDF clínico: resumir, extrair tabela, identificar vieses.
Planilha do consultório: organizar, limpar, gerar gráfico.
Slides: gerar apresentação a partir de tópicos soltos.

Você já sabe conversar.
Na aula_02 você começa a trabalhar.

Até lá."

---

**FIM DO ROTEIRO**
