# Aula 38 — Da Bancada pra Prateleira: o App que Anda Sozinho

**Formato:** Gravada em um take no OBS Studio
**Duração:** ~58 min
**Tom:** Do orgulho de construir ao orgulho de entregar. "Você não é mais só quem usa software — é quem entrega software." Honesto sobre os limites (é grande, o antivírus cheira), encantado com o resultado (dois cliques, na mão de qualquer um).
**Módulo:** S11.02 — Empacotar o app como .exe de Windows (flet pack)

---

## SEÇÃO 1: ABERTURA — A FÓRMULA NA BANCADA — 5 min

**Tom:** Reflexivo. Retoma o gancho da aula_37 e nomeia o desconforto: o app lindo está preso.

"Na aula passada você passou o ferro no jaleco do app. Paleta da TribeMD, fonte Inter, ícones, tudo respirando. Por dentro é à prova de bala, por fora tem a cara disso. E aí eu te deixei com uma farpa no fim. Lembra?

Esse app maravilhoso só abre de um jeito: você, abrindo o terminal, digitando `uv run flet run main.py`. Pra você, que fez o curso inteiro, isso é trivial. Mas pensa no seu colega cardiologista, da sala ao lado — o que não sabe o que é um terminal, exatamente como você não sabia na aula um.

Como é que ELE abre o seu app?

---

Hoje, ele não abre.

O seu app é uma fórmula manipulada: poderosíssima, mas só funciona na sua bancada, com você do lado, sob a sua receita — aquele comando no terminal. Na farmácia de manipulação, o paciente não entra e se serve.

---

Hoje a gente faz o que a indústria faz: pega a sua fórmula e transforma ela no remédio de prateleira. Mesma molécula por dentro. Mas numa caixa que qualquer médico pega e usa, sem você, sem terminal, sem receita. Dois cliques.

E, como sempre, você não vai escrever nem ler uma linha de código. Você vai pedir. E ver a caixa nascer."

---

## SEÇÃO 2: O REMÉDIO DE PRATELEIRA — O CONCEITO — 8 min

**Tom:** Didático, tranquilo. A maquete mental de "empacotar = tornar independente" antes de qualquer comando.

"Antes de pedir nada, a ideia que faz isso funcionar — e ela é linda de simples.

Pensa em como o app abre hoje. Pra rodar, precisa de: ter o Python instalado, ter o uv instalado, ter os arquivos do projeto na máquina, abrir o terminal, e digitar o comando exato. Cinco pré-condições. Isso é a sua bancada de manipulação: tudo precisa estar ali, e você precisa saber o feitiço.

---

Agora imagina o oposto. Um único arquivo: `ClinMd-Tribe.exe`. Clica. Abre. Fim.

Zero pré-condição. O colega não tem Python? Não importa. Não sabe o que é terminal? Não importa. Nunca ouviu falar de Claude? Não importa. A caixa traz tudo dentro.

---

Empacotar é isso: pegar tudo que o app precisa pra viver — o Python, as peças, as suas telas — e selar dentro de uma caixa só. Antes, o app dependia da sua bancada. Depois, anda com as próprias pernas.

A palavra técnica é 'independente'. Esquece a palavra. Lembra do remédio que anda sozinho na bolsa do médico, longe da farmácia.

---

Agora, três verdades honestas sobre o remédio de prateleira — porque ele não é mágica, e é melhor você saber antes:

Primeira: ele tem a embalagem do Windows. Quem usa Windows abre e usa. Quem usa Mac precisaria de outra caixa — mesma fórmula, embalagem diferente. Como a sua turma é quase toda Windows, a gente faz a do Windows hoje.

Segunda: a caixa é maior que o pozinho da fórmula, porque vem com tudo dentro — inclusive o Python inteiro. Caixa cheia é caixa pesada. É o preço de não depender de nada lá fora.

Terceira: quando o seu colega abrir uma caixa nova, o Windows pode parar e cheirar. Não porque tem veneno — porque é novo e ele não te conhece ainda. Eu te mostro como liberar, sem desarmar a segurança dele.

Guarda a imagem: hoje, fórmula na bancada; no fim da aula, remédio na caixa."

---

## SEÇÃO 3: VOCÊ DECIDE — 8 min

**Tom:** Colaborativo. Duas perguntas, raciocínio clínico, zero código.

"Antes de pedir a caixa pro Claude, duas perguntas. Pensa como quem decide se um remédio está pronto pra sair da farmácia e ir pra prateleira.

---

**PERGUNTA UM — por que o seu colega consegue abrir o programa mesmo sem ter Python, terminal ou Claude na máquina dele?**

A: porque o Windows dele baixa o Python sozinho na hora de abrir.

B: porque o programa é uma caixa que já traz tudo que o app precisa lacrado dentro — o Python, as peças, as telas. Nada precisa estar na máquina do colega.

C: porque o app na verdade roda na SUA máquina pela internet, e o colega só vê a tela de longe.

Pensa um segundo.

---

É a B — e essa é a ideia inteira da aula numa frase.

A está errado e é perigoso de acreditar: o Windows não sai baixando Python sozinho; se o app dependesse disso, ele falharia na máquina do colega. C está MUITO errado, e repara por que isso importa pra você: se o app rodasse na sua máquina pela internet, o dado do paciente do colega viajaria até você — e isso seria uma violação de privacidade gravíssima. Não é isso. O programa roda cem por cento na máquina do colega, sozinho, offline.

Critério que fica: empacotar é tornar independente. A caixa não pede nada emprestado da máquina de quem recebe, e não conversa com ninguém pela rede. É essa independência que deixa você entregar o app pra qualquer um — e que mantém o dado de cada médico trancado na máquina dele.

---

**PERGUNTA DUAS — quando o colega clicar no programa novo e o Windows mostrar 'aplicativo não reconhecido', qual é a atitude certa?**

A: pedir pro colega desligar o antivírus do computador inteiro, abrir o app, e deixar desligado.

B: entender que é o Windows desconfiando de uma caixa nova que ele ainda não conhece — e usar o 'Mais informações' e 'Executar assim mesmo' pra liberar APENAS aquele app, mantendo todo o resto da segurança ligado.

C: concluir que o app está com vírus e jogar fora.

Pensa.

---

É a B.

A é o erro clássico, e é grave: desligar o antivírus inteiro pra abrir um programa é como desarmar o hospital inteiro pra deixar uma única caixa entrar. Você nunca faz isso, e nunca pede pro seu colega fazer. C também está errado e joga fora um app perfeitamente seguro — é como descartar um remédio bom porque o fiscal parou pra cheirar.

O certo é a B: o fiscal cheirou porque a caixa é nova e ele não te conhece ainda, não porque tem veneno dentro. Você libera só AQUELA caixa, AQUELA vez, e deixa o fiscal de guarda pra todo o resto.

Critério que fica: segurança não se desliga, se calibra. Você nunca compra autonomia desarmando a proteção de quem usa. Libera o específico, mantém o geral."

---

## SEÇÃO 4: SELANDO A CAIXA — O PRIMEIRO PACK — 11 min

**Tom:** Mãos à obra. Ritual de terreno limpo, decisão honesta do que vai dentro, e o pedido de empacotamento.

"Hora de montar a caixa. E como sempre, antes de mexer, o ritual: conferir que o terreno está limpo e que nada de paciente entra na caixa. Cola:"

[TELA: digitar o Prompt 0 no Claude Code]

```
Você é meu par de programação. Hoje eu quero transformar o meu app ClinMd-Tribe
(feito em Flet) num programa de Windows — um arquivo .exe — que abre com dois cliques,
sem terminal e sem Python instalado, pra eu entregar na mão de um colega médico.

Antes de tudo, confira o terreno e me responda em português, SEM saída técnica crua:
  1. Eu estou num computador Windows? (Gerar .exe só funciona no Windows — se eu
     estiver em Mac ou Linux, me avise e me diga meu caminho.)
  2. O meu trabalho está salvo (git em dia)?
  3. A pasta data/ continua protegida pelo .gitignore? Banco, artigos e qualquer dado
     de paciente NÃO podem entrar no programa que eu vou distribuir.

Se algo estiver pendente, conserte e confirme em uma frase. NÃO me mostre código nem
configuração.
```

"Terreno confirmado, `data/` trancada. Agora, uma decisão honesta antes de empacotar: o que vai dentro da caixa.

O seu app tem uma parte pesada — a busca inteligente, o RAG, com aquele cérebro de leitura de uns noventa megas e bibliotecas grandes. Embrulhar isso numa caixa de distribuição deixa o pacote enorme e frágil. Então a gente faz o que um bom produto faz: a versão de bolso, pro colega, leva o que ele mais usa no plantão — as calculadoras, o checklist cirúrgico, o painel. A busca inteligente continua sua, no seu ambiente completo, mas fica de fora desta caixa que viaja. Menos é mais quando o objetivo é caber na mão de qualquer um.

Cola o pedido:"

[TELA: digitar o Prompt 1 — o empacotamento]

```
Agora empacote o meu app ClinMd-Tribe como um programa de Windows (.exe), usando o
flet pack, para qualquer médico abrir com dois cliques, sem Python e sem terminal.

O escopo do que vai dentro:
  - Inclua as partes leves e mais usadas: as calculadoras médicas, o checklist
    cirúrgico e o painel/dashboard.
  - NÃO inclua a busca inteligente (o RAG): ela depende de um modelo pesado de uns
    90 MB e de bibliotecas grandes que tornam o pacote enorme e frágil. Deixe a busca
    de fora desta versão de distribuição — ela continua existindo para mim no ambiente
    completo, mas não vai nesta caixa de bolso.
  - Dê ao programa o nome "ClinMd-Tribe" e o ícone clínico da identidade visual.
  - NENHUM dado de paciente no pacote: a pasta data/ NÃO pode ser embrulhada junto.
    O colega recebe o app limpo e começa do zero.

Garanta que as bibliotecas pesadas da busca (torch, sentence-transformers, chromadb)
NÃO entrem no pacote — nem por import indireto. Se o ponto de entrada atual importa a
busca, crie um ponto de entrada de distribuição que não a importe e empacote esse.
Confira o tamanho do .exe no fim: se passar de uns 300 MB, alguma biblioteca pesada
vazou — investigue e corrija antes de me entregar.

Cuide você mesmo de toda a parte de empacotamento (dependências, exclusão da busca,
assets), sem me mostrar arquivo nenhum. Quando terminar, me diga em português: (1) que
o app está empacotado, e o que ficou dentro (calculadoras, checklist, painel) e fora
(a busca); (2) o comando exato que eu rodo para gerar e quanto costuma demorar; (3)
onde o arquivo .exe vai aparecer e o tamanho dele.
```

"O Claude prepara tudo e te dá o comando pra rodar. É um comando só. Vai ser parecido com este, mas mais comprido — o Claude acrescenta os detalhes do ícone e o que fica de fora. Você não decora nada: cola exatamente o que o Claude te deu:"

[TELA: no terminal — o comando que o Claude forneceu, na forma simplificada]

```bash
flet pack main.py --name ClinMd-Tribe
```

"Dá enter. E aí vem a paciência: empacotar demora. A tela vai cuspir um monte de texto correndo — não precisa ler nada, é a caixa sendo montada peça por peça. Pode levar alguns minutos. Espera ele terminar e dizer 'pronto', ou apontar um erro.

E se der erro na primeira vez — e pode dar — não entra em pânico. O jeito de resolver é o de sempre: você copia a última parte do que apareceu na tela e cola no Claude com este pedido:"

[TELA: digitar o Prompt 2 — só se der erro]

```
O empacotamento deu erro. Vou colar a última parte do que apareceu na tela. Me
explique em português simples o que aconteceu, conserte se for algo do projeto, e me
diga o comando pra tentar de novo. NÃO me mostre arquivo.

[colo aqui o erro]
```

"O Claude lê o erro como você lê um exame alterado, e te diz a conduta. Errar aqui é parte do processo, não é fracasso."

---

## SEÇÃO 5: O CLÍMAX — DOIS CLIQUES — 12 min

**Tom:** O ápice. Desacelera. O .exe abre com dois cliques, sem terminal. Payoff observável.

"O Claude terminou de montar. Ele te diz onde a caixa ficou — numa pasta chamada `dist`. Vamos abrir essa pasta pra achar o programa:"

[TELA: no terminal]

```bash
explorer dist
```

"O Windows abre a janela de arquivos direto na pasta. E olha o que tem ali: um arquivo chamado `ClinMd-Tribe.exe`, com o ícone do seu app. É um programa de Windows de verdade. Igual o do Word. Igual o do WhatsApp.

Repara num detalhe: no comando você escreveu só `ClinMd-Tribe`, sem o `.exe`. O `.exe` é o sobrenome que o Windows dá automaticamente pra todo programa — você não digita, ele aparece sozinho no arquivo.

---

Agora o momento.

Duplo-clique no `ClinMd-Tribe.exe`.

Um aviso honesto: como tudo está espremido num arquivo só, a primeira abertura pode levar uns segundinhos a mais — o programa está se desempacotando por dentro. Da segunda vez em diante, mais rápido.

[pausa]

Olha o que NÃO aconteceu. Você não abriu o terminal. Não digitou comando. Não tinha Claude por perto. Clicou. Abriu. Como o Word.

E olha o que abriu: o seu app, com a roupa da TribeMD da aula passada, vivo, numa janela limpa. Sem nenhum terminal preto por trás.

---

Navega. Abre uma calculadora — calcula um escore. Abre o checklist cirúrgico — marca um item, o horário aparece. Abre o painel. Tudo funcionando, dentro da caixa, sem internet, sem Python, sem nada.

---

[pausa]

E aqui vem o pulo do gato. Esse único arquivo — esse `.exe` sozinho — você copia num pen drive, manda pro seu colega, e ele clica na máquina DELE. Sem Python. Sem terminal. Sem você. A fórmula virou remédio que anda sozinho.

Para um segundo e pensa no que você fez. No começo do curso, você não sabia o que era um terminal. Hoje você pegou um app que ajudou a construir, e transformou ele num programa de Windows que qualquer médico do planeta abre com dois cliques. Você não é mais só quem usa software. Você é quem entrega software. A fórmula saiu da bancada."

---

## SEÇÃO 6: O FISCAL NA PORTA — O ANTIVÍRUS — 6 min

**Tom:** Tranquilizador e honesto. A armadilha do antivírus, enquadrada antes de assustar.

"Agora uma coisa que PODE acontecer — e se acontecer, não é você que quebrou nada.

Quando o seu colega clicar no programa pela primeira vez, o Windows pode parar e mostrar uma tela azul: 'O Windows protegeu o seu computador', 'aplicativo não reconhecido', 'editor desconhecido'.

---

Por quê? Lembra do fiscal na entrada do hospital. Caixa de remédio que ele nunca viu, de um laboratório que ele não conhece ainda — ele para e cheira. Não é que o remédio tá envenenado. É que é novo, e ele não te conhece.

Tecnicamente: o seu programa não é 'assinado' — não tem ainda um carimbo de fabricante reconhecido que o Windows confie de cara. Então o fiscal desconfia por precaução. É chato, mas é o fiscal fazendo o trabalho dele.

---

Como liberar, sem desligar a segurança do seu colega: naquela tela azul, tem um link pequeno, 'Mais informações'. Clica nele. Aí aparece um botão: 'Executar assim mesmo'. Isso diz pro Windows: 'eu conheço esse programa, pode passar'.

Repara no que você NUNCA faz: você nunca pede pro colega desligar o antivírus inteiro. Isso seria desarmar o hospital pra entregar uma caixa. Você libera só AQUELA caixa, AQUELA vez. Da segunda abertura em diante, o Windows já confia e nem pergunta mais.

---

E o jeito definitivo de o fiscal nunca mais te parar — assinar digitalmente o seu programa, como um CRM do software — é assunto de produto profissional, e a gente toca nele na próxima aula, quando falar de soltar isso no mundo direito."

---

## SEÇÃO 7: A CAIXA TEM TAMANHO (E TÁ TUDO BEM) — 3 min

**Tom:** Desmistificador, leve. O peso e o Windows-only como esperados, não como defeito.

"Mais duas coisas que você vai notar, e que são normais.

A primeira: o arquivo é maior que um app comum. Mesmo sem a busca pesada, a caixa traz o Python inteiro dentro pra não depender de nada lá fora. É o preço da independência, e é um preço justo: você troca 'leve, mas preso à minha bancada' por 'maior, mas anda sozinho na mão de qualquer um'. Por isso a entrega vai de pen drive ou link, não por e-mail.

A segunda: esse programa é do Windows. Roda em qualquer Windows, do seu colega, da secretária, da clínica. Um colega no Mac precisaria de uma caixa diferente — mesma fórmula, outra embalagem. Pra sua turma, que é quase toda Windows, essa é a caixa certa.

Nada disso é defeito. É a natureza de um remédio de prateleira: vem pronto, vem completo, e por isso vem numa caixa de tamanho de gente grande."

---

## SEÇÃO 8: ENCERRAMENTO — DA BANCADA PRA PRATELEIRA — 6 min

**Tom:** Síntese pelo aluno, LGPD como ápice do eixo, e a ponte para aula_39.

"Recapitula, você dizendo na sua cabeça.

Você pegou a sua fórmula manipulada — o app que só rodava na sua bancada, com o seu comando — e transformou ela num remédio de prateleira. Um programa de Windows que abre com dois cliques, sem terminal, sem você, na máquina de qualquer médico. Você decidiu, com cabeça de produto, o que vai na caixa de bolso: as calculadoras e o checklist, o que mais se usa. Aprendeu que a caixa é maior porque traz tudo dentro, e que o fiscal-antivírus pode cheirar uma caixa nova e como liberar sem desarmar o hospital. E não escreveu nem leu uma linha de código. Você pediu uma caixa e abriu ela.

---

E agora a privacidade — e essa é a aula onde tudo que a gente martelou o curso inteiro fecha com chave de ouro.

Durante semanas eu repeti: dado de paciente não sai, tudo roda local, na sua máquina. Hoje aconteceu uma coisa nova e poderosa. O app saiu da sua máquina — virou uma caixa que você entrega pro colega. E mesmo assim, repara: o eixo não quebrou. Ficou mais forte.

Porque o programa roda cem por cento offline, na máquina do colega, sem internet. Quando ELE usar o app pra calcular um escore ou guardar um checklist de cirurgia, o dado do paciente DELE fica na máquina DELE — não vem pra você, não sobe pra lugar nenhum, não passa pela nuvem. Você entregou a ferramenta, não os dados. Cada médico vira dono do próprio cofre.

E olha o detalhe que prova isso: lembra que a gente fez questão de NÃO deixar a pasta `data/` entrar na caixa? Foi de propósito. A caixa leva o app — as telas, as contas. A caixa NÃO leva paciente nenhum. O colega recebe uma farmácia vazia e limpa; quem coloca remédio nas prateleiras dele é ele, na máquina dele.

Esse é o ápice do 'tudo local': não importa em quantas mãos o app chegue, o dado de cada um fica trancado em cada um. Isso é privacidade desenhada na raiz, não remendada depois.

---

Mas calma antes de sair distribuindo. Você fez a caixa. Ela abre. O remédio funciona. Só que um laboratório sério não joga a caixa na rua assim.

Antes de o remédio chegar na prateleira, tem uma última conferência: a caixa tá lacrada direito? Não escapou nada que não devia ir junto — nenhuma chave secreta, nenhum dado, nenhuma sobra? E o colega vai saber usar — cadê a bula?

Na próxima aula, a última do polimento, a gente faz essa conferência final, como uma auditoria de qualidade antes do lote sair. Passa um pente-fino de segurança no que você vai entregar, monta um checklist de entrega — a sua bula — e fala de como soltar isso no mundo direito.

Você já sabe fazer o remédio. Na próxima, a gente aprende a entregar ele como um laboratório de respeito entrega. Até lá."

---

**FIM DO ROTEIRO**

---

> **NOTAS DE PRODUÇÃO (não falar — operacional):**
>
> - **Decisão do Dr. Petrus (escopo):** o `.exe` é a versão LEVE — calculadoras + checklist + painel, SEM o RAG. Ferramenta: **`flet pack`** (PyInstaller), NÃO `flet build windows` (que exigiria Visual Studio + Flutter). Sem o torch/sentence-transformers, o empacotamento é robusto e o aluno não instala nada pesado.
> - **Excluir o RAG do pack (CRÍTICO) — gate verificável:** o Prompt 1 manda deixar a busca de fora E conferir o tamanho. **Se o `.exe` passar de ~300-400 MB, o torch vazou** → exigir um ponto de entrada de distribuição que NÃO importe o módulo de busca + `--exclude-module=torch --exclude-module=chromadb --exclude-module=sentence_transformers`. NÃO gravar antes de confirmar o tamanho. PyInstaller faz análise estática de imports: `--exclude-module` sozinho não basta se `main.py` importa a busca no topo — daí o entry-point de distribuição separado. **Cravar o comportamento:** a versão distribuível deve NÃO renderizar o item de busca no menu (REMOVER, não só desabilitar) — a narração diz "fica de fora", então o app não pode mostrar a busca na tela. Validar que calculadoras/checklist/painel funcionam offline.
> - **`flet pack` só roda no Windows** (para gerar .exe). Confirmar que a conta-piloto grava no Windows. Saída em `dist/` (padrão PyInstaller).
> - **Tempo/tamanho:** o pack demora (tela cheia de texto verbose — avisar "não precisa ler"); cortar a espera na edição. Sem o RAG, o tamanho é bem menor que seria, mas ainda dezenas-centenas de MB (Python runtime). Confirmar o tamanho real e ajustar a fala da Seção 7.
> - **SmartScreen/antivírus:** `.exe` não-assinado dispara a tela azul do SmartScreen. Se na conta-piloto não disparar (varia por reputação), gravar como "pode acontecer, e se acontecer é isto". Caminho: Mais informações → Executar assim mesmo. NUNCA ensinar a desligar o antivírus.
> - **Prova do "máquina de qualquer um" (forte):** se possível, gravar o `.exe` abrindo numa 2ª máquina Windows SEM Python instalado — é a prova definitiva. E mostrar uma busca... não: a busca está fora; mostrar calculadora+checklist offline (Wi-Fi desligado) reforça o LGPD.
> - **Prompt 2 (diagnóstico):** errar no 1º pack é esperado; o aluno cola o erro no Prompt 2 e o Claude orienta. Não cortar essa possibilidade da narração (Seção 4 já avisa).
> - **Distribuição (onefile — CORRIGIDO):** o `flet pack` (default) gera UM `.exe` autossuficiente em `dist/` — NÃO precisa de DLLs ao lado; pode entregar o `.exe` solto. Zipar é opcional (evita bloqueio de download do navegador). Pen drive (presencial, 100% offline) ou link (à distância); nunca e-mail (tamanho). Onefile: a 1ª abertura é mais lenta (auto-extração num tempdir) e tende a disparar MAIS o SmartScreen — ambos avisados na narração. A analogia "Word/WhatsApp" da Seção 5 é sobre "ser um programa de verdade", NÃO sobre tamanho — não cruzar com a discussão de peso da Seção 7.
> - **Armadilha bash:** os únicos comandos são `flet pack ...`, `explorer dist`, `git`. Zero `uv run python -c`.
> - **Gancho aula_39:** auditoria final (token/segredo, `data/`, o que vai junto) + checklist de entrega ("bula") + distribuição responsável.
