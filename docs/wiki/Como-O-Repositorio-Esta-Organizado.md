# Como o repositório está organizado

Esta página é um **passeio guiado pelas pastas e arquivos** deste projeto. A ideia é que, ao terminar de ler, você consiga abrir o repositório e saber o que é cada coisa, sem se sentir perdido.

> Lembrete rápido: **repositório** é a pasta do projeto inteiro, com todos os arquivos e o histórico de mudanças. Se algum termo abaixo soar estranho, a página [[Glossario]] tem todos eles explicados.

Pense nisto como conhecer um hospital novo: primeiro alguém te mostra onde fica a recepção, os consultórios, o laboratório e o arquivo. Depois você circula sozinho com tranquilidade.

## A planta baixa, de relance

```
claude-code-para-medicos/
├── README.md              <- apresentação curta do projeto
├── CLAUDE.md              <- instruções internas do projeto (para a IA)
├── TODO.md                <- a lista oficial das aulas e seu status
├── SECURITY.md            <- como reportar uma falha de segurança
├── arvore_aulas.html      <- mapa visual das aulas (abre no navegador)
├── aula_01/ ... aula_42/  <- uma pasta por aula, com o roteiro
├── aula_abertura/         <- a aula de abertura do curso
├── aulas/                 <- organização das aulas por fase e módulo
├── clinmd_tribe/          <- o aplicativo de exemplo (gabarito do instrutor)
├── docs/                  <- documentos do projeto (incluindo esta wiki)
└── resources/             <- imagens e arquivos de apoio
```

Agora vamos cômodo por cômodo.

## Os arquivos da entrada (a recepção)

Esses ficam soltos na **raiz** do projeto (a "raiz" é a pasta principal, a primeira que você abre, antes de entrar em qualquer subpasta). Eles ficam logo na entrada porque são a porta de entrada do projeto.

### `README.md`
O **cartão de visitas** do repositório. Em quase todo projeto, o arquivo chamado README (em inglês, "leia-me") é a primeira coisa que se lê: um resumo do que o projeto é e como começar. O `.md` no final indica que está escrito em Markdown (texto simples formatado). Veja o [README.md](../../README.md) na raiz.

### `CLAUDE.md`
Um arquivo de **instruções internas**, escrito para orientar o próprio Claude Code quando ele trabalha neste projeto. Define o tom das aulas, o público-alvo (médicos iniciantes em tecnologia), as ferramentas usadas na fase avançada e as regras de ensino. Você pode lê-lo por curiosidade, mas ele é mais um "manual de bordo" para a IA do que material de aula. Está em [CLAUDE.md](../../CLAUDE.md).

### `TODO.md`
A **lista oficial de todas as aulas**, com o status de cada uma (concluída, pendente, a refatorar), a fase a que pertence e a ordem em que aparecem. "TODO" é inglês para "a fazer". Este é o documento que manda: quando há dúvida sobre quantas aulas existem ou em que ordem, a resposta está aqui. Veja [TODO.md](../../TODO.md).

### `SECURITY.md`
Explica **como avisar, com sigilo, se alguém encontrar uma falha de segurança** no projeto. É uma boa prática de qualquer repositório público. Veja [SECURITY.md](../../SECURITY.md).

### `arvore_aulas.html`
Um **mapa visual do curso, feito para abrir no navegador** (por isso termina em `.html`). Para vê-lo, basta dar dois cliques no arquivo e ele abre no Chrome, Firefox ou Safari, mostrando a árvore completa das aulas de forma bonita, com as cores da identidade TribeMD (o roxo `#5213B9`). Você também pode [ver a árvore renderizada online aqui](https://htmlpreview.github.io/?https://github.com/petrinhu/claude-code-para-medicos/blob/main/arvore_aulas.html), sem baixar nada.

## As pastas de aula (os consultórios)

Esta é a maior parte do repositório, e o coração do material didático.

### `aula_01/`, `aula_02/`, ..., `aula_42/`
Cada aula do curso tem **a sua própria pasta**. Dentro de cada uma, você encontra o mesmo par de arquivos:

- `roteiro.md` - o roteiro da aula **em Markdown** (texto puro, fácil de editar). É o conteúdo escrito da aula: a fala, as seções, os comandos.
- `roteiro.html` - o **mesmo roteiro, mas em formato de página** para abrir no navegador, formatado e agradável de ler.

> Você vai notar que a numeração vai até `aula_42`, mas o curso tem 40 aulas. Não falta nada: a numeração pula alguns números porque aulas foram **condensadas** ou fundidas (combinadas em um único encontro mais longo, de 45 a 60 minutos cada). Essas 40 aulas cobrem os **52 tópicos** do currículo. A lista oficial em [TODO.md](../../TODO.md) mostra exatamente como tudo se distribui pelas pastas.

### Por que existem dois arquivos (`.md` e `.html`) para cada aula?
Boa pergunta, e a resposta mostra uma ideia bonita do projeto: **escreve-se uma vez, publica-se de duas formas**.

O roteiro é escrito uma única vez, em Markdown (`roteiro.md`), que é leve e fácil de revisar. Depois, um programa chamado **pandoc** converte automaticamente esse Markdown na versão `.html` formatada. O conteúdo é o mesmo; o pandoc só muda a roupagem.

A vantagem é evitar trabalho duplicado e evitar erros: o instrutor edita só o Markdown, e a versão visual é gerada a partir dele. É como ter um único prontuário-fonte do qual saem tanto a via impressa quanto a via digital, sempre idênticas.

> Termo do [[Glossario]]: **pandoc** é um conversor de documentos. Ele pega o `.md` e produz o `.html` sem ninguém refazer nada à mão.

### `aula_abertura/`
A **aula de boas-vindas do curso**, que apresenta o instrutor, desmistifica a inteligência artificial e dá o tom do que vem pela frente. Ela existe fora da numeração porque é uma introdução especial, não uma das 40 aulas regulares. Segue o mesmo padrão `roteiro.md` + `roteiro.html`.

### `aulas/`
Uma pasta que **organiza as aulas por fase e por módulo**, com pequenos arquivos de apoio (README) que explicam cada agrupamento. Ajuda a enxergar o curso pela lógica das fases (iniciante, intermediário, avançado), enquanto as pastas `aula_NN/` guardam o conteúdo de cada encontro. A página [[O-Curso]] explica essa divisão em fases com calma.

## O aplicativo de exemplo (o laboratório)

### `clinmd_tribe/`
Aqui mora o **ClinMd-Tribe**, o aplicativo clínico que serve de gabarito do instrutor na fase avançada. É um programa de verdade, que funciona, com calculadoras clínicas e testes automatizados. Tem inclusive um README próprio em [clinmd_tribe/README.md](../../clinmd_tribe/README.md).

Como esta pasta merece uma explicação detalhada (incluindo o passo a passo para rodar os testes você mesmo), dedicamos uma página inteira a ela: **[[O-App-ClinMd-Tribe]]**.

## Os documentos e a wiki (o arquivo médico)

### `docs/`
A pasta de **documentos do projeto**. Aqui ficam decisões, planos e a própria wiki que você está lendo agora. Dois itens valem destaque:

- `docs/decisoes_curriculo.md` - um **registro das decisões sobre o currículo** do curso (por exemplo: por que tal aula absorveu tal conteúdo). É a fonte oficial dessas decisões; a página [[O-Curso]] aponta para ele em vez de repetir o conteúdo, para que exista uma só verdade num só lugar.
- `docs/wiki/` - é **onde estas páginas de wiki vivem** dentro do repositório, antes de serem publicadas. A página [[Como-Publicar-Esta-Wiki]] explica como levá-las para o ar.

## Os apoios (almoxarifado de recursos)

### `resources/`
Pasta de **imagens e arquivos de apoio** usados nos materiais (logotipos, máscaras de gravação, ícones). Nada que você precise mexer; é o almoxarifado de recursos visuais do projeto.

## E os arquivos que começam com ponto?

Você pode notar nomes como `.git`, `.gitignore` ou `.claude`. O ponto no começo marca **arquivos e pastas de configuração**, que ficam meio escondidos porque servem ao funcionamento interno, não ao conteúdo. Os principais:

- `.git/` - é onde o **git guarda todo o histórico** do projeto (o "prontuário" de mudanças). Nunca se mexe nisso à mão.
- `.gitignore` - uma **lista de coisas que o git deve ignorar** (arquivos temporários que não fazem parte do projeto).

Você não precisa abrir nem entender esses arquivos para aproveitar o curso. Eles cuidam dos bastidores.

## Em resumo

- Os **arquivos da raiz** (`README`, `TODO`, `CLAUDE`, `SECURITY`, os dois `.html`) são a recepção: apresentam e organizam o todo.
- As **pastas `aula_NN/`** são o coração: cada aula com seu roteiro em Markdown e a versão para navegador, gerada pelo pandoc.
- A pasta **`clinmd_tribe/`** é o aplicativo de exemplo, detalhado em [[O-App-ClinMd-Tribe]].
- A pasta **`docs/`** guarda documentos e esta wiki.

Com esse mapa na cabeça, você circula pelo repositório sem se perder. Próxima parada sugerida: [[O-Curso]], para entender a lógica pedagógica por trás de tudo isso.
