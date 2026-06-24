# Aula 03 — PubMed + Fichamento e Leitura Crítica

**Formato:** Gravada no OBS Studio, editada no Kdenlive  
**Duração:** ~55 min  
**Tom:** Colega com humor leve e didático  

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta desta aula.
- [ ] Sessão limpa, sem conversa anterior carregada (a demo nasce do zero).
- [ ] Conector PubMed (plugin `pubmed@life-sciences` da Anthropic) já instalado e ativo num perfil de backup, para o caso de a instalação ao vivo da Seção 4 falhar na gravação. Confirme com `/mcp` que ele aparece como ativo.

**Confira antes de gravar:**

- [ ] Internet ativa (o MCP do PubMed busca online em tempo real).
- [ ] Faça uma busca de teste no PubMed (ex.: 'atrial fibrillation') e descarte, para confirmar que o conector responde antes de gravar.
- [ ] Tenha em mente que os artigos retornados variam a cada busca (a aula já avisa o aluno disso); o que importa é o fluxo, não a lista exata.

**Navegador:** nenhum site é necessário nesta aula (a busca no PubMed acontece dentro do Claude Code, via MCP).

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Direto, conectando com a aula anterior, elevando o nível

**[Aviso rápido dos óculos, antes de mergulhar]**

"Rapidinho, antes de começar: hoje a gente vai ler títulos de artigo e abstract direto no terminal, e essa fonte às vezes encolhe que nem rótulo de ampola. Quem usa óculos pra perto, separa eles agora. A gente não vai diagnosticar de longe hoje, vai ler de perto. Combinado? Bora."

"Na aula passada a gente trabalhou com arquivos locais — PDFs que estavam
no seu computador, planilhas que você já tinha, slides que você montou.

Hoje a gente sobe um degrau.

Ao invés de trabalhar com o que você já tem, a gente vai buscar
evidência científica diretamente do PubMed — sem abrir o navegador,
sem copiar e colar resumo, sem perder tempo em interface.

Tudo dentro do Claude Code.

E no final, você vai sair com uma ficha de leitura crítica pronta
para apresentar em reunião clínica.

Vamos lá."

---

## SEÇÃO 2: O CENÁRIO (3 min)

**Tom:** Situação real, tensão clínica, resolução com Claude Code

"Cenário de hoje.

Você está na visita da enfermaria, terça de manhã.
O chefe de equipe vira pra você e fala:
'Na reunião clínica de amanhã quero evidência atual sobre anticoagulação
em fibrilação atrial não-valvar. Me traz o que saiu de novo nos últimos 2 anos.'

Silêncio.

Você podia abrir o PubMed, pesquisar manualmente, filtrar por data,
baixar 10 artigos, ler os abstracts um por um, selecionar os relevantes,
fazer fichamento à mão, classificar nível de evidência...

São facilmente 3 horas de trabalho.

Ou.

Você abre o Claude Code, conecta no PubMed, e deixa ele fazer isso por você
enquanto você termina a visita.

É isso que a gente vai fazer agora."

---

## SEÇÃO 3: O QUE É MCP (5 min)

**Tom:** Explicativo, analogia clínica forte, sem jargão

"Antes de conectar no PubMed, preciso explicar uma coisa.

Como é que o Claude Code consegue acessar o PubMed se ele é só
um assistente de texto?

A resposta se chama MCP — Model Context Protocol.

Não precisa decorar o nome. Precisa entender o conceito.

Pensa assim: você tem um eletrocardiógrafo no consultório.
O equipamento sabe interpretar sinais elétricos.
Mas pra registrar o traçado do coração do paciente,
você precisa de cabos — os eletrodos — que conectam o paciente à máquina.

O Claude Code é a máquina. Ele já sabe raciocinar, sintetizar, responder.
O MCP é o cabo que conecta ele a uma fonte de dados externa.

Neste caso: o PubMed.

Existem conectores MCP pra muita coisa além do PubMed.
Google Calendar. Planilhas online. Banco de dados de medicamentos.
Sistemas de agendamento. Cada um é um 'cabo' diferente.

A gente instala o cabo uma vez — e o Claude passa a enxergar aquela fonte
em todas as conversas futuras.

É como calibrar o ECG uma vez e usar pra sempre.

Entendeu o conceito? Ótimo. Vamos instalar."

---

## SEÇÃO 4: SETUP DO MCP PUBMED (8 min)

**Tom:** Pausado, didático, mostrando cada passo com calma

"A própria Anthropic, a empresa que faz o Claude, mantém um pacote pronto de
conectores para ciências da vida, e o PubMed está dentro dele. A gente não precisa
caçar nada por fora: instala direto.

Primeiro passo, dentro do Claude Code, vocês digitam este comando, que adiciona o
catálogo de conectores de ciências da vida da Anthropic:

```
/plugin marketplace add anthropics/life-sciences
```

[colar e executar]

Agora instala o conector do PubMed a partir desse catálogo:

```
/plugin install pubmed@life-sciences
```

[aguardar instalação]

Pode aparecer uma confirmação na tela. Confirmem.

[aguardar]

Pronto. O conector está instalado.

Agora reiniciem o Claude Code para ele reconhecer o novo conector:

```
claude
```

[reiniciar]

E pra conferir que o PubMed está mesmo plugado, digitem:

```
/mcp
```

[mostrar que o PubMed aparece na lista de conectores ativos]

Lá está ele. Conector do PubMed, ativo.

Uma coisa importante: isso foi feito uma única vez.
Da próxima vez que vocês abrirem o Claude Code, o PubMed já vai estar lá.
Não precisam repetir este passo.

É como instalar o cabo do ECG na primeira vez: depois fica plugado.

Vamos testar? Vou digitar uma pergunta simples pra confirmar que está funcionando:

```
O conector do PubMed está ativo? Faça uma busca rápida por 'atrial fibrillation' 
e me mostre o título do primeiro artigo encontrado.
```

[executar e mostrar que o Claude acessou o PubMed]

Funcionou. O Claude está conectado ao PubMed.

Agora a busca de verdade."

---

## SEÇÃO 5: DEMO — BUSCA NO PUBMED (10 min)

**Tom:** Focado, mostrando a construção do prompt de busca

"Vamos buscar evidência atual sobre anticoagulação em FA não-valvar.

A chave aqui é o prompt. Quanto mais específico, melhor o resultado.
Lembra da regra de ouro da aula de abertura? Prompt vago, resposta vaga.

Vou construir o prompt em camadas, pra vocês verem a diferença.

Prompt básico — ruim:

```
Busque artigos sobre fibrilação atrial.
```

Isso vai trazer 50 mil resultados. Inútil.

Agora o prompt que vou usar de verdade:

```
Use o PubMed para buscar artigos sobre anticoagulação em fibrilação atrial não-valvar.
Filtros obrigatórios:
- Publicados entre 2022 e 2024
- Tipos de estudo: ensaios clínicos randomizados, metanálises ou revisões sistemáticas
- Idioma: inglês ou português
Me retorne os 5 artigos mais relevantes com: título, autores, ano, revista e abstract resumido em 3 bullets.
```

[executar e mostrar resultado]

Olha a diferença.

5 artigos. Todos recentes. Todos com design metodológico forte — RCT ou metanálise.
Cada um com abstract resumido em bullets, pronto para eu ler.

Isso que levaria 40 minutos de pesquisa manual saiu em 30 segundos.

E lembrem: os artigos que aparecem pra vocês podem ser diferentes dos meus.
O PubMed tem milhões de papers, o Claude seleciona com base nos critérios,
mas a seleção pode variar. Isso é normal — o processo é o que importa, não a lista exata."

---

## SEÇÃO 6: DEMO — TRIAGEM DOS RESULTADOS (7 min)

**Tom:** Crítico, ensinando a hierarquia de evidência de forma prática

"Tenho 5 artigos. Mas pra reunião clínica de amanhã, preciso de no máximo 2.
Quais são os mais relevantes?

Eu poderia ler todos os abstracts e decidir.
Ou posso pedir pro Claude fazer a triagem com critério clínico.

Prompt de triagem:

```
Dos 5 artigos que você encontrou, selecione os 2 mais relevantes para apresentar
em uma reunião clínica sobre anticoagulação em FA não-valvar.
Critérios de prioridade, nesta ordem:
1. Metanálise ou revisão sistemática com metanálise
2. Ensaio clínico randomizado de alta qualidade
3. Guideline de sociedade internacional (ESC, AHA, SBC)
Descarte: relato de caso, carta ao editor, opinião de especialista sem dados.
Justifique a escolha de cada um em 2 frases.
```

[executar e mostrar resultado]

Pronto. Dois artigos, com justificativa clínica da escolha.

Isso é hierarquia de evidência aplicada na prática — Oxford, GRADE, o que for.
O princípio é o mesmo: metanálise > RCT > coorte > caso-controle > relato de caso.

O Claude não inventa isso — ele aplica o que já está na literatura de metodologia.

Agora pego o artigo mais relevante e faço o fichamento completo."

---

## SEÇÃO 7: DEMO — FICHAMENTO E LEITURA CRÍTICA (15 min)

**Tom:** Metódico, ensinando cada componente da leitura crítica

"Aqui está o coração da aula.

Leitura crítica não é ler o artigo inteiro. É extrair o que importa
de forma estruturada — PICO, nível de evidência, vieses.

Vou pegar o artigo mais relevante da triagem e fazer o fichamento completo.

Prompt:

```
Faça um fichamento completo de leitura crítica do artigo mais relevante que você selecionou.
Estruture assim:

1. REFERÊNCIA COMPLETA
   Título, autores, revista, ano, DOI

2. PICO
   P — Pacientes/População: quem foram os participantes?
   I — Intervenção: o que foi testado?
   C — Comparação: qual foi o controle ou comparador?
   O — Outcome/Desfecho: o que foi medido? Qual foi o resultado principal?

3. DESENHO DO ESTUDO
   Tipo de estudo, tamanho amostral, duração do seguimento

4. NÍVEL DE EVIDÊNCIA
   Classificação Oxford (1a a 5) ou GRADE (alta/moderada/baixa/muito baixa)
   Justifique a classificação

5. VIESES PRINCIPAIS
   Para cada viés abaixo, avalie se está presente, ausente ou incerto:
   - Viés de seleção (randomização adequada?)
   - Viés de aferição (desfechos cegos?)
   - Viés de confundimento (grupos comparáveis no baseline?)
   - Viés de publicação (resultados negativos suprimidos?)

6. MENSAGEM CLÍNICA PRINCIPAL
   Em 2 frases: o que este artigo muda (ou não muda) na prática clínica?
```

[executar e mostrar resultado]

Olha o que saiu.

PICO completo. Nível de evidência com justificativa.
Vieses avaliados um a um. Mensagem clínica em 2 frases.

Isso é exatamente o que o chefe de equipe quer amanhã na reunião.

E percebam o tempo que isso levou — menos de 1 minuto.
Versus fazer isso à mão: 20, 30 minutos por artigo.

Uma observação importante: o Claude está fazendo essa análise com base
no abstract e nos metadados disponíveis no PubMed.
Para uma análise mais profunda, você pode baixar o PDF do artigo,
anexar ao Claude e pedir o mesmo fichamento com acesso ao texto completo.
O resultado vai ser ainda mais detalhado.

Mas pra triagem inicial? O que saiu aqui já é ouro."

---

## SEÇÃO 8: ENCERRAMENTO + DEVER DE CASA (5 min)

**Tom:** Motivador, resumo rápido, desafio concreto

"Resumo do que a gente fez hoje.

Saímos de um pedido do chefe — 'me traz evidência sobre anticoagulação em FA' —
e chegamos em ficha de leitura crítica pronta, em menos de 1 hora.

O fluxo foi:
1. Entender o que é MCP — o cabo que conecta Claude a fontes externas
2. Instalar o conector do PubMed — uma vez só
3. Busca estruturada com filtros — tipo de estudo, ano, idioma
4. Triagem com hierarquia de evidência — o que priorizar e por quê
5. Fichamento completo — PICO, nível de evidência, vieses, mensagem clínica

Esse fluxo funciona pra qualquer tema. FA hoje, sepse amanhã, diabetes depois.
O processo é idêntico.

Agora o dever de casa.

Antes da próxima aula, quero que vocês façam isso:

Pensem em um tema da sua especialidade que vocês precisam se atualizar.
Abram o Claude Code, conectem no PubMed, e busquem 3 artigos recentes com este prompt:

```
Use o PubMed para buscar os 3 artigos mais recentes e relevantes sobre [SEU TEMA].
Filtre por: últimos 2 anos, ensaios clínicos ou metanálises.
Me retorne título, ano e abstract em 3 bullets para cada.
```

Depois peçam a triagem: qual dos 3 é o mais relevante e por quê.

Só isso. 10 minutos.

Na aula_04: a gente vai transformar os artigos que você leu em flashcards do Anki
e montar um briefing automático que chega todo dia de manhã com as novidades do seu tema.

Até lá."

---

**FIM DO ROTEIRO**
