# Como publicar esta wiki no Codeberg

Esta página é um **guia prático para o dono do repositório** (Dr. Petrus) colocar estas páginas de wiki no ar, no Codeberg. As páginas estão guardadas dentro do repositório, na pasta `docs/wiki/`, mas isso ainda não as torna a wiki oficial visível no site. Esta é a etapa que falta, e é **manual**: precisa ser feita uma vez pelo dono, com permissão de acesso ao repositório.

> Esta página é mais técnica que as outras, porque a publicação envolve alguns comandos de terminal. Ainda assim, vai tudo explicado passo a passo. Se algum termo soar estranho, o [[Glossario]] está ali do lado.

## A ideia geral (por que existe um passo manual)

No Codeberg (e em plataformas parecidas, como Forgejo e GitHub), a wiki de um projeto é, por baixo dos panos, **um segundo repositório git, separado do principal** (repositório e git estão explicados no [[Glossario]], se precisar). O repositório do código tem um endereço; a wiki tem outro, quase igual, só com `.wiki` no final. Por exemplo:

- Código: `https://codeberg.org/petrinhu/claude-code-para-medicos.git`
- Wiki: `https://codeberg.org/petrinhu/claude-code-para-medicos.wiki.git`

Publicar a wiki, então, é **copiar os arquivos `.md` de `docs/wiki/` para esse repositório de wiki** e enviá-los. Por isso é um passo à parte: o conteúdo já existe no projeto, mas precisa ser levado para o "endereço da wiki".

Há também uma convenção de nomes que o Codeberg entende automaticamente, e que esta wiki já segue:

- `Home.md` vira a **página inicial** da wiki.
- `_Sidebar.md` vira a **barra lateral** de navegação.
- `_Footer.md` vira o **rodapé** que aparece em todas as páginas.
- Os demais arquivos viram páginas comuns, e os links no formato `[[NomeDaPagina]]` ligam uma à outra.

## Passo 1: habilitar a wiki nas configurações do repositório

Antes de enviar qualquer arquivo, a wiki precisa estar **ligada** no projeto. No Codeberg, recursos como wiki, issues e pull requests podem ser ativados ou desativados.

1. Abra o repositório no Codeberg, no navegador: `https://codeberg.org/petrinhu/claude-code-para-medicos`.
2. Entre em **Settings** (Configurações), no menu do repositório.
3. Procure a seção de recursos (em inglês, costuma aparecer como *Units*, *Features* ou *Advanced Settings*).
4. Marque a opção **Wiki** para habilitá-la e salve.

A partir daí, o repositório passa a ter o endereço de wiki (`...wiki.git`) disponível para receber o conteúdo.

> Dica: ao habilitar, o Codeberg pode oferecer criar uma primeira página automaticamente pela interface. Você pode aceitar (isso já inicializa o repositório da wiki) ou seguir direto para os passos abaixo, que também o inicializam.

## Passo 2: baixar (clonar) o repositório da wiki

Agora, no terminal, você vai trazer o repositório da wiki para o seu computador. "Clonar" é o termo do git para **baixar uma cópia completa de um repositório**.

Escolha uma pasta de trabalho qualquer (fora do repositório principal, para não confundir) e rode:

```bash
git clone https://codeberg.org/petrinhu/claude-code-para-medicos.wiki.git
```

Isso cria uma pasta chamada `claude-code-para-medicos.wiki` com o conteúdo atual da wiki (que pode estar vazia ou com uma página de exemplo, se você criou uma no passo anterior).

> Se o Codeberg pedir usuário e senha, use suas credenciais do Codeberg. Em muitos casos, no lugar da senha entra um **token de acesso**: uma espécie de senha descartável e específica, que você gera nas configurações da sua conta no Codeberg (em *Settings*, na parte de *Applications* ou *Access Tokens*). Se você usa um, é ele que vai aqui. Nunca compartilhe esse token nem o coloque em arquivos do projeto.

## Passo 3: copiar os arquivos da wiki

Agora copie os arquivos `.md` que estão em `docs/wiki/` (no repositório principal) para dentro da pasta da wiki que você acabou de clonar.

Supondo que o repositório principal esteja em `~/claude-code-para-medicos` e a wiki clonada esteja na pasta atual, o comando é:

```bash
cp ~/claude-code-para-medicos/docs/wiki/*.md claude-code-para-medicos.wiki/
```

> Ajuste os caminhos para o lugar real onde cada pasta está no seu computador. O `cp` é o comando de copiar; `*.md` quer dizer "todos os arquivos que terminam em `.md`".

São sete arquivos no total, que devem ficar assim dentro da pasta da wiki:

```
claude-code-para-medicos.wiki/
├── Home.md
├── _Sidebar.md
├── _Footer.md
├── Glossario.md
├── Como-O-Repositorio-Esta-Organizado.md
├── O-Curso.md
├── O-App-ClinMd-Tribe.md
└── Como-Publicar-Esta-Wiki.md
```

## Passo 4: registrar e enviar (commit e push)

Com os arquivos no lugar, entre na pasta da wiki e registre as mudanças no git, depois envie para o Codeberg. São três comandos em sequência. O primeiro, `git add .`, marca os arquivos novos para serem salvos (o `.` ali no final quer dizer "tudo o que mudou nesta pasta"). Os outros dois, `git commit` e `git push`, estão explicados no lembrete abaixo.

> Lembrete do [[Glossario]]: um **commit** é uma "foto" salva das mudanças, com uma mensagem; o **push** é o ato de enviar essas mudanças para o servidor (o Codeberg). No comando abaixo, `origin` é o apelido que o git dá ao endereço de onde você baixou a wiki (o Codeberg), e `master` é o nome da linha principal de trabalho.

```bash
cd claude-code-para-medicos.wiki
git add .
git commit -m "Publica wiki do curso: home, glossario, organizacao, curso, app e guia de publicacao"
git push origin master
```

Uma observação sobre o nome da linha principal (no [[Glossario]] ela aparece como **branch**, a "linha de trabalho"): repositórios de wiki no Codeberg às vezes usam `master` e às vezes `main` para esse nome. Se o comando de `push` acima reclamar, descubra qual é o nome certo com o comando abaixo (ele lista as linhas de trabalho existentes e marca a atual):

```bash
git branch
```

Depois, use o nome que aparecer no lugar de `master` no comando de `push`.

## Passo 5: conferir no navegador

Pronto. Abra a aba **Wiki** do repositório no Codeberg:

`https://codeberg.org/petrinhu/claude-code-para-medicos/wiki`

A página inicial (vinda do `Home.md`) deve aparecer, com a barra lateral à esquerda (do `_Sidebar.md`) e o rodapé embaixo (do `_Footer.md`). Clique pelos links e confira se a navegação entre as páginas funciona.

## E quando a wiki precisar ser atualizada?

Sempre que você editar os arquivos em `docs/wiki/` no repositório principal, a wiki publicada **não muda sozinha**. Para atualizar, é só repetir os passos 3 e 4: copiar os `.md` novos para a pasta da wiki clonada, e fazer `git add`, `git commit` e `git push` de novo.

> Dica de organização: trate o `docs/wiki/` no repositório principal como a **fonte de verdade** (onde você edita), e a wiki publicada como a **vitrine** (para onde você copia). Assim o conteúdo fica versionado junto com o projeto e nunca se perde.

## Sobre o espelho no GitHub

Este projeto também tem uma cópia espelhada no GitHub. O GitHub tem o seu próprio recurso de wiki, que funciona com a mesma ideia (um repositório `.wiki.git` separado e os mesmos arquivos `Home.md`, `_Sidebar.md`, `_Footer.md`). Se um dia você quiser publicar a wiki também lá, o procedimento é equivalente, trocando o endereço do Codeberg pelo do GitHub. Por ora, a wiki oficial vive no Codeberg, que é o repositório de origem do projeto.

## Em resumo

1. **Habilite a wiki** nas configurações do repositório no Codeberg.
2. **Clone** o repositório da wiki (`...wiki.git`).
3. **Copie** os sete arquivos `.md` de `docs/wiki/` para dentro dele.
4. **Registre e envie** com `git add`, `git commit` e `git push`.
5. **Confira** na aba Wiki do Codeberg.

Feito isso, qualquer pessoa que abrir o repositório vai encontrar esta wiki acolhedora esperando por ela, começando pela [[Home]].
