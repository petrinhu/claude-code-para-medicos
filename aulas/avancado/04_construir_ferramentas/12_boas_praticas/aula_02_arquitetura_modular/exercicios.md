# Exercicios: Arquitetura Modular

## Exercicio 1: Auditoria de tamanho

```bash
# Listar arquivos Python por numero de linhas
find clinmd_tribe/src -name "*.py" | xargs wc -l | sort -rn | head -10
```

Qualquer arquivo acima de 150 linhas e candidato a divisao.

## Exercicio 2: Divisao com agente

Pegue o maior arquivo encontrado no exercicio 1 e peca ao agente:
```
software-architect, este arquivo tem X linhas e faz as seguintes coisas:
[descreva o que ele faz].
Proponha como dividir em modulos menores seguindo Clean Architecture.
```

## Gabarito

Nao ha resposta unica. O criterio de aprovacao e: cada modulo resultante
pode ser descrito em menos de 10 palavras e tem responsabilidade unica.
