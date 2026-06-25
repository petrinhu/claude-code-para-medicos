# Aula 39 — A Conferência Final: o Lote Sai do Laboratório

**Formato:** Gravada no OBS Studio, editada no Kdenlive
**Duração:** ~55 min
**Tom:** Orgulho contido de quem fecha um produto. "Funcionar é metade; liberar é assumir a responsabilidade pelo que vai pra mão do outro." Ritual de conferência, e o gesto adulto de assinar a liberação.
**Módulo:** S11.03 — Auditoria final e distribuição (última do polimento)

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] git em dia (trabalho salvo e enviado).
- [ ] O .exe gerado na aula passada existe e está localizado na pasta dist/.

**Confira antes de gravar:**

- [ ] O veredito honesto do LACRE é "limpo" (o app é offline e não usa token de API); NÃO invente um token falso. Se a conta-piloto tiver um token real no histórico de algum teste antigo, o cenário "ATENÇÃO GRAVE, gancho aula 40" fica mais forte; grave a fala pronta nos dois cenários (achou / não achou).
- [ ] A pasta data/ já está excluída desde a aula 38; o item PUREZA confirma, não refaz.
- [ ] O gate de tamanho do SOBRA reusa o da aula 38 (.exe acima de uns 300 MB = peça pesada vazou); o Claude reporta o tamanho real.
- [ ] A bula é gerada como LEIA-ME.txt (não .md, pra o colega zero-TI abrir com dois cliques no Bloco de Notas), no máximo 1 página, salva na mesma pasta do .exe.
- [ ] A versão é carimbada SÓ depois do laudo "liberado": git tag v1.0 (o Claude cria) com o nome EXATO v1.0, e git push origin v1.0 (você cola).
- [ ] PROIBIDO nesta aula: mostrar .env, qualquer string de chave (sk-...), git log/histórico cru, ou explicar variável de ambiente; isso é 100% da aula 40.

**Navegador:** nenhum site é necessário ao vivo (o git push origin v1.0 vai pela linha de comando; o GitHub Release pra anexar o .exe é só mencionado, não executado).

---

## SEÇÃO 1: ABERTURA — O REMÉDIO FUNCIONA. MAS O LOTE NÃO SAIU AINDA. — 5 min

**Tom:** Reflexivo, orgulho contido. Retoma a ponte herdada da aula_38 e nomeia o que falta.

**[Aviso rápido dos óculos, antes de mergulhar]**

"Última conferência do produto pede última conferência da sua vista também: põe os óculos. Hoje você vai ler um laudo linha por linha, igual hemograma, e quem libera lote não confere com a tela embaçada. Visão nítida, assinatura tranquila."

"Na aula passada você fez a caixa. Ela abre com dois cliques, o remédio funciona, na mão de qualquer médico. Para um segundo e sente o tamanho disso — no começo do curso você não sabia o que era um terminal.

E aí eu te segurei na porta. Lembra? Eu disse: um laboratório sério não joga a caixa na rua assim. Antes do lote chegar na prateleira, tem uma última conferência.

---

Funcionar é uma coisa. Liberar é outra.

Funcionar é o remédio fazer efeito na sua bancada. Liberar é o controle de qualidade do laboratório dizer, de cabeça erguida e assinando embaixo: este lote pode ir pra mão de outro médico.

Hoje você é esse controle de qualidade. Do seu próprio produto.

---

A gente vai fazer a conferência final: o lacre está fechado? Não escapou nenhuma chave, nenhum dado de paciente, nenhuma sobra? E o colega vai saber usar — cadê a bula?

E como o curso inteiro: você não vai ler uma linha de código. Você vai PEDIR a conferência, VER ela acontecer, e ASSINAR a liberação."

---

## SEÇÃO 2: O QUE O CONTROLE DE QUALIDADE CONFERE — 9 min

**Tom:** Didático, tranquilo. A maquete mental antes de qualquer comando: o que é auditar uma entrega, e por que se confere mesmo achando que está tudo bem.

"Antes de pedir nada, o mapa do que a gente vai conferir. E você já fez isso uma vez, com outro nome.

Lembra do checklist cirúrgico que você construiu? O time-out. Antes da incisão, a equipe para, confere item por item, em voz alta, ANTES do ponto sem volta. A entrega tem o ponto sem volta dela: o momento em que a caixa sai da sua mão e você não controla mais. A conferência é antes disso.

---

São quatro itens. Quatro vistos antes de liberar:

Primeiro — o LACRE. Foi alguma chave secreta, alguma senha sua, junto na caixa? Nenhum segredo pode viajar numa entrega.

Segundo — a PUREZA. A pasta `data/` ficou de fora? Nenhum banco, nenhum artigo, nenhum dado de paciente entrou?

Terceiro — a SOBRA. A caixa tem só o app de bolso? Não vazou peça pesada que você mandou deixar de fora?

Quarto — a BULA. O colega vai saber usar? Cadê as instruções?

---

Agora, a pergunta que você já está fazendo: 'meu app é offline, não tem senha nenhuma dentro, pra que conferir?'.

Eu te respondo com a regra do bom laboratório: a conferência que mais vale é a que dá tudo certo. Porque foi ela que te deixou assinar tranquilo.

No centro cirúrgico, ninguém pula o time-out porque 'é uma cirurgia simples e eu sei o que tô fazendo'. Justamente nessas a falha passa. A gente não confere porque desconfia do app. A gente confere porque é a conferência que vira a sua assinatura em algo seguro.

Quem confia sem conferir, um dia entrega a caixa com a chave dentro.

---

No fim de hoje, o que mais vale não é um arquivo novo. É uma coisa mais rara: o direito de dizer 'liberado'."

---

## SEÇÃO 3: VOCÊ DECIDE — 8 min

**Tom:** Colaborativo. Duas perguntas, raciocínio clínico, zero código.

"Antes de pedir a conferência pro Claude, duas perguntas. Pensa como o controle de qualidade que decide se um lote sai ou não.

---

**PERGUNTA UM — o seu app é 100% offline e você tem certeza de que nunca colocou senha nenhuma dentro dele. Vale a pena fazer a conferência de segurança antes de entregar?**

A: Não. Se você sabe que é offline e que não tem senha, conferir é perda de tempo.

B: Sim, sempre. Você confere não porque desconfia do app, mas porque é a conferência que transforma o seu 'acho que está limpo' em 'está limpo, eu verifiquei' — e é isso que te deixa assinar a entrega com responsabilidade.

C: Só se for entregar pra muita gente. Pra um colega só, dá pra pular.

Pensa um segundo.

---

É a B, e essa é a alma da aula de hoje.

A é a armadilha mais perigosa do profissional confiante: 'eu sei que está tudo bem, não preciso conferir'. É exatamente assim que a caixa sai com a chave dentro — não por maldade, por excesso de confiança.

C é perigosa de um jeito sutil: o tamanho da plateia não muda o seu dever. Um segredo que vaza pra UMA pessoa errada já vazou. A responsabilidade da entrega é absoluta, não proporcional ao número de colegas.

Critério que fica: 'não tinha' só vale depois de 'eu procurei'.

---

**PERGUNTA DUAS — você vai mandar o programa pro seu colega por um link. O que precisa ir junto?**

A: Só o programa. Ele é médico, é inteligente, descobre sozinho como abrir. Bula é firula.

B: O programa e uma bula curta em português leigo — como abrir, o que fazer se o Windows avisar 'aplicativo não reconhecido', e que é offline.

C: O programa, a bula, e também a sua senha pra ele conseguir conectar o app na internet.

Pensa.

---

É a B.

A confunde competência clínica com competência de informática. O seu colega é craque em medicina — e na aula um, você, craque em medicina, não sabia o que era um terminal. Sem a bula, ele clica, o Windows mostra a tela azul, ele se assusta e desiste. O seu ótimo app morre na porta por falta de uma instrução de uma linha. Software sem bula é alta sem orientação de alta.

C tem dois erros graves. Primeiro: este app não precisa de senha nenhuma — é offline. Segundo, e mais sério: você NUNCA manda uma senha ou chave sua junto com um programa. Isso é o erro de segurança clássico, e é o assunto da próxima aula inteira. A bula ensina a USAR; ela jamais carrega a sua chave.

Critério que fica: pronto inclui usável. A entrega leva o app e o mínimo pra quem recebe usar com autonomia — e leva zero segredo seu."

---

## SEÇÃO 4: A CONFERÊNCIA DO LOTE — A AUDITORIA AO VIVO — 13 min

**Tom:** Mãos à obra, ritmo de ritual. O aluno pede a auditoria e LÊ o laudo em português.

"Hora da conferência. Como sempre, o ritual de terreno primeiro. Cola:"

[TELA: digitar o Prompt 0 no Claude Code]

```
Você é meu par de programação e, hoje, o meu controle de qualidade. A aula de hoje é a
conferência final antes de eu entregar o app ClinMd-Tribe (o .exe da aula passada) na mão
de um colega. Não vamos mudar o app — vamos AUDITAR o que vai ser entregue.

Confirme em português, SEM saída técnica crua, em uma frase cada: (1) o meu trabalho está
salvo e enviado (git em dia)? (2) o .exe que eu gerei na aula passada existe e está
localizado? Se algo estiver pendente, me avise. NÃO me mostre código nem configuração.
```

"Terreno confirmado. Agora a auditoria de verdade. Eu vou pedir um laudo — igual ao laudo de um exame, com resultado em cada linha. Cola:"

[TELA: digitar o Prompt 1 — a auditoria]

```
Agora faça uma auditoria de segurança da minha entrega e me devolva um LAUDO em português,
escrito pra um médico, SEM me mostrar nenhum código, arquivo ou saída técnica crua. Trate
cada item como um exame, com resultado: OK (verde), ATENÇÃO (amarelo) ou PARE (vermelho).

Confira:

  1. LACRE — nenhum segredo viajou junto. Vasculhe os arquivos do projeto E todo o histórico
     de versões procurando qualquer senha, chave ou token de API. Confirme também que existe
     a regra que mantém fora do projeto o arquivo onde chaves secretas ficariam guardadas. Se
     encontrar um segredo, marque ATENÇÃO GRAVE, me diga o que é, mas NÃO tente consertar —
     isso é assunto da próxima aula.

  2. PUREZA — nenhum dado de paciente viajou junto. Confirme que a pasta data/ (banco,
     artigos, busca) está protegida e nunca foi parar no projeto enviado, e que o programa
     que viaja começa vazio.

  3. SOBRA — só o que devia ir, foi. Confirme que o pacote (.exe) tem só a versão de bolso
     (calculadoras, checklist, painel) e que nenhuma peça pesada da busca vazou. Cheque o
     tamanho: se estourou o esperado, algo pesado entrou.

No fim, um VEREDITO de uma linha: "lote liberado para entrega" ou "lote retido — corrija X
antes". Para cada OK, diga em uma frase por que está seguro. Para ATENÇÃO/PARE, diga o que é
e a conduta; conserte só o que for simples e seguro (como adicionar uma regra ao .gitignore).
NÃO me mostre código.
```

"E o Claude te devolve um laudo. Mais ou menos assim:

LACRE — verde. Varri os arquivos e o histórico inteiro: nenhuma senha, nenhuma chave. Limpo.
PUREZA — verde. O banco e os artigos estão na pasta data/, protegida; nenhum paciente saiu.
SOBRA — verde. Só calculadoras, checklist e painel; tamanho dentro do esperado, sem a busca.
VEREDITO: lote liberado para entrega.

---

Olha que coisa boa. E olha por que a gente conferiu mesmo assim.

O laudo diz: não achei chave nenhuma. Ótimo. Mas você só pode dormir tranquilo porque PROCUROU. 'Não tinha' só vale depois de 'eu procurei'.

Você leu isso exatamente como lê um hemograma: a coluna da esquerda é o resultado, a frase do lado é o que ele significa. Você não abriu um arquivo, não leu uma linha de código. Pediu o exame e leu o laudo.

---

Se algum item viesse amarelo — ATENÇÃO — você não jogava fora. Você corrigia o simples na hora e conferia de novo. E se viesse vermelho — PARE — aí o lote não sai: vermelho é 'retém até resolver', não 'corrige e segue'. No nosso app offline isso não vai acontecer, mas o critério fica. Erro na conferência é a conferência funcionando.

Agora, o quarto item — a bula. Cola:"

[TELA: digitar o Prompt 2 — a bula]

```
A auditoria passou. Agora gere a BULA da entrega: um arquivo de texto simples chamado
LEIA-ME.txt, escrito pra um colega médico que NÃO fez este curso e não sabe nada de
computador. Linguagem de bula de remédio: curta, clara, sem jargão. No máximo uma página.

Inclua, nesta ordem:
  - O que é o programa (calculadoras, checklist cirúrgico, painel; roda no Windows).
  - Como abrir: dois cliques no ClinMd-Tribe.exe; a 1ª abertura demora uns segundos
    (normal); não precisa instalar nada.
  - O aviso azul do Windows: se aparecer "O Windows protegeu o seu computador", clicar em
    "Mais informações" e depois "Executar assim mesmo"; não é vírus; NUNCA desligar o
    antivírus.
  - Funciona 100% offline; os dados ficam só na máquina dele; sem nuvem, sem login.
  - Requisitos: Windows 10 ou 11.

Salve como LEIA-ME.txt na pasta onde está o .exe. Me mostre o texto pronto, em português,
pra eu ler e aprovar.
```

"O Claude escreve a bula e te mostra. Lê com calma — é o texto que o seu colega vai ler. Está em português de gente, sem jargão? Tem o aviso do antivírus? Diz que é offline? Aprovado. Quatro itens, quatro vistos."

---

## SEÇÃO 5: A ASSINATURA — O LOTE ESTÁ LIBERADO — 10 min

**Tom:** O ápice de uma aula de fechamento. Desacelera. O clímax não é técnico — é o gesto de liberar e carimbar.

"Vamos ver o lote pronto. Abre a pasta da caixa:"

[TELA: no terminal]

```bash
explorer dist
```

"O Windows abre a janela de arquivos. E agora tem dois arquivos lado a lado: o `ClinMd-Tribe.exe` e o `LEIA-ME.txt`. A caixa e a bula. O kit de entrega completo.

---

Para. Olha o que tem na sua frente: o programa, e o papel que ensina a abrir o programa. Isso é um lote pronto pra sair de um laboratório de respeito.

E agora você faz uma coisa que nenhum software seu fez até hoje: você LIBERA. Confere mentalmente os quatro vistos — lacre, fechado; pureza, sem paciente; sobra, só o que devia; bula, escrita. E assina: este lote pode ir pra mão do meu colega.

---

E um laboratório sério carimba o número do lote. Vamos dar a este uma versão oficial: a 1.0. Cola:"

[TELA: digitar o Prompt 3 — carimbar a versão]

```
A entrega está auditada e com bula. Quero carimbar isso como a primeira versão oficial, a
"1.0" — como o número de lote de um remédio liberado.

Antes de carimbar, garanta que tudo que faz parte da entrega (inclusive a bula que a gente
acabou de gerar) está salvo e enviado, pra a marca apontar exatamente pro lote que eu
auditei. Cuide disso você, sem me mostrar comando — só confirme em uma frase que está em dia.

Depois, crie a marca de versão com o nome EXATO `v1.0` (não `v1.0.0`, não outro formato) e
me dê o comando de envio já com esse nome `v1.0` dentro, pra eu colar igual. Me explique em
uma frase o que essa marca significa, e em outra como eu poderia, se quisesse, anexar o .exe
a essa versão no GitHub pra um colega baixar por link — sem fazer agora. NÃO me mostre código.
```

[TELA: no terminal — o comando que o Claude forneceu]

```bash
git push origin v1.0
```

"Pronto. Versão 1.0, carimbada e registrada. O seu produto tem número de lote.

---

Para um segundo e pensa no caminho.

No começo do curso você abria o software dos outros. Depois você construiu o seu. Hoje você fez a coisa mais adulta que um construtor faz: olhou pro próprio produto, conferiu com rigor, e assumiu a responsabilidade de entregar.

Você não é mais só quem usa software. Nem só quem constrói. Você é quem responde pelo que entrega."

---

## SEÇÃO 6: O QUE A CONFERÊNCIA NÃO É — E A CHAVE QUE MERECE UMA AULA — 4 min

**Tom:** Honesto, desmistificador, plantador do gancho. Abre a porta para a aula_40 sem invadir o conteúdo.

"Duas honestidades pra fechar bem.

A primeira: a conferência não é blindagem eterna. Você conferiu ESTE lote, HOJE. Se amanhã você mudar o app e gerar uma caixa nova, confere de novo. Liberação é por lote, não pra sempre. Igual no laboratório.

---

A segunda — e aqui mora a porta pra próxima aula.

No item LACRE, a gente procurou por uma chave secreta e, ainda bem, não achou — porque este app é offline e não usa nenhuma. Mas existe um tipo de chave que vale ouro, e que um dia você vai ter na mão: o token de API. A senha que dá acesso a um serviço na sua conta, no seu dinheiro.

Esse tipo de chave NUNCA pode chegar nem perto de uma caixa que você entrega, nem de um lugar público. E tem um detalhe traiçoeiro: apagar a chave de um arquivo não apaga ela do histórico — ela fica guardada lá atrás.

Como se guarda uma chave dessas do jeito certo, pra ela nunca vazar — é a sua próxima aula, inteira. Hoje você aprendeu a PROCURAR a chave na saída. Na próxima, a guardá-la na entrada."

---

## SEÇÃO 7: ENCERRAMENTO — LOTE LIBERADO, LABORATÓRIO DE RESPEITO — 6 min

**Tom:** Síntese pelo aluno, LGPD como ato, fechamento do arco S11, ponte curta para S12.

"Diz na sua cabeça o que você fez hoje.

Você conferiu quatro itens — lacre, pureza, sobra, bula. Pediu um laudo e leu como lê um exame. Escreveu a bula pro colega. Carimbou a versão 1.0. E assinou a liberação. Sem ler uma linha de código.

---

E aqui a privacidade dá o passo final do curso.

Durante semanas eu disse: dado de paciente não sai, tudo roda local. Na aula passada você viu isso virar design — a `data/` ficou de fora da caixa de propósito. Hoje você fez algo a mais, e é o que separa intenção de garantia: você CONFERIU.

A auditoria de entrega É um ato de privacidade. Não basta desenhar privado; antes de soltar no mundo, você PROVA que está privado. Desenhar certo foi a aula passada. Conferir que está certo, hoje, é o que te deixa entregar de cabeça erguida.

---

E com isso, o seu ClinMd-Tribe está pronto. De verdade.

Polido por fora, empacotado numa caixa, e liberado por um controle de qualidade — você. O arco de construir esse produto fecha aqui.

O que vem agora não é mais construir. São os hábitos de quem já entrega: como guardar as suas chaves, como manter a casa arrumada por dentro, como trabalhar com o seu time de agentes. As boas práticas que separam quem fez um app de quem virou, de fato, alguém que entrega software com responsabilidade.

Você fechou o produto. Na próxima, a gente cuida das chaves. Até lá."

---

**FIM DO ROTEIRO**

---

> **NOTAS DE PRODUÇÃO (não falar — operacional):**
>
> - **Fronteira com a aula_40 (CRÍTICA):** esta aula menciona "token/segredo/chave" SOMENTE como (a) item LACRE da auditoria e (b) gancho da Seção 6. **PROIBIDO aqui:** mostrar `.env`, mostrar `sk-ant-...`/qualquer string de chave, mostrar `git log`/histórico cru, explicar variável de ambiente ou `python-dotenv`. O conceito de segredo e o tratamento (reescrever histórico, rotacionar chave) é 100% da aula_40 (S12.01). Aqui é gancho, não conteúdo.
> - **Verdade técnica do app (calibra o LACRE):** o ClinMd-Tribe é 100% offline e NÃO usa token de API em runtime → o veredito honesto e esperado do LACRE é "limpo". Isso é força pedagógica (ensina o HÁBITO da conferência com resultado positivo), não fraqueza. **NÃO inventar** um token falso só para ter achado dramático — o drama vem do gesto de conferir. Gravar a fala pronta nos dois cenários (achou / não achou) — se a conta-piloto tiver um token real no histórico (de algum teste antigo), o cenário "ATENÇÃO GRAVE → gancho aula_40" fica ainda mais forte.
> - **`data/` já excluída (aula_38):** o PUREZA confirma, não refaz.
> - **Gate de tamanho (SOBRA):** reusa o da aula_38 (.exe > ~300 MB = peça pesada vazou). Mostrar o Claude reportando o tamanho real.
> - **A bula:** gerar `LEIA-ME.txt` (não `.md` — o colega zero-TI abre `.txt` com dois cliques no Bloco de Notas). Máx. 1 página. Mostrar o texto renderizado em português — é o único "documento" que o aluno lê, e é prosa, não código.
> - **Versão v1.0:** simples — `git tag v1.0` (o Claude cria) + `git push origin v1.0` (o aluno cola). GitHub Release fica como menção (anexar o .exe por link), não passo obrigatório. Só carimbar DEPOIS do laudo "liberado".
> - **Armadilha bash:** os únicos comandos são `explorer dist` e `git push origin v1.0`. Zero `uv run python -c`.
> - **Tom de fechamento:** última do polimento (arco S11 fecha), mas NÃO é a última do curso — vêm S12.01-03. Fechar o PRODUTO com peso; a ponte da Seção 7 deixa claro que o curso continua em "boas práticas". Não dizer "fim do curso".
> - **Callback aula_31 (time-out):** a Seção 2 reusa o checklist OMS que o aluno já construiu — referenciar como algo que ele JÁ fez (reduz carga).
> - **Clímax de fechamento:** o ápice (Seção 5) é o gesto de liberar/carimbar, não um artefato novo. Segurar o respiro na "assinatura". Frame-síntese: a pasta com `.exe` + `LEIA-ME.txt` lado a lado.
