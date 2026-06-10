# ClinMd-Tribe

App clínico pessoal 100% local. Roda no navegador. Exportável como .exe.

## Instalação

```bash
uv sync
uv run python -m src.presentation.main
```

## Estrutura

```
src/
├── presentation/    # UI Flet: telas e componentes
├── application/     # Casos de uso: orquestração
├── domain/          # Regras de negócio puras: calculadoras, modelos
└── infrastructure/  # I/O externo: arquivos, RAG, persistência
```

## Domínio (calculadoras clínicas)

`src/domain/` guarda as regras clínicas puras, uma por arquivo (fonte única de verdade):

- `meld.py`: MELD (piso de creatinina parametrizado em `PISO_CREATININA`)
- `cha2ds2vasc.py`: CHA2DS2-VASc (risco tromboembólico na FA)
- `phq9.py`: PHQ-9 (rastreio de depressão)
- `gad7.py`: GAD-7 (rastreio de ansiedade)

## Testes

```bash
# Só o domínio (não exige flet; bom para Python 3.14):
uv run --with pytest --no-project pytest -q

# No ambiente completo do projeto (Python 3.11 a 3.13):
uv run --extra dev pytest
```

## Módulo do curso

Este diretório é o app-piloto (gabarito do instrutor) do curso. Cada aula adiciona uma feature; o aluno NUNCA lê este código, vê apenas o comportamento (laudos, testes verdes, app rodando). Material didático: pastas `aula_NN/` na raiz.
