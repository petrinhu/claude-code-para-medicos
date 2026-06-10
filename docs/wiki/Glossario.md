# Glossário: as palavras técnicas, explicadas de verdade

Esta é a sua "tabela de equivalências". Toda palavra de computação que aparece no curso ou nesta wiki está aqui, explicada em duas a quatro frases, com uma analogia (sempre que possível, clínica). Você não precisa decorar nada: use como consulta, do mesmo jeito que consulta uma bula ou um escore que não usa todo dia.

Os termos estão agrupados por assunto para facilitar. Dentro de cada grupo, vão do mais básico ao mais específico.

---

## O básico do computador

### Terminal (ou linha de comando)
O terminal é uma janela onde você **escreve ordens para o computador em texto**, em vez de clicar em botões. Você digita um comando, aperta Enter, e o computador executa. Parece antigo, mas é poderoso e preciso: é a diferença entre apontar para o que você quer num cardápio com figuras e simplesmente falar o pedido exato para o garçom. No curso, o terminal é a sala onde você conversa com o Claude Code.

### Linha de comando
É o mesmo que terminal. "Linha de comando" enfatiza que você dá uma ordem por linha de texto. Quando alguém diz "rode isso na linha de comando", quer dizer "digite isso no terminal e aperte Enter".

### CLI
Sigla em inglês para *Command Line Interface*, ou seja, "interface de linha de comando". É o nome técnico de qualquer programa que você usa digitando comandos no terminal, em vez de clicar. O Claude Code é uma CLI: você conversa com ele por texto, no terminal.

### Comando
Uma ordem que você digita no terminal. Por exemplo, `ls` é um comando que lista os arquivos de uma pasta. Cada comando faz uma coisa específica. Pense num comando como uma prescrição de uma linha: instrução exata, resultado exato.

---

## Inteligência artificial e o Claude Code

### Claude Code
A estrela do curso. É uma ferramenta de **inteligência artificial** feita pela empresa Anthropic, que você usa pelo terminal. Você pede coisas em português ("crie um folheto sobre hipertensão", "organize esta planilha"), e ele faz. Não é mágica: é uma ferramenta muito boa que segue instruções. O curso ensina a usá-la do básico ao avançado.

### Inteligência artificial (IA)
Programas de computador capazes de realizar tarefas que normalmente exigiriam raciocínio humano, como escrever um texto, resumir um artigo ou responder perguntas. No curso, a IA que usamos é o Claude. Boa comparação: assim como um exame de imagem não "pensa", mas extrai padrões úteis, a IA processa linguagem e produz respostas úteis, dentro de limites.

### Prompt
É **o pedido que você escreve** para a IA. Se você digita "resuma este artigo em cinco tópicos", esse texto inteiro é o seu prompt. Quanto mais claro e específico o pedido, melhor a resposta, exatamente como uma boa anamnese leva a um melhor diagnóstico. Boa parte do curso é aprender a escrever bons prompts.

### MCP
Sigla em inglês para *Model Context Protocol*, ou "protocolo de contexto do modelo". É uma forma padronizada de **conectar o Claude Code a ferramentas externas**, como uma base de artigos (o PubMed, por exemplo) ou um sistema seu. Pense num MCP como um adaptador universal: permite que o Claude Code "fale" com outros sistemas sem gambiarra. O curso mostra MCP na prática.

### Agente
No contexto do curso, um agente é um **assistente de IA com um papel definido**, que trabalha como parte de um time. Em vez de um único ajudante genérico, você pode ter um agente que pensa como engenheiro, outro como revisor de segurança, outro como gestor. É como montar uma junta médica: cada especialista olha o caso por um ângulo. O curso tem uma "BigTech Virtual", um time inteiro de agentes, com uma aula dedicada a cada papel.

---

## Versionamento e histórico do projeto

### Git
O **git** é um programa que registra cada mudança feita nos arquivos de um projeto, com data, autor e descrição. É o "prontuário do código": toda alteração fica registrada, e você pode voltar a qualquer ponto do passado. Se algo der errado, dá para desfazer com segurança. O curso ensina git como uma ferramenta de organização, não de programação.

### Repositório
Uma pasta de projeto que está sendo acompanhada pelo git. Reúne todos os arquivos mais o histórico completo de mudanças. "Este repositório" é justamente a pasta do curso, com as 40 aulas, o aplicativo de exemplo e os documentos. Em inglês aparece abreviado como *repo*.

### Commit
Um **commit** é uma "foto" salva do projeto num momento específico, com uma mensagem curta dizendo o que mudou (por exemplo: "adiciona aula 15"). É como assinar e datar uma evolução no prontuário: fica registrado que naquele instante o projeto estava daquele jeito, e por quê. O histórico de um projeto é uma sequência de commits.

### Branch
A palavra inglesa para "ramo" ou "galho". Uma **branch** é uma linha de trabalho paralela: você cria uma cópia da situação atual para experimentar mudanças sem mexer na versão principal. Se a experiência der certo, você junta de volta; se der errado, descarta sem estrago. É como testar uma conduta num cenário controlado antes de aplicar no protocolo oficial. A versão principal costuma se chamar `main`.

### Codeberg / GitHub
São **sites onde repositórios git ficam hospedados na internet**, para guardar uma cópia segura e permitir colaboração. Funcionam como uma nuvem especializada em código e projetos. Este projeto mora no **Codeberg** (uma plataforma sem fins lucrativos, sediada na Europa) e tem uma cópia espelhada no **GitHub** (a plataforma mais popular do mundo para isso).

### Wiki
Uma **wiki** é um conjunto de páginas de documentação, escritas em texto simples e ligadas entre si por links, fácil de ler e de atualizar. A Wikipédia é a wiki mais famosa do mundo. Estas páginas que você está lendo agora são a wiki deste projeto. No Codeberg e em plataformas parecidas, a wiki é um recurso embutido do repositório.

---

## Formatos de texto e documentos

### Markdown
O **Markdown** é uma forma simples de escrever texto com formatação usando apenas sinais comuns do teclado. Por exemplo: `# Título` vira um título grande; `**palavra**` deixa a palavra em negrito; um traço no começo da linha vira um item de lista. Os arquivos terminam em `.md`. É como escrever uma receita à mão de forma organizada: legível já no texto puro, e bonita quando exibida. Quase tudo nesta wiki é Markdown.

### HTML
Sigla em inglês para *HyperText Markup Language*, a linguagem que monta as **páginas que você vê no navegador**. Quando um arquivo termina em `.html`, ele foi feito para ser aberto num navegador (Chrome, Firefox, Safari) e mostrar texto, cores, imagens e botões. No curso, vários roteiros de aula têm uma versão `.html` bonita para visualizar.

### Pandoc
O **pandoc** é um programa que **converte documentos de um formato para outro** automaticamente. No curso, ele transforma os roteiros escritos em Markdown (`.md`) em páginas `.html` formatadas, sem ninguém precisar refazer o trabalho à mão. Pense num tradutor juramentado de formatos: o conteúdo é o mesmo, só muda a apresentação.

---

## A parte avançada: programação e o aplicativo

> Aviso importante: os termos abaixo só aparecem na **fase avançada** do curso, que é opcional. Mesmo lá, você nunca precisa ler ou escrever este código à mão. Ele está aqui para você entender as palavras quando elas surgirem.

### Python
Uma **linguagem de programação**, ou seja, um idioma que serve para escrever instruções que o computador executa. O Python é famoso por ser uma das linguagens mais legíveis e amigáveis para quem está começando. É a linguagem usada para construir o aplicativo de exemplo do curso. Você não programa em Python no curso: o Claude Code escreve, e você acompanha o resultado.

### uv
O **uv** é uma ferramenta que **instala e organiza tudo que um projeto Python precisa para funcionar**, de forma rápida e sem dor de cabeça. Pense nele como o farmacêutico do projeto: você pede, e ele separa e organiza todos os "insumos" (as bibliotecas) na dose certa. No curso, comandos começam com `uv run ...` justamente porque o uv prepara o ambiente antes de rodar.

### Flet
O **Flet** é uma ferramenta que permite **criar aplicativos com telas, botões e campos** usando Python. Com ele, o aplicativo do curso roda no navegador e pode até virar um programa de Windows (um arquivo `.exe`). É o que dá "cara" ao aplicativo: a interface que o usuário vê e toca.

### .exe
Um arquivo terminado em `.exe` é um **programa pronto para usar no Windows**: a pessoa dá dois cliques e ele abre, sem precisar instalar nada de programação. É o "remédio de prateleira" do projeto: a fórmula virou um produto pronto. O curso mostra como transformar o aplicativo num `.exe`.

### Clean Architecture
Em português, "arquitetura limpa". É uma **forma de organizar o código em camadas separadas**, cada uma com uma responsabilidade clara, para que o projeto seja fácil de entender e de mudar sem quebrar. A analogia oficial do curso é o **plantão hospitalar**: a recepção atende, a triagem organiza, o médico decide a conduta, o laboratório executa os exames; cada um no seu papel. A página [[O-App-ClinMd-Tribe]] detalha as quatro camadas.

### RAG
Sigla em inglês para *Retrieval-Augmented Generation*, que dá para traduzir como "geração com apoio de busca". É uma técnica que faz a IA **responder com base nos seus próprios documentos**, em vez de só no que ela aprendeu de forma genérica. A analogia do curso é o **residente que leu todos os seus guidelines**: quando você pergunta algo, ele procura nos artigos que você forneceu e responde com base neles; e se a resposta não estiver lá, ele diz honestamente que não sabe, em vez de inventar.

### ChromaDB
Uma ferramenta que **guarda e busca os seus documentos** de um jeito que a IA consegue encontrar o trecho mais relevante para a sua pergunta. É a "estante inteligente" do RAG: você guarda os artigos lá, e quando faz uma pergunta, ela devolve as passagens certas. Funciona inteiramente no seu computador.

### sentence-transformers
Uma ferramenta que **transforma frases em números** de um jeito que frases parecidas ficam com números parecidos. Isso é o que permite à busca encontrar trechos relevantes mesmo quando você não usou exatamente as mesmas palavras do texto. É um detalhe técnico do RAG; você não precisa entender os números, só saber que é isso que faz a busca "entender" o sentido, não só as palavras exatas.

---

## Qualidade e testes

### Teste automatizado
Um **teste automatizado** é um pequeno programa que **confere se outro programa está funcionando certo**, sozinho e na hora. Em vez de você abrir o aplicativo e testar tudo na mão a cada mudança, o computador roda as verificações em segundos. É o controle de qualidade do laboratório: cada amostra passa pelos mesmos critérios, sempre, sem cansaço nem distração.

### pytest
A **ferramenta usada no curso para rodar testes automatizados em Python**. Você digita um comando, e ela executa todas as verificações e diz quais passaram e quais falharam. O nome vem de "Python" + "test". Na página [[O-App-ClinMd-Tribe]] você roda o pytest com as próprias mãos, passo a passo.

### Teste verde
Quando um teste passa (o programa se comportou como esperado), ele aparece como **verde** ou com um "ok". "Está tudo verde" quer dizer que todas as verificações passaram e o programa está se comportando como deveria. Se algo falha, aparece em **vermelho** - é o sinal de que algo quebrou e precisa de atenção. Verde tranquiliza; vermelho chama o plantão.

### TDD
Sigla em inglês para *Test-Driven Development*, "desenvolvimento guiado por testes". É uma forma de trabalhar em que você **escreve primeiro o teste** (a regra que o programa deve cumprir) e só depois faz o programa atender a essa regra. Garante que cada pedaço novo já nasce conferido. É como definir o critério de sucesso de um protocolo antes de aplicá-lo.

### CI/CD
Sigla em inglês para *Continuous Integration / Continuous Delivery*, "integração contínua e entrega contínua". Na prática do curso, é um **robô na internet que roda todos os testes automaticamente a cada mudança** enviada ao repositório, garantindo que nada quebrou antes de seguir adiante. É o porteiro e o controle de qualidade trabalhando 24 horas, sem você precisar pedir.

---

## Privacidade

### LGPD
Sigla para **Lei Geral de Proteção de Dados**, a lei brasileira que regula o uso de dados pessoais, incluindo os dados sensíveis de saúde dos pacientes. No curso, a LGPD é levada a sério o tempo todo, com duas regras de ouro: **dado de paciente nunca entra no Claude Code**, e o aplicativo construído **roda inteiramente no seu computador**, sem enviar nada para a internet. Privacidade não é um detalhe; é um eixo do curso inteiro.

### Local (rodar local / 100% local)
"Rodar local" significa que o programa **funciona inteiramente dentro do seu próprio computador**, sem enviar informação para a internet (sem mandar nada para os computadores de outras empresas, os chamados servidores). Para dados de saúde, isso é essencial: o que é seu fica com você. O aplicativo de exemplo do curso, o ClinMd-Tribe, foi feito para rodar 100% local exatamente por causa disso.

---

Faltou alguma palavra? Volte para a [[Home]] ou consulte as outras páginas; muitos termos também são reexplicados no contexto onde aparecem.
