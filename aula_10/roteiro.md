# Aula 10 — Setup do Ambiente Dev + ClinMd-Tribe Reveal

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~48 min  
**Tom:** Colega com humor leve e didático — momento de passagem de nível

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Virada de página — a fase avançada começa

"Nas últimas nove aulas você dominou o Claude Code — sete sem programação, duas aprendendo Git.

Você pesquisou literatura no PubMed, criou flashcards, gerou um pôster de congresso,
publicou carrossel no Instagram e fez um dashboard de gestão do consultório.

Tudo isso com o Claude como co-piloto.

Agora a pergunta é: e se você pudesse construir algo seu?
Uma ferramenta clínica. Que funciona offline. No seu computador.
Que você controla completamente.

Esta aula começa a responder essa pergunta.

Bem-vindo à fase avançada."

---

## SEÇÃO 2: CLINMD-TRIBE — O REVEAL (3 min)

**Tom:** Revelação com entusiasmo contido — deixar o produto falar

"O que a gente vai construir juntos nas próximas semanas tem um nome.

ClinMd-Tribe.

É um app clínico 100% local. Roda no seu computador.
Não precisa de internet. Não manda dado para servidor nenhum.
Funciona no Windows, no Mac, no Linux.

O que ele faz?

Primeiro: calculadoras clínicas — CHA₂DS₂-VASc, PHQ-9, GAD-7, YMRS, HAM-D.
Sem anuncio. Sem login. Clicou, calculou.

Segundo: anotador clínico — templates de consulta, salvamento local.
Seu modelo de anamnese, do jeito que você gosta.

Terceiro: busca inteligente em PDFs — guidelines, artigos que você salvou.
Você pergunta em linguagem natural, ele acha.

É isso. Um app para uso diário no consultório.
Construído do zero, por você, com o Claude como par de programação.

Nas próximas aulas você vai entender como ele funciona por dentro.
Hoje você prepara o ambiente para construir."

---

## SEÇÃO 3: O AMBIENTE DE UM DEV REAL (2 min)

**Tom:** Didático — analogia clínica para ferramentas de desenvolvimento

"Todo médico que vai fazer uma cirurgia prepara o campo operatório primeiro.

Você não entra na sala e começa a cortar. Você esteriliza os instrumentos,
monta a bandeja, posiciona o paciente.

Desenvolvimento de software é igual.

Antes de escrever a primeira linha de código do ClinMd-Tribe,
você vai instalar quatro categorias de ferramentas:

Plugins — superpoderes adicionais para o Claude Code.
Skills — atalhos de trabalho que o Claude conhece.
Agents — especialistas virtuais que o Claude aciona quando precisa.
MCPs — conexões com ferramentas externas como PubMed e Canva.

E no final: uv — o gerenciador de dependências que vai organizar o projeto.

Vamos instalar tudo. Passo a passo."

---

## SEÇÃO 4: DEMO — PLUGIN OFICIAL + SKILLS (10 min)

**Tom:** Prático, dois momentos — o oficial e o personalizado

"Começa pelo plugin oficial.

Abra o terminal e inicie o Claude Code:

```
claude
```

Dentro do Claude Code, digite:

```
/plugin install superpowers@claude-plugins-official
```

[aguardar instalação]

Pronto. Isso instalou o pacote superpowers — ele adiciona um conjunto de skills
prontas para uso: brainstorming, planejamento, revisão de código, debuggin...

Perceba a barra `/` — no Claude Code, comandos que começam com `/` são internos.
São como atalhos de teclado, mas para o Claude.

Documentação oficial em: https://docs.anthropic.com/pt/claude-code/plugins

---

Agora as skills que eu criei — ficam no Codeberg, meu servidor git privado.

São três. Cada uma resolve um problema real de desenvolvimento.

Jeito difícil: clona manualmente cada repositório.

```
git clone https://codeberg.org/petrinhu/forgejo-skill.git ~/.claude/skills/forgejo
git clone https://codeberg.org/petrinhu/memo_persistente.git ~/.claude/skills/memo_persistente
git clone https://codeberg.org/petrinhu/tab_pendencias.git ~/.claude/skills/tab_pendencias
```

[executar e mostrar as pastas criadas em ~/.claude/skills/]

Mas tem um jeito mais fácil.

Jeito fácil: você fecha o Claude Code, abre um novo terminal e escreve:

```
claude "Clone os três repositórios de skills do Dr. Petrus a partir do Codeberg:
1. https://codeberg.org/petrinhu/forgejo-skill.git → ~/.claude/skills/forgejo
2. https://codeberg.org/petrinhu/memo_persistente.git → ~/.claude/skills/memo_persistente
3. https://codeberg.org/petrinhu/tab_pendencias.git → ~/.claude/skills/tab_pendencias
Execute os clones e confirme cada um."
```

[mostrar o Claude executando automaticamente]

Resultado idêntico. O Claude fez o trabalho.

Para que serve cada uma?

/forgejo — controla seu servidor de código diretamente do Claude.
/memo_persistente — salva memórias permanentes entre sessões.
/tab_pendencias — gera tabela de tarefas ordenada por prioridade.

A partir da aula de agents, você vai usar as três o tempo todo."

---

## SEÇÃO 5: DEMO — AGENTS: JEITO DIFÍCIL E JEITO FÁCIL (12 min)

**Tom:** Revelação progressiva — mostrar a escala e depois simplificar

"Agents são especialistas que o Claude aciona dependendo do contexto.

Quando você pede pra criar uma tela, o Claude pode chamar o frontend-engineer.
Quando você pede análise de segurança, chama o security-engineer.
Quando você quer saber se uma feature vale a pena, chama o product-manager.

Eu tenho 65 agents instalados em ~/.claude/agents/.

Vamos ver a lista:

```
ls ~/.claude/agents/ | sort
```

[mostrar a lista — 65 arquivos .md]

Cada arquivo .md é um agent. Dentro dele: nome, descrição, instruções de comportamento.

O jeito difícil de instalar é criar cada arquivo manualmente.

Vou mostrar a estrutura de um:

```
cat ~/.claude/agents/qa-engineer.md | head -20
```

[mostrar o cabeçalho do arquivo]

Você vê: nome, descrição, ferramentas disponíveis, instruções.

Para criar o seu próprio agent, você escreve um arquivo assim e salva em ~/.claude/agents/.

---

Mas ninguém faz isso para 65 agents à mão.

O jeito fácil: você manda o Claude buscar e instalar.

Meu repositório de backup do ~/.claude/ fica em:
https://codeberg.org/petrinhu/claude-memory

A pasta agents/ lá dentro tem todos os 65 arquivos.

O comando:

```
claude "Visite https://codeberg.org/petrinhu/claude-memory e baixe todos os arquivos .md
da pasta agents/. Salve cada um em ~/.claude/agents/. Confirme quantos foram instalados."
```

[mostrar o Claude executando — navegando, baixando, salvando]

Pronto. 65 agents instalados com um comando.

---

Os 12 agents C-level são a liderança virtual do projeto:

| Agent | Papel |
|-------|-------|
| celso-ceo | Estratégia geral |
| capitolino-cpo | Produto — o que construir |
| caetano-cto | Tecnologia — como construir |
| camilo-cmo | Marketing e comunicação |
| cosmo-coo | Execução e coordenação |
| narciso-ciso | Segurança da informação |
| candido-cdo | Dados e analytics |
| caio-caio | Inteligência artificial |
| confucio-cfo | Finanças e orçamento |
| cicero-cro | Receita e vendas |
| claudio-clo | Jurídico e compliance |
| cosimo-chief-of-staff | Roteador — monta o time certo para cada tarefa |

Os outros 53 são os especialistas operacionais — o time de desenvolvimento.
Você vai conhecer cada um deles ao longo da fase avançada.

Para hoje: eles estão instalados. Quando você precisar, o Claude aciona o certo.

Tem um arquivo de referência completo — skills.html — na pasta desta aula.
Guarde ele. É a sua folha de cola do time."

---

## SEÇÃO 6: DEMO — MCPS INSTALADOS (5 min)

**Tom:** Rápido, mostrando o inventário já instalado

"MCPs são conectores.

MCP significa Model Context Protocol — o padrão que o Claude usa
para se conectar com ferramentas externas.

Para ver o que está instalado, dentro do Claude Code:

```
/mcp
```

[mostrar a listagem]

Os ativos aqui no nosso ambiente:

PubMed — busca artigos científicos diretamente
GitHub / Forgejo — gerencia repositórios de código
Canva — cria designs sem sair do Claude
Google Drive — acessa seus arquivos
Playwright — controla o navegador para automação
Desktop Commander — controla o desktop
Microsoft Docs — documentação técnica da Microsoft
Hostinger — gerenciamento de hosting web

Para o ClinMd-Tribe, os mais relevantes são PubMed e GitHub.

Se você quiser instalar um MCP novo:

```
claude mcp add [nome] [comando]
```

Ou pelo arquivo de configuração em ~/.claude/claude.json.

O detalhe importante: depois de instalar um MCP, reinicie o Claude.
A próxima seção explica exatamente quando reiniciar."

---

## SEÇÃO 7: QUANDO REINICIAR + CLAUDE -C (4 min)

**Tom:** Prático, resolve uma dúvida que todo iniciante tem

"Quando você instala um plugin ou um MCP,
o Claude precisa ser reiniciado para carregar a mudança.

É como reinstalar um driver no Windows — precisa reiniciar.

Para reiniciar: dentro do Claude Code, pressione Ctrl+C ou ESC,
feche o terminal, abra de novo e inicie com:

```
claude
```

---

Mas às vezes você estava no meio de uma conversa importante.
Você reiniciou e agora o Claude esqueceu tudo.

Para retomar de onde parou:

```
claude -c
```

O -c é de 'continue' — retomar a última conversa.

O Claude carrega o contexto da sessão anterior e continua.

Regra simples:

— Instalou algo novo? Reinicia com `claude`
— Quer continuar de onde parou? Abre com `claude -c`

Guarda essa regra. Você vai usar ela toda semana."

---

## SEÇÃO 8: DEMO — UV + CLINMD-TRIBE (8 min)

**Tom:** Mão na massa — o primeiro passo do produto

"Chegou a hora de criar o projeto.

Antes: precisamos do uv.

uv é o gerenciador de pacotes Python — pensa nele como a farmácia do projeto.
Ele sabe exatamente quais 'remédios' (bibliotecas) o projeto precisa,
em qual versão, e garante que nada vai conflitar.

Instalar o uv. No Windows, abra o PowerShell e cole:

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

[aguardar instalação]

Feche o PowerShell e abra um novo para que o uv fique no path.

Confirme a instalação:

```
uv --version
```

---

Agora o projeto.

Vamos criar dentro da pasta Documentos:

```
cd ~/Documents
uv init clinmd-tribe
```

[executar e mostrar a estrutura criada]

O uv criou:

clinmd-tribe/
  .python-version    — versão do Python que o projeto usa
  main.py            — arquivo inicial vazio
  pyproject.toml     — o prontuário do projeto: nome, versão, dependências

Abra o arquivo pyproject.toml:

```
cat clinmd-tribe/pyproject.toml
```

Você vê o nome 'clinmd-tribe'. Esse é o início do ClinMd-Tribe.

A partir da próxima aula, você vai adicionar a primeira dependência
e escrever as primeiras linhas de Python.

Mas hoje o que importa é que o campo operatório está pronto.
Ambiente instalado. Projeto criado. Time de desenvolvimento no lugar."

---

## SEÇÃO 9: ENCERRAMENTO (2 min)

**Tom:** Motivador, resumo do que ficou pronto, visão para frente

"Resumo do que ficou pronto hoje.

Plugin superpowers instalado.
Skills /forgejo, /memo_persistente e /tab_pendencias prontas.
65 agents no lugar — C-levels e time de desenvolvimento.
MCPs conectados: PubMed, GitHub, Canva e mais.
Projeto ClinMd-Tribe criado com uv.

Você tem agora o mesmo ambiente que eu uso para desenvolver com o Claude.

---

Dever de casa.

Abra o arquivo skills.html que está na pasta desta aula.
Leia as descrições dos 12 C-levels e escolha dois que mais fazem sentido
para o produto clínico que você imagina construir.

Na próxima aula, Python com analogias clínicas — sem sofrimento,
do jeito que você aprendeu a interpretar um ECG: um achado de cada vez.

Até lá."

---

**FIM DO ROTEIRO**
