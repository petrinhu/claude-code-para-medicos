# Casos de teste CHA2DS2-VASc (gabarito de bastidor)

Dados ficticios. Nenhum paciente real. Use para conferir, ao vivo, se o app bate
com o calculo feito a mao. So o instrutor ve isto; nao aparece na aula.

Cutoff: homem score >= 2 anticoagula; mulher score >= 3 anticoagula.
Cada criterio vale 1 ponto, exceto Idade >= 75 (2 pts) e AVC previo (2 pts).

## Caso 1 (ancora da aula): score 3, Anticoagular

Paciente 001 - 68 anos, masculino.

| Criterio          | Valor | Pontos |
|-------------------|-------|--------|
| CHF (IC)          | nao   | 0      |
| HAS               | sim   | 1      |
| Idade >= 75       | nao   | 0      |
| DM                | sim   | 1      |
| AVC previo        | nao   | 0      |
| Doenca vascular   | nao   | 0      |
| Idade 65-74       | sim   | 1      |
| Sexo feminino     | nao   | 0      |
| **Total**         |       | **3**  |

Esperado no app: score 3, recomendacao "Anticoagular".

## Caso 2: score 0, Sem indicacao

Paciente 002 - 55 anos, masculino, sem nenhum fator de risco.
Todos os campos desmarcados, idade 55, sexo masculino.

Esperado no app: score 0, recomendacao "Sem indicacao no momento".

## Caso 3: score 7, Anticoagular

Paciente 003 - 77 anos, feminina. IC, hipertensa, AVC previo.

| Criterio          | Valor | Pontos |
|-------------------|-------|--------|
| CHF (IC)          | sim   | 1      |
| HAS               | sim   | 1      |
| Idade >= 75       | sim   | 2      |
| AVC previo        | sim   | 2      |
| Sexo feminino     | sim   | 1      |
| **Total**         |       | **7**  |

Esperado no app: score 7, recomendacao "Anticoagular".
