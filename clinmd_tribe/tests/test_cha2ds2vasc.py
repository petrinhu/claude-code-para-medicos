"""Guardioes do CHA2DS2-VASc. Casos espelham os usados na aula de testes."""

from src.domain.cha2ds2vasc import calcular_cha2ds2vasc


def test_homem_68_anos_has_e_dm_da_tres():
    # 65-74 anos (1) + HAS (1) + DM (1) = 3.
    assert calcular_cha2ds2vasc(
        idade=68,
        sexo_feminino=False,
        insuficiencia_cardiaca=False,
        hipertensao=True,
        diabetes=True,
        avc_ait_previo=False,
        doenca_vascular=False,
    ) == 3


def test_homem_55_anos_sem_fatores_da_zero():
    assert calcular_cha2ds2vasc(
        idade=55,
        sexo_feminino=False,
        insuficiencia_cardiaca=False,
        hipertensao=False,
        diabetes=False,
        avc_ait_previo=False,
        doenca_vascular=False,
    ) == 0


def test_mulher_77_anos_ic_has_avc_da_sete():
    # >=75 (2) + feminino (1) + IC (1) + HAS (1) + AVC previo (2) = 7.
    assert calcular_cha2ds2vasc(
        idade=77,
        sexo_feminino=True,
        insuficiencia_cardiaca=True,
        hipertensao=True,
        diabetes=False,
        avc_ait_previo=True,
        doenca_vascular=False,
    ) == 7


def test_avc_previo_isolado_da_dois():
    assert calcular_cha2ds2vasc(
        idade=60,
        sexo_feminino=False,
        insuficiencia_cardiaca=False,
        hipertensao=False,
        diabetes=False,
        avc_ait_previo=True,
        doenca_vascular=False,
    ) == 2


def test_todos_os_fatores_dao_nove():
    assert calcular_cha2ds2vasc(
        idade=80,
        sexo_feminino=True,
        insuficiencia_cardiaca=True,
        hipertensao=True,
        diabetes=True,
        avc_ait_previo=True,
        doenca_vascular=True,
    ) == 9


def test_fronteiras_de_idade():
    base = dict(
        sexo_feminino=False,
        insuficiencia_cardiaca=False,
        hipertensao=False,
        diabetes=False,
        avc_ait_previo=False,
        doenca_vascular=False,
    )
    assert calcular_cha2ds2vasc(idade=64, **base) == 0
    assert calcular_cha2ds2vasc(idade=65, **base) == 1
    assert calcular_cha2ds2vasc(idade=74, **base) == 1
    assert calcular_cha2ds2vasc(idade=75, **base) == 2
