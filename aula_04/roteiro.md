# Aula 04 — Flashcards Anki + Briefing Automático

**Formato:** Gravada no OBS Studio, editada no Kdenlive  
**Duração:** ~50 min  
**Tom:** Colega com humor leve e didático  

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Você providencia (material de terceiros):**

- [ ] O guideline da ADA "Standards of Care in Diabetes 2024", em PDF. Baixe do site oficial (diabetesjournals.org/care, seção Standards of Care) e deixe à mão. Não foi incluído no projeto por ter direitos autorais. Insumo da Seção 3.
- [ ] Anki instalado no computador. Baixe do site oficial (apps.ankiweb.net), gratuito. Insumo da Seção 3 (importação dos flashcards).

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta desta aula.
- [ ] Sessão limpa, sem conversa anterior carregada (a demo nasce do zero).
- [ ] Anki já aberto na tela, pronto para a importação ao vivo do `anki_dm2.txt` (gerado durante a aula).
- [ ] Conector MCP do PubMed ativo (reaproveitado da aula_03; o briefing das Seções 4 e 5 depende dele).

**Confira antes de gravar:**

- [ ] O PDF da ADA anexa e o Claude consegue lê-lo (faça um resumo de teste e descarte).
- [ ] Teste a importação no Anki uma vez: gere um `anki_dm2.txt` de ensaio, importe com separador ponto-e-vírgula e confirme que os cards entram, depois apague o deck de teste.
- [ ] Os arquivos `anki_dm2.txt` e `briefing_dm2.txt` são criados ao vivo pelo Claude; saiba em que pasta eles caem para abri-los na tela.
- [ ] Internet ativa (o briefing busca no PubMed em tempo real).

**Navegador:** nenhum site é obrigatório durante a gravação. Se quiser mostrar a página de download do Anki, abra a aba: https://apps.ankiweb.net

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Direto, conectando com aula_03, anunciando as duas entregas do dia

**[Aviso rápido dos óculos, antes de mergulhar]**

"Um segundo antes de a gente começar: hoje tem flashcard e tem terminal, e os dois adoram letra miúda. Quem precisa de óculos pra leitura, é agora, porque eu não quero ninguém forçando a vista feito residente lendo bula de plantão às 3 da manhã. Ajeitou? Então vamos."

"Na aula passada a gente foi ao PubMed, buscou artigos sobre fibrilação atrial,
triou por hierarquia de evidência e fez um fichamento completo com PICO, nível de
evidência e vieses.

Você saiu de lá com uma ficha pronta pra reunião clínica.

Hoje a gente vai um passo além.

Vamos pegar esse mesmo fluxo e transformar em duas coisas:
primeiro, uma ferramenta de estudo — flashcards no Anki, gerados automaticamente;
segundo, uma rotina de atualização que funciona sozinha, todo dia, sem você precisar
lembrar de nada.

Diabetes tipo 2 é o tema de hoje. Guideline da ADA.

Vamos lá."

---

## SEÇÃO 2: O CENÁRIO (3 min)

**Tom:** Situação real, pressão clínica com humor, duas necessidades claras

"Cenário.

Você decidiu fazer a prova de título em endocrinologia. Daqui a 3 meses.

Você tem dois problemas ao mesmo tempo:

Problema 1: você precisa dominar o conteúdo. Guideline da ADA, critérios diagnósticos,
alvos glicêmicos, escalonamento de terapia, complicações. É muita coisa pra decorar
só lendo uma vez.

Problema 2: a prova de título pede literatura atualizada. E o campo de DM2 publica
estudos novos toda semana. Você não tem 1 hora por dia pra varrer o PubMed.

O Anki resolve o problema 1.
O briefing automático resolve o problema 2.

E o Claude Code resolve os dois.

Vamos começar pelo Anki."

---

## SEÇÃO 3: DEMO — FLASHCARDS ANKI (15 min)

**Tom:** Didático, explicando o Anki antes da demo, depois mostrando passo a passo

"Antes de gerar os flashcards, deixa eu apresentar o Anki pra quem não conhece.

Anki é um aplicativo gratuito de repetição espaçada.

Repetição espaçada é uma técnica de memorização baseada em evidência:
você revisa cada card no momento certo — antes de esquecer, não depois.
É como fazer um esquema de reforço vacinal personalizado pra cada informação.

Você baixa no site oficial: apps.ankiweb.net. Gratuito, roda em Windows, Mac e Linux.

[mostrar o Anki aberto na tela]

O Anki importa cards em arquivo de texto simples — um card por linha,
frente e verso separados por ponto-e-vírgula.

Agora vamos gerar esses cards com o Claude Code.

Vou usar o guideline da ADA 2024 sobre Standards of Care in Diabetes.
É documento público, em PDF.

[mostrar PDF anexado]

Prompt:

```
Você é um especialista em educação médica e em diabetes.
Analise este guideline da ADA (Standards of Care in Diabetes 2024) e gere
20 flashcards para uma prova de título em endocrinologia.

Regras dos flashcards:
- Frente: pergunta clínica objetiva (como a prova vai perguntar)
- Verso: resposta concisa, máxima de 3 linhas
- Cobrir obrigatoriamente: critérios diagnósticos, alvos glicêmicos por perfil,
  primeira linha de tratamento, quando adicionar GLP-1 ou SGLT2, metas de HbA1c,
  triagem de complicações microvasculares
- Formato de saída: uma linha por card, frente;verso (separado por ponto-e-vírgula)
- Sem cabeçalhos, sem numeração, sem markdown — só as linhas de texto
```

[executar e mostrar resultado]

Olha o formato.

Cada linha é um card: pergunta, ponto-e-vírgula, resposta.
Exatamente o que o Anki precisa pra importar.

Agora vou salvar esse resultado em arquivo.

```
Salve o resultado acima em um arquivo chamado anki_dm2.txt na pasta atual.
```

[executar]

Pronto. Arquivo criado.

Agora importo no Anki:

[mostrar no Anki: Arquivo → Importar → selecionar anki_dm2.txt →
separador ponto-e-vírgula → importar]

Viu? 20 cards importados em 10 segundos.

Já pode começar a revisar hoje à noite."

---

## SEÇÃO 4: DEMO — BRIEFING MANUAL (8 min)

**Tom:** Prático, mostrando a construção de uma rotina reutilizável

"Agora o segundo problema: se manter atualizado sem perder horas toda semana.

A solução mais simples é ter um prompt pronto — você abre o Claude Code de manhã,
cola o prompt, e em 30 segundos tem o resumo das novidades da semana.

Vou criar esse prompt agora e salvar em arquivo pra reusar todo dia.

Prompt que vou usar:

```
Use o PubMed para buscar artigos sobre diabetes tipo 2 publicados nos últimos 7 dias.
Filtros: ensaios clínicos, metanálises, revisões sistemáticas ou guidelines.
Me retorne um briefing matinal com:
- Número de publicações encontradas
- Os 3 mais relevantes clinicamente: título, autores, revista, resumo em 2 bullets
- Uma frase final: 'O que muda na prática?' (ou 'Nada muda por enquanto' se não houver impacto)
Tom: direto, para especialista em endocrinologia.
```

[executar e mostrar resultado]

Isso é o briefing. Em 30 segundos.

Agora vou salvar esse prompt em arquivo pra não precisar redigitar todo dia:

```
Salve o prompt de briefing acima em um arquivo chamado briefing_dm2.txt na pasta atual.
```

[executar]

Toda manhã: você abre o terminal e digita uma linha só, que joga o conteúdo do
arquivo pra dentro do Claude no modo de uma resposta só (o `-p`, de 'print',
que faz ele responder e já sair, sem abrir a tela de conversa):

```
cat briefing_dm2.txt | claude -p
```

E ele executa o prompt e entrega o resumo.

Mas espera — isso ainda é manual. Vou mostrar como automatizar de verdade."

---

## SEÇÃO 5: DEMO — BRIEFING AUTOMÁTICO (12 min)

**Tom:** Técnico mas acessível, analogia com alarme de celular, mostrando Linux e Windows

"O prompt salvo já é uma melhora enorme. Mas você ainda precisa lembrar de rodar.

Vamos automatizar: o computador roda o briefing sozinho toda manhã às 7h
e salva o resultado em arquivo com a data do dia.

É como configurar o alarme do celular — você faz uma vez e ele dispara sozinho.

**No Linux (cron):**

Abro o terminal e digito:

```
crontab -e
```

Isso abre o agendador de tarefas do Linux.
Adiciono esta linha:

```
0 7 * * * cd ~/briefings && cat ~/briefing_dm2.txt | claude -p > briefing_$(date +%Y-%m-%d).txt 2>&1
```

[explicar lendo a linha em voz alta]

'0 7 * * *' significa: todo dia às 7h em ponto.
'cd ~/briefings' entra na pasta onde quero salvar.
'cat ~/briefing_dm2.txt | claude -p' joga o prompt no Claude no modo resposta-única.
'> briefing_2024-01-15.txt' salva o resultado com a data de hoje.

Salvo, fecho. Pronto.

[mostrar que o cron está ativo]

**No Windows (Task Scheduler):**

Vou no menu Iniciar, busco 'Agendador de Tarefas'.

[mostrar Task Scheduler aberto]

Clico em 'Criar Tarefa Básica'.
Nome: 'Briefing DM2'.
Disparador: diariamente, às 7h00.
Ação: iniciar programa.
Programa: `cmd.exe`
Argumentos:

```
/c "cd /d C:\Users\SeuNome\briefings && type C:\Users\SeuNome\briefing_dm2.txt | claude -p > briefing_%date:~-4,4%-%date:~-7,2%-%date:~0,2%.txt"
```

[configurar e salvar]

Pronto. Windows ou Linux — resultado igual.

Todo dia de manhã, antes de você acordar, o Claude já foi ao PubMed,
buscou as novidades, resumiu, e deixou o arquivo na pasta.

Você acorda, abre o arquivo, lê em 2 minutos, e está atualizado.

Um detalhe honesto pra não te frustrar: pra esse agendamento rodar sozinho de
madrugada, o Claude já precisa estar logado na sua máquina e o conector do PubMed
já instalado, que é o que a gente fez na aula passada. Você configura uma vez,
e depois ele trabalha enquanto você dorme.

Isso é o que eu chamo de medicina baseada em evidência automatizada."

---

## SEÇÃO 6: ENCERRAMENTO + DEVER DE CASA (5 min)

**Tom:** Motivador, resumo das duas entregas, desafio concreto

"Resumo do que a gente fez hoje.

Dois problemas reais do médico que estuda pra título — ou que só quer se manter
atualizado sem morrer afogado em literatura:

**Problema 1 — dominar o conteúdo:**
Anki com 20 flashcards gerados da guideline ADA, exportados em formato importável,
prontos pra revisar hoje à noite. Repetição espaçada, evidência sólida de retenção.

**Problema 2 — se manter atualizado:**
Briefing automático que roda sozinho todo dia às 7h, busca no PubMed,
resumo em 30 segundos, salvo em arquivo com a data do dia.

Tudo isso sem programar. Sem saber de cron. Sem saber de Task Scheduler.
Só descrevendo o que quer em linguagem natural.

Agora o dever de casa.

Pegue um tema da sua especialidade — pode ser o mesmo que você usou na aula_03
ou um novo — e faça isso:

```
Você é especialista em [SUA ESPECIALIDADE].
Analise este documento e gere 10 flashcards para revisão clínica.
Formato: frente;verso, uma linha por card, sem markdown.
```

Só 10 cards. Importe no Anki. Revise hoje.

Na próxima aula entramos no M3 — conteúdo, pesquisa e consultório.
Vamos aprender a criar posts e carrosséis para redes sociais,
newsletter com SEO, pôster de congresso e muito mais.

Até lá."

---

**FIM DO ROTEIRO**
