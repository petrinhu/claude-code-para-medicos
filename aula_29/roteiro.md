# Aula 29 — Busca Semântica: Perguntando ao Arquivo

**Formato:** Gravada em um take no OBS Studio
**Duração:** ~42 min
**Tom:** Cardiologista testando se o app realmente aprendeu o que está nos artigos
**Módulo:** S07.03 — Busca Semântica em Produção

---

## SEÇÃO 1: ABERTURA — A BIBLIOTECA EXISTE. HORA DE PERGUNTAR. — 3 min

**Tom:** Bridge com aula_28 — celebrar o que foi construído e antecipar o clímax

"Na aula anterior você fez algo que nenhuma das nossas calculadoras havia feito antes.

O ClinMd-Tribe leu artigos.

Três artigos sobre anticoagulação em fibrilação atrial.
Baixados do PubMed.
Cortados em trechos.
Indexados em um banco vetorial.

A biblioteca existe.

---

Hoje você faz a primeira pergunta.

Não uma pergunta para o Claude.
Uma pergunta para o app.

Uma pergunta que ele vai responder consultando os artigos que leu —
sem sair da sua máquina.
Sem inventar.
Sem alucinação.

---

E o momento mais importante desta aula não vai ser quando o app responder certo.

Vai ser quando ele disser que não sabe.

---

Um sistema que inventa quando não tem a resposta é perigoso.
Para qualquer profissional — mas especialmente para um médico.

Um sistema que responde 'não encontrei' é confiável.
Você sabe o que ele sabe.
Você sabe o que ele não sabe.

Isso se chama rastreabilidade.

E é o que você vai ver ao vivo hoje."

---

## SEÇÃO 2: PROMPT DO BUSCADOR — 8 min

**Tom:** Professor explica a arquitetura do buscador antes de digitar — a regra de isolamento é crítica

"Antes de escrever o prompt, preciso explicar onde o buscador vai morar.

Não é uma decisão estética.
É uma decisão que vai proteger seu app quando o ChromaDB for atualizado —
ou substituído por algo melhor.

---

A estrutura em 4 camadas para o buscador:

**`domain/rag/porta_busca.py`** — a interface abstrata.
O domínio define o contrato: 'existe uma busca que recebe uma pergunta e retorna resultados'.
ZERO import de chromadb aqui.
O domínio não sabe como a busca é feita.
Ele só sabe que ela existe.

**`infrastructure/rag/chroma_repositorio.py`** — o ÚNICO arquivo que importa chromadb.
Esse arquivo já existe da aula anterior.
Hoje ele vai ser atualizado para implementar a interface do domínio.

**`application/servicos/busca_service.py`** — o orquestrador.
Recebe a pergunta do médico, chama a busca, devolve os resultados.
E aqui mora a parte mais importante, que eu preciso te explicar antes: o banco vetorial é teimoso. Ele SEMPRE devolve os três trechos mais próximos da sua pergunta, mesmo que os três sejam ruins, mesmo que o tema esteja a quilômetros dos seus artigos. Ele nunca devolve vazio sozinho.
Então quem decide 'isto está perto o bastante pra contar' é uma régua: o corte de relevância. Cada trecho volta com um score de distância; se o melhor estiver longe demais, além da régua, o serviço descarta e devolve lista vazia. É assim que o app consegue dizer 'não tenho', sem texto inventado.

---

Por que isso importa?

Se sair um banco vetorial melhor que o ChromaDB amanhã —
você reescreve um único arquivo: `chroma_repositorio.py`.

A tela não muda.
O serviço não muda.
O domínio não muda.

Isso é Clean Architecture no trabalho real.

---

Agora o prompt.

[ler cada parte em voz alta antes de enviar]

```
Implemente a busca semântica do ClinMd-Tribe sobre data/chroma_db/.
Respeite as 4 camadas.

domain/rag/resultado_busca.py
  - O resultado da busca é uma coisa simples e pura do domínio.
  - Cada resultado guarda quatro informações: o trecho de texto encontrado,
    a fonte (de qual artigo veio), o número do trecho dentro do artigo, e
    um score de distância (o quão perto esse trecho está da pergunta).

domain/rag/porta_busca.py
  - Aqui mora só o contrato da busca: "existe uma busca que recebe uma
    pergunta e devolve uma lista de resultados".
  - O domínio define o que a busca faz, nunca COMO ela faz.
  - ZERO conhecimento do chromadb aqui. O domínio não sabe que o ChromaDB existe.

infrastructure/rag/chroma_repositorio.py
  - Atualizar o arquivo que já existe da aula anterior.
  - Este é o ÚNICO lugar do app que conhece o ChromaDB.
  - Reaproveite a mesma conexão com o banco que o indexador já criou.
  - Devolva os N trechos mais próximos semanticamente da pergunta.
  - SEMPRE preencha a fonte e o número do trecho em cada resultado.

application/servicos/busca_service.py
  - O serviço é o orquestrador: recebe a pergunta do médico, dispara a busca,
    aplica o corte de relevância e devolve os resultados.
  - Por padrão, traz os 3 trechos mais próximos; a quantidade deve ser ajustável.
  - CORTE DE RELEVÂNCIA (essencial): o banco vetorial SEMPRE devolve os N trechos mais
    próximos, mesmo quando o tema está fora dos artigos. Para o app poder dizer "não tenho",
    descarte os resultados cujo score de distância ultrapasse um LIMIAR de relevância; se
    não sobrar nenhum, devolva lista VAZIA (nunca texto inventado). Exponha esse limiar como
    uma constante nomeada e ajustável (ex.: LIMIAR_DISTANCIA), com valor inicial conservador
    que eu vou calibrar depois.

Regras:
  - Nenhum dado sai da máquina. Busca 100% offline.
  - Todo resultado DEVE ter fonte. Trecho sem fonte não pode ser exibido ao médico.

Quando terminar, confirme em português, sem me mostrar código, quais
arquivos foram criados ou atualizados em cada camada.
```

[enviar o prompt ao Claude Code]

**[TELA: mostrar o Claude Code gerando os arquivos]**"

---

## SEÇÃO 3: CLAUDE IMPLEMENTA + LAUDO DE CONFORMIDADE — 12 min

**Tom:** Aguardar + auditar pelo laudo — três perguntas, cada uma verifica um princípio crítico, em português

[aguardar o Claude Code processar]

**[TELA: mostrar o Claude Code trabalhando]**

"Quatro arquivos, nas quatro camadas certas.

A entidade do resultado, no domínio.
O contrato da busca, no domínio.
O repositório do ChromaDB, na infraestrutura.
O serviço orquestrador, na aplicação.

Você não escreveu nenhuma linha.
Você escreveu o prompt.

Agora, antes de rodar qualquer busca, você audita o que foi construído.

E você não vai ler código para isso.
Você é cardiologista, não revisor de código.

Você vai pedir um laudo.

Do mesmo jeito que você não lê o traçado bruto do aparelho de RM,
você lê o laudo do radiologista.
Aqui o Claude é o seu radiologista de código.
Você faz três perguntas, ele responde em português, e você confere o laudo.

Cole este pedido:

```
Sem me mostrar código, me responda em português e em laudo curto, três perguntas
sobre a busca que você acabou de implementar:

1. ISOLAMENTO: o domínio (porta_busca.py e resultado_busca.py) está livre do
   ChromaDB? Confirme que o único arquivo do app que conhece o ChromaDB é o
   repositório na infraestrutura, e que nem a tela, nem o serviço, nem o domínio
   sabem que o ChromaDB existe.

2. PROVENIÊNCIA: todo resultado devolvido pela busca sai com a fonte preenchida,
   ou seja, com o nome do artigo de origem? Confirme que nenhum trecho pode ser
   devolvido com a fonte vazia ou em branco. Nenhum trecho órfão.

3. LISTA VAZIA: quando nenhum trecho fica perto o bastante (acima da régua, do
   corte de relevância), a busca devolve uma lista vazia? Confirme que ela nunca
   devolve texto inventado nem uma resposta aproximada quando não há nada relevante.

Responda cada item com OK ou ATENÇÃO e uma frase de justificativa, em português.
```

**[TELA: mostrar o laudo do Claude Code em português]**

[ler o laudo em voz alta junto com o aluno]"

---

**Pergunta 1 do laudo — Interface no domínio (a regra mais importante):**

"O Claude vai confirmar: o domínio não conhece o ChromaDB.

E por que essa é a pergunta mais importante?

Porque o domínio define só o contrato: 'existe uma busca que recebe uma
pergunta e devolve resultados'.
Ele não sabe COMO a busca é feita.
Quem sabe fazer a busca de verdade é a infraestrutura, e só ela.

Se o ChromaDB for descontinuado amanhã:
você troca um único arquivo, o repositório na infraestrutura.
O resto do app continua sem saber que algo mudou.

A tela não sabe que existe ChromaDB.
O serviço não sabe que existe ChromaDB.
O domínio não sabe que existe ChromaDB.

Apenas a infraestrutura sabe.
E a infraestrutura é o único lugar que pode mudar.

Se o laudo voltou OK no item 1, isolamento respeitado."

---

**Pergunta 2 do laudo — Proveniência obrigatória:**

"O segundo item do laudo confirma a proveniência: todo trecho sai com a fonte.

Por que isso é inegociável?

Um médico não pode receber um trecho sem saber de qual artigo veio.
Isso é responsabilidade clínica.

Se o trecho diz 'a dose de rivaroxabana deve ser ajustada para 15mg em insuficiência renal moderada',
o médico precisa saber de qual artigo isso veio.
Para verificar.
Para citar.
Para discordar, se necessário.

Não importa o nome interno que o ChromaDB dá às coisas; isso muda conforme a versão.
O que importa é o laudo: nenhum trecho é devolvido com a fonte em branco.
Nenhum trecho órfão chega aos olhos do médico.

Se o laudo voltou OK no item 2, proveniência garantida."

---

**Pergunta 3 do laudo — Lista vazia quando não encontra:**

"O terceiro item é o coração da confiança do app.

O que acontece quando nada está perto o bastante da pergunta?

A busca devolve lista vazia.
Não texto inventado.
Não 'baseado no meu conhecimento geral...'.
Não uma resposta aproximada.

Lista vazia.

Isso é o residente que não chuta.
Quando não sabe, diz que não sabe.

E é exatamente esse comportamento que você vai ver ao vivo daqui a pouco,
quando a gente perguntar sobre um tema que não está nos artigos.

Se o laudo voltou OK no item 3, sem invenção."

---

## SEÇÃO 4: GABARITO 1 — PERGUNTA DENTRO DO KB — TRECHOS RETORNADOS COM FONTE — 5 min

**Tom:** Primeira demonstração — o app responde com rastreabilidade

"Vamos à primeira pergunta.

Pergunta dentro do knowledge_base.
Os artigos que indexamos falam sobre anticoagulação em FA.
Vamos perguntar sobre anticoagulação em FA.

Cole este pedido ao Claude Code:

```
Teste a busca do app por 'anticoagulação em fibrilação atrial' e me mostre,
em português, cada trecho encontrado com a sua fonte (o nome do artigo) e o
número do trecho. NÃO me mostre código, só o resultado da busca em prosa.
```

**[TELA: mostrar o Claude Code rodando a busca e relatando o resultado]**

[aguardar o relato]

**[NOTA DE PRODUÇÃO: anotar os trechos reais e nomes de arquivo antes de gravar, os nomes abaixo são exemplos]**

---

O relato vai ser algo assim:

```
Fonte: 39123456_anticoagulation_fa_guidelines_2023.txt | Trecho 4
The CHA₂DS₂-VASc score is recommended for stroke risk stratification in
patients with non-valvular atrial fibrillation. Anticoagulation is
recommended for scores ≥ 2 in men and ≥ 3 in women...
---
Fonte: 40234567_af_stroke_prevention_meta_analysis.txt | Trecho 12
Direct oral anticoagulants demonstrated superior efficacy and safety
profiles compared to warfarin across multiple randomized controlled trials
in atrial fibrillation populations...
---
Fonte: 38765432_warfarin_vs_noac_systematic_review.txt | Trecho 7
Time in therapeutic range remains a critical determinant of warfarin
efficacy. Patients with TTR below 65% should be considered for transition
to DOAC therapy when clinically appropriate...
---
```

---

Três trechos.
Três fontes diferentes.
Cada um de um artigo diferente.

O cardiologista sabe de qual artigo cada trecho veio.
Pode verificar.
Pode citar.
Pode discordar.

Isso é rastreabilidade clínica."

---

## SEÇÃO 5: GABARITO 2 — BUSCA SEMÂNTICA EM AÇÃO — SINÔNIMOS E PARÁFRASES FUNCIONAM — 4 min

**Tom:** Demonstrar o poder da semântica — busca por sentido, não por palavra exata

"Agora uma pergunta diferente.

Mas que fala sobre a mesma coisa.

Note que eu nem vou usar a palavra 'anticoagulação'. Vou perguntar com outras
palavras, do jeito que um médico perguntaria no corredor.

Cole este pedido ao Claude Code:

```
Teste a busca do app por 'quando suspender o anticoagulante antes de
procedimento' e me mostre, em português, cada trecho encontrado com a sua
fonte e o número do trecho. NÃO me mostre código, só o resultado em prosa.
```

**[TELA: mostrar o Claude Code rodando a busca e relatando o resultado]**

[aguardar o relato]

---

Os trechos retornados vão falar sobre manejo perioperatório, bridging, janela terapêutica.

Nenhum deles precisa ter a palavra exata 'suspender' no texto.

---

Isso é busca semântica.

O banco não está procurando a palavra 'suspender'.
Ele está procurando trechos que ficam próximos no espaço semântico da pergunta.

'Suspender anticoagulante antes de procedimento'
e
'manejo perioperatório de anticoagulação'
significam a mesma coisa para o modelo de linguagem.

Os vetores ficam próximos.
A busca encontra.

---

Uma busca por palavra-chave — como o Google dos anos 90 —
não encontraria nada sem a palavra exata.

A busca semântica encontra por sentido.

Para o médico que pergunta de formas diferentes a cada dia:
isso é a diferença entre um app útil e um app frustrante."

---

## SEÇÃO 6: GABARITO 3 — PERGUNTA FORA DO KB — LISTA VAZIA — CLÍMAX — 5 min

**Tom:** Pausa dramática antes de rodar — preparar o aluno para o momento mais importante da aula

"Agora vem o momento mais importante desta aula.

[pausar]

Vou fazer uma pergunta sobre algo que os artigos não cobrem.

Os artigos indexados são sobre anticoagulação em FA.
A pergunta que vou fazer é sobre diabetes.

Não é sobre FA.
Não é sobre anticoagulação.
Não está nos artigos.

---

O que um LLM normal faria?

O ChatGPT.
O Claude.
Qualquer modelo de linguagem grande.

Eles tentariam responder.
'Baseado no meu conhecimento sobre diabetes tipo 2...'
'Metformina é considerada a primeira linha de tratamento...'

Às vezes a resposta seria correta.
Às vezes seria uma alucinação — uma informação inventada com confiança.

O problema não é errar.
O problema é errar sem avisar.

---

O que o nosso app deve fazer?

Dizer que não sabe.

---

[pausa de 3 segundos antes de pedir o teste]

Cole este pedido ao Claude Code:

```
Teste a busca do app por 'como tratar diabetes tipo 2 com metformina' e me
diga, em português, quantos trechos foram encontrados e quais são. NÃO me
mostre código, só o resultado da busca em prosa.
```

**[TELA: mostrar o Claude Code rodando a busca e relatando o resultado, aguardar o relato]**

---

E o relato volta assim:

```
Resultados encontrados: 0. A busca não encontrou nenhum trecho relevante o
bastante nos artigos indexados. Lista vazia.
```

---

O app não inventou nada.

Não disse 'baseado no meu conhecimento geral sobre diabetes...'.
Não disse 'metformina é a droga de escolha...'.
Devolveu zero resultados.

E sabe por quê? Pela régua que a gente botou: o corte de relevância. Os trechos mais próximos de 'diabetes' nos seus artigos de anticoagulação até existem, mas estão longe demais, além da régua. O serviço mediu a distância, viu que nada estava perto o bastante pra contar, e descartou tudo. Zero não foi sorte, foi a régua funcionando.

---

Para um cardiologista que vai usar essa informação com um paciente real —
isso não é limitação.

Isso é garantia.

---

Você sabe o que o app sabe:
anticoagulação em FA.
Os três artigos que você indexou.

Você sabe o que o app não sabe:
qualquer coisa fora desses artigos.

Esse comportamento tem um nome.

Epistemic humility.
Humildade epistêmica.

O app sabe o que sabe.
E admite o que não sabe.

---

Compare com qualquer LLM:
O ChatGPT, o Claude, qualquer modelo de linguagem —
eles vão tentar responder sempre.
Às vezes inventam.
Às vezes com muita confiança.

O RAG com busca semântica não responde além do que foi indexado.

Se não está nos artigos,
não está na resposta.

---

E tem mais uma camada de segurança aqui.

O app não consultou nenhum servidor externo para responder isso.
Não logou a pergunta do médico em lugar nenhum.
Não enviou o nome do paciente para a nuvem.

Isso é LGPD na prática: a pergunta ficou na sua máquina.
O resultado ficou na sua máquina.
O banco vetorial ficou na sua máquina."

---

## SEÇÃO 7: ENCERRAMENTO + DEVER DE CASA — 4 min

**Tom:** Consolidar conquistas, bridge para aula_30, dever de casa prático

"O que está pronto.

Um buscador semântico funcionando no terminal.
Três gabaritos validados:
— pergunta dentro do knowledge_base: trechos retornados com fonte
— busca por sentido: sinônimos e paráfrases funcionam
— pergunta fora do knowledge_base: lista vazia — sem invenção

A infraestrutura de RAG do ClinMd-Tribe está funcionando.

---

Mas o médico não vai pedir a busca ao Claude Code.

Hoje, para validar, você pediu ao Claude que rodasse a busca e te relatasse
o resultado. Foi assim que você auditou o comportamento do app.

Mas o médico de verdade não quer falar com o Claude para usar o app.
Ele vai abrir o ClinMd-Tribe, digitar uma pergunta num campo de texto,
e ver os resultados na tela.

Na próxima aula você liga o buscador na interface do Flet.

E vai aprender a diagnosticar quando a busca está ruim —
quando os resultados retornados não fazem sentido para a pergunta feita.

Isso se chama avaliação de relevância.
É o que o médico faz quando o residente traz uma referência errada.

---

Antes da próxima aula:

Peça ao Claude Code para testar mais duas perguntas na busca do app.

Uma dentro do seu `knowledge_base/`: sobre anticoagulação, sobre FA, o que você indexou.
Uma completamente fora: sobre um tema que não está nos artigos.

Em cada pedido, peça o resultado em português, com a fonte de cada trecho, e
sem mostrar código.

Observe o comportamento em cada caso e compare os dois relatos.

Esse exercício vai preparar você para a próxima aula,
onde você vai conectar exatamente esse comportamento na interface do app."

---

**Dever de casa:**

"Antes da próxima aula, peça ao Claude Code para testar mais 2 perguntas na busca do app: uma dentro do seu `knowledge_base/` e uma completamente fora. Peça o resultado em português, com a fonte, sem mostrar código. Observe o comportamento em cada caso."

---

**FIM DO ROTEIRO**

---

> **NOTAS DE PRODUÇÃO (não falar, operacional):**
>
> - **Corte de relevância / LIMIAR_DISTANCIA (CRÍTICO p/ o clímax da Seção 6 e p/ a aula_34):** o ChromaDB nunca devolve lista vazia sozinho; o "tema ausente devolve vazio" SÓ funciona com o corte de relevância que o Prompt da Seção 2 agora exige explicitamente. Antes de gravar, calibrar o limiar empiricamente: rodar 3 a 4 perguntas que ESTÃO nos artigos (devem passar) e 3 a 4 que NÃO estão (devem cair para vazio), observar os scores de distância, e fixar o `LIMIAR_DISTANCIA` num ponto conservador que separe os dois grupos (no app clínico, preferir devolver vazio a devolver trecho irrelevante). Validar que `buscar("como tratar diabetes tipo 2 com metformina")` devolve vazio ANTES de gravar a Seção 6.
> - **Métrica de distância:** confirmar se o ChromaDB do projeto está em distância de cosseno ou L2 (muda a escala do limiar). O valor do corte é relativo ao modelo de embeddings e ao corpus, então NÃO existe número mágico universal; é calibração local.
> - **Zero-código (S07) aplicado:** esta aula foi refatorada para a regra "zero código para o aluno LER" (ver memória feedback-zero-codigo-para-ler). A leitura supervisionada de código virou LAUDO DE CONFORMIDADE (Seção 3: o aluno pede ao Claude para confirmar isolamento, proveniência e lista vazia em português, sem ver código). Os heredocs Python das Seções 4, 5 e 6 viraram PROMPTS de busca (o aluno pede ao Claude para rodar a busca e relatar em prosa). O material do corte de relevância (LIMIAR_DISTANCIA, fala da régua na Seção 2 e no clímax da Seção 6) foi preservado integralmente. Os blocos de output mostrados são exemplos de PROSA em português (fonte + trecho), nunca código a analisar.
