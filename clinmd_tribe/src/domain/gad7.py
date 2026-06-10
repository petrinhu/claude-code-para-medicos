"""Calculadora GAD-7 (rastreio de ansiedade).

Regra clinica PURA. Fonte unica de verdade do GAD-7 no app (camada de dominio).
Sete itens, cada um de 0 a 3; total de 0 a 21.
"""

NUMERO_DE_ITENS = 7
PONTUACAO_MAXIMA_POR_ITEM = 3

# Pontos de corte da gravidade (limite inferior de cada faixa).
CORTE_LEVE = 5
CORTE_MODERADO = 10
CORTE_GRAVE = 15


def classificar_gad7(total: int) -> str:
    """Traduz o total (0 a 21) em faixa de gravidade."""
    if total >= CORTE_GRAVE:
        return "grave"
    if total >= CORTE_MODERADO:
        return "moderada"
    if total >= CORTE_LEVE:
        return "leve"
    return "minima"


def calcular_gad7(respostas: list[int]) -> tuple[int, str]:
    """Soma os 7 itens e retorna (total, classificacao).

    respostas: lista de exatamente 7 inteiros, cada um de 0 a 3.
    """
    if len(respostas) != NUMERO_DE_ITENS:
        raise ValueError(f"O GAD-7 exige exatamente {NUMERO_DE_ITENS} respostas.")
    for valor in respostas:
        if not 0 <= valor <= PONTUACAO_MAXIMA_POR_ITEM:
            raise ValueError("Cada resposta do GAD-7 deve estar entre 0 e 3.")

    total = sum(respostas)
    return total, classificar_gad7(total)
