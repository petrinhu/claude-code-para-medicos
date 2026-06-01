# Roteiro do Professor: Claude Code no Celular via Acesso Remoto

## Abertura (5 min)

Motivação: você está no plantão, no consultório ou em casa no sofá. O PC está ligado. Você abre o celular e continua seu trabalho no Claude Code como se estivesse sentado na frente do computador. Isso é possível hoje, gratuitamente.

## Teoria com Analogia Clínica (15 min)

**Analogia:** é como o acesso remoto ao HIS (sistema hospitalar) pelo celular. Você não carrega o servidor no bolso; você carrega apenas a tela. O processamento acontece no seu PC, mas você comanda de qualquer lugar.

**Como funciona o `/remote`:**
- O comando `/remote` no Claude Code gera uma URL temporária segura
- Essa URL abre uma sessão do seu Claude Code no navegador do celular
- O PC precisa estar ligado e com Claude Code rodando
- A sessão expira quando você fecha ou digita `/remote stop`

**Casos de uso médico:**
- Revisar um roteiro de aula enquanto espera o paciente
- Pedir um resumo de artigo no intervalo do plantão
- Continuar um exercício do curso no trajeto de carro (passageiro, claro!)

## Demo ao Vivo (25 min)

### Passo 1: No PC, iniciar o modo remoto

```bash
/remote
```

Claude Code vai exibir uma URL parecida com:
```
Remote session available at:
https://claude.ai/code/remote/xxxx-xxxx-xxxx
```

### Passo 2: No celular, abrir a URL

- Copie a URL ou escaneie o QR code (se disponível)
- Abra no navegador do celular (Chrome, Safari, Firefox)
- Faça login com sua conta Anthropic se pedido

### Passo 3: Usar normalmente pelo celular

A interface é a mesma do PC. Você pode:
- Digitar prompts
- Anexar arquivos (via compartilhar do celular)
- Ver respostas em tempo real

### Passo 4: Encerrar a sessão remota

```bash
/remote stop
```

Ou simplesmente feche a aba no celular. A sessão no PC continua ativa.

## Exercício Guiado (10 min)

Aluno faz junto:
1. Abre o `/remote` no PC
2. Acessa pelo celular
3. Envia um prompt simples: "Resuma em 3 linhas o que aprendi até aqui no curso"
4. Recebe a resposta no celular

## Fechamento (5 min)

Com o `/remote` você tem o Claude Code no bolso. Nas próximas aulas vamos usar isso para fazer exercícios em qualquer lugar. Na fase intermediária, vamos combinar o acesso remoto com tarefas agendadas: o PC trabalha de madrugada, você confere de manhã pelo celular.
