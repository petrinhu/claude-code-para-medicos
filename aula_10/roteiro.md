# Aula 10 — Terminal + uv: o Bisturi Digital

**Formato:** Gravada no OBS Studio, editada no Kdenlive  
**Duração:** ~48 min  
**Tom:** Colega com humor leve e didático — "você passa de usuário para construtor"  
**Módulo:** S01.01 — Fundação da Fase Avançada  
**SO:** Windows/PowerShell (padrão único do curso)  

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Aberto e pronto:**

- [ ] PowerShell aberto e limpo (esta aula é toda no PowerShell; o Claude Code é só citado, não usado nas demos).
- [ ] Pasta `Documents\projetos` já criada (foi pedida na aula de abertura): a Seção 4 entra nela com `cd $HOME\Documents\projetos`. Se não existir, crie antes para o `cd` não falhar na câmera.
- [ ] Garanta que `clinmd-tribe` ainda NÃO existe dentro de `projetos` (apague se sobrou de um teste): o `uv init clinmd-tribe` da Seção 4 precisa criar a pasta do zero, e o `type pyproject.toml` da Seção 5 deve mostrar `dependencies = []` antes do primeiro `uv add`.
- [ ] Decida se grava a instalação do uv (Seção 4): se o uv já estiver instalado, o `winget install` não roda igual. Para gravar a instalação completa, use uma máquina/usuário sem uv; para pular, deixe instalado e foque no `uv --version`.

**Confira antes de gravar:**

- [ ] Teste antes, numa pasta de rascunho, o fluxo inteiro (`uv init`, `type pyproject.toml`, `uv add flet`, `dir`, `type uv.lock`, `uv run python main.py`), para confirmar cada saída. O primeiro `uv add flet` baixa pacotes da internet e pode demorar: garanta conexão estável e, se quiser, deixe o cache do uv já populado para o download sair rápido na gravação.
- [ ] Confirme que o `dir` na Seção 4 mostra exatamente os três arquivos descritos (`.python-version`, `main.py`, `pyproject.toml`) e que, após o `uv add flet` na Seção 6, aparecem a pasta `.venv` e o `uv.lock`, como o roteiro narra.
- [ ] Se o `winget` não estiver disponível na sua máquina, tenha o comando alternativo (`irm https://astral.sh/uv/install.ps1 | iex`) já testado, para não improvisar diante da câmera.
- [ ] Lembre que após instalar o uv é preciso FECHAR e abrir um novo PowerShell para o `uv --version` reconhecer o comando, como o roteiro avisa; tenha esse segundo PowerShell pronto.

**Navegador:** nenhum site é necessário nesta aula (a instalação do uv é por comando no PowerShell, não por download manual no navegador).

---

## SEÇÃO 1: ABERTURA — 2 min

**Tom:** Virada de página — a fase avançada começa aqui

**[Aviso rápido dos óculos, antes de mergulhar]**

"Recado de pré-consulta: ajuste os óculos antes da gente abrir o terminal. Hoje vai ter saída de instalação rolando rápido na tela, nome de pacote, número de versão, e essas letrinhas são finas que nem cateter. Vista o foco certo agora pra não perder nenhum sinal vital do uv."

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

| Comando | O que faz |
|---|---|
| `uv init nome` | Cria projeto novo |
| `uv add pacote` | Instala dependência |
| `uv remove pacote` | Remove dependência |
| `uv run python arquivo.py` | Executa no ambiente do projeto |
| `uv sync` | Reinstala tudo a partir do pyproject.toml |

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
