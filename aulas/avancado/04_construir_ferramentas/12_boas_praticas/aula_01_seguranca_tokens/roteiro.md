# Roteiro do Professor: Seguranca — Nunca Suba seu Token de API

## Abertura (5 min)

Motivacao: em 2024, um estudo mostrou que mais de 100 mil tokens de API vazaram no GitHub publico em um unico mes. Muitos eram de desenvolvedores iniciantes que nem perceberam. Um token vazado pode gerar uma conta de milhares de dolares em horas.

Analogia clinica: e como deixar o carimbo medico e a senha do sistema de prescricao colados na porta do consultorio. Qualquer um que passar ve.

## Teoria com Analogia Clinica (15 min)

**O que e um token de API:**
- E sua identidade + autorizacao para usar um servico (Claude, OpenAI, etc.)
- Qualquer um que tiver seu token pode usar o servico na sua conta e no seu limite

**O problema do git:**
- O git guarda o HISTORICO completo de todos os arquivos
- Se voce subiu um token em um commit, mesmo que delete depois, ele continua no historico
- Repositorios publicos sao indexados por robos em minutos

**A solucao: variaveis de ambiente**

```bash
# ERRADO: nunca faca isso
ANTHROPIC_API_KEY = "sk-ant-xxxxxxxxxxxxx"  # direto no codigo
```

```bash
# CERTO: use um arquivo .env local
# arquivo: .env (NUNCA sobe pro git)
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

```python
# CERTO: leia a variavel no codigo
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
```

## Demo ao Vivo (25 min)

### Passo 1: Criar o .env

```bash
# Na raiz do projeto
touch .env
echo "ANTHROPIC_API_KEY=sua-chave-aqui" >> .env
```

### Passo 2: Garantir que .env esta no .gitignore

```bash
# Verificar se ja esta
cat .gitignore | grep .env

# Se nao estiver, adicionar
echo ".env" >> .gitignore
echo "*.env" >> .gitignore
```

### Passo 3: Instalar python-dotenv

```bash
uv add python-dotenv
```

### Passo 4: Ler a variavel no codigo

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY nao encontrada. Verifique o arquivo .env")
```

### Passo 5: Verificar que o token NAO esta no git

```bash
git status          # .env nao deve aparecer
git log --all -p | grep "sk-ant"  # deve retornar vazio
```

### Passo 6: Criar .env.example para documentar (sem valores reais)

```bash
cat > .env.example << 'ENVEOF'
ANTHROPIC_API_KEY=sua-chave-aqui
ENVEOF

git add .env.example
git commit -m "docs: adicionar .env.example com variaveis necessarias"
```

## Exercicio Guiado (10 min)

Aluno faz junto: criar o .env, adicionar ao .gitignore, verificar com git status que nao aparece.

## Fechamento (5 min)

Regra de ouro: se tem "chave", "token", "secret", "password" ou "key" no nome da variavel, ela vai no .env. Nunca no codigo. Nunca no commit.
