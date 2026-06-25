# Aula 40 — A Chave que Vale Ouro: Nunca Suba seu Token

**Formato:** Gravada no OBS Studio, editada no Kdenlive
**Duração:** ~55 min
**Tom:** Abertura de um arco novo — os hábitos de quem entrega. Sério sobre o risco (chave vazada custa caro), tranquilizador sobre a prática. O reflexo de segurança ancorado no que o médico já vive: a chave do armário de controlados.
**Módulo:** S12.01 — Segurança: nunca suba seu token de API (1ª aula de Boas Práticas)

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] App-piloto com o trabalho salvo e em dia (nada pendente para commitar), porque o Prompt 0 pergunta "o meu trabalho está salvo e em dia?".

**Confira antes de gravar:**

- [ ] App offline confirmado: o ClinMd-Tribe não usa nenhum token de API quando roda (é a resposta esperada do Prompt 0); o cofre nasce vazio de propósito.
- [ ] Conta-piloto sem nenhuma chave de verdade exposta: o laudo da Seção 4 (itens PROJETO e HISTÓRICO) deve voltar limpo. Confira fora de gravação se nenhum token (GitHub, Claude Code) ficou solto dentro da pasta do projeto ou em algum commit antigo; se ficou, grave a fala alternativa "achou" (notas da Seção 5) e trate como rotação.
- [ ] Chaves reais (Claude Code, GitHub) moram no sistema/usuário, FORA da pasta do projeto: é o que o Prompt 1 vai confirmar; valide a resposta do Claude antes de gravar.
- [ ] NADA de chave ou token na tela: nenhum valor de chave (sk-ant-..., ghp_...), nenhum .env aberto, nenhum comando que ecoe segredo. A regra do Prompt 0 proíbe; confira que o seu ambiente não mostra nada por acidente.

**Navegador:** abra a página de tokens do GitHub (Configuracoes, Developer settings, Personal access tokens) só para mostrar onde fica o botão "Revoke" na Seção 5. NÃO clique em Revoke (quebraria a conexão do repositório) e garanta que nenhuma chave fique visível na tela (conta-piloto sem tokens valiosos, ou captura com o valor tarjado).

---

## SEÇÃO 1: ABERTURA — A CHAVE QUE VALE OURO — 5 min

**Tom:** Reflexivo, retoma o gancho da aula_39 com peso e vira a chave do tema.

**[Aviso rápido dos óculos, antes de mergulhar]**

"Antes de começar: a aula de hoje é sobre uma chave pequenininha que vale ouro, e no terminal ela aparece em letras igualmente pequenininhas. Então faz o favor de aproximar a cadeira, ou pôr os óculos de perto. Hoje a gente não quer que NADA escape do seu campo de visão.

---

"Na aula passada você liberou o seu produto. E no meio da conferência, lembra do item LACRE? A gente procurou por uma chave secreta na sua entrega — e, ainda bem, não achou nenhuma, porque o seu app é offline.

Mas eu te deixei uma promessa. Existe um tipo de chave que vale ouro: o token de API. A senha que dá acesso a um serviço na sua conta, no seu dinheiro.

---

E o perigo dela é real. Todo ano, milhões de chaves dessas escapam sem querer para lugares públicos na internet — e robôs as encontram em minutos. Uma chave esquecida no lugar errado vira uma conta de milhares de dólares numa única madrugada, no SEU cartão.

---

Ontem você aprendeu a procurar a chave na saída. Hoje você aprende a guardá-la na entrada — pra ela nunca, jamais, sair.

E como sempre, você não vai ler uma linha de código. Você vai pedir a proteção, ver ela ficar de pé, e provar que a chave está guardada.

---

Hoje começa uma parte nova do curso. Você já construiu o produto. Agora vêm os hábitos de quem entrega software de verdade — e o primeiro, o mais inegociável, é este: a sua chave nunca vaza."

---

## SEÇÃO 2: A CHAVE DO ARMÁRIO DE CONTROLADOS — 9 min

**Tom:** Didático, tranquilo, sem comando nenhum ainda. Constrói a analogia central inteira antes de tocar no teclado.

"Antes de pedir nada, a maquete mental. E ela é uma coisa que você vive todo dia: a chave do armário de controlados.

Pensa nessa chave. Quem tem ela, abre o armário no seu nome — pega o que quiser de lá, na sua responsabilidade. Um token de API é isso: quem tem a chave, age na sua conta, gasta o seu dinheiro, no seu nome.

---

Agora, como você trata a chave do armário de controlados?

Ela anda separada e presa em você. Nunca fica pendurada no corredor do hospital, à vista de quem passa. E nunca, jamais, viaja junto com o material que você entrega pra enfermaria. O carrinho de medicação vai; a chave fica no seu bolso.

A chave digital é igual. Ela mora separada do código. E nunca viaja na caixa que você entrega.

---

E agora o detalhe mais importante — e você já sabe a resposta, pela sua própria vida.

Imagina que você desconfia que alguém tirou uma cópia da chave do armário de controlados. Você corre atrás da cópia? Pega ela de volta?

Não tem como. Você não sabe quem copiou, nem quantas cópias existem. O que você faz?

Você troca a fechadura. Na hora.

---

Guarda isso, porque é o coração da aula de hoje: chave que vazou não se recolhe. Se troca. Apagar a chave de um papel não desfaz as cópias que já foram tiradas. Trocar a fechadura, sim — no segundo em que você troca, todas as cópias viram lixo.

---

E olha uma coisa: você já tem chaves dessas, na mão, há semanas.

Lembra da aula nove, quando você criou sua conta no GitHub? Naquele momento o GitHub te deu uma chave pra você ser você lá dentro. E o próprio Claude Code, pra funcionar, tem uma chave guardada que prova que é a sua assinatura — você nunca a viu, nunca a digitou em lugar nenhum. E é exatamente assim que tem que ser.

Três palavras pra levar: a chave fica separada do código, não viaja na entrega, e se vazar a gente troca a fechadura. O resto da aula é só você ver isso virar realidade."

---

## SEÇÃO 3: VOCÊ DECIDE — 8 min

**Tom:** Colaborativo, raciocínio clínico, zero código.

"Antes de ver o Claude agir, duas perguntas. Pensa como quem é responsável por uma chave que abre coisas valiosas.

---

**PERGUNTA UM — você percebe que, semanas atrás, colou uma chave secreta dentro de um arquivo do projeto, e o projeto já foi enviado pro GitHub. Você apaga a chave do arquivo e envia de novo. Está resolvido?**

A: Sim. Você apagou a chave e enviou a versão limpa. A chave não está mais lá.

B: Não. Apagar a chave do arquivo de hoje não a apaga do histórico — ela continua guardada nas versões antigas. A chave precisa ser trocada na origem: você vai no site do serviço e revoga aquela chave, gerando uma nova. Só assim a cópia que vazou vira inútil.

C: Não, mas basta deletar o repositório e criar outro. Aí o histórico some junto.

Pensa um segundo.

---

É a B.

A é a armadilha mais perigosa do iniciante — 'apaguei, sumiu'. É falsa pelo mesmo motivo que recolher o papel onde estava a senha não desfaz as cópias que alguém já tirou. O histórico do projeto guarda uma fotografia de cada versão; a versão antiga, com a chave, continua existindo.

C parece esperta mas erra no fundo: deletar o repositório é trabalhoso, nem sempre apaga as cópias que robôs já fizeram, e — o erro principal — não invalida a chave. A chave vazada continua válida no serviço. Você apaga o rastro, mas se a fechadura é a mesma, a cópia ainda abre.

Critério que fica: chave que saiu não se recolhe — se troca na origem.

---

**PERGUNTA DUAS — você vai usar um serviço de IA pago, que te entrega uma chave ligada ao seu cartão. Onde essa chave deve morar?**

A: Dentro do código do programa, junto com o resto — assim o programa sempre acha a chave.

B: Num cofre separado do código — um arquivo que serve só pra guardar chaves, marcado para nunca viajar numa entrega. O programa lê a chave de lá quando precisa, mas a chave nunca anda junto com o código que você compartilha.

C: Num post-it colado no monitor, pra você não esquecer. É só sua, ninguém vê.

Pensa.

---

É a B.

A é o erro clássico e caríssimo: chave dentro do código é chave que viaja com o código. No dia em que você enviar o projeto, fizer um backup, ou pedir ajuda a um colega, a chave vai junto — colada à porta do consultório, à vista de quem passar. É literalmente o que faz milhões de chaves vazarem por ano.

C é falsa privacidade: 'ninguém vê' é ilusão — qualquer pessoa que entra na sua sala, qualquer foto de fundo numa chamada de vídeo, qualquer técnico que mexe na máquina lê o post-it. Chave ligada ao seu cartão num papel exposto é a chave do armário pendurada no corredor.

Critério que fica: a chave mora separada do código, num cofre que não viaja."

---

## SEÇÃO 4: O DRILL — MONTANDO O COFRE AO VIVO — 14 min

**Tom:** Mãos à obra, ritmo de paramentação. O aluno pede a proteção, o Claude monta, e o aluno prova que está protegido lendo um laudo. Nenhum arquivo é aberto.

"Hora do treino. E repara: isto é um drill — o seu app é offline, não usa chave nenhuma hoje. A gente está praticando o ritual de segurança no manequim, antes do paciente real. Quando a chave de verdade chegar, a sua mão já sabe o caminho.

Primeiro, o terreno. Cola:"

[TELA: digitar o Prompt 0 no Claude Code]

```
Você é meu par de programação e, hoje, o meu responsável pela segurança das chaves. A aula
de hoje é sobre como guardar uma chave secreta (um token de API) do jeito certo, pra ela
nunca vazar. Não vamos mudar o app — vamos cuidar de um HÁBITO de segurança.

Confirme em português, SEM saída técnica crua, em uma frase cada: (1) o meu trabalho está
salvo e em dia? (2) este app, o ClinMd-Tribe, é offline e não usa nenhum token de API quando
roda — certo?

NÃO me mostre código nem configuração. E regra valendo para a aula inteira: você NUNCA deve
escrever na tela o conteúdo de uma chave ou token de verdade. Se precisar se referir a alguma,
descreva o tipo dela, jamais o valor.
```

"Repara na última regra do prompt: eu proibi o Claude de mostrar qualquer chave na tela. Numa aula sobre não vazar chave, a primeira coisa é garantir que nenhuma apareça aqui. Chave não se digita, não se cola, nem pra testar.

---

Agora, onde as chaves que você JÁ tem moram hoje. Cola:"

[TELA: digitar o Prompt 1 — onde as chaves moram]

```
Quero entender, em português de leigo, onde as chaves que EU já tenho ficam guardadas hoje —
porque eu uso este computador com você (Claude Code) e com o GitHub, e os dois pediram algum
tipo de chave ou login em algum momento.

Me explique, SEM me mostrar código e sem me mostrar nenhuma chave, em no máximo uma frase cada:
  1. A minha conexão com o Claude Code e com o GitHub guarda essas chaves DENTRO da pasta deste
     projeto, ou fora dela, num lugar do sistema que não viaja quando eu entrego o app?
  2. Por que esse lugar é seguro — por que essas chaves NÃO correm o risco de viajar junto
     quando eu mando o app pro meu colega?
```

"O Claude confirma, e o normal no setup que a gente montou é este: as suas chaves do Claude Code e do GitHub moram no seu sistema, no seu usuário — FORA da pasta do projeto. Por isso elas nunca viajaram nas entregas que você fez. Você já estava seguro, e nem sabia. A chave mora no cofre da casa, não na sala de espera.

---

Agora a parte preventiva: deixar a casa pronta pro dia em que uma chave de verdade chegar. Cola:"

[TELA: digitar o Prompt 2 — a tranca preventiva]

```
Agora a parte preventiva. No futuro, se algum projeto meu PRECISAR usar um token de API, o
lugar certo da chave é um arquivo-cofre chamado .env, que fica fora do código e fora do
repositório. Quero deixar esse hábito pronto neste projeto, como exemplo.

Faça e me explique em português, SEM me mostrar código e SEM escrever nenhuma chave de verdade:
  1. Garanta que existe a regra que mantém o arquivo .env SEMPRE fora do repositório. Se não
     existir, crie; se já existir, só confirme.
  2. Em uma frase, o que essa regra faz: que mesmo que um .env exista um dia, ele nunca viaja
     quando eu enviar ou entregar o projeto.
  3. Em uma frase, a diferença entre 'a chave dentro do cofre' e 'a chave escrita no meio do
     código' — e por que a segunda é o erro que a gente está prevenindo.

NÃO me mostre o conteúdo de nenhum arquivo. Só confirme a tranca e me explique o princípio.
```

"O Claude instala a tranca e explica. Você não abriu arquivo nenhum. Instalou uma fechadura na porta antes mesmo de ter algo de valor na sala — e isso é o certo.

---

E pra fechar, a auditoria. Igual ao laudo da aula passada. Cola:"

[TELA: digitar o Prompt 3 — a auditoria de cofre]

```
Agora faça uma auditoria de segredos e me devolva um LAUDO em português, igual a um exame com
resultado em cada linha: OK (verde), ATENÇÃO (amarelo) ou PARE (vermelho). SEM me mostrar
código, histórico cru ou o conteúdo de qualquer chave.

  1. A TRANCA — a regra que mantém o cofre .env fora do repositório está no lugar?
  2. O PROJETO — vasculhe os arquivos atuais: existe alguma senha, chave ou token escrito solto
     em algum lugar que não devia? (Espero que não — é offline.)
  3. O HISTÓRICO — vasculhe TODO o histórico de versões: alguma chave ficou guardada lá atrás,
     numa versão antiga, mesmo que já tenha sido apagada do arquivo de hoje?

Se NÃO encontrar nada, me diga em uma frase por linha por que está seguro. Se encontrar QUALQUER
chave de verdade: marque PARE, me diga só o TIPO dela (ex.: 'uma chave do GitHub') SEM NUNCA
escrever o valor, e a conduta — NÃO conserte sozinho, NÃO mostre a chave. Veredito de uma linha:
"cofre em ordem, nenhuma chave vazou" ou "atenção — uma chave precisa de conduta".
```

"O laudo volta: tranca no lugar, projeto limpo, histórico limpo. Cofre em ordem, nenhuma chave vazou.

Você leu como leu o hemograma da aula passada — resultado na esquerda, frase do lado. E repara no item do histórico: eu mandei varrer o passado, não só o presente. Porque, se um dia uma chave entrasse e você só apagasse depois, ela continuaria viva lá atrás. 'Não tinha' só vale depois de 'eu procurei'."

---

## SEÇÃO 5: A FECHADURA QUE SE TROCA — ROTAÇÃO — 10 min

**Tom:** O coração conceitual. Desacelera. A defesa final não está no arquivo — está em invalidar a chave.

"E agora a lição mais importante de hoje. A que você tem que sair daqui sabendo de cor.

Voltamos ao armário de controlados. A chave foi copiada. Você troca a fechadura — e a cópia, na mão de quem for, vira um pedaço de metal inútil.

A chave digital tem a mesma fechadura trocável. Cola, e olha o que ele te explica:"

[TELA: digitar o Prompt 4 — a conduta da rotação]

```
Última coisa, e a mais importante de hoje. Quero entender a CONDUTA certa para o dia em que uma
chave minha vazar — por exemplo, se eu sem querer colocar um token num lugar público, ou ele
acabar guardado no histórico de versões.

Me explique em português de leigo, SEM código e SEM mostrar nenhuma chave, com uma analogia do
dia a dia:
  1. Por que apagar a chave do arquivo NÃO basta — por que ela continua "viva" mesmo depois de
     apagada.
  2. Qual é a PRIMEIRA conduta, a que mais importa: revogar (cancelar) a chave velha no painel
     do serviço e gerar uma nova — e o que acontece com a chave velha no instante em que eu a
     revogo.
  3. Por que limpar o histórico é uma conduta SECUNDÁRIA, e não a primeira.

Resuma no fim com uma regra curta pra eu decorar: "se vazou, a primeira coisa é trocar a
fechadura, não esconder a cópia da chave".
```

"O Claude explica e fecha com a regra. Deixa eu traduzir em gesto, porque é simples:

No dia em que você suspeitar que uma chave escapou, você não fica tentando apagar dos arquivos achando que resolveu. Você vai no site do serviço que te deu a chave — o GitHub, ou o que for — e faz duas coisas, nessa ordem: primeiro revoga a chave velha, depois gera uma nova no lugar dela. Naquele segundo em que você revoga, a chave velha morre. Mesmo que alguém tenha a cópia, ela não abre mais nada.

---

E tem um lugar real pra você conhecer o caminho. No GitHub, em Configurações, tem uma página de chaves de acesso — onde você cria, e onde você revoga. Com um clique, sem programar.

[TELA: mostrar a página de tokens do GitHub — só a tela com o botão de revogar, sem expor nenhuma chave]

Olha o botão 'Revoke'. Eu não vou clicar — isso quebraria a conexão do meu repositório. Mas é esse o caminho. No dia que precisar, você sabe onde fica a fechadura.

---

A regra de ouro, devagar: apagar a chave do arquivo é recolher o papel. Revogar a chave no site é trocar a fechadura. Só a segunda te protege de quem já tirou cópia.

E a ordem é clínica: primeiro você estanca a hemorragia — revoga a chave. Depois, se quiser, limpa a sala — e essa faxina do histórico, no dia em que precisar, você pede ao Claude. Fechadura primeiro, faxina depois. Nunca o contrário."

---

## SEÇÃO 6: O QUE ESTE DRILL NÃO É — 5 min

**Tom:** Honesto, desmistificador. Fecha buracos, impede falsa sensação de segurança.

"Três honestidades pra fechar bem.

Primeira: o ClinMd-Tribe não usa nenhuma chave hoje — ele é offline. Então por que treinar? Pelo mesmo motivo que você pratica entubação no manequim antes do paciente real. Quando a chave de verdade chegar, a sua mão já sabe o caminho, e você não improvisa com algo que vale o seu cartão de crédito.

---

Segunda: o cofre que a gente preparou está vazio, de propósito. Isso é o certo. Cofre não nasce com a chave dentro — a chave entra no dia em que existir, por uma porta que nunca apareceu nesta aula.

---

Terceira: guardar a chave no cofre certo não te torna invulnerável a tudo. Te protege do erro mais comum e mais caro — o token vazado no público. Os outros cuidados de sempre — senha forte, não compartilhar login — continuam valendo, como na vida."

---

## SEÇÃO 7: ENCERRAMENTO — A CASA ARRUMADA POR DENTRO — 4 min

**Tom:** Síntese pelo aluno, LGPD como elo, ponte para a aula_41.

"Diz na sua cabeça o que você fez hoje.

Você entendeu que um token é a chave do seu armário de controlados. Viu que as chaves que você já tem moram no sistema, fora do projeto — seguras. Instalou um cofre, preventivo, e provou com um laudo que ele não viaja. E aprendeu a conduta que salva: se uma chave vazar, você troca a fechadura no site, não corre atrás da cópia. Sem ler uma linha de código.

---

E a privacidade, que é o eixo do curso, ganhou hoje uma camada nova.

Uma chave de API é a porta de um serviço. Um token que vaza não é só a sua conta e o seu dinheiro em risco — é uma porta aberta. Proteger a credencial não é um detalhe técnico separado da privacidade: é parte de proteger o paciente. Quem cuida das chaves cuida de quem confia na gente. É o mesmo voto que você faz quando tranca o armário de controlados.

---

Hoje você guardou a chave do lado de fora do código — separada, no lugar dela. Isso é um caso de uma ideia maior, que é a próxima aula: cada coisa tem o seu cômodo.

A chave tem o cofre dela. E o programa, por dentro, também precisa de cômodos separados. Quando um app cresce e tudo fica amontoado numa sala só, vira o que a gente chama de monolito — uma bagunça onde você mexe numa coisa e quebra outra do outro lado, sem entender por quê.

Você já viu o começo disso quando construiu o ClinMd-Tribe em quatro camadas. Na próxima, a gente volta pra esse mapa com olhos de quem já entrega: como manter a casa organizada por dentro pra ela nunca virar um amontoado perigoso.

Hoje você guardou a chave. Na próxima, a gente arruma a casa. Até lá."

---

**FIM DO ROTEIRO**

---

> **NOTAS DE PRODUÇÃO (não falar — operacional):**
>
> - **Anti-padrão PROIBIDO (CRÍTICO):** NUNCA mostrar na tela `ANTHROPIC_API_KEY=...`, qualquer string `sk-ant-...`/`ghp_...`, `os.getenv`, `load_dotenv`, `git log -p`, `cat .env`, `echo ... >> .env`, `env`/`printenv`. O aluno NUNCA abre o `.env` nem o `.gitignore` — vê só o comportamento (laudo em português) e o gesto web (botão Revoke). A versão legada (`aulas/avancado/.../aula_01_seguranca_tokens/`) usa esse código lido — é o anti-padrão a substituir.
> - **ZERO comando de terminal digitado pelo aluno (decisão de segurança):** diferente das aulas 38/39, aqui o aluno só conversa com o Claude (prompts) e, opcionalmente, VÊ uma página web. Isso elimina a chance de ele colar um comando que ecoe uma chave. O Claude executa git/arquivo internamente e relata em prosa.
> - **App offline = cofre vazio de propósito:** ClinMd-Tribe não usa token em runtime. A aula é DRILL preventivo + hábito, ancorado nos 2 tokens reais (GitHub aula_09 + auth Claude Code). NÃO inventar chave falsa para drama (regra da aula_39). Se a conta-piloto tiver, por acaso, um token real num commit antigo, o laudo (item HISTÓRICO) vira ouro → emendar na Seção 5 (rotação). Gravar fala pronta nos 2 cenários (limpo / achou).
> - **Estatística da Seção 1:** "milhões de chaves vazam/ano" — confirmar número atual antes de gravar (GitGuardian State of Secrets Sprawl: ~23,8 mi de novos segredos expostos no GitHub público em 2024; GitHub Secret Scanning, ano corrente) e citar com fonte na tela. Não usar número desatualizado.
> - **Fala da Seção 4 (Prompt 1) assume a resposta padrão:** a narração "O Claude confirma..." pressupõe o setup normal montado no curso (chaves do Claude Code e do GitHub no sistema/usuário, FORA da pasta do projeto). Conferir na conta-piloto que a resposta do Claude bate com isso antes de gravar. Se algum setup atípico tiver guardado credencial dentro do projeto, regravar a fala e tratar o caso na auditoria (Prompt 3) e na rotação (Seção 5).
> - **Demonstração web (Seção 5):** GitHub → Settings → Developer settings → Personal access tokens — mostrar só a tela com o botão "Revoke", SEM expor nenhuma chave (conta-piloto sem tokens valiosos, ou screenshot tarjado). O aluno NÃO clica em Revoke (quebraria o repo) — só vê onde fica.
> - **Âncoras de continuidade:** GitHub token = aula_09 (o aluno criou); Clean Architecture/4 camadas/plantão = aula_15 (gancho aula_41). Referenciar como "você já fez/viu".
> - **Bordão a gravar com ênfase:** "Se a chave vazou, a primeira coisa é trocar a fechadura — não esconder a cópia da chave."
> - **Tom de abertura de módulo:** 1ª de S12 ("agora são hábitos de quem entrega"); abre porta nova, não fecha arco. Não repetir o peso de fechamento da aula_39.
> - **Armadilha bash:** zero `uv run python -c` (e zero comando de terminal do aluno, ver acima).
