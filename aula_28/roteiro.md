# Aula 28 — PubMed → knowledge_base/ → Banco Vetorial

**Formato:** Gravada em um take no OBS Studio
**Duração:** ~55 min
**Tom:** Cardiologista que transforma sua biblioteca de artigos em memória do app
**Módulo:** S07.02 — Construindo a Biblioteca do Residente

---

## SEÇÃO 1: ABERTURA — BRIDGE COM AULA_03 — 5 min

**Tom:** Reconhecimento de conquista passada — o aluno já usou o MCP do PubMed; hoje esse mesmo MCP alimenta o app

"Na aula 03 você usou o MCP do PubMed pela primeira vez.

Lembra o que você fez?

Digitou uma pergunta em português.
O Claude Code foi até o PubMed, trouxe artigos, resumiu, referenciou.

Era pesquisa.
Você estava estudando.

---

Hoje o mesmo MCP vai fazer algo diferente.

Não vai trazer artigos para você ler.
Vai trazer artigos para o app ler.

A diferença é enorme.

---

Quando um residente começa o plantão,
ele não pesquisa do zero cada decisão que vai tomar.

Ele tem memória.
Anos de leitura, cursos, casos vistos.

O ClinMd-Tribe ainda não tem isso.

Hoje ele vai ter.

---

A estrutura é simples.

Uma pasta chamada `knowledge_base/`.
Cada arquivo `.txt` dentro dela é um artigo que o residente 'leu'.

Ao final desta aula, o app vai ter lido três artigos sobre anticoagulação em fibrilação atrial.

Amanhã — na aula 29 — você vai fazer a primeira pergunta a ele.

Mas antes de perguntar, ele precisa ter estudado.

Isso é o que fazemos hoje."

---

## SEÇÃO 2: PROMPT DE DOWNLOAD — 12 min

**Tom:** Professor conduz ao vivo — mostrar o prompt, executar, ver os arquivos nascerem

"Antes de digitar, abra o terminal na raiz do projeto.

Verifique que a pasta `knowledge_base/` existe.
Se não existir, o Claude vai criá-la — mas é bom confirmar.

**[TELA: mostrar o terminal na raiz do projeto ClinMd-Tribe]**

---

Agora o prompt.

Vou ler cada parte antes de enviar.

[ler em voz alta e digitar]

```
Busque 3 artigos sobre anticoagulação em fibrilação atrial no PubMed.
Para cada artigo encontrado:
  - Salve o texto completo em knowledge_base/<pmid>_<titulo_curto>.txt
  - Se o texto completo não estiver disponível, salve título + abstract + PMID
  - O nome do arquivo deve ser seguro (sem caracteres especiais, espaços substituídos por _)
Ao final, liste os arquivos criados com o tamanho de cada um.
```

---

[enviar o prompt ao Claude Code]

**[TELA: mostrar o Claude Code buscando — MCP do PubMed em ação]**

Repare que o Claude não está abrindo o navegador.
Ele está usando o MCP do PubMed diretamente — a mesma integração da aula 03.

A diferença é o destino.
Na aula 03, o resultado foi para o chat.
Agora, o resultado vai para arquivos.

---

[aguardar conclusão]

O output esperado vai ser algo assim:

```
Arquivos criados em knowledge_base/:
  39123456_anticoagulation_fa_guidelines_2023.txt   (42 KB)
  38765432_warfarin_vs_noac_systematic_review.txt   (38 KB)
  40234567_af_stroke_prevention_meta_analysis.txt   (51 KB)
```

**[NOTA DE PRODUÇÃO: anotar os nomes e tamanhos reais dos arquivos antes de gravar — os nomes acima são exemplos]**

---

Agora abra um dos arquivos.

**[NOTA DE PRODUÇÃO: confirmar que o VS Code está instalado e o comando `code` está no PATH antes de gravar. Alternativa se não estiver disponível: abrir o arquivo pelo explorador de arquivos, ou usar `cat knowledge_base/<nome_do_arquivo>.txt | head -60` no terminal.]**

```
code knowledge_base/39123456_anticoagulation_fa_guidelines_2023.txt
```

**[NOTA DE PRODUÇÃO: usar o nome real do primeiro arquivo criado]**

**[TELA: mostrar o conteúdo do .txt — parágrafos de texto médico em inglês]**

Título.
Abstract.
Introdução.
Métodos.
Resultados.
Conclusão.

Texto médico real.
Em inglês, como está no PubMed.

Isso é o que o app vai indexar."

---

## SEÇÃO 3: VER OS .TXT CRIADOS — A BIBLIOTECA EXISTE — 3 min

**Tom:** Pausa para deixar o momento assentar — contraste com as aulas anteriores

"Três arquivos.
Três artigos.
Sobre anticoagulação em FA.

Pause por um segundo.

---

Nas últimas aulas — calculadoras, dashboard, formulários —
você era o autor dos dados.

Você digitava a bilirrubina.
Você digitava a receita do consultório.

Aqui foi diferente.

Você não digitou nenhum dado.
O Claude Code foi buscar o conhecimento.
O MCP do PubMed entregou os artigos.
Os arquivos foram criados.

A biblioteca existe.

---

Mas ela existe como texto.
Parágrafos e mais parágrafos.

Para que o app consiga responder perguntas baseado nesses artigos,
ele precisa transformar esse texto em outra coisa.

Em vetores.
Em memória pesquisável.

Isso se chama indexação.

E é o que fazemos agora."

---

## SEÇÃO 4: PROMPT DO INDEXADOR — 8 min

**Tom:** Professor explica os três riscos antes de digitar — didático e clínico

"Antes de escrever o prompt do indexador, preciso explicar três regras.

Não são detalhes técnicos opcionais.
São regras críticas.
Se uma delas for violada, o indexador vai funcionar — mas de forma errada.
E o erro vai aparecer só depois, quando você tentar fazer uma busca.

---

Regra 1: caminho ancorado.

O banco vetorial vai ser criado dentro da pasta `data/`, na raiz do projeto.
O programa vai precisar saber onde essa pasta está.

Existe uma forma frágil de informar isso: dar um caminho solto, do tipo 'a pasta data, aqui do lado'.
O problema é que 'aqui do lado' depende de onde você está parado quando roda o programa.
Se você rodar de dentro da pasta do projeto, funciona.
Se você rodar de outra pasta qualquer, o banco vai nascer no lugar errado.
Sem dar erro.
Sem avisar.
O banco vai estar lá, mas não onde você espera.

A forma correta é ancorar o caminho no próprio código: 'a pasta data fica em relação a este arquivo, não em relação a onde o usuário está parado'.
Ancorado ao código. Sempre no lugar certo, não importa de onde você rode.

---

Regra 2: idempotência.

Idempotência é uma palavra que você vai usar bastante no ClinMd-Tribe.

Significa: rodar a mesma operação duas vezes dá o mesmo resultado que rodar uma vez.

Se você rodar o indexador hoje, ele vai criar os trechos no banco.
Se você rodar de novo amanhã, porque atualiza os artigos, ou porque deu erro,
ele deve atualizar os trechos existentes, não duplicar.

A forma de garantir isso tem duas partes.

Primeira: cada trecho precisa de um nome fixo e previsível, que não muda de uma execução para a outra. O mesmo parágrafo do mesmo artigo sempre recebe a mesma etiqueta.

Segunda: ao gravar, o indexador precisa seguir a regra 'se este trecho já existe, atualiza; se não existe, cria'. Em vez da regra ingênua 'sempre adiciona mais um'.

Com a regra ingênua, rodar duas vezes deixa cada trecho duplicado.
Com a regra de atualizar-ou-criar, rodar duas vezes dá o mesmo resultado de rodar uma.

---

Regra 3: chunking por parágrafo.

O indexador vai cortar os artigos em trechos.
A pergunta é: como cortar?

A forma errada é cortar por número fixo de caracteres.
Imagine: 'a dose de rivaroxabana deve ser ajustada conforme a fun—'
Trecho termina aqui.
Próximo trecho começa: '—ção renal do paciente.'
Clinicamente inútil.

A forma correta é cortar por parágrafo.
Cada parágrafo é uma unidade de sentido.
Com overlap de um parágrafo entre trechos consecutivos —
assim o contexto não se perde na divisão.

---

Essas três regras estão no prompt.
Agora vamos digitar.

Repare: eu não vou dizer ao Claude QUAL comando usar nem QUAL linha escrever.
Eu descrevo o EFEITO que eu quero, em português.
Quem escolhe como implementar é ele.
Esse é o jeito que a gente trabalha no curso inteiro.

[ler cada parte em voz alta e digitar]

```
Implemente o indexador do ClinMd-Tribe respeitando a Clean Architecture (as 4 camadas).
A função dele: ler os arquivos .txt da pasta knowledge_base e indexar tudo num
banco vetorial guardado na pasta data, na raiz do projeto.

Quero o trabalho dividido em três responsabilidades, cada uma na sua camada:

1. Um leitor de artigos, na camada de infraestrutura, no arquivo
   infrastructure/rag/txt_loader.py.
   - Lê todos os .txt da pasta knowledge_base.
   - Usa um caminho ancorado à raiz do projeto, não um caminho solto: o leitor
     deve achar a pasta knowledge_base mesmo que eu rode o programa de outra pasta.
   - Corta cada artigo em trechos por parágrafo, com uma pequena sobreposição
     entre trechos vizinhos (um parágrafo de overlap), para o contexto não se
     perder na divisão. Nunca cortar por número fixo de caracteres.
   - Descarta os trechos muito curtos (referências bibliográficas soltas), que
     não ajudam numa busca clínica.
   - Para cada trecho, guarda de onde ele veio: de qual artigo e qual a posição
     dele dentro do artigo.

2. Um repositório do banco vetorial, também na camada de infraestrutura, no arquivo
   infrastructure/rag/chroma_repositorio.py.
   - O banco fica guardado em disco, na pasta data, com o caminho ancorado à raiz
     do projeto (mesma regra do leitor: nunca um caminho solto).
   - Ao gravar os trechos, garante idempotência: rodar o indexador duas vezes não
     pode duplicar nada. Cada trecho tem um nome fixo e previsível, e a gravação
     segue a regra atualiza-se-já-existe, cria-se-é-novo, em vez de sempre adicionar
     mais um.

3. Um serviço que orquestra os dois, na camada de aplicação, no arquivo
   application/servicos/indexador_service.py.
   - Chama o leitor, manda indexar e, ao final, imprime no terminal uma frase no
     formato: "X trechos indexados de Y arquivos".
   - Deixe esse serviço executável direto pelo terminal pelo comando:
     uv run python -m application.servicos.indexador_service

Regra de arquitetura que não pode ser quebrada: só a camada de infraestrutura pode
conhecer a tecnologia do banco vetorial. As camadas de aplicação e de domínio não
podem importar nada do banco diretamente.

Ao final, me diga como rodar o indexador pelo terminal.
```

---

[enviar o prompt ao Claude Code]

**[TELA: mostrar o Claude Code gerando os arquivos]**"

---

## SEÇÃO 5: CLAUDE IMPLEMENTA + LAUDO DE CONFORMIDADE - 15 min

**Tom:** Aguardar e auditar pelo laudo. Você não lê o código; você pede um laudo em português e confere as três regras

[aguardar o Claude Code processar]

**[TELA: mostrar os arquivos sendo criados]**

"Três arquivos novos.

O leitor de artigos, na infraestrutura, criado.
O repositório do banco vetorial, na infraestrutura, criado.
O serviço que orquestra os dois, na aplicação, criado.

Você não escreveu nenhuma linha.
Você escreveu o prompt.

Agora vem a parte importante: você confere antes de rodar.

Só que você não vai ler código.
Você é médico, não programador.
Ler arquivo de programa linha por linha não é o seu trabalho, e nunca vai ser.

O seu trabalho é o mesmo de sempre na medicina: pedir o exame certo e ler o laudo.

Então em vez de abrir os arquivos, você pede um laudo.
Você manda o Claude auditar o próprio trabalho e te confirmar, em português,
que as três regras críticas foram respeitadas.

Cole este prompt:

```
Audite os três arquivos que você acabou de criar para o indexador.
Não me mostre código. Me responda em português, como um laudo, item por item.

Para cada um dos três pontos abaixo, diga se está CONFORME ou se há um ATENÇÃO,
e explique em uma frase o que você verificou:

1. Caminho ancorado: o leitor e o banco vetorial usam um caminho ancorado à raiz
   do projeto (e não um caminho solto, que dependeria de onde eu rodo o programa)?

2. Idempotência: rodar o indexador duas vezes NÃO duplica os trechos? Confirme que
   cada trecho tem um nome fixo e previsível e que a gravação atualiza o que já
   existe em vez de sempre adicionar mais um.

3. Chunking por parágrafo: os artigos são cortados por parágrafo, com sobreposição
   entre trechos vizinhos, e nunca por número fixo de caracteres?

E confirme também: a tecnologia do banco vetorial só aparece na camada de
infraestrutura? As camadas de aplicação e de domínio ficaram livres dela?

Se algum item não estiver conforme, corrija o código você mesmo e me avise o que mudou.
```

---

[enviar o prompt e aguardar o laudo]

**[TELA: mostrar o laudo do Claude em português, sem código, item por item]**

"O Claude responde em português, item por item.
Você lê o laudo do mesmo jeito que lê o laudo de um exame: procurando o que está
conforme e o que está em atenção.

Vou explicar por que cada um desses três itens importa tanto a ponto de virar laudo.
Porque quando um deles falha, o erro não aparece agora. Aparece lá na frente, na busca,
quando já é difícil descobrir a causa."

---

**Item 1 do laudo - Caminho ancorado:**

"Este é o erro mais silencioso desta aula.

Se o caminho do banco for solto, em vez de ancorado, acontece o seguinte:
você indexa os artigos hoje, tudo funciona, você fecha o terminal.
Amanhã você abre o programa de outra pasta, e o banco parece vazio.
Os trechos não sumiram. Eles estão lá, mas num lugar que o programa não procura mais.

Nenhum erro vermelho na tela. Nenhum aviso. Só uma busca que não acha nada.

Por isso o laudo precisa dizer, em letras claras: caminho ancorado, CONFORME."

---

**Item 2 do laudo - Idempotência:**

"Aqui o risco é a duplicação.

Sem a regra de atualizar-ou-criar, cada vez que você roda o indexador, os trechos
entram de novo. Roda duas vezes, cada trecho aparece duas vezes no banco.

E quando você buscar, mais tarde, 'dose de rivaroxabana em FA com clearance reduzido',
o app vai te devolver o mesmo trecho repetido.
O ClinMd-Tribe vai parecer com um eco, repetindo a mesma informação.
E vai ser difícil entender por quê, porque a busca em si funciona.

O laudo confirma: rodar duas vezes não duplica. Idempotência, CONFORME."

---

**Item 3 do laudo - Chunking por parágrafo:**

"Este é o mais clínico dos três.

Se o artigo for cortado por número fixo de caracteres, os trechos quebram no meio
das frases. Um trecho termina em 'a dose de rivaroxabana deve ser ajustada conforme
a função', e para ali.
Esse pedaço é inútil para o app responder uma pergunta sobre dosagem: a informação
que importa ficou cortada ao meio.

Cortar por parágrafo respeita a unidade de sentido do texto médico.
Cada parágrafo é um pensamento completo. E a sobreposição entre trechos vizinhos
garante que nada de importante se perca exatamente na linha do corte.

O laudo confirma: chunking por parágrafo com sobreposição, CONFORME."

---

"Três itens, três CONFORME.
E o laudo ainda confirma que a tecnologia do banco ficou só na infraestrutura,
do jeito que a Clean Architecture exige.

Você auditou um indexador inteiro sem ler uma linha de código.
Leu um laudo. Como faz todo dia.

O indexador está pronto para rodar."

---

## SEÇÃO 6: RODAR O INDEXADOR — 5 min

**Tom:** Aviso crítico antes de executar — modelo, LGPD, output esperado

"Antes de rodar, um aviso importante.

Na primeira execução, o indexador vai baixar um modelo de linguagem.
O nome é `all-MiniLM-L6-v2`.
Tamanho: aproximadamente 90 MB.

Pense como a calibração inicial de um equipamento novo.
Um ecocardiograma novo chega ao consultório e precisa de uma configuração inicial.
Depois: funciona instantaneamente.
O modelo é a mesma coisa.

Não interrompa enquanto o progresso aparecer no terminal.

---

Uma nota sobre LGPD.

Esse download é o único momento nesta aula em que algo sai da sua máquina.
É o modelo que desce — não o seu dado.

Os artigos do PubMed estão na sua pasta.
A indexação acontece localmente.
O banco vetorial fica no seu computador.

Depois que o modelo baixar: 100% offline.
Dado de paciente não entra, dado de paciente não sai.

---

Agora rodamos.

```
uv run python -m application.servicos.indexador_service
```

**[TELA: mostrar o terminal — progresso do download do modelo na primeira execução]**

[aguardar o download e a indexação]

---

O output esperado:

```
141 trechos indexados de 3 arquivos.
```

**[NOTA DE PRODUÇÃO: anotar o número exato de trechos antes de gravar — o número 141 é uma estimativa baseada em artigos típicos de ~40KB]**

---

Três artigos.
Cento e quarenta e um trechos.

Cada trecho é um parágrafo — ou par de parágrafos com overlap —
que o app vai conseguir buscar quando você fizer uma pergunta.

A biblioteca está indexada."

---

## SEÇÃO 7: IDEMPOTÊNCIA AO VIVO — 4 min

**Tom:** Demonstração prática da Regra 2 — fechar, reabrir, rodar de novo

"Vou provar a Regra 2 ao vivo.

Fecha o terminal.

**[TELA: fechar o terminal]**

---

Abre um terminal novo.

**[TELA: abrir terminal na raiz do projeto]**

Roda o indexador de novo.

```
uv run python -m application.servicos.indexador_service
```

**[TELA: mostrar o terminal rodando — sem o download desta vez, apenas a indexação]**

---

O output:

```
141 trechos indexados de 3 arquivos.
```

Mesmo número.

---

O banco não duplicou.

O indexador reconheceu cada trecho pelo nome fixo que ele já tinha,
verificou que todos já existiam, e atualizou sem criar duplicatas.

Um indexador ingênuo, daqueles que sempre adicionam mais um em vez de atualizar o que já existe,
teria 282 trechos agora.
E quando você buscasse 'dose de rivaroxabana em FA com clearance reduzido',
receberia cada trecho relevante duas vezes.
O app pareceria com um eco, repetindo as mesmas informações.

Idempotência resolve isso.
Rodar duas vezes — ou dez vezes — dá o mesmo resultado."

---

## SEÇÃO 8: ENCERRAMENTO — 3 min

**Tom:** Consolidar o que foi construído + gancho para aula_29

"O que está pronto.

A pasta `knowledge_base/` com três artigos sobre anticoagulação em FA.
O banco vetorial em `data/chroma_db/` com 141 trechos indexados.
Um indexador idempotente que você pode rodar quantas vezes quiser.

---

Voltando à analogia do residente.

Antes desta aula, o ClinMd-Tribe não tinha lido nada.

Agora ele leu.

Três artigos.
Anticoagulação.
Fibrilação atrial.

A biblioteca existe.
O banco está indexado.

---

Mas ele ainda não respondeu nenhuma pergunta.

E o momento mais importante não vai ser quando ele responder certo.

Vai ser quando ele disser que não sabe.

Um residente que inventa respostas é perigoso.
Um app que alucina é perigoso.

Na próxima aula você vai fazer a primeira pergunta ao ClinMd-Tribe.
E você vai ver como ele responde —
e como ele reconhece quando a resposta não está na biblioteca.

Até lá."

---

**Dever de casa:**

"Antes da próxima aula, adicione um quarto artigo ao `knowledge_base/`.

Pode ser qualquer tema clínico do seu interesse — não precisa ser FA.

Peça ao Claude Code:

```
Busque 1 artigo sobre [tema da sua escolha] no PubMed e salve em knowledge_base/.
```

Depois rode o indexador novamente.

Observe: o número de trechos vai subir — e os trechos dos três artigos anteriores não vão duplicar.

Isso confirma que a idempotência funciona com dados novos também."

---

**FIM DO ROTEIRO**
