# ClinMd-Tribe

App clinico pessoal 100% local. Roda no navegador. Exportavel como .exe.

## Instalacao

```bash
uv sync
uv run python -m src.presentation.main
```

## Estrutura

```
src/
├── presentation/    # UI Flet: telas e componentes
├── application/     # Casos de uso: orquestracao
├── domain/          # Regras de negocio puras: calculadoras, modelos
└── infrastructure/  # I/O externo: arquivos, RAG, persistencia
```

## Modulo do curso

Cada modulo do curso adiciona uma feature neste app. Veja `../aulas/` para o material didatico.
