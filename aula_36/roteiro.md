# Aula 36 — O Porteiro: o Robô que Tranca a Porta, Não Só Acende a Luz

**Formato:** Gravada em um take no OBS Studio
**Duração:** ~55 min
**Tom:** Clínico-arquiteto; do alívio da aula passada ao rigor inegociável — "agora ele não me deixa errar nem se eu insistir". Visceral no instante em que a entrega é recusada.
**Módulo:** S10.02 — Branch protection: o CI que bloqueia (GitHub)

---

## SEÇÃO 1: ABERTURA — O ALERTA QUE VOCÊ PODE IGNORAR — 5 min

**Tom:** Reflexivo. Retoma o gancho da aula_35 e nomeia o defeito.

"Aula passada foi uma vitória. Você criou um robô que roda os guardiões sozinho, no servidor, toda vez que você entrega. Nunca mais precisa lembrar.

Mas eu te deixei com um incômodo de propósito. Lembra?

Quando o robô ficou vermelho — quando eu quebrei a regra do AVC — eu ainda consegui entregar o código quebrado. O robô pintou de vermelho... e me deixou seguir. Ele avisou. Mas não me impediu.

---

Pensa no seu sistema de prescrição eletrônica. Aquele alerta amarelo que pisca: 'atenção, interação medicamentosa'. Você lê, clica em 'ciente', e prescreve assim mesmo. O alerta informa. Mas a porta continua aberta. O erro continua possível.

O robô de ontem é esse alerta amarelo. Útil. Mas ignorável.

---

Hoje a gente fecha a porta.

Hoje o robô deixa de ser o alerta que você clica 'ciente' — e vira o bloqueio que não te deixa assinar. O hard-stop. Aquele que, na interação fatal, deixa o botão de confirmar cinza, e te obriga a corrigir antes de seguir.

Ele não vai te avisar do erro. Ele não vai te deixar cometer o erro sem perceber.

---

Mas antes de trancar a porta, eu preciso conferir uma coisa: estão todos os guardiões de plantão? Porque não adianta trancar a porta se um deles ainda está dormindo. E tem um dormindo — desde a aula passada."

---

## SEÇÃO 2: O GUARDIÃO QUE FALTAVA — TRAZENDO A BUSCA PARA O ROBÔ — 9 min

**Tom:** Mãos à obra. Resolve o débito da aula_35. Um prompt, fecha o arco do CI.

"Lembra que, na aula do robô, eu deixei um guardião de fora? O da busca. O da honestidade — aquele que confere se o app admite quando não sabe, em vez de inventar.

Eu deixei de fora por um motivo técnico bobo: o cérebro da busca é um arquivo grande, e eu não quis fazer você esperar ele baixar ao vivo. Mas o robô estava incompleto. Ele vigiava a calculadora e o checklist — e deixava a parte mais perigosa do app, a que pode inventar uma referência, sem vigia no servidor.

Um porteiro que vigia duas portas e ignora a terceira não é porteiro. Então, antes de trancar, eu trago o terceiro guardião pra dentro.

---

Mas primeiro, o ritual de sempre — conferir que o terreno está limpo e que nada de paciente sobe. Cola:"

[TELA: digitar o Prompt 0 no Claude Code]

```
Você é meu par de programação. Hoje eu vou transformar o robô de testes num porteiro
que BLOQUEIA código quebrado. Antes de começar, confira o estado do meu projeto e me
responda em português, SEM me mostrar saída técnica crua, apenas:
  1. se o meu projeto está conectado ao repositório clinmd-tribe no GitHub e se o meu
     último trabalho já foi enviado (push), com a branch main em dia;
  2. se a pasta data/ continua protegida pelo .gitignore — eu não quero banco, artigos
     nem dado de paciente saindo da minha máquina;
  3. se o robô de testes que eu criei na aula passada (o que roda a calculadora e o
     checklist a cada push) ainda está no projeto e funcionando.

Se algo estiver pendente, conserte você mesmo e confirme em uma frase. NÃO me mostre
código nem arquivos de configuração.
```

"Terreno confirmado, `data/` trancada. Agora o terceiro guardião. Repara no formato — eu descrevo em português, não toco em configuração:"

[TELA: digitar o Prompt do RAG no robô]

```
Lembra do robô de CI (GitHub Actions) que a gente criou? Ele hoje roda só os testes
da calculadora e do checklist e deixa os testes da busca/RAG de fora, porque eles
baixam o modelo grande de embeddings.

Agora quero COMPLETAR o robô: faça ele rodar TAMBÉM os testes da busca, para cobrir
todos os guardiões — inclusive o da honestidade.

Requisitos:
  - Para o download do modelo não repetir a cada entrega, configure o robô para
    GUARDAR esse modelo em cache entre uma execução e outra (o cache do próprio
    GitHub Actions). A primeira entrega baixa; as próximas reaproveitam.
  - Coloque os testes da busca num TRABALHO separado dos da calculadora e do checklist,
    para a parte rápida continuar terminando rápido mesmo se a busca demorar a carregar
    o modelo. Eu quero enxergar os dois trabalhadores na aba Actions.
  - Continua sem tocar na pasta data/: a busca dos testes usa o corpus fictício
    separado que a gente já montou, nunca os meus artigos de verdade.

NÃO me mostre o conteúdo do arquivo. Quando terminar, me diga em português: (1) que o
robô agora cobre todos os guardiões; (2) os comandos git para enviar; (3) o que vou
ver de novo na aba Actions.
```

[TELA: enviar, com os comandos que o Claude deu]

```bash
git add .
git commit -m "ci: robô passa a cobrir todos os guardiões, inclusive a busca"
git push
```

"Abre a aba Actions. Agora você vê dois trabalhadores: um rápido — calculadora e checklist — que fica verde num instante; e um mais vagaroso — a busca — que nesta primeira vez está carregando a biblioteca pesada e guardando uma cópia. Espera ele... e os dois ficam verdes.

Agora sim. Os três guardiões — calculadora, checklist, e a honestidade da busca — todos de plantão, no servidor, a cada entrega. O robô está completo. Agora ele merece virar porteiro."

---

## SEÇÃO 3: VOCÊ DECIDE — 9 min

**Tom:** Colaborativo. Duas perguntas, raciocínio clínico, zero código.

"Antes de trancar a porta, duas perguntas. Pensa na diferença entre um alerta que pisca e um bloqueio que segura a sua mão.

---

**PERGUNTA UM — qual a diferença, de verdade, entre o robô de ontem e o porteiro de hoje?**

Ontem o robô já ficava vermelho quando você quebrava uma regra. Então o que muda hoje?

A: o robô de hoje roda os testes mais rápido.

B: o robô de hoje roda testes melhores, diferentes.

C: os testes são exatamente os mesmos — o que muda é a consequência. Ontem o vermelho avisava, mas deixava você entregar mesmo assim. Hoje o vermelho tranca a porta, e a entrega não é aceita até voltar ao verde.

Pensa.

---

É a C. Os guardiões são os mesmos — A e B estão errados, não tem teste novo nem mais rápido.

O que mudou não está dentro do robô. Está no que acontece depois dele ficar vermelho.

Ontem: alerta amarelo. Pisca, você clica 'ciente', prescreve a interação assim mesmo. A decisão de errar continuava sua.

Hoje: hard-stop. O botão de assinar fica cinza. A decisão de errar saiu da mesa — a máquina não te deixa.

Critério que fica: a diferença entre avisar e impedir não está na inteligência do controle. Está na consequência que você liga em cima dele. O mesmo robô, com uma trava, vira porteiro.

---

**PERGUNTA DOIS — a porta trancou no vermelho. Você precisa MESMO entregar. Como você abre?**

A: procurar um jeito de forçar a entrega, contornar o porteiro, mandar o código entrar na marra.

B: desligar a trava que você acabou de ligar, entregar o código quebrado, e religar depois.

C: consertar a regra — fazer o robô voltar pro verde. A porta abre sozinha no instante em que o controle passa.

Pensa.

---

É a C. E repara por que A e B, mesmo sendo possíveis, são perigosos.

A — forçar a entrada na marra. Aqui eu vou ser honesto com você: como a casa é sua, o GitHub te dá, sim, um botão de emergência pra furar. Mas ele te obriga a marcar, com todas as letras, 'estou ignorando os controles de propósito'. É uma confissão assinada, não um atalho confortável. E pra qualquer pessoa que entre no seu time e não seja dona, esse botão nem aparece. Forçar nunca é o caminho — é a saída de incêndio que você não quer ter que usar.

B — desligar a trava pra passar o quebrado — é pior ainda: é desativar o alarme de incêndio pra poder fumar dentro do hospital. Você entrega o erro E deixa a porta destrancada pro próximo.

C é o único caminho honesto: você conserta, e a porta abre sozinha, limpa, sem confissão nenhuma. O verde é a chave, e o conserto é o que fabrica a chave.

Critério que fica: um porteiro de verdade só abre de um jeito tranquilo — corrigindo o que ele apontou. Furar até pode, sendo dono — mas o sistema te obriga a assinar embaixo. E o que você quer não é aprender a furar; é não precisar."

---

## SEÇÃO 4: A ANTECÂMARA E A FECHADURA — 11 min

**Tom:** Mãos à obra, mas calmo. Aqui entra o único conceito novo do dia — o Pull Request — ancorado numa imagem que o médico já tem no corpo.

"Pra trancar a porta, eu preciso te apresentar uma ideia nova. Uma só. E você já conhece ela do bloco cirúrgico.

Você não entra no centro cirúrgico direto do corredor. Você passa por uma antecâmara. Para. Confere a paramentação. E só então a segunda porta, a que dá pra sala, abre.

No código existe exatamente essa antecâmara. O nome técnico é Pull Request — mas esquece o nome, lembra da antecâmara. Em vez de empurrar a sua mudança direto pra linha principal do app, você a deixa esperando na antecâmara. O robô confere. E a porta pra principal só abre se ele aprovar.

---

Vou pedir ao Claude pra preparar essa antecâmara e me ensinar a ligar a fechadura. Repara: a fechadura em si, quem liga sou eu, clicando no GitHub. Porque trancar a porta da casa é decisão do dono — não dá pra terceirizar. Cola:"

[TELA: digitar o Prompt da antecâmara + guia]

```
Eu quero transformar o robô num porteiro: nada deve entrar na minha branch principal
(main) sem o robô de testes ter ficado verde. Para o GitHub conseguir bloquear, a
minha mudança precisa primeiro passar por uma "antecâmara" chamada Pull Request, em
vez de eu empurrar direto na main.

Faça duas coisas:

PARTE 1 (você faz, me entregando o comando pronto):
  - Crie uma branch de trabalho separada da main, chamada "teste-do-porteiro", e me
    deixe pronto para trabalhar nela. Me diga, em uma linha, o comando que eu rodo
    para enviar minhas mudanças para essa branch (já com o nome dela preenchido).

PARTE 2 (eu faço, clicando — você é meu guia):
  - Me conduza, passo a passo, em português, pelos cliques em Settings -> Branches do
    meu repositório clinmd-tribe no GitHub, para criar uma regra que proteja a main e
    EXIJA que o robô de testes fique verde antes de permitir juntar (merge) qualquer
    mudança na main. Eu trabalho sozinho, então NÃO quero exigir aprovação de outra
    pessoa — só o robô verde. Liste os cliques com o nome de cada botão como aparece
    na tela. NÃO mude a configuração por mim; eu quero clicar.

NÃO me mostre arquivos de configuração.
```

"O Claude prepara a branch e me dá o passo a passo. Eu sigo os cliques na tela dele — Settings, lá em cima; Branches, na lateral; criar a regra; nome da branch protegida, `main`; e a caixinha que importa: 'exigir que os controles passem antes de juntar'. Seleciono o meu robô na lista. Salvo.

---

Pronto. Não escrevi uma linha. Cliquei. A porta agora tem fechadura: o GitHub passou a exigir que o robô esteja verde antes de aceitar qualquer mudança na linha principal.

Em português de gente, isso quer dizer uma coisa só: daqui pra frente, mudança quebrada não entra na `main`. A antecâmara segura. Agora vamos ver isso acontecer — e a melhor forma de ver uma fechadura funcionar é tentar entrar com a chave errada."

---

## SEÇÃO 5: O CLÍMAX — A PORTA QUE NÃO ABRE — 12 min

**Tom:** O ápice. Desacelera, silêncios. A sabotagem reencena a da aula_35 — mas o desfecho é o oposto: a entrega é recusada.

"Aula passada, quando eu sabotei o AVC, o robô ficou vermelho — mas eu consegui entregar mesmo assim. Hoje eu vou fazer a mesmíssima sabotagem. Presta atenção no que vai ser diferente.

O mesmo erro de sempre: o AVC prévio valendo um ponto em vez de dois. O erro que subtrata paciente. Mas agora na antecâmara — na branch de teste, não na principal."

[TELA: digitar o Prompt da sabotagem]

```
Agora eu quero PROVAR que o porteiro bloqueia. Na minha branch de teste
(teste-do-porteiro), introduza de propósito o mesmo erro de antes: faça o AVC prévio
valer 1 ponto em vez de 2 no serviço da calculadora CHA2DS2-VASc. NÃO mexa nos testes
— só na regra. Não rode nada na minha máquina. Quando terminar, me lembre em uma linha
os comandos para enviar essa mudança para a branch teste-do-porteiro.
```

[TELA: enviar para a branch, com os comandos que o Claude deu]

```bash
git add .
git commit -m "test: quebra a regra do AVC para validar o porteiro"
git push
```

"A mudança quebrada foi pra antecâmara — a branch de teste. Repara: eu não estou mais mexendo na linha principal. Estou na antecâmara, de propósito, justamente pra poder quebrar as coisas longe da `main`. Por isso o comando de enviar que o Claude me deu tem o nome dela no fim.

Agora abre o GitHub no navegador. Logo depois do push costuma aparecer uma faixa amarela no topo: 'teste-do-porteiro' teve mudanças, com o botão 'Compare & pull request'. Clico nele. (Se a faixa não estiver lá, dá no mesmo lugar: aba 'Pull requests', botão 'New pull request', escolho a branch 'teste-do-porteiro'.) Depois, 'Create pull request'. Não preciso escrever nada.

---

Olha a tela do Pull Request. A antecâmara, aberta.

Desce um pouco. Tem uma caixa com os controles, e os guardiões já estão lá dentro trabalhando — bolinhas amarelas girando. O rápido, da calculadora e do checklist, termina primeiro. E fica vermelho: pegou o AVC. O da busca pode ainda estar girando, carregando a biblioteca pesada — mas não importa. Um guardião vermelho já basta pra trancar.

E o botão 'Merge pull request' — o de abrir a segunda porta? Ele não fica verde. O GitHub deixa explícito, ali, que os controles não passaram: a entrega não está liberada.

---

[pausa]

Para um segundo nisso. E presta atenção, porque aqui tem uma honestidade que eu não vou te esconder.

Esse repositório é seu. Você é o dono do prédio inteiro. E o GitHub, pro dono, não tranca a porta com você do lado de fora — ele te dá uma saída de emergência. Se eu quiser MESMO furar, aparece uma opção pra isso. Mas olha o que ela me obriga a marcar, com todas as letras: 'juntar sem cumprir os requisitos — ignorar a proteção'.

Sentiu a diferença pra ontem? Ontem, o código quebrado entrava liso, no automático, sem ninguém perceber. Hoje, pra ele entrar, EU tenho que parar, ler, e assinar conscientemente que estou ignorando o porteiro. O erro deixou de ser silencioso. Virou uma confissão.

E tem mais: no dia em que entrar mais alguém no seu time, esse botão de furar some pra quem não é dono. Aí o porteiro é absoluto — ninguém passa no vermelho, ponto.

---

Esse é o pulo de hoje. Ontem: 'o robô me avisa, e eu ignoro sem nem pensar'. Hoje: 'o robô não me deixa errar sem perceber — pra furar, eu tenho que confessar'. O alerta amarelo virou um hard-stop que, no mínimo, me obriga a olhar nos olhos do erro antes de cometê-lo.

E o jeito certo, claro, não é furar. É consertar. A porta abre sozinha, limpa, no instante em que o robô voltar pro verde — sem marcar nada, sem confissão nenhuma."

[TELA: digitar o Prompt do conserto]

```
Perfeito, o porteiro bloqueou. Agora conserte na branch teste-do-porteiro: o AVC prévio
tem que voltar a valer 2 pontos. Confirme que está corrigido, e me lembre os comandos
para enviar de novo para a mesma branch. Quero ver o robô ficar verde e o botão de
juntar liberar.
```

[TELA: enviar o conserto para a mesma branch]

```bash
git add .
git commit -m "fix: AVC prévio volta a valer 2 pontos"
git push
```

"Repara: eu mandei pra mesma antecâmara. Não preciso abrir um Pull Request novo — o que já está aberto se atualiza sozinho.

Volta na tela do PR. Bolinhas amarelas de novo, girando... e vira verde. 'Todos os controles passaram.'

E o botão 'Merge pull request' agora está verde e limpo — clicável, sem nenhum aviso, sem nenhuma caixa de 'ignorar' pra marcar. A porta destrancou do jeito certo.

Clico. 'Confirm merge.' E aparece: 'juntado com sucesso'. Agora sim — só agora, com o verde — o código entrou na linha principal. Posso até apagar a branch de teste; ela cumpriu o papel.

---

Olha o ciclo inteiro: app são, eu quebrei, tentei entregar, a porta trancou, consertei, a porta abriu. Em nenhum momento o código quebrado encostou na linha principal do seu app. O porteiro fez o trabalho que ontem ficava na sua memória — e hoje não depende nem da sua memória, nem da sua disciplina, nem da sua boa vontade numa sexta à noite."

---

## SEÇÃO 6: ENCERRAMENTO — O PORTEIRO ESTÁ DE PLANTÃO — 9 min

**Tom:** Síntese pelo aluno, LGPD orgânico, o brinde do selo, e a ponte para a forma visível.

"Recapitula — você dizendo, na sua cabeça.

Você completou o robô: os três guardiões — calculadora, checklist e a honestidade da busca — rodam no servidor a cada entrega. Você ligou a fechadura, clicando, sem digitar nada. E viu a porta trancar: o mesmo código quebrado que ontem entrou, hoje foi barrado, e só passou depois de consertado. O robô deixou de avisar e passou a impedir.

---

E a privacidade, que é o eixo de tudo.

Repara: a fechadura que você ligou hoje protege a qualidade do código — não muda nada sobre o que sobe pro servidor. O que o robô roda continua sendo só a receita do app e os pacientes fictícios dos controles. A pasta `data/` — o banco com as suas cirurgias, os seus artigos — segue trancada, como sempre. O porteiro vigia o que entra no seu código; ele nunca vê, nunca toca, nunca deixa sair o que é do paciente. Você ganhou uma trava de qualidade sem abrir um milímetro na trava de privacidade.

---

E um presentinho de dois minutos, porque você merece um troféu na parede. Cola:"

[TELA: digitar o Prompt do selo]

```
Por último, coloque no topo do meu arquivo README.md um selo (badge) que mostra, para
quem abrir o repositório, se os testes estão passando — aquele selinho verde escrito
"passing" quando o robô está verde. Use o selo oficial do GitHub Actions, que reflete
o estado real do meu robô. Edite o README por mim e, quando terminar, me diga os
comandos git para enviar e onde no GitHub eu vou ver o selo. Não precisa me mostrar o
conteúdo do README.
```

[TELA: enviar]

```bash
git add .
git commit -m "docs: adiciona selo de testes passando no README"
git push
```

"Abre a página inicial do seu repositório. Lá no topo, um selo verde: 'passing'. É o crachá do seu app na recepção, dizendo a quem chega: 'aqui o porteiro está de plantão, e está tudo verde'. Você não fez por vaidade — fez porque um app clínico que se diz seguro tem que provar, na porta, que é.

(E um detalhe pra próxima fronteira: esse robô usou uma chave pra trabalhar — uma credencial. Guarda essa palavra: chave. Mais pra frente a gente garante que ela nunca vaze.)

---

Agora para um segundo e pensa onde a gente chegou.

A fundação do seu app está à prova de bala. As contas estão certas e guardadas por testes. O checklist é imutável. A busca é honesta. E um porteiro tranca a porta pra qualquer coisa quebrada — sem depender de você lembrar de nada. Por dentro, esse app é sólido como poucos sistemas que você usa no hospital.

Mas tem uma coisa que a gente nunca cuidou. Uma coisa que o paciente — e você, todo santo dia — vê primeiro.

A cara do app.

As cores. As letras. Os ícones. O espaço entre as coisas. Tudo que faz a diferença entre uma tela que dá confiança e uma tela que parece um experimento de laboratório.

Na próxima aula, agora que a fundação está à prova de bala, a gente cuida do que o paciente VÊ: a aparência do ClinMd-Tribe. Vamos vestir esse app sólido com uma roupa à altura — uma identidade visual médica, limpa, profissional. A engenharia está pronta. Agora vem a forma.

Até lá."

---

**FIM DO ROTEIRO**

---

> **NOTAS DE PRODUÇÃO (não falar — operacional):**
>
> - **RAG no runner (Seção 2):** confirmar o robô completo (com RAG) verde ANTES de gravar; cache do modelo configurado. A narração da Seção 2 descreve a experiência real do aluno na 1ª vez (download + "guardar a cópia"); na gravação, ou registrar esse 1º download de fato (cortando a espera na edição) OU, se o cache já estiver quente, ajustar a fala para "restaurando a cópia guardada, rápido".
> - **Branch protection (CRÍTICO, Seção 4):** confirmar o caminho exato (Settings → Branches **ou** Settings → Rules → Rulesets) na conta-piloto e gravar com os rótulos exatos da tela. O status check só aparece na lista DEPOIS de o CI ter rodado ≥1 vez; selecionar o check com o nome do job **idêntico** ao do robô (divergência = check "pendente eterno").
> - **NÃO ligar "Include administrators" / "Do not allow bypassing":** senão o dono solo se tranca fora da própria main sem rota de correção emergencial.
> - **Required status checks (Seção 4):** marcar como obrigatório ao menos o check do job RÁPIDO (calculadora+checklist) — é o que pega a sabotagem do AVC e garante o vermelho rápido no clímax. Se marcar também o job do RAG como obrigatório, confirmar na pré-gravação que o cache está quente e ele fica verde rápido, senão o conserto pode ficar "pendente" esperando o RAG e o merge não liberar ao vivo.
> - **Comportamento do clímax (Seção 5) — admin/dono solo (CRÍTICO):** branch protection NÃO se aplica ao admin por padrão (e a nota acima manda NÃO trancar o admin). Logo, no vermelho, o botão "Merge" limpo não fica disponível, MAS o GitHub oferece a caixa "Merge without waiting for requirements to be met (bypass branch protections)". O roteiro foi escrito para ESSA verdade (o dono pode furar marcando a confissão; o merge limpo só aparece no verde). **NÃO** prometer botão morto/inclicável — isso só ocorreria com "Do not allow bypassing" ligado, que trancaria o dono. Confirmar os rótulos exatos na pré-gravação.
> - **PR atualiza sozinho:** o 2º push (conserto) vai para a MESMA branch; o PR existente reavalia — NÃO abrir PR novo.
> - **1º push da branch nova:** o upstream da `teste-do-porteiro` pode não estar setado; o Claude entrega o comando correto (ex.: `git push origin teste-do-porteiro`); o aluno não adivinha flag.
> - **Reversibilidade:** a sabotagem vive na branch descartável (deletada no merge); a `main` nunca recebe o quebrado — sem working tree sujo no fim.
> - **Cota de Actions:** 2 jobs + cache consomem mais minutos; usar `clinmd-tribe-demo` se apertar.
