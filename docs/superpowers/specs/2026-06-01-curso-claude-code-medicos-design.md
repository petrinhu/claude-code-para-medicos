# Design Spec — Curso "Claude Code do Zero ao Avançado" para Médicos

**Data:** 2026-06-01  
**Autor:** Dr. Petrus Silva Costa  
**Parceiro:** Luiz Dieckmann (TribeMD)  
**Status:** Aprovado pelo Dr. Petrus

---

## Contexto

Curso prático de Claude Code e desenvolvimento de software para médicos.  
Produto capstone: **ClinMd-Tribe** — app clínico 100% local (Flet + Python).  
Distribuição: turma fechada (parceria Petrus × TribeMD).  
Contrapartida: assinatura anual TribeMD Assist + logo de parceiro no site de Petrus.

---

## Escopo

- ~28 aulas de 1h cada
- Do zero absoluto (abrir terminal) ao avançado (orquestração de agents em paralelo)
- Cobre: terminal, git, CI/CD, Clean Architecture, Flet, RAG local, API Claude, MCP, skills, hooks, BigTech Virtual (63 agents)
- Cada aula = user story real + commit no `clinmd_tribe/`

---

## Estrutura de Pastas

```
aulas_claude_dieckmann/
├── aulas/
│   ├── 00_fundacao/           # terminal, uv, Python básico com analogias médicas
│   ├── 01_git/                # git init → commit → branch → Forgejo
│   ├── 02_python_flet/        # Python clínico, Flet hello world médico
│   ├── 03_clean_arch/         # 4 camadas, scaffold clinmd_tribe
│   ├── 04_agents_bigtech/     # Claude Code, API, MCP, skills, hooks, /tab_pendencias, BigTech Virtual
│   ├── 05_calculadoras/       # CHA2DS2-VASc, PHQ-9+GAD-7, HAM-D+YMRS, +outros
│   ├── 06_anotador/           # templates, salvamento local, busca
│   ├── 07_rag_tribe/          # embed, indexar PDFs, busca semântica, integração
│   ├── 08_gerador_evolucao/   # gerar texto para PEP/TISS
│   ├── 09_testes/             # TDD, pytest, testes de calculadoras
│   ├── 10_cicd/               # Forgejo + Woodpecker, pipeline CI
│   └── 11_polimento_final/    # UI médica, .exe, auditoria, distribuição
│
├── clinmd_tribe/
│   ├── src/
│   │   ├── presentation/
│   │   ├── application/
│   │   ├── domain/
│   │   └── infrastructure/
│   ├── tests/
│   ├── knowledge_base/
│   └── data/
│
├── docs/
│   └── superpowers/specs/
├── workshop_iago/             # material Dieckmann (já existente)
├── projeto.txt
├── roadmap.html               # atualizado com os 12 módulos
├── conversa.txt
└── CLAUDE.md
```

---

## Template de Aula

Cada aula segue estrutura consistente:

```
aulas/05_calculadoras/
└── aula_01_cha2ds2vasc/
    ├── README.md       # guia do aluno: objetivo, pré-requisitos, o que entregar
    ├── roteiro.md      # script do professor (Dr. Petrus): passo a passo detalhado
    └── exercicios.md   # TODOs comentados para o aluno resolver
```

---

## Evolução do App (Commits por Módulo)

| Módulo | Entrega no `clinmd_tribe/` |
|--------|---------------------------|
| 00 | pyproject.toml + estrutura vazia |
| 01 | .gitignore + primeiro commit real |
| 02 | main.py Flet com tela de boas-vindas médica |
| 03 | 4 camadas Clean Arch scaffoldadas |
| 04 | CLAUDE.md do app + agents configurados |
| 05 | Calculadoras clínicas + psiquiátricas funcionando |
| 06 | Anotador com templates e salvamento local |
| 07 | RAG indexando PDFs do `knowledge_base/` |
| 08 | Gerador de evolução clínica |
| 09 | Suite pytest verde (TDD) |
| 10 | Pipeline CI passando no Woodpecker |
| 11 | .exe gerado + UI médica polida + auditoria |

---

## CLAUDE.md Local — Conteúdo

1. **Persona**: engenheiro sênior + mestre em pedagogia, humor leve de TI, didático para médicos
2. **Contexto**: ClinMd-Tribe para TribeMD, turma fechada, 28 aulas
3. **Stack obrigatória**: Python 3.11+, Flet, uv, Clean Architecture 4 camadas, RAG local
4. **Regras de ensino**: linguagem médica, analogias clínicas, comandos copiáveis, passos numerados, paciente e motivador
5. **BigTech Virtual**: referência à constelação `~/.claude/agents/` (Celso/CEO, Caetano/CTO, etc.)
6. **Links canônicos**: CONTRACT.md, AGILE.md, TESTES.md, DEPLOY_CHECKLIST.md, TOOLING.md do vault
7. **Mapa de módulos**: 12 módulos com épico correspondente
8. **Regra de design**: nunca decidir arquitetura sozinho — apresentar 2-3 opções ao Dr. Petrus

---

## Calculadoras Médicas (Épico 5)

**Clínicas:** CHA2DS2-VASc, HAS-BLED, CURB-65, MELD, SOFA, APACHE II  
**Psiquiatria (alta prioridade):** PHQ-9, GAD-7, HAM-D (Hamilton), YMRS (Young Mania), AUDIT, CAGE, MMSE, MoCA, PANSS, CGI

---

## Apêndice Opcional

- **Grok Build**: mencionado por Petrus como possível apêndice pós-curso (conforme conversa.txt). Não faz parte do currículo principal. Decisão final do Dr. Petrus antes do módulo 11.

---

## Critérios de Sucesso

- Médico sem experiência em TI consegue rodar o app até a aula 5
- Cada aula tem ≥1 commit real no repo
- Suite de testes verde no CI antes do módulo 11
- App exportável como `.exe` e usável em consultório real
- Material pode ser entregue ao editor do Dieckmann (1 aula/semana)
