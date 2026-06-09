# Aula 24 — Roteiro Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Escrever o roteiro completo da aula_24 (MELD + MMSE, arco duplo simétrico, ~58 min) em `aula_24/roteiro.md` e gerar `aula_24/roteiro.html` via pandoc.

**Architecture:** Documento de roteiro de gravação seguindo o padrão canônico do curso (seções numeradas, Tom, falas entre aspas, blocos copiáveis, tabelas clínicas). 10 seções cobrindo dois arcos completos: MELD (seções 1–5) e MMSE (seções 6–10). Zero código escrito pelo aluno — professor conduz prompts descritivos.

**Tech Stack:** Markdown + pandoc para geração HTML.

---

## Arquivos

- **Criar/Sobrescrever:** `aula_24/roteiro.md` (roteiro completo ~600-700 linhas)
- **Gerar:** `aula_24/roteiro.html` via pandoc
- **Referência de formato:** `aula_23/roteiro.md` (padrão canônico)
- **Spec:** `docs/superpowers/specs/2026-06-09-aula24-design.md`

---

## Conteúdo por seção (resumo para execução)

| # | Seção | Min | Conteúdo-chave |
|---|---|---|---|
| 1 | Abertura | 3 | Dois paradigmas novos — fórmula + composto |
| 2 | MELD como especificação | 7 | Fórmula ln, faixas mortalidade, caso âncora manual 4.5/1.8/1.2→20 |
| 3 | Prompt MELD | 6 | float, min=1.0, math.log — professor conduz |
| 4 | Claude implementa MELD + leitura | 10 | 4 perguntas (float, log natural, min=1.0 no domínio ←crítica, service) |
| 5 | App ao vivo MELD + validação | 5 | Caso 1 bili=4.5→20→19.6%, Caso 2 bili=8.0→31→52.6% |
| 6 | MMSE como especificação | 6 | 6 subtestes limites heterogêneos 5/5/3/5/3/9, caso âncora 3/4/2/3/1/7→20 |
| 7 | Prompt MMSE | 5 | Limites por subteste, tooltip ⚙ pentágonos |
| 8 | Claude implementa MMSE + leitura | 8 | 3 perguntas (limites, cutoff 24, service) |
| 9 | App ao vivo MMSE + validação | 4 | Caso 3 →20→leve, Caso 4 →7→grave |
| 10 | Encerramento + bridge S06 | 4 | S05 encerrado, 6 calculadoras, 3 paradigmas, próxima: dinheiro |

---

## Task 1: Escrever aula_24/roteiro.md

**Files:**
- Create: `aula_24/roteiro.md`

- [ ] **Step 1: Escrever o roteiro completo**

Conteúdo abaixo (completo, sem placeholders).

Ver seção "Roteiro completo" abaixo.

- [ ] **Step 2: Verificar contagem de seções**

```bash
grep "^## SEÇÃO" aula_24/roteiro.md | wc -l
```
Esperado: 10

- [ ] **Step 3: Commit roteiro.md**

```bash
git add aula_24/roteiro.md
git commit -m "feat: aula_24 roteiro.md gerado"
```

---

## Task 2: Gerar aula_24/roteiro.html

**Files:**
- Generate: `aula_24/roteiro.html`

- [ ] **Step 1: Gerar HTML via pandoc**

```bash
pandoc aula_24/roteiro.md -o aula_24/roteiro.html --standalone --metadata title="Aula 24 — MELD + MMSE"
```

- [ ] **Step 2: Verificar tamanho**

```bash
wc -l aula_24/roteiro.html
```
Esperado: > 100 linhas

- [ ] **Step 3: Commit HTML**

```bash
git add aula_24/roteiro.html
git commit -m "feat: aula_24 roteiro.html gerado"
```

---

## Task 3: Atualizar TODO.md

**Files:**
- Modify: `TODO.md`

- [ ] **Step 1: Mover S05.04 de ⏳ para ✅**

Remover da tabela ⏳:
```
| S05.04 | 10 | Avançado · S05 Calculadoras | MELD + MMSE → aula_24 ... | Média | S05.03 | Médio | ⏳ Pendente | ⏳ |
```

Adicionar na tabela ✅:
```
| S05.04 | 10 | Avançado · S05 Calculadoras | MELD + MMSE → aula_24 (padrões novos: fórmula contínua + scoring composto) | Média | S05.03 | Médio | ✅ Concluído | ✅ |
```

Atualizar cabeçalho: `33 ✅ · 0 🚫 · 19 ⏳` → `34 ✅ · 0 🚫 · 18 ⏳`

- [ ] **Step 2: Commit TODO.md**

```bash
git add TODO.md
git commit -m "chore: TODO.md — S05.04 ✅, contadores 34✅/18⏳"
```
