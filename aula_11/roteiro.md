# Aula 11 — uv: A Farmácia do Seu Projeto

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~40 min  
**Tom:** Colega com humor leve e didático — construindo sobre o projeto criado na aula_10

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Direto, contextualizando onde estamos

"Na aula passada você instalou o ambiente completo — plugins, agents, MCPs —
e criou o projeto ClinMd-Tribe com um único comando:

```
uv init clinmd-tribe
```

O uv criou três arquivos. Você viu eles aparecer no terminal.

Mas não entendemos ainda o que o uv realmente faz.

Hoje a gente vai abrir a farmácia e entender como ela funciona.

Porque nas próximas aulas, quando o Claude Code começar a construir
o ClinMd-Tribe, ele vai usar o uv para instalar cada 'remédio' que o projeto precisa.

Você vai precisar entender o que está acontecendo."

---

## SEÇÃO 2: TOUR PELO PROJETO (5 min)

**Tom:** Didático — abrindo o pyproject.toml e entendendo cada linha

"Abra o PowerShell e entre na pasta do projeto:

```
cd Documents\projetos\clinmd-tribe
```

Liste os arquivos:

```
dir
```

Você vê três arquivos. Vamos abrir o mais importante.

---

Abra o pyproject.toml no Notepad:

```
notepad pyproject.toml
```

[mostrar o arquivo aberto]

O arquivo tem este conteúdo:

```toml
[project]
name = 'clinmd-tribe'
version = '0.1.0'
description = 'Add your description here'
requires-python = '>=3.11'
dependencies = []
```

Leia como um prontuário básico:

**name** — nome do projeto. É a identidade.
**version** — 0.1.0 significa: versão inicial, ainda em desenvolvimento.
**requires-python** — o projeto precisa de Python 3.11 ou mais novo.
**dependencies** — a lista de remédios que o projeto precisa. Está vazia agora.

Esse arquivo é o prontuário do ClinMd-Tribe.
Tudo que você instalar vai aparecer aqui."

---

## SEÇÃO 3: UV ADD — INSTALANDO A PRIMEIRA DEPENDÊNCIA (10 min)

**Tom:** Prático — primeiro remédio do projeto

"O ClinMd-Tribe vai ter interface gráfica.
Para isso, vamos usar uma biblioteca chamada Flet.

Biblioteca em programação é como um medicamento já pronto.
Você não fabrica o ibuprofeno na sua cozinha. Você compra na farmácia.

Flet é o ibuprofeno da interface gráfica — alguém já fez o trabalho duro,
você só usa.

Para instalar o Flet no projeto, o comando é:

```
uv add flet
```

[executar e mostrar o resultado]

Olha o que aconteceu.

O uv foi até a farmácia online — o repositório PyPI —
buscou o pacote Flet, baixou, instalou dentro do projeto.

E atualizou o pyproject.toml automaticamente.

[mostrar o pyproject.toml atualizado]

Agora dependencies tem 'flet'. O prontuário foi atualizado.

---

Também foi criado um arquivo novo: uv.lock.

Abra:

```
notepad uv.lock
```

[mostrar rapidamente]

O lock file é o registro detalhado de exatamente qual versão de cada remédio
foi dispensado. Se o projeto precisar ser recriado no computador de outro médico,
o uv.lock garante que as versões serão idênticas.

É como o registro da dispensação: remédio X, lote Y, validade Z.

Você não precisa editar esse arquivo nunca. O uv cuida dele.

---

Antes de seguir: vamos consultar o Caetano — nosso CTO virtual.

No Claude Code:

```
@caetano-cto, acabei de instalar o Flet com uv add flet para o ClinMd-Tribe.
Essa é a escolha técnica certa para um app clínico local em Windows?
Tem alguma dependência adicional que você recomenda para esta fase inicial?
```

[mostrar a resposta do Caetano]

O Caetano vai confirmar a escolha e pode recomendar dependências adicionais.
Você não precisa tomar essa decisão técnica sozinho — tem um CTO disponível
para consultar antes de cada passo."

---

## SEÇÃO 4: AMBIENTE VIRTUAL — O QUE É E POR QUE IMPORTA (5 min)

**Tom:** Conceito importante explicado com analogia

"Quando você rodou 'uv add flet', o uv não instalou o Flet no seu Windows inteiro.

Ele instalou dentro de uma pasta escondida chamada '.venv', que fica dentro do projeto.

Por que isso?

Imagine que você atende dois tipos de pacientes:
cardíacos e psiquiátricos.

Para cardíacos você usa uma dose de betabloqueador.
Para psiquiátricos você usa outra dose de betabloqueador, em concentração diferente.

Se você misturar tudo num único armário sem separação, vira confusão.

Ambiente virtual é a separação dos armários.

Cada projeto tem a sua própria pasta de dependências.
O ClinMd-Tribe usa Flet versão X.
Outro projeto seu pode usar Flet versão Y.
Os dois coexistem sem conflito.

Você não precisa criar o ambiente virtual manualmente.
O uv faz isso automático quando você roda 'uv add' pela primeira vez."

---

## SEÇÃO 5: UV RUN — EXECUTANDO O PROJETO (8 min)

**Tom:** Prático — primeiro teste do ambiente

"O projeto tem um arquivo chamado main.py.
Vamos abrir e editar ele.

```
notepad main.py
```

O arquivo está vazio (ou tem uma linha de exemplo). Substitua tudo com:

```python
print('ClinMd-Tribe iniciado com sucesso')
```

Salve e feche o Notepad.

Agora execute:

```
uv run python main.py
```

[mostrar o resultado]

Apareceu 'ClinMd-Tribe iniciado com sucesso' no terminal.

Você executou o primeiro código Python do ClinMd-Tribe.

---

Por que 'uv run' e não só 'python main.py'?

'python main.py' usa o Python do Windows — que pode não ter o Flet instalado.
'uv run python main.py' usa o Python do ambiente virtual do projeto — que tem tudo instalado.

Regra: sempre use 'uv run' para executar qualquer coisa dentro do projeto.

É como prescrever: você não usa o armário genérico do hospital,
você usa o armário deste paciente específico."

---

## SEÇÃO 6: COMANDOS UV — RESUMO PRÁTICO (5 min)

**Tom:** Referência, tabela mental

"Deixa eu dar o mapa completo do uv que você vai usar no curso.

```
uv init nome-do-projeto    ← cria projeto novo
uv add nome-pacote         ← instala dependência
uv remove nome-pacote      ← remove dependência
uv run python arquivo.py   ← executa Python no projeto
uv sync                    ← instala todas as dependências do pyproject.toml
```

O 'uv sync' é útil quando você clona o projeto de outro computador.
Você baixa o código, roda 'uv sync', e o uv instala tudo que está no pyproject.toml.
Farmácia de volta ao estado correto.

---

Uma dica prática: o Claude Code vai usar esses comandos por você.

Quando você pedir ao Claude Code para 'adicionar a calculadora CHA2DS2-VASc',
ele vai rodar 'uv add' se precisar de uma dependência nova,
vai criar arquivos .py, vai organizar as pastas.

Você não precisa digitar todos esses comandos manualmente.
Mas precisa entender o que acontece quando o Claude diz que fez.

Você assina a evolução, não assina às cegas."

---

## SEÇÃO 7: ENCERRAMENTO (2 min)

**Tom:** Resumo e ponte para Python

"Resumo do que ficou pronto hoje.

uv add flet — primeira dependência instalada.
pyproject.toml atualizado — prontuário do projeto completo.
uv.lock criado — registro da dispensação.
main.py executado com 'uv run' — primeiro código rodando.

O projeto ClinMd-Tribe tem agora:
— Versionamento Git ativo
— Dependência Flet instalada
— Ambiente virtual configurado
— Código rodando

O campo operatório está completo.

---

Dever de casa.

Rode 'uv add requests' — instala uma biblioteca de acesso à internet.
Depois rode 'uv remove requests' — remove ela.
Abra o pyproject.toml depois de cada comando e veja o que muda.

O objetivo é ver o prontuário sendo atualizado em tempo real.

Na próxima aula, Python com analogias clínicas — as estruturas básicas da linguagem
do jeito que você aprendeu anatomia: um sistema de cada vez.

---

Antes de fechar: veja as pendências do projeto.

```
/tab_pendencias
```

[mostrar a tabela — vai listar Flet instalado como concluído e
Python + interface como próximas tarefas]

Até lá."

---

**FIM DO ROTEIRO**
