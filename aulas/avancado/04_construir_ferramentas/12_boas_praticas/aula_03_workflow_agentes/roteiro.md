# Roteiro do Professor: Workflow com Agentes — Sempre Discuta com o Time

## Abertura (5 min)

Motivacao: o maior erro de desenvolvedores iniciantes nao e escrever codigo ruim. E tomar decisoes de arquitetura sozinhos, sem discutir. Com a BigTech Virtual voce tem um time completo disponivel 24h. Use.

Analogia clinica: antes de indicar uma cirurgia complexa, voce chama a equipe para uma reuniao de caso. Nao decide sozinho. Com o Claude Code e a mesma coisa.

## Teoria com Analogia Clinica (15 min)

**Quando chamar o time:**
- Antes de comecar uma feature nova: chame Cosimo (Chief of Staff) para classificar o porte
- Antes de escolher stack: chame Caetano (CTO) para discutir trade-offs
- Antes de definir escopo: chame Capitolino (CPO) para validar a necessidade
- Antes de qualquer commit grande: use /tab_pendencias para ordenar o backlog

**O fluxo correto:**
```
1. /bigtech -> Cosimo classifica o projeto e monta o time
2. Discutir com CTO/CPO antes de codificar
3. /tab_pendencias -> ver o que fazer primeiro (WSJF)
4. Codificar com agentes operacionais (backend, frontend, qa)
5. Revisao com code-reviewer antes de merge
```

## Demo ao Vivo (25 min)

### Exemplo: adicionar uma nova calculadora ao ClinMd-Tribe

**Errado (sem discutir):**
```
# Abre o arquivo e sai codificando direto
```

**Certo (com o time):**
```bash
# Passo 1: chamar o time
/bigtech
> Quero adicionar a calculadora APACHE II ao ClinMd-Tribe.
> Cosimo, classifique o porte e diga quem precisa participar.

# Passo 2: discutir com Caetano (CTO)
> Caetano, onde encaixa no Clean Architecture?
> Domain ou Application?

# Passo 3: atualizar pendencias
/tab_pendencias
> Adicionar "Implementar APACHE II" na fila.
> Qual a prioridade comparado com as outras pendencias?

# Passo 4: codificar com o agente certo
> backend-engineer, implemente a calculadora APACHE II
> no domain/calculadoras/ seguindo o padrao existente.
```

## Exercicio Guiado (10 min)

Aluno escolhe uma feature do seu projeto e faz todo o fluxo: /bigtech, discussao com CTO, /tab_pendencias, antes de escrever uma linha de codigo.

## Fechamento (5 min)

Regra de ouro: nenhuma decisao de arquitetura sem passar pelo Cosimo (Chief of Staff) primeiro. O /tab_pendencias antes de codificar. O code-reviewer antes do merge. Esse fluxo e o que separa um projeto que escala de um que vira monolito.
