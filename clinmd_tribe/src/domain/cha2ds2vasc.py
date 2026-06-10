"""Calculadora CHA2DS2-VASc (risco tromboembolico na fibrilacao atrial).

Regra clinica PURA. Fonte unica de verdade do escore no app (camada de dominio).
Pontuacao: idade>=75 vale 2; AVC/AIT previo vale 2; demais fatores 1 cada.
"""

# Idade pontua em faixas: >=75 -> 2 pontos; 65 a 74 -> 1 ponto.
IDADE_ALTO_RISCO = 75
IDADE_RISCO_INTERMEDIARIO = 65


def calcular_cha2ds2vasc(
    idade: int,
    sexo_feminino: bool,
    insuficiencia_cardiaca: bool,
    hipertensao: bool,
    diabetes: bool,
    avc_ait_previo: bool,
    doenca_vascular: bool,
) -> int:
    """Retorna o escore CHA2DS2-VASc (0 a 9)."""
    pontos = 0

    if idade >= IDADE_ALTO_RISCO:
        pontos += 2
    elif idade >= IDADE_RISCO_INTERMEDIARIO:
        pontos += 1

    if avc_ait_previo:           # S2 - vale 2 pontos
        pontos += 2

    if insuficiencia_cardiaca:   # C
        pontos += 1
    if hipertensao:              # H
        pontos += 1
    if diabetes:                 # D
        pontos += 1
    if doenca_vascular:          # V
        pontos += 1
    if sexo_feminino:            # Sc
        pontos += 1

    return pontos
