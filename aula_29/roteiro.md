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
Se não encontrar nada: devolve lista vazia. Nunca texto inventado.

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
  - Entidade pura ResultadoBusca com campos:
    trecho: str, fonte: str, numero_trecho: int, score: float

domain/rag/porta_busca.py
  - Interface abstrata BuscaRAG com método:
    buscar(consulta: str, n: int) → list[ResultadoBusca]
  - ZERO import de chromadb aqui — só o contrato

infrastructure/rag/chroma_repositorio.py
  - Atualizar arquivo existente: implementar a interface BuscaRAG
  - Usar o mesmo PersistentClient já criado no indexador
  - Retornar os N trechos mais próximos semanticamente
  - SEMPRE incluir fonte e numero_trecho nos resultados

application/servicos/busca_service.py
  - def buscar(consulta: str, n: int = 3) -> list[ResultadoBusca]   ← função pública (não classe)
  - Recebe a pergunta do médico (str) e n (int, padrão 3)
  - Chama BuscaRAG.buscar()
  - Se lista vazia: retorna lista vazia — nunca texto inventado
  - Retorna list[ResultadoBusca]

Regras:
  - Nenhum dado sai da máquina. Busca 100% offline.
  - Todo resultado DEVE ter fonte. Trecho sem fonte não pode ser exibido ao médico.

Me mostre como testar a busca pelo terminal antes de conectar na tela.
```

[enviar o prompt ao Claude Code]

**[TELA: mostrar o Claude Code gerando os arquivos]**"

---

## SEÇÃO 3: CLAUDE IMPLEMENTA + LEITURA SUPERVISIONADA — 12 min

**Tom:** Aguardar + auditar — três perguntas, cada uma verifica um princípio crítico

[aguardar o Claude Code processar]

**[TELA: mostrar os arquivos sendo criados e atualizados]**

"Quatro arquivos.

`domain/rag/resultado_busca.py` — criado.
`domain/rag/porta_busca.py` — criado.
`infrastructure/rag/chroma_repositorio.py` — atualizado.
`application/servicos/busca_service.py` — criado.

Você não escreveu nenhuma linha.
Você escreveu o prompt.

Agora você lê antes de rodar.

Três perguntas."

---

**Pergunta 1 — Interface no domínio (a regra mais importante):**

"Abra `domain/rag/porta_busca.py`.

Existe algum `import chromadb` nesse arquivo?

Não deve.

O domínio define o contrato — não sabe como a busca é implementada.

**[TELA: mostrar o conteúdo de porta_busca.py — confirmar ausência de import chromadb]**

Agora abra `infrastructure/rag/chroma_repositorio.py`.

Aqui sim o `import chromadb` aparece.

---

Por que isso importa?

Se o ChromaDB for descontinuado:
você reescreve esse único arquivo.
O resto do app continua sem saber que mudou.

A tela não sabe que existe ChromaDB.
O serviço não sabe que existe ChromaDB.
O domínio não sabe que existe ChromaDB.

Apenas a infraestrutura sabe.
E a infraestrutura é o único lugar que pode mudar.

**[TELA: mostrar o import chromadb em chroma_repositorio.py — confirmar que está só aqui]**

Correto — isolamento respeitado."

---

**Pergunta 2 — Proveniência obrigatória:**

"Em `infrastructure/rag/chroma_repositorio.py`, no método de busca:

Cada `ResultadoBusca` está sendo criado com o campo `fonte` preenchido?

O campo `fonte` não pode ser vazio.

Um médico não pode receber um trecho sem saber de qual artigo veio.
Isso é responsabilidade clínica.
Se o trecho diz 'a dose de rivaroxabana deve ser ajustada para 15mg em insuficiência renal moderada'
— o médico precisa saber de qual artigo isso veio.
Para verificar.
Para citar.
Para discordar, se necessário.

"O que importa verificar não são as chaves internas do ChromaDB — essas mudam conforme a implementação.
O que importa: cada `ResultadoBusca` retornado tem o campo `fonte` preenchido?
Abra `infrastructure/rag/chroma_repositorio.py` e confirme que nenhum `ResultadoBusca` é criado com `fonte=''` ou `fonte=None`."

**[TELA: mostrar o código do método de busca — confirmar fonte preenchida em cada resultado]**

Correto — proveniência garantida."

---

**Pergunta 3 — Lista vazia quando não encontra:**

"Em `application/servicos/busca_service.py`:

O que acontece quando o ChromaDB não retorna nada?

Deve retornar lista vazia.
Não texto inventado.
Não 'baseado no meu conhecimento geral...'.
Não uma resposta aproximada.

Lista vazia.

O padrão esperado:

```python
return resultados  # pode ser []
```

Simples assim.

Isso é o residente que não chuta.
Quando não sabe, diz que não sabe.

**[TELA: mostrar o return em busca_service.py — confirmar lista vazia]**

Correto — sem invenção."

---

## SEÇÃO 4: GABARITO 1 — PERGUNTA DENTRO DO KB — TRECHOS RETORNADOS COM FONTE — 5 min

**Tom:** Primeira demonstração — o app responde com rastreabilidade

"Vamos à primeira pergunta.

Pergunta dentro do knowledge_base.
Os artigos que indexamos falam sobre anticoagulação em FA.
Vamos perguntar sobre anticoagulação em FA.

```bash
uv run python - <<'EOF'
from application.servicos.busca_service import buscar
resultados = buscar('anticoagulação em fibrilação atrial', n=3)
for r in resultados:
    print(f'Fonte: {r.fonte} | Trecho {r.numero_trecho}')
    print(r.trecho[:200])
    print('---')
EOF
```

**[TELA: mostrar o terminal rodando o comando]**

[aguardar o output]

**[NOTA DE PRODUÇÃO: anotar os trechos reais e nomes de arquivo antes de gravar — os nomes abaixo são exemplos]**

---

O output vai ser algo assim:

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

```bash
uv run python - <<'EOF'
from application.servicos.busca_service import buscar
resultados = buscar('quando suspender o anticoagulante antes de procedimento', n=3)
for r in resultados:
    print(f'Fonte: {r.fonte} | Trecho {r.numero_trecho}')
    print(r.trecho[:200])
    print('---')
EOF
```

**[TELA: mostrar o terminal rodando o comando]**

[aguardar o output]

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

[pausa de 3 segundos antes de rodar o teste]

```bash
uv run python - <<'EOF'
from application.servicos.busca_service import buscar
resultados = buscar('como tratar diabetes tipo 2 com metformina', n=3)
print(f'Resultados encontrados: {len(resultados)}')
if not resultados:
    print('Lista vazia.')
EOF
```

**[TELA: mostrar o terminal rodando o comando — aguardar o output]**

---

```
Resultados encontrados: 0
Lista vazia.
```

---

O app não inventou nada.

Não disse 'baseado no meu conhecimento geral sobre diabetes...'.
Não disse 'metformina é a droga de escolha...'.
Devolveu zero resultados.

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

Mas o médico não vai usar o terminal.

Ele não vai digitar `uv run python -c "..."`.

Ele vai abrir o app, digitar uma pergunta num campo de texto,
e ver os resultados na tela.

Na próxima aula você liga o buscador na interface do Flet.

E vai aprender a diagnosticar quando a busca está ruim —
quando os resultados retornados não fazem sentido para a pergunta feita.

Isso se chama avaliação de relevância.
É o que o médico faz quando o residente traz uma referência errada.

---

Antes da próxima aula:

Teste mais duas perguntas no terminal.

Uma dentro do seu `knowledge_base/` — sobre anticoagulação, sobre FA, o que você indexou.
Uma completamente fora — sobre um tema que não está nos artigos.

Observe o comportamento em cada caso.

Copie o terminal.
Compare os dois outputs.

Esse exercício vai preparar você para a próxima aula,
onde você vai conectar exatamente esse comportamento na interface do app."

---

**Dever de casa:**

"Antes da próxima aula, teste mais 2 perguntas no terminal — uma dentro do seu `knowledge_base/` e uma completamente fora. Observe o comportamento em cada caso."

---

**FIM DO ROTEIRO**
