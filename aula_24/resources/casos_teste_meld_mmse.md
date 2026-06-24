# Casos de teste MELD e MMSE (gabarito de bastidor)

Dados ficticios. Nenhum paciente real. Use para conferir, ao vivo, se o app bate
com o calculo feito a mao. So o instrutor ve isto; nao aparece na aula.

## MELD (formula continua)

Formula: MELD = round(3.78*ln(bili) + 11.2*ln(INR) + 9.57*ln(crea) + 6.43).
Convencao: aplicar min 1.0 em cada variavel antes do logaritmo natural (math.log).
Faixas de mortalidade em 90 dias: <10 = 3.7%; 10-19 = 6.0%; 20-29 = 19.6%;
30-39 = 52.6%; >=40 = 71.3%.

### Caso 1 (ancora): score 20, mortalidade 19.6%

Paciente 001 - 58 anos, masculino. Cirrose alcoolica descompensada.

| Variavel            | Valor |
|---------------------|-------|
| Bilirrubina (mg/dL) | 4.5   |
| INR                 | 1.8   |
| Creatinina (mg/dL)  | 1.2   |

Conferencia a mao:
3.78 * ln(4.5) = 5.685
11.2 * ln(1.8) = 6.583
9.57 * ln(1.2) = 1.745
soma + 6.43 = 20.44 -> arredonda para 20.

Esperado: score 20, "Mortalidade em 90 dias: 19.6%".

### Caso 2 (grave): score 31, mortalidade 52.6%

Paciente 002 - cirrose descompensada severa.

| Variavel            | Valor |
|---------------------|-------|
| Bilirrubina (mg/dL) | 8.0   |
| INR                 | 2.5   |
| Creatinina (mg/dL)  | 2.0   |

Esperado: score 31, "Mortalidade em 90 dias: 52.6%".

## MMSE (subtestes com tetos diferentes)

6 subtestes, score total 0 a 30.
Tetos: orientacao temporal 5, orientacao espacial 5, registro 3,
atencao e calculo 5, evocacao 3, linguagem e praxia 9.
Faixas: >=24 Normal; 18-23 Comprometimento leve; 10-17 moderado; <10 grave.
A figura dos pentagonos sobrepostos (subteste linguagem/praxia) esta em
`resources/pentagonos_mmse.png` para usar no tooltip/ícone de referencia da tela.

### Caso 3 (ancora): score 20, Comprometimento leve

Paciente 003 - 72 anos, feminina. Esquecimento crescente ha 6 meses.

| Subteste              | Valor | Teto |
|-----------------------|-------|------|
| Orientacao temporal   | 3     | 5    |
| Orientacao espacial   | 4     | 5    |
| Registro              | 2     | 3    |
| Atencao e calculo     | 3     | 5    |
| Evocacao              | 1     | 3    |
| Linguagem e praxia    | 7     | 9    |
| **Total**             | **20**|      |

Esperado: score 20, "Comprometimento leve" (amarelo).

### Caso 4 (grave): score 7, Comprometimento grave

Paciente 004 - idoso, desorientado, linguagem comprometida.

| Subteste              | Valor | Teto |
|-----------------------|-------|------|
| Orientacao temporal   | 1     | 5    |
| Orientacao espacial   | 1     | 5    |
| Registro              | 0     | 3    |
| Atencao e calculo     | 1     | 5    |
| Evocacao              | 0     | 3    |
| Linguagem e praxia    | 4     | 9    |
| **Total**             | **7** |      |

Esperado: score 7, "Comprometimento grave" (vermelho).
