# Claude Code para Médicos, do Zero ao Avançado

Curso prático de Claude Code para médicos. Sem programação nas fases iniciante e intermediário. Programação completa na fase avançada (opcional).

**Plataforma:** MDlife Academy  
**Parceria:** Dr. Petrus Silva Costa x TribeMD (Luiz Dieckmann)

## Estrutura

```
aulas/
  iniciante/          # M0 (4 aulas) + M1 (4 aulas): sem código
  intermediario/      # M2 (4 aulas) + M3 (5 aulas): sem código
  avancado/           # M4 com 12 submódulos: Python/Flet/ClinMd-Tribe
clinmd_tribe/         # app capstone da fase avançada (Clean Architecture)
workshop_iago/        # material de referência (Dieckmann)
docs/                 # specs e planos do projeto
arvore_aulas.html     # árvore visual de aulas (design MDlife Academy)
```

## Como usar

```bash
# Ver aulas de uma fase
ls aulas/iniciante/
ls aulas/intermediario/
ls aulas/avancado/04_construir_ferramentas/

# Rodar o app capstone (fase avançada)
cd clinmd_tribe
uv sync
uv run python -m src.presentation.main
```

## Módulos

### Iniciante (sem programação)

| # | Módulo | Aulas |
|---|--------|-------|
| M0 | Primeiros passos sem medo | 4 |
| M1 | Assistente de produtividade | 4 |

### Intermediário (sem programação)

| # | Módulo | Aulas |
|---|--------|-------|
| M2 | Aprender e acompanhar a literatura | 4 |
| M3 | Conteúdo, pesquisa e consultório | 5 |

### Avançado, opcional (Python + Flet + ClinMd-Tribe)

| # | Submódulo | Aulas |
|---|-----------|-------|
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

**Total: 22 aulas obrigatórias + 31 aulas fase avançada**

Veja a [árvore de aulas](arvore_aulas.html) para a visualização completa.
