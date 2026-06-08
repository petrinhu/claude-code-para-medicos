# Aula 12 — Python com Analogias Clínicas

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~40 min  
**Tom:** Colega com humor leve e didático — primeira aula de Python, zero presumido

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Desarmador — tirar o medo antes de começar

"Python.

Esse nome assusta muita gente que nunca programou.
Parece coisa de TI, parece complexo, parece que você precisa de anos de estudo.

Não precisa.

Você aprendeu a interpretar um ECG com 12 derivações.
Você aprendeu a ler uma gasometria. Você aprendeu anatomia com nomes em latim.

Python é mais fácil do que qualquer um desses.

Mas tem um detalhe: você precisa parar de tentar aprender Python como programador.
Você vai aprender Python como médico aprende um protocolo novo —
do básico ao avançado, um conceito de cada vez, com lógica clínica.

Hoje: quatro conceitos. Só quatro.
Variáveis, funções, condições e listas.

Vamos lá."

---

## SEÇÃO 2: O QUE É PYTHON (3 min)

**Tom:** Analogia médica — idioma de comunicação com o computador

"Python é um idioma.

Você se comunica com pacientes em português.
Você se comunica com colegas internacionais em inglês.
Você se comunica com o computador em Python.

O computador não entende 'calcule o IMC desse paciente'.
Mas entende isso:

```python
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
```

Parece estranho agora. Mas daqui a 20 minutos você vai entender cada símbolo.

Python foi criado com um princípio: ser legível.
O criador, Guido van Rossum, queria que código Python lesse quase como inglês.

Você vai ver isso na prática agora."

---

## SEÇÃO 3: VARIÁVEIS — O PRONTUÁRIO DO CÓDIGO (10 min)

**Tom:** Conceito central, exemplos médicos, quatro tipos

"Variável é um lugar na memória do computador onde você guarda um valor.

Pense como um campo do prontuário eletrônico.

No prontuário você tem: Nome, Idade, Peso, Diabético.
Em Python:

```python
nome = 'João Silva'
idade = 45
peso = 82.5
diabetico = True
```

Veja a simplicidade. Você escreve o nome, um sinal de igual, e o valor.
Acabou.

[mostrar no main.py, salvar, rodar com uv run python main.py]

---

Mas os tipos importam. Cada tipo de dado em Python se comporta diferente.

**String** — texto. Sempre entre aspas simples ou duplas.
```python
nome = 'João Silva'
especialidade = 'Cardiologia'
```
Analogia: o campo 'Queixa Principal' do prontuário. Texto livre.

**Integer** — número inteiro. Sem ponto decimal.
```python
idade = 45
numero_consultas = 12
```
Analogia: número do leito. Não tem 'leito 12.5'.

**Float** — número com decimal. Com ponto (não vírgula — Python usa ponto).
```python
peso = 82.5
hemoglobina = 13.2
```
Analogia: resultado de laboratório. Sempre tem decimal.

**Boolean** — verdadeiro ou falso. Só dois valores possíveis: True ou False.
```python
diabetico = True
hipertenso = False
gestante = False
```
Analogia: checkbox do prontuário. Marcado ou não marcado.

[digitar cada um no main.py e mostrar rodando]

---

Para mostrar o valor de uma variável no terminal, use print:

```python
print(nome)
print(idade)
print(diabetico)
```

[executar e mostrar]

print é como mandar o resultado pra tela. É o display do monitor cardíaco."

---

## SEÇÃO 4: FUNÇÕES — O PROTOCOLO CLÍNICO (10 min)

**Tom:** Conceito de reutilização — escreva uma vez, use muitas vezes

"Você tem um protocolo para avaliar risco de AVC em fibrilação atrial.
Toda vez que um paciente novo chega, você segue o mesmo protocolo.

Não reescreve o protocolo do zero. Você aplica.

Função em Python é isso: você escreve o protocolo uma vez,
e aplica quantas vezes quiser.

Veja um exemplo:

```python
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
```

Leia em voz alta como uma instrução médica:

**def** — 'defina um protocolo chamado...'
**calcular_imc** — esse é o nome do protocolo
**(peso, altura)** — você precisa dessas informações para aplicar
**imc = peso / (altura ** 2)** — o cálculo em si
**return imc** — devolva o resultado

[digitar no main.py]

Agora como você usa esse protocolo:

```python
resultado = calcular_imc(82.5, 1.75)
print(resultado)
```

[executar e mostrar o resultado]

O Python calculou o IMC. Você escreveu o protocolo uma vez.
Pode chamar com qualquer paciente:

```python
print(calcular_imc(70, 1.68))
print(calcular_imc(95, 1.80))
print(calcular_imc(55, 1.60))
```

[executar]

Três IMCs calculados em três linhas.
Sem copiar o cálculo. Sem repetir a fórmula.

Isso é o poder da função: escreva uma vez, use sempre."

---

## SEÇÃO 5: CONDIÇÕES — TOMADA DE DECISÃO CLÍNICA (8 min)

**Tom:** Lógica clínica direta — if/elif/else

"Agora combinamos variável e função com tomada de decisão.

Em clínica você faz isso o tempo todo:

Se PA sistólica maior que 180: crise hipertensiva.
Se entre 140 e 180: hipertensão grau 2.
Se entre 120 e 140: hipertensão grau 1.
Se menor que 120: normal.

Em Python:

```python
def classificar_pressao(pas):
    if pas >= 180:
        return 'Crise hipertensiva'
    elif pas >= 140:
        return 'Hipertensao grau 2'
    elif pas >= 120:
        return 'Hipertensao grau 1'
    else:
        return 'Normal'
```

Leia:

**if** — se
**elif** — senão, se (abreviação de 'else if')
**else** — em qualquer outro caso

A indentação — os espaços no começo das linhas — é obrigatória em Python.
É como a hierarquia do prontuário: seção e subseção.
Python usa espaços para entender o que pertence a quem.

[digitar e testar com alguns valores]

```python
print(classificar_pressao(185))
print(classificar_pressao(150))
print(classificar_pressao(125))
print(classificar_pressao(110))
```

[executar e mostrar]

Quatro valores, quatro classificações corretas."

---

## SEÇÃO 6: LISTAS — A ENFERMARIA DO CÓDIGO (5 min)

**Tom:** Rápido — conceito de coleção, loop simples

"Última estrutura básica: lista.

Uma lista é uma coleção de valores na mesma variável.

É como uma enfermaria — vários pacientes, um registro.

```python
pacientes = ['João', 'Maria', 'Carlos', 'Ana']
```

Para percorrer cada paciente:

```python
for paciente in pacientes:
    print(paciente)
```

Leia: para cada paciente na lista, execute o print.

[executar]

João. Maria. Carlos. Ana. Cada um na sua vez.

Adicionar um paciente novo:

```python
pacientes.append('Beatriz')
print(pacientes)
```

[executar]

Beatriz entrou para a lista.

Quantos pacientes:

```python
print(len(pacientes))
```

Cinco.

Esses quatro conceitos — variável, função, condição, lista —
são 80% do que o ClinMd-Tribe vai usar.
O resto você vai aprender no contexto de cada funcionalidade."

---

## SEÇÃO 7: JUNTANDO TUDO — MINI PROTOCOLO CLÍNICO (5 min)

**Tom:** Síntese motivacional — ver os quatro conceitos em ação

"Vamos juntar os quatro conceitos num mini protocolo.

```python
def avaliar_paciente(nome, peso, altura, pas):
    imc = calcular_imc(peso, altura)
    pressao = classificar_pressao(pas)
    print(f'{nome}: IMC {imc:.1f}, Pressao: {pressao}')

pacientes = [
    ('Joao', 82.5, 1.75, 150),
    ('Maria', 65.0, 1.62, 118),
    ('Carlos', 98.0, 1.80, 185),
]

for nome, peso, altura, pas in pacientes:
    avaliar_paciente(nome, peso, altura, pas)
```

[digitar e executar]

Três pacientes avaliados. IMC e pressão de cada um.
Em doze linhas de código.

Você escreveu isso. Você entendeu cada linha.

Nas próximas aulas, o Claude Code vai escrever código Python por você —
mas você vai reconhecer o padrão. Variáveis, funções, condições, listas.
É sempre isso.

Você não precisa mais ter medo do Python."

---

## SEÇÃO 8: ENCERRAMENTO (2 min)

**Tom:** Resumo e ponte para Flet

"Resumo do que ficou pronto hoje.

Quatro conceitos aprendidos com analogias clínicas:
— Variável: campo do prontuário
— Função: protocolo clínico reutilizável
— Condição: tomada de decisão clínica (if/elif/else)
— Lista: enfermaria do código

Um mini protocolo completo rodando no terminal.

---

Dever de casa.

Adicione uma quinta variável ao paciente: glicemia.
Crie uma função 'classificar_glicemia(glicemia)' com a lógica:
abaixo de 70: hipoglicemia, 70-99: normal, 100-125: pré-diabetes, acima de 126: diabetes.
Teste com três valores.

Na próxima aula: Flet. A interface gráfica do ClinMd-Tribe.
Você vai ver na tela o que hoje está só no terminal.

Até lá."

---

**FIM DO ROTEIRO**
