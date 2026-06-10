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

O banco vetorial vai ser criado em `data/chroma_db/`.
O Claude vai precisar saber onde essa pasta está.

Se usar uma string simples — `'data/chroma_db'` —
o banco vai ser criado no lugar errado quando você rodar o programa de outra pasta.
Sem dar erro.
Sem avisar.
O banco vai estar lá, mas não onde você espera.

A forma correta usa `Path(__file__).parent.parent / 'data' / 'chroma_db'`.
Isso significa: 'vai dois níveis acima do arquivo que estou escrevendo, e procura a pasta data/chroma_db'.
Ancorado ao código. Sempre no lugar certo.

---

Regra 2: idempotência.

Idempotência é uma palavra que você vai usar bastante no ClinMd-Tribe.

Significa: rodar a mesma operação duas vezes dá o mesmo resultado que rodar uma vez.

Se você rodar o indexador hoje, ele vai criar os trechos no banco.
Se você rodar de novo amanhã — porque atualiza os artigos, ou porque deu erro —
ele deve atualizar os trechos existentes, não duplicar.

A forma de garantir isso: IDs determinísticos e `upsert` em vez de `add`.

ID determinístico significa que o mesmo trecho sempre tem o mesmo nome.
`upsert` significa: se já existe, atualiza. Se não existe, cria.

Com `add`, rodar duas vezes = cada trecho duplicado.
Com `upsert`, rodar duas vezes = mesmo resultado.

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

[ler cada parte em voz alta e digitar]

```
Implemente o indexador do ClinMd-Tribe respeitando Clean Architecture (4 camadas).
Lê arquivos .txt de knowledge_base/ e indexa no banco vetorial em data/chroma_db/.

infrastructure/rag/txt_loader.py
  - Lê todos os .txt de knowledge_base/
    (caminho ancorado na raiz: Path(__file__).parent.parent / "knowledge_base")
  - Chunking por parágrafo com overlap de 1 parágrafo entre trechos consecutivos
  - Descarta trechos com menos de 150 caracteres (referências bibliográficas)
  - Cada trecho guarda metadado: nome_arquivo (str) e numero_trecho (int)
  - Retorna lista de dicts: {"texto": str, "nome_arquivo": str, "numero_trecho": int}

infrastructure/rag/chroma_repositorio.py
  - chromadb.PersistentClient com path ANCORADO na raiz do projeto:
    Path(__file__).parent.parent / "data" / "chroma_db"
  - Usa get_or_create_collection("clinmd_rag")
  - Método indexar(documentos: list[dict]) → None
    IDs determinísticos: f"{doc['nome_arquivo']}_{doc['numero_trecho']}"
    Usa upsert (não add) para garantir idempotência

application/servicos/indexador_service.py
  - Importa txt_loader e chroma_repositorio
  - Chama o loader, manda indexar
  - Imprime no terminal: "X trechos indexados de Y arquivos"

NÃO importe chromadb em application/ nem em domain/. Apenas em infrastructure/.
Ao final, me diga como rodar o indexador pelo terminal.
```

---

[enviar o prompt ao Claude Code]

**[TELA: mostrar o Claude Code gerando os arquivos]**"

---

## SEÇÃO 5: CLAUDE IMPLEMENTA + LEITURA SUPERVISIONADA — 15 min

**Tom:** Aguardar + auditar — três perguntas, cada uma corresponde a um risco técnico explicado na seção anterior

[aguardar o Claude Code processar]

**[TELA: mostrar os arquivos sendo criados]**

"Três arquivos novos.

`infrastructure/rag/txt_loader.py` — criado.
`infrastructure/rag/chroma_repositorio.py` — criado.
`application/servicos/indexador_service.py` — criado.

Você não escreveu nenhuma linha.
Você escreveu o prompt.

Agora você lê antes de rodar.

Três perguntas.
Cada uma verifica uma das regras que eu expliquei."

---

**Pergunta 1 — Caminho ancorado (Risco A):**

"Abra `infrastructure/rag/chroma_repositorio.py`.

Você está procurando o `PersistentClient`.
Ele usa `Path(__file__)` ou usa uma string simples?

O padrão correto é este:

```python
from pathlib import Path

_DB_PATH = Path(__file__).parent.parent / "data" / "chroma_db"
client = chromadb.PersistentClient(path=str(_DB_PATH))
```

Se você ver `chromadb.PersistentClient(path='data/chroma_db')` — string simples —
o banco vai ser criado em um lugar diferente dependendo de onde você rodar o programa.
Você vai indexar os artigos, fechar o terminal, abrir de outra pasta,
e o banco vai parecer vazio.

Esse é o erro mais silencioso desta aula.

**[TELA: mostrar o código — confirmar Path(__file__) ancorado]**

Correto — caminho ancorado."

---

**Pergunta 2 — Idempotência (Risco B):**

"Agora, no mesmo arquivo, procure o método que grava os trechos.

Você está procurando duas coisas:

Primeira: os IDs são determinísticos?
Procure algo como:

```python
id = f"{doc['nome_arquivo']}_{doc['numero_trecho']}"
```

Segunda: o método usa `upsert` ou `add`?

Com `upsert`, rodar o indexador duas vezes = mesmo número de trechos no banco.
Com `add`, rodar o indexador duas vezes = cada trecho duplicado.

Quando você fizer uma busca num banco duplicado,
vai receber o mesmo trecho duas vezes na resposta.
O app vai parecer repetitivo — e vai ser difícil saber por quê.

**[TELA: mostrar o código — confirmar upsert e IDs determinísticos]**

Correto — upsert, IDs determinísticos."

---

**Pergunta 3 — Chunking por parágrafo (Risco C):**

"Agora abra `infrastructure/rag/txt_loader.py`.

O texto está sendo dividido por `\n\n` — quebra dupla de linha — ou por número fixo de caracteres?

Procure algo assim:

```python
paragrafos = texto.split('\n\n')
```

Se você ver `texto[i:i+500]` — corte por número fixo de caracteres —
os trechos vão quebrar no meio de frases clínicas.
Um trecho que termina em 'a dose de rivaroxabana deve ser ajustada conforme a função'
é inútil para o app responder perguntas sobre dosagem.

O chunking por parágrafo respeita a unidade de sentido do texto médico.

**[TELA: mostrar o código — confirmar split('\n\n') com overlap]**

Correto — chunking por parágrafo com overlap.

---

As três regras estão respeitadas.

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

O indexador reconheceu os IDs — `nome_arquivo_numero_trecho` —
verificou que já existiam, e atualizou sem criar duplicatas.

Um indexador ingênuo — usando `add` em vez de `upsert` —
teria 282 trechos agora.
E quando você buscasse 'dose de rivaroxabana em FA com clearance reduzido',
receberia cada trecho relevante duas vezes.
O app pareceria com um eco — repetindo as mesmas informações.

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

**FIM DO ROTEIRO**
