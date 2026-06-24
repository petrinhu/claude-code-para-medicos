# Aula 07 — Gestão do Consultório: Indicadores, Faturamento e Automação

**Formato:** Gravada no OBS Studio, editada no Kdenlive  
**Duração:** ~48 min  
**Tom:** Colega com humor leve e didático — "hoje você vira gestora do próprio negócio"  
**Persona:** Metabologista de consultório — continuidade das aulas 05 e 06  

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Já preparado em `resources/` (é só usar):**

- [ ] `resources/consultas_agosto.csv` : planilha fictícia de 120 atendimentos de agosto/2025 (mesmo formato do CSV gerado ao vivo, dados diferentes), insumo da Seção 5 (demonstração de reaproveitar o prompt trocando só o arquivo).

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta desta aula.
- [ ] Sessão limpa, sem conversa anterior carregada (a demo nasce do zero).
- [ ] O `resources/consultas_agosto.csv` copiado para a pasta de trabalho da sessão (ou tenha o caminho à mão), para que o Claude o leia quando você "mostrar o segundo CSV" na Seção 5.

**Confira antes de gravar:**

- [ ] O CSV principal (`consultas_2025.csv`) e o dashboard (`dashboard_consultorio.html`) são criados ao vivo pelo Claude; saiba em que pasta eles caem para abri-los na tela.
- [ ] Abra o `consultas_agosto.csv` uma vez antes de gravar para confirmar que está legível (120 linhas, colunas de convênio, valores e status).
- [ ] Teste a abertura do dashboard HTML no navegador (duplo-clique) antes de gravar. Para o momento de impacto da Seção 6 no celular, mande o arquivo `.html` para o seu próprio WhatsApp ou e-mail e confirme que ele abre no navegador do telefone (arquivo self-contained abre em qualquer celular). Não dependa do `/remote` para isso: o Remote Control conecta a SESSÃO do Claude ao celular, não serve um arquivo HTML local para o navegador do telefone.

**Navegador:** o dashboard HTML gerado é aberto no navegador na Seção 6 (arquivo local, sem site externo). Nenhuma URL precisa estar pré-aberta.

---

## SEÇÃO 1: ABERTURA — 2 min

**Tom:** Callback do arco do M3 — fechar o módulo com sensação de progressão

**[Aviso rápido dos óculos, antes de mergulhar]**

"Último recado dos óculos antes do grand finale do módulo: hoje a tela vai ter planilha, número de faturamento e dashboard, e dígito pequeno a gente não chuta, a gente confere. Quem usa óculos pra perto, é a deixa pra colocar, porque conta de consultório errada por causa de vista cansada dói mais que glosa. Ajeitou? Então vamos fechar esse módulo com chave de ouro."

"Nas últimas duas aulas você aprendeu a comunicar e a publicar.

aula_05: posts para o Instagram, newsletter, conteúdo para o Substack.
aula_06: estudo científico, análise estatística, pôster de congresso.

Hoje você fecha o Módulo 3.

E fecha de um jeito diferente.

Hoje você não vai criar conteúdo para o mundo exterior.
Hoje você vai olhar para dentro.

Você vai enxergar o que está acontecendo dentro do próprio consultório.

Qual convênio paga mais? Em qual dia há mais no-show?
O faturamento está crescendo ou caindo?

Perguntas que todo médico tem — e quase nenhum consegue responder com dado."

---

## SEÇÃO 2: CENÁRIO — 4 min

**Tom:** Situação real, identificação imediata, dois problemas concretos

"Cenário.

A mesma metabologista das últimas duas aulas.
Consultório próprio. Seis anos de carreira.
Três convênios no CNPJ: Convênio Alfa, Convênio Beta, Convênio Gama. Mais particular.

Ela atende 20 a 25 pacientes por semana —
consultas de primeira vez, retornos, pequenos procedimentos ambulatoriais.

Dois problemas que ela não consegue resolver sem dado.

---

Problema 1: ela não sabe qual convênio paga mais pela mesma consulta.

Acha que é o Convênio Alfa. Mas não tem certeza.
Só descobre quando o extrato chega no fim do mês —
e nem entende o extrato porque vem cheio de glosa.

Glosa: o valor que o convênio deveria pagar menos o que efetivamente pagou.
Um convênio pode tabular 300 reais e repassar 240.
Sem dado, ela não sabe qual convênio glosa mais.

---

Problema 2: a taxa de no-show está alta, mas ela não sabe em qual dia.

Desconfia que é segunda-feira. E provavelmente está certa.
Mas sem dado, é chute. E chute não vira decisão de agenda.

---

Hoje ela vai ter os dados.

Tudo em uma tela, em um arquivo.
Que ela manda para o contador e ele entende.

Vamos começar."

---

## SEÇÃO 3: DEMO — CSV DE ATENDIMENTOS — 8 min

**Tom:** Prático, explicando cada coluna e o que ela representa financeiramente

"Primeiro: os dados.

Na vida real, você exportaria uma planilha do sistema do consultório.
Mas vamos gerar um CSV simulado — o fluxo é exatamente o mesmo.

[digitar no terminal]

```
Gere uma planilha CSV simulada com 120 atendimentos de um consultório de
endocrinologia/metabolismo dos últimos 6 meses (janeiro a junho de 2025).

Colunas:
- Data: distribuída entre janeiro e junho de 2025
- Dia_semana: segunda a sexta
- Tipo_atendimento: Consulta (primeira vez), Retorno, Procedimento
  (proporções realistas — Retorno é o mais frequente)
- Convenio: Convênio Alfa, Convênio Beta, Convênio Gama, Particular
  (distribua de forma realista — Convênio Alfa é o mais comum)
- Valor_tabela_R$: valor que o convênio deveria pagar
- Valor_recebido_R$: valor que efetivamente entrou (menor que tabela = glosa)
- Status: Realizado, No-show, Cancelado
- Mes: janeiro a junho (para facilitar agrupamento)

Use 'Paciente 001, 002...' se precisar de coluna de paciente.
Salve como consultas_2025.csv.
```

[aguardar e mostrar o arquivo]

---

Pronto. 120 linhas, 8 colunas.

Olha a coluna Valor_tabela_R$ e a Valor_recebido_R$.

Em todo atendimento de convênio, o valor recebido é menor que o tabelado.
Essa diferença é a glosa.

Você trabalhou, o convênio pagou menos do que prometeu.
Quanto? Depende do convênio. E você vai descobrir agora.

E a coluna Status: Realizado, No-show, Cancelado.
No-show é o paciente que marcou e não veio — sem aviso, sem cancelamento.
Esse espaço vazio custa dinheiro real.

Uma nota rápida: a coluna Tipo_atendimento diz 'Procedimento' — e isso é intencional.
Se você é cirurgião, lê como cirurgia. Se é psiquiatra, lê como sessão de procedimento.
A lógica financeira é idêntica para qualquer especialidade.

Esse arquivo é a radiografia financeira do consultório.
Agora vamos fazer a leitura."

---

## SEÇÃO 4: DEMO — ANÁLISE DE INDICADORES — 8 min

**Tom:** Didático, mostrando cada indicador com reação clínica concreta

"Com a planilha criada, vamos pedir a análise completa.

[digitar no terminal — com o consultas_2025.csv já na sessão]

```
Analise o arquivo consultas_2025.csv e me entregue um relatório
de indicadores de gestão do consultório:

1. Faturamento total dos 6 meses (valor recebido)
2. Faturamento por convênio — ranking do maior para o menor pagador
3. Taxa de glosa por convênio: diferença entre valor_tabela e valor_recebido
4. Taxa de no-show geral (%) e por dia da semana — em qual dia tenho mais falta?
5. Sazonalidade: os 3 meses com mais atendimentos e os 3 com menos
6. Tendência de faturamento mês a mês — estou crescendo ou caindo?

Para cada indicador: uma tabela + uma frase de interpretação prática.
```

[aguardar e mostrar resultado]

---

Olha o que saiu.

Faturamento total: você sabe pela primeira vez exatamente quanto entrou em 6 meses.

Ranking de convênios: o Convênio Alfa realmente paga mais? Ou o Particular bate todos?
Isso muda decisão de credenciamento.

Glosa por convênio: qual convênio desconta mais do que deveria?
Se o Convênio Beta glosa 20% e o Convênio Gama glosa 8% — você tem argumento para renegociar.

No-show por dia: segunda realmente lidera?
Confirme aqui e já ajuste a agenda —
segunda pode virar dia de retorno curto, não de primeira consulta.

Sazonalidade: quais meses são fracos?
Fevereiro caiu — provavelmente carnaval.
Julho caiu — férias.
Outubro subiu — isso pode ser planejado.

Esses números contam a história do consultório.
Agora você vai aprender a reusar esse raciocínio todo mês sem reescrever nada."

---

## SEÇÃO 5: DEMO — AUTOMAÇÃO — 9 min

**Tom:** Revelar o conceito de automação sem código antes de demonstrar

"Aqui entra o M3.05 que estava no nome da aula e que a gente ainda não chegou:
automação.

Automação sem programação não é mandar email sozinho.
Não é robô clicando na tela.

É isso: você escreve o raciocínio uma vez — e usa toda vez que precisar.

O trabalho que se repete não é o resultado.
É o raciocínio para chegar no resultado.
E o Claude guarda o raciocínio para você.

---

Vou demonstrar.

Preparei um segundo CSV — agosto de 2025.
Um mês a mais, mesmo formato, dados diferentes.

[mostrar consultas_agosto.csv na tela]

Agora rodar o mesmo prompt de indicadores com esse arquivo.
Sem reescrever nada:

[digitar no terminal — mesmo prompt da seção anterior]

```
Analise o arquivo consultas_agosto.csv e me entregue um relatório
de indicadores de gestão do consultório:

1. Faturamento total do mês (valor recebido)
2. Faturamento por convênio — ranking do maior para o menor pagador
3. Taxa de glosa por convênio
4. Taxa de no-show geral (%) e por dia da semana
5. Comparação com o mês anterior — cresceu ou caiu?

Para cada indicador: uma tabela + uma frase de interpretação prática.
```

[aguardar e mostrar resultado]

---

Mesmo relatório. Estrutura idêntica. Dados do mês novo.

Você não reescreveu nada.
Trocou o arquivo, não o prompt.

Salva esse prompt em um arquivo de texto.
Todo mês: troca o CSV, roda o prompt, tem o relatório.

Isso é automação sem programação.

---

Segundo entregável de automação: o checklist de fechamento mensal.

[digitar no terminal]

```
Crie um checklist de fechamento financeiro mensal para um consultório
de metabolismo, em passos numerados, para eu seguir todo último dia útil do mês.
Inclua: conferência de repasses de convênio, glosas a recontestar,
faturamento particular recebido, contas fixas a pagar, e os 3 indicadores
que devo calcular. Formato: lista de tarefas com [ ].
```

[mostrar resultado]

---

Agora você tem uma rotina de fechamento.
Igual a um protocolo de alta hospitalar — cada passo checado, nada esquecido.

---

Antes de ir para o dashboard: uma pausa obrigatória.

Você vai querer usar isso com dados reais do seu consultório.
E você deve — é para isso que serve.

Mas siga esta regra antes de subir qualquer arquivo:
des-identifica primeiro.

Nome do paciente: vira 'Paciente 001, 002'.
CPF: apaga.
Diagnóstico nominal: apaga.

O Claude precisa do padrão financeiro —
data, convênio, valor, status.
Não precisa saber quem é o paciente.

Dado que identifica o paciente nunca entra.
O padrão financeiro pode entrar des-identificado.

Vou repetir isso em toda aula deste curso."

---

## SEÇÃO 6: DEMO — DASHBOARD HTML — 12 min

**Tom:** Revelação — abrir o arquivo no navegador é o momento de maior impacto da aula

"Agora a cereja do bolo.

Tudo que analisamos vai virar um dashboard —
uma tela com gráficos e indicadores —
em um único arquivo que você abre no navegador.

Sem instalar nada. Sem login. Sem servidor.
Funciona no Windows, no Mac, no celular.
Você manda por email para o contador e ele abre no computador dele.

[digitar no terminal]

```
Com base nos dados de consultas_2025.csv, crie um dashboard de gestão
do consultório de metabolismo.

O resultado deve ser um único arquivo HTML que funciona no navegador
sem precisar de internet ou servidor (self-contained).
A biblioteca de gráficos deve estar EMBUTIDA dentro do próprio arquivo —
sem nenhum link para CDN ou internet externa.
O arquivo precisa abrir com duplo-clique no Windows sem instalar nada.

Conteúdo:

Linha superior — 4 cards de resumo:
- Faturamento total (6 meses, valor recebido)
- Total de atendimentos realizados
- Taxa de no-show (%)
- Convênio que mais paga

Gráficos:
1. Barras: faturamento recebido por convênio
2. Linha: faturamento mensal (janeiro a junho)
3. Barras horizontais: no-show por dia da semana

Tabela: sazonalidade — atendimentos por mês,
com destaque visual nos meses fortes e nos meses fracos.

Estilo: limpo, fundo branco, cores sóbrias.
Salve como dashboard_consultorio.html.
```

[aguardar]

[abrir o arquivo no navegador]

---

Olha isso.

Cards de resumo no topo — uma olhada e você sabe o semestre.
Gráfico de barras — em dois segundos você vê qual convênio paga mais.
Gráfico de linha — a tendência dos 6 meses na frente dos seus olhos.
Tabela de sazonalidade — os meses fracos em vermelho, os fortes em verde.

[mandar o arquivo .html para o próprio WhatsApp e abrir no celular]

E abre no celular. Mesmo arquivo.
Porque ele é self-contained, autossuficiente: tudo dentro de um arquivo só.
Você manda por WhatsApp para o contador, ele toca no arquivo, e abre, sem instalar nada.

---

Agora para um segundo.

Este arquivo tem 400, 500 linhas de código por dentro.
Você não viu nenhuma.

Você só descreveu o que queria:
quatro cards, três gráficos, uma tabela, self-contained, fundo branco.

E o Claude construiu os meios.

É exatamente assim que o Claude Code funciona:
você descreve o resultado, ele constrói os meios.

Guarda essa frase.
Ela vale para o dashboard, para os slides, para o folheto.
E vai valer para tudo que você vai construir na fase avançada."

---

## SEÇÃO 7: FECHAMENTO DO M3 — 5 min

**Tom:** Dois destinos válidos — validar quem para ANTES de convidar quem continua

"Resumo do que a gente fez hoje.

CSV de 6 meses de atendimentos, com glosa e no-show.
Análise de indicadores: faturamento, convênio, sazonalidade.
Prompt-receita: o mesmo raciocínio rodando todo mês com um arquivo novo.
Checklist de fechamento: protocolo de alta para o financeiro do consultório.
Dashboard HTML: uma tela, offline, para mandar para o contador.

Sem Excel complexo. Sem Power BI. Sem programar.
Só descrevendo o problema em linguagem natural.

---

Dever de casa.

Pegue uma planilha real do seu consultório —
de agendamentos, de faturamento, do que você tiver.

Antes de qualquer coisa: des-identifica.
Nome → Paciente 001. CPF → apaga. Diagnóstico → apaga.

Depois peça ao Claude os mesmos indicadores que a gente gerou hoje.

E — isso é o mais importante —
salve o prompt como receita.
Coloca em um arquivo de texto.
Você vai usar no mês que vem.

---

E com isso a gente fecha o Módulo 3.

Pensa no que você fez neste módulo:

aula_05: criou conteúdo para o Instagram e newsletter em minutos.
aula_06: montou um estudo científico com análise estatística e pôster.
aula_07: transformou dados do consultório em indicadores e dashboard.

Tudo sem programar.
Tudo descrevendo o problema em linguagem natural.

---

Se você quiser parar aqui:

Você já entrega mais do que a maioria dos médicos com IA.
Você sabe conversar, pesquisar, criar, publicar e gerir.
Isso é mais do que suficiente para mudar o jeito que você trabalha.

---

Se quiser ir além:

A fase avançada começa na próxima aula.

Vai ter um pouco de código — mas guiado, passo a passo,
do jeito que você aprendeu um novo protocolo clínico.

O dashboard que você fez hoje é a versão descartável —
você gera, usa uma vez, e refaz no mês seguinte.

Na fase avançada você aprende a construir algo que fica permanente:
um app clínico, com interface gráfica, banco de dados local,
busca inteligente em PDFs de guideline.

A habilidade é a mesma que você já tem.
Só vai mais fundo.

---

Nos dois casos: obrigado por chegar até aqui."

---

**FIM DO ROTEIRO**
