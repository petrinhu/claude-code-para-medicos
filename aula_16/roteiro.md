# Aula 16 — Scaffold do ClinMd-Tribe: A Planta e o Prédio

**Formato:** Gravada em um take no OBS Studio  
**Duração:** ~43 min  
**Tom:** Colega com humor leve e didático — o mapa da aula_15 vira estrutura real de código

---

## SEÇÃO 1: ABERTURA — A PLANTA E O PRÉDIO (3 min)

**Tom:** Contraste visual — o artefato da aula anterior como gancho

"Na aula passada você criou esse arquivo.

[abrir o terminal na pasta do projeto]

```
type arquitetura.txt
```

[mostrar o conteúdo]

```
clinmd-tribe/
  presentation/     # telas Flet: botões, campos, janelas, AppBar
  application/      # orquestração: lê tela, chama domínio, pede pra salvar
  domain/           # regras clínicas: CHA2DS2-VASc, PHQ-9, critérios diagnósticos
  infrastructure/   # arquivos, banco de dados SQLite, indexação de PDFs
```

Quatro alas. Quatro responsabilidades. Tudo no papel.

Agora olha o que existe de verdade no projeto:

```
dir /s /b
```

[mostrar — só main.py, pyproject.toml, uv.lock e uv venv internos]

As pastas não existem.
O arquitetura.txt descreve um hospital que ainda não foi construído.

Hoje a gente constrói.

Com um único prompt ao Claude Code."

---

## SEÇÃO 2: PROMPT DE SCAFFOLD — UM COMANDO, QUATRO ANDARES (12 min)

**Tom:** Explore — o prompt gera, o professor valida junto com o aluno

"Abra o Claude Code:

```
cd Documents\projetos\clinmd-tribe
claude
```

Agora o prompt:

```
No projeto ClinMd-Tribe, cria o scaffold completo da Clean Architecture.

Faça exatamente isto:

1. Cria as pastas: presentation, application, domain, infrastructure

2. Em cada pasta, cria um __init__.py com um comentário de uma linha
   explicando o papel clínico da camada:
   - presentation:   # Recepção — telas e interação com o usuário
   - application:    # Triagem — orquestração do fluxo clínico
   - domain:         # Médico — regras clínicas e protocolos
   - infrastructure: # Laboratório — arquivos, banco e persistência

3. Cria um arquivo placeholder em cada pasta (sem lógica funcional ainda):
   - presentation/tela_inicial.py
   - application/orquestrador.py
   - domain/calculadoras.py
   - infrastructure/armazenamento.py

   Cada placeholder deve ter:
   - Docstring clínica explicando o que vai morar nessa camada
   - Uma função chamada camada() que retorna o nome da camada em português

4. Atualiza o main.py para importar camada() de cada módulo e imprimir
   no terminal, antes de abrir a janela Flet:
   Recepção pronta
   Triagem pronta
   Médico pronto
   Laboratório pronto

5. Garante que uv run python main.py roda sem erro de import.
   Me explica em uma linha o que fez em cada camada.
```

[aguardar o Claude gerar — mostrar os arquivos sendo criados um a um]

---

Agora o teste definitivo:

```
uv run python main.py
```

[mostrar o terminal]

```
Recepção pronta
Triagem pronta
Médico pronto
Laboratório pronto
```

[janela Flet abre — a calculadora de IMC da aula_13 ainda funciona]

Quatro linhas. Janela abrindo. Sem linha vermelha de erro.

Se apareceu assim: o scaffold está de pé.

---

Uma observação sobre erro.

Se aparecer um traceback vermelho — não entre em pânico.
Copie o erro e cole direto no Claude Code:

```
Apareceu esse erro ao rodar uv run python main.py: [cole o erro aqui].
Por favor, corrija.
```

O Claude identifica e corrige. Erro vermelho é informação, não catástrofe."

---

## SEÇÃO 3: TOUR PELO CÓDIGO GERADO (10 min)

**Tom:** Explain — professor narra cada arquivo, aluno reconhece a ala

"Vamos abrir cada arquivo e entender o que o Claude criou.

Começamos pelo mais importante.

---

**O Médico — domain/calculadoras.py**

```
type domain\calculadoras.py
```

[mostrar — docstring + def camada()]

O Claude escreveu uma docstring assim:

'Camada de Domínio do ClinMd-Tribe.
Aqui ficam os protocolos clínicos: CHA2DS2-VASc, PHQ-9, GAD-7
e qualquer critério diagnóstico.
Esta camada não sabe se há interface gráfica.
Não sabe se há banco de dados.
Só sabe medicina.'

Você, médico, é o dono desta pasta.
Quando a diretriz mudar, você vem aqui.
Quando quiser adicionar um escore novo, você vem aqui.
Tela, banco, arquivo — não é problema desta camada.

---

**O Laboratório — infrastructure/armazenamento.py**

```
type infrastructure\armazenamento.py
```

[mostrar]

A docstring vai falar em arquivos, SQLite, salvar resultados.
O que não vai mencionar? Calcular IMC. Diagnosticar fibrilação atrial.
Laboratório executa pedidos. Não pensa.

---

**A Recepção — presentation/tela_inicial.py**

```
type presentation\tela_inicial.py
```

[mostrar]

Botões, campos, janelas. Tudo que o usuário vê e toca.
A Recepção não calcula nada. Só recebe e exibe.

---

**A Triagem — application/orquestrador.py**

```
type application\orquestrador.py
```

[mostrar]

Orquestração. Pega o dado da Recepção, aciona o Médico, pede ao Laboratório.
A Triagem não decide a conduta — ela coordena quem decide.

---

**A credencial do andar — __init__.py**

```
type domain\__init__.py
```

[mostrar — uma linha de comentário]

Esse arquivo pequeno tem um papel crítico.

Em Python, uma pasta com `__init__.py` é reconhecida como módulo —
como um departamento hospitalar com identidade própria.
Sem ele, o `main.py` não consegue importar a camada.

É como um andar sem placa no painel do elevador.
O andar existe. Mas quando você aperta o botão,
o sistema não sabe que esse andar existe.

O `__init__.py` é a placa. É a credencial.

---

**O corredor central — main.py**

```
type main.py
```

[mostrar — imports das 4 camadas + prints + ft.app(main)]

Veja o topo do arquivo.
O Claude importou `camada` de cada pasta e chamou as 4 funções.
Resultado: as 4 linhas no terminal antes da janela.

O `main.py` é o único lugar onde as 4 camadas se encontram —
e elas se encontram aqui, não diretamente entre si.
Nenhuma pasta fala com outra diretamente.
Tudo passa pelo corredor central."

---

## SEÇÃO 4: TRANSFERÊNCIA — 3 PERGUNTAS (4 min)

**Tom:** Retórico — professor pergunta e responde, reforça a independência entre camadas

"Três perguntas. São perguntas que vão aparecer de novo quando o projeto crescer.

---

**Pergunta 1:**
O ClinMd-Tribe foi pedido para rodar como página web em vez de app desktop.
Qual pasta muda?

Só `presentation/` — a Recepção.
O Médico não sabe se há Flet ou HTML.
O Laboratório não sabe se há botão roxo ou link azul.
Você troca a Recepção. O hospital continua funcionando.

---

**Pergunta 2:**
Nova diretriz: no CHA2DS2-VASc, idade maior que 75 anos agora vale 3 pontos.
Qual pasta muda?

Só `domain/` — o Médico.
A Recepção não recebeu nenhum memorando clínico.
A Triagem continua orquestrando do mesmo jeito.
O Laboratório continua salvando do mesmo jeito.
Só o protocolo clínico muda — e está isolado no lugar certo.

---

**Pergunta 3:**
A clínica quer migrar o armazenamento local para um banco SQLite centralizado.
Qual pasta muda?

Só `infrastructure/` — o Laboratório.
O Médico não sabe onde o resultado é guardado.
A Triagem só pede 'salva isso' — não sabe como.
Você treina o Laboratório no novo sistema. O resto não muda.

---

Três perguntas. Três vezes a mesma resposta: só uma pasta.

Isso é o que a Clean Architecture compra para o ClinMd-Tribe.
Cada mudança — clínica, visual ou técnica — tem um endereço certo.
Sem varrer o código inteiro. Sem risco de quebrar o que não devia."

---

## SEÇÃO 5: @software-architect — VALIDAÇÃO ARQUITETURAL (3 min)

**Tom:** Consulta especializada — decisão arquitetural validada antes de avançar

"Antes de ir para as calculadoras, vamos consultar o arquiteto do time.

```
@software-architect, o ClinMd-Tribe está usando Clean Architecture
com 4 camadas: presentation, application, domain, infrastructure.
Cada camada tem __init__.py e um placeholder.
As dependências apontam para dentro — domain não importa nada das outras camadas.
Essa estrutura é robusta para crescer com calculadoras clínicas,
anotador e RAG local? Algum risco arquitetural a antecipar?
```

[mostrar a resposta do software-architect]

O arquiteto vai validar as decisões estruturais e pode apontar
padrões que aparecem nos próximos módulos — como onde colocar
utilitários compartilhados entre camadas.
Guarde as sugestões."

---

## SEÇÃO 6: @caetano-cto — VALIDAÇÃO TÉCNICA (3 min)

**Tom:** Aprovação do CTO antes de avançar para features

"Agora o CTO técnico do time:

```
@caetano-cto, o scaffold do ClinMd-Tribe está gerado e rodando.
4 pastas, 4 __init__.py, 4 placeholders, main.py integrado.
uv run python main.py imprime as 4 camadas e abre a janela Flet sem erro.
Validação técnica: estamos prontos para começar
as calculadoras clínicas no próximo módulo?
```

[mostrar a resposta do Caetano]

O Caetano vai confirmar a prontidão técnica e pode recomendar
algum ajuste antes de entrar no módulo das calculadoras."

---

## SEÇÃO 7: @capitolino-cpo — VALIDAÇÃO DE PRODUTO (3 min)

**Tom:** Confirmação do roadmap de produto antes de fechar o módulo

"E o CPO — para garantir que a estrutura que construímos
suporta o produto que planejamos:

```
@capitolino-cpo, o scaffold do ClinMd-Tribe está pronto em Clean Architecture.
presentation, application, domain, infrastructure.
O próximo módulo implementa as calculadoras clínicas:
CHA2DS2-VASc, PHQ-9, GAD-7.
Essa arquitetura suporta o roadmap completo do produto —
incluindo o anotador e o RAG local que vêm depois?
```

[mostrar a resposta do Capitolino]

O CPO olha pelo lado do produto — se a estrutura técnica
serve o que o médico vai precisar usar no consultório."

---

## SEÇÃO 8: /tab_pendencias (2 min)

**Tom:** Registro canônico — fechar o ciclo de trabalho

"Atualize as pendências:

```
/tab_pendencias
```

[mostrar a tabela — scaffold concluído, calculadora CHA2DS2-VASc como próxima tarefa]

Olha o que mudou de posição.
'Scaffold ClinMd-Tribe' passou para Concluído.
'Calculadora CHA2DS2-VASc' está no topo das próximas tarefas.

Essa tabela é o placar do seu projeto.
Cada aula move uma peça."

---

## SEÇÃO 9: ENCERRAMENTO + DEVER DE CASA (3 min)

**Tom:** Síntese motivacional e ponte para as calculadoras

"Resumo do que ficou pronto hoje.

Um único prompt ao Claude Code transformou o arquitetura.txt
em estrutura real:
4 pastas, 4 credenciais, 4 placeholders clínicos, main.py integrado.

O projeto roda. As 4 linhas apareceram no terminal.
A janela Flet abriu.

Você não digitou uma linha de código.
Você descreveu o que queria. O Claude construiu. Você validou.

---

E você sabe o que muda quando cada componente muda:
só uma pasta, sempre a pasta certa.

Isso é o que separa um código que cresce
de um código que emperra na segunda mudança.

---

Dever de casa.

Escreva num papel ou arquivo de texto — não no código:

Primeira: qual calculadora você quer implementar primeiro?
CHA2DS2-VASc, PHQ-9, GAD-7, NIHSS — a que você mais usa na prática.

Segunda: em qual pasta ela vai morar, e por quê?

Terceira: qual seria o primeiro prompt que você daria ao Claude Code?

Na próxima aula: as calculadoras clínicas.
O CHA2DS2-VASc sai do arquitetura.txt e entra no domain/calculadoras.py —
como código real, isolado, testável.

Até lá."

---

**FIM DO ROTEIRO**
