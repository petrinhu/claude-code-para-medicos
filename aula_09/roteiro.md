# Aula 09 — Git Remoto: Seu Código na Nuvem + Clone de Ferramentas

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~42 min  
**Tom:** Colega com humor leve e didático — Git remoto e primeiro clone real

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Continuidade direta da aula anterior

"Na aula passada você instalou o Git e fez seus primeiros commits.

Seu repositório existe. Tem histórico. Funciona.

Mas só na sua máquina.

Se o computador queimar, o projeto some. Se você quiser trabalhar
de outro computador, não tem como. Se um colega quiser contribuir,
não há como compartilhar.

Git local é como guardar o prontuário só em papel na gaveta.

Hoje você vai colocar esse repositório na nuvem — de forma
segura, sem custo, e controlada por você.

E no final desta aula, você vai usar esse mesmo conhecimento
para clonar as ferramentas do Claude Code do Codeberg.

Vamos lá."

---

## SEÇÃO 2: REPOSITÓRIO REMOTO — O QUE É (3 min)

**Tom:** Analogia clínica, sem jargão

"Quando o prontuário eletrônico sincroniza com o servidor do hospital,
você consegue acessá-lo de qualquer computador do plantão.

Repositório remoto é a mesma coisa para o seu código.

Você tem o repositório local — na sua máquina.
Você tem o repositório remoto — no servidor na internet.

Os dois ficam sincronizados. O que você salva localmente,
você envia para o servidor. Se precisar pegar de outro computador,
você baixa do servidor.

A ferramenta que usamos para isso se chama GitHub.

GitHub é gratuito, é o padrão da indústria, e é onde a maioria
dos projetos de software do mundo vive — incluindo o código do Linux,
do Python, e do próprio Claude Code.

Vamos criar sua conta e subir o projeto."

---

## SEÇÃO 3: CONTA NO GITHUB + CRIAR REPOSITÓRIO (8 min)

**Tom:** Passo a passo no navegador

"Abra o navegador e acesse:

```
https://github.com
```

Clique em 'Sign up' e crie uma conta gratuita.
Use um e-mail profissional — de preferência o mesmo que você
configurou no Git na aula anterior.

[aguardar criação de conta]

Com a conta criada, clique no botão '+' no canto superior direito
e escolha 'New repository'.

Preencha:
- Repository name: clinmd-tribe
- Description: App clínico local — ClinMd-Tribe
- Visibilidade: Private (seu código, seus dados)

Deixe as outras opções como estão. Clique em 'Create repository'.

[mostrar tela criada]

O GitHub criou um repositório vazio e já mostrou os comandos
que você precisa rodar para conectar o seu repositório local.

Copie os comandos que aparecem na seção 'push an existing repository'.
Vamos usar em seguida."

---

## SEÇÃO 4: CONECTAR LOCAL AO REMOTO + PRIMEIRO PUSH (10 min)

**Tom:** Mão na massa — os três comandos do ciclo remoto

"Abra o PowerShell. Entre na pasta do projeto.

Se você criou 'meu-primeiro-repo' na aula passada, entre nele.
Se criou 'consultorio-digital', use esse.

Vamos usar o repositório do dever de casa da aula anterior.

---

**Conectar o repositório local ao remoto:**

O GitHub gerou um comando parecido com este:

```
git remote add origin https://github.com/seu-usuario/clinmd-tribe.git
```

Cole e execute esse comando com o URL do SEU repositório
(o GitHub já mostra o URL correto na tela).

'Remote' significa repositório remoto.
'Origin' é o apelido que damos para o remoto principal.
É como nomear o servidor do hospital: 'hospital-central'.

---

**Enviar os commits para o GitHub:**

```
git push -u origin main
```

[aguardar — pode pedir login]

Se pedir usuário e senha: use o usuário e senha do GitHub.
O Windows pode abrir uma janela de autenticação — pode autorizar.

[mostrar o resultado no terminal]

[mostrar o repositório atualizado no GitHub]

Os arquivos apareceram no GitHub. Seu código está na nuvem.

---

O ciclo a partir de agora é simples:

```
git add .            ← prepara todas as mudanças
git commit -m "..."  ← tira a foto
git push             ← envia para o GitHub
```

Três comandos. Você vai usar eles toda vez que terminar uma sessão
de trabalho com o Claude Code."

---

## SEÇÃO 5: DEMO — GIT CLONE: INSTALAR FERRAMENTAS DO CODEBERG (12 min)

**Tom:** Revelação prática — o motivo real de aprender Git agora

"Agora vou mostrar por que você aprendeu Git antes de tudo.

Na próxima aula você vai instalar skills e agents para o Claude Code.
Essas ferramentas ficam em repositórios Git — no Codeberg,
que é meu servidor pessoal de repositórios.

Para instalar, o comando é 'git clone'.

Clone é baixar uma cópia de um repositório remoto para o seu computador.

Vamos fazer um preview. No PowerShell:

```
git clone https://codeberg.org/petrinhu/memo_persistente.git ~\.claude\skills\memo_persistente
```

[executar e mostrar]

O Git baixou o repositório inteiro. A skill está instalada.

Isso é o que vai acontecer na próxima aula para cada skill e agent.
Você não precisou entrar no site, fazer download manual, descompactar arquivo.
Um comando e pronto.

---

Pode fazer o mesmo com qualquer repositório público do GitHub.
Por exemplo, para baixar o código-fonte do Flask (framework Python):

```
git clone https://github.com/pallets/flask.git
```

Claro que você não vai fazer isso agora. Mas é bom saber que
o Git é a forma padrão de distribuir software no mundo inteiro.

Quando o Claude Code instalar uma dependência Python usando uv,
por baixo dos panos também tem Git envolvido.

Git é invisível quando funciona. Você só percebe quando não está lá."

---

## SEÇÃO 6: PULL — ATUALIZAR LOCAL COM O REMOTO (5 min)

**Tom:** Rápido, complementando o ciclo

"Mais um comando para fechar o ciclo.

Imagine que você está num tablet no consultório e fez um commit.
Em casa, no computador principal, você quer puxar essa atualização.

O comando é:

```
git pull
```

Pull é o oposto de push.
Push envia do local para o remoto.
Pull traz do remoto para o local.

Ciclo completo:

```
git pull             ← pega atualizações do servidor
[trabalha, edita]
git add .
git commit -m "..."
git push             ← envia para o servidor
```

É o mesmo ciclo de um médico que acessa o PEP no hospital,
atualiza o prontuário e fecha.

Com o tempo isso vira reflexo. Você não vai pensar nos comandos —
vai só fazer, como salvar um documento."

---

## SEÇÃO 7: ENCERRAMENTO (2 min)

**Tom:** Resumo, motivação e ponte para a aula_10

"Resumo do que ficou pronto hoje.

Conta no GitHub criada.
Repositório clinmd-tribe criado na nuvem.
Primeiro push feito — código na nuvem.
git clone demonstrado com skill real do Claude Code.
Ciclo completo: pull, add, commit, push.

Você agora tem o ambiente de versionamento de um desenvolvedor profissional.

---

Dever de casa.

Faça três commits no repositório clinmd-tribe.
Um por dia, nos próximos três dias.
Pode ser qualquer mudança — adicionar um arquivo de anotações,
uma lista de ideias para o app, qualquer coisa.

O objetivo não é o conteúdo. É criar o hábito de commitar.

Na próxima aula — a aula_10 — a gente revela o produto que você vai construir.
Instala o ambiente completo: plugins, agents, MCPs.
E cria o projeto ClinMd-Tribe com o gerenciador de pacotes.

Junto com o produto, você vai conhecer a skill `/tab_pendencias` — que gera
a tabela de tarefas do projeto ordenada por prioridade — e os agents C-levels:
Caetano (CTO) para decisões de arquitetura, Cósimo (Chief of Staff) para
montar o time, e os especialistas operacionais para cada parte do código.

Git + /tab_pendencias + agents = o fluxo de trabalho completo de um dev profissional.

Git pronto. Agora vamos montar o laboratório.

Até lá."

---

**FIM DO ROTEIRO**
