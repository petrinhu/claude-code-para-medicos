"""Guardioes do PHQ-9. Travam soma e faixas de gravidade."""

import pytest

from src.domain.phq9 import calcular_phq9


def test_tudo_zero_e_minima():
    assert calcular_phq9([0] * 9) == (0, "minima")


def test_tudo_no_maximo_e_grave():
    assert calcular_phq9([3] * 9) == (27, "grave")


def test_fronteira_minima_para_leve():
    assert calcular_phq9([1, 1, 1, 1, 0, 0, 0, 0, 0]) == (4, "minima")
    assert calcular_phq9([1, 1, 1, 1, 1, 0, 0, 0, 0]) == (5, "leve")


def test_corte_moderada():
    assert calcular_phq9([2, 2, 2, 2, 2, 0, 0, 0, 0]) == (10, "moderada")


def test_corte_moderadamente_grave():
    assert calcular_phq9([3, 3, 3, 3, 3, 0, 0, 0, 0]) == (15, "moderadamente grave")


def test_corte_grave():
    assert calcular_phq9([3, 3, 3, 3, 3, 3, 2, 0, 0]) == (20, "grave")


def test_numero_de_respostas_invalido():
    with pytest.raises(ValueError):
        calcular_phq9([0] * 8)


def test_resposta_fora_da_faixa():
    with pytest.raises(ValueError):
        calcular_phq9([4, 0, 0, 0, 0, 0, 0, 0, 0])
