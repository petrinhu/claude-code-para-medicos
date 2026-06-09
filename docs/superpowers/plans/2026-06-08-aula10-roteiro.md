# Aula 10 — Roteiro Refatorado — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Substituir `aula_10/roteiro.md` com roteiro correto cobrindo S01.01 — Terminal + uv (~48 min), deprecar `aula_11/roteiro.md` com nota de incorporação, e gerar os HTMLs correspondentes.

**Architecture:** Dois arquivos Markdown canônicos do curso (seções numeradas, Tom, falas entre aspas, blocos copiáveis) + HTMLs gerados via pandoc. Segue spec aprovado em `docs/superpowers/specs/2026-06-08-aula10-design.md`. Zero código escrito pelo aluno — comandos são PowerShell/uv, nunca editor de texto.

**Tech Stack:** Markdown, pandoc (HTML export), Git.

---

## Referência rápida do spec

| Seção | Conteúdo | Duração |
|---|---|---|
| 1 | Abertura: virada de fase — "você passa de usuário para construtor" | 2 min |
| 2 | ClinMd-Tribe Reveal: calculadoras + anotador + PDF, sem 4 camadas | 3 min |
| 3 | uv: por que existe — interação medicamentosa + analogia farmácia | 2 min |
| 4 | Demo: install + init — PowerShell, `uv --version`, `uv init`, `dir` | 8 min |
| 5 | Demo: type pyproject.toml — prontuário vazio antes de instalar | 5 min |
| 6 | Demo: uv add + .venv + uv.lock — prontuário muda, carrinho do leito | 10 min |
| 7 | Demo: uv run — `type main.py`, `uv run python main.py`, regra definitiva | 8 min |
| 8 | Referência de comandos uv — tabela: init/add/remove/run/sync | 5 min |
| 9 | Encerramento + dever — uv add/remove requests + git status + ponte aula_12 | 5 min |

**Fusão:** aula_10 absorve aula_11. Removidos: Plugin/Skills/Agents/MCPs, Clean Arch preview, `claude -c`.  
**Zero código:** Médico nunca escreve Python. Claude escreve, médico supervisiona.

---

## Task 1: Escrever `aula_10/roteiro.md`

**Files:**
- Modify: `aula_10/roteiro.md` (sobrescrever conteúdo atual)

- [ ] **Step 1: Escrever o roteiro completo**

Conteúdo completo do arquivo:

```markdown
# Aula 10 — Terminal + uv: o Bisturi Digital

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~48 min  
**Tom:** Colega com humor leve e didático — "você passa de usuário para construtor"  
**Módulo:** S01.01 — Fundação da Fase Avançada  
**SO:** Windows/PowerShell (padrão único do curso)  

---

## SEÇÃO 1: ABERTURA — 2 min

**Tom:** Virada de página — a fase avançada começa aqui

"Nas últimas nove aulas você aprendeu a pedir.

Você pesquisou no PubMed, resumiu guidelines, criou slides,
gerou um pôster, publicou no Instagram,
fez um dashboard de gestão do consultório.

Tudo descrevendo o problema em linguagem natural.

Agora a pergunta muda.

Não é mais 'o que o Claude pode fazer por mim'.

É: o que eu posso construir com o Claude como par de programação?

Bem-vindo à fase avançada."

---

## SEÇÃO 2: CLINMD-TRIBE REVEAL — 3 min

**Tom:** Revelação com entusiasmo contido — deixar o produto falar

"O que a gente vai construir juntos tem um nome: ClinMd-Tribe.

Três funcionalidades.

Calculadoras clínicas — CHA₂DS₂-VASc, PHQ-9, GAD-7, YMRS.
Sem anúncio. Sem login. Clicou, calculou.

Anotador clínico — templates de consulta salvos localmente,
do jeito que você gosta, no seu padrão.

Busca inteligente em PDF — você pergunta em linguagem natural,
ele acha no guideline ou no artigo que você salvou.

100% local. Funciona no seu computador sem internet.
Dado de paciente não sai da sua máquina.

O dashboard que você fez na aula_07 foi descartável —
você gerou, usou, refez no mês seguinte.

O ClinMd-Tribe é permanente.
Você vai construí-lo do zero, aula por aula, com o Claude como parceiro.

Hoje a gente monta o laboratório."

---

## SEÇÃO 3: UV — POR QUE EXISTE — 2 min

**Tom:** Contextualizar o problema antes de instalar a solução

"Antes de qualquer coisa, precisamos falar de um problema real.

Python tem um ecossistema enorme de bibliotecas —
ferramentas prontas que você usa no projeto.
Você não escreve o ibuprofeno na sua cozinha. Você compra na farmácia.

O problema: duas bibliotecas às vezes precisam de versões incompatíveis de uma terceira.

É como uma interação medicamentosa:
remédio A e remédio B funcionam sozinhos.
Juntos, na mesma dose, conflito.

O uv resolve isso.

Ele é o gerenciador de dependências — a farmácia do projeto.
Ele sabe exatamente quais remédios o projeto precisa,
em qual versão, e garante que nada conflita.

Primeiro passo: instalar a farmácia."

---

## SEÇÃO 4: DEMO — INSTALL + INIT — 8 min

**Tom:** Prático, passo a passo, confirmando cada etapa antes de avançar

"Abra o PowerShell.

Vamos instalar o uv. Método recomendado no Windows:

[digitar no PowerShell]

```
winget install --id=astral-sh.uv -e
```

[aguardar a instalação]

Se o winget não estiver disponível no seu Windows, use este comando alternativo:

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

Instalado. Agora: feche o PowerShell e abra um novo.

Isso é necessário para que o Windows reconheça o uv no caminho do sistema.

No novo PowerShell, confirme a instalação:

```
uv --version
```

[mostrar o número de versão]

Sinal vital positivo. O uv está vivo.

---

Agora vamos para a pasta de projetos.

Na aula de abertura eu pedi para você criar a pasta
`projetos` dentro de Documentos, no Windows Explorer.

Navegar até lá:

```
cd $HOME\Documents\projetos
```

Criar o projeto ClinMd-Tribe:

```
uv init clinmd-tribe
```

[mostrar o output do uv init]

Entrar na pasta:

```
cd clinmd-tribe
```

Ver o que foi criado:

```
dir
```

[mostrar os três arquivos]

Três arquivos. Só três.

`.python-version` — qual versão de Python este projeto usa.
`main.py` — o arquivo de entrada do projeto, gerado automaticamente.
`pyproject.toml` — o prontuário do projeto.

A farmácia está de pé. Ainda vazia — mas organizada."

---

## SEÇÃO 5: DEMO — TYPE PYPROJECT.TOML — 5 min

**Tom:** Didático — ler o prontuário em voz alta, campo por campo

"Vamos abrir o prontuário.

Não abrir para editar — abrir para ler.
No PowerShell, o comando `type` lê um arquivo sem modificar nada:

```
type pyproject.toml
```

[mostrar o conteúdo]

Vai aparecer algo assim:

```
[project]
name = 'clinmd-tribe'
version = '0.1.0'
description = 'Add your description here'
requires-python = '>=3.11'
dependencies = []
```

Leitura clínica desse arquivo:

`name` — o nome do projeto. A identidade.

`version` — 0.1.0 significa versão inicial, ainda em desenvolvimento.
Quando você lança a primeira versão estável, vira 1.0.0.

`requires-python` — este projeto precisa de Python 3.11 ou mais novo.
Se alguém tentar rodar com Python 3.9, o uv avisa.

`dependencies` — a lista de remédios. Está vazia agora.
O prontuário existe, mas o paciente ainda não tem prescrição.

---

Uma nota importante.

Você não edita esse arquivo na mão. Nunca.
O uv edita por você, automaticamente, quando você instala ou remove uma biblioteca.

O mesmo vale para o uv.lock que vamos ver daqui a pouco.

No curso inteiro: você descreve o que quer, o Claude e o uv fazem.
Você lê e supervisiona."

---

## SEÇÃO 6: DEMO — UV ADD + .VENV + UV.LOCK — 10 min

**Tom:** Mostrar o antes e depois do pyproject.toml como evidência

"O ClinMd-Tribe vai ter interface gráfica.

A biblioteca que vamos usar chama Flet.
Para instalar:

```
uv add flet
```

[aguardar — o uv vai baixar e instalar]

Agora vamos ver o que mudou no prontuário:

```
type pyproject.toml
```

[mostrar o conteúdo atualizado]

Olha: `dependencies` agora tem `flet`.
O prontuário foi atualizado automaticamente pelo uv.
Você não tocou no arquivo.

---

Agora veja o que apareceu na pasta:

```
dir
```

[mostrar os novos itens]

Apareceram duas coisas novas: a pasta `.venv` e o arquivo `uv.lock`.

---

A pasta `.venv` é o ambiente virtual.

Vou explicar com a analogia da farmácia, porque é importante.

Imagine que você tem dois projetos no mesmo computador:
o ClinMd-Tribe e um projeto de pesquisa separado.

O ClinMd-Tribe precisa do Flet versão 0.25.
O projeto de pesquisa precisa do Flet versão 0.20.

Se você instalasse tudo no mesmo lugar — no Python geral do Windows —
as versões conflitariam. Interação medicamentosa.

O `.venv` é a solução.

É como o carrinho de medicação do leito 3.
Só tem o que este paciente precisa.
Não mistura com o carrinho do leito 7.

Cada projeto tem o seu próprio `.venv`.
Cada um com as versões certas para aquele projeto.

---

Agora o `uv.lock`. Vamos ler:

```
type uv.lock
```

[mostrar o começo do arquivo]

É um arquivo longo — não precisa ler tudo.
O importante é entender para que serve.

O uv.lock é o registro da dispensação:
remédio X, versão exata Y, de qual fonte Z, qual hash de verificação.

Você não edita esse arquivo. Nunca.
O uv cuida dele.

Mas se você precisar recriar o projeto em outro computador —
ou mandar para um colega — o uv.lock garante que tudo fica idêntico.
Exatamente as mesmas versões, exatamente o mesmo ambiente."

---

## SEÇÃO 7: DEMO — UV RUN — 8 min

**Tom:** Prático — mostrar o que o uv init criou e executar sem escrever nada

"O uv init já criou um `main.py` para você.
Vamos ler o que ele gerou — sem modificar nada:

```
type main.py
```

[mostrar o conteúdo]

O uv init gerou isso por você.
Sem você escrever uma linha.

---

Aqui vale pausar e marcar uma regra do curso.

No curso inteiro: você descreve o que quer, o Claude escreve.
Você lê, revisa, aprova. Nunca digita código.

É assim nas aulas de Python, nas aulas de interface, nas aulas de banco de dados.
O médico supervisiona. O Claude e as ferramentas executam.

---

Agora vamos executar o que o uv criou.

```
uv run python main.py
```

[mostrar o output]

Funcionou.

E perceba: usamos `uv run python main.py` — não `python main.py` diretamente.

Por quê?

Porque o `uv run` garante que o Python que executa é o do ambiente deste projeto —
o carrinho do leito 3, com os remédios certos,
não o estoque geral do hospital.

Regra simples e definitiva:

Dentro do projeto ClinMd-Tribe, todo comando Python começa com `uv run`. Sempre.

O Claude vai fazer isso por você na maioria das vezes.
Mas quando você vir `uv run` no terminal, você vai saber exatamente o que está acontecendo.

Você assina a evolução. Não assina às cegas."

---

## SEÇÃO 8: REFERÊNCIA DE COMANDOS UV — 5 min

**Tom:** Referência — dar o mapa completo antes de encerrar

"Deixa eu dar o mapa completo do uv que você vai usar no curso.

[mostrar na tela]

```
uv init nome-do-projeto    ← cria projeto novo
uv add nome-pacote         ← instala dependência
uv remove nome-pacote      ← remove dependência
uv run python arquivo.py   ← executa Python no projeto
uv sync                    ← instala tudo do pyproject.toml
```

O `uv sync` merece uma explicação especial.

Imagine que você clonou o ClinMd-Tribe em um novo computador.
O código está lá. O pyproject.toml está lá. O uv.lock está lá.
Mas a pasta `.venv` não — ela fica só na sua máquina, não vai para o Git.

Você roda `uv sync` e o uv recria toda a farmácia:
baixa exatamente as versões do uv.lock,
monta o `.venv` igual ao original.

---

Uma dica prática final.

O Claude Code vai usar esses comandos por você.

Quando você pedir para adicionar a calculadora CHA₂DS₂-VASc,
o Claude vai rodar `uv add` se precisar de uma dependência nova,
vai criar arquivos, vai organizar as pastas.

Você não precisa digitar tudo manualmente.

Mas agora você sabe o que acontece quando o Claude diz que fez.
E isso faz toda a diferença."

---

## SEÇÃO 9: ENCERRAMENTO + DEVER DE CASA — 5 min

**Tom:** Resumo do que ficou pronto + dever que reforça o aprendizado + ponte

"Resumo do que ficou pronto hoje.

uv instalado e funcionando.
Projeto ClinMd-Tribe criado com `uv init`.
Flet instalado com `uv add` — primeira dependência do projeto.
pyproject.toml: o prontuário, lido e entendido.
`.venv`: carrinho de medicação isolado para este projeto.
`uv.lock`: registro da dispensação, gerado automaticamente.
`uv run`: a regra que vale para todo o curso.

---

Dever de casa.

Três passos. Uns dez minutos.

Antes de qualquer coisa: pense e escreva numa frase —
o que você acha que vai mudar no pyproject.toml quando rodar `uv add requests`?

Depois rode:

```
uv add requests
type pyproject.toml
```

Veja se a sua previsão bateu.

Agora remova:

```
uv remove requests
type pyproject.toml
```

Veja o que sumiu.

Por último:

```
git status
git diff
```

Você vai ver que o Git rastreou tudo que o uv mexeu.
O pyproject.toml mudou. O uv.lock mudou.
São dois instrumentos que trabalham juntos — você aprendeu os dois.

Tire um print do terminal mostrando a dependência aparecendo e depois sumindo.
É o seu comprovante de que o ambiente está funcionando.

---

Na próxima aula: Python com analogias clínicas.

As estruturas básicas da linguagem, do jeito que você aprendeu anatomia —
um sistema de cada vez.

Sem decorar sintaxe.
Com o contexto clínico que você já tem.

Até lá."

---

**FIM DO ROTEIRO**
```

- [ ] **Step 2: Verificar contra o spec**

| Item do spec | Presente no roteiro? |
|---|---|
| Abertura "você passa de usuário para construtor" | ✓ S1 |
| ClinMd-Tribe reveal (3 funcionalidades + local + LGPD) | ✓ S2 |
| uv: por que existe + analogia farmácia | ✓ S3 |
| `winget install` + alternativa `irm` | ✓ S4 |
| Fechar/reabrir PowerShell + `uv --version` | ✓ S4 |
| `cd $HOME\Documents\projetos` (Windows) | ✓ S4 |
| `uv init clinmd-tribe` + `dir` | ✓ S4 |
| `type pyproject.toml` (leitura, não edição) | ✓ S5 |
| Explicação de cada campo do pyproject.toml | ✓ S5 |
| "Você não edita esse arquivo na mão" | ✓ S5 |
| `uv add flet` + ver pyproject.toml mudar | ✓ S6 |
| `.venv` = carrinho do leito 3 | ✓ S6 |
| `uv.lock` = registro da dispensação | ✓ S6 |
| `type main.py` (sem editar) | ✓ S7 |
| Regra do curso: médico nunca digita código | ✓ S7 |
| `uv run python main.py` + explicação | ✓ S7 |
| Tabela de comandos uv (5 comandos) | ✓ S8 |
| `uv sync` explicado | ✓ S8 |
| Dever: add/remove requests + git status/diff | ✓ S9 |
| Ponte para aula_12 (Python) | ✓ S9 |
| Zero código escrito pelo aluno | ✓ todo o roteiro |
| SO Windows/PowerShell único | ✓ todo o roteiro |
| Plugin/Skills/Agents/MCPs ausentes | ✓ não aparecem |
| Clean Architecture preview ausente | ✓ não aparece |
| claude -c ausente | ✓ não aparece |
| Duração ~48 min | ✓ (2+3+2+8+5+10+8+5+5=48) |

- [ ] **Step 3: Commitar o roteiro**

```bash
git add aula_10/roteiro.md
git commit -m "feat: aula_10 Terminal + uv bisturi digital — fusão 10+11, zero código (~48min)"
```

---

## Task 2: Gerar `aula_10/roteiro.html`

**Files:**
- Create/Overwrite: `aula_10/roteiro.html`

- [ ] **Step 1: Gerar via pandoc**

```bash
pandoc aula_10/roteiro.md -o aula_10/roteiro.html \
  --standalone \
  --metadata title="Aula 10 — Terminal + uv: o Bisturi Digital"
```

Expected: arquivo criado sem erros.

- [ ] **Step 2: Verificar**

```bash
ls -lh aula_10/roteiro.html
```

Expected: arquivo com tamanho > 0.

- [ ] **Step 3: Commitar**

```bash
git add aula_10/roteiro.html
git commit -m "feat: aula_10 roteiro.html gerado

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Task 3: Deprecar `aula_11/roteiro.md`

**Files:**
- Modify: `aula_11/roteiro.md` (substituir pelo aviso de deprecação)

- [ ] **Step 1: Escrever a nota de deprecação**

Conteúdo completo do arquivo:

```markdown
# Aula 11 — Incorporada à Aula 10

> **Esta aula foi fusionada com a aula_10 em 2026-06-08.**

O conteúdo de `uv` (uv add, uv remove, uv run, uv sync, ambiente virtual, pyproject.toml)
foi incorporado à aula_10 conforme S01.01 do `arvore_aulas.html`,
que define esta seção como uma única aula.

**Roteiro completo:** `aula_10/roteiro.md`

---

## Por que a fusão?

- A divisão aula_10/aula_11 não estava no HTML canônico do curso
- Ambas cobriam o mesmo tópico (uv) sem reset de contexto entre elas
- A aula_11 isolada ficava abaixo do alvo de 45-60 min (~40 min)
- Fusionadas: ~48 min, dentro do alvo
```

- [ ] **Step 2: Commitar**

```bash
git add aula_11/roteiro.md
git commit -m "deprecate: aula_11 incorporada à aula_10 (fusão S01.01)

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Task 4: Atualizar `aula_11/roteiro.html`

**Files:**
- Overwrite: `aula_11/roteiro.html`

- [ ] **Step 1: Gerar via pandoc**

```bash
pandoc aula_11/roteiro.md -o aula_11/roteiro.html \
  --standalone \
  --metadata title="Aula 11 — Incorporada à Aula 10"
```

- [ ] **Step 2: Commitar**

```bash
git add aula_11/roteiro.html
git commit -m "deprecate: aula_11 roteiro.html atualizado (nota de fusão)

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Checklist de self-review do plano

- [x] **Spec coverage:** todos os 25 itens verificados na Task 1 Step 2
- [x] **Placeholder scan:** sem TBDs — prompts e comandos reais em todas as seções
- [x] **Zero código:** nenhuma seção do roteiro pede ao aluno que abra editor ou escreva Python
- [x] **Windows/PowerShell:** todos os comandos são `dir`, `type`, `cd $HOME\...`, `winget` — sem `ls`, `cat`, `cd ~/`
- [x] **Fusão limpa:** Plugin/Skills/Agents/MCPs, Clean Arch, claude -c ausentes
- [x] **Analogia coerente:** farmácia → prontuário → remédio → carrinho do leito — consistente do S3 ao S7
- [x] **Dever de casa:** zero código Python, usa Git (espaçamento aulas 08-09), artefato verificável (print)
- [x] **aula_11 deprecada:** nota clara com motivo e ponteiro para aula_10
