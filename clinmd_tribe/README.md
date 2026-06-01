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

## Módulo do curso

Cada módulo do curso adiciona uma feature neste app. Veja `../aulas/` para o material didático.
