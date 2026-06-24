# Casos de teste PHQ-9 e GAD-7 (gabarito de bastidor)

Dados ficticios. Nenhum paciente real. Use para conferir, ao vivo, se o app bate
com o calculo feito a mao. So o instrutor ve isto; nao aparece na aula.

Escala Likert por item: 0 Nunca, 1 Alguns dias, 2 Mais da metade dos dias, 3 Quase todo dia.

## PHQ-9 (9 itens, score 0 a 27)

Faixas: 0-4 Minimo; 5-9 Leve; 10-14 Moderado; 15-19 Moderadamente grave; 20-27 Grave.
Cutoff de acao: 10.
Item 9 (pensamentos de morte/auto-lesao): alerta independente do score se >= 1.

### Caso 1 (ancora): score 7, Leve, sem alerta

Paciente 001 - 45 anos, feminina. "To meio triste, doutor."

| Item              | Valor |
|-------------------|-------|
| 1 interesse       | 1     |
| 2 deprimido       | 1     |
| 3 sono            | 2     |
| 4 energia         | 2     |
| 5 apetite         | 0     |
| 6 autoestima      | 0     |
| 7 concentracao    | 1     |
| 8 agitacao        | 0     |
| 9 item_9          | 0     |
| **Total**         | **7** |

Esperado: score 7, faixa "Leve" (verde), sem alerta de suicidio.

### Caso 2 (grave + alerta): score 20, Grave, alerta ativo

Paciente 002 - 58 anos, masculino. Isolamento, anedonia.

| Item              | Valor |
|-------------------|-------|
| 1 interesse       | 3     |
| 2 deprimido       | 3     |
| 3 sono            | 3     |
| 4 energia         | 3     |
| 5 apetite         | 2     |
| 6 autoestima      | 2     |
| 7 concentracao    | 2     |
| 8 agitacao        | 1     |
| 9 item_9          | 1     |
| **Total**         | **20**|

Esperado: score 20, faixa "Grave" (vermelho),
caixa de alerta "Avaliar risco de suicidio imediatamente" ativa (item_9 = 1).

## GAD-7 (7 itens, score 0 a 21)

Faixas: 0-4 Minimo; 5-9 Leve; 10-14 Moderado; 15-21 Grave. Sem item de alerta.

### Caso 3: score 11, Moderado

Paciente 003 - 32 anos, masculino. Ansiedade e palpitacoes.

| Item                         | Valor |
|------------------------------|-------|
| 1 nervoso                    | 2     |
| 2 preocupacao incontrolavel  | 2     |
| 3 preocupacao excessiva      | 2     |
| 4 relaxar                    | 2     |
| 5 inquietacao                | 1     |
| 6 irritabilidade             | 1     |
| 7 medo                       | 1     |
| **Total**                    | **11**|

Esperado: score 11, faixa "Moderado" (amarelo).
