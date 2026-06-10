"""Calculadora MELD (Model for End-Stage Liver Disease).

Regra clinica PURA: estima a gravidade da doenca hepatica cronica a partir de
bilirrubina, INR e creatinina. Nao sabe de tela, banco de dados ou arquivo.
Esta e a unica fonte de verdade do MELD no app (camada de dominio).
"""

import math

# Pisos laboratoriais: valores abaixo destes sao elevados ao piso antes do calculo.
# (Convencao classica do MELD: nenhum dos tres parametros entra abaixo de 1,0.)
PISO_BILIRRUBINA = 1.0
PISO_INR = 1.0
PISO_CREATININA = 1.0  # ponto que a aula da Ronda altera para demonstrar "tocar 1 arquivo"

# Creatinina e limitada superiormente; dialise recente assume o teto.
TETO_CREATININA = 4.0

# Faixa de saida usada pela alocacao de orgaos (UNOS): MELD entre 6 e 40.
MELD_MINIMO = 6
MELD_MAXIMO = 40


def calcular_meld(
    bilirrubina: float,
    inr: float,
    creatinina: float,
    dialise_recente: bool = False,
) -> int:
    """Retorna o escore MELD arredondado, na faixa de 6 a 40.

    bilirrubina, creatinina em mg/dL; inr adimensional.
    dialise_recente=True (>=2 sessoes nos ultimos 7 dias) fixa creatinina no teto.
    """
    bili = max(bilirrubina, PISO_BILIRRUBINA)
    inr_ajustado = max(inr, PISO_INR)

    if dialise_recente:
        creat = TETO_CREATININA
    else:
        creat = min(max(creatinina, PISO_CREATININA), TETO_CREATININA)

    escore = (
        3.78 * math.log(bili)
        + 11.2 * math.log(inr_ajustado)
        + 9.57 * math.log(creat)
        + 6.43
    )
    return max(MELD_MINIMO, min(MELD_MAXIMO, round(escore)))
