# Roteiro do Professor: Arquitetura Modular — Evitando o Monolito

## Abertura (5 min)

Analogia clinica: imagine um prontuario medico onde tudo fica num unico documento de 500 paginas misturando anamnese, exames, evolucoes, receitas e laudos. Impossivel de usar. Codigo monolitico e a mesma coisa.

## Teoria com Analogia Clinica (15 min)

**O que e um monolito:**
- Um arquivo Python com 800 linhas que faz calculo, interface, banco de dados e integracao com API ao mesmo tempo
- Sintoma: voce tem medo de mexer em qualquer parte porque pode quebrar outra

**Regra de ouro: responsabilidade unica**
- Cada arquivo tem UMA responsabilidade
- Cada funcao faz UMA coisa
- Se voce nao consegue descrever o arquivo em menos de 10 palavras, esta grande demais

**Mapeamento com Clean Architecture:**
```
presentation/   -> so interface (Flet)
application/    -> so logica de negocio e casos de uso
domain/         -> so regras puras (calculadoras, modelos)
infrastructure/ -> so I/O (arquivos, banco, API externa)
```

## Demo ao Vivo (25 min)

Pegar um arquivo monolitico de exemplo e dividir ao vivo em modulos usando o Claude Code com o agente `software-architect` para orientar a divisao.

```
/bigtech
> Caetano, temos um arquivo de 400 linhas misturando UI e calculo.
> Proponha como dividir seguindo Clean Architecture.
```

## Exercicio Guiado (10 min)

Aluno identifica o maior arquivo do seu projeto e propoe uma divisao com ajuda do agente.

## Fechamento (5 min)

Se um arquivo passou de 200 linhas, pare e pergunte ao agente: "Este arquivo esta fazendo mais de uma coisa?"
