# Aula 33 — O Guardião que Não Dorme: o App que Confere as Próprias Regras

**Formato:** Gravada no OBS Studio, editada no Kdenlive
**Duração:** ~55 min
**Tom:** Clínico-arquiteto que aprende a fazer o app provar as próprias regras — calmo, depois visceral no clímax
**Módulo:** S09.01 — Testes Automatizados (TDD + pytest)

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] O ClinMd-Tribe com a calculadora CHA₂DS₂-VASc (serviço `calcular_cha2ds2vasc`) e o checklist cirúrgico da aula_31 (serviço `marcar_item` com o horário-testemunha imutável) já funcionando. Os testes desta aula cobrem essas duas regras.
- [ ] `pytest` disponível no ambiente do projeto (`uv run pytest` deve rodar; ainda sem testes, ele só não acha nada).

**Confira antes de gravar:**

- [ ] Working tree limpo e commitado ANTES de gravar (a sabotagem da Seção 6 mexe na regra do AVC prévio). Se o conserto divergir do original, `git checkout -- <arquivo da regra>` restaura na hora. Nunca encerre a gravação com o app divergente do último commit.
- [ ] Na pré-gravação, rode o Prompt 1 e anote quantos testes o Claude gera e como o `-v` os lista (podem ser agrupados ou parametrizados). Ajuste as falas "quatro guardiões / quatro passaram" (Seção 4) e a contagem da Seção 5 ao que aparecer na tela.
- [ ] Confirme que, antes da sabotagem, `uv run pytest -v` está todo verde (calculadora + timestamp).
- [ ] Confirme que a sabotagem do AVC prévio (1 ponto em vez de 2) faz o teste do AVC ficar vermelho, e que o conserto volta tudo a verde. A fala foi mantida agnóstica ("dois contra um"); aponte para a tela, sem ler a string em inglês do `assert`.

**Navegador:** nenhum site é necessário nesta aula; tudo roda no terminal.

---

## SEÇÃO 1: ABERTURA — O CONTROLE DA MANHÃ — 5 min

**Tom:** Reflexivo, reconhecível. Retoma o gancho da aula_31 e ancora num ritual que o médico já confia cegamente.

**[Aviso rápido dos óculos, antes de mergulhar]**

"Detalhe operacional antes de começar: óculos de perto, por favor. Hoje a gente vai ler barrinhas verdes e vermelhas no terminal, e a diferença entre um PASSED e um FAILED é coisa de poucos pixels. Igual ler um leucograma sem os óculos: o número está lá, mas você não jura. Foco no lugar? Seguimos."

"Na aula do checklist cirúrgico, eu te fiz uma promessa.

Lembra? Eu provei que o horário não podia ser falsificado — clicando, na mão, na frente de vocês. Marquei, fechei o app, reabri, tentei mudar. Três experimentos no dedo.

E eu te deixei uma pergunta no ar: e se a própria máquina provasse isso sozinha? Toda vez. Sem eu precisar clicar.

Hoje eu cumpro essa promessa.

---

Mas deixa eu começar por um lugar que você conhece melhor do que eu: o laboratório.

Toda manhã, antes do primeiro exame de paciente sair, o laboratório roda uma amostra-controle. Um material que não é de paciente nenhum — é padronizado, com um valor que já se sabe qual é. A glicemia-controle vale cem. Todo mundo sabe que vale cem.

A máquina lê o controle. Deu cem? Está calibrada. Pode liberar os exames do dia.

Deu cento e trinta? Trava tudo. Ninguém libera um resultado de paciente até consertar o aparelho.

---

Repara no que o controle faz. Ele não testa o paciente. Ele testa a máquina que vai medir o paciente.

E ele só funciona por um motivo: você sabe a resposta certa de antemão. Cem. Se você não soubesse que era cem, a leitura não provaria nada.

---

Hoje você vai construir a amostra-controle do seu app.

Um material de valor conhecido, que roda toda vez, e que trava tudo se o app errar uma regra que importa. Em vez de glicemia-controle, vão ser pacientes que você conhece de cor. Em vez de a máquina do laboratório, vai ser a sua calculadora e o seu checklist.

Tem nome técnico: testes automatizados. Mas guarda a imagem do controle da manhã. É tudo o que você precisa."

---

## SEÇÃO 2: TRÊS PALAVRAS — VERMELHO, VERDE, GUARDIÃO — 6 min

**Tom:** Didático e tranquilo. Monta a maquete mental antes de qualquer comando. Zero código.

"Antes de pedir qualquer coisa ao Claude Code, três palavras. Você já entende as três do laboratório — só falta o nome novo.

---

**Verde.**

Verde é o controle deu certo. A máquina leu cem, o app acertou a regra. Quando você rodar os testes e tudo estiver verde, significa: cada caso que você conhece deu o resultado que você esperava. Calibrado. Pode confiar.

---

**Vermelho.**

Vermelho é o controle falhou. A máquina leu cento e trinta. Alguma regra que importa está errada. E aqui vem a parte que parece estranha mas é linda: vermelho é uma boa notícia.

Pensa comigo. Se uma regra do seu app quebrou, você quer descobrir como? Por um paciente prejudicado? Ou por um alarme vermelho na sua tela, antes de qualquer paciente chegar perto?

Vermelho é o guardião gritando 'PARA' antes do dano. Vermelho é de graça. Paciente prejudicado, não.

---

**Guardião.**

Cada teste é um guardião. Ele vigia uma regra específica. O AVC prévio tem que valer dois pontos — tem um guardião pra isso. O horário do checklist não pode mudar — tem um guardião pra isso.

Você não escreve esses guardiões. Você pede pro Claude criar. E eles ficam lá, parados, em silêncio — até a hora em que uma regra quebra. Aí eles acordam todos juntos e apontam exatamente o que saiu do lugar.

---

Verde, vermelho, guardião.

Calibrado, alarme, vigia.

É a mesma lógica do controle de qualidade que você já confia todo dia. Só que agora é o controle de qualidade do seu app — e quem o roda é um comando só."

---

## SEÇÃO 3: VOCÊ DEFINE O CONTROLE — 8 min

**Tom:** Colaborativo e instigante. O médico decide o que merece um guardião. Duas perguntas, nenhum código.

"Antes de criar os guardiões, duas decisões. E quem decide é você — porque guardião demais atrapalha, e guardião de menos deixa passar o que importa.

Duas perguntas. Raciocínio clínico, não código.

---

**PERGUNTA UM — quais regras merecem um guardião?**

Você não vai testar tudo. Seria como rodar controle pra cada parafuso da centrífuga. Você testa o que, se quebrar, machuca.

Te dou três coisas do seu app. Qual delas, se quebrasse em silêncio — sem ninguém perceber — seria a mais perigosa para um paciente?

A: a cor do botão 'Calcular'.

B: o AVC prévio valer dois pontos no CHA₂DS₂-VASc.

C: o alinhamento do texto na tela.

Pensa um segundo.

---

É a B. E o detalhe é a palavra 'silêncio'.

Se a cor do botão quebrar, você vê na hora. Se o texto desalinhar, você vê na hora. Ninguém se machuca por um botão torto.

Mas se o AVC prévio passar a valer um ponto em vez de dois? A tela mostra um número plausível. Parece certo. Você confia. E o paciente é subtratado — sem que nada na tela grite que está errado.

Regra que merece guardião é essa: a que, quando quebra, quebra calada e perigosa. Não se testa estética. Testa-se segurança.

---

**PERGUNTA DOIS — o que um controle precisa ter pra servir de teste?**

Imagina que eu te entrego um tubo e digo: 'roda no aparelho'. A máquina lê noventa e seis. Isso prova que o aparelho está calibrado?

Pensa. O que está faltando pra esse número significar alguma coisa?

---

Falta você saber o valor verdadeiro do tubo de antemão.

Noventa e seis não prova nada se eu não te disse que aquele controle vale cem. Um controle só funciona porque a resposta certa é conhecida antes de rodar. Sem gabarito, o número é só um número.

E aqui está o pulo do gato — isso é literalmente o que vamos fazer. No próximo prompt, eu não vou dizer 'teste a calculadora'. Eu vou dizer: 'paciente com AVC prévio TEM que dar dois pontos'. Eu entrego o gabarito junto com o caso. Sem gabarito, não há controle.

---

Duas decisões tomadas, e você nem tocou no teclado. Você decidiu o que vigiar — as regras perigosas. E entendeu por que um teste é confiável — porque a resposta certa vem antes. Agora a gente pede os guardiões."

---

## SEÇÃO 4: PROMPT 1 — OS GUARDIÕES E O PRIMEIRO VERDE — 12 min

**Tom:** Mãos à obra. Pede os testes da calculadora em linguagem clínica, roda, e lê a barra verde como um laudo.

"Vou pedir ao Claude pra criar os guardiões da sua calculadora CHA₂DS₂-VASc. Repara no formato do pedido: cada guardião é um caso clínico que você conhece de cor, com o escore que você sabe ser o certo. Eu entrego o gabarito junto — como manda o controle.

São os mesmos casos que você validou à mão lá na aula da calculadora. Cola o prompt:"

[TELA: digitar o Prompt 1 no Claude Code]

```
Você é meu par de programação. Quero criar testes automatizados (pytest) que
funcionem como o controle de qualidade do meu laboratório: cada teste tem um caso
clínico de entrada e o resultado que eu SEI que é o certo. NÃO me mostre o código
dos testes — só crie os arquivos e, ao final, me diga em uma frase como eu rodo
todos eles.

Crie testes para a calculadora CHA₂DS₂-VASc (o serviço calcular_cha2ds2vasc),
usando estes casos clínicos, com a entrada e o escore esperado:

  - 68 anos, masculino, hipertenso e diabético, sem mais nada
    -> escore esperado: 3 (recomendação: Anticoagular)
  - 55 anos, masculino, sem nenhum fator de risco
    -> escore esperado: 0 (recomendação: Sem indicação no momento)
  - 77 anos, feminina, com insuficiência cardíaca, hipertensão e AVC prévio
    -> escore esperado: 7 (recomendação: Anticoagular)
  - paciente masculino com AVC prévio e mais nada
    -> escore esperado: 2, recomendação Anticoagular (a regra S2: AVC prévio
       vale 2 pontos, nunca 1)

Cada teste compara o escore que a calculadora devolve com o escore que eu informei
aqui, e passa só se forem iguais. Coloque os testes na pasta padrão tests/, com
nomes descritivos em português.

Ao final, sem mostrar código, me diga quantos testes você criou e o comando exato
para rodar todos.
```

"Cola, enter, deixa ele criar os guardiões. Ele vai te dizer no fim quantos criou e o comando pra rodar. O comando é esse — vou rodar agora:"

[TELA: rodar os testes]

```bash
uv run pytest -v
```

"Olha a tela. Cada linha é um guardião reportando. Em português, o nome do caso, e do lado: PASSED, em verde.

Quatro guardiões. Quatro verdes. No rodapé: 'quatro passaram'.

---

Deixa eu traduzir esse laudo pra você — porque é exatamente um laudo.

Cada linha verde é um controle que bateu. O paciente de sessenta e oito anos deu três, como você calculou à mão. O de cinquenta e cinco deu zero. A senhora de setenta e sete deu sete — insuficiência cardíaca, hipertensão, mais de setenta e cinco anos, AVC prévio, e o ponto do sexo feminino; exatamente como você somaria à mão. E o AVC prévio sozinho deu dois — a regra crítica, confirmada.

Sua calculadora está calibrada. Como a máquina que leu cem no controle da manhã.

---

E você não leu uma linha de Python pra saber disso. Você leu a barra verde. Do mesmo jeito que você lê 'TGO dentro da faixa' sem saber como o aparelho mede a TGO.

Essa é a habilidade nova: confiar no guardião pelo veredito, não pelo código. Verde é normal. E nós temos quatro normais."

---

## SEÇÃO 5: O GUARDIÃO DO TIMESTAMP — A MÁQUINA CLICA SOZINHA — 8 min

**Tom:** Satisfação narrativa. A promessa da aula_31 cumprida — a máquina faz sozinha os três cliques.

"Agora eu volto à promessa do começo. O checklist cirúrgico.

Na aula dele, eu provei que o horário não muda — clicando três vezes na mão. Marquei, fechei e reabri, tentei re-marcar. Lembra do meu dedo na tela?

Vamos criar um guardião que faz esses três cliques sozinho. Toda vez. Sem o meu dedo."

[TELA: digitar o prompt do guardião do timestamp]

```
Agora crie um guardião para a regra mais importante do meu checklist cirúrgico:
o horário de quando um item é marcado não pode mudar depois.

Crie testes (pytest) que provem, usando um banco de teste SEPARADO (nunca o banco
real do app em data/clinmd.db), que:
  - marcar um item gera um horário de conclusão;
  - marcar o MESMO item de novo NÃO altera o horário do primeiro toque;
  - o horário continua o mesmo depois de recarregar os itens do banco.

NÃO me mostre o código. Ao final, me diga o comando para rodar esses testes junto
com os outros.
```

"Repara numa coisa que eu pedi: banco de teste separado. O guardião nunca encosta no banco real do seu app, com os horários das suas cirurgias de verdade. Ele monta um banco de mentira, faz o teste lá, e joga fora. Os seus dados ficam intocados.

---

Criado. Rodo tudo de novo:"

[TELA: rodar]

```bash
uv run pytest -v
```

"Agora são mais guardiões na lista. E os novos, os do timestamp — verdes também.

Aquilo que eu provei com três cliques na aula do checklist, a máquina acabou de provar sozinha. Ela marcou um item, marcou de novo, conferiu que o horário não mudou, recarregou e conferiu outra vez. Em frações de segundo. Sem ninguém clicando.

A promessa que eu te fiz no fim da aula do checklist? Cumprida. A máquina prova a própria regra. Agora, toda vez que você rodar esse comando, o guardião reconfere — pra sempre.

---

E é aqui que a coisa fica séria. Porque até agora foi tudo verde, tudo bonito. Mas eu quero te mostrar o que esses guardiões fazem quando algo dá errado.

Pra isso, eu vou quebrar uma regra de propósito."

---

## SEÇÃO 6: CLÍMAX — A SABOTAGEM: O ALARME QUE SALVA O PACIENTE — 11 min

**Tom:** O ápice. Ritmo desacelera, deliberado, teatral. Silêncios. É o momento que o aluno leva pra vida.

"Vou pedir ao Claude pra estragar uma regra. De propósito. O erro mais comum que existe nessa calculadora — aquele que eu te avisei lá na aula da calculadora.

Vou fazer o AVC prévio valer um ponto, em vez de dois. É um erro real. Acontece em implementações de verdade, no mundo lá fora, porque alguém confunde o S de AVC com os critérios de um ponto.

E eu não vou tocar nos guardiões. Só na regra. Quero ver se eles acordam."

[TELA: digitar o Prompt da sabotagem]

```
Quero te mostrar uma coisa. Por favor, introduza de propósito o erro mais comum
dessa calculadora: faça o AVC prévio valer 1 ponto em vez de 2 na lógica do
CHA₂DS₂-VASc. NÃO mexa nos testes — só na regra. Quero ver o que acontece quando
eu rodo o controle.
```

"Pronto. O Claude mudou a regra. Agora o AVC prévio vale um ponto. O app está errado — silenciosamente errado. Se eu abrisse a calculadora na tela agora, ela mostraria um número plausível. Eu não veria nada de estranho.

Mas eu não vou abrir a tela. Eu vou rodar o controle."

[TELA: rodar]

```bash
uv run pytest -v
```

"Olha.

Vermelho.

A linha do AVC prévio: FAILED. Em vermelho.

E embaixo, em vermelho, o guardião mostra o confronto: o número que ele exigia contra o número que recebeu. Dois contra um. Ele esperava dois, e o app entregou um.

---

[pausa]

Para um segundo nisso.

O guardião pegou. Sozinho. Na hora.

Ele sabia que AVC prévio tem que dar dois pontos — porque você disse isso a ele, no gabarito. O app entregou um. E ele travou tudo, gritou vermelho, e apontou o dedo exatamente na regra que quebrou.

Esse paciente — um homem com AVC prévio — deveria pontuar dois. Dois é o suficiente para anticoagular. Com o bug, ele pontua um. Cai abaixo do corte. A recomendação vira 'sem indicação' — e ele fica sem a anticoagulação que o protegeria de um próximo AVC. Um erro que mata, calado.

E quem te avisou não foi uma sindicância. Não foi um paciente que teve um AVC. Foi um guardião de software, de graça, em meio segundo, antes de qualquer paciente chegar perto.

---

Agora eu conserto."

[TELA: digitar o Prompt do conserto]

```
Perfeito, o guardião pegou. Agora conserte: o AVC prévio tem que voltar a valer
2 pontos, como manda o escore. Depois confirme que todos os testes voltaram a passar.
```

[TELA: rodar]

```bash
uv run pytest -v
```

"Verde de novo. Tudo verde.

O controle voltou a ler cem. Máquina recalibrada.

---

Olha o ciclo inteiro que acabou de acontecer, porque é o coração de tudo:

Tudo estava verde. Alguém mexeu no app — nesse caso fui eu, mas amanhã pode ser o Claude fazendo uma melhoria que você pediu. A mudança quebrou uma regra, em silêncio. O guardião acordou, ficou vermelho, e mostrou exatamente o quê. Consertou. Verde de novo.

Isso tem um nome no mundo da programação: regressão. É quando você mexe numa coisa e, sem querer, quebra outra que já funcionava. É o pesadelo de todo software que cresce.

E o guardião é a sua defesa contra isso. Toda vez que o app mudar, você roda o controle. Verde, pode seguir. Vermelho, parou — tem uma regra quebrada, e você sabe qual, antes de chegar no paciente.

Você não confia mais no app porque ele é bonito. Você confia porque os guardiões estão verdes."

---

## SEÇÃO 7: ENCERRAMENTO — O GUARDIÃO QUE NÃO DORME + O QUE VEM — 5 min

**Tom:** Síntese conduzida pelo aluno, caloroso, e abre a tensão da próxima aula. LGPD orgânico.

"Recapitula o que você fez hoje — e quero que seja você dizendo, na sua cabeça.

Você criou guardiões pra calculadora e pro checklist. Rodou o controle e viu verde. Quebrou uma regra de propósito e viu o guardião acordar vermelho, apontar o erro, e te deixar consertar — antes de qualquer paciente. E você fez tudo isso sem ler uma linha de código de teste. Você leu laudos. Verde, vermelho. Normal, alterado.

---

E repara num detalhe bonito sobre privacidade.

Os 'pacientes' que eu usei nos testes — o de sessenta e oito anos, a senhora de setenta e sete — nenhum deles é gente de verdade. São controles. Material padronizado, como a amostra-controle nunca é sangue de um paciente real. Então até os testes respeitam o eixo do curso: nenhum dado de paciente real entrou aqui.

E mais: o guardião roda inteiro na sua máquina. Aquele comando, `uv run pytest`, arranca o cabo de rede e ele funciona igual. Ele não liga pra nuvem nenhuma pra conferir suas regras. O controle de qualidade do seu app é tão privado quanto o resto — fica com você.

---

Agora, o que vem.

Hoje os guardiões da calculadora foram fáceis num ponto: a calculadora é exata. Sessenta e oito anos, hipertenso e diabético, dá três. Sempre três. O gabarito é cravado.

Mas e a busca do RAG — aquele buscador de artigos que você construiu? Ela não dá sempre a mesma resposta exata. Ela traz o mais parecido, o mais relevante. É aproximada, de propósito.

Como você cria um guardião pra uma coisa que muda? Como se faz controle de qualidade de algo que, por natureza, não tem uma resposta única e cravada?

Esse é o próximo desafio. Testar o exato você já sabe. Na próxima aula, a gente testa o aproximado.

Até lá."

---

**FIM DO ROTEIRO**

---

> **NOTAS DE PRODUÇÃO (não falar — operacional):**
>
> - **Salvaguarda da sabotagem (Seção 6):** antes de gravar, ter o working tree limpo e commitado (git, ensinado no S00). Se o conserto do Prompt 2b divergir do código original, `git checkout -- <arquivo da regra>` restaura na hora. Nunca encerrar a gravação com o app divergente do commit anterior.
> - **Números e nomes dos testes:** as falas "quatro guardiões / quatro passaram" (Seção 4) e a contagem da Seção 5 dependem de quantos testes o Claude gera e de como o `-v` os lista (casos podem ser agrupados/parametrizados). Rodar o app na pré-gravação e ajustar os números/nomes citados ao que aparecer na tela. A Seção 5 terá mais verdes que a Seção 4 (calculadora + timestamp somados).
> - **Saída do FAILED:** o pytest costuma imprimir algo como `assert 1 == 2`. A fala foi mantida agnóstica ("dois contra um") — apontar para a tela, sem citar string literal em inglês.
