# Claude Code do Zero ao Avançado

Curso prático de Claude Code para médicos.
Produto final: **ClinMd-Tribe**, app clínico 100% local.

**Parceria:** Dr. Petrus Silva Costa x TribeMD (Luiz Dieckmann)

## Estrutura

```
aulas/          # 12 módulos, 31 aulas de 1h
clinmd_tribe/   # app capstone (cresce a cada módulo)
workshop_iago/  # material de referência (Dieckmann)
docs/           # specs e planos do projeto
```

## Como usar

```bash
# Acesse a aula pelo módulo
ls aulas/05_calculadoras/

# Rode o app capstone
cd clinmd_tribe
uv sync
uv run python -m src.presentation.main
```

## Módulos

| # | Módulo | Aulas |
|---|--------|-------|
| 00 | Fundação (terminal, uv, Python) | 2 |
| 01 | Git | 2 |
| 02 | Python + Flet | 2 |
| 03 | Clean Architecture | 2 |
| 04 | Agents e BigTech Virtual | 4 |
| 05 | Calculadoras Médicas | 4 |
| 06 | Anotador Clínico | 2 |
| 07 | RAG Tribe | 4 |
| 08 | Gerador de Evolução | 2 |
| 09 | Testes | 2 |
| 10 | CI/CD | 2 |
| 11 | Polimento Final | 3 |

**Total: 31 aulas**

Veja o [roadmap.html](roadmap.html) para visualização completa.
