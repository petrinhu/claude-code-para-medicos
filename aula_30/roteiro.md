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

**[NOTA DE PRODUÇÃO: a tela_busca_rag ainda não está no menu — o Flet vai abrir, mas a tela de busca só aparecerá após a Seção 3. Esta execução é para confirmar que o app não quebrou.]**

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

"Agora rodamos o app completo — com a tela de busca no menu:

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

## SEÇÃO 4: PERGUNTA DE SUPERVISÃO: SÓ A INFRAESTRUTURA CONHECE O CHROMADB? (4 min)

**Tom:** Auditoria arquitetural; a regra mais importante do módulo

"Antes de seguir, uma pergunta de supervisão.

É a regra arquitetural mais importante do módulo inteiro.

---

Você viu na aula_27 o ChromaDB no seu lugar na arquitetura, e cravou a regra nas aulas_28 e 29: apenas um lugar do projeto pode conhecer o ChromaDB.

A camada de infraestrutura.

Só ela.

---

Após adicionar a tela de busca, vamos confirmar que a regra continua valendo.

Pense em quem NÃO pode conhecer o banco:

A tela de busca, que você acabou de criar.
O serviço de busca, que a tela chama.
O domínio, que define o contrato.

Nenhum dos três pode falar com o ChromaDB diretamente.
Só a infraestrutura pode.

---

Em vez de você ir caçar isso arquivo por arquivo, peça o laudo ao Claude.
Igual a pedir um exame e ler o resultado, não a fórmula.

```
Faça uma auditoria de arquitetura no ClinMd-Tribe e me responda em portugues, sem me mostrar nenhum codigo:

1. Apenas a camada de infraestrutura conhece o ChromaDB diretamente?
2. Alguma tela, algum servico ou o dominio fala com o ChromaDB sem passar pela infraestrutura? Liste se houver.
3. Conclua: se eu trocar o banco vetorial amanha, isso mexeria em quantos lugares do projeto?

Responda so com o laudo em portugues. Nao cole codigo.
```

[enviar o prompt ao Claude Code]

**[TELA: mostrar o Claude Code respondendo o laudo em texto, sem código]**

Laudo esperado: só a infraestrutura conhece o ChromaDB. Tela, serviço e domínio passam por ela. Trocar o banco mexeria em um único lugar.

---

Por que isso importa?

Se amanhã sair um banco vetorial melhor que o ChromaDB,
você troca um único lugar.

A camada de infraestrutura.

Só ela.

A tela não sabe que mudou.
O serviço não sabe que mudou.
O domínio não sabe que mudou.

Apenas a infraestrutura sabe.
E a infraestrutura é o único lugar que pode mudar.

---

Isso é Clean Architecture protegendo o seu trabalho.
A tela, o serviço e o domínio nem sabem que o ChromaDB existe;
por isso o dia da troca é trabalho de um lugar só, não do projeto inteiro."

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

O indexador da aula_28 já descarta os trechos muito curtos.
Mas referências bibliográficas costumam passar desse corte mínimo.

Solução: subir o critério de tamanho mínimo do trecho para 200 caracteres.

```
Em infrastructure/rag/txt_loader.py, aumente o critério de tamanho mínimo do trecho para 200 caracteres.
```

[enviar o prompt ao Claude Code]

---

Depois de implementar: deletar o banco vetorial e reindexar.

O comando de reindexação é o mesmo módulo que você rodou na aula_28.
Você só executa e vê o resultado; não há código para ler.

```bash
rm -rf data/chroma_db/
uv run python -m application.servicos.indexador_service
```

**[NOTA DE PRODUÇÃO: mostrar o terminal rodando a reindexação; confirmar que os trechos retornados após o ajuste são melhores]**

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

Para testar essa hipótese, peça ao Claude para fazer a mesma busca em inglês e te dar o veredito em português.

```
Teste a busca do ClinMd-Tribe por "warfarin dosing elderly", em ingles.
Me diga em portugues se voltou algum resultado e de qual artigo, sem me mostrar codigo.
```

[enviar o prompt ao Claude Code]

**[TELA: mostrar o Claude Code respondendo em português se a busca em inglês voltou resultado]**

---

Se a busca em inglês retornou resultados mas a busca em português não:
a causa era o idioma da busca.

Isso é uma limitação real do RAG com artigos em inglês.
Buscar em inglês pode funcionar melhor quando os artigos estão em inglês.

---

Para o médico: quando o artigo estiver em inglês e a busca não encontrar —
tente reformular a pergunta em inglês.
O app vai encontrar.

---

Se precisar de artigos em português, use o prompt:

```
Busque 1 artigo sobre [tema] no PubMed que tenha abstract em português. Salve em knowledge_base/.
```

Depois reindexe normalmente. O banco combina artigos em inglês e português — cada busca vai encontrar nos dois idiomas."

---

**Diagnóstico 3 — Resultados repetidos:**

"Sintoma: o mesmo trecho aparece duas vezes no resultado.

Na tela você vê algo assim: o trecho do escore CHA2DS2-VASc, vindo da fonte anticoagulation_fa, trecho número 4. E logo abaixo, de novo, o mesmo trecho do escore CHA2DS2-VASc, da mesma fonte anticoagulation_fa, com o mesmo número 4. Texto idêntico, fonte idêntica, número idêntico. Repetido.

---

Causa: o indexador rodou mais de uma vez sem idempotência correta.
O mesmo trecho foi guardado duas vezes no banco com identificadores diferentes, então a busca devolve o repetido.

---

Diagnóstico: peça ao Claude para conferir se o banco tem trechos duplicados.

```
Verifique se o banco do ClinMd-Tribe tem trechos duplicados.
Busque "anticoagulacao" e me diga, em portugues, se algum trecho aparece repetido (mesma fonte e mesmo numero de trecho), sem me mostrar codigo.
```

[enviar o prompt ao Claude Code]

**[TELA: mostrar o Claude Code respondendo em português se há trechos repetidos]**

Se o Claude apontar trechos com a mesma fonte e o mesmo número aparecendo mais de uma vez, há duplicatas no banco.

---

Solução: deletar o banco e reindexar uma vez.
Mesmo módulo de reindexação da aula_28; você só roda e vê o resultado.

```bash
rm -rf data/chroma_db/
uv run python -m application.servicos.indexador_service
```

Ao reindexar do zero, cada trecho entra no banco uma única vez, e a repetição desaparece.

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

Aula_27: entendeu embeddings, RAG e onde cada peça mora na Clean Architecture. Só o mapa, sem prompt.
Aula_28: baixou artigos do PubMed via MCP, construiu o knowledge_base e indexou os primeiros trechos no ChromaDB.
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

Na aula trinta e um você começa o S08 — o primeiro checklist.

Você vai construir um app que acompanha procedimentos passo a passo.
Cada item marcado.
Timestamp registrado.
O app que não deixa você pular uma etapa.

---

Dever de casa:

Antes da próxima aula, teste o Diagnóstico 1.

Peça ao Claude para aumentar o mínimo de caracteres para 200 no carregador de artigos.
Delete o banco vetorial e reindexe com o mesmo módulo da aula_28; você só roda e vê o resultado.

```bash
rm -rf data/chroma_db/
uv run python -m application.servicos.indexador_service
```

Depois, peça ao Claude para fazer a busca por 'anticoagulação em FA' e te mostrar, em português, os trechos retornados.
Compare com os trechos que você via antes do ajuste.

Observe a diferença.
Registre o que mudou.

Esse exercício vai consolidar o diagnóstico que você aprendeu hoje."

---

**FIM DO ROTEIRO**
