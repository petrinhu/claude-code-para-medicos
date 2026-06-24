# Casos de teste HAS-BLED + Decisao FA (gabarito de bastidor)

Dados ficticios. Nenhum paciente real. Use para conferir, ao vivo, se o app bate
com o calculo feito a mao. So o instrutor ve isto; nao aparece na aula.

HAS-BLED: 7 criterios, 1 ponto cada. Score 0 a 7.
Interpretacao: < 3 baixo risco; = 3 risco moderado; > 3 alto risco.

Cutoff CHA2DS2-VASc da Decisao FA: homem >= 2; mulher >= 3.

## Caso 1 (ancora da aula): HAS-BLED 1, Decisao "Anticoagular - baixo risco"

Paciente 001 - 68 anos, masculino, hipertenso controlado, diabetico.

| Criterio                         | Valor | Pontos |
|----------------------------------|-------|--------|
| H - HAS nao controlada           | nao   | 0      |
| A - disfuncao renal/hepatica     | nao   | 0      |
| S - AVC/AIT previo               | nao   | 0      |
| B - sangramento previo           | nao   | 0      |
| L - INR labil                    | nao   | 0      |
| E - idade > 65                   | sim   | 1      |
| D - drogas/alcool                | nao   | 0      |
| **Total**                        |       | **1**  |

Esperado HAS-BLED: score 1, "Baixo risco de sangramento".
Decisao FA: CHA2DS2-VASc = 3, sexo masculino.
Esperado: "Anticoagular - baixo risco de sangramento" (verde).

## Caso 2: HAS-BLED 7, Decisao "individualizada"

Paciente 002 - 78 anos, feminina. Hipertensa nao controlada, DRC estagio 4,
AVC isquemico ha 2 anos, sangramento GI previo, INR labil, em uso de AAS.

Todos os 7 criterios marcados.

Esperado HAS-BLED: score 7, "Alto risco de sangramento".
Decisao FA: CHA2DS2-VASc = 6, sexo feminino.
Esperado: "Decisao individualizada - discutir risco/beneficio" (laranja).
Nota: o app nao decide quando os dois scores sao altos; ele pede a conversa.
