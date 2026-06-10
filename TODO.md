# TODO — Curso Claude Code para Médicos
> **Fonte de verdade:** `arvore_aulas.html` · Atualizado: 2026-06-09
> **Legenda:** ✅ Concluído · 🚫 Refatorar (conteúdo ≠ HTML) · ⏳ Pendente
> **Resumo:** 44 ✅ · 0 🚫 · 8 ⏳ · **Total: 52 aulas**
>
> Nota: condensação de aulas é permitida (45–60 min por aula). 🚫 marca apenas **conteúdo errado ou ausente**, não quantidade de aulas.
> `aula_abertura` existe mas não é numerada no HTML — mantida como intro especial fora da contagem.

---

## 🚫 Refatorar — 0 itens

Nenhuma aula pendente de refatoração. Todas as correções de conteúdo foram concluídas.

---

## ⏳ Pendente — 8 itens

| ID | Onda | Grupo | Descrição | Prioridade | Pré-req | Dificuldade | Status | Auditado |
|---|:---:|---|---|:---:|---|:---:|:---:|:---:|
| S10.01 | 15 | Avançado · S10 CI/CD | Forgejo e pipeline CI básico → aula_35 | Baixa | S09 | Complexo | ⏳ Pendente | ⏳ |
| S10.02 | 15 | Avançado · S10 CI/CD | Woodpecker: automatizando builds → aula_36 | Baixa | S10.01 | Complexo | ⏳ Pendente | ⏳ |
| S11.01 | 16 | Avançado · S11 Polimento | UI médica: paleta, tipografia, ícones → aula_37 | Baixa | S10 | Médio | ⏳ Pendente | ⏳ |
| S11.02 | 16 | Avançado · S11 Polimento | Exportar como .exe para Windows → aula_38 | Baixa | S11.01 | Médio | ⏳ Pendente | ⏳ |
| S11.03 | 16 | Avançado · S11 Polimento | Auditoria final e distribuição → aula_39 | Baixa | S11.02 | Médio | ⏳ Pendente | ⏳ |
| S12.01 | 17 | Avançado · S12 Boas Práticas | Segurança: nunca suba seu token de API → aula_40 | Baixa | S11 | Simples | ⏳ Pendente | ⏳ |
| S12.02 | 17 | Avançado · S12 Boas Práticas | Arquitetura modular: evitando o monolito → aula_41 | Baixa | S11 | Simples | ⏳ Pendente | ⏳ |
| S12.03 | 17 | Avançado · S12 Boas Práticas | Workflow com agentes: sempre discuta com o time (C-levels + devs) → aula_42 | Baixa | S11 | Simples | ⏳ Pendente | ⏳ |

---

## ✅ Concluído — 44 itens

| ID | Onda | Grupo | Descrição | Prioridade | Pré-req | Dificuldade | Status | Auditado |
|---|:---:|---|---|:---:|---|:---:|:---:|:---:|
| M0.01 | 1 | Iniciante · M0 | O que é o Claude Code → aula_01 (~50-55 min, Demo-First, CC=prontuário/Web UI=post-it, condensado com M0.02-05) | Alta | — | Simples | ✅ Concluído | ✅ |
| M0.02 | 1 | Iniciante · M0 | Instalação e primeiro contato → aula_01 (condensado) | Alta | M0.01 | Simples | ✅ Concluído | ✅ |
| M0.03 | 1 | Iniciante · M0 | Como conversar: pedir, anexar, revisar e iterar → aula_01 (condensado) | Alta | M0.01 | Simples | ✅ Concluído | ✅ |
| M0.04 | 1 | Iniciante · M0 | Bons hábitos de prompt para o contexto clínico → aula_01 (condensado) | Alta | M0.01 | Simples | ✅ Concluído | ✅ |
| M0.05 | 1 | Iniciante · M0 | Claude Code no celular: /remote → aula_01 (condensado) | Alta | M0.01 | Simples | ✅ Concluído | ✅ |
| M1.01 | 2 | Iniciante · M1 | Trabalhar com arquivos: PDFs, bullets, tabelas → aula_02 (~46-50 min, demo encadeada, tema depressão/APA, condensado com M1.02-04) | Alta | M0 | Simples | ✅ Concluído | ✅ |
| M1.02 | 2 | Iniciante · M1 | Gerar documentos: folhetos, ofícios, modelos → aula_02 (condensado) | Alta | M0 | Simples | ✅ Concluído | ✅ |
| M1.03 | 2 | Iniciante · M1 | Slides a partir de tópicos soltos → aula_02 (condensado) | Alta | M0 | Simples | ✅ Concluído | ✅ |
| M1.04 | 2 | Iniciante · M1 | Planilhas: organizar, limpar, gerar gráficos → aula_02 (condensado) | Alta | M0 | Simples | ✅ Concluído | ✅ |
| M3.05 | 4 | Intermediário · M3 | Gestão do consultório: indicadores, faturamento e automação → aula_07 (~48 min, metabologista, dashboard HTML self-contained) | Alta | M2 | Simples | ✅ Concluído | ✅ |
| M2.01 | 3 | Intermediário · M2 | Buscar e triar artigos pelo conector de PubMed → aula_03 (condensado com M2.02) | Média | M1 | Simples | ✅ Concluído | ✅ |
| M2.02 | 3 | Intermediário · M2 | Fichamento e leitura crítica: PICO, nível de evidência, vieses → aula_03 (condensado) | Média | M1 | Simples | ✅ Concluído | ✅ |
| M2.03 | 3 | Intermediário · M2 | Flashcards (Anki) e simulados a partir de guidelines → aula_04 (condensado com M2.04) | Média | M1 | Simples | ✅ Concluído | ✅ |
| M2.04 | 3 | Intermediário · M2 | Briefing automático: resumo das novidades toda manhã → aula_04 (condensado) | Média | M1 | Simples | ✅ Concluído | ✅ |
| M3.01 | 4 | Intermediário · M3 | Posts e carrosséis para redes sociais → aula_05 (condensado com M3.02) | Média | M2 | Simples | ✅ Concluído | ✅ |
| M3.02 | 4 | Intermediário · M3 | Newsletter e blog com SEO → aula_05 (condensado) | Média | M2 | Simples | ✅ Concluído | ✅ |
| M3.03 | 4 | Intermediário · M3 | Pôster e slides de congresso → aula_06 (condensado com M3.04) | Média | M2 | Simples | ✅ Concluído | ✅ |
| M3.04 | 4 | Intermediário · M3 | Estatística de dados anonimizados e gráficos para publicação → aula_06 (condensado) | Média | M2 | Simples | ✅ Concluído | ✅ |
| S00.01 | 5 | Avançado · S00 Git | Git: o prontuário do seu código (init, add, commit, log) → aula_08 | Média | M3 | Simples | ✅ Concluído | ✅ |
| S00.02 | 5 | Avançado · S00 Git | Git remoto: GitHub e clone de ferramentas → aula_09 | Média | S00.01 | Simples | ✅ Concluído | ✅ |
| S01.01 | 6 | Avançado · S01 Fundação | Terminal + uv: seu bisturi digital → aula_10 (~48 min, fusão 10+11; aula_11 deprecada) | Alta | S00 | Médio | ✅ Concluído | ✅ |
| S01.02 | 6 | Avançado · S01 Fundação | Python com analogias clínicas → aula_12 | Média | S01.01 | Médio | ✅ Concluído | ✅ |
| S02.01 | 7 | Avançado · S02 Python+Flet | Flet Hello World médico → aula_13 | Média | S01 | Médio | ✅ Concluído | ✅ |
| S02.02 | 7 | Avançado · S02 Python+Flet | Layout, cores e componentes Flet → aula_14 | Média | S02.01 | Médio | ✅ Concluído | ✅ |
| S03.01 | 8 | Avançado · S03 Clean Arch | As 4 camadas: analogia com sistemas do corpo → aula_15 | Média | S02 | Médio | ✅ Concluído | ✅ |
| S03.02 | 8 | Avançado · S03 Clean Arch | Scaffold do ClinMd-Tribe → aula_16 | Média | S03.01 | Médio | ✅ Concluído | ✅ |
| S04.01 | 9 | Avançado · S04 Agents | Claude Code: seu residente de plantão 24h → aula_17 | Média | S03 | Médio | ✅ Concluído | ✅ |
| S04.02 | 9 | Avançado · S04 Agents | MCP e Skills: estendendo o bisturi → aula_18 (expandido; ver docs/decisoes_curriculo.md) | Média | S04.01 | Médio | ✅ Concluído | ✅ |
| S04.03 | 9 | Avançado · S04 Agents | BigTech Virtual: montando o time completo → aula_19 | Média | S04.01 | Médio | ✅ Concluído | ✅ |
| S04.04 | 9 | Avançado · S04 Agents | /tab_pendencias: gestão ágil do projeto → aula_20 | Média | S04.01 | Médio | ✅ Concluído | ✅ |
| S05.01 | 10 | Avançado · S05 Calculadoras | CHA₂DS₂-VASc → aula_21 (~55 min, cardiologista, prompt único descritivo) | Alta | S04 | Médio | ✅ Concluído | ✅ |
| S05.02 | 10 | Avançado · S05 Calculadoras | HAS-BLED → aula_22 (~45 min, cardiologista, painel decisão FA) | Alta | S05.01 | Médio | ✅ Concluído | ✅ |
| S05.03 | 10 | Avançado · S05 Calculadoras | PHQ-9 e GAD-7 → aula_23 (paradigma Likert 0-3) | Alta | S05.02 | Médio | ✅ Concluído | ✅ |
| S05.04 | 10 | Avançado · S05 Calculadoras | MELD + MMSE → aula_24 (padrões novos: fórmula contínua + scoring composto) | Média | S05.03 | Médio | ✅ Concluído | ✅ |
| S06.01 | 11 | Avançado · S06 Dashboard | Entrada de dados: formulários mensais (receita, glosas, consultas) → aula_25 | Média | S04 | Médio | ✅ Concluído | ✅ |
| S06.02 | 11 | Avançado · S06 Dashboard | KPIs e gráficos: visualização financeira do consultório → aula_26 | Média | S06.01 | Médio | ✅ Concluído | ✅ |
| S07.01 | 12 | Avançado · S07 RAG | O que é RAG: analogia com memória médica → aula_27 | Média | S04 | Médio | ✅ Concluído | ✅ |
| S07.02 | 12 | Avançado · S07 RAG | PubMed → knowledge_base/ → indexador ChromaDB → aula_28 | Média | S07.01 | Complexo | ✅ Concluído | ✅ |
| S07.03 | 12 | Avançado · S07 RAG | Busca semântica em produção → aula_29 | Média | S07.02 | Complexo | ✅ Concluído | ✅ |
| S07.04 | 12 | Avançado · S07 RAG | Integração RAG com app Flet + qualidade da busca → aula_30 | Média | S07.03 | Complexo | ✅ Concluído | ✅ |
| S08.01 | 13 | Avançado · S08 Checklist | Criar e gerenciar checklist (estilo OMS / WHO) → aula_31 (~55min, cirurgião, 19 itens 7/7/5, condensa S08.01+02, ensino sem leitura de código) | Média | S04 | Médio | ✅ Concluído | ✅ |
| S08.02 | 13 | Avançado · S08 Checklist | Uso em procedimento: log com timestamp imutável → aula_31 (condensado, sem export PDF) | Média | S08.01 | Médio | ✅ Concluído | ✅ |
| S09.01 | 14 | Avançado · S09 Testes | TDD + pytest: o guardião que confere as próprias regras → aula_33 (~55min, controle de qualidade lab, clímax sabotagem CHA₂DS₂-VASc, sem leitura de código) | Baixa | S05+S07 | Médio | ✅ Concluído | ✅ |
| S09.02 | 14 | Avançado · S09 Testes | Testar o RAG não-determinístico (sensibilidade/especificidade) → aula_34 (~55min, clímax sabotagem da honestidade, corpus de teste isolado) | Baixa | S09.01 | Médio | ✅ Concluído | ✅ |
