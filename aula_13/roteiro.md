# Aula 13 — Flet: Sua Primeira Tela Clínica

**Formato:** Gravada no OBS Studio, editada no Kdenlive  
**Duração:** ~42 min  
**Tom:** Colega com humor leve e didático — momento de revelar a interface do ClinMd-Tribe

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, dentro da pasta do projeto: `cd Documents\projetos\clinmd-tribe` e depois `claude` (é o que a Seção 3 mostra).
- [ ] Projeto `clinmd-tribe` já existente com o uv funcionando e o Flet já instalado (`uv add flet`, feito na aula de Terminal + uv): a aula assume o Flet pronto e todos os `uv run python main.py` dependem disso.
- [ ] Sessão do Claude Code limpa, sem conversa anterior carregada (a demo nasce do primeiro prompt, reescrevendo o `main.py` do zero).
- [ ] Agent `frontend-engineer` instalado e disponível (é invocado na Seção 5.5 com `@frontend-engineer`); confirme que ele responde antes de gravar.
- [ ] Skill `/tab_pendencias` instalada (é chamada no fim da Seção 5.5); confirme que o comando existe nesta sessão.

**Confira antes de gravar:**

- [ ] Ensaie antes os três prompts Flet (janela com identidade TribeMD, botão com evento, calculadora de IMC completa) e confirme que cada `uv run python main.py` ABRE de fato uma janela na sua máquina, esta aula depende da janela gráfica aparecer na captura de tela. Em alguns ambientes o Flet abre no navegador em vez de janela nativa; teste antes para saber onde a janela vai surgir e enquadrar a câmera/captura.
- [ ] Confirme as cores TribeMD que o roteiro pede (`#5213B9` roxo, `#FAFAFA` fundo, `#646C6F` cinza, `#2E3233` texto escuro) aparecem corretas na janela gerada.
- [ ] Teste o caso de erro da calculadora (Seção 5): digite texto onde se espera número e confirme que a mensagem de erro aparece (o Claude costuma adicionar `try/except`), pois o roteiro narra essa validação ao vivo.
- [ ] O `main.py` desta aula é reescrito várias vezes pelos prompts; tudo bem ele já existir do `uv init`, o roteiro manda reescrever. Privacidade (LGPD): peso/altura/nome usados são fictícios, nenhum dado de paciente real.

**Navegador:** nenhum site externo é necessário; observação: dependendo do ambiente, o próprio app Flet pode abrir numa aba do navegador local (não é um site, é o app rodando localmente).

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Virada de página — do terminal para a tela

**[Aviso rápido dos óculos, antes de mergulhar]**

"Última checagem antes de abrir a tela: os óculos. Hoje é dia de janela com cores e botões, mas o código por trás ainda tem hex de cor e nome de campo em letra fina. Ajusta o foco igual quem vai conferir a cor de uma lâmina no microscópio: detalhe importa. Pronto? Primeira tela clínica chegando."

"Na aula passada você entendeu os conceitos básicos de Python.
Variáveis, funções, condições, listas.
Tudo apareceu em texto numa tela preta.

Hoje isso muda.

Você vai pedir ao Claude Code para criar uma janela.
Com botões. Com campos de texto. Com cores.
Com a identidade visual do ClinMd-Tribe.

A biblioteca que torna isso possível se chama Flet.
E você já instalou ela na aula_10 com 'uv add flet'.

Vamos abrir a primeira janela."

---

## SEÇÃO 2: O QUE É FLET (3 min)

**Tom:** Analogia médica — o que Flet faz e por que foi escolhido

"Flet é uma biblioteca Python que cria interfaces gráficas.

Pense assim: você conhece o prontuário em papel versus o PEP.

O prontuário em papel é o Python puro no terminal — funciona,
mas é texto, linha por linha, sem interface.

O PEP é o Flet — o mesmo dado, mas com janelas, abas, cores, botões.
A lógica é a mesma. A apresentação é radicalmente diferente.

Por que Flet e não outras bibliotecas?

Primeira: funciona no Windows, Mac e Linux sem modificar o código.

Segunda: exporta como .exe para Windows. O ClinMd-Tribe vai rodar
com um duplo clique, sem precisar do Python instalado no computador do paciente.

Terceira: a sintaxe que o Claude gera em Flet é legível.
Você vai conseguir ler o código gerado e entender o que cada parte faz."

---

## SEÇÃO 3: HELLO WORLD MÉDICO — PRIMEIRA JANELA (12 min)

**Tom:** Primeiro prompt Flet — explicar o resultado gerado

"Abra o PowerShell, entre na pasta do projeto e abra o Claude Code:

```
cd Documents\projetos\clinmd-tribe
claude
```

Prompt:

```
Crie um arquivo main.py com um app Flet que abre uma janela com o titulo
ClinMd-Tribe. A janela deve ter fundo branco (#FAFAFA) e mostrar dois textos:
o titulo ClinMd-Tribe em roxo (#5213B9), tamanho 32, negrito;
e o subtitulo 'Seu assistente clinico local' em cinza (#646C6F), tamanho 16.
```

[aguardar o Claude gerar o arquivo]

[mostrar o arquivo gerado no terminal]

Agora execute:

```
uv run python main.py
```

[aguardar — uma janela vai abrir]

[mostrar a janela aberta]

Você tem sua primeira janela.

---

Agora leia o código gerado comigo — você precisa reconhecer as partes
para saber o que pedir nas próximas aulas.

**import flet as ft** — importa a biblioteca com o apelido 'ft'.
Em vez de escrever 'flet.Text', você escreve 'ft.Text'.
Como chamar um colega pelo apelido.

**def main(page: ft.Page):** — função principal do app.
O Flet chama essa função quando o app abre.
'page' é a janela — o canvas onde os elementos são colocados.

**page.title** — o texto na barra de título da janela.

**page.bgcolor** — cor de fundo. #FAFAFA é o branco-gelo do TribeMD.

**ft.Text(...)** — um elemento de texto na tela.
'value' é o texto, 'size' é o tamanho, 'color' é a cor.

**page.add(...)** — coloca os elementos na janela, na ordem que você listar.

**ft.app(main)** — inicia o app chamando a função main.

Doze linhas. Janela com identidade visual TribeMD."

---

## SEÇÃO 4: BOTÃO E EVENTO — INTERATIVIDADE (8 min)

**Tom:** Evento clínico — ação que dispara uma resposta

"Uma interface sem interatividade é um cartaz.

Prompt ao Claude Code:

```
No main.py, adicione um botao 'Iniciar sistema' com fundo roxo (#5213B9)
e texto branco. Quando clicar, deve aparecer a mensagem
'Sistema iniciado. Bem-vindo, doutor.' em texto escuro (#2E3233).
```

[aguardar e mostrar o código atualizado]

Execute:

```
uv run python main.py
```

[mostrar — clicar no botão e ver a mensagem aparecer]

---

Leia o padrão no código gerado.

O Claude criou uma função que responde ao clique — isso se chama handler.
Quando o botão é clicado, a função executa, muda o texto e chama page.update()
para a tela redesenhar.

O padrão é sempre o mesmo:

**Evento** — algo acontece: clique, digitação, tecla pressionada.
**Handler** — uma função que responde ao evento.
**Atualização** — page.update() redesenha a tela com as mudanças.

É o ciclo diagnóstico: estímulo, processamento, resposta.
O paciente apresenta o sintoma. Você processa. Você age.

Você não escreveu esse padrão. Mas agora você reconhece quando o Claude usa."

---

## SEÇÃO 5: CALCULADORA DE IMC — PEDINDO AO CLAUDE O APP COMPLETO (12 min)

**Tom:** Síntese — um prompt claro gera um app clínico funcional

"Agora o momento principal da aula.

Você vai pedir ao Claude Code para construir uma calculadora de IMC com interface.
Num único prompt, descrevendo o resultado que quer.

> [CONFERIR CLÍNICO: faixas de IMC do prompt (<18.5 abaixo do peso, 18.5-24.9 normal, 25-29.9 sobrepeso, >30 obesidade) usadas como exemplo. Conferir contra a referência adotada antes de gravar.]

Prompt:

```
Reescreve o main.py como uma calculadora de IMC com interface Flet.
O app deve ter:
- titulo 'ClinMd-Tribe - Calculadora de IMC' na janela
- fundo branco (#FAFAFA) com padding de 30
- campo de texto para Peso em kg
- campo de texto para Altura em metros
- botao 'Calcular IMC' com fundo roxo (#5213B9) e texto branco
- area de resultado que mostra o IMC calculado e a classificacao:
  abaixo de 18.5 abaixo do peso, 18.5 a 24.9 peso normal,
  25 a 29.9 sobrepeso, acima de 30 obesidade
- se o usuario digitar algo que nao e numero, mostrar mensagem de erro
```

[aguardar o Claude gerar o app completo]

Execute:

```
uv run python main.py
```

[mostrar — preencher peso e altura, clicar em Calcular]

[mostrar resultado correto e depois testar com texto para ver o erro]

Você tem uma calculadora de IMC funcional com interface gráfica.

---

Leia o código gerado e reconheça as partes.

Da aula de Python: função de cálculo, função de classificação, if/elif/else, float().

Do Flet: ft.TextField para os campos, ft.ElevatedButton para o botão,
ft.Text para o resultado, page.add, page.update.

E um bloco que o Claude adicionou por conta própria: try/except.

'try' — tente executar.
'except ValueError' — se o usuário digitar texto onde esperava número, faça isso.

É um protocolo de segurança. O Claude adicionou porque é boa prática.
Você validou que funciona — digitou texto e viu a mensagem de erro.
Isso é validar o que o Claude gerou.

Um prompt. Um app clínico completo."

---

## SEÇÃO 5.5: FRONTEND-ENGINEER — VALIDANDO A INTERFACE (2 min)

**Tom:** Consulta especializada — o aluno tem um time técnico disponível

"Você tem uma calculadora de IMC funcional com interface gráfica.

Antes de encerrar: vamos consultar o frontend-engineer para validar
a abordagem e antecipar melhorias.

No Claude Code:

```
@frontend-engineer, construi uma calculadora de IMC em Flet com campos
de texto, botão roxo e área de resultado. A interface funciona mas está
sem layout organizado. Quais são as próximas melhorias de interface
mais importantes para um app clínico?
```

[mostrar a resposta do frontend-engineer]

O frontend-engineer vai listar prioridades de layout —
que é exatamente o que a próxima aula vai resolver.

---

Veja as pendências:

```
/tab_pendencias
```

[mostrar a tabela — layout e arquitetura vão aparecer como próximas tarefas]"

---

## SEÇÃO 6: ENCERRAMENTO (3 min)

**Tom:** Resumo, motivação e o que vem a seguir

"Resumo do que ficou pronto hoje.

Primeira janela Flet criada com cores TribeMD — via prompt ao Claude Code.
Botão com evento e resposta — via prompt.
Calculadora de IMC com interface gráfica completa — via prompt.

Em nenhum momento você abriu um editor e digitou Python.
Você descreveu o que queria. O Claude construiu. Você validou.

Esse é o fluxo do ClinMd-Tribe inteiro.

---

Dever de casa.

Peça ao Claude Code:

```
No main.py da calculadora de IMC, adiciona um campo de texto
para o nome do paciente. Quando calcular, o resultado deve incluir
o nome: por exemplo 'Joao Silva - IMC: 26.8 - Sobrepeso'.
```

Execute. Valide que o nome aparece no resultado.
Se não estiver certo, corrija o prompt e peça de novo.

Na próxima aula: layout. Você vai ver que a calculadora está funcional
mas visualmente desorganizada — e vai pedir ao Claude para deixá-la
com cara de software profissional.

Até lá."

---

**FIM DO ROTEIRO**
