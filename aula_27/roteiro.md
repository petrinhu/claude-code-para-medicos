# Aula 27 — RAG: O Residente que Leu Todos os Guidelines

**Formato:** Gravada em um take no OBS Studio
**Duração:** ~42 min
**Tom:** Cardiologista que quer que o app saiba o que está nos artigos que ele lê
**Módulo:** S07.01 — RAG: O que é e por que importa

---

## SEÇÃO 1: ABERTURA — 3 min

**Tom:** Contraste direto com S06 — o app que calcula e guarda, mas não lê

"Nas últimas seis aulas você construiu um app que calcula e guarda.

Seis calculadoras clínicas.
Um dashboard financeiro que persiste entre sessões.

O app processa o que você digita.
Mas não lê o que você já tem.

---

Você tem artigos salvos.
Guidelines em PDF.
Protocolos que você consultou na última internação.

Se você perguntar para o seu app:
'Quando suspender a anticoagulação antes de uma cardioversão?'

Ele não sabe.

Porque ninguém ensinou a ele o que está nos seus artigos.

---

Isso muda hoje.

Hoje o ClinMd-Tribe aprende a ler.

E quando você perguntar algo que ele não sabe — ele vai dizer que não sabe.

Isso pode parecer fraqueza.
Mas é o que diferencia IA confiável de IA que inventa.

---

O personagem de hoje é um cardiologista.

Especialista em arritmias.
Acompanha pacientes com fibrilação atrial há dez anos.
Tem uma pasta com artigos sobre anticoagulação que ele consultou ao longo da carreira.

Hoje esses artigos viram a memória do app."

---

## SEÇÃO 2: ANALOGIA — O RESIDENTE QUE LEU TUDO — 5 min

**Tom:** Narrativo. A analogia deve ser cristalina antes de mostrar qualquer técnica.

"Você já trabalhou com um residente que leu tudo.

Não o que chuta.
O que leu o Harrison, os guidelines, os artigos do NEJM.

Quando você pergunta: 'qual a dose de rivaroxabana em FA com função renal reduzida?'
Ele responde: 'está na diretriz de 2022, página 14, segunda coluna.'

Ele não inventou.
Ele leu e aponta a fonte.

---

E quando você pergunta algo que não está nos artigos que ele leu?

Ele diz: 'não tenho isso aqui, doutor.'

Não chuta.
Não tenta parecer que sabe.

---

O RAG é exatamente isso.

RAG: Retrieval-Augmented Generation.
Geração augmentada por recuperação.

Tradução clínica:
o app vai buscar nos artigos antes de responder.
E vai te dizer de qual artigo veio.

---

Três etapas:

Primeiro: você entrega os artigos para o app indexar.
O app lê, divide em trechos, guarda o 'sabor' de cada trecho.

Segundo: você faz uma pergunta.
O app compara o 'sabor' da pergunta com o 'sabor' de cada trecho.
Traz os mais parecidos.

Terceiro: você vê o trecho e a fonte.
Sem inventar. Sem misturar.

---

'Sabor' — isso é uma metáfora.

O nome técnico é embedding.

E é aí que está a mágica."

---

## SEÇÃO 3: O QUE É EMBEDDING — 7 min

**Tom:** Didático, sem fórmulas. A ideia central: significado virou número.

"Embedding é uma palavra técnica para uma ideia simples.

Toda palavra, toda frase, todo parágrafo
pode ser representado como uma lista de números.

Não os caracteres.
O significado.

---

Pense numa escala de dor.

Zero é sem dor.
Dez é insuportável.

Se eu disser 'dor torácica intensa' — esse paciente está onde na escala?
Próximo ao dez.

Se eu disser 'desconforto leve no peito' — onde está?
Em torno do quatro.

Esses dois pacientes têm sintomas parecidos.
Eles estão próximos na escala.

---

Embedding faz isso para qualquer texto.
Mas com muito mais dimensões.

Não uma escala de um a dez.
Centenas de escalas simultâneas.

Urgência. Localização. Órgão. Gravidade. Tempo.

---

O resultado:

'Dor torácica intensa' e 'angina pectoris' ficam próximos nesse espaço.

'Como tratar diabetes tipo 2' fica longe.

Não porque alguém programou isso.
Porque o modelo aprendeu, lendo bilhões de frases médicas,
que essas expressões têm o mesmo significado.

---

Busca semântica é isso:
você pergunta em linguagem natural,
o sistema encontra os trechos mais próximos no espaço do significado.

Não a mesma palavra.
O mesmo sentido."

---

## SEÇÃO 4: DEMO AO VIVO — EMBEDDING — 10 min

**Tom:** Professor roda o script. Aluno observa o output. Zero explicação de código.

"Vou mostrar isso acontecendo.

Tenho um script preparado.
Não quero que você leia o código agora.
Quero que você veja o resultado."

---

**[TELA: rodar no terminal, SEM abrir o arquivo do script; o aluno vê só o resultado na tela, nunca o código]**

```
uv run python aula_27/resources/demo_embedding.py
```

**[NOTA DE PRODUÇÃO: na primeira execução o modelo é baixado (~90MB). Rodar antes da gravação para o modelo já estar em cache. Se aparecer barra de download durante a gravação: pausar o OBS, aguardar o download concluir, reiniciar o take da seção 4.]**

**[OUTPUT — aproximado:]**

```
Referência: 'dor torácica intensa'

  0.71  ██████████████  angina pectoris
  0.46  █████████       fibrilação atrial com flutter
  0.39  ████████        prescrição de varfarina
  0.21  ████            como tratar diabetes tipo 2
```

---

"Olha o que aconteceu.

Ninguém disse para o sistema que 'angina pectoris' e 'dor torácica' são a mesma coisa.

O modelo aprendeu isso lendo textos médicos.

O número 0.71 significa: esses dois conceitos ficam muito próximos no espaço do significado.

Diabetes — 0.21. Longe.
Varfarina — 0.39. Mais próximo. Faz sentido: é um medicamento cardiovascular.

---

É assim que o RAG funciona.

Você pergunta.
O sistema calcula a distância entre a sua pergunta e cada trecho dos artigos.
Traz os mais próximos.

E te diz de qual artigo veio.

Sem inventar. Sem misturar."

---

## SEÇÃO 5: ARQUITETURA RAG — 8 min

**Tom:** Visual e claro. Mostrar o fluxo completo antes de construir.

"Antes de construir, deixa eu mostrar o que vai existir no final.

Quatro etapas. Quatro lugares.

---

**Etapa 1: Baixar**

Você pede para o Claude Code buscar artigos no PubMed.
Ele usa o MCP — o mesmo conector que você usou na aula três.
Os artigos chegam como arquivos de texto em uma pasta chamada `knowledge_base/`.

**Etapa 2: Indexar**

Um script lê todos os `.txt`.
Divide em trechos.
Calcula o embedding de cada trecho.
Guarda em um banco vetorial local — o ChromaDB.

O ChromaDB é para embeddings o que o SQLite é para tabelas.
Persistente, local, sem servidor.

**Etapa 3: Buscar**

Você digita uma pergunta.
O sistema calcula o embedding da pergunta.
Compara com os embeddings guardados.
Traz os trechos mais próximos.
Com o nome do arquivo de onde veio.

**Etapa 4: Exibir**

A tela Flet mostra o resultado:
o trecho e a fonte.
O médico vê e decide.

---

Esses quatro passos respeitam as quatro camadas da Clean Architecture
que você aprendeu na aula quinze.

**[TELA: mostrar a estrutura de pastas do projeto — presentation/, application/, domain/, infrastructure/]**

O ChromaDB fica na camada de infraestrutura.
A lógica de busca fica no domínio e na aplicação.
A tela fica na apresentação.

Cada camada cuida do que é dela."

---

## SEÇÃO 6: O QUE VEM A SEGUIR — 5 min

**Tom:** Mapa claro das próximas três aulas.

"Quatro aulas. Quatro etapas. Aqui está o mapa.

---

**Aula de hoje — aula vinte e sete:**
Você entendeu o conceito.
O que é embedding.
Como o RAG funciona.
Qual é a arquitetura.

Nenhum prompt ainda. Só o mapa.

**Aula vinte e oito:**
Você vai ao PubMed com o Claude Code.
Baixa três artigos sobre anticoagulação em FA.
Constrói o indexador.
No final: uma pasta `knowledge_base/` com artigos reais
e um banco vetorial com todos os trechos.

**Aula vinte e nove:**
Você pergunta ao banco vetorial.
Testa no terminal.
O clímax: você pergunta algo que não está nos artigos — e o app diz que não sabe.

**Aula trinta:**
Você liga tudo na tela Flet.
E aprende a diagnosticar quando a busca está ruim.

---

Quatro aulas. Um módulo.

No final, o ClinMd-Tribe vai ter uma feature que a maioria dos apps clínicos comerciais não tem:
ele vai citar a fonte."

---

## SEÇÃO 7: ENCERRAMENTO — 3 min

**Tom:** A frase que fica. Confiança como critério.

"Antes de encerrar, quero deixar uma ideia que vai guiar as próximas aulas.

---

O que diferencia o residente que você confia do que você não confia?

Não é o que ele sabe.

É o que ele faz quando não sabe.

O que não confia — chuta.
O que confia — diz: 'não tenho isso aqui, doutor.'

---

O RAG que vamos construir vai fazer a mesma coisa.

Se você perguntar algo que não está nos artigos indexados,
o app vai retornar uma lista vazia.

Não vai inventar.
Não vai misturar.

---

Isso parece pouco.

Mas para um médico que precisa de informação confiável,
uma resposta vazia e honesta
vale mais do que uma resposta completa e inventada.

Esse é o comportamento que vamos construir:
um app que admite quando não sabe.

Ele não chuta. Ele admite que não sabe.

E isso, no contexto clínico, é segurança.

---

Na próxima aula: PubMed, `knowledge_base/`, e o indexador.

Vejo você lá."

---

**FIM DO ROTEIRO**
