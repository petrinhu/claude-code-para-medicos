# Aula 14 — Layout Flet: Do Caos à Clareza Clínica

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~42 min  
**Tom:** Colega com humor leve e didático — transformar o funcional em profissional

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Diagnóstico visual — a calculadora funciona mas não impressiona

"Na aula passada você criou uma calculadora de IMC com interface gráfica.

Ela funciona. Calcula correto. Trata o erro de entrada.

Mas se você abrir ela agora e mostrar para um colega médico,
ele vai dizer: 'isso parece um software dos anos 90.'

Os elementos estão colados. Sem margem. Sem organização.
É como um prontuário em papel amassado na gaveta — os dados estão lá,
mas a apresentação compromete a credibilidade.

Hoje você vai pedir ao Claude Code para transformar essa tela.
Cinco prompts. Cinco conceitos de layout.
O mesmo app, mas com cara de software profissional.

Vamos lá."

---

## SEÇÃO 2: COLUMN COM SPACING — O ESPAÇO QUE ORGANIZA (8 min)

**Tom:** Conceito central de layout vertical — o esqueleto da interface

"Primeiro conceito: Column.

Você conhece a lista de problemas do PEP — Prontuário Eletrônico do Paciente.
Cada problema na sua linha. Espaçados. Um embaixo do outro, com respiro visual.

No Flet, Column é exatamente isso: um container que empilha elementos
verticalmente, com espaço controlado entre eles.

O problema visual na sua calculadora agora:
os campos, o botão e o resultado estão amontoados sem respiro.
Parece uma lista de tarefas sem espaçamento — denso, sufocante.

Prompt ao Claude Code:

```
No main.py da calculadora de IMC, organiza todos os elementos
dentro de uma ft.Column com spacing=15 e horizontal_alignment
centralizado na tela. Mantém a lógica de cálculo intacta.
```

[aguardar o Claude atualizar o arquivo]

Execute:

```
uv run python main.py
```

[mostrar — os elementos agora têm espaço entre eles]

---

Leia o código gerado comigo.

O Claude envolveu os elementos em `ft.Column(controls=[...], spacing=15,
horizontal_alignment=ft.CrossAxisAlignment.CENTER)`.

`controls` — a lista de elementos filhos da Column.
`spacing=15` — 15 pixels de espaço entre cada filho.
`horizontal_alignment` — centraliza os filhos no eixo horizontal.

Note: spacing é o espaço ENTRE os filhos.
Não é o espaço interno de cada elemento. Isso vem no próximo conceito.

A Column com spacing resolveu o problema do amontoamento.
Mas os elementos ainda encostam na borda da janela."

---

## SEÇÃO 3: CONTAINER COM PADDING — A MARGEM DO RECEITUÁRIO (7 min)

**Tom:** Conceito de respiro interno — a caixa que dá ar ao conteúdo

"Segundo conceito: Container com padding.

Você usa receituário? Aquela margem branca em volta do conteúdo —
ela existe para que o texto não encoste na borda do papel.
O conteúdo respira. A leitura é confortável.

Container no Flet é a moldura com margem interna.
Padding é o tamanho dessa margem.

O problema visual agora: a Column está no canto da janela,
sem respiro nas bordas. Parece um formulário sem moldura.

Prompt ao Claude Code:

```
No main.py, envolve a Column da calculadora num ft.Container
com padding=30 e bgcolor='#FFFFFF'. Centraliza o Container
na tela usando expand=True na page.
```

[aguardar e mostrar o resultado]

Execute:

```
uv run python main.py
```

[mostrar — a calculadora agora tem margem interna, respira]

---

Leia o código gerado comigo.

`ft.Container(content=coluna, padding=30, bgcolor='#FFFFFF')` —
content é o que está dentro, padding é a margem interna em todos os lados.

Perceba a diferença:
`padding` = ar dentro da caixa, entre a borda e o conteúdo.
`spacing` da Column = ar entre os filhos.

Não são a mesma coisa. Confundir os dois é o erro mais comum em layout Flet.

A calculadora já está melhor. Mas ainda parece uma caixa flutuando no nada.
Falta elevação, falta moldura."

---

## SEÇÃO 4: CARD — O PRONTUÁRIO COM MOLDURA (6 min)

**Tom:** Componente de destaque visual — elevação e identidade

"Terceiro conceito: Card.

Prontuário impresso versus prontuário projetado na parede.
O impresso tem papel, borda, elevação física — destaca do fundo.

Card no Flet é isso: um Container com elevação (sombra sutil)
e cantos arredondados. Destaca o conteúdo do background da janela.

O problema visual agora: o Container está lá,
mas sem elevação ele some no fundo branco da janela.

Prompt ao Claude Code:

```
No main.py, substitui o ft.Container que envolve a calculadora
por um ft.Card com elevation=2 e shape com border_radius de 12.
Dentro do Card, coloca um ft.Container com padding=20
para manter o respiro interno.
```

[aguardar e mostrar]

Execute:

```
uv run python main.py
```

[mostrar — o Card aparece destacado do fundo com sombra sutil e cantos arredondados]

---

Leia o código gerado comigo.

`ft.Card(elevation=2, shape=ft.RoundedRectangleBorder(radius=12), content=...)`

`elevation=2` — sombra sutil que destaca do fundo. Não é pesada, é discreta.
`border_radius=12` — cantos arredondados. Dá leveza ao componente.

A armadilha: Card não tem padding automático.
Se você colocar o conteúdo direto no Card, ele encosta nas bordas do Card.
Por isso o Claude colocou um `ft.Container(padding=20)` dentro do Card —
o Container cuida do respiro, o Card cuida da elevação.

Card resolve o destaque visual. Mas os campos de Peso e Altura
ainda estão empilhados quando poderiam estar lado a lado."

---

## SEÇÃO 5: ROW — A LINHA DE SINAIS VITAIS (8 min)

**Tom:** Layout horizontal — o que fica lado a lado

"Quarto conceito: Row.

Você olha para uma planilha de sinais vitais: PA, FC, FR, SpO₂.
Todos na mesma linha — não empilhados. Lado a lado, cada um no seu espaço.

Row no Flet é a Column virada de lado: empilha elementos horizontalmente.

O problema visual agora: Peso e Altura estão um embaixo do outro,
ocupando altura desnecessária. Num formulário real, estariam lado a lado.

Prompt ao Claude Code:

```
No main.py, coloca os campos de Peso e Altura lado a lado
numa ft.Row com spacing=10. Cada campo deve ter expand=True
para dividir o espaço igualmente.
```

[aguardar e mostrar]

Execute:

```
uv run python main.py
```

[mostrar — Peso e Altura lado a lado, cada um ocupando metade do espaço]

---

Leia o código gerado comigo.

`ft.Row(controls=[campo_peso, campo_altura], spacing=10)`
Cada `ft.TextField` com `expand=True`.

A armadilha do `expand=True`: sem ele, os campos ficam espremidos
ou saem da tela. `expand=True` diz ao Flet: 'divide o espaço disponível
igualmente entre os filhos que têm expand.'

Sem expand → campos espremidos no tamanho mínimo.
Com expand → cada campo ocupa metade do espaço da Row.

É o mesmo princípio de uma tabela HTML com colunas de largura igual.
Você não especifica a largura exata — você diz que cada um expande.

A calculadora está tomando forma. Mas ainda falta identidade visual no topo.
Não tem nada que diga 'isso é o ClinMd-Tribe'."

---

## SEÇÃO 6: APPBAR — O TIMBRE DO RECEITUÁRIO (5 min)

**Tom:** Identidade no topo — o cabeçalho que identifica o sistema

"Quinto e último conceito: AppBar.

Receituário médico tem timbre no topo: nome do médico, CRM, especialidade.
Identifica de quem é o documento antes mesmo de ler o conteúdo.

AppBar no Flet é o timbre da janela: barra fixa no topo,
com o nome do app e a cor de identidade visual.

O problema visual agora: a janela não tem identidade.
O título aparece na barra de título do Windows, pequeno e sem cor.
Não tem nada que identifique o ClinMd-Tribe ao abrir.

Prompt ao Claude Code:

```
No main.py, adiciona um ft.AppBar com title 'ClinMd-Tribe',
bgcolor='#5213B9' e title_color='#FFFFFF'.
Define também page.bgcolor='#E5E9EA' para o fundo da janela
ficar cinza-claro e o Card se destacar mais.
```

[aguardar e mostrar]

Execute:

```
uv run python main.py
```

[mostrar — AppBar roxo com 'ClinMd-Tribe' em branco no topo,
fundo cinza-claro, Card branco se destacando]

---

Leia o código gerado comigo.

`page.appbar = ft.AppBar(title=ft.Text('ClinMd-Tribe', color='#FFFFFF'),
bgcolor='#5213B9')`

O AppBar é atribuído diretamente à `page.appbar` —
não vai dentro do `page.add()`, vai como propriedade da página.

`#5213B9` é o roxo primário do TribeMD.
`#E5E9EA` é o cinza de fundo da seção — cria contraste com o Card branco.

Cinco prompts. A mesma calculadora de IMC da aula passada,
agora com cara de software profissional."

---

## SEÇÃO 6.5: TIME DE DESIGN — VALIDANDO O LAYOUT (2 min)

**Tom:** Consulta ao especialista — o designer valida, o aluno aprende

"Você aplicou cinco conceitos de layout.

Antes de encerrar: vamos consultar o UX designer do time.

No Claude Code:

```
@ux-ui-designer, apliquei Column com spacing, Container com padding,
Card com elevation, Row com expand e AppBar roxo na calculadora de IMC.
A interface está funcional. O que mais pode melhorar a experiência
do médico que vai usar esse app no consultório?
```

[mostrar a resposta do UX designer]

O designer vai sugerir melhorias de usabilidade clínica — tipografia,
espaçamento, hierarquia visual, estados de feedback.
Guarde as sugestões: elas vão aparecer no módulo de polimento final.

---

Atualize as pendências:

```
/tab_pendencias
```

[mostrar a tabela — layout concluído, Clean Architecture como próxima grande tarefa]"

---

## SEÇÃO 7: ENCERRAMENTO (3 min)

**Tom:** Resumo, motivação e dever de casa

"Resumo do que ficou pronto hoje.

Cinco conceitos de layout, cinco prompts ao Claude Code:

Column com spacing — organiza verticalmente com respiro.
Container com padding — cria margem interna.
Card com elevation — destaca o conteúdo com sombra e bordas arredondadas.
Row com expand — coloca elementos lado a lado com divisão igual.
AppBar — identidade visual fixa no topo com as cores TribeMD.

Em nenhum momento você abriu o main.py para editar.
Você descreveu o que queria. O Claude organizou. Você validou.

---

Dever de casa.

Peça ao Claude Code:

```
Cria um novo arquivo chamado cartao_paciente.py.
O app deve ter:
- AppBar com titulo 'ClinMd-Tribe - Cartão do Paciente',
  bgcolor #5213B9 e texto branco
- page.bgcolor '#E5E9EA'
- Um Card centralizado com elevation 2 e cantos de 12
- Dentro do Card: nome do paciente (TextField), idade (TextField)
- Uma Row com dois campos lado a lado: PA sistólica e FC
- Um texto de resultado abaixo, inicialmente vazio
- Um botão 'Registrar' roxo que ao clicar mostra um resumo
  com nome, idade, PA e FC
```

Execute com `uv run python cartao_paciente.py` e valide.

Esse exercício usa os cinco conceitos da aula em um contexto novo —
sem lógica clínica nova, só layout.

Na próxima aula: arquitetura. Você vai entender por que o ClinMd-Tribe
tem quatro camadas separadas e como o código vai se organizar
conforme o projeto cresce.

Até lá."

---

**FIM DO ROTEIRO**
