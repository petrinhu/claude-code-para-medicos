# Aula 18 — MCP, Skills, Hooks e Plugins: Estendendo o Bisturi

**Formato:** Gravada no OBS Studio, editada no Kdenlive  
**Duração:** ~38 min  
**Tom:** Colega com humor leve e didático — aprofundar o que já existe e apresentar o único conceito novo: hooks

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] O scaffold da aula 16 presente (4 pastas + `arquitetura.txt` + `main.py`), pois a Seção 5 manda atualizar o `arquitetura.txt` para disparar o hook.
- [ ] O plugin superpowers e as skills `/forgejo`, `/memo_persistente`, `/tab_pendencias` instalados (referência da Seção 1 e leitura da skill na Seção 2).
- [ ] O MCP do GitHub configurado e autenticado, com o repositório do ClinMd-Tribe já criado e contendo pelo menos 5 commits (insumo da Seção 3, `@github liste os últimos 5 commits`). Use um repositório de demonstração só com código do app, sem qualquer dado de paciente.
- [ ] Ambiente Python/uv pronto.

**Confira antes de gravar:**

- [ ] Teste o prompt da skill na Seção 2 (`leia o arquivo da skill tab_pendencias`) antes de gravar e confira que o conteúdo exibido é texto/instrução, sem nenhum dado sensível.
- [ ] Teste o `@github` da Seção 3 antes de gravar: confirme que a autenticação está válida e os 5 commits aparecem; se pedir login, resolva fora da gravação.
- [ ] Confira se já existe `.claude/settings.json` no projeto. A Seção 5 cria/modifica esse arquivo com o hook PostToolUse. Se já houver hooks ali de outro teste, decida antes se vai mostrar a criação do zero (apague) ou a modificação (mantenha).
- [ ] Depois de gravar a demo do hook (Seção 5), lembre que o hook continua ativo na sua máquina: a cada escrita ou edição de arquivo o hook vai anexar uma linha no `registro_residente.txt` nas próximas sessões. Remova o hook do `settings.json` (e apague o `registro_residente.txt`) após a gravação se não quiser esse comportamento permanente.
- [ ] Teste o comando do hook fora da gravação antes: a saída de stdout de um hook PostToolUse não aparece direto na tela do terminal (fica no log de debug), por isso a demo anexa num arquivo e depois mostra o conteúdo com `type registro_residente.txt`. Confirme que o arquivo recebe a linha ao salvar.

**Navegador:** nenhum site é necessário nesta aula. O acesso ao GitHub acontece pelo MCP dentro do Claude Code, não pelo browser.

---

## SEÇÃO 1: REVISÃO RELÂMPAGO — OS TRÊS CONHECIDOS (3 min)

**Tom:** Reconexão, não introdução — o aluno já sabe, só precisa nomear

**[Aviso rápido dos óculos, antes de mergulhar]**

"Antes da gente começar: óculos de perto, por favor. Hoje vai ter um trecho de configuração com chaves, aspas e dois-pontos, aquele JSON cheio de pontuação miúda. Ler isso sem óculos é tipo auscultar com o estetoscópio entupido: dá pra tentar, mas você perde o detalhe que importa."

"Você já usa três dessas extensões há semanas.

Na aula_03 você instalou o MCP do PubMed — o cabo que conecta o Claude
a uma fonte de dados externa. Você pediu artigos sem abrir o navegador.

Na aula_10 você instalou o plugin superpowers e três skills:
/forgejo, /memo_persistente, /tab_pendencias.
Desde então você usa /tab_pendencias toda aula.

Então você já sabe:

MCP — cabo que conecta o Claude a ferramentas externas.
Skill — protocolo que você invoca pelo nome.
Plugin — kit que empacotou skills e MCPs numa instalação só.

---

Hoje tem dois objetivos.

Primeiro: aprofundar esses três no contexto do ClinMd-Tribe.
Não como conceito isolado — como ferramenta que você vai usar no projeto.

Segundo: apresentar o quarto. O único que você ainda não conhece.

[mostrar a tabela vazia na tela]

| Conceito | O que é | Como acionar | Análogo no plantão |
|----------|---------|-------------|-------------------|
| Skill | ? | /nome | ? |
| MCP | ? | @nome | ? |
| Hook | ? | ? | ? |
| Plugin | ? | plugin install | ? |

Vamos preencher essa tabela juntos."

---

## SEÇÃO 2: SKILLS — LENDO O PROTOCOLO POR DENTRO (7 min)

**Tom:** Aprofundamento — desmistificar o que a skill é de verdade

"Você usa /tab_pendencias toda semana.

Mas o que é esse comando por dentro?

Prompt ao Claude Code:

```
Leia o arquivo da skill tab_pendencias e me mostre o conteúdo completo.
```

[aguardar e mostrar o conteúdo do arquivo]

---

Olha o que apareceu.

É basicamente texto: instruções em linguagem comum, descrevendo passo a passo o que o Claude deve fazer. Pode ter um cabeçalho curto no topo e algum exemplo, mas o miolo é instrução escrita, não um programa que você precisa entender.

Uma skill é um protocolo escrito que alguém deixou pronto.
Igual ao POP da UTI — Procedimento Operacional Padrão.
Quando um residente novo entra no serviço, ele lê o POP e segue.
Não é mágica. É instrução formalizada.

O Claude lê esse arquivo no início da sessão e passa a saber
o que fazer quando você digita /tab_pendencias.

---

Isso tem uma implicação importante.

Qualquer protocolo clínico que você usa repetidamente no ClinMd-Tribe
pode virar uma skill.

'Toda vez que eu pedir uma análise de escore clínico,
quero que o Claude siga este roteiro: verificar os critérios,
calcular, classificar o risco, sugerir conduta.'

Isso pode ser escrito num arquivo de skill.
O Claude vai seguir cada vez que você invocar.

Não é escopo desta aula criar uma skill —
mas agora você sabe que não é mágica.
É um arquivo de texto que você pode ler e entender.

[preencher linha 1 da tabela]

| Skill | Protocolo institucional invocado pelo nome | /nome | POP da UTI |"

---

## SEÇÃO 3: MCP — GITHUB NO CLINMD-TRIBE (8 min)

**Tom:** Do conceito ao uso real no projeto — o MCP que já existe trabalhando

"Na aula_10 você viu a lista de MCPs disponíveis.
GitHub estava lá. Mas você nunca usou no projeto.

Hoje usa.

[entrar na pasta do ClinMd-Tribe e abrir o Claude Code]

```
cd Documents\projetos\clinmd-tribe
claude
```

Prompt:

```
@github liste os últimos 5 commits do repositório ClinMd-Tribe
e me diga em qual camada da Clean Architecture cada mudança aconteceu.
```

[aguardar e mostrar o resultado]

---

O Claude acessou o repositório remoto.
Sem você abrir o GitHub no browser.
Sem copiar e colar URL.
Sem navegar pelo histórico manualmente.

E ainda cruzou com o que ele sabe sobre o projeto:
mapeou cada commit na camada da Clean Architecture correspondente.

Isso é o MCP no trabalho real.

---

O residente passou a ter acesso ao prontuário histórico do projeto.

Sabe quando cada andar do hospital foi construído.
Sabe o que mudou na Recepção, o que mudou no Domínio.

Conforme o ClinMd-Tribe crescer — mais commits, mais features —
você vai usar isso para se orientar:

```
@github o que mudou no domain/ nos últimos 10 commits?
```

```
@github existe alguma issue aberta no repositório?
```

O GitHub MCP é o arquivo do hospital.
O residente consulta sem você precisar abrir uma nova aba.

[preencher linha 2 da tabela]

| MCP | Cabo que conecta a ferramentas externas | @nome | PACS, laboratório, arquivo |"

---

## SEÇÃO 4: HOOKS — A ROTINA AUTOMÁTICA (6 min)

**Tom:** Introdução do conceito novo — o único que o aluno ainda não conhece

"Agora o quarto.

Skills e MCPs têm algo em comum: você convoca.
Você digita /tab_pendencias. Você escreve @github.
Você pede. O Claude responde.

Hooks são diferentes.

---

Pensa numa rotina do plantão que dispara sem você pedir.

'Antes de toda alta, confere a prescrição.'

Não é você que lembra. Não é o residente que você precisa instruir na hora.
É uma ordem permanente que já existe no sistema.
Quando o evento acontece — alta confirmada — o checklist roda sozinho.

Hook é isso.

É uma instrução que você configura uma vez e que dispara automaticamente
quando um evento específico acontece no Claude Code.

---

Os eventos que um hook pode monitorar:

PreToolUse — antes de o Claude usar uma ferramenta.
PostToolUse — depois de o Claude usar uma ferramenta.
Notification — quando o Claude envia uma notificação.
Stop — quando o Claude termina de responder.

Você escolhe o evento. Você define o que deve rodar quando ele acontece.

---

Onde fica a configuração?

No arquivo `.claude/settings.json` dentro do projeto.

[mostrar o arquivo na tela — ou mostrar como seria]

```json
{
  \"hooks\": {
    \"PostToolUse\": [
      {
        \"matcher\": \"Write|Edit\",
        \"hooks\": [
          {
            \"type\": \"command\",
            \"command\": \"echo residente salvou um arquivo >> registro_residente.txt\"
          }
        ]
      }
    ]
  }
}
```

Leia junto comigo.

PostToolUse — depois de usar uma ferramenta.
matcher: Write|Edit — quando a ferramenta for de escrita ou edição de arquivo.
command — execute este comando.

Detalhe importante de como o hook se comunica:
a saída de um comando de hook não aparece direto na tela do terminal,
ela fica nos bastidores. Por isso o nosso comando não tenta 'falar' na tela:
ele anexa uma linha num arquivo de registro, o `registro_residente.txt`.
Toda vez que o Claude salvar um arquivo, uma linha nova entra nesse registro.
Sem você pedir. Automático. E depois a gente abre o registro pra ver a prova.

[preencher linha 3 da tabela — mas ainda sem demo]

| Hook | Rotina automática disparada por evento | Automático | Checklist cirúrgico |"

---

## SEÇÃO 5: HOOK AO VIVO — DEMO NO CLINMD-TRIBE (6 min)

**Tom:** Revelar — o aluno vê acontecer sem pedir

"Agora vamos criar esse hook no ClinMd-Tribe.

Prompt ao Claude Code:

```
No arquivo .claude/settings.json do projeto ClinMd-Tribe,
adiciona um hook PostToolUse com matcher para Write e Edit.
A cada disparo, o hook deve anexar a linha 'residente salvou um arquivo'
no arquivo registro_residente.txt na raiz do projeto.
Cria o settings.json se ele não existir.
```

[aguardar o Claude criar ou modificar o settings.json]

---

Agora faça qualquer modificação no projeto.
Vou pedir ao Claude para atualizar o arquitetura.txt:

```
Atualiza o arquitetura.txt para incluir uma linha indicando
que o scaffold foi concluído na aula_16.
```

[aguardar o Claude salvar o arquivo]

Agora a prova. Vou abrir o registro:

```
type registro_residente.txt
```

[mostrar — a linha 'residente salvou um arquivo' apareceu sozinha no registro]

---

Aconteceu sem você pedir.

Você pediu uma atualização de arquivo.
O residente atualizou.
E o hook disparou sozinho, anexando a linha no registro —
prova de que o arquivo foi tocado, sem nenhum comando seu para isso.

É pequeno. Mas o princípio é poderoso.

Conforme o ClinMd-Tribe crescer, você pode usar hooks para:
— avisar quando um arquivo do domain/ for modificado
— rodar uma verificação automática antes de qualquer commit
— registrar em log toda vez que o Claude escrever na infrastructure/

O residente tem reflexos agora.
Você treinou ele para ter checklist automático."

---

## SEÇÃO 6: TABELA COMPLETA — OS QUATRO JUNTOS (4 min)

**Tom:** Consolidação visual — fechar o ciclo dos 4 conceitos

"Tabela completa.

[mostrar a tabela preenchida]

| Conceito | O que é | Como acionar | Análogo no plantão |
|----------|---------|-------------|-------------------|
| Skill | Protocolo institucional escrito | /nome | POP da UTI |
| MCP | Cabo para ferramentas externas | @nome | PACS, arquivo, laboratório |
| Hook | Rotina automática por evento | Automático | Checklist cirúrgico |
| Plugin | Kit com skills + MCPs + hooks | plugin install | Maleta de admissão completa |

---

Três perguntas rápidas. Responda antes de eu falar.

Para buscar um artigo no PubMed direto do Claude Code, que tipo de extensão uso?

[pausa]

MCP. O cabo que conecta o Claude ao PubMed.

---

Para gerar a tabela de pendências do projeto, que tipo?

[pausa]

Skill. Você digita /tab_pendencias e o protocolo roda.

---

Para registrar automaticamente toda vez que o Claude modificar um arquivo
no domain/ do ClinMd-Tribe, que tipo?

[pausa]

Hook. Você configura uma vez e ele dispara sozinho no evento."

---

## SEÇÃO 7: /TAB_PENDENCIAS + ENCERRAMENTO (4 min)

**Tom:** Registro e ponte para BigTech Virtual

"Atualize as pendências:

```
/tab_pendencias
```

[mostrar a tabela — aula_18 concluída, BigTech Virtual como próxima]

---

Resumo do que ficou claro hoje.

Você já sabia três — agora conhece os três mais fundo.

Skill é um arquivo de texto que qualquer residente lê e segue.
MCP conecta o Claude ao GitHub, ao PubMed, ao que você precisar,
sem abrir o browser, no contexto do projeto.
Hook é o checklist automático — dispara no evento, sem você pedir.
Plugin é a maleta que trouxe tudo junto.

---

Dever de casa.

Pensa num evento do ClinMd-Tribe que deveria disparar automaticamente.

Pode ser:
'toda vez que o Claude modificar um arquivo em domain/, quero um aviso'
'antes de qualquer commit, quero que apareça uma mensagem de confirmação'
'quando o Claude terminar de responder, quero um som de notificação'

Escreva o prompt que você daria ao Claude Code para criar esse hook.
Não precisa executar — só o prompt.

Na próxima aula: BigTech Virtual.
Você vai conhecer o time completo de C-levels e agents operacionais
que está disponível dentro do Claude Code —
e vai aprender a consultar o especialista certo para cada decisão do ClinMd-Tribe.

Até lá."

---

**FIM DO ROTEIRO**
