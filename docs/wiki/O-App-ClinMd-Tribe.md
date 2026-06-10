# O aplicativo de exemplo: ClinMd-Tribe

Esta página apresenta o **ClinMd-Tribe**, o aplicativo clínico que o curso constrói na fase avançada. Você vai entender o que ele é, por que ele existe, como está organizado por dentro (com analogias simples) e, ao final, vai ter um **passo a passo para rodar os testes você mesmo**, mesmo sem nunca ter programado.

> Termos como Python, Flet, Clean Architecture e teste automatizado aparecem aqui. Todos estão explicados no [[Glossario]], caso queira consultar enquanto lê.

## O que é o ClinMd-Tribe

O ClinMd-Tribe é um **aplicativo clínico pessoal que roda 100% no seu computador**. Ele tem telas com botões e campos, calcula escores clínicos conhecidos e pode até virar um programa de Windows (um arquivo `.exe`). Tem o seu próprio cartão de visitas em [clinmd_tribe/README.md](../../clinmd_tribe/README.md).

O nome junta "ClinMd" (de clínica/medicina) com "Tribe", em referência à TribeMD, a parceira do curso. A identidade visual segue o padrão TribeMD, com o roxo `#5213B9` como cor principal.

E, fiel ao eixo do curso, ele foi desenhado para ser **100% local**: nenhum dado sai para a internet. O que é do paciente fica no computador do médico.

## Por que ele existe (e por que você não precisa ler o código dele)

O ClinMd-Tribe é o **gabarito do instrutor**. Ele é o aplicativo completo, pronto e funcionando, que serve de referência para a fase avançada do curso.

Aqui entra uma das ideias mais importantes do curso (explicada em detalhe na página [[O-Curso]]): **o aluno aprende pelo comportamento observável, não lendo código.** Ou seja, o código do ClinMd-Tribe está todo aqui, mas ele não é material de leitura obrigatória. O médico observa **o que o aplicativo faz** (o laudo na tela, o teste que fica verde, o programa rodando) em vez de decifrar linha por linha.

Pense neste aplicativo como o **caso-modelo de um protocolo**: ele existe pronto para você ver o resultado correto e comparar, não para você reconstruí-lo de cabeça. O Claude Code é quem escreve o código durante as aulas; o aplicativo aqui é a versão de referência.

## Como ele está organizado por dentro: o plantão hospitalar

Por baixo das telas, o ClinMd-Tribe segue a **Clean Architecture** (arquitetura limpa), que separa o programa em **quatro camadas**, cada uma com uma responsabilidade clara. A analogia oficial do curso é o **plantão hospitalar**, e ela funciona muito bem.

Imagine um paciente chegando ao hospital para ser atendido. Ele percorre um fluxo, e cada profissional tem o seu papel:

| Camada (nome técnico) | No plantão | O que faz |
|---|---|---|
| **Apresentação** | Recepção / balcão | Recebe a pessoa, mostra a tela, coleta o que foi digitado. Não decide nada clínico. |
| **Aplicação** | Enfermagem de triagem | Organiza o fluxo: pega o pedido, aciona quem precisa, coloca na ordem certa. Não é dona da regra clínica. |
| **Domínio** | O médico / o protocolo | A regra de decisão pura: o escore, o critério clínico. Não sabe se existe tela ou banco de dados. |
| **Infraestrutura** | Laboratório / arquivo / farmácia | Guarda no disco, busca documentos, lê PDFs. Executa pedidos, não pensa. |

A regra de ouro dessa organização: **o protocolo clínico (o Domínio) existe de forma independente**. Você pode trocar a recepção (a aparência das telas) sem mexer no protocolo. Pode trocar o laboratório (a forma de guardar dados) sem mudar o diagnóstico. O cálculo do escore continua o mesmo, isolado e protegido.

Por que isso é bom? Porque facilita mudanças sem quebrar o que funciona. Se amanhã sair uma diretriz nova que muda um critério clínico, você mexe **só no Domínio**, sem precisar navegar por código de telas ou de armazenamento. É a diferença entre um prontuário organizado em seções e um prontuário onde anamnese, prescrição e a conta do hospital estão todas no mesmo parágrafo embolado.

No repositório, essas camadas aparecem como pastas dentro de `clinmd_tribe/src/`:

```
clinmd_tribe/src/
├── presentation/    <- Apresentação (a recepção: telas Flet)
├── application/     <- Aplicação (a triagem: organiza o fluxo)
├── domain/          <- Domínio (o protocolo: as calculadoras clínicas)
└── infrastructure/  <- Infraestrutura (o laboratório: guarda e busca dados)
```

## As calculadoras clínicas (o coração do Domínio)

A camada de Domínio guarda as **regras clínicas puras**, uma por arquivo, como fonte única de verdade. São escores que você provavelmente já conhece da prática:

- **CHA2DS2-VASc** - estima o risco de eventos tromboembólicos (como AVC) em pacientes com fibrilação atrial.
- **HAS-BLED** - estima o risco de sangramento em quem usa anticoagulação (apresentado no curso ao lado do CHA2DS2-VASc, formando o painel de decisão da fibrilação atrial).
- **PHQ-9** - questionário de rastreio de depressão.
- **GAD-7** - questionário de rastreio de ansiedade.
- **MELD** - escore de gravidade de doença hepática (com o piso de creatinina configurável).

Cada calculadora vive isolada no seu próprio arquivo. Isso quer dizer que mexer numa não afeta as outras: ajustar o PHQ-9 não toca no MELD. É o mesmo princípio de manter cada protocolo em sua própria seção, bem separado.

## Rodar os testes você mesmo (passo a passo)

Esta é a parte prática. O ClinMd-Tribe vem com **testes automatizados**, e você pode executá-los, mesmo sem saber programar. É uma boa forma de ver, com os próprios olhos, a ideia de "teste verde".

> O que é isto, de novo? Um **teste automatizado** é um pequeno programa que confere se o aplicativo está se comportando certo, sozinho e em segundos. É o controle de qualidade do laboratório: cada regra clínica é conferida contra os critérios esperados. Quando tudo passa, o resultado aparece **verde**. Se algo quebra, aparece **vermelho**.

O que os testes fazem aqui, na prática: eles pegam cada calculadora clínica, alimentam com casos de exemplo e conferem se o resultado bate com o esperado. Se alguém mudar uma fórmula por engano, um teste fica vermelho e avisa na hora.

### O que você precisa antes de começar

1. **Um terminal aberto.** É a janela onde você digita comandos (veja [[Glossario]] se precisar). No Windows costuma se chamar "Prompt de Comando" ou "PowerShell"; no Mac e no Linux, "Terminal".
2. **A ferramenta `uv` instalada.** O `uv` é o "farmacêutico" do projeto: prepara tudo que o Python precisa para rodar. A instalação do `uv` é ensinada na fase avançada do curso; se você está só explorando, esse é o único pré-requisito.
3. **Estar dentro da pasta do aplicativo.** Para isso, você precisa primeiro ter o repositório baixado no seu computador (como baixar uma cópia é ensinado na fase avançada do curso, e o mesmo gesto aparece na página [[Como-Publicar-Esta-Wiki]]). Com o repositório baixado, no terminal você "entra" na pasta `clinmd_tribe` usando o comando `cd`, de *change directory* (mudar de diretório, ou seja, mudar de pasta). Você digitaria algo como:

```bash
cd caminho/ate/claude-code-para-medicos/clinmd_tribe
```

Esse `caminho/ate/` é só um exemplo: troque pelo lugar real onde o repositório ficou no seu computador (o "caminho" é o endereço da pasta, como `C:\Users\seu-nome\...` no Windows ou `/home/seu-nome/...` no Mac e Linux).

### O comando para rodar os testes

Com o terminal aberto dentro da pasta `clinmd_tribe`, digite exatamente isto e aperte Enter:

```bash
uv run --with pytest --no-project pytest -q
```

Vamos traduzir o que cada pedaço quer dizer, sem mistério:

- `uv run` - peça ao `uv` para preparar tudo que é preciso e então rodar algo.
- `--with pytest` - inclua a ferramenta de testes chamada **pytest** nessa preparação.
- `--no-project` - rode de forma enxuta, sem instalar o aplicativo inteiro (mais rápido e suficiente para testar as calculadoras).
- `pytest -q` - execute os testes; o `-q` é de *quiet* (silencioso), para um resultado mais limpo na tela.

### O que você deve ver

Depois de alguns segundos, o terminal mostra um resumo. Se tudo estiver certo, aparece algo parecido com:

```
26 passed
```

Isso significa que **as 26 verificações passaram**: todas as calculadoras clínicas estão se comportando como deveriam. Esse é o famoso "tudo verde". Pode comemorar: você acabou de executar um controle de qualidade automatizado.

Se em vez disso aparecer alguma linha em vermelho com a palavra `failed` (falhou), significa que alguma verificação não passou. Num computador onde nada foi alterado, isso não deve acontecer; se acontecer, geralmente é sinal de que algum pré-requisito (como o `uv`) ainda não está instalado.

### Uma alternativa (com o projeto totalmente instalado)

Se você tiver o projeto totalmente instalado no computador (com todas as ferramentas que ele usa já preparadas, algo que a fase avançada também ensina), há uma segunda forma de rodar os mesmos testes:

```bash
uv run --extra dev pytest
```

Para quem está apenas explorando, o primeiro comando (`uv run --with pytest --no-project pytest -q`) é o caminho mais simples e direto. Ambos estão documentados no [README do aplicativo](../../clinmd_tribe/README.md).

## Em resumo

- O **ClinMd-Tribe** é o aplicativo clínico de exemplo do curso, **100% local**, que serve de **gabarito do instrutor**.
- O aluno **não precisa ler o código dele**; aprende pelo comportamento observável.
- Por dentro, ele usa a **Clean Architecture**, organizada como um **plantão hospitalar**: recepção, triagem, protocolo e laboratório.
- O coração clínico são as **calculadoras** (CHA2DS2-VASc, HAS-BLED, PHQ-9, GAD-7, MELD), cada uma isolada em seu arquivo.
- Você pode **rodar os 26 testes** com um único comando e ver o "tudo verde" com os próprios olhos.

Quer publicar esta wiki para outras pessoas lerem? A próxima página, **[[Como-Publicar-Esta-Wiki]]**, ensina o passo a passo (é uma tarefa do dono do repositório).
