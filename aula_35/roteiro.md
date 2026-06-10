# Aula 35 — O Guardião que Acorda Sozinho: o Controle que Roda a Cada Entrega

**Formato:** Gravada em um take no OBS Studio
**Duração:** ~55 min
**Tom:** Clínico-arquiteto; o alívio de não depender mais da própria memória, e o impacto de ver o robô pegar o erro sozinho, longe do paciente
**Módulo:** S10.01 — Integração Contínua (CI) com GitHub Actions

---

## SEÇÃO 1: ABERTURA — O CONTROLE QUE AINDA PRECISA DE VOCÊ — 5 min

**Tom:** Reflexivo. Retoma literalmente o gancho da aula_34 e nomeia o problema humano.

"Nas últimas duas aulas você construiu os guardiões. O da calculadora, o do checklist, o da busca. Pequenas testemunhas automáticas que conferem, em meio segundo, se as regras que importam continuam de pé.

E no fim da aula passada eu te deixei com um incômodo. Lembra?

Esses guardiões só protegem se forem acordados. Você precisa LEMBRAR de rodar o controle. Digitar o comando, toda vez que mexer no app.

---

E se você esquecer?

Pensa numa sexta à noite. Você está cansado. Faz uma mudancinha rápida no app — 'só um ajuste, é pequeno'. Não roda o controle. Sobe assim mesmo.

E aquela mudancinha quebrou a regra do AVC prévio sem você ver.

O guardião existia. Estava lá, pronto. Mas dormindo. Ninguém o acordou.

---

Hoje a gente resolve isso de vez.

Hoje você vai fazer o que todo laboratório de verdade já faz: o controle deixa de depender de alguém lembrar. Ele passa a rodar **sozinho**.

Um guardião que acorda por conta própria — toda vez que você entrega uma mudança. Você nunca mais vai precisar lembrar. Porque ele não esquece."

---

## SEÇÃO 2: O CONTROLE QUE LIGA SOZINHO — 7 min

**Tom:** Didático, tranquilo. A maquete mental antes de qualquer comando.

"Volta comigo pro laboratório, que é onde essa ideia já vive.

Toda manhã, antes do primeiro exame de paciente sair, a máquina roda a amostra-controle. Sozinha. Ninguém chega às seis da manhã e aperta um botão de 'rodar controle'. Está programado: deu o horário, a máquina roda. Se o controle bate, libera o dia. Se não bate, trava tudo.

O controle não espera o técnico lembrar. Ele tem um gatilho automático: o relógio.

---

O seu app vai ganhar exatamente isso. Um controle com gatilho automático.

Só que o gatilho não vai ser o relógio. Vai ser a **entrega**.

Toda vez que você entrega uma mudança — toda vez que você faz aquele `git push` que você já conhece desde a aula nove — esse ato, sozinho, dispara o controle. Você não aperta o botão do controle. O ato de entregar aperta por você.

É a mesma lógica da prescrição eletrônica que checa a interação medicamentosa antes de você assinar: ninguém pediu a checagem, ela acontece sozinha, no caminho. O robô é isso para o seu código.

---

E tem uma diferença linda em relação às aulas passadas.

Antes, o controle rodava na sua máquina. Agora ele vai rodar **lá no servidor**, no GitHub, longe da sua máquina. Você entrega o código, e um robô do GitHub — não você — pega esse código, roda todos os guardiões, e mostra o resultado: verde ou vermelho.

Você pode até desligar o computador. O robô roda mesmo assim, no servidor. O controle não está mais preso à sua memória, nem à sua máquina.

---

Esse robô tem um nome técnico: integração contínua. Em inglês, CI. Mas esquece a sigla. Lembra do controle da manhã que roda sozinho. É isso, do começo ao fim."

---

## SEÇÃO 3: VOCÊ DECIDE — 9 min

**Tom:** Colaborativo. Duas perguntas, raciocínio clínico, zero código.

"Duas perguntas antes de a gente ligar o robô. Pensa como médico.

---

**PERGUNTA UM — por que botar um robô pra rodar os testes, se você já roda na sua máquina?**

Você já tem o hábito de rodar o controle antes de entregar. Então qual é a real vantagem de um robô fazer de novo, no servidor?

A: porque o robô roda mais rápido que a sua máquina.

B: porque você, humano, esquece. O robô não. Ele roda SEMPRE, a cada entrega, mesmo na sexta à noite, mesmo cansado, mesmo quando você decidiu pular o controle 'só dessa vez'.

C: porque o robô roda testes melhores que os seus.

Pensa um segundo.

---

É a B.

Não é sobre velocidade — A está errado, a sua máquina até roda mais rápido. Não é sobre qualidade — C está errado, são exatamente os mesmos guardiões, os seus.

É sobre uma fraqueza humana que você conhece bem: a gente esquece. A gente pula etapa quando está cansado. A gente confia que 'dessa vez não precisa'.

O robô não tem sexta à noite. Não tem cansaço. Não tem 'só dessa vez'. Ele roda o controle em toda entrega, sem falta. É a rede embaixo do trapezista — você espera nunca precisar, mas é ela que te deixa trabalhar tranquilo.

Critério que fica: o robô não substitui você rodar o controle. Ele garante que o controle SEMPRE roda, mesmo nas vezes em que você não rodaria.

---

**PERGUNTA DOIS — o robô ficou vermelho numa entrega. O que isso significa?**

Você entregou uma mudança, o robô rodou, e ficou vermelho. Como você deve tratar isso?

A: nada demais, é só um aviso, pode seguir em frente e consertar depois.

B: que aquela entrega tem uma regra quebrada e não deveria ser usada — nem publicada, nem mostrada a ninguém — até você consertar. O vermelho é um portão fechado.

Pensa.

---

É a B.

Vermelho não é um aviso decorativo. É um portão fechado. Significa: tem uma regra clínica quebrada nessa versão do app. Se o AVC prévio está valendo um ponto em vez de dois, essa versão subtrata paciente — e ela não pode ser usada até voltar pro verde.

Tratar o vermelho como 'depois eu vejo' é o mesmo que liberar exames com o controle da manhã alterado. Ninguém faz isso. Você trava, conserta, e só então segue.

Critério que fica: verde é 'pode seguir'. Vermelho é 'pare e conserte antes de qualquer coisa'. Guarda isso — na próxima aula a gente vai transformar esse portão num porteiro de verdade."

---

## SEÇÃO 4: PEDINDO O ROBÔ — 11 min

**Tom:** Mãos à obra. Dois prompts: um blinda o terreno, o outro cria o robô.

"Antes de criar o robô, deixa o Claude conferir que o terreno está limpo. Eu quero ter certeza de duas coisas: que o meu projeto está mesmo conectado ao GitHub, e — mais importante — que nenhum dado de paciente sobe junto.

Cola este primeiro prompt:"

[TELA: digitar o Prompt 0 no Claude Code]

```
Você é meu par de programação. Antes de eu criar o robô de testes automáticos,
confira o estado do meu Git e me diga, em português e SEM me mostrar saída técnica
crua, apenas:
  1. se este projeto já está conectado ao meu repositório no GitHub (o clinmd-tribe
     que eu criei lá atrás) e se o meu último commit já foi enviado (push);
  2. se a pasta data/ — onde ficam o banco do app, os artigos e o banco vetorial —
     está protegida pelo .gitignore e portanto NUNCA é enviada para o GitHub. Eu não
     quero dado de paciente nem banco nenhum saindo da minha máquina.

Se algo estiver faltando (não conectado, push pendente, ou data/ desprotegida),
conserte você mesmo e confirme em uma frase que está tudo certo. NÃO me mostre
código nem arquivos de configuração.
```

"O Claude confere e responde em português: está conectado, o push está em dia, e — repara nisso — a pasta `data/` está protegida. O banco com os horários das suas cirurgias, os artigos, o banco vetorial: nada disso sobe. Só o código do app e os controles, aqueles pacientes fictícios. O paciente não viaja. Esse é o nosso eixo, e o Claude acabou de confirmar pra você, em voz alta.

---

Terreno limpo. Agora eu peço o robô. Repara no formato: eu descrevo, em português, o que o robô faz. Eu não escrevo robô nenhum, não escrevo configuração nenhuma. Cola:"

[TELA: digitar o Prompt 1 no Claude Code]

```
Agora crie o robô de integração contínua (CI) deste projeto no GitHub, usando
GitHub Actions. O objetivo, em uma frase: toda vez que eu enviar uma mudança
(git push), um robô do GitHub instala as dependências do projeto com uv e roda os
meus testes automaticamente, mostrando verde se passarem ou vermelho se algum falhar.

Requisitos:
  - O robô roda os mesmos testes que eu rodo na minha máquina com: uv run pytest
  - Por enquanto, rode apenas os testes da calculadora e do checklist. Deixe os
    testes da busca/RAG de fora deste primeiro robô — eles baixam um modelo grande,
    e a gente liga isso numa próxima aula. Se precisar, marque os testes da busca
    com uma etiqueta para o robô conseguir pulá-los de forma limpa.
  - Deve disparar a cada push na branch main e também quando eu pedir manualmente
    pelo site do GitHub.
  - Use uma versão de Python compatível com a do meu projeto e instale tudo com uv,
    do mesmo jeito que funciona aqui na máquina.
  - O robô não precisa de nenhum dado meu: roda só o código e os testes com
    pacientes fictícios. Ele nunca acessa a pasta data/.

Coloque o arquivo do robô no lugar certo do projeto. NÃO me mostre o conteúdo do
arquivo — eu não preciso ler. Quando terminar, me diga em português: (1) que o robô
está pronto; (2) exatamente quais comandos git eu rodo para enviá-lo ao GitHub;
(3) onde no site do GitHub eu vou ver a bolinha do robô trabalhando.
```

"O Claude cria o arquivo do robô — num cantinho do projeto que você nunca vai precisar abrir — e te explica em português o que fazer. O robô está pronto na sua máquina. Mas ele só ganha vida quando você ENTREGA. É o que a gente faz na próxima seção."

---

## SEÇÃO 5: A PRIMEIRA ENTREGA VERDE — 11 min

**Tom:** O payoff. O robô ganha vida na frente do aluno.

"Hora de entregar o robô e vê-lo trabalhar pela primeira vez. Os comandos que o Claude te deu são estes — os mesmos `add`, `commit`, `push` que você já conhece desde a aula nove:"

[TELA: no terminal]

```bash
git add .
git commit -m "feat: adiciona robô de CI que roda os guardiões a cada push"
git push
```

"Enter. O código subiu. Agora abre o navegador, vai no seu repositório `clinmd-tribe` no GitHub, e clica na aba lá em cima escrita **Actions**.

---

Olha o que aparece.

Uma linha, com a mensagem da sua entrega, e do lado uma **bolinha amarela girando**. Essa bolinha é o robô trabalhando. Ele pegou a sua entrega logo depois do push, e começou a rodar.

Clica na linha. Você vê as etapas, uma a uma, virando verdes: instalar as ferramentas, instalar as dependências, rodar os guardiões.

E no topo, a bolinha vira um **✓ verde**.

---

Para um segundo nisso.

Verde. O robô rodou os guardiões da calculadora e do checklist — sozinho, no servidor — e todos passaram.

E olha o que você NÃO fez: você não digitou `pytest`. Você não rodou nada. Você só entregou. O robô fez o resto, no servidor do GitHub, no exato instante em que você deu push.

Aquele incômodo da abertura — 'e se eu esquecer de rodar o controle?' — acabou de morrer. Você não precisa mais lembrar. O robô lembra por você.

---

E não é uma vez só. É pra sempre, a cada entrega.

Deixa eu provar. Vou pedir uma mudança boba pro Claude — só um ajuste de texto, nada que quebre regra — e entregar de novo."

[TELA: após a mudança trivial]

```bash
git add .
git commit -m "chore: pequeno ajuste de texto"
git push
```

"Volta na aba Actions. Olha: uma nova bolinha amarela, girando, já apareceu. Sozinha. Eu não pedi. O ato de entregar acordou o robô de novo. Vira verde.

Isso agora faz parte de respirar. Toda entrega, o controle roda. Sem você lembrar.

E se um dia você quiser rodar o controle sem entregar nada — só pra conferir — tem um botão 'Run workflow' ali mesmo na aba Actions. Mas no dia a dia você nem precisa: o push já faz por você."

---

## SEÇÃO 6: O CLÍMAX — A SABOTAGEM QUE FICA VERMELHA SOZINHA — 9 min

**Tom:** O ápice. Desacelera. O robô pega o erro sozinho, no servidor, longe do paciente.

"Até agora foi tudo verde. Lindo. Mas o robô só vale alguma coisa se ele pegar o erro quando ele acontece. Então vamos fazer um erro acontecer.

Vou pedir ao Claude pra quebrar uma regra de propósito. A mesma da aula dos testes: o AVC prévio valendo um ponto em vez de dois. O erro que subtrata paciente.

E presta atenção no que eu vou pedir junto: **não rode nada na minha máquina**. Eu não quero conferir aqui. Eu quero ver o robô do GitHub pegar sozinho."

[TELA: digitar o Prompt da sabotagem]

```
Quero mostrar o robô trabalhando quando algo dá errado. De propósito, introduza no
serviço da calculadora CHA2DS2-VASc o erro mais comum: faça o AVC prévio valer 1
ponto em vez de 2. NÃO mexa nos testes — só na regra. Não rode nada na minha
máquina. Eu quero ver o robô do GitHub pegar o erro sozinho.
```

"Pronto. O app está quebrado agora. Silenciosamente quebrado. Se eu não tivesse robô nenhum, eu entregaria isso numa sexta à noite e nem perceberia.

Vou entregar:"

[TELA: no terminal]

```bash
git add .
git commit -m "test: quebra a regra do AVC de propósito para validar o robô"
git push
```

"Entrega feita. Agora abre a aba Actions, e olha.

Bolinha amarela girando... e vira **✗ vermelho**.

---

[pausa]

Vermelho. No servidor.

Eu não rodei nada aqui na minha máquina. Não digitei `pytest`, não conferi nada. Eu só entreguei o código quebrado — e o robô, lá no GitHub, rodou os guardiões sozinho, logo que recebeu a entrega, e pegou.

Clica no vermelho. Ele te mostra exatamente qual guardião falhou: o do AVC prévio — aquela regra que você conhece de cor: AVC ou AIT prévio pesa dois pontos no escore, não um. É a letra que dobra. Com um ponto, o paciente cai abaixo do corte e fica sem anticoagular. O guardião esperava dois, recebeu um. O robô aponta o dedo na regra que quebrou — e eu não li uma linha de código pra saber disso.

---

Pensa no que isso significa. Numa sexta à noite, cansado, eu subi um app que subtrata paciente. E em vez de isso chegar num paciente, chegou num robô — que travou, pintou de vermelho, registrou exatamente o que está errado. De graça. Em segundos. Longe de qualquer pessoa de verdade.

Esse é o guardião que não dorme E não depende da sua memória. Agora eu conserto."

[TELA: digitar o Prompt do conserto]

```
Perfeito, o robô pegou o erro. Agora conserte: o AVC prévio tem que voltar a valer
2 pontos. Depois confirme que está corrigido. Eu vou enviar de novo e quero ver o
robô ficar verde.
```

[TELA: no terminal]

```bash
git add .
git commit -m "fix: AVC prévio volta a valer 2 pontos"
git push
```

"Entrega. Aba Actions. Nova bolinha, gira... **✓ verde**.

Recalibrado, e o servidor confirma. O ciclo inteiro: estava verde, alguém quebrou, o robô gritou vermelho na hora — sozinho, no servidor — consertou, verde de novo. E em nenhum momento você precisou lembrar de rodar nada."

---

## SEÇÃO 7: ENCERRAMENTO — O ROBÔ AVISA, MAS AINDA NÃO BLOQUEIA — 3 min

**Tom:** Síntese pelo aluno, LGPD orgânico, e abre a tensão da próxima aula.

"Recapitula — você dizendo, na sua cabeça.

Você criou um robô que roda os guardiões sozinho, no servidor, toda vez que você entrega. Viu ele ficar verde quando o app está são. Quebrou uma regra de propósito e viu ele ficar vermelho sozinho, longe de qualquer paciente, apontando exatamente o erro. E fez tudo isso sem ler uma linha de código ou de configuração. Você leu bolinhas: verde, vermelho.

---

E a privacidade, que é o eixo de tudo.

Lembra que, antes de criar o robô, o Claude confirmou pra você que a pasta `data/` está trancada? Isso não foi detalhe. O que subiu pro GitHub foi a receita do app e os controles fictícios — a calculadora, o checklist, os pacientes de mentira dos testes. O banco com as suas cirurgias de verdade, os seus artigos, o prontuário: nada disso saiu da sua máquina. O robô roda no servidor, mas ele nunca toca no que é sensível. O paciente não viaja — nem quando o código viaja.

---

Agora, um detalhe que vai te incomodar — de propósito.

O robô hoje AVISA. Verde ou vermelho. Mas repara: quando ele ficou vermelho, eu ainda CONSEGUI entregar o código quebrado. Ele não me impediu. Ele só pintou de vermelho e me deixou seguir, se eu quisesse ignorar.

E se o robô pudesse fazer mais? E se ele virasse um porteiro de verdade — que não deixa código quebrado passar, que tranca a porta até estar tudo verde?

É isso que vem na próxima aula. O robô deixa de ser um aviso e vira um portão que não abre no vermelho.

Até lá."

---

**FIM DO ROTEIRO**

---

> **NOTAS DE PRODUÇÃO (não falar — operacional):**
>
> - **GitHub Actions é habilitado por padrão** em repositórios — basta o `.github/workflows/ci.yml` existir e dar push; não precisa "ligar" em Settings. Confirmar na pré-gravação que a aba Actions aparece e executa.
> - **Cota de Actions:** repo privado consome minutos da cota gratuita. Confirmar saldo na conta de gravação; se necessário, gravar com a conta-piloto do Dr. Petrus num `clinmd-tribe-demo`.
> - **Escopo determinístico:** o Prompt 1 exclui os testes do RAG (modelo `sentence-transformers` ~90MB → risco de lentidão/timeout no runner ao vivo). O RAG entra no CI na aula_36.
> - **Isolamento RAG (pré-condição do CI verde):** confirmar na pré-gravação COMO o pipeline separa calculadora+checklist do RAG — por caminho (`tests/test_calculadora.py tests/test_checklist.py`), por marcador (`-m "not rag"`), ou por nome. Se não houver mecanismo limpo, instruir o Claude a criar um marcador `@pytest.mark.rag` nos testes da busca ANTES de configurar o robô. Sem isso, o runner pode baixar o modelo de 90MB e estourar timeout ao vivo.
> - **Upstream do push:** confirmar que `git push` simples funciona (upstream `origin/main` já setado pelo `-u` da aula_09); se não, rodar `git push -u origin main` uma vez antes de gravar.
> - **Latência da run (estado "Queued"):** após o push, a run pode aparecer como "Queued" (relógio) por alguns segundos antes da bolinha amarela "in progress". Narrar o beat ("o robô recebeu, está entrando na fila") em vez de afirmar surgimento instantâneo; cortar a espera na edição se for longa.
> - **Sabotagem reversível:** working tree limpo/commitado antes do clímax; a sabotagem é um commit real que vai ao remote (ok, é didático); o conserto restaura. Não encerrar com o app quebrado.
> - **Nomes/aparência reais:** ajustar as falas que citam contagem de testes e a aparência da aba Actions ao que aparecer na pré-gravação (label exato, ordem das etapas).
> - **Autenticação:** o aluno usa o git já autenticado da aula_09 (token/credencial guardada); nenhuma chave é colada em arquivo — gancho para S12.01 ("nunca suba seu token").
