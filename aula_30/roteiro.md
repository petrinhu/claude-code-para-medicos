# Aula 30 — Integração Flet + Qualidade da Busca

**Formato:** Gravada em um take no OBS Studio
**Duração:** ~46 min
**Tom:** Cardiologista usando o app e aprendendo a confiar (ou não) na busca
**Módulo:** S07.04 — Integração e Qualidade

---

## SEÇÃO 1: ABERTURA — BUSCADOR FUNCIONA NO TERMINAL. HORA DE LIGAR NA TELA. — 3 min

**Tom:** Bridge com aula_29 — celebrar os três gabaritos e anunciar a virada: terminal → interface

"Na aula anterior você validou três gabaritos.

Pergunta dentro do knowledge_base — trechos retornados com fonte.
Busca por sentido — sinônimos e paráfrases funcionaram.
Pergunta fora do knowledge_base — lista vazia. Sem invenção.

O buscador semântico do ClinMd-Tribe funciona.

---

Mas funciona onde?

No terminal.

O médico não vai usar o terminal.
Ele vai abrir o app, digitar uma pergunta num campo de texto,
e ver os resultados na tela.

---

Hoje são duas coisas.

Primeira: ligar o buscador na interface Flet.
Segunda: aprender a diagnosticar quando a busca retornar resultados ruins.

---

Porque o app vai funcionar.
Mas em alguns momentos ele vai retornar trechos sem sentido.
Ou uma lista vazia quando deveria encontrar algo.
Ou o mesmo resultado repetido.

E você vai precisar saber o que fazer quando isso acontecer.

---

O médico que sabe diagnosticar é mais valioso do que o app que nunca falha.

Um app perfeito é uma abstração.
Um médico que sabe o que fazer quando o app falha — esse é o profissional que você está se tornando."

---

## SEÇÃO 2: CRIAR TELA_BUSCA_RAG.PY — 12 min

**Tom:** Professor explica o contexto antes do prompt — o aluno já sabe construir telas

"Você já construiu várias telas no ClinMd-Tribe.

Cada calculadora tem uma tela.
O dashboard financeiro tem uma tela.

O padrão que você usou em todas elas vale aqui também.
A diferença é que esta tela não calcula — ela busca.

---

Antes de escrever o prompt, visualize o que a tela precisa ter:

Um campo de texto para digitar a pergunta.
Um botão 'Buscar'.
Uma lista onde cada item mostra:
— o trecho encontrado
— o nome do arquivo de onde veio
— o número do trecho

E dois estados especiais:
— 'Nenhum resultado encontrado.' quando a lista estiver vazia
— um indicador de carregamento enquanto a busca roda

---

E uma regra: a tela nunca acessa o ChromaDB diretamente.
A tela chama `busca_service.buscar()`.

Você já aprendeu por que isso importa na aula anterior:
se o ChromaDB for substituído, a tela não precisa mudar.

---

Agora o prompt.

[ler cada parte em voz alta antes de enviar]

```
Crie a tela de busca RAG do ClinMd-Tribe em presentation/telas/tela_busca_rag.py.

A tela deve ter:
  - Um campo de texto para digitar a pergunta
  - Um botão "Buscar"
  - Uma lista de resultados onde cada item mostra:
      • O trecho encontrado (primeiros 300 caracteres)
      • O nome do arquivo de origem em destaque
      • O número do trecho (ex: "Trecho 12")
  - Mensagem "Nenhum resultado encontrado." quando a lista estiver vazia
  - Indicador de carregamento enquanto a busca roda

A tela chama busca_service.buscar() — nunca acessa chromadb diretamente.
Use as cores padrão do ClinMd-Tribe.
Siga o padrão das outras telas do projeto.
```

[enviar o prompt ao Claude Code]

**[TELA: mostrar o Claude Code gerando o arquivo presentation/telas/tela_busca_rag.py]**"

---

"Quatro elementos na tela.

Campo de texto.
Botão.
Lista de resultados com trecho, fonte e número.
Estado vazio com mensagem.

Você não escreveu nenhuma linha de Python.
Você escreveu o prompt.

---

Agora rodar e testar ao vivo.

```bash
uv run flet run main.py
```

**[TELA: mostrar o app abrindo no navegador]**

Navegue até a tela de busca — ela ainda não está no menu.
Por enquanto rode direto: `uv run flet run presentation/telas/tela_busca_rag.py`

Digite: `anticoagulação em FA`
Clique em Buscar.

**[NOTA DE PRODUÇÃO: confirmar que a busca retorna resultados antes de gravar — se a tela abre mas retorna lista vazia, verificar que data/chroma_db/ existe e que os artigos foram indexados na aula_28]**

---

O trecho aparece.
O nome do arquivo aparece embaixo.
O número do trecho aparece.

O médico sabe o que o app encontrou.
O médico sabe de onde veio.

Isso é o que você construiu."

---

## SEÇÃO 3: ADICIONAR TELA DE BUSCA NO MENU DO CLINMD-TRIBE — 5 min

**Tom:** Rápido e prático — o aluno já fez isso antes para outras telas

"O app tem a tela.
Mas a tela ainda não está acessível pelo menu.

O médico não vai digitar comandos no terminal para abrir uma tela.
Ele vai clicar no menu.

---

Mesmo prompt que você usou para adicionar as calculadoras ao menu.

```
Adicione a tela de busca RAG ao menu de navegação do ClinMd-Tribe.
O item do menu deve ter o texto "Busca em Artigos".
Siga o padrão dos outros itens de menu do projeto.
```

[enviar o prompt ao Claude Code]

**[TELA: mostrar o Claude Code atualizando o menu]**"

---

"Agora testar a navegação.

```bash
uv run flet run main.py
```

**[TELA: mostrar o app abrindo — clicar no item 'Busca em Artigos' no menu]**

A tela abre.

---

Digitar 'anticoagulação em FA'.
Clicar em Buscar.
Ver os resultados aparecerem com a fonte embaixo de cada trecho.

O trecho está na tela.
O nome do arquivo aparece.
O médico sabe de qual artigo veio.

---

Seis calculadoras.
Um dashboard financeiro.
Um buscador semântico com interface.

O módulo de RAG do ClinMd-Tribe está funcionando de ponta a ponta."

---

## SEÇÃO 4: PERGUNTA DE SUPERVISÃO — ALGUM `import chromadb` FORA DE `infrastructure/`? — 4 min

**Tom:** Auditoria arquitetural — a regra mais importante do módulo

"Antes de seguir, uma pergunta de supervisão.

É a regra arquitetural mais importante do módulo inteiro.

---

Você aprendeu na aula_27 que apenas um arquivo do projeto pode importar o ChromaDB.

`infrastructure/rag/chroma_repositorio.py`.

Só esse.

---

Após adicionar a tela de busca, vamos verificar que a regra continua valendo.

Três arquivos para verificar:

`domain/rag/porta_busca.py` — tem `import chromadb`? Não deve.
`application/servicos/busca_service.py` — tem `import chromadb`? Não deve.
`presentation/telas/tela_busca_rag.py` — tem `import chromadb`? Não deve.

---

```bash
grep -r "import chromadb" domain/ application/ presentation/
```

**[TELA: mostrar o terminal rodando o comando]**

Output esperado: nenhuma linha.

O grep retorna vazio.

---

Agora verificar onde ele deve aparecer:

```bash
grep -r "import chromadb" infrastructure/
```

**[TELA: mostrar o terminal rodando o comando]**

Output esperado:

```
infrastructure/rag/chroma_repositorio.py:import chromadb
```

Uma linha.
Um único arquivo.

---

Por que isso importa?

Se amanhã sair um banco vetorial melhor que o ChromaDB —
você troca um arquivo.

`infrastructure/rag/chroma_repositorio.py`.

Só esse.

A tela não sabe que mudou.
O serviço não sabe que mudou.
O domínio não sabe que mudou.

Apenas a infraestrutura sabe.
E a infraestrutura é o único lugar que pode mudar.

---

Isso é Clean Architecture protegendo o seu trabalho."

---

## SEÇÃO 5: `.gitignore` — ADICIONAR `knowledge_base/` E `data/chroma_db/` — 3 min

**Tom:** Rápido e direto — analogia com o clinmd.db da aula_25

"Você lembra da aula_25.

O banco de dados `clinmd.db` ficou no `.gitignore`.

O raciocínio: dados locais não sobem para o repositório.
O banco do médico A não deve ir para a máquina do médico B.

---

O mesmo raciocínio vale aqui.

`knowledge_base/` — os artigos que você baixou do PubMed.
`data/chroma_db/` — o banco vetorial gerado a partir desses artigos.

Esses diretórios são dados locais.
Cada médico vai ter os seus próprios artigos.
Cada médico vai ter o seu próprio banco vetorial.

Não devem ir para o repositório compartilhado.

---

```
Adicione ao .gitignore do projeto:
  knowledge_base/
  data/chroma_db/

Esses diretórios são dados locais — artigos e banco vetorial.
Cada médico vai ter os seus próprios artigos e seu próprio banco.
Não devem ir para o repositório.
```

[enviar o prompt ao Claude Code]

**[TELA: mostrar o Claude Code atualizando o .gitignore]**

---

E aqui tem uma camada de LGPD.

Os artigos que você indexou podem conter dados sensíveis.
O banco vetorial é derivado desses artigos.

Ambos ficam na máquina de quem usa.
Não no repositório compartilhado.

O código sobe.
Os dados ficam."

---

## SEÇÃO 6: QUALIDADE DA BUSCA — 3 DIAGNÓSTICOS AO VIVO — 14 min

**Tom:** Médico diagnosticando o app — cada problema tem sintoma, causa e tratamento

"O app está funcionando.

Mas às vezes a busca vai retornar resultados ruins.

Trechos sem sentido.
Lista vazia para perguntas que deveriam encontrar algo.
O mesmo resultado aparecendo duas vezes.

Isso não é defeito do conceito.
É configuração.

E assim como o médico diagnostica pelo sintoma —
você vai aprender a diagnosticar pelo que a busca retorna.

---

Três diagnósticos."

---

**Diagnóstico 1 — Trechos muito curtos ou sem sentido:**

"Sintoma: você pergunta sobre 'protocolo de anticoagulação peri-operatória' e o resultado retornado é:

```
et al. (2019). Journal of Cardiology.
```

Uma referência bibliográfica.
Não um trecho clínico.

---

Causa: o indexador incluiu trechos muito curtos — referências, rodapés, fragmentos.
O filtro de tamanho mínimo está baixo demais.

---

O indexador da aula_27 já filtra trechos com menos de 150 caracteres.
Mas referências bibliográficas costumam ter mais de 150 caracteres.

Solução: aumentar o critério de tamanho mínimo para 200.

```
Em infrastructure/rag/txt_loader.py, aumente o critério de tamanho mínimo do trecho para 200 caracteres.
```

[enviar o prompt ao Claude Code]

---

Depois de implementar: deletar o banco vetorial e reindexar.

```bash
rm -rf data/chroma_db/
uv run python - <<'EOF'
from application.servicos.indexador_service import indexar_pasta
indexar_pasta('knowledge_base/')
EOF
```

**[NOTA DE PRODUÇÃO: mostrar o terminal rodando a reindexação — confirmar que os trechos retornados após o ajuste são melhores]**

Os trechos curtos não vão mais aparecer.
O filtro mais rigoroso elimina referências bibliográficas e fragmentos.

Sintoma resolvido."

---

**Diagnóstico 2 — Lista vazia para perguntas que deveriam encontrar algo:**

"Sintoma: você pergunta sobre 'dose de varfarina em idoso' — lista vazia.
Mas você tem certeza que um dos artigos fala sobre isso.

---

Duas causas possíveis.

**Causa A: o arquivo .txt está vazio.**

O PubMed nem sempre fornece o texto completo dos artigos.
Às vezes o .txt foi criado mas está vazio — só o título e o abstract.

Verificar: abrir o arquivo .txt correspondente e checar se tem conteúdo clínico.

Se vazio: buscar outro artigo com texto disponível no PubMed e reindexar.

---

**Causa B: o artigo está em inglês e a busca foi feita em português.**

Os modelos de embedding têm desempenho melhor quando a pergunta e o artigo estão no mesmo idioma.

Tentar buscar em inglês:

```bash
uv run python - <<'EOF'
from application.servicos.busca_service import buscar
for r in buscar('warfarin dosing elderly', n=2):
    print(r.fonte, r.trecho[:150])
EOF
```

**[TELA: mostrar o terminal rodando o comando]**

---

Se retornou resultados em inglês mas não em português:
a causa era o idioma da busca.

Isso é uma limitação real do RAG com artigos em inglês.
Buscar em inglês pode funcionar melhor quando os artigos estão em inglês.

---

Para o médico: quando o artigo estiver em inglês e a busca não encontrar —
tente reformular a pergunta em inglês.
O app vai encontrar."

---

**Diagnóstico 3 — Resultados repetidos:**

"Sintoma: o mesmo trecho aparece duas vezes no resultado.

```
Fonte: 39123456_anticoagulation_fa.txt | Trecho 4
The CHA₂DS₂-VASc score...
---
Fonte: 39123456_anticoagulation_fa.txt | Trecho 4
The CHA₂DS₂-VASc score...
---
```

---

Causa: o indexador rodou mais de uma vez sem idempotência correta.
Os IDs dos vetores não eram determinísticos — o mesmo trecho foi inserido duas vezes com IDs diferentes.

---

Diagnóstico via terminal:

```bash
uv run python - <<'EOF'
from application.servicos.busca_service import buscar
r = buscar('anticoagulação', n=6)
fontes = [f'{x.fonte}_{x.numero_trecho}' for x in r]
print(fontes)
print('duplicatas:', len(fontes) - len(set(fontes)))
EOF
```

**[TELA: mostrar o terminal rodando o comando]**

Se `duplicatas:` retornar um número maior que zero — há duplicatas no banco.

---

Solução: deletar o banco e reindexar uma vez.

```bash
rm -rf data/chroma_db/
uv run python - <<'EOF'
from application.servicos.indexador_service import indexar_pasta
indexar_pasta('knowledge_base/')
EOF
```

O `upsert` do ChromaDB vai garantir que cada trecho seja inserido apenas uma vez.

---

Três diagnósticos.
Três tratamentos.

O médico que sabe diagnosticar o app é mais valioso do que o app perfeito.

Porque nenhum app é perfeito.
Mas todo problema tem causa.
E toda causa tem solução."

---

## SEÇÃO 7: ENCERRAMENTO + BRIDGE S08 + DEVER DE CASA — 4 min

**Tom:** Consolidar o módulo inteiro — de quatro aulas para um produto funcionando

"O módulo S07 está encerrado.

O que você construiu em quatro aulas:

Aula_27: entendeu embeddings e Clean Architecture. Indexou os primeiros artigos no ChromaDB.
Aula_28: baixou artigos do PubMed via MCP. Construiu o knowledge_base com artigos reais.
Aula_29: validou os três gabaritos no terminal. O buscador funcionou — com rastreabilidade, com semântica, sem invenção.
Aula_30: ligou o buscador na interface Flet. Aprendeu a diagnosticar quando a busca está ruim.

---

Seis calculadoras.
Um dashboard financeiro.
Um buscador semântico que lê artigos e cita a fonte.

---

Pense no que aconteceu em quatro aulas.

Você usou o MCP do PubMed — que aprendeu na aula_03 — para construir uma feature de IA.
O conhecimento acumulou.

Uma habilidade que parecia isolada — usar o MCP para buscar artigos —
virou o bloco de entrada de um sistema RAG completo.

É assim que o ClinMd-Tribe cresce.
Cada módulo usa o que veio antes.

---

O S08 é completamente diferente.

Não é sobre saber.
É sobre não esquecer.

O médico sabe que existe um protocolo de sedação para procedimentos.
Mas em situação de urgência — com o paciente instável — ele pode pular uma etapa.

O S08 é o módulo de checklists.
Estilo OMS.

Você vai construir um app que acompanha procedimentos passo a passo.
Cada item marcado.
Timestamp registrado.
O app que não deixa você pular uma etapa.

---

Dever de casa:

Antes da próxima aula, teste o Diagnóstico 1.

Aumente o mínimo de caracteres para 200 em `txt_loader.py`.
Delete o banco vetorial e reindexe.

```bash
rm -rf data/chroma_db/
uv run python - <<'EOF'
from application.servicos.indexador_service import indexar_pasta
indexar_pasta('knowledge_base/')
EOF
```

Faça a mesma busca de antes — 'anticoagulação em FA'.
Compare os trechos retornados com os de antes.

Observe a diferença.
Registre o que mudou.

Esse exercício vai consolidar o diagnóstico que você aprendeu hoje."

---

**FIM DO ROTEIRO**
