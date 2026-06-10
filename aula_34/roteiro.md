# Aula 34 — O Guardião do Aproximado: Controle de Qualidade de uma Busca que Muda

**Formato:** Gravada em um take no OBS Studio
**Duração:** ~55 min
**Tom:** Clínico-arquiteto que aprende a testar o que não tem resposta cravada — calmo, depois visceral no clímax da honestidade
**Módulo:** S09.02 — Testes do RAG (busca semântica não-determinística)

---

## SEÇÃO 1: ABERTURA — O EXAME QUE NÃO DÁ UM NÚMERO — 6 min

**Tom:** Reflexivo, instigante. Retoma literalmente o gancho que a aula anterior deixou no ar.

"Na aula passada eu te deixei no ar com uma pergunta.

A calculadora é exata. Sessenta e oito anos, hipertenso e diabético, dá três. Sempre três. O gabarito é cravado, e o guardião só precisa conferir se o número bate.

Mas eu te perguntei: e a busca do RAG, aquele buscador de artigos que você construiu? Ela não dá sempre a mesma resposta exata. Ela traz o mais parecido. Como você cria um guardião pra uma coisa que muda?

Hoje eu respondo.

---

Deixa eu te tirar do laboratório de bioquímica e te levar pra beira do leito.

A glicemia é um exame quantitativo. Dá um número. E o controle confere o número — deu cem, calibrado.

Agora pensa num teste rápido. Reagente, não-reagente. Ele não te dá cento e vinte. Ele te diz: está aqui, ou não está.

Como é que o laboratório valida um teste desses? Não perguntando se deu cento e vinte. Perguntando duas coisas.

---

Primeira: quando a doença ESTÁ ali, o teste acha? Isso é sensibilidade.

Segunda: quando a doença NÃO está, o teste fica quieto, dá negativo? Isso é especificidade.

Um teste bom faz as duas. Acha o que existe. E não inventa o que não existe.

---

A busca do seu app é exatamente um exame qualitativo.

Pergunta sobre anticoagulação — está nos artigos? Ela tem que achar. Sensibilidade.

Pergunta sobre algo que não está em artigo nenhum — ela tem que ficar quieta, devolver vazio. Especificidade.

O guardião de hoje não confere um número. Ele confere essas duas perguntas. É assim que se faz controle de qualidade de uma coisa que, de propósito, não tem resposta cravada."

---

## SEÇÃO 2: POR QUE NÃO DÁ PRA PEDIR "O TRECHO EXATO" — 7 min

**Tom:** Didático, revelador. Aqui o aluno entende por que a receita da aula passada não serve — e isso é o conteúdo da aula.

"O instinto, depois da aula passada, seria esse: 'então é só eu dar o gabarito — a busca por anticoagulação TEM que devolver exatamente aquele trecho do primeiro artigo'.

Parece a mesma receita. Mas é uma armadilha. Deixa eu te mostrar por quê.

---

Imagina que amanhã você baixa um quarto artigo. Melhor, mais recente. Você reindexa.

A busca, que agora tem material melhor, passa a trazer um trecho ainda mais relevante — de outro artigo.

O que o guardião do 'trecho exato' faria? Ficaria vermelho. Ele gritaria 'ERRO' porque a busca melhorou.

Um guardião que trava uma melhoria não é um guardião. É um sabotador.

---

Então a gente vira a chave.

A gente não testa a RESPOSTA — que tem direito de mudar. A gente testa a PROPRIEDADE — o que tem que valer sempre, não importa qual trecho venha.

E você já sabe duas delas, porque eu te dei na abertura: sensibilidade — achou o que existe? — e especificidade — ficou quieto quando não havia nada? Essas duas são o par do exame qualitativo, o que todo médico já tem no corpo.

E tem uma terceira, de outra natureza — essa não é do laboratório, é da emergência: a ordem da fila. O caso certo no topo. Eu te mostro ela daqui a pouco.

As três valem hoje, valem com três artigos, valem com trezentos. A resposta muda. A propriedade, não.

---

E repara: eu não vou olhar dentro do guardião. Eu não preciso. Eu pergunto a ele, em português, 'a lista veio vazia, sim ou não?' — e ele me responde verde ou vermelho.

Do mesmo jeito que você lê 'reagente' sem saber a química do reagente."

---

## SEÇÃO 3: VOCÊ DEFINE AS PROPRIEDADES — 9 min

**Tom:** Colaborativo. O médico decide o que vira propriedade testável. Duas perguntas, nenhum código.

"Antes de pedir os guardiões, duas perguntas. Raciocínio clínico.

---

**PERGUNTA UM — qual pedido vira um guardião que funciona, e qual vira um sabotador?**

Você quer um guardião pra busca de anticoagulação. Três jeitos de pedir. Qual cria um guardião confiável — e qual vai te dar vermelho mesmo quando o app está certo?

A: 'a busca tem que devolver exatamente este trecho do artigo, palavra por palavra.'

B: 'a busca tem que devolver uma lista não-vazia, com pelo menos um resultado, e com fonte.'

C: 'a busca tem que devolver pelo menos cinco resultados, sempre.'

Pensa um segundo.

---

É a B.

A é o sabotador. Exige a resposta exata. No dia em que você indexar um artigo melhor, a busca traz um trecho melhor — e A fica vermelho por uma melhoria. A testa a resposta. A resposta tem direito de mudar.

C é arbitrário. Por que cinco? Se o corpus tem material pra três trechos realmente relevantes, exigir cinco força o app a raspar o fundo do tacho e trazer lixo só pra bater a meta. Número mágico não é propriedade.

B é a propriedade. Não amarra qual trecho, nem quantos exatos. Amarra o que tem que valer sempre: achou algo, e tem fonte. Sobrevive a artigos novos, a reindexação, a melhorias.

Critério que fica: propriedade boa é a que continua verdadeira depois de uma melhoria. Se uma melhoria deixa o guardião vermelho, você testou a coisa errada.

---

**PERGUNTA DOIS — qual erro do app é mais perigoso para o paciente: não achar, ou inventar?**

A busca pode falhar de dois jeitos opostos.

A: você pergunta sobre anticoagulação — que ESTÁ nos artigos — e o app devolve lista vazia. Tinha a informação e não achou.

B: você pergunta sobre algo que NÃO está em artigo nenhum — e o app, em vez de dizer 'não tenho', inventa um trecho plausível com cara de fonte real.

Qual é o mais perigoso?

---

B. Guarda essa resposta — ela vai voltar mais tarde, do jeito mais incômodo possível.

A é ruim, sem dúvida. Frustra, te obriga a procurar na mão. Mas A tem uma vantagem enorme: ele falha às claras. A lista veio vazia, você VÊ que não achou, você sabe que precisa procurar em outro lugar. Falha honesta.

B é o pesadelo. O app te entrega uma resposta com cara de certa, fonte com cara de real, e você não tem como saber que é invenção. Você pode levar isso pro paciente. B é o residente que chuta com confiança — e o chute com confiança é o que mata.

Critério que fica: num sistema clínico, o erro silencioso e confiante — inventar — é pior que o erro barulhento e visível — não achar. A gente testa os dois. O clímax é o silencioso."

---

## SEÇÃO 4: PROMPT 1 — O GUARDIÃO DA SENSIBILIDADE E O PRIMEIRO VERDE — 11 min

**Tom:** Mãos à obra. Pede os primeiros guardiões da busca, roda, lê a barra como laudo.

"Vou pedir ao Claude os primeiros guardiões da busca. Repara no formato: eu não dou o trecho que tem que vir. Eu dou a propriedade.

E tem uma coisa importante que eu peço junto: um corpus de teste separado. O guardião não vai buscar nos seus artigos de verdade — porque se você trocar os artigos amanhã, ele quebraria sem o app estar errado. Ele monta uns textinhos de teste só dele, num cantinho separado, e testa lá. Os seus artigos de verdade ficam intocados.

Cola o prompt:"

[TELA: digitar o Prompt 1 no Claude Code]

```
Você é meu par de programação. Quero criar testes automatizados (pytest) para a
busca semântica do ClinMd-Tribe — a função busca_service.buscar(consulta, n), que
devolve uma lista de ResultadoBusca (campos: trecho, fonte, numero_trecho, score).

Essa busca é diferente da calculadora: ela NÃO devolve sempre o mesmo texto exato.
Então NÃO quero testar igualdade de texto — quero testar PROPRIEDADES estáveis.

Para os testes não dependerem dos artigos que estão na minha máquina hoje, monte um
knowledge_base de TESTE pequeno e fixo — 2 ou 3 textos curtos sobre anticoagulação
em fibrilação atrial, criados só para o teste — e indexe num banco vetorial
SEPARADO, numa pasta temporária de teste. NUNCA use o data/chroma_db/ real do app.
O teste cria esse corpus, roda contra ele, e descarta no fim.

Crie estes guardiões:
  - SENSIBILIDADE: buscar um tema que ESTÁ no corpus de teste
    ("anticoagulação em fibrilação atrial") devolve lista NÃO-vazia.
  - BUSCA POR SENTIDO: buscar o mesmo assunto com outras palavras
    ("quando suspender o anticoagulante antes de um procedimento") também devolve
    lista NÃO-vazia — a busca entende o sentido, não só a palavra exata.
  - PROCEDÊNCIA: todo resultado devolvido tem o campo 'fonte' preenchido e o campo
    'trecho' preenchido — um médico nunca recebe um trecho sem saber de qual artigo
    veio.

NÃO me mostre o código. Coloque os testes em tests/, com nomes descritivos em
português, somados aos guardiões da calculadora que já existem. Cada propriedade
deve ser uma função de teste separada, com nome próprio, para aparecer como uma
linha distinta nos resultados. Ao final, sem mostrar código, diga quantos testes
criou e o comando para rodar todos.
```

"Cola, enter, deixa ele montar o corpus de teste e os guardiões. Quando terminar, rodo:"

[TELA: rodar]

```bash
uv run pytest -v
```

"Olha a barra. Os guardiões da sensibilidade — verdes.

Deixa eu traduzir, apontando pra tela:

A linha do tema presente passou — perguntei sobre anticoagulação e ele achou.

A linha da busca por sentido passou — perguntei com outras palavras, e ele achou mesmo assim. Entendeu o significado, não só a palavra.

A linha da procedência passou — todo trecho que ele trouxe tinha a fonte. Nenhum trecho órfão.

---

E repara no que eu NÃO fiz: nem uma vez eu disse qual trecho tinha que vir. Eu só exigi que viesse alguma coisa, e com fonte.

Você leu verde, não leu Python. Verde aqui significa: quando a doença está na lâmina, o app enxerga. Sensibilidade confirmada."

---

## SEÇÃO 5: O GUARDIÃO DA TRIAGEM — O CASO CERTO NO TOPO — 8 min

**Tom:** Satisfação narrativa, eleva a régua.

"Achar alguma coisa é o piso. Mas pensa na triagem do pronto-socorro.

Não importa a ordem exata dos quarenta e sete da fila. Importa que o infarto não fique em trigésimo. O caso certo no topo.

O guardião da triagem confere isso: quando eu pergunto sobre o que um artigo cobre, o trecho daquele artigo aparece entre os primeiros — não enterrado lá embaixo.

---

E olha a beleza: eu ainda não estou exigindo o trecho exato. Estou exigindo que a fonte certa apareça no topo. A busca tem liberdade de escolher qual pedaço daquele artigo trazer — mas o artigo relevante tem que estar lá em cima.

Liberdade no detalhe, rigor na propriedade. Cola:"

[TELA: digitar o Prompt 2]

```
Agora adicione um guardião da TRIAGEM, no mesmo conjunto de testes e usando o mesmo
corpus de teste isolado. NÃO me mostre o código.

  - Para uma consulta sobre um tema concentrado em UM dos textos do corpus de teste,
    buscar com n=3 deve trazer um trecho cuja 'fonte' seja aquele texto, entre os 3
    primeiros resultados. Não exijo posição exata, nem o trecho exato — só que a
    fonte certa apareça no top-3. Verifique pela 'fonte', não pelo conteúdo do trecho.

Ao final, sem mostrar código, me diga o comando para rodar tudo.
```

[TELA: rodar]

```bash
uv run pytest -v
```

"Verde. O caso certo chegou ao topo da fila.

A triagem do app funciona. E funcionaria igual se a busca trocasse de trecho amanhã — porque eu testei o que importa, não a forma.

---

Até aqui foi tudo verde, tudo bonito. O app acha o que existe e põe no topo.

Mas eu guardei a propriedade mais importante pro final. A que protege o paciente de verdade.

E pra mostrar o que ela faz, eu vou fazer o app mentir de propósito."

---

## SEÇÃO 6: CLÍMAX — A SABOTAGEM DA HONESTIDADE — 11 min

**Tom:** O ápice. Ritmo desacelera. Silêncios. O momento que o aluno leva pra vida.

"A terceira propriedade é a especificidade. A honestidade.

Lembra da aula da busca, quando eu perguntei sobre diabetes — que não estava em artigo nenhum — e o app devolveu lista vazia? Não inventou. Disse 'não tenho'.

Naquele dia eu provei isso uma vez, na mão. Hoje eu transformo aquela prova num guardião que reconfere pra sempre.

Primeiro, crio o guardião:"

[TELA: digitar o Prompt 3]

```
Agora o guardião mais importante, no mesmo conjunto e mesmo corpus de teste. NÃO me
mostre o código.

  - HONESTIDADE: buscar um tema médico de verdade que NÃO está no corpus de teste
    de anticoagulação ("como tratar diabetes tipo 2 com metformina") deve devolver
    lista VAZIA. O app não pode inventar nada quando não tem a informação.

Ao final, sem mostrar código, me diga o comando para rodar tudo.
```

[TELA: rodar]

```bash
uv run pytest -v
```

"Verde. Perguntei sobre diabetes — um tema médico de verdade, mas que não está nos meus artigos de anticoagulação — e o guardião confirmou: o app devolveu nada. Não chutou uma resposta só porque a pergunta tinha cara de plausível. A honestidade está provada, sozinha.

---

Agora vem a parte que importa. Pra você ver esse guardião trabalhar, eu vou cometer o pecado que aquele app jurou nunca cometer: vou fazer ele inventar.

Existe um vício clássico — o residente que, perguntado sobre algo que não sabe, em vez de dizer 'não sei', enrola uma resposta genérica pra não ficar mal. 'Bom, de modo geral, considerando o quadro...'.

Eu vou ensinar esse vício pro app. Vou fazer ele, quando não achar nada, devolver um texto de enchimento em vez de lista vazia. É a alucinação. É o que o ChatGPT faria. E é exatamente o que esse app foi construído pra nunca fazer."

[TELA: digitar o Prompt da sabotagem]

```
Quero te mostrar uma coisa sobre o guardião da honestidade. De propósito, introduza
no busca_service.buscar este erro: faça com que, quando a busca não encontrar nada
relevante, em vez de devolver lista vazia ele devolva um único resultado genérico
inventado — um texto tipo "Não há trecho específico, mas de modo geral sobre o
tema..." com fonte "conhecimento_geral". NÃO mexa nos testes — só na regra do
serviço. Quero ver o que o controle faz.
```

"Pronto. Agora o app, quando não acha, inventa. Se eu abrisse a tela e perguntasse sobre algo fora dos artigos, ele me devolveria um textinho plausível, com cara de resposta. Eu poderia até acreditar.

Mas eu não vou abrir a tela. Eu vou rodar o controle."

[TELA: rodar]

```bash
uv run pytest -v
```

"Olha.

Vermelho.

A linha da honestidade: falhou. O guardião perguntou 'busca fora do corpus devolveu lista vazia?' — e o app respondeu 'não, devolvi um resultado'. Um, quando tinha que ser zero.

---

[pausa]

Para um segundo.

Esse é o guardião mais importante do app inteiro. Ele não confere se uma conta deu certo. Ele confere se o app é HONESTO. Se ele admite o que não sabe.

Aquele comportamento que eu te mostrei uma vez, na aula da busca — 'quando não sei, devolvo vazio' — agora tem um guardião que reconfere isso a cada mudança, pra sempre. E ele acabou de pegar o app no exato momento em que ele começou a mentir.

---

Por que isso importa mais que tudo? Porque um app que inventa uma dose, uma conduta, uma referência — com confiança, com cara de certo — é mais perigoso que um app que diz 'não sei'. O 'não sei' você complementa com a sua cabeça. A invenção, você pode não pegar.

O guardião da honestidade é a prova, reconferida automaticamente, de que esse app nunca vai te empurrar uma resposta que ele não tem.

---

Agora eu conserto."

[TELA: digitar o Prompt do conserto]

```
Perfeito, o guardião pegou. Agora conserte: quando a busca não encontrar nada
relevante, o serviço tem que voltar a devolver lista VAZIA — nunca um resultado
inventado. Depois confirme que todos os testes voltaram a passar.
```

[TELA: rodar]

```bash
uv run pytest -v
```

"Verde de novo. O app voltou a ser honesto.

E olha o ciclo inteiro: estava tudo verde. Alguém mexeu — fui eu agora, mas amanhã pode ser o Claude fazendo uma melhoria que você pediu, e sem querer estragando a honestidade. O guardião acordou, ficou vermelho, apontou exatamente a regra: 'o app parou de admitir que não sabe'. Consertou. Verde.

Você não confia no app porque ele é bonito. Você confia porque o guardião da honestidade está verde."

---

## SEÇÃO 7: ENCERRAMENTO — O GUARDIÃO QUE NÃO DORME — 3 min

**Tom:** Síntese conduzida pelo aluno, caloroso, abre a tensão da próxima aula. LGPD orgânico.

"Recapitula — e quero você dizendo na sua cabeça.

Você criou guardiões pra uma coisa que muda. Não testou o trecho exato — testou três propriedades que valem sempre: o app acha o que existe, sensibilidade; põe o certo no topo, triagem; e fica quieto quando não há nada, especificidade. Você sabotou a honestidade do app e viu o guardião pegar. E fez tudo isso sem ler uma linha de código. Você leu laudos: reagente, não-reagente.

---

E repara na privacidade.

As perguntas que eu fiz nos testes — anticoagulação, prevenção de AVC — não têm paciente nenhum. São consultas-controle, como a amostra-controle nunca é sangue real.

E o guardião roda inteiro na sua máquina. A sua biblioteca de artigos é sua, o banco vetorial é seu, o controle é seu. Arranca o cabo de rede e ele confere tudo igual. O controle de qualidade do app que lê seus artigos é tão privado quanto os artigos. Nada disso liga pra lugar nenhum.

---

Agora pensa numa coisa.

Você já tem os guardiões — da calculadora, do checklist, da busca. Mas tem um problema humano: você precisa LEMBRAR de rodar o controle. Toda vez que mexer no app, digitar o comando.

E se você esquecer? E se for tarde, você está cansado, faz uma mudancinha rápida e não roda? O guardião só protege se for acordado.

Na próxima aula, a gente resolve isso de vez: um guardião que não precisa ser acordado. Que roda sozinho, automático, toda vez que o app muda — sem você lembrar de nada. O controle de qualidade que liga sozinho.

Até lá."

---

**FIM DO ROTEIRO**

---

> **NOTAS DE PRODUÇÃO (não falar — operacional):**
>
> - **Honestidade depende do limiar de relevância (CRÍTICO p/ o clímax):** o ChromaDB sempre devolve os N vizinhos mais próximos; "tema ausente, lista vazia" só funciona porque o `busca_service.buscar()` aplica um corte de score/distância. Esse corte agora é ensinado explicitamente na aula_29 (constante `LIMIAR_DISTANCIA`, calibrada empiricamente, valor conservador), então o serviço construído lá já deve trazê-lo. Mesmo assim, confirmar na pré-gravação que `buscar("como tratar diabetes tipo 2 com metformina")` no corpus de teste devolve lista vazia ANTES de gravar; se não devolver, o limiar está frouxo: pedir ao Claude para apertá-lo (é pré-condição do clímax, não conteúdo de aula). Se diabetes (tema médico, semanticamente mais perto) não cair vazio de forma estável, usar um tema mais distante como fallback.
> - **Forma do FAILED da honestidade:** se o `-v` mostrar `assert [ResultadoBusca(...)] == []` em vez de `assert 1 == 0`, ajustar a fala "Um, quando tinha que ser zero" para "ele trouxe um resultado, e o guardião exigia nenhum" (apontar a tela, sem ler string em inglês).
> - **Corpus de teste isolado (CRÍTICO):** confirmar na pré-gravação que os testes criam o próprio knowledge_base de teste e NÃO apontam para o `data/chroma_db/` real. Prova: apagar `data/chroma_db/` e rodar — os testes do RAG devem seguir verdes. Se falharem por ambiente, repetir o Prompt 1 enfatizando "banco vetorial separado, não o data/chroma_db real".
> - **Propriedade do top-N (Seção 5) — risco de instabilidade:** se o guardião da triagem não passar de forma estável (~5 execuções seguidas) com o corpus de teste, afrouxar para top-5 ou trocar a consulta por um tema mais inequivocamente concentrado em um texto. Não gravar antes de passar consistente.
> - **Custo do embedding:** sentence-transformers carrega o modelo na 1ª execução (pode demorar/baixar). Aquecer rodando uma vez antes de gravar.
> - **Reversibilidade da sabotagem (Seção 6):** working tree limpo e commitado antes. Se o conserto divergir, `git checkout -- application/servicos/busca_service.py` restaura. Nunca encerrar a gravação com o serviço divergente do commit.
> - **Números e nomes dos testes:** ajustar as falas que citam contagem/nomes ao que o `-v` listar na pré-gravação.
> - **Saída do FAILED:** o pytest costuma imprimir algo como `assert 1 == 0`. Fala mantida agnóstica ("um, quando tinha que ser zero") — apontar a tela, sem citar string em inglês.
