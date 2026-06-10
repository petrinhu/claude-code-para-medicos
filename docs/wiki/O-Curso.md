# O curso: como ele foi pensado

Esta página explica a **lógica pedagógica** do curso: as fases, as 40 aulas, a filosofia de ensino e o cuidado constante com a privacidade. Se a página [[Como-O-Repositorio-Esta-Organizado]] mostrou *onde* estão as coisas, esta aqui mostra *por que* o curso é do jeito que é.

## O que o curso ensina, de novo e em uma frase

**"Claude Code para Médicos, do Zero ao Avançado"** ensina médicos a usar o Claude Code (a ferramenta de inteligência artificial da Anthropic, usada pelo terminal) para tarefas reais da vida clínica e acadêmica, partindo do absoluto zero em tecnologia.

> Se "terminal", "Claude Code" ou "inteligência artificial" ainda soam vagos, dê um pulo no [[Glossario]] e volte. Para acompanhar esta página, basta ter lido a [[Home]].

## A filosofia: ensinar como se ensina um protocolo clínico

O aluno-alvo do curso é um **médico experiente em medicina e iniciante total em tecnologia**: alguém que sabe o que é uma veia, mas talvez nunca tenha aberto um terminal. A escolha pedagógica central é tratar cada conceito técnico como se fosse um **novo protocolo clínico**: explicado do básico, passo a passo, sem pular etapas e sem jargão solto.

Por isso, cada conceito de computação ganha uma **analogia clínica**. Alguns exemplos que aparecem ao longo do curso:

- O **git** (que registra cada mudança no projeto) é apresentado como o **prontuário do código**.
- A **Clean Architecture** (a forma de organizar o programa em camadas) é o **plantão hospitalar**: recepção, triagem, médico, laboratório, cada um no seu papel.
- O **RAG** (a técnica que faz a IA responder com base nos seus documentos) é o **residente que leu todos os seus guidelines** e que diz "não sei" quando a resposta não está nos artigos.

A ideia é simples e poderosa: você já domina o raciocínio clínico; o curso usa esse raciocínio como ponte para o território novo.

## As três fases

O curso é dividido em três fases, que sobem em dificuldade de forma gradual. As duas primeiras **não têm nenhuma linha de programação**: é Claude Code puro, conversando em português. A terceira é opcional e mais técnica.

### Fase iniciante (sem programação)
O objetivo é **perder o medo e ganhar autonomia** no uso da ferramenta. Cobre os primeiros passos (o que é o Claude Code, como instalar, como conversar com ele, bons hábitos de pedido) e o uso como assistente de produtividade (trabalhar com PDFs, gerar documentos, montar slides e organizar planilhas). Tudo isso sem escrever código, apenas pedindo.

### Fase intermediária (sem programação)
Aqui o médico aprende a usar o Claude Code para **literatura e produção acadêmica e de consultório**: buscar e triar artigos científicos, fazer fichamento e leitura crítica, gerar flashcards de estudo, produzir conteúdo para redes sociais e pôsteres de congresso, e organizar indicadores do consultório. Continua sem programação: é a IA fazendo o trabalho pesado a partir dos seus pedidos.

### Fase avançada (opcional, com programação)
Esta é a fase do "do zero ao avançado" de verdade. O médico acompanha a **construção de um aplicativo clínico completo**, o ClinMd-Tribe, do começo ao fim. Passa por fundamentos (terminal, instalação de ferramentas, noções de Python), git, criação de telas com Flet, a Clean Architecture, o time de agentes (a "BigTech Virtual"), as calculadoras clínicas, um sistema de busca em documentos (RAG), testes automatizados, automação de qualidade (CI/CD) e o polimento final até virar um programa de Windows pronto para usar.

**Detalhe que tranquiliza:** mesmo na fase avançada, o aluno **não precisa ler nem escrever código à mão**. Esse é um princípio do curso, explicado a seguir.

## A regra de ouro do ensino: zero código para o aluno ler

Talvez a decisão pedagógica mais importante do curso seja esta: **o aluno aprende pelo comportamento observável, não lendo código.**

Na prática, isso quer dizer que, mesmo na fase avançada, o material nunca pede para o médico encarar uma tela cheia de código e tentar decifrá-la. Em vez disso, ele observa **o que o programa faz**: o laudo que aparece na tela, o teste que fica verde, o aplicativo rodando. O Claude Code escreve o código; o aluno conduz, pede, verifica o resultado e aprende com o que vê acontecer.

Por que essa escolha? Porque ler código é uma habilidade própria, que leva tempo e atrapalharia o objetivo real do curso: tornar o médico **capaz de dirigir a ferramenta com confiança**. É a diferença entre saber pilotar bem um equipamento de imagem e saber projetar o equipamento por dentro. Para a prática clínica, pilotar bem é o que importa.

É também por isso que o aplicativo de exemplo (o ClinMd-Tribe) existe como **gabarito do instrutor**: o código completo está lá, funcionando, para referência e para gerar os comportamentos que o aluno observa, mas não é material de leitura obrigatória. A página [[O-App-ClinMd-Tribe]] explica esse aplicativo com calma.

## O eixo que atravessa tudo: privacidade e LGPD

Da primeira à última aula, um cuidado nunca sai de cena: a **proteção dos dados dos pacientes**, conforme a LGPD (a Lei Geral de Proteção de Dados brasileira). Duas regras de ouro guiam o curso inteiro:

1. **Dado de paciente nunca entra no Claude Code.** Todos os exemplos usam dados fictícios ou anonimizados. Informação real e identificável de paciente fica de fora, sempre.
2. **O aplicativo construído roda 100% local**, ou seja, inteiramente dentro do computador do médico, sem enviar nada para a internet. O que é do paciente fica com o médico.

Esse eixo não é um aviso isolado no começo; ele é reforçado aula após aula, porque é parte da responsabilidade de quem cuida de gente.

## As 40 aulas e a fonte oficial

O curso tem **40 aulas**, distribuídas pelas três fases e por módulos temáticos. A contagem, a ordem, o status de cada aula (concluída, pendente) e a que módulo pertencem estão na **lista oficial do projeto**: o arquivo [TODO.md](../../TODO.md) na raiz do repositório. Quando houver qualquer dúvida sobre a estrutura, é esse o documento que vale.

> Por que a numeração das pastas vai só até `aula_42`? Porque várias aulas foram **condensadas** em encontros únicos mais longos (de 45 a 60 minutos). Nada se perdeu; é só uma forma de agrupar. O [TODO.md](../../TODO.md) mostra exatamente como as aulas se distribuem.

## Decisões de currículo: onde mora o detalhe

Ao longo da construção do curso, algumas decisões importantes foram tomadas (por exemplo, uma aula absorver um tema que não tinha lugar próprio). Essas decisões ficam registradas em um documento oficial, para que exista **uma só verdade num só lugar** e ninguém precise adivinhar o porquê das escolhas.

Esse registro é o arquivo [docs/decisoes_curriculo.md](../../docs/decisoes_curriculo.md). Em vez de copiar o conteúdo dele para cá (o que correria o risco de ficar desatualizado), esta wiki simplesmente **aponta para a fonte**. Para o detalhe das decisões curriculares, consulte aquele arquivo.

## Em resumo

- O curso ensina médicos iniciantes em tecnologia a usar o Claude Code, **do zero ao avançado**, com **analogias clínicas** em cada conceito.
- São **três fases**: iniciante e intermediária (sem programação) e avançada (opcional, constrói o aplicativo ClinMd-Tribe).
- A **regra de ouro** é aprender pelo comportamento observável: o aluno nunca precisa ler código.
- A **LGPD** atravessa tudo: dado de paciente fora do Claude Code, aplicativo rodando 100% local.
- A estrutura oficial das **40 aulas** está no [TODO.md](../../TODO.md); as decisões de currículo, em [docs/decisoes_curriculo.md](../../docs/decisoes_curriculo.md).

Próxima parada sugerida: **[[O-App-ClinMd-Tribe]]**, para conhecer o aplicativo de exemplo por dentro (com analogias) e rodar os testes você mesmo.
