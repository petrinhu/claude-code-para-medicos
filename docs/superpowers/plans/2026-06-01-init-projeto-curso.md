# Init Projeto Curso — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Inicializar estrutura completa do repositório do curso "Claude Code do Zero ao Avançado" com 12 módulos, scaffold Clean Architecture, CLAUDE.md local e roadmap.html atualizado.

**Architecture:** Repo monolítico com `aulas/` (material didático) e `clinmd_tribe/` (app capstone evoluindo por módulo). Cada aula tem roteiro.md (professor) + README.md (aluno) + exercicios.md. App segue Clean Architecture 4 camadas desde o scaffold.

**Tech Stack:** Python 3.11+, Flet, uv, Clean Architecture, Markdown para docs, HTML/Tailwind para roadmap.

---

## Mapa de Arquivos

### Criados neste plano

```
aulas_claude_dieckmann/
├── CLAUDE.md                                        # Task 3
├── README.md                                        # Task 5
├── roadmap.html                                     # Task 4 (substituir)
├── aulas/
│   ├── 00_fundacao/aula_01_terminal_uv/            # Task 1
│   │   ├── README.md
│   │   ├── roteiro.md
│   │   └── exercicios.md
│   ├── 00_fundacao/aula_02_python_medico/          # Task 1
│   ├── 01_git/aula_01_git_init_commit/             # Task 1
│   ├── 01_git/aula_02_branch_forgejo/              # Task 1
│   ├── 02_python_flet/aula_01_flet_hello/         # Task 1
│   ├── 02_python_flet/aula_02_flet_layout/        # Task 1
│   ├── 03_clean_arch/aula_01_4_camadas/           # Task 1
│   ├── 03_clean_arch/aula_02_scaffold_app/        # Task 1
│   ├── 04_agents_bigtech/aula_01_claude_code/     # Task 1
│   ├── 04_agents_bigtech/aula_02_mcp_skills/      # Task 1
│   ├── 04_agents_bigtech/aula_03_bigtech_virtual/ # Task 1
│   ├── 04_agents_bigtech/aula_04_tab_pendencias/  # Task 1
│   ├── 05_calculadoras/aula_01_cha2ds2vasc/       # Task 1
│   ├── 05_calculadoras/aula_02_phq9_gad7/         # Task 1
│   ├── 05_calculadoras/aula_03_hamd_ymrs/         # Task 1
│   ├── 05_calculadoras/aula_04_outras/            # Task 1
│   ├── 06_anotador/aula_01_templates/             # Task 1
│   ├── 06_anotador/aula_02_salvamento_busca/      # Task 1
│   ├── 07_rag_tribe/aula_01_embed_conceitos/      # Task 1
│   ├── 07_rag_tribe/aula_02_indexar_pdfs/         # Task 1
│   ├── 07_rag_tribe/aula_03_busca_semantica/      # Task 1
│   ├── 07_rag_tribe/aula_04_integracao_app/       # Task 1
│   ├── 08_gerador_evolucao/aula_01_gerador/       # Task 1
│   ├── 08_gerador_evolucao/aula_02_integracao/    # Task 1
│   ├── 09_testes/aula_01_tdd_pytest/              # Task 1
│   ├── 09_testes/aula_02_testes_calculadoras/     # Task 1
│   ├── 10_cicd/aula_01_forgejo_pipeline/          # Task 1
│   ├── 10_cicd/aula_02_woodpecker/                # Task 1
│   ├── 11_polimento_final/aula_01_ui_medica/      # Task 1
│   ├── 11_polimento_final/aula_02_exe/            # Task 1
│   └── 11_polimento_final/aula_03_auditoria/      # Task 1
└── clinmd_tribe/                                    # Task 2
    ├── pyproject.toml
    ├── .gitignore
    ├── README.md
    ├── src/
    │   ├── __init__.py
    │   ├── presentation/
    │   │   ├── __init__.py
    │   │   └── .gitkeep
    │   ├── application/
    │   │   ├── __init__.py
    │   │   └── .gitkeep
    │   ├── domain/
    │   │   ├── __init__.py
    │   │   └── .gitkeep
    │   └── infrastructure/
    │       ├── __init__.py
    │       └── .gitkeep
    ├── tests/
    │   └── __init__.py
    ├── knowledge_base/
    │   └── .gitkeep
    └── data/
        └── .gitkeep
```

---

## Task 1: Scaffold pasta aulas/ — 12 módulos, 27 aulas

**Files:**
- Create: toda a árvore `aulas/` conforme mapa acima

- [ ] **Step 1: Criar todos os diretórios**

```bash
cd /home/petrus/IDrive/Documentos/projetos_claudebrain/Projects/aulas_claude_dieckmann

dirs=(
  "aulas/00_fundacao/aula_01_terminal_uv"
  "aulas/00_fundacao/aula_02_python_medico"
  "aulas/01_git/aula_01_git_init_commit"
  "aulas/01_git/aula_02_branch_forgejo"
  "aulas/02_python_flet/aula_01_flet_hello"
  "aulas/02_python_flet/aula_02_flet_layout"
  "aulas/03_clean_arch/aula_01_4_camadas"
  "aulas/03_clean_arch/aula_02_scaffold_app"
  "aulas/04_agents_bigtech/aula_01_claude_code"
  "aulas/04_agents_bigtech/aula_02_mcp_skills"
  "aulas/04_agents_bigtech/aula_03_bigtech_virtual"
  "aulas/04_agents_bigtech/aula_04_tab_pendencias"
  "aulas/05_calculadoras/aula_01_cha2ds2vasc"
  "aulas/05_calculadoras/aula_02_phq9_gad7"
  "aulas/05_calculadoras/aula_03_hamd_ymrs"
  "aulas/05_calculadoras/aula_04_outras"
  "aulas/06_anotador/aula_01_templates"
  "aulas/06_anotador/aula_02_salvamento_busca"
  "aulas/07_rag_tribe/aula_01_embed_conceitos"
  "aulas/07_rag_tribe/aula_02_indexar_pdfs"
  "aulas/07_rag_tribe/aula_03_busca_semantica"
  "aulas/07_rag_tribe/aula_04_integracao_app"
  "aulas/08_gerador_evolucao/aula_01_gerador"
  "aulas/08_gerador_evolucao/aula_02_integracao"
  "aulas/09_testes/aula_01_tdd_pytest"
  "aulas/09_testes/aula_02_testes_calculadoras"
  "aulas/10_cicd/aula_01_forgejo_pipeline"
  "aulas/10_cicd/aula_02_woodpecker"
  "aulas/11_polimento_final/aula_01_ui_medica"
  "aulas/11_polimento_final/aula_02_exe"
  "aulas/11_polimento_final/aula_03_auditoria"
)

for d in "${dirs[@]}"; do mkdir -p "$d"; done
```

- [ ] **Step 2: Criar README.md de cada módulo (cabeçalho do módulo)**

```bash
# Módulo 00
cat > aulas/00_fundacao/README.md << 'EOF'
# Módulo 00 — Fundação

Objetivo: sair do zero absoluto com ambiente funcional e Python rodando.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | Terminal + uv: seu bisturi digital | 1h |
| 02 | Python com analogias clínicas | 1h |

Pré-requisito: computador com Linux ou WSL2.
EOF

# Módulo 01
cat > aulas/01_git/README.md << 'EOF'
# Módulo 01 — Git

Objetivo: versionar código como um prontuário — cada commit é uma entrada.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | git init, add, commit, log | 1h |
| 02 | Branch, merge e Forgejo | 1h |

Pré-requisito: Módulo 00.
EOF

# Módulo 02
cat > aulas/02_python_flet/README.md << 'EOF'
# Módulo 02 — Python + Flet

Objetivo: primeiro app médico visual rodando no navegador.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | Flet Hello World médico | 1h |
| 02 | Layout, cores e componentes Flet | 1h |

Pré-requisito: Módulos 00 e 01.
EOF

# Módulo 03
cat > aulas/03_clean_arch/README.md << 'EOF'
# Módulo 03 — Clean Architecture

Objetivo: estruturar o ClinMd-Tribe com 4 camadas sólidas como órgãos do corpo.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | As 4 camadas: analogia com sistemas do corpo | 1h |
| 02 | Scaffold do ClinMd-Tribe | 1h |

Pré-requisito: Módulos 00–02.
EOF

# Módulo 04
cat > aulas/04_agents_bigtech/README.md << 'EOF'
# Módulo 04 — Agents e BigTech Virtual

Objetivo: usar Claude Code, MCP, skills, hooks e orquestrar 63 agents especializados.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | Claude Code: seu residente de plantão 24h | 1h |
| 02 | MCP e Skills: estendendo o bisturi | 1h |
| 03 | BigTech Virtual: montando o time completo | 1h |
| 04 | /tab_pendencias: gestão ágil do projeto | 1h |

Pré-requisito: Módulos 00–03.
EOF

# Módulo 05
cat > aulas/05_calculadoras/README.md << 'EOF'
# Módulo 05 — Calculadoras Médicas

Objetivo: implementar calculadoras clínicas e psiquiátricas com TDD.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | CHA2DS2-VASc e HAS-BLED | 1h |
| 02 | PHQ-9 e GAD-7 (rastreio psiquiátrico) | 1h |
| 03 | HAM-D, YMRS, AUDIT, CAGE | 1h |
| 04 | MMSE, MoCA, PANSS, CGI + CURB-65, MELD, SOFA | 1h |

Pré-requisito: Módulos 00–04.
EOF

# Módulo 06
cat > aulas/06_anotador/README.md << 'EOF'
# Módulo 06 — Anotador Clínico

Objetivo: criar anotador com templates de evolução, atestado e receita.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | Templates profissionais (evolução, atestado, receita) | 1h |
| 02 | Salvamento automático local e busca | 1h |

Pré-requisito: Módulos 00–05.
EOF

# Módulo 07
cat > aulas/07_rag_tribe/README.md << 'EOF'
# Módulo 07 — RAG Tribe

Objetivo: busca semântica em PDFs, guidelines e protocolos pessoais.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | O que é RAG: analogia com memória médica | 1h |
| 02 | Indexar PDFs do knowledge_base/ | 1h |
| 03 | Busca semântica em produção | 1h |
| 04 | Integração com o app Flet | 1h |

Pré-requisito: Módulos 00–06.
EOF

# Módulo 08
cat > aulas/08_gerador_evolucao/README.md << 'EOF'
# Módulo 08 — Gerador de Evolução

Objetivo: gerar texto clínico pronto para colar no PEP ou TISS.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | Gerador com RAG + templates | 1h |
| 02 | Integração completa no app | 1h |

Pré-requisito: Módulos 00–07.
EOF

# Módulo 09
cat > aulas/09_testes/README.md << 'EOF'
# Módulo 09 — Testes

Objetivo: cobrir o app com testes automatizados usando TDD.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | TDD e pytest: receita em vez de intuição | 1h |
| 02 | Testes das calculadoras e RAG | 1h |

Pré-requisito: Módulos 00–08.
EOF

# Módulo 10
cat > aulas/10_cicd/README.md << 'EOF'
# Módulo 10 — CI/CD

Objetivo: pipeline automático que testa e entrega o app.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | Forgejo e pipeline CI básico | 1h |
| 02 | Woodpecker: automatizando builds | 1h |

Pré-requisito: Módulos 00–09.
EOF

# Módulo 11
cat > aulas/11_polimento_final/README.md << 'EOF'
# Módulo 11 — Polimento Final

Objetivo: UI médica profissional, exportar .exe e auditoria de qualidade.

| Aula | Título | Duração |
|------|--------|---------|
| 01 | UI médica: paleta, tipografia, ícones | 1h |
| 02 | Exportar como .exe para Windows | 1h |
| 03 | Auditoria final e distribuição | 1h |

Pré-requisito: Módulos 00–10.
EOF
```

- [ ] **Step 3: Criar arquivos README.md, roteiro.md e exercicios.md para cada aula**

```bash
# Template gerador — cria 3 arquivos por aula
create_aula() {
  local dir="$1"
  local titulo="$2"
  local prereq="$3"

  cat > "$dir/README.md" << EOF
# ${titulo}

## Objetivo
<!-- O que o aluno vai conseguir fazer ao final desta aula -->

## Pré-requisitos
${prereq}

## O que você vai entregar
- [ ] Código funcionando
- [ ] Commit no repositório
- [ ] Exercício resolvido

## Duração estimada
1 hora
EOF

  cat > "$dir/roteiro.md" << EOF
# Roteiro do Professor — ${titulo}

## Abertura (5 min)
<!-- Motivação: por que isso importa para o médico -->

## Teoria com Analogia Clínica (15 min)
<!-- Explicar o conceito técnico usando linguagem médica -->

## Demo ao Vivo (25 min)
<!-- Passo a passo com comandos copiáveis -->

\`\`\`bash
# Comandos da aula aqui
\`\`\`

## Exercício Guiado (10 min)
<!-- Aluno faz junto, professor guia -->

## Fechamento (5 min)
<!-- Resumo + próxima aula -->
EOF

  cat > "$dir/exercicios.md" << EOF
# Exercícios — ${titulo}

## Exercício 1
<!-- TODO: descreva o exercício -->

\`\`\`python
# TODO: complete o código abaixo
\`\`\`

## Gabarito
<!-- Revelar depois da tentativa do aluno -->
EOF
}

create_aula "aulas/00_fundacao/aula_01_terminal_uv" "Terminal + uv: seu bisturi digital" "Nenhum."
create_aula "aulas/00_fundacao/aula_02_python_medico" "Python com analogias clínicas" "Aula 00.01"
create_aula "aulas/01_git/aula_01_git_init_commit" "git init, add, commit, log" "Módulo 00"
create_aula "aulas/01_git/aula_02_branch_forgejo" "Branch, merge e Forgejo" "Aula 01.01"
create_aula "aulas/02_python_flet/aula_01_flet_hello" "Flet Hello World médico" "Módulos 00–01"
create_aula "aulas/02_python_flet/aula_02_flet_layout" "Layout, cores e componentes Flet" "Aula 02.01"
create_aula "aulas/03_clean_arch/aula_01_4_camadas" "As 4 camadas: analogia com sistemas do corpo" "Módulos 00–02"
create_aula "aulas/03_clean_arch/aula_02_scaffold_app" "Scaffold do ClinMd-Tribe" "Aula 03.01"
create_aula "aulas/04_agents_bigtech/aula_01_claude_code" "Claude Code: seu residente de plantão 24h" "Módulos 00–03"
create_aula "aulas/04_agents_bigtech/aula_02_mcp_skills" "MCP e Skills: estendendo o bisturi" "Aula 04.01"
create_aula "aulas/04_agents_bigtech/aula_03_bigtech_virtual" "BigTech Virtual: montando o time completo" "Aula 04.02"
create_aula "aulas/04_agents_bigtech/aula_04_tab_pendencias" "/tab_pendencias: gestão ágil do projeto" "Aula 04.03"
create_aula "aulas/05_calculadoras/aula_01_cha2ds2vasc" "CHA2DS2-VASc e HAS-BLED" "Módulos 00–04"
create_aula "aulas/05_calculadoras/aula_02_phq9_gad7" "PHQ-9 e GAD-7" "Aula 05.01"
create_aula "aulas/05_calculadoras/aula_03_hamd_ymrs" "HAM-D, YMRS, AUDIT, CAGE" "Aula 05.02"
create_aula "aulas/05_calculadoras/aula_04_outras" "MMSE, MoCA, PANSS, CGI, CURB-65, MELD, SOFA" "Aula 05.03"
create_aula "aulas/06_anotador/aula_01_templates" "Templates profissionais" "Módulos 00–05"
create_aula "aulas/06_anotador/aula_02_salvamento_busca" "Salvamento automático e busca" "Aula 06.01"
create_aula "aulas/07_rag_tribe/aula_01_embed_conceitos" "O que é RAG: analogia com memória médica" "Módulos 00–06"
create_aula "aulas/07_rag_tribe/aula_02_indexar_pdfs" "Indexar PDFs do knowledge_base/" "Aula 07.01"
create_aula "aulas/07_rag_tribe/aula_03_busca_semantica" "Busca semântica em produção" "Aula 07.02"
create_aula "aulas/07_rag_tribe/aula_04_integracao_app" "Integração RAG com app Flet" "Aula 07.03"
create_aula "aulas/08_gerador_evolucao/aula_01_gerador" "Gerador com RAG + templates" "Módulos 00–07"
create_aula "aulas/08_gerador_evolucao/aula_02_integracao" "Integração do gerador no app" "Aula 08.01"
create_aula "aulas/09_testes/aula_01_tdd_pytest" "TDD e pytest: receita em vez de intuição" "Módulos 00–08"
create_aula "aulas/09_testes/aula_02_testes_calculadoras" "Testes das calculadoras e RAG" "Aula 09.01"
create_aula "aulas/10_cicd/aula_01_forgejo_pipeline" "Forgejo e pipeline CI básico" "Módulos 00–09"
create_aula "aulas/10_cicd/aula_02_woodpecker" "Woodpecker: automatizando builds" "Aula 10.01"
create_aula "aulas/11_polimento_final/aula_01_ui_medica" "UI médica: paleta, tipografia, ícones" "Módulos 00–10"
create_aula "aulas/11_polimento_final/aula_02_exe" "Exportar como .exe para Windows" "Aula 11.01"
create_aula "aulas/11_polimento_final/aula_03_auditoria" "Auditoria final e distribuição" "Aula 11.02"
```

- [ ] **Step 4: Verificar estrutura criada**

```bash
find aulas/ -type f | sort | wc -l
# Esperado: ~120 arquivos (31 aulas × 3 arquivos + 12 README de módulo)

find aulas/ -name "README.md" | wc -l
# Esperado: 43 (12 módulos + 31 aulas)
```

- [ ] **Step 5: Commit**

```bash
git add aulas/
git commit -m "feat: scaffold 12 módulos e 31 aulas com templates"
```

---

## Task 2: Scaffold clinmd_tribe/ — Clean Architecture

**Files:**
- Create: `clinmd_tribe/pyproject.toml`
- Create: `clinmd_tribe/src/__init__.py` e sub-camadas
- Create: `clinmd_tribe/tests/__init__.py`
- Create: `clinmd_tribe/.gitignore`
- Create: `clinmd_tribe/README.md`

- [ ] **Step 1: Criar estrutura de diretórios**

```bash
mkdir -p clinmd_tribe/src/{presentation,application,domain,infrastructure}
mkdir -p clinmd_tribe/{tests,knowledge_base,data}
```

- [ ] **Step 2: Criar __init__.py e .gitkeep**

```bash
touch clinmd_tribe/src/__init__.py
touch clinmd_tribe/src/presentation/__init__.py
touch clinmd_tribe/src/application/__init__.py
touch clinmd_tribe/src/domain/__init__.py
touch clinmd_tribe/src/infrastructure/__init__.py
touch clinmd_tribe/tests/__init__.py
touch clinmd_tribe/knowledge_base/.gitkeep
touch clinmd_tribe/data/.gitkeep
```

- [ ] **Step 3: Criar pyproject.toml**

```bash
cat > clinmd_tribe/pyproject.toml << 'EOF'
[project]
name = "clinmd-tribe"
version = "0.1.0"
description = "App clínico pessoal 100% local — capstone do curso Claude Code do Zero ao Avançado"
requires-python = ">=3.11"
dependencies = [
    "flet>=0.24.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=5.0.0",
]
rag = [
    "sentence-transformers>=3.0.0",
    "chromadb>=0.5.0",
    "pypdf>=4.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
EOF
```

- [ ] **Step 4: Criar .gitignore**

```bash
cat > clinmd_tribe/.gitignore << 'EOF'
__pycache__/
*.py[cod]
*.egg-info/
.venv/
dist/
build/
.coverage
htmlcov/
data/*.db
data/*.sqlite
knowledge_base/*.pdf
EOF
```

- [ ] **Step 5: Criar README do app**

```bash
cat > clinmd_tribe/README.md << 'EOF'
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
├── presentation/    # UI Flet — telas e componentes
├── application/     # Casos de uso — orquestração
├── domain/          # Regras de negócio puras — calculadoras, modelos
└── infrastructure/  # I/O externo — arquivos, RAG, persistência
```

## Módulo do curso

Cada módulo do curso adiciona uma feature neste app. Veja `../aulas/` para o material didático.
EOF
```

- [ ] **Step 6: Verificar**

```bash
find clinmd_tribe/ -type f | sort
# Esperado: pyproject.toml, .gitignore, README.md, 5× __init__.py, 2× .gitkeep
```

- [ ] **Step 7: Commit**

```bash
git add clinmd_tribe/
git commit -m "feat: scaffold clinmd_tribe com Clean Architecture 4 camadas"
```

---

## Task 3: Criar CLAUDE.md local

**Files:**
- Create: `CLAUDE.md`

- [ ] **Step 1: Criar CLAUDE.md com conteúdo completo**

```bash
cat > CLAUDE.md << 'EOF'
# CLAUDE.md — Curso Claude Code do Zero ao Avançado

Auto-carrega em qualquer sessão Claude Code nesta pasta.

## Persona

Você é um engenheiro de computação sênior, ex-lead de dev teams, com mestrado em Pedagogia do Ensino Superior. Tem humor leve de TI com alguns memes e é extremamente prático e didático. Use agentes existentes quando aplicável.

## Contexto do Curso

- **Curso:** Claude Code do Zero ao Avançado
- **Produto capstone:** ClinMd-Tribe — app clínico 100% local (Flet + Python)
- **Parceria:** Dr. Petrus Silva Costa × Luiz Dieckmann (TribeMD)
- **Turma:** Fechada — médicos selecionados
- **Carga:** ~28 aulas de 1h, entrega 1/semana ao editor do Dieckmann
- **Líder supremo:** Dr. Petrus Silva Costa — todas as decisões passam por ele

## Aluno-alvo

Médico experiente em medicina, zero em TI. Sabe o que é uma veia mas não sabe o que é um terminal. Ensinar como se explicasse um novo protocolo clínico: do básico ao avançado, sem pular etapas.

## Stack Obrigatória

- Python 3.11+
- Flet (roda no navegador + exportável para .exe)
- uv como gerenciador de pacotes
- Clean Architecture (4 camadas: presentation, application, domain, infrastructure)
- RAG local (ChromaDB + sentence-transformers)

## Regras de Ensino (SEMPRE seguir)

1. Use linguagem médica com analogias clínicas para cada conceito técnico
2. Forneça comandos sempre em blocos copiáveis
3. Use passos numerados, nunca pule etapas
4. Seja paciente, motivador e prático
5. Cada resposta deve ensinar + avançar o projeto simultaneamente
6. Transforme cada aula em uma User Story real

## BigTech Virtual (OBRIGATÓRIO)

Constelação de agents em `~/.claude/agents/`:

| Agent | Papel |
|-------|-------|
| Celso | CEO |
| Caetano | CTO |
| Capitolino | CPO |
| Camilo | CMO |
| Cosmo | COO |
| Narciso | CISO |
| Cândido | CDO |
| Caio | CAIO |
| Confúcio | CFO |
| Cícero | CRO |
| Cláudio | CLO |
| Cósimo | Chief of Staff |

Agents operacionais: backend-engineer, frontend-engineer, qa-engineer, devops-sre, data-engineer, ml-engineer, security-engineer, e ~50 outros.

Skill `/bigtech` invoca Cósimo e monta o time completo.
Skill `/tab_pendencias` cria tabela de pendências ordenada por dependência e valor.
**Módulo 04 tem aula dedicada a cada um destes.**

## Mapa de Módulos

| Módulo | Conteúdo | Aulas |
|--------|----------|-------|
| 00_fundacao | Terminal, uv, Python básico com analogias médicas | 2 |
| 01_git | git init → commit → branch → Forgejo | 2 |
| 02_python_flet | Python clínico, Flet hello world médico | 2 |
| 03_clean_arch | 4 camadas, scaffold ClinMd-Tribe | 2 |
| 04_agents_bigtech | Claude Code, API, MCP, skills, hooks, /tab_pendencias, BigTech Virtual | 4 |
| 05_calculadoras | CHA2DS2-VASc, PHQ-9+GAD-7, HAM-D+YMRS, outros | 4 |
| 06_anotador | Templates, salvamento local, busca | 2 |
| 07_rag_tribe | Embed, indexar PDFs, busca semântica, integração | 4 |
| 08_gerador_evolucao | Gerar texto para PEP/TISS | 2 |
| 09_testes | TDD, pytest, cobertura | 2 |
| 10_cicd | Forgejo + Woodpecker, pipeline CI | 2 |
| 11_polimento_final | UI médica, .exe, auditoria, distribuição | 3 |

**Total: 31 aulas**

## Links Canônicos (Vault)

- `~/IDrive/Documentos/projetos_claudebrain/CONTRACT.md`
- `~/IDrive/Documentos/projetos_claudebrain/TESTES.md`
- `~/IDrive/Documentos/projetos_claudebrain/AGILE.md`
- `~/IDrive/Documentos/projetos_claudebrain/DEPLOY_CHECKLIST.md`
- `~/IDrive/Documentos/projetos_claudebrain/AUDITORIAS.md`
- `~/IDrive/Documentos/projetos_claudebrain/TOOLING.md`

## Regra de Design (CRÍTICA)

NUNCA tomar decisões de arquitetura, stack, escopo ou design sem:
1. Apresentar 2–3 alternativas com prós/contras
2. Indicar qual é a opção recomendada
3. Aguardar aprovação do Dr. Petrus

## Apêndice Opcional

Grok Build — mencionado pelo Dr. Petrus como possível apêndice pós-módulo 11. Decisão a ser tomada após módulo 10.
EOF
```

- [ ] **Step 2: Verificar**

```bash
wc -l CLAUDE.md
# Esperado: > 80 linhas
grep "BigTech" CLAUDE.md
# Esperado: linha com "BigTech Virtual"
```

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "feat: adiciona CLAUDE.md local com persona, módulos e BigTech Virtual"
```

---

## Task 4: Recriar roadmap.html com 12 módulos

**Files:**
- Modify: `roadmap.html` (substituição completa)

- [ ] **Step 1: Substituir roadmap.html**

Escrever novo `roadmap.html` com os 12 módulos, mesmo estilo visual (dark, Tailwind CDN, gradiente azul no header). Conteúdo:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ClinMd-Tribe • Roadmap do Curso Claude Code</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: 'Inter', system-ui, sans-serif; }
        .header-bg { background: linear-gradient(135deg, #1e40af, #3b82f6); }
    </style>
</head>
<body class="bg-slate-950 text-slate-200">
    <div class="max-w-4xl mx-auto p-8">

        <!-- Header -->
        <div class="header-bg rounded-2xl p-10 text-white mb-10 shadow-2xl">
            <div class="flex items-center gap-4 mb-6">
                <div class="w-16 h-16 bg-white rounded-2xl flex items-center justify-center text-4xl">🩺</div>
                <div>
                    <h1 class="text-4xl font-bold">ClinMd-Tribe</h1>
                    <p class="text-xl opacity-90">Claude Code do Zero ao Avançado</p>
                </div>
            </div>
            <p class="text-lg max-w-lg">31 aulas práticas para médicos criarem seu app clínico pessoal 100% local — do terminal ao .exe.</p>
            <div class="mt-6 flex flex-wrap gap-3">
                <div class="bg-white/20 px-4 py-2 rounded-xl text-sm">Flet + Python</div>
                <div class="bg-white/20 px-4 py-2 rounded-xl text-sm">Clean Architecture</div>
                <div class="bg-white/20 px-4 py-2 rounded-xl text-sm">RAG Local</div>
                <div class="bg-white/20 px-4 py-2 rounded-xl text-sm">Claude Code + Agents</div>
                <div class="bg-white/20 px-4 py-2 rounded-xl text-sm">CI/CD</div>
            </div>
        </div>

        <!-- Visão Geral -->
        <div class="mb-12">
            <h2 class="text-3xl font-semibold mb-4 text-emerald-400">📋 Visão Geral</h2>
            <p class="text-slate-300 leading-relaxed">
                Do zero absoluto (abrir o terminal) ao avançado (orquestração de agents em paralelo).
                Cada aula tem <strong>~1 hora</strong> e entrega um commit real no app ClinMd-Tribe.
                Parceria <strong>Dr. Petrus Silva Costa × TribeMD (Dieckmann)</strong>.
            </p>
        </div>

        <!-- Módulos -->
        <div class="space-y-6">

            <!-- Módulo 00 -->
            <div class="bg-slate-900 border border-slate-700 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-blue-600 rounded-xl flex items-center justify-center text-lg font-bold">00</div>
                    <div>
                        <h3 class="text-xl font-bold">Fundação</h3>
                        <p class="text-slate-400 text-sm">2 aulas · Terminal, uv, Python médico</p>
                    </div>
                </div>
                <ul class="text-slate-400 text-sm space-y-1 ml-12">
                    <li>• Aula 01 — Terminal + uv: seu bisturi digital</li>
                    <li>• Aula 02 — Python com analogias clínicas</li>
                </ul>
            </div>

            <!-- Módulo 01 -->
            <div class="bg-slate-900 border border-slate-700 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-blue-600 rounded-xl flex items-center justify-center text-lg font-bold">01</div>
                    <div>
                        <h3 class="text-xl font-bold">Git</h3>
                        <p class="text-slate-400 text-sm">2 aulas · Versionamento e Forgejo</p>
                    </div>
                </div>
                <ul class="text-slate-400 text-sm space-y-1 ml-12">
                    <li>• Aula 01 — git init, add, commit, log</li>
                    <li>• Aula 02 — Branch, merge e Forgejo</li>
                </ul>
            </div>

            <!-- Módulo 02 -->
            <div class="bg-slate-900 border border-slate-700 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-purple-600 rounded-xl flex items-center justify-center text-lg font-bold">02</div>
                    <div>
                        <h3 class="text-xl font-bold">Python + Flet</h3>
                        <p class="text-slate-400 text-sm">2 aulas · Primeiro app médico visual</p>
                    </div>
                </div>
                <ul class="text-slate-400 text-sm space-y-1 ml-12">
                    <li>• Aula 01 — Flet Hello World médico</li>
                    <li>• Aula 02 — Layout, cores e componentes Flet</li>
                </ul>
            </div>

            <!-- Módulo 03 -->
            <div class="bg-slate-900 border border-slate-700 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-purple-600 rounded-xl flex items-center justify-center text-lg font-bold">03</div>
                    <div>
                        <h3 class="text-xl font-bold">Clean Architecture</h3>
                        <p class="text-slate-400 text-sm">2 aulas · 4 camadas, scaffold do app</p>
                    </div>
                </div>
                <ul class="text-slate-400 text-sm space-y-1 ml-12">
                    <li>• Aula 01 — As 4 camadas: analogia com sistemas do corpo</li>
                    <li>• Aula 02 — Scaffold do ClinMd-Tribe</li>
                </ul>
            </div>

            <!-- Módulo 04 -->
            <div class="bg-slate-900 border border-amber-700/50 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-amber-600 rounded-xl flex items-center justify-center text-lg font-bold">04</div>
                    <div>
                        <h3 class="text-xl font-bold">Agents e BigTech Virtual</h3>
                        <p class="text-slate-400 text-sm">4 aulas · Claude Code, MCP, skills, 63 agents</p>
                    </div>
                </div>
                <ul class="text-slate-400 text-sm space-y-1 ml-12">
                    <li>• Aula 01 — Claude Code: seu residente de plantão 24h</li>
                    <li>• Aula 02 — MCP e Skills: estendendo o bisturi</li>
                    <li>• Aula 03 — BigTech Virtual: montando o time completo</li>
                    <li>• Aula 04 — /tab_pendencias: gestão ágil do projeto</li>
                </ul>
            </div>

            <!-- Módulo 05 -->
            <div class="bg-slate-900 border border-slate-700 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-rose-600 rounded-xl flex items-center justify-center text-lg font-bold">05</div>
                    <div>
                        <h3 class="text-xl font-bold">Calculadoras Médicas</h3>
                        <p class="text-slate-400 text-sm">4 aulas · Clínicas + Psiquiatria</p>
                    </div>
                </div>
                <div class="ml-12 grid grid-cols-2 gap-4 text-sm text-slate-400">
                    <div>
                        <p class="text-amber-400 font-semibold mb-1">Clínicas</p>
                        <p>CHA2DS2-VASc, HAS-BLED, CURB-65, MELD, SOFA</p>
                    </div>
                    <div>
                        <p class="text-amber-400 font-semibold mb-1">Psiquiatria</p>
                        <p>PHQ-9, GAD-7, HAM-D, YMRS, AUDIT, CAGE, MMSE, MoCA, PANSS, CGI</p>
                    </div>
                </div>
            </div>

            <!-- Módulo 06 -->
            <div class="bg-slate-900 border border-slate-700 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-rose-600 rounded-xl flex items-center justify-center text-lg font-bold">06</div>
                    <div>
                        <h3 class="text-xl font-bold">Anotador Clínico</h3>
                        <p class="text-slate-400 text-sm">2 aulas · Templates, salvamento, busca</p>
                    </div>
                </div>
                <ul class="text-slate-400 text-sm space-y-1 ml-12">
                    <li>• Aula 01 — Templates profissionais (evolução, atestado, receita)</li>
                    <li>• Aula 02 — Salvamento automático local e busca</li>
                </ul>
            </div>

            <!-- Módulo 07 -->
            <div class="bg-slate-900 border border-cyan-700/50 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-cyan-600 rounded-xl flex items-center justify-center text-lg font-bold">07</div>
                    <div>
                        <h3 class="text-xl font-bold">RAG Tribe</h3>
                        <p class="text-slate-400 text-sm">4 aulas · Busca semântica em PDFs e guidelines</p>
                    </div>
                </div>
                <ul class="text-slate-400 text-sm space-y-1 ml-12">
                    <li>• Aula 01 — O que é RAG: analogia com memória médica</li>
                    <li>• Aula 02 — Indexar PDFs do knowledge_base/</li>
                    <li>• Aula 03 — Busca semântica em produção</li>
                    <li>• Aula 04 — Integração RAG com app Flet</li>
                </ul>
            </div>

            <!-- Módulo 08 -->
            <div class="bg-slate-900 border border-slate-700 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-orange-600 rounded-xl flex items-center justify-center text-lg font-bold">08</div>
                    <div>
                        <h3 class="text-xl font-bold">Gerador de Evolução</h3>
                        <p class="text-slate-400 text-sm">2 aulas · Texto pronto para PEP/TISS</p>
                    </div>
                </div>
                <ul class="text-slate-400 text-sm space-y-1 ml-12">
                    <li>• Aula 01 — Gerador com RAG + templates</li>
                    <li>• Aula 02 — Integração completa no app</li>
                </ul>
            </div>

            <!-- Módulo 09 -->
            <div class="bg-slate-900 border border-slate-700 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-green-600 rounded-xl flex items-center justify-center text-lg font-bold">09</div>
                    <div>
                        <h3 class="text-xl font-bold">Testes</h3>
                        <p class="text-slate-400 text-sm">2 aulas · TDD e pytest</p>
                    </div>
                </div>
                <ul class="text-slate-400 text-sm space-y-1 ml-12">
                    <li>• Aula 01 — TDD e pytest: receita em vez de intuição</li>
                    <li>• Aula 02 — Testes das calculadoras e RAG</li>
                </ul>
            </div>

            <!-- Módulo 10 -->
            <div class="bg-slate-900 border border-slate-700 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-green-600 rounded-xl flex items-center justify-center text-lg font-bold">10</div>
                    <div>
                        <h3 class="text-xl font-bold">CI/CD</h3>
                        <p class="text-slate-400 text-sm">2 aulas · Forgejo + Woodpecker</p>
                    </div>
                </div>
                <ul class="text-slate-400 text-sm space-y-1 ml-12">
                    <li>• Aula 01 — Forgejo e pipeline CI básico</li>
                    <li>• Aula 02 — Woodpecker: automatizando builds</li>
                </ul>
            </div>

            <!-- Módulo 11 -->
            <div class="bg-slate-900 border border-emerald-700/50 rounded-2xl p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-9 h-9 bg-emerald-600 rounded-xl flex items-center justify-center text-lg font-bold">11</div>
                    <div>
                        <h3 class="text-xl font-bold">Polimento Final</h3>
                        <p class="text-slate-400 text-sm">3 aulas · UI, .exe, auditoria</p>
                    </div>
                </div>
                <ul class="text-slate-400 text-sm space-y-1 ml-12">
                    <li>• Aula 01 — UI médica: paleta, tipografia, ícones</li>
                    <li>• Aula 02 — Exportar como .exe para Windows</li>
                    <li>• Aula 03 — Auditoria final e distribuição</li>
                </ul>
            </div>

        </div>

        <!-- Footer -->
        <div class="mt-16 text-center text-slate-500 text-sm">
            <p class="text-lg font-semibold text-slate-300 mb-2">Total: 31 aulas · ~31 horas</p>
            <p>ClinMd-Tribe • Curso Claude Code do Zero ao Avançado</p>
            <p class="mt-1">Dr. Petrus Silva Costa × TribeMD (Luiz Dieckmann)</p>
        </div>
    </div>
</body>
</html>
```

- [ ] **Step 2: Verificar HTML**

```bash
grep -c "Módulo\|Aula" roadmap.html
# Esperado: > 50 ocorrências
wc -l roadmap.html
# Esperado: > 150 linhas
```

- [ ] **Step 3: Commit**

```bash
git add roadmap.html
git commit -m "feat: roadmap.html atualizado com 12 módulos e 31 aulas"
```

---

## Task 5: Criar README.md raiz

**Files:**
- Create: `README.md`

- [ ] **Step 1: Criar README.md**

```bash
cat > README.md << 'EOF'
# Claude Code do Zero ao Avançado

Curso prático de Claude Code para médicos.
Produto final: **ClinMd-Tribe** — app clínico 100% local.

**Parceria:** Dr. Petrus Silva Costa × TribeMD (Luiz Dieckmann)

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
EOF
```

- [ ] **Step 2: Verificar**

```bash
wc -l README.md
# Esperado: > 40 linhas
```

- [ ] **Step 3: Commit final**

```bash
git add README.md
git commit -m "feat: README.md raiz com mapa completo do curso"
```

---

## Self-Review

**Spec coverage:**
- ✅ 12 módulos em `aulas/` — Task 1
- ✅ `clinmd_tribe/` Clean Architecture — Task 2
- ✅ CLAUDE.md local completo — Task 3
- ✅ `roadmap.html` atualizado — Task 4
- ✅ README.md raiz — Task 5
- ✅ `/tab_pendencias` mencionada em CLAUDE.md e módulo 04 — Task 1 + Task 3
- ✅ BigTech Virtual com 63 agents — Task 3
- ✅ Grok Build como apêndice opcional — Task 3

**Placeholder scan:** nenhum TBD/TODO/placeholder em tasks não-scaffold.

**Type consistency:** n/a (sem código de produção neste plano — só scaffold).
