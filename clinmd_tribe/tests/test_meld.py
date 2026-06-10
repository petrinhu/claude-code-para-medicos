"""Guardioes do MELD. Travam o comportamento clinico da calculadora."""

import pytest

from src.domain.meld import calcular_meld, MELD_MAXIMO


def test_todos_os_valores_no_piso_dao_meld_minimo():
    # bilirrubina=INR=creatinina=1,0 -> apenas a constante 6,43 -> arredonda para 6.
    assert calcular_meld(1.0, 1.0, 1.0) == 6


def test_valores_abaixo_do_piso_sao_elevados_ao_piso():
    # 0,8 de creatinina entra como 1,0; o resultado nao muda em relacao ao piso.
    assert calcular_meld(1.0, 1.0, 0.8) == calcular_meld(1.0, 1.0, 1.0)


def test_caso_intermediario_conhecido():
    # 3,78*ln2 + 11,2*ln1,5 + 9,57*ln1,5 + 6,43 = 17,47 -> 17.
    assert calcular_meld(2.0, 1.5, 1.5) == 17


def test_dialise_recente_fixa_creatinina_no_teto():
    # Dialise assume creatinina = 4,0; demais no piso -> 9,57*ln4 + 6,43 = 19,70 -> 20.
    assert calcular_meld(1.0, 1.0, 1.0, dialise_recente=True) == 20


def test_creatinina_acima_do_teto_e_limitada():
    # Creatinina 10,0 e limitada a 4,0 -> mesmo resultado da dialise.
    assert calcular_meld(1.0, 1.0, 10.0) == 20


def test_valores_extremos_sao_limitados_ao_maximo():
    assert calcular_meld(50.0, 10.0, 4.0) == MELD_MAXIMO
