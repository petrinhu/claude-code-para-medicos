# Aula 01 — Windows, Linux, CLI vs Web UI e Bons Hábitos

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~30-35 min  
**Tom:** Colega com humor leve e didático  

---

## SEÇÃO 1: WINDOWS VS LINUX (3-5 min)

**Tom:** Descontraído, "não é tão diferente assim"

"Na aula de abertura a gente instalou no Windows e ficou lá.

Agora vou mostrar o meu Linux — porque eu uso Linux no dia a dia
e vocês vão me ver nele durante todo o curso.

Vocês olham e falam: 'Ué, mudou tudo?'

Não mudou não. Terminal é terminal. O conceito é idêntico.

Única coisa que muda é o NOME dos comandos e como o computador
organiza as pastas.

No Windows, vocês digitam 'dir'. No Linux, vocês digitam 'ls'.
Windows organiza pastas como `C:\Users\Petrus\Documents`.
Linux organiza como `/home/petrus/Documents`.

É tipo dois dialetos do mesmo idioma. Alemão e holandês —
parecem diferentes, mas o nativo entende os dois.

Por que as diferenças? Porque Windows é propriedade da Microsoft
e Linux é código aberto. Histórias diferentes.

**MAS** — e isto é importante — para o que vocês vão fazer com Claude Code,
não importa NADA qual sistema vocês usam.

Claude Code funciona igual no Windows, igual no Mac, igual no Linux.
O comando de instalação é o mesmo. O comando 'claude --version' é o mesmo.
O arquivo que vocês anexam funciona igual em qualquer um.

Então não se preocupem com isto. Vocês podem usar Windows,
vocês podem usar Mac, vocês podem usar Linux.
Eu usei todos os três, funciona em qualquer um.

Vocês vão aprender UMA VEZ e usar em qualquer máquina.

Próxima seção: CLI vs Web UI. Qual a diferença?"

---

## SEÇÃO 2: CLI VS WEB UI (5-7 min)

**Tom:** Prático, "Code é o profissional, Web UI é pra brincar"

"Agora vocês têm duas formas de usar Claude.

**FORMA 1: Claude Code** — terminal, CLI.
É o que a gente está aprendendo neste curso inteiro.

**FORMA 2: Claude.ai Web** — no navegador, conversinha simples.

Qual a diferença?

Claude.ai Web é tipo conversar com um colega no café.
Vocês fazem pergunta, ele responde. Conversinha, voltinha, tudo bem.

MAS — e isto é crítico — Web UI é quase incapaz de criar um app real.

Por quê? Porque app real é MODULAR. Tem vários arquivos, várias pastas,
dependências, testes, configuração. Não é um script simples.

Web UI não consegue navegar uma estrutura assim. Ela vê arquivo por arquivo,
mas não consegue orquestrar um projeto de 10, 20, 100 arquivos.

Claude Code consegue.

Claude Code faz o que? Claude Code **vê toda a estrutura do projeto**.
Vocês têm um app com 50 arquivos? Claude Code lê todos, entende
a relação entre eles, monta quebra-cabeça.

Claude Code **mantém contexto**. Ao longo de uma sessão, Claude lembra
de tudo que aconteceu — qual foi o bug que vocês tiveram,
qual foi a solução, como isto afeta outro arquivo.

Web UI? Não. Web UI é conversa desconectada. Vocês perguntam algo,
ela responde, vocês perguntam outra coisa, ela não lembra do contexto anterior.

Exemplo:
- **Web UI:** vocês pedem 'faz um código de login'. Ela faz um arquivo .py simples. Fim.
- **Claude Code:** vocês pedem 'faz um app com login, dashboard e relatórios'.
  Claude vê a arquitetura toda, cria 15 arquivos interconectados, testa tudo,
  e no final vocês têm um app que funciona de verdade.

Por isto este curso é Claude Code, não Web UI.

Web UI é pra você conversar, fazer perguntas rápidas, brincar.
Claude Code é pra você **construir coisas reais**.

E é isto que vocês vão aprender."

---

## SEÇÃO 3: CLAUDE CODE NO CELULAR — ACESSO REMOTO (5 min)

**Tom:** Prático, cenário real, mostrando uma solução elegante

"Agora que você entende a diferença entre CLI e Web UI,
deixa eu te mostrar um recurso que une os dois mundos.

Você tem um projeto acontecendo. Está no meio de algo importante.
Aí você precisa sair de casa, vai pra uma consulta, pra uma viagem,
e não vai levar o notebook.

O que você faz?

Você abre o Claude.ai no celular pelo navegador? Pode. Mas você perde o contexto
do projeto que está rodando no seu computador. É uma conversa nova, sem os arquivos,
sem o histórico.

Existe uma solução melhor.

O Claude Code tem um comando chamado /remote.

Você digita no terminal do seu computador:

```
/remote
```

Ele gera um link — tipo um link de acesso temporário.
Você abre esse link no celular, no navegador mesmo, e pronto:
você está dentro do seu Claude Code, com acesso ao projeto, aos arquivos,
ao contexto que estava rodando.

De qualquer lugar. Sem instalar nada no celular.

[mostrar ao vivo: rodar /remote, copiar link, abrir no celular e fazer um prompt simples]

Viu? É o mesmo projeto, o mesmo contexto, agora na tela do celular.

Isso é especialmente útil quando você está entre consultas e quer checar
como está o andamento de algo que o Claude estava processando,
ou quando surge uma ideia e você quer continuar de onde parou.

O computador continua rodando. Você acessa de onde estiver.

Simples assim."

---

## SEÇÃO 4: COMO CONVERSAR + BONS HÁBITOS DE PROMPT (10 min)

**Tom:** Didático, com analogia clínica e exemplo contrastante

"Agora vocês sabem instalar, abrir o terminal e a diferença entre Claude Code e Web UI.

Mas ainda falta o mais importante: como conversar com o Claude de forma que ele
entenda exatamente o que você quer.

Isso parece óbvio. Não é.

**O ciclo de uma boa conversa com o Claude tem 4 passos:**

Primeiro: **pedir**. Você descreve o que quer em linguagem natural — não é comando técnico,
não é programação. É como você falaria com um colega.

Segundo: **anexar**. Se você tem um arquivo — PDF, planilha, texto — arraste pro Claude
ou use o comando de anexar. Claude lê o arquivo antes de responder.

Terceiro: **revisar**. Você lê a resposta com olho clínico. Está correto? Está completo?
Está no tom certo? Você valida, como valida um resultado de exame.

Quarto: **iterar**. Se não ficou bom, você não desiste — você ajusta o pedido.
Mesma lógica de quando você manda um colega buscar algo e ele entendeu errado.
Você não troca de colega, você reformula o pedido.

Esse ciclo — pedir, anexar, revisar, iterar — é o núcleo de tudo que vocês vão fazer.

[pausa]

Agora: bons hábitos de prompt. Três regras de ouro.

**Regra 1: dê contexto clínico sempre.**

Compare esses dois prompts:

Prompt ruim: 'Me fala sobre depressão.'

Prompt bom: 'Você é um psiquiatra experiente. Preciso preparar uma aula de 30 minutos
sobre depressão para residentes de clínica médica. Foque em diagnóstico precoce
e quando encaminhar para psiquiatria. Use linguagem acessível para não especialistas.'

Qual resposta vai ser mais útil? A segunda. Sempre.

O Claude não sabe quem você é, pra quem você está fazendo, nem qual é o objetivo.
Você precisa falar. É como dar anamnese pro colega especialista antes de pedir conduta.
Sem anamnese, a conduta vai ser vaga.

**Regra 2: dado de paciente não entra. Nunca.**

Isso é LGPD, é ética médica, e é bom senso.

Se você quer analisar um caso, você anonimiza. Troca o nome, troca a data.
O Claude não precisa saber que é o João da sala 3 — ele precisa do quadro clínico.

Esse princípio vai aparecer em toda aula deste curso. Vou repetir até vocês sonharem.

**Regra 3: prompt vago, resposta vaga.**

O Claude é tão específico quanto você for.

Se você pede 'faça um resumo', ele vai fazer algum resumo.
Se você pede 'faça um resumo em 5 bullets para residentes de psiquiatria
com foco em critérios diagnósticos do DSM-5', ele vai fazer exatamente isso.

A qualidade da saída depende da qualidade da entrada.
É lei de qualquer sistema médico: garbage in, garbage out.

Três regras. Contexto clínico. Zero dado de paciente. Seja específico."

---

## SEÇÃO 5: ENCERRAMENTO (3 min)

**Tom:** Motivador, resumo rápido, próximos passos claros

"Pronto. Fim de papo da aula_01.

Deixa eu resumir o que a gente fez hoje:

1. Windows e Linux — mesma lógica, nomes diferentes. Claude Code funciona em qualquer um.
2. CLI vs Web UI — Code é o profissional, mantém contexto, constrói projetos reais.
   Web é pra brincar.
3. /remote — acesso ao projeto pelo celular, de qualquer lugar, sem perder contexto.
4. O ciclo de conversa — pedir, anexar, revisar, iterar.
5. As 3 regras de ouro — contexto clínico, zero dado de paciente, seja específico.

Agora vem a aula_02.

**AULA 2 — 'Assistente de Produtividade'** — a gente vai:
— Abrir o Claude Code de verdade pela primeira vez com um arquivo real
— Resumir um PDF clínico
— Gerar slides de aula a partir de um texto
— Analisar uma planilha do consultório
— Entender tokens, modelos e quando usar Haiku vs Sonnet

Se vocês tiverem dúvidas antes:
[canal de dúvidas — Discord, fórum, email]

Até a aula_02!"

---

**FIM DO ROTEIRO**
