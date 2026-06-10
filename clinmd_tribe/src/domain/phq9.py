"""Calculadora PHQ-9 (rastreio de depressao).

Regra clinica PURA. Fonte unica de verdade do PHQ-9 no app (camada de dominio).
Nove itens, cada um de 0 a 3; total de 0 a 27. A classificacao usa pontos de
corte que vivem so aqui (a aula da Ronda altera um deles para demonstrar
"tocar 1 arquivo").
"""

NUMERO_DE_ITENS = 9
PONTUACAO_MAXIMA_POR_ITEM = 3

# Pontos de corte da gravidade (limite inferior de cada faixa).
CORTE_LEVE = 5
CORTE_MODERADO = 10
CORTE_MODERADAMENTE_GRAVE = 15
CORTE_GRAVE = 20


def classificar_phq9(total: int) -> str:
    """Traduz o total (0 a 27) em faixa de gravidade."""
    if total >= CORTE_GRAVE:
        return "grave"
    if total >= CORTE_MODERADAMENTE_GRAVE:
        return "moderadamente grave"
    if total >= CORTE_MODERADO:
        return "moderada"
    if total >= CORTE_LEVE:
        return "leve"
    return "minima"


def calcular_phq9(respostas: list[int]) -> tuple[int, str]:
    """Soma os 9 itens e retorna (total, classificacao).

    respostas: lista de exatamente 9 inteiros, cada um de 0 a 3.
    """
    if len(respostas) != NUMERO_DE_ITENS:
        raise ValueError(f"O PHQ-9 exige exatamente {NUMERO_DE_ITENS} respostas.")
    for valor in respostas:
        if not 0 <= valor <= PONTUACAO_MAXIMA_POR_ITEM:
            raise ValueError("Cada resposta do PHQ-9 deve estar entre 0 e 3.")

    total = sum(respostas)
    return total, classificar_phq9(total)
