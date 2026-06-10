# 🩺 Claude Code para Médicos, do Zero ao Avançado

![Aulas](https://img.shields.io/badge/aulas-40-5213B9)
![Fases](https://img.shields.io/badge/fases-3-5213B9)
![Avancado](https://img.shields.io/badge/avancado-Python%20%2B%20Flet-3776AB)
![Local](https://img.shields.io/badge/100%25%20local-LGPD-2E8B57)
![MDlife](https://img.shields.io/badge/MDlife-Academy-F47920)
![Conteudo](https://img.shields.io/badge/conteudo-completo-brightgreen)

> Do "nunca toquei num terminal" até construir um aplicativo clínico do zero.
> Curso prático de Claude Code para médicos: sem programação nas fases iniciante e intermediária, Python completo na fase avançada (opcional).

**Plataforma:** MDlife Academy  
**Liderança:** Dr. Petrus Silva Costa · **Gestão:** Dr. Luiz Dieckmann

---

## 📚 Sobre o curso

São **40 aulas** (encontros gravados) em **3 fases**, do zero absoluto ao app clínico próprio, cobrindo **52 tópicos** do currículo. Um eixo costura tudo do começo ao fim: **privacidade e LGPD** (dado de paciente nunca entra no Claude Code, e tudo roda na sua máquina).

| Fase | Precisa programar? | Aulas |
|------|:---:|:---:|
| 🟢 Iniciante | Não | 2 |
| 🟡 Intermediário | Não | 5 |
| 🔵 Avançado (opcional) | Python + Flet | 33 |
| | **Total** | **40** |

> **40 aulas, 52 tópicos:** as **40 aulas** são os encontros gravados que você assiste; elas cobrem os **52 tópicos** do currículo (cada assunto planejado, com códigos como M0.01 ou S07.03 no `TODO.md`). Vários tópicos foram condensados num mesmo encontro mais longo (por exemplo, os 5 tópicos da introdução viram 1 aula). Por isso a numeração das pastas vai até `aula_42`, mas o total de aulas é 40.

## 🧭 Por onde começar

- 🌳 **[Árvore visual de aulas](arvore_aulas.html)** : o mapa completo do curso, fase a fase.
- 📖 **Wiki para iniciante total em computação:** pasta [`docs/wiki/`](docs/wiki/), publicada em [codeberg.org/petrinhu/claude-code-para-medicos/wiki](https://codeberg.org/petrinhu/claude-code-para-medicos/wiki).
- ✅ **[TODO.md](TODO.md)** : sequência das aulas, status e fonte de verdade.

## 📂 Estrutura do repositório

```
aula_01/ ... aula_42/   # roteiros das aulas (cada uma: roteiro.md + roteiro.html)
aula_abertura/          # aula de abertura do curso
aulas/                  # atalhos por fase (iniciante, intermediario, avancado)
clinmd_tribe/           # app-piloto da fase avancada (Python, Flet, Clean Architecture)
docs/                   # specs, planos e a wiki (docs/wiki/)
arvore_aulas.html       # arvore visual de aulas
TODO.md                 # sequencia e status do curso
CLAUDE.md               # instrucoes do projeto
```

## ▶️ Rodar o app-piloto (fase avançada)

O `clinmd_tribe/` é o gabarito do app que o aluno constrói ao longo da fase avançada. Para conferir as calculadoras clínicas com os testes automatizados:

```bash
cd clinmd_tribe
uv run --with pytest --no-project pytest -q
```

Você deve ver `26 passed`: os guardiões das calculadoras (MELD, CHA2DS2-VASc, PHQ-9, GAD-7) passando.

## 📖 Módulos e aulas

### 🟢 Iniciante, sem programação (2 aulas)

| Módulo | Aulas | Tópicos cobertos |
|--------|:---:|------|
| **M0** Primeiros Passos sem Medo | 1 | O que é o Claude Code, instalação, como conversar, bons hábitos de prompt, uso no celular |
| **M1** Assistente de Produtividade | 1 | Arquivos e PDFs, gerar documentos, slides, planilhas |

### 🟡 Intermediário, sem programação (5 aulas)

| Módulo | Aulas | Tópicos cobertos |
|--------|:---:|------|
| **M2** Aprender e Acompanhar a Literatura | 2 | PubMed, fichamento (PICO, nível de evidência), flashcards (Anki), briefing matinal |
| **M3** Conteúdo, Pesquisa e Consultório | 3 | Posts e carrosséis, newsletter com SEO, pôster de congresso, estatística, gestão do consultório |

### 🔵 Avançado, opcional (Python + Flet + ClinMd-Tribe) (33 aulas)

| # | Submódulo | Aulas |
|---|-----------|:---:|
| **S00** | Git | 2 |
| **S01** | Fundação (terminal, uv, Python) | 2 |
| **S02** | Python + Flet | 2 |
| **S03** | Clean Architecture | 2 |
| **S04** | Agents e BigTech Virtual | 4 |
| **S05** | Calculadoras Médicas | 4 |
| **S06** | Dashboard Financeiro | 2 |
| **S07** | RAG (a memória do app) | 4 |
| **S08** | Checklist de Procedimentos (estilo OMS) | 1 |
| **S09** | Testes | 2 |
| **S10** | CI/CD (GitHub Actions) | 2 |
| **S11** | Polimento Final | 3 |
| **S12** | Boas Práticas | 3 |

O capstone da fase avançada é o **ClinMd-Tribe**: um app clínico 100% local (calculadoras, anotador, dashboard financeiro, busca em artigos via RAG, checklist), construído aula a aula em Clean Architecture.

## 🛡️ Privacidade e LGPD

Eixo transversal de todas as 40 aulas: **dado de paciente nunca entra no Claude Code, e o app roda 100% na máquina do médico.** Nada sobe para a nuvem.

---

<sub>MDlife Academy · Claude Code para Médicos, do Zero ao Avançado · Liderado por Dr. Petrus Silva Costa e gerenciado por Dr. Luiz Dieckmann</sub>
