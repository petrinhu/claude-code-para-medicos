# Exercicios: Seguranca de Tokens

## Exercicio 1: Proteger o token do Claude

No projeto ClinMd-Tribe:
1. Crie o arquivo `.env` com sua chave `ANTHROPIC_API_KEY`
2. Confirme que `.env` esta no `.gitignore`
3. Substitua qualquer chave hardcoded no codigo por `os.getenv()`
4. Rode `git log --all -p | grep "sk-ant"` e confirme que retorna vazio

## Exercicio 2: Auditoria de segredos

Rode no terminal:
```bash
git log --all -p | grep -iE "(api_key|token|secret|password|sk-ant)" | head -20
```
Se encontrar algo, o gabarito mostra como remover do historico.

## Gabarito

Se encontrou tokens no historico:
```bash
# Instalar git-filter-repo
pip install git-filter-repo

# Remover o arquivo que tinha o token de todo o historico
git filter-repo --path .env --invert-paths

# Revogar o token IMEDIATAMENTE no painel do provedor
# Gerar um novo token
# Atualizar o .env com o novo token
```

Regra: token vazado = token morto. Sempre revogar e gerar novo.
