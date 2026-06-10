"""Guardioes do GAD-7. Travam soma e faixas de gravidade."""

import pytest

from src.domain.gad7 import calcular_gad7


def test_tudo_zero_e_minima():
    assert calcular_gad7([0] * 7) == (0, "minima")


def test_tudo_no_maximo_e_grave():
    assert calcular_gad7([3] * 7) == (21, "grave")


def test_corte_leve():
    assert calcular_gad7([1, 1, 1, 1, 1, 0, 0]) == (5, "leve")


def test_corte_moderada():
    assert calcular_gad7([2, 2, 2, 2, 2, 0, 0]) == (10, "moderada")


def test_corte_grave():
    assert calcular_gad7([3, 3, 3, 3, 3, 0, 0]) == (15, "grave")


def test_numero_de_respostas_invalido():
    with pytest.raises(ValueError):
        calcular_gad7([0] * 6)
