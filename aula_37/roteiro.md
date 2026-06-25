# Aula 37 — A Roupa do App: Vestindo o ClinMd-Tribe de Uma Vez Só

**Formato:** Gravada no OBS Studio, editada no Kdenlive
**Duração:** ~60 min
**Tom:** Clínico-zeloso com a forma; do orgulho da engenharia sólida ao cuidado com a forma. "Por dentro é à prova de bala — agora a cara precisa dizer isso." A virada emocional é ver várias telas desconjuntadas virarem uma família visual com um único pedido.
**Módulo:** S11.01 — UI médica: paleta, tipografia, ícones (Flet)

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] Projeto conectado ao repositório clinmd-tribe no GitHub, com o último trabalho já enviado (push), branch main em dia.
- [ ] As telas das aulas anteriores (calculadora, checklist, busca, painel) já estão montadas num app único navegável, e uv run flet run main.py abre a janela.

**Confira antes de gravar:**

- [ ] Existe um "antes" feio real: grave o 1o uv run flet run main.py ANTES de aplicar o tema (telas com a cor default do Flet) e o 2o depois.
- [ ] A fonte Inter você providencia via Google Fonts: o prompt já pede ao Claude carregar a Inter pela internet (page.fonts) e registrar como fonte do app; NÃO baixe a fonte aqui.
- [ ] A URL da Inter é de versão ESTÁTICA (o Flet só renderiza fontes estáticas; a Inter padrão do Google Fonts é variável e pode não aparecer). Se a conexão for instável, considere baixar a Inter estática para assets/fonts/ e usar assets_dir; ajuste a fala do "flash" se for o caso.
- [ ] git push direto na main é aceito pra o dono-admin (a aula passada ligou branch protection sem trancar o admin); se a proteção barrar o admin, reescreva as entregas como micro-PR.
- [ ] O pipeline (aula 35/36) fica verde após o push do tema e do acabamento da Seção 7 (mudança só visual não pode quebrar teste); a narração promete "verde".
- [ ] O par texto #2E3233 sobre fundo #FAFAFA tem contraste seguro; mantenha o secundário #646C6F só sobre fundos claros.

**Navegador:** nenhum site é necessário nesta aula (o trabalho é no terminal e na janela do app; a Inter chega da internet sozinha pelo prompt).

---

## SEÇÃO 1: ABERTURA — O JALECO AMASSADO — 5 min

**Tom:** Reflexivo. Retoma o gancho da aula_36 e nomeia o desconforto da forma.

**[Aviso rápido dos óculos, antes de mergulhar]**

"Hoje a aula é sobre cor, letra e o que dá gosto de olhar, então convém olhar bem: põe os óculos. Seria irônico passar a aula inteira falando de legibilidade com o terminal embaçado, não acha? Olho descansado pra julgar a roupa nova do app."

"Nas últimas aulas a gente blindou o seu app por dentro. As contas estão certas e guardadas por testes. O checklist é imutável. A busca é honesta. E um porteiro tranca a porta pra qualquer coisa quebrada, sozinho, a cada entrega. Por dentro, o ClinMd-Tribe é sólido como poucos sistemas que você usa no hospital.

E no fim da aula passada eu te prometi uma coisa. Lembra?

A cara do app. As cores, as letras, os ícones, o espaço entre as coisas. A roupa.

---

Pensa numa coisa que você sente todo dia, mesmo sem nomear.

Dois médicos, igualmente competentes. Um te recebe de jaleco impecável, prontuário organizado, sala limpa. O outro, jaleco amassado, papel pra todo lado, letra ilegível. Os dois podem ser geniais. Mas a confiança que o paciente deposita antes da primeira palavra — ela já começou a ser decidida pela forma.

O seu app hoje é o segundo médico. Genial por dentro. Amassado por fora.

---

A calculadora tem uma cara. O checklist tem outra. A busca tem outra. O painel financeiro, outra. Cada tela nasceu numa aula diferente, e cada uma escolheu a própria cor de botão, o próprio tamanho de letra, o próprio espaçamento. Não é feio — é desconjuntado. Parece quatro apps diferentes morando no mesmo lugar.

Hoje a gente passa o ferro nesse jaleco. Não tela por tela — isso seria trabalho de formiga. A gente vai definir a roupa UMA vez, num lugar só, e ela vai vestir o app inteiro de uma vez. E você não vai escrever nem ler uma linha de código pra isso. Você vai descrever a roupa. E ver o app se vestir."

---

## SEÇÃO 2: O UNIFORME DO HOSPITAL — 8 min

**Tom:** Didático, tranquilo. A maquete mental do "tema central" antes de qualquer prompt. Aqui mora a primeira decisão técnica, traduzida.

"Antes de pedir nada, deixa eu te mostrar a ideia que faz isso funcionar — porque ela é o coração da aula, e ela é simples.

Pensa num hospital grande, bem administrado. Os jalecos não são escolhidos por cada funcionário no balcão da loja. Existe um padrão definido numa sala só — a cor do tecido, o logo no bolso, a fonte do crachá. Foi decidido uma vez, lá em cima. E todo mundo, em todo andar, veste aquilo. Chegou funcionário novo? Recebe o mesmo uniforme. Ninguém precisa avisar tela por tela, andar por andar.

---

O seu app vai ganhar exatamente essa sala.

No mundo do Flet — a ferramenta em que o seu app é feito — existe um lugar onde se define a identidade visual de tudo: a cor principal, as cores de apoio, a fonte, o estilo dos cartões. O nome técnico disso é tema. Mas esquece o nome. Lembra da sala onde o uniforme do hospital é decidido. É isso.

Você define a roupa nessa sala UMA vez. E todas as telas — a calculadora, o checklist, a busca, o painel — herdam aquilo automaticamente. Mudou a cor na sala? Mudou em todas as telas, no mesmo instante. Nasceu uma tela nova amanhã? Já nasce vestida certo, sem você fazer nada.

---

E olha por que isso importa pro futuro — porque isso não é só sobre hoje.

Imagina o oposto: cada tela com a cor escrita na mão, lá dentro dela. Pra trocar o roxo do app, você teria que abrir a calculadora, trocar; abrir o checklist, trocar; abrir a busca, trocar; e rezar pra não esquecer nenhuma. Um erro de cópia em qualquer uma, e o app fica com duas caras. Isso é o que a gente chama de remendo espalhado — e é exatamente o tipo de bagunça que, lá na frente, vira um monstro pra mexer.

A sala única é o contrário do remendo espalhado. Uma fonte de verdade pra aparência. Decide num lugar, vale em todo lugar.

Guarda essa ideia — 'decidir num lugar só pra valer em todo lugar'. Daqui a duas aulas ela volta com força, quando a gente falar de não deixar o app virar um monolito embolado. Hoje você vai sentir o gostinho dela na pele, com cor."

---

## SEÇÃO 3: A PALETA DA TRIBEMD — 6 min

**Tom:** Apresentar a identidade real, sem tecnês. Dar nome de gente a cada cor.

"Agora, qual roupa? A gente não vai inventar cor no susto. O seu app faz parte de um mundo — o da TribeMD — e esse mundo já tem uma identidade definida, pensada por gente de design. A gente vai vestir o ClinMd-Tribe com ela. Assim o seu app conversa com o resto da marca, e parece o que é: profissional.

Deixa eu te apresentar a paleta, em português de gente:

---

A cor da casa é um roxo. Um roxo sério, encorpado — não é o roxo de festa, é o roxo de marca médica confiável. Ele é a cor dos botões, dos links, das coisas em que você clica. Quando você bate o olho e pensa 'isso aqui é uma ação', é esse roxo que aparece.

A cor da letra é um quase-preto. Não o preto duro de caneta — um cinza-escuro profundo, que cansa menos a vista numa tela que você vai encarar o dia inteiro. E pra textos de apoio, legendas, coisas secundárias, um cinza mais suave, que recua e não disputa atenção com o que importa.

O fundo é claro, quase branco. Limpo. Tipo papel de qualidade. As seções e os cartões usam um cinza muito leve pra se destacarem do fundo sem precisar de borda grossa nem sombra pesada. O estilo é leve, arejado, editorial — parece um bom artigo de revista médica, não um formulário de repartição.

E a fonte: uma letra moderna, redonda, altamente legível, chamada Inter. É a letra que a TribeMD usa. Ela funciona bem em tamanho pequeno e em tela — exatamente o que um app clínico precisa.

---

Resumo da roupa: roxo pra ação, quase-preto pra ler, fundo claro pra respirar, cartões leves, e a fonte Inter em tudo. Essa é a identidade. Agora a gente entrega ela pro Claude — e ele costura."

---

## SEÇÃO 4: VOCÊ DECIDE — 9 min

**Tom:** Colaborativo. Duas perguntas, raciocínio clínico/estético, zero código.

"Antes de pedir pro Claude vestir o app, guarda quatro palavras — os quatro sinais de uma tela que dá confiança. Consistência: tudo da mesma família. Hierarquia: o olho sabe o que ler primeiro, o título forte, o apoio recuado. Contraste: dá pra ler sem esforço. E respiro: nada espremido. Consistência, hierarquia, contraste, respiro — no fim da aula você vai usar esses quatro óculos pra julgar a sua própria tela.

E agora, duas perguntas. Pensa como quem cuida da forma porque a forma protege o conteúdo.

---

**PERGUNTA UM — por que definir a cor num lugar só, em vez de em cada tela?**

A gente tem quatro telas. Eu poderia pintar cada uma na mão, ali mesmo onde ela mora. Por que insistir na 'sala única'?

A: porque a sala única deixa o app mais bonito do que pintar tela por tela.

B: porque pintar tela por tela espalha a mesma decisão por quatro lugares — e no dia que eu quiser mudar uma cor, ou esquecer de atualizar uma tela, o app fica com duas caras. Num lugar só, eu mudo uma vez e vale pra tudo, sem risco de esquecer.

C: porque a sala única roda mais rápido.

Pensa um segundo.

---

É a B.

Não é sobre beleza — A está errado: a roupa fica igualzinha das duas formas, no primeiro dia. Não é sobre velocidade — C está errado, isso não tem nada a ver com rapidez.

É sobre o que acontece no segundo dia, e no centésimo. No dia em que a TribeMD ajustar o tom do roxo. No dia em que você criar uma quinta tela. Com a cor escrita na mão em cada lugar, cada mudança é uma caça ao tesouro, e um esquecimento deixa o app remendado. Com a sala única, é um ajuste só.

Critério que fica: repetir a mesma decisão em vários lugares não é trabalho a mais — é risco a mais. Toda decisão que vale pra tudo deve morar num lugar só. Vale pra cor hoje; vale pra arquitetura do app inteiro, como você vai ver na frente.

---

**PERGUNTA DUAS — você vai pôr a letra do app num cinza-escuro sobre fundo quase-branco. Tem um cuidado clínico aí. Qual?**

A: nenhum — qualquer cor de letra sobre qualquer fundo serve, é só gosto.

B: a letra precisa ter contraste suficiente com o fundo pra ser lida sem esforço — por uma pessoa cansada, num plantão, numa tela com brilho ruim, talvez com a vista já não tão boa. Cor demais clara, ou contraste de menos, e você cria um app que cansa ou exclui.

Pensa.

---

É a B.

Isso tem até nome técnico — acessibilidade — mas pensa nela como você pensa no tamanho da letra de uma bula. Uma bula com letra cinza-claro minúscula sobre fundo branco é uma bula que machuca o paciente, não por veneno, por ilegibilidade.

O seu app vai ser usado por gente cansada, em horários ruins, em telas baratas. A escolha de um quase-preto encorpado sobre um fundo claro não é capricho de designer — é a mesma lógica de prescrever com letra legível. A forma, aqui, é segurança.

Critério que fica: cor não é só estética; legibilidade é cuidado com quem usa. Quando a gente pedir a roupa pro Claude, a gente vai pedir explicitamente que ele garanta esse contraste. Beleza que não se lê não serve a paciente nenhum."

---

## SEÇÃO 5: COSTURANDO A ROUPA — A SALA ÚNICA — 11 min

**Tom:** Mãos à obra. Primeiro o ritual de terreno limpo, depois o prompt que cria o tema central e veste o app inteiro de uma vez.

"Hora de vestir o app. E como sempre, antes de mexer, o ritual: conferir que o terreno está limpo e que nada de paciente se mistura. Cola:"

[TELA: digitar o Prompt 0 no Claude Code]

```
Você é meu par de programação. Hoje eu vou dar uma identidade visual ao meu app
ClinMd-Tribe (feito em Flet): paleta de cores, fonte e estilo, aplicados ao app
inteiro. Antes de começar, confira o estado do meu projeto e me responda em
português, SEM me mostrar saída técnica crua, apenas:
  1. se o meu projeto está conectado ao repositório clinmd-tribe no GitHub e se o
     meu último trabalho já foi enviado (push), com a branch main em dia;
  2. se a pasta data/ continua protegida pelo .gitignore — eu não quero banco,
     artigos nem dado de paciente saindo da minha máquina;
  3. se o app ainda roda normalmente hoje (o comando uv run flet run main.py),
     para a gente comparar a aparência antes e depois.

Se algo estiver pendente, conserte você mesmo e confirme em uma frase. NÃO me mostre
código nem arquivos de configuração.
```

"Terreno confirmado, `data/` trancada, o app roda. Agora a roupa. Repara no tamanho do pedido — eu vou descrever a identidade inteira, com as cores em código de cor (aquele `#` com letras e números é só o jeito universal de nomear uma cor exata, como o número de um tom de tinta na loja), e vou exigir três coisas: que ele guarde tudo numa sala única, que aplique no app inteiro de uma vez, e que garanta o contraste. Cola:"

[TELA: digitar o Prompt 1 — o tema central]

```
Agora dê uma identidade visual profissional ao meu app ClinMd-Tribe, usando o
sistema de tema do Flet. O objetivo, em uma frase: definir a aparência UMA vez, num
único lugar, e fazer todas as telas do app (calculadoras, checklist, busca, painel
financeiro) herdarem essa aparência automaticamente — sem cor escrita à mão tela
por tela.

A identidade é a da TribeMD:
  - Cor principal (botões, links, ações): roxo #5213B9.
  - Cor do texto principal: #2E3233 (um quase-preto). Texto secundário/legendas: #646C6F.
  - Fundo do app: #FAFAFA (quase branco). Fundo de seções: #E5E9EA. Realce/chips
    ao passar o mouse: #E9E1F5. Rodapé/áreas escuras: #1F0646.
  - Fonte: Inter (a fonte da TribeMD) como fonte padrão de TODOS os textos do app.
    Carregue a Inter pela internet (Google Fonts) e a registre como fonte do app,
    para ela aparecer mesmo em quem não tem a fonte instalada. Use uma versão
    ESTÁTICA da Inter — o Flet só aceita fontes estáticas, não a versão variável;
    se a URL que você achar for da Inter variável, escolha um peso estático.
  - Estilo geral: claro, arejado, editorial — cartões com cantos suaves e
    separação leve do fundo, SEM sombras pesadas nem bordas grossas.

Requisitos importantes:
  - Centralize TUDO num único lugar de tema na camada de apresentação do projeto (um
    arquivo só de cores/fonte/estilo). Aplique esse tema no app inteiro de uma vez,
    no ponto onde o app é montado — não repita cor nenhuma escrita à mão dentro das
    telas individuais. Se hoje houver cor escrita à mão em alguma tela, troque por
    referência a esse tema central.
  - Garanta contraste e legibilidade: o texto #2E3233 sobre o fundo #FAFAFA precisa
    ser confortável de ler por uma pessoa cansada numa tela comum. Se algum par de
    cores ficar difícil de ler, me avise em português qual e ajuste para um contraste
    seguro.
  - Não mude o que o app FAZ — só a aparência. As contas, o checklist, a busca e os
    testes têm que continuar funcionando igual.
  - Não toque na pasta data/.

NÃO me mostre o conteúdo dos arquivos — eu não preciso ler. Quando terminar, me diga
em português: (1) que a identidade está aplicada e onde ela mora (a "sala única");
(2) o comando para eu rodar o app e ver a transformação; (3) o que eu vou notar de
diferente nas telas. Se eu pedir para mudar uma cor depois, me explique que basta
mudar nesse único lugar.
```

"E pronto. O Claude vai criar a sala única — um lugar só, na parte do projeto que cuida da aparência — e ligar ela no app inteiro. Ele baixa a fonte Inter da internet e registra ela como a letra oficial. E onde antes tinha cor escrita na mão, ele troca por uma referência à sala. Você não escreveu nada. Você descreveu uma roupa. Agora vamos ver o app vestir."

---

## SEÇÃO 6: O CLÍMAX — ANTES E DEPOIS — 12 min

**Tom:** O ápice. Desacelera. A transformação visual acontece na frente do aluno: a tela crua, depois a tela vestida. O payoff é puramente visual.

"Aqui é a parte que dá gosto. A gente vai ver a roupa entrar no corpo. E pra isso, eu preciso primeiro te mostrar o app pelado — pra você sentir a diferença na pele.

Antes de rodar, um detalhe da fonte que importa: a letra Inter vem da internet. Então, na primeiríssima vez que o app abrir, pode ser que o texto pisque por um segundo com uma letra qualquer, e logo troque pra Inter quando ela terminar de chegar. É normal — é a roupa chegando da lavanderia. Da segunda vez em diante, ela já está ali, instantânea.

Roda o app:"

[TELA: no terminal]

```bash
uv run flet run main.py
```

"O que você espera ver: o app abre numa janela. E olha as telas — a calculadora, o checklist, a busca. Repara, agora com olho crítico, em três coisas: os botões, com a cor padrão sem graça, meio azulado-genérico, sem personalidade. A letra, naquela fonte padrão do sistema, que serve mas não diz nada. E o conjunto, desconjuntado — cada tela com o seu próprio jeito, como a gente falou na abertura. Esse é o jaleco amassado. Guarda essa imagem na cabeça.

Fecha a janela do app — é só fechar a janela na tela, ou apertar `Ctrl + C` no terminal pra encerrar.

---

Agora eu peço pro Claude aplicar tudo. Ele já entendeu o pedido na seção anterior — se ele ainda não terminou de costurar, é agora que ele finaliza e confirma em português: 'pronto, a identidade está aplicada, ela mora num lugar só, pode rodar'.

E aqui vem o momento. Roda de novo, exatamente o mesmo comando:"

[TELA: no terminal]

```bash
uv run flet run main.py
```

"[pausa]

Olha agora.

A janela abre — e é outro app. Os botões agora são daquele roxo encorpado da TribeMD. Aquele mesmo roxo, repara, em todas as telas: o botão de calcular o escore, o botão do checklist, o botão de buscar. A mesma cor, a mesma família. A letra mudou pra Inter — mais redonda, mais limpa, mais fácil de ler. O fundo clareou, ficou arejado. Os cartões agora se separam do fundo com leveza, sem aquela borda dura. E o texto está naquele quase-preto confortável.

E o pulo do gato: passa de uma tela pra outra. Calculadora, checklist, busca, painel. Todas vestidas igual. Mesma cor de ação, mesma letra, mesmo respiro. Não parecem mais quatro apps. Parecem um app só, com identidade. Uma família.

E agora pega aqueles quatro óculos e diagnostica a melhora você mesmo. Consistência: ganhou — é a mesma família agora, do checklist à busca. Hierarquia: o resultado que importa salta, o rótulo recuou. Contraste: texto quase-preto em fundo claro, lê de longe. Respiro: os elementos descolaram, a tela acalmou. Quatro mudanças, quatro princípios — e você não desenhou nada, só pediu e soube dizer por que ficou melhor.

E não é vaidade. Lembra da bula? Essa letra, esse contraste, esse respiro — é a mesma tela, mas agora ela se lê num plantão de madrugada sem forçar a vista. Ficou bonita, sim. Mas, principalmente, ficou mais difícil de errar lendo ela. A forma virou segurança, na frente dos seus olhos.

---

[pausa]

Para um segundo e pensa no que você acabou de fazer — e principalmente em como.

Você não abriu a tela da calculadora pra pintar o botão. Não abriu o checklist pra trocar a letra. Você descreveu uma roupa, em português, num pedido só. E o app inteiro se vestiu de uma vez — porque a roupa mora num lugar só, e todas as telas bebem dali.

E é por isso que eu insisti tanto na 'sala única'. Imagina se cada tela tivesse a sua cor escrita na mão: pra ver essa transformação, o Claude teria que abrir e repintar tela por tela, e qualquer esquecimento deixaria uma tela velha no meio das novas. Em vez disso: um lugar, uma vez, tudo muda. Esse é o poder de decidir num lugar só.

---

Quer sentir o poder na ponta dos dedos? Vamos provar que a sala manda. Eu vou pedir uma troca de cor — e olha como ela é cirúrgica:"

[TELA: digitar o Prompt da prova — opcional, ao vivo]

```
Só para eu sentir como funciona a "sala única": troque a cor principal do app de roxo
#5213B9 para um roxo um tom mais escuro, mexendo APENAS no lugar central do tema, sem
tocar em nenhuma tela individual. Depois me diga em uma frase que você mudou só num
lugar, e o comando para eu rodar e ver. Logo em seguida, volte para o roxo original
#5213B9 do mesmo jeito.
```

"Repara no que o Claude diz: ele mexeu num lugar, e os botões de TODAS as telas mudaram juntos. Não teve caça ao tesouro. É a sala mandando no hospital inteiro. (E ele já devolveu pro roxo certo da marca — a gente só queria ver a alavanca funcionar.)

---

Agora que a roupa está pronta e aprovada, a gente registra esse trabalho. E aqui vale uma ponte com a aula passada: lembra que você trancou a porta da main e fez tudo passar pela antecâmara? Aquela trava continua lá — pra mudança de regra clínica, que é séria. Mas você é o dono do prédio, e o dono tem a chave: pra uma troca de roupa, que não mexe em conta nenhuma, você entra direto. O robô ainda confere por cima do seu ombro — se a roupa tivesse quebrado uma conta, ele ficaria vermelho. A antecâmara obrigatória fica pra quem não é dono, e pra mudança de regra de verdade."

[TELA: no terminal]

```bash
git add .
git commit -m "feat: identidade visual TribeMD aplicada via tema central (paleta, Inter, cards)"
git push
```

"O que esperar: o push sobe direto pra main. O robô acorda no GitHub e roda os guardiões — não pra te barrar, mas pra te confirmar que a roupa nova não quebrou nada. Mudou só a aparência, então as contas continuam certas, o checklist imutável, a busca honesta. O robô fica verde. E a antecâmara, o porteiro que tranca a porta, fica reservada pro que mexe em regra de verdade — roupa, o dono passa direto, de olho no robô."

---

## SEÇÃO 7: OS ÍCONES E O RESPIRO — 8 min

**Tom:** Acabamento fino. Ícones clínicos coerentes e espaçamento editorial, ainda sem o aluno tocar em código.

"A roupa está vestida. Falta o acabamento — os detalhes que separam 'arrumado' de 'caprichado'. Dois deles: os ícones e o respiro entre as coisas.

Ícones primeiro. Repara que algumas telas têm uns símbolos — ou deviam ter. O Flet já vem com uma biblioteca enorme de ícones prontos, profissionais, do mesmo estilo. Você não precisa desenhar nada, nem caçar imagem na internet. Você só precisa pedir, em português, qual ícone combina com cada coisa: um coração pra calculadora cardiológica, uma prancheta com tique pro checklist cirúrgico, uma lupa pra busca, um gráfico pro painel financeiro. O Claude escolhe da biblioteca e encaixa, todos no mesmo estilo e na cor da casa.

E o respiro — o espaço entre os elementos. Um app que aperta tudo num canto cansa e confunde. Um app editorial deixa as coisas respirarem: margem em volta dos cartões, espaço entre um campo e outro, alinhamento limpo. Isso também é só pedir.

Cola este último pedido de acabamento:"

[TELA: digitar o Prompt do acabamento]

```
Agora dê o acabamento final na aparência do app, sem mudar o que ele faz e mantendo
tudo coerente com o tema central que a gente acabou de criar (não escreva cor à mão
nas telas):

  1. Ícones: use ícones da biblioteca pronta do Flet (Material), todos no mesmo
     estilo e na cor principal do tema, coerentes com cada tela clínica. Sugestões:
     um ícone de coração para a calculadora cardiológica; uma prancheta com marca de
     verificação para o checklist; uma lupa para a busca; um gráfico/painel para o
     financeiro. Escolha os mais adequados da biblioteca e me diga em português quais
     você usou em cada tela.

  2. Espaçamento e cartões: dê um respiro editorial — margens confortáveis em volta
     dos cartões, espaço agradável entre campos e botões, alinhamento limpo. Sem
     apertar tudo num canto. Mantenha o estilo leve, sem sombras pesadas.

  3. Consistência: garanta que TODAS as telas usem a MESMA cor de botão (o roxo do
     tema), o MESMO tipo de cartão e o MESMO espaçamento. Se você achar alguma tela
     fora do padrão, alinhe ela ao resto.

NÃO me mostre o código. Quando terminar, me diga em português o que mudou em cada
tela e o comando para eu rodar e ver.
```

[TELA: no terminal]

```bash
uv run flet run main.py
```

"Roda. Olha o acabamento: cada tela com o seu ícone clínico, todos da mesma família, todos no roxo. E tudo respirando — os cartões com margem, os campos com espaço, nada espremido. Agora sim parece um produto, não um protótipo.

Entrega de novo, pro porteiro abençoar:"

[TELA: no terminal]

```bash
git add .
git commit -m "style: ícones clínicos coerentes e espaçamento editorial nas telas"
git push
```

"Verde de novo. O robô confirma: acabamento aprovado, contas intactas."

---

## SEÇÃO 8: ENCERRAMENTO — A FORMA À ALTURA DO CONTEÚDO — 6 min

**Tom:** Síntese pelo aluno, LGPD orgânico, e a ponte para a próxima aula (exportar .exe).

"Recapitula — você dizendo, na sua cabeça.

Você deu uma identidade visual profissional ao seu app — a paleta da TribeMD, a fonte Inter, o estilo editorial. E fez isso do jeito certo: definindo a roupa UMA vez, numa sala única, e deixando todas as telas herdarem. Você viu o app pelado, descreveu a roupa em português, e viu o app inteiro se vestir de uma vez. Trocou ícones, deu respiro, alinhou tudo. E em nenhum momento abriu uma tela pra pintar botão na mão, nem leu uma linha de código. Você leu telas: a crua, e a vestida.

---

E a privacidade, que é o eixo de tudo.

Repara: hoje a gente mexeu só na casca — cor, letra, ícone, espaço. Nada disso toca em dado nenhum. A pasta `data/` — o banco com as suas cirurgias, os seus artigos — continua trancada, como sempre. O que subiu pro GitHub junto com a roupa nova foi só a receita visual do app: a sala de cores, a referência da fonte. O paciente não tem cor, não tem fonte, não viajou. Você embelezou a vitrine sem nunca abrir o cofre.

---

E olha onde a gente chegou.

Por dentro, o app é à prova de bala: contas guardadas, checklist imutável, busca honesta, porteiro de plantão. E agora, por fora, ele tem a cara disso. Uma identidade limpa, consistente, profissional. A engenharia e a forma, finalmente, falando a mesma língua. O jaleco está passado.

---

Mas tem uma coisa que ainda incomoda — e é a próxima fronteira.

Esse app lindo, sólido, vestido... ele só roda quando você abre o terminal e digita aquele comando. `uv run flet run main.py`. Pra você, hoje, tudo bem. Mas pensa no seu colega, o cardiologista da sala ao lado, que não sabe o que é um terminal — exatamente como você não sabia no começo deste curso. Como é que ELE abre o seu app? Você vai ensinar ele a digitar comando? Não.

Um produto de verdade abre com dois cliques. Um ícone na área de trabalho. Sem terminal, sem comando, sem você por perto.

Na próxima aula, a gente faz exatamente isso: empacota o ClinMd-Tribe num programa de Windows de verdade — um `.exe` — que qualquer médico abre clicando, como abre o Word. O app sai da sua máquina de desenvolvedor e vira algo que você entrega na mão de um colega.

A forma está pronta. Agora vem a entrega.

Até lá."

---

**FIM DO ROTEIRO**

---

> **NOTAS DE PRODUÇÃO (não falar — operacional):**
>
> **DECISÕES TÉCNICAS (resumo para quem for executar a pré-gravação no app real):**
>
> - **Tema central — onde mora:** um único módulo de tema na camada de apresentação (ex.: `clinmd_tribe/src/presentation/theme.py`), expondo os tokens da TribeMD (cores nomeadas + `font_family="Inter"`) e uma função que devolve o objeto de tema do Flet pronto. Justificativa: Clean Architecture já existente (a UI é `presentation`); o tema é decisão de apresentação, não de domínio. Isso materializa a "sala única" da narração e é a semente concreta da S12.02 (arquitetura modular / anti-monolito). NÃO espalhar cor hard-coded nas telas — o prompt da Seção 5 instrui o Claude a substituir cor literal por referência ao tema.
> - **Aplicação única:** o tema é atribuído UMA vez em `page.theme` (e `page.dark_theme` se houver modo escuro) no ponto de montagem do app (`main.py` / função `main(page)`), de onde o Flet propaga para todos os controles e telas, salvo override explícito por container. Confirmado na doc oficial de theming do Flet: um `Theme` em `page` propaga app-wide.
> - **Fonte Inter — como carrega:** via `page.fonts = {"Inter": "<url Google Fonts da Inter>"}` + `Theme(font_family="Inter")`. A Inter é servida pela internet (Google Fonts/asset remoto); por isso a narração da Seção 6 avisa do possível "flash" de fonte fallback no 1º load (FOUT) — a fonte precisa chegar antes de renderizar definitivamente. Confirmar na pré-gravação a URL que o Claude usar e que a Inter de fato aparece; se a conexão de gravação for instável, considerar baixar a Inter para `assets/` e usar `assets_dir` (fonte local, sem flash) — ajustar a fala do "flash" se for o caso.
> - **Cores — tokens TribeMD:** primária `#5213B9`; texto `#2E3233` / secundário `#646C6F`; bg `#FAFAFA`; seção `#E5E9EA`; hover/chip `#E9E1F5`; footer/escuro `#1F0646`. No Flet, mapear primária para `ColorScheme(primary=...)` e definir background/surface coerentes; demais tokens como constantes do módulo de tema referenciadas pelas telas.
> - **Ícones:** biblioteca Material embutida do Flet (`ft.Icons.*`) — sem assets externos. O Claude escolhe os semânticos (coração, prancheta+check, lupa, gráfico) e os tinge com a primária do tema. Sem o aluno codar nada.
>
> **CALIBRE / ARMADILHA BASH (CRÍTICO):**
> - **NUNCA** usar `uv run python -c` nem qualquer execução inline de Python em tela. Os ÚNICOS comandos de terminal mostrados ao aluno são `uv run flet run main.py` e `git` (`add`/`commit`/`push`). Conferido contra a restrição da aula.
> - O aluno NÃO lê nem escreve código/CSS/tema. Todo o trabalho visual é via prompt em linguagem natural + observação da tela (antes/depois). Os blocos de prompt são para COLAR no Claude Code, não para o aluno entender por dentro.
>
> **PRÉ-GRAVAÇÃO (estado do app real):**
> - O repo hoje tem o esqueleto Clean Arch (`clinmd_tribe/src/{presentation,application,domain,infrastructure}`) com `__init__.py` por camada; as telas (calculadoras, checklist, busca, painel) são materializadas pelos prompts das aulas S05–S08/S06/S07. CONFIRMAR na conta-piloto que existe um `main.py` que monta as telas e que `uv run flet run main.py` abre a janela ANTES de gravar o "antes". Se as telas ainda não estiverem todas montadas num app único navegável, esse é pré-requisito da aula_37 e deve ser resolvido na pré-gravação (não ao vivo).
> - **Antes/depois observável:** o efeito visual depende de existir um "antes" feio real. Gravar o 1º `uv run flet run main.py` ANTES de o Claude aplicar o tema (telas com cor default do Flet) e o 2º DEPOIS. Se a edição preferir, capturar as duas execuções em momentos separados e cortar a espera de compilação/download na pós.
> - **Prova da "sala única" (Seção 6, troca de cor):** opcional ao vivo; se incluída, garantir que o Claude reverte para `#5213B9` no mesmo turno (o prompt já pede). Se o tempo apertar, cortar essa demonstração e manter só o antes/depois principal.
> - **CI verde após mudança visual:** mudança só de aparência NÃO deve quebrar testes. Confirmar na pré-gravação que o pipeline (aula_35/36) fica verde após o push do tema **e do acabamento da Seção 7** (o acabamento mexe em layout/ícones — é o candidato mais provável a esbarrar em algum teste estrutural). Se algum teste tocar em layout/texto literal, ajustar antes (não ao vivo). A narração das Seções 6 e 7 promete "verde" — não encerrar com o porteiro vermelho.
> - **FONTE ESTÁTICA (CRÍTICO p/ o clímax):** o Flet só renderiza fontes ESTÁTICAS. A Inter padrão do Google Fonts é VARIÁVEL (`Inter[opsz,wght].ttf`) e pode silenciosamente não aparecer — matando o "depois" da Seção 6. Validar na pré-gravação que a URL é de Inter estática; se necessário, baixar Inter-Regular/SemiBold estáticos para `assets/fonts/` e usar `assets_dir`. (O Prompt 1 já pede versão estática.)
> - **PUSH DIRETO NA MAIN — interação com a aula_36 (CRÍTICO):** a aula_36 ligou branch protection na main. Confirmar na conta-piloto que `git push` direto na main é ACEITO para o dono-admin (bypass de admin, conforme a nota da aula_36 que NÃO liga "Do not allow bypassing"). Se a proteção barrar o push direto mesmo para o admin, a narração "o push sobe direto" fica falsa — nesse caso, reescrever as entregas das Seções 6 e 7 como micro-PR (branch → push → CI verde → merge). NÃO gravar antes de validar empiricamente o push direto.
> - **Contraste/acessibilidade (Seção 4 P2 + prompt Seção 5):** `#2E3233` sobre `#FAFAFA` tem contraste alto (seguro). O prompt pede ao Claude validar e avisar pares de baixo contraste; checar que nenhum texto secundário (`#646C6F`) caia sobre fundo escuro sem contraste — manter `#646C6F` apenas sobre fundos claros (`#FAFAFA`/`#FFFFFF`/`#E5E9EA`).
> - **Consistência (Seção 7):** validar visualmente que TODAS as telas usam o mesmo roxo de botão e o mesmo padrão de cartão após o prompt de acabamento — é o critério de "feito" da aula. Qualquer tela fora do padrão = sinal de cor hard-coded remanescente; reabrir o prompt para alinhar via tema central.
>
> **GANCHOS:**
> - **S12.02 (aula_41, anti-monolito):** "decidir num lugar só pra valer em todo lugar" é plantado de propósito nas Seções 2, 4 (P1) e 6 — a sala única é o exemplo palpável de modularidade que a S12.02 generaliza.
> - **S11.02 (aula_38, próxima):** o encerramento abre a tensão "o app só roda por comando no terminal" → empacotar como `.exe` clicável. A fala "como o seu colega abre isso?" é a ponte direta.
> - **Reversibilidade:** a troca-e-volta de cor da Seção 6 não deixa working tree sujo se revertida no mesmo turno antes do commit; commitar apenas o estado final aprovado (roxo `#5213B9`).
