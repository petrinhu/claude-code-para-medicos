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

Mas tem um detalhe importante: você não vai escrever Python.
Você vai pedir ao Claude Code para escrever.
E você vai entender o que ele escreveu — para poder validar, corrigir e evoluir.

É como laudar um exame que o aparelho gerou.
Você não calibrou o aparelho. Mas você entende o resultado e assina se estiver certo.

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

Daqui a 20 minutos você vai entender cada símbolo desse código.

Python foi criado com um princípio: ser legível.
O criador, Guido van Rossum, queria que código Python lesse quase como inglês.

Você vai ver isso agora — lendo o que o Claude Code escreve para você."

---

## SEÇÃO 3: VARIÁVEIS — O PRONTUÁRIO DO CÓDIGO (10 min)

**Tom:** Conceito central, exemplos médicos, quatro tipos

"Variável é um lugar na memória do computador onde você guarda um valor.

Pense como um campo do prontuário eletrônico.

No prontuário você tem: Nome, Idade, Peso, Diabético.
Em Python é exatamente isso — cada campo tem um nome e um valor.

Existem quatro tipos principais:

**String** — texto. Campo 'Queixa Principal': texto livre, entre aspas.

**Integer** — número inteiro. Número do leito: não tem 'leito 12.5'.

**Float** — número com decimal. Resultado de laboratório: sempre tem decimal.
Python usa ponto, não vírgula: 82.5, não 82,5.

**Boolean** — verdadeiro ou falso. Checkbox do prontuário: marcado ou não marcado.
Em Python: True ou False, com letra maiúscula.

---

Agora veja esses conceitos em código real.

Abra o PowerShell, entre na pasta do projeto e abra o Claude Code:

```
cd Documents\projetos\clinmd-tribe
claude
```

Dê este prompt:

```
Crie um arquivo chamado conceitos.py com exemplos de variáveis Python
para um paciente clínico: nome (string), idade (int), peso (float)
e diabetico (bool). Adicione um print para cada variável mostrando
o nome do campo e o valor. Use nomes de variáveis em português.
```

[aguardar o Claude gerar o arquivo]

[mostrar o arquivo gerado]

Leia o código gerado comigo.

Veja: 'nome = João Silva' — a variável se chama 'nome' e guarda o texto.
'idade = 45' — número inteiro, sem ponto decimal.
'peso = 82.5' — número com decimal, ponto como separador.
'diabetico = True' — boolean, começa com maiúscula.

Agora execute:

```
uv run python conceitos.py
```

[mostrar o resultado no terminal]

Cada print mostrou o valor da variável correspondente.

print é como o display do monitor cardíaco — você manda exibir, ele exibe."

---

## SEÇÃO 4: FUNÇÕES — O PROTOCOLO CLÍNICO (10 min)

**Tom:** Conceito de reutilização — defina uma vez, aplique sempre

"Você tem um protocolo para avaliar risco de AVC em fibrilação atrial.
Toda vez que um paciente novo chega, você segue o mesmo protocolo.

Não reescreve o protocolo do zero. Você aplica.

Função em Python é isso: um protocolo escrito uma vez que você aplica quantas vezes quiser.

Prompt ao Claude Code:

```
No arquivo conceitos.py, adicione uma função chamada calcular_imc
que recebe peso e altura e retorna o IMC calculado.
Depois chame essa função com três pacientes diferentes e imprima os resultados.
```

[aguardar o Claude atualizar o arquivo]

[mostrar o código gerado]

Leia comigo o que o Claude escreveu.

A linha que começa com 'def' define o protocolo.
'def calcular_imc(peso, altura):' — defina um protocolo chamado calcular_imc
que precisa de peso e altura para funcionar.

'return' — devolva o resultado calculado.

Abaixo, três chamadas com pacientes diferentes.
O protocolo foi escrito uma vez e aplicado três vezes.

Execute:

```
uv run python conceitos.py
```

Três IMCs calculados. A mesma função. Três pacientes."

---

## SEÇÃO 5: CONDIÇÕES — TOMADA DE DECISÃO CLÍNICA (8 min)

**Tom:** Lógica clínica direta — if/elif/else

"Agora o conceito mais parecido com raciocínio clínico.

Em medicina você faz isso o tempo todo:

Se PA sistólica maior que 180: crise hipertensiva.
Se entre 140 e 180: hipertensão grau 2.
Se entre 120 e 140: hipertensão grau 1.
Se menor que 120: normal.

Python escreve exatamente essa lógica.

Prompt ao Claude Code:

```
No arquivo conceitos.py, adicione uma função chamada classificar_pressao
que recebe a pressao arterial sistolica e retorna a classificacao:
acima de 180 crise hipertensiva, entre 140 e 180 hipertensao grau 2,
entre 120 e 140 hipertensao grau 1, abaixo de 120 normal.
Teste com os valores 185, 150, 125 e 110.
```

[aguardar o Claude atualizar o arquivo]

[mostrar o código gerado]

Leia comigo.

'if' — se.
'elif' — senão, se. Abreviação de 'else if'.
'else' — em qualquer outro caso.

Percebe como lê quase como português?

Os espaços no início de cada linha — a indentação — são obrigatórios.
Python usa isso para saber o que pertence a qual condição.
É como a hierarquia do prontuário: seção e subseção.

Execute:

```
uv run python conceitos.py
```

Quatro valores, quatro classificações corretas."

---

## SEÇÃO 6: LISTAS — A ENFERMARIA DO CÓDIGO (5 min)

**Tom:** Rápido — conceito de coleção e loop

"Última estrutura básica: lista.

Uma lista guarda vários valores na mesma variável.
É como uma enfermaria — vários pacientes, um registro.

Prompt ao Claude Code:

```
No arquivo conceitos.py, adicione uma lista com quatro nomes de pacientes
e um loop que imprime cada nome com o numero do paciente na lista.
Depois mostre como adicionar um paciente novo à lista e contar quantos tem.
```

[aguardar e mostrar o código gerado]

Leia comigo.

Colchetes marcam a lista. Cada item separado por vírgula.
'for paciente in pacientes' — para cada paciente na lista, execute este bloco.
'.append' adiciona um item ao final. 'len' conta quantos itens existem.

Execute e veja a lista percorrida, o paciente novo adicionado, a contagem final."

---

## SEÇÃO 7: JUNTANDO TUDO (5 min)

**Tom:** Síntese — ver os quatro conceitos integrados num protocolo real

"Agora peça ao Claude Code para integrar tudo num mini protocolo clínico.

Prompt:

```
No arquivo conceitos.py, crie uma função avaliar_paciente que recebe
nome, peso, altura e pressao arterial sistolica. Ela deve calcular o IMC
usando calcular_imc, classificar a pressao usando classificar_pressao
e imprimir um resumo do paciente. Crie uma lista com tres pacientes
e aplique a funcao para cada um usando um loop.
```

[aguardar e mostrar o código gerado]

[executar]

Três pacientes avaliados. IMC e pressão de cada um.

Olha o que o Claude escreveu — e olha o que você reconhece:
variáveis, funções, condições, lista, loop.

Você não escreveu uma linha. Mas você entendeu cada uma.

Isso é exatamente o que vai acontecer no ClinMd-Tribe:
o Claude escreve, você lê, valida, e pede ajustes.
Você é o médico. O Claude é o residente que executa."

---

## SEÇÃO 8: ENCERRAMENTO (2 min)

**Tom:** Resumo e ponte para Flet

"Resumo do que ficou pronto hoje.

Quatro conceitos lidos e entendidos com analogias clínicas:
— Variável: campo do prontuário
— Função: protocolo clínico reutilizável
— Condição: tomada de decisão com if/elif/else
— Lista: enfermaria do código com loop

Um mini protocolo completo gerado pelo Claude e rodando no terminal.

---

Dever de casa.

Peça ao Claude Code:

```
No arquivo conceitos.py, adicione uma função classificar_glicemia
que recebe o valor da glicemia e retorna: hipoglicemia (abaixo de 70),
normal (70 a 99), pre-diabetes (100 a 125) ou diabetes (acima de 126).
Teste com os valores 60, 90, 110 e 140.
```

Execute, leia o código gerado e valide se as classificações estão corretas.

Na próxima aula: Flet. A interface gráfica do ClinMd-Tribe.
Você vai ver na tela o que hoje está só no terminal.

Até lá."

---

**FIM DO ROTEIRO**
