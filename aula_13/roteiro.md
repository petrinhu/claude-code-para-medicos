# Aula 13 — Flet: Sua Primeira Tela Clínica

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~42 min  
**Tom:** Colega com humor leve e didático — momento de revelar a interface do ClinMd-Tribe

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Virada de página — do terminal para a tela

"Nas últimas aulas você escreveu Python no terminal.
Variáveis, funções, condições, listas.
Tudo apareceu em texto numa tela preta.

Hoje isso muda.

Hoje você vai criar uma janela. Com botões. Com campos de texto.
Com cores. Com a identidade visual do ClinMd-Tribe.

Em Python. Sem instalar nada além do que já está instalado.

A biblioteca que vai fazer isso se chama Flet.
E você já instalou ela na aula_11 com 'uv add flet'.

Vamos abrir a primeira janela."

---

## SEÇÃO 2: O QUE É FLET (3 min)

**Tom:** Analogia médica — o que Flet faz e por que foi escolhido

"Flet é uma biblioteca Python que cria interfaces gráficas.

Pense numa analogia: você conhece o prontuário em papel versus o PEP.

O prontuário em papel é o Python puro no terminal — funciona,
mas é texto, linha por linha, sem interface.

O PEP é o Flet — o mesmo dado, mas com janelas, abas, cores, botões.
A lógica é a mesma. A apresentação é radicalmente diferente.

Por que Flet e não outras bibliotecas?

Três razões.

Primeira: funciona no Windows, Mac e Linux sem modificar o código.
Você desenvolve uma vez, roda em qualquer sistema.

Segunda: exporta como .exe para Windows. O ClinMd-Tribe vai rodar
com um duplo clique, sem precisar do Python instalado.

Terceira: a sintaxe é legível. Você vai ver agora e vai entender."

---

## SEÇÃO 3: HELLO WORLD MÉDICO — PRIMEIRA JANELA (12 min)

**Tom:** Mão na massa — cada linha explicada com analogia

"Abra o PowerShell, entre na pasta do projeto:

```
cd Documents\projetos\clinmd-tribe
```

Abra o main.py no Notepad:

```
notepad main.py
```

Apague o conteúdo anterior e substitua por:

```python
import flet as ft

def main(page: ft.Page):
    page.title = 'ClinMd-Tribe'
    page.bgcolor = '#FAFAFA'

    titulo = ft.Text(
        value='ClinMd-Tribe',
        size=32,
        weight=ft.FontWeight.BOLD,
        color='#5213B9'
    )

    subtitulo = ft.Text(
        value='Seu assistente clinico local',
        size=16,
        color='#646C6F'
    )

    page.add(titulo, subtitulo)

ft.app(main)
```

Salve. Execute:

```
uv run python main.py
```

[aguardar — uma janela vai abrir]

[mostrar a janela aberta]

Você criou sua primeira janela.

---

Agora leia o código linha por linha.

**import flet as ft** — importa a biblioteca. 'as ft' é um apelido.
Em vez de escrever 'flet.Text', você escreve 'ft.Text'.
Como chamar um colega pelo apelido em vez do nome completo.

**def main(page: ft.Page):** — função principal do app.
O Flet chama essa função quando o app abre.
'page' é a janela — o canvas onde você vai colocar os elementos.

**page.title** — o título que aparece na barra da janela.

**page.bgcolor** — cor de fundo. Usamos #FAFAFA — o fundo do TribeMD.

**ft.Text(...)** — um elemento de texto na tela.
value é o texto. size é o tamanho. weight é o peso (bold = negrito).
color é a cor — usamos #5213B9, o roxo do TribeMD.

**page.add(...)** — coloca os elementos na janela.
É como adicionar itens ao prontuário. Você adiciona na ordem que quer exibir.

**ft.app(main)** — inicia o app chamando a função main.
É o 'ligar a máquina'.

Agora você tem uma janela. Dois textos. Cores TribeMD.
Doze linhas de código."

---

## SEÇÃO 4: BOTÃO E EVENTO — INTERATIVIDADE (8 min)

**Tom:** Evento clínico — ação que dispara uma resposta

"Uma interface sem interatividade é um cartaz.

Vamos adicionar um botão.

Modifique o main.py — adicione abaixo do subtitulo:

```python
    def ao_clicar(e):
        mensagem.value = 'Sistema iniciado. Bem-vindo, doutor.'
        page.update()

    botao = ft.ElevatedButton(
        text='Iniciar sistema',
        on_click=ao_clicar,
        bgcolor='#5213B9',
        color='white'
    )

    mensagem = ft.Text(value='', color='#2E3233')

    page.add(titulo, subtitulo, botao, mensagem)
```

(Substitua o 'page.add' anterior por este novo que inclui botao e mensagem)

Execute:

```
uv run python main.py
```

[mostrar — clicar no botão]

Clicou no botão, apareceu a mensagem.

---

O padrão que você está vendo é fundamental em toda interface:

**Evento** — algo acontece (clique, digitação, enter)
**Handler** — uma função que responde ao evento (ao_clicar)
**Atualização** — a tela é redesenhada (page.update)

É como o ciclo diagnóstico: estímulo, processamento, resposta.
O paciente apresenta o sintoma. Você processa. Você age.

Em Flet: o usuário clica. A função processa. A tela atualiza."

---

## SEÇÃO 5: MINI CALCULADORA DE IMC — JUNTANDO TUDO (12 min)

**Tom:** Síntese — Python + Flet + lógica clínica numa tela real

"Agora vamos construir algo real: uma calculadora de IMC com interface.

Substitua o conteúdo do main.py por:

```python
import flet as ft

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25.0:
        return 'Peso normal'
    elif imc < 30.0:
        return 'Sobrepeso'
    else:
        return 'Obesidade'

def main(page: ft.Page):
    page.title = 'ClinMd-Tribe — Calculadora de IMC'
    page.bgcolor = '#FAFAFA'
    page.padding = 30

    campo_peso = ft.TextField(
        label='Peso (kg)',
        hint_text='Ex: 82.5',
        width=200
    )

    campo_altura = ft.TextField(
        label='Altura (m)',
        hint_text='Ex: 1.75',
        width=200
    )

    resultado = ft.Text(value='', size=18, color='#5213B9')

    def calcular(e):
        try:
            peso = float(campo_peso.value)
            altura = float(campo_altura.value)
            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)
            resultado.value = f'IMC: {imc:.1f} — {classificacao}'
        except ValueError:
            resultado.value = 'Preencha os campos corretamente.'
        page.update()

    botao = ft.ElevatedButton(
        text='Calcular IMC',
        on_click=calcular,
        bgcolor='#5213B9',
        color='white'
    )

    page.add(
        ft.Text('Calculadora de IMC', size=24, weight=ft.FontWeight.BOLD),
        campo_peso,
        campo_altura,
        botao,
        resultado
    )

ft.app(main)
```

Execute:

```
uv run python main.py
```

[mostrar — preencher peso e altura, clicar em Calcular]

Você tem uma calculadora de IMC funcional com interface gráfica.

---

Olha o que você usou aqui.

Da aula de Python: calcular_imc, classificar_imc, if/elif/else, float().

Do Flet: ft.TextField (campo de texto), ft.ElevatedButton, ft.Text,
page.add, page.update.

E uma novidade: o bloco try/except.

**try** — tente executar isso
**except ValueError** — se der erro de valor (usuário digitou letra, por exemplo): faça isso

É como um protocolo de segurança: tente o procedimento, se der erro, acione o plano B.

Você não precisa decorar tudo isso.
O Claude Code vai escrever esse tipo de código por você.

Mas agora você sabe o que está olhando quando ele escreve."

---

## SEÇÃO 6: ENCERRAMENTO (3 min)

**Tom:** Resumo, motivação e o que vem a seguir

"Resumo do que ficou pronto hoje.

Primeira janela Flet criada com cores TribeMD.
Botão com evento e resposta na tela.
Calculadora de IMC com interface gráfica — campos, botão, resultado.

Você juntou Python da aula_12 com Flet desta aula.
O resultado é um software clínico funcional.

---

Dever de casa.

Adicione um campo 'Nome do Paciente' à calculadora.
Quando clicar em Calcular, a mensagem deve incluir o nome:
'João Silva — IMC: 26.8 — Sobrepeso'.

Na próxima aula: layout, organização de telas e componentes do Flet.
Você vai aprender a organizar os elementos em colunas e linhas
do jeito que um bom PEP organiza as seções do prontuário.

Até lá."

---

**FIM DO ROTEIRO**
