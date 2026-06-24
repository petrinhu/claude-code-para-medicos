# Aula 08 — Git: O Prontuário do Seu Código

**Formato:** Gravada no OBS Studio, editada no Kdenlive  
**Duração:** ~40 min  
**Tom:** Colega com humor leve e didático — primeiro contato com versionamento

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Aberto e pronto:**

- [ ] PowerShell aberto e limpo (esta aula é toda no PowerShell; o Claude Code não é usado nas demos de Git, mas pode estar aberto numa aba à parte se você quiser).
- [ ] Pasta `Documents` (Documentos) acessível: a demo cria `meu-primeiro-repo` dentro dela na Seção 4.
- [ ] Garanta que `meu-primeiro-repo` NÃO existe ainda (apague se sobrou de um teste), para o `git init` nascer do zero limpo na frente da câmera.
- [ ] Decida se vai gravar a instalação do Git de fato ou se ela já está feita: se o Git já estiver instalado, o instalador da Seção 3 não roda igual. Para gravar a instalação completa, use uma máquina/usuário sem Git; para pular, deixe instalado e foque no `git --version`.

**Confira antes de gravar:**

- [ ] Teste antes o fluxo inteiro numa pasta de rascunho (`git init`, `echo`, `git add`, `git commit -m`, `git log --oneline`) para confirmar que cada comando devolve a saída que o roteiro descreve.
- [ ] Se você ainda NÃO configurou `user.name` e `user.email` nesta máquina, o `git commit` da Seção 4 pode pedir essa configuração antes de deixar commitar. Para o commit sair limpo na demo, ou configure antes (e então a Seção 5 vira reforço) ou tenha o texto de erro à mão para explicar e configurar na hora.
- [ ] Tenha em mente o nome e e-mail que vai digitar na Seção 5 (pode ser fictício para a gravação: `Dr. Exemplo` / `dr.exemplo@gmail.com`), para não expor dado pessoal real na tela.

**Navegador:** abra a aba: https://git-scm.com/download/win (usada na Seção 3 para baixar o Git for Windows).

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Direto, contextualizando a posição no curso

**[Aviso rápido dos óculos, antes de mergulhar]**

"Antes da gente começar: se você usa óculos de perto, é hora de calibrar a acomodação. O terminal hoje vai cuspir umas saídas com fonte miudinha, e eu não quero você forçando a vista igual quem tenta ler hemograma no plantão da madrugada. Põe os óculos, ajusta o foco, e vamos."

"Chegamos na aula 08, a porta de entrada da fase avançada.

Até aqui você usou o Claude Code sem programar. Pesquisa de literatura,
flashcards, dashboard de consultório, pôster de congresso.
Tudo funcionou. Tudo ficou salvo na pasta do seu computador.

Mas agora vamos dar um passo além. Vamos construir um app clínico real.
E pra fazer isso do jeito certo, você precisa de uma ferramenta que
protege o seu trabalho enquanto constrói.

Essa ferramenta se chama Git.

Nesta aula você vai instalar o Git, entender o que ele faz,
e começar a usá-lo da mesma forma que você anota uma evolução clínica.

Sem susto. Passo a passo."

---

## SEÇÃO 2: O QUE É GIT (3 min)

**Tom:** Analogia médica — PEP com histórico de versões

"Pensa no prontuário eletrônico do seu paciente.

Você faz uma consulta. Escreve a evolução. Salva.
Semana que vem, o paciente volta. Você escreve de novo.
O sistema guarda a evolução anterior — você consegue ler
o que estava escrito três meses atrás.

O PEP tem memória de versões.

Git faz a mesma coisa com os seus arquivos de código.

Cada vez que você faz uma 'foto' do projeto — a gente chama de commit —
o Git guarda como estava naquele momento.

Deu errado? Você volta para a foto anterior.
Quer ver o que mudou ontem? O Git mostra.
Quer trabalhar em duas versões ao mesmo tempo? Git permite.

Git é o prontuário eletrônico do seu projeto de software.

E assim como o PEP não é opcional para um médico sério,
Git não é opcional para quem vai construir software com o Claude."

---

## SEÇÃO 3: INSTALAÇÃO — GIT FOR WINDOWS (5 min)

**Tom:** Didático, pausado — cada clique explicado

"Vamos instalar o Git.

Abra o navegador e acesse:

```
https://git-scm.com/download/win
```

Clique em 'Click here to download' — o download vai começar.

[aguardar download]

Execute o instalador. Quando aparecer a tela de opções,
você pode clicar em 'Next' em tudo — as configurações padrão são boas.

A única tela pra prestar atenção é 'Choosing the default editor'.
Mude para 'Use Notepad' se aparecer o Vim como opção padrão.
Vim é um editor antigo que pode confundir quem está começando.

[aguardar instalação]

Quando terminar, feche o instalador.

Agora: abra o PowerShell.

Windows + R, digite 'powershell', Enter.

Digite:

```
git --version
```

Se aparecer algo como 'git version 2.44.0', funcionou.
Git instalado."

---

## SEÇÃO 4: DEMO — PRIMEIROS COMANDOS (15 min)

**Tom:** Mão na massa, explicando cada comando com analogia

"Agora vamos criar o primeiro repositório.

Repositório é o nome técnico para 'projeto com Git ativado'.
Pensa como uma pasta de prontuários que o PEP controla.

Vamos criar dentro de Documentos.

No PowerShell:

```
cd Documents
```

Agora crie uma pasta chamada 'meu-primeiro-repo':

```
mkdir meu-primeiro-repo
cd meu-primeiro-repo
```

---

**Passo 1: inicializar o repositório**

```
git init
```

[executar e mostrar o resultado]

O Git respondeu algo como 'Initialized empty Git repository'.

Isso significa que essa pasta agora tem memória. O Git está ativo.

---

**Passo 2: criar um arquivo de teste**

```
echo "Meu primeiro arquivo" > arquivo.txt
```

Você criou um arquivo chamado arquivo.txt dentro da pasta.

---

**Passo 3: verificar o status**

```
git status
```

[mostrar resultado]

O Git mostra que arquivo.txt existe mas ainda não foi 'fotografado'.
Aparece como 'untracked file' — arquivo ainda não rastreado.

Analogia: você escreveu a evolução do paciente, mas ainda não salvou no PEP.

---

**Passo 4: preparar para o commit**

```
git add arquivo.txt
```

Agora rode git status de novo:

```
git status
```

Mudou. O arquivo agora aparece em verde — 'Changes to be committed'.

Você preparou a evolução para salvar. Falta só confirmar.

---

**Passo 5: fazer o commit**

```
git commit -m "Meu primeiro commit"
```

[mostrar resultado]

Git respondeu com algo como '[main f3c2a1] Meu primeiro commit'.

Pronto. Você tirou a primeira foto do projeto.

O '-m' é de 'message' — mensagem que descreve o que mudou.
Boa prática: mensagem clara, verbo no imperativo.
'Adiciona calculadora de risco', 'Corrige cálculo do YMRS'.
Você vai ler isso daqui a seis meses — escreva como se fosse uma anotação de prontuário.

---

**Passo 6: ver o histórico**

```
git log --oneline
```

[mostrar resultado]

Aparece um código curto e a mensagem do seu commit.

Esse histórico vai crescer. Cada commit é uma linha.
É a linha do tempo do seu projeto.

---

Deixa eu resumir o ciclo:

```
git add [arquivo]         ← prepara a foto
git commit -m "mensagem"  ← tira a foto
git status                ← vê o estado atual
git log --oneline         ← vê o histórico de fotos
```

São quatro comandos. Você vai usar esses quatro toda semana enquanto construir software."

---

## SEÇÃO 5: CONFIGURAÇÃO INICIAL (5 min)

**Tom:** Rápido — configuração que precisa ser feita uma vez

"Tem mais uma coisa que precisa ser feita uma única vez.

O Git precisa saber quem é você — porque cada commit fica assinado.
É como a assinatura digital no prontuário: registra quem fez.

No PowerShell:

```
git config --global user.name "Dr. Seu Nome"
git config --global user.email "seu.email@gmail.com"
```

Substitua pelo seu nome e e-mail reais.

Feito isso, todos os commits futuros em qualquer projeto vão ter
sua assinatura. Você só faz isso uma vez na máquina."

---

## SEÇÃO 6: POR QUE ISSO IMPORTA PRO CLINMD-TRIBE (5 min)

**Tom:** Contextualizando — ponte pra aula seguinte

"Você pode estar pensando: 'Petrus, pra que isso tudo?
Eu só quero usar o Claude Code.'

Resposta em três partes.

**Parte 1:** Na próxima aula, você vai clonar repositórios do Codeberg
para instalar skills e agents do Claude Code.
O comando que vai usar para isso é 'git clone'.
Se não tiver Git instalado, o comando não funciona.

**Parte 2:** Quando o Claude Code constrói o ClinMd-Tribe,
ele vai criar arquivos, modificar arquivos, às vezes quebrar coisas.
Com Git, qualquer erro tem voltar atrás. Sem Git, se o Claude errar
e você salvar, pode perder trabalho.

**Parte 3:** Git é a ferramenta que permite colaborar.
Se um dia você quiser mostrar seu projeto pra alguém — um colega,
um dev que vai ajudar — você envia o repositório.
É como compartilhar acesso ao prontuário de forma segura.

Git não é burocracia. É segurança clínica para o seu código.

---

**Bônus: o que está vindo na aula_10.**

Junto com o Git, você vai instalar duas categorias de ferramentas que rodam
dentro do Claude Code:

Skills — atalhos de trabalho. A mais importante para o ClinMd-Tribe é
a `/tab_pendencias`: você digita esse comando no Claude Code e recebe
uma tabela com todas as tarefas pendentes do projeto, ordenadas por prioridade.
Toda semana você abre o Claude Code com `/tab_pendencias` e sabe exatamente
o que pedir.

Agents — especialistas virtuais. Um frontend-engineer para a interface Flet,
um backend-engineer para a lógica, um Caetano (CTO) para decisões de arquitetura,
um Cósimo (Chief of Staff) que monta o time certo para cada momento.
Você não precisa saber tudo — você tem o time disponível para cada pergunta.

Git é a fundação. Skills e agents rodam em cima dela."

---

## SEÇÃO 7: ENCERRAMENTO (2 min)

**Tom:** Resumo e dever de casa

"Resumo do que ficou pronto hoje.

Git instalado no Windows.
Primeiro repositório criado em Documentos.
Quatro comandos aprendidos: add, commit, status, log.
Identidade configurada: cada commit tem seu nome.

Dever de casa.

Crie uma pasta chamada 'consultorio-digital' em Documentos.
Inicialize com 'git init'.
Crie um arquivo de texto com qualquer conteúdo.
Faça dois commits — um agora, edite o arquivo, faça outro.
Veja o histórico com 'git log --oneline'.

Dois commits no histórico. É isso.

Na próxima aula, você vai aprender a sincronizar esse repositório
com a internet — e usar o Git para instalar as ferramentas do Claude Code.

Até lá."

---

**FIM DO ROTEIRO**
