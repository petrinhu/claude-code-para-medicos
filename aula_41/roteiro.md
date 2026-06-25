# Aula 41 — A Ronda: Não Deixe a Casa Virar Bagunça

**Formato:** Gravada no OBS Studio, editada no Kdenlive
**Duração:** ~55 min
**Tom:** Segunda aula dos hábitos de quem entrega. Sobre MANUTENÇÃO, não construção. A casa que você montou não fica arrumada sozinha — e hoje você aprende a ronda que impede a bagunça. Clínico, prático, com o alívio no fim.
**Módulo:** S12.02 — Arquitetura modular: evitando o monolito (2ª aula de Boas Práticas)

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] App-piloto com as quatro calculadoras modulares no Domínio, uma por arquivo (MELD, CHA2DS2-VASc, PHQ-9, GAD-7), em clinmd_tribe/src/domain/, porque toda a ronda (Seções 5 e 6) depende disso.
- [ ] Trabalho salvo e em dia (nada pendente para commitar): o Prompt 0 pergunta "o meu trabalho está salvo e em dia?".

**Confira antes de gravar:**

- [ ] Testes verdes ANTES de gravar: a partir da pasta clinmd_tribe/, rode "uv run --with pytest --no-project pytest -q" e confirme tudo verde (referência: 26 testes passando). É a rede de segurança que prova a arrumação da Seção 6 não quebrou nada.
- [ ] Casa limpa para o laudo da Seção 5: as camadas apresentação, aplicação e infraestrutura não têm regra clínica dentro (estão sem lógica de cálculo), então a ronda volta "casa arrumada" de verdade. Confira fora de gravação antes de gravar a fala "todo verde".
- [ ] Demo do clímax MELD pronta: mudar o piso de creatinina no arquivo do MELD toca 1 arquivo só, e o pytest continua verde. Ensaie fora de gravação e reverta a mudança antes de gravar, para a fala "Toquei um arquivo. O do MELD, no Domínio. Mais nada." ser literal.
- [ ] (Opcional) Se for demonstrar uma "sala virando depósito", cole temporariamente uma regra clínica num arquivo de apresentação fora de gravação, grave a fala "achou um amarelo", e reverta logo depois.

**Navegador:** nenhum site é necessário nesta aula.

---

## SEÇÃO 1: ABERTURA — A SALA QUE VIROU DEPÓSITO — 5 min

**Tom:** Pega a bola da aula_40 e abre com uma imagem clínica visceral. Zero código.

**[Aviso rápido dos óculos, antes de mergulhar]**

"Pequeno ritual de sempre antes da ronda: ponha os óculos de perto. A gente vai vistoriar a casa do app, e numa boa vistoria você quer enxergar até o canto do armário. Letrinha de terminal não perdoa quem esquece os óculos no bolso do jaleco.

---

"Na aula passada você guardou a chave no cômodo certo, fora do código. E eu te fiz uma promessa: que hoje a gente arruma a casa inteira.

Só que tem um detalhe que ninguém te conta. A casa não fica arrumada sozinha.

---

Pensa numa enfermaria no dia em que ela abre. Tudo no lugar: o carro de medicação aqui, o material de curativo ali, os prontuários na baia. Perfeita.

Aí entra a vida real. A correria. Alguém deixa a caixa de luvas em cima do carro de medicação — 'só por hoje'. Depois um soro. Depois o foco de luz que quebrou e 'vai pro conserto qualquer hora'. Seis meses de plantão depois, pra você pegar uma ampola, precisa afastar três caixas que não deviam estar ali. E um dia — você já viu isso — alguém pega o frasco errado, porque dois que nunca deviam estar lado a lado estavam.

Repara: ninguém decidiu bagunçar. A bagunça se acumulou. Sozinha.

---

O seu app sofre exatamente da mesma doença. Você montou ele organizado, em quatro cômodos, lá na aula das camadas. Mas a cada coisa nova que entra na pressa, um pedaço vaza pro cômodo errado. E se ninguém faz a ronda, seis meses depois você tem um amontoado onde mexer numa coisa quebra outra do outro lado — sem você entender por quê.

Isso tem nome: monolito. E hoje você aprende a ronda que pega ele cedo, e o gesto que arruma antes de virar caos.

E como sempre: você não vai ler uma linha de código. Vai pedir a ronda, ler o laudo, e mandar arrumar.

Uma frase pra levar a aula inteira: construir a casa foi uma aula. Manter a casa arrumada é um hábito. Hoje você aprende a ronda."

---

## SEÇÃO 2: A CASA QUE VOCÊ JÁ MONTOU — 5 min

**Tom:** Recuperação ativa rápida. Reativa a aula_15 SEM reensinar. Marca a fronteira com honestidade.

"Antes de seguir, uma coisa importante: eu NÃO vou reensinar arquitetura hoje. Você já montou a casa. Lá na aula das quatro camadas, com a analogia do plantão. Então vamos só aquecer a memória — três perguntas relâmpago. Responde na sua cabeça antes de eu dizer.

---

**Primeira:** na casa que você montou, a regra clínica pura — o cálculo de um escore, o ponto de corte — mora em qual cômodo?

[pausa]

No Domínio. O cômodo do Médico. A regra pura, que não sabe se existe tela ou banco de dados.

---

**Segunda:** monolito, na palavra do dia a dia, é o quê?

[pausa]

Tudo amontoado numa sala só. O consultório onde o mesmo médico atende, receita, cobra e arquiva — funciona com três pacientes, vira caos com trezentos.

E olha: lá na aula das camadas eu te disse que, pra um script rápido de uso próprio, amontoar até serve. É verdade. O problema não é o amontoado em si, é o amontoado num app que cresce e que você quer manter, como o seu. Aí ele cobra caro.

---

**Terceira:** quem decide a cor de um botão na tela sabe calcular o CHA2DS2-VASc?

[pausa]

Não. São cômodos diferentes. A recepção não faz diagnóstico.

---

Pronto. Memória aquecida. Repara no que essas três respostas têm em comum: elas descrevem uma casa BEM montada. Uma foto, parada, de tudo no lugar.

Hoje a gente sai da foto e entra no filme. Porque a pergunta de hoje não é 'como montar a casa'. É: como ela NÃO vira bagunça com o tempo? Essa é a parte que ninguém te ensina."

---

## SEÇÃO 3: O CHEIRO DA BAGUNÇA — 8 min

**Tom:** Didático, nomeia os sintomas como num diagnóstico. Analogia do prontuário-paredão. Zero código.

"Toda doença tem quadro clínico. O monolito também. São três sinais — e você reconhece os três sem ver uma linha de código, porque são coisas que você SENTE.

---

**Sinal um: pra mudar uma coisa, você toca vários lugares.**

Imagina o prontuário-paredão. Aquele onde anamnese, hipótese, conduta e prescrição estão tudo no mesmo parágrafo corrido, sem cabeçalho. Funciona? O plantonista escreveu, está lá. Mas quando você precisa mudar SÓ a conduta, você relê o parágrafo inteiro e arrisca editar no lugar errado — e a prescrição sai contaminada com dado da anamnese.

Agora o mesmo prontuário com seções carimbadas: Anamnese, Hipótese, Conduta, Prescrição. Muda a conduta? Você vai direto na seção Conduta. O resto não te atrapalha, e você não atrapalha o resto.

A casa modular é o prontuário carimbado. O monolito é o paredão de texto. Quando você precisa de um lugar e toca em cinco, é o cheiro do paredão.

---

**Sinal dois: a mesma regra aparece espalhada, copiada.**

A mesma dose rabiscada em três fichas diferentes. No dia em que a diretriz muda a dose, você tem que achar as três — e se esquecer uma, fica uma ficha mentindo. No código é igual: a mesma regra de um escore escrita em dois lugares. Mude um, esqueça o outro, e o app passa a dar duas respostas diferentes pro mesmo paciente.

Guarda essa, porque é o coração do perigo de hoje: regra espalhada é o mesmo paciente recebendo dois resultados divergentes, porque alguém atualizou metade.

---

**Sinal três: você mexe aqui e quebra ali.**

Você troca a cor de um botão e, sem entender por quê, um cálculo para de funcionar. Isso é sinal de que duas coisas que deviam viver em cômodos separados estão grudadas. Mexeu numa, a outra caiu junto.

---

Um aviso honesto, pra você não sair com a régua errada na mão. Arquivo grande, por si só, NÃO é doença. Um arquivo grande com UMA responsabilidade clara pode estar perfeitamente saudável. Tamanho é só a febre — o sinal que faz você ir investigar. O diagnóstico não é 'quantas linhas', é 'quantas responsabilidades diferentes estão amontoadas aqui, e quantos motivos esse arquivo tem pra mudar'. Febre alta pede exame; não é o exame."

---

## SEÇÃO 4: VOCÊ DECIDE — DIAGNÓSTICO DO CÔMODO — 8 min

**Tom:** Jogo de classificação, estilo aula_40. Preditivo: o aluno decide antes da revelação. Tudo em prosa, zero código.

"Agora a parte que mais ensina. Cinco situações. Pra cada uma, você decide: CASA ARRUMADA, ou SALA VIRANDO DEPÓSITO? E se for depósito, o que está fora do lugar? Decide antes de eu revelar.

---

**Situação um:** pra mudar o ponto de corte do PHQ-9, você toca um lugar só, e o app inteiro passa a usar o corte novo.

[pausa]

CASA ARRUMADA. Uma verdade, um lugar. A regra mora num cômodo só, e todo mundo vai lá perguntar.

---

**Situação dois:** a regra do GAD-7 está escrita um pouco na tela, um pouco junto do código que salva no disco.

[pausa]

DEPÓSITO. A regra clínica vazou pra cômodos que não são dela — a tela e o arquivo. O Médico deixou bilhete de conduta colado na recepção e na farmácia.

---

**Situação três:** você mudou a cor de um botão e, sem querer, o cálculo de um escore parou de funcionar.

[pausa]

DEPÓSITO, e dos graves. Tela e regra clínica estão grudadas. É o 'mexo aqui, quebra ali' na veia.

---

**Situação quatro:** o cômodo que guarda os arquivos no disco também decide se o paciente tem depressão moderada.

[pausa]

DEPÓSITO. O Laboratório está fazendo trabalho do Médico. Quem só era pra arquivar está dando diagnóstico.

---

**Situação cinco — essa é pegadinha, presta atenção:** você adicionou o PHQ-9 do lado do CHA2DS2-VASc. Cada um ganhou seu formulário na tela, sua regra no Domínio, e os dois salvam pelo mesmo cômodo de arquivos.

[pausa]

CASA ARRUMADA. E se isso te soa familiar, é porque lá na aula das camadas você já classificou esse caso: feature grande toca tudo, e tá tudo bem. Hoje a gente olha pro mesmo caso com outra pergunta — não 'onde mexo', mas 'isso é bagunça?'. E aqui mora a sutileza mais importante da aula: uma feature grande tocou VÁRIOS cômodos — e isso NÃO é bagunça. É cada cômodo fazendo a parte dele. Espalhar a MESMA regra é doença; uma coisa nova usar vários cômodos, cada um no seu papel, é saúde.

Não saia daqui paranoico achando que 'tocar vários lugares é sempre ruim'. O ruim é a mesma verdade picada em pedaços. O bom é cada cômodo cuidando do que é dele.

---

E a saída honesta, igual à das outras aulas: não soube diagnosticar de cabeça? Ótimo, é normal. O gesto certo não é adivinhar — é PEDIR a ronda ao Claude. Saber pedir a vistoria é o skill. Ter o diagnóstico decorado, não. É exatamente isso que a gente vai fazer agora."

---

## SEÇÃO 5: A RONDA — O LAUDO DE ORGANIZAÇÃO — 11 min

**Tom:** Mãos à obra. O gesto 1. O aluno pede o laudo e lê. Nenhum arquivo é aberto.

"Hora da ronda de verdade. Primeiro, o terreno — igual a toda aula. Cola:"

[TELA: digitar o Prompt 0 no Claude Code]

```
Você é meu par de programação e, hoje, o meu inspetor de organização. A aula de hoje é sobre
um HÁBITO de manutenção: manter o app organizado por dentro conforme ele cresce, pra ele nunca
virar uma bagunça onde mexer numa coisa quebra outra. Não vamos mudar o que o app faz.

Confirme em português, em uma frase cada: (1) o meu trabalho está salvo e em dia? (2) você
entendeu que hoje é sobre organização interna, não sobre adicionar funcionalidade?

Regra valendo para a aula INTEIRA: explique tudo em português de leigo, em forma de LAUDO.
NUNCA me mostre código, função, nem o conteúdo de nenhum arquivo por dentro. Quando precisar
falar de organização, fale de CÔMODOS e do que mora em cada um — não de classes e arquivos.
```

"Repara na última regra: hoje a gente fala de cômodos, não de código. O Claude é o inspetor; eu só leio o laudo.

---

Agora, a planta baixa da casa. Isso é permitido — é o mapa dos cômodos, não o que tem dentro de cada um. Cola:"

[TELA: digitar o Prompt 1 — a planta da casa]

```
Me mostre a PLANTA da casa do ClinMd-Tribe: só os nomes dos cômodos (as pastas das quatro
camadas — apresentação, aplicação, domínio, infraestrutura) e, em UMA frase por cômodo, o que
mora ali.

NÃO abra nenhum arquivo, NÃO me mostre o conteúdo de nada. Só a planta e a função de cada
cômodo, em português.
```

"Isso é o limite exato do que você vê: a planta da casa, nunca os móveis por dentro. Como a planta baixa de uma reforma — você vê onde é a cozinha, não o que tem dentro das gavetas.

---

E agora o coração da aula. A ronda. O laudo de organização. Cola:"

[TELA: digitar o Prompt 2 — a ronda]

```
Agora faça uma RONDA de organização no projeto e me devolva um LAUDO em português, igual a um
exame com resultado em cada linha: OK (verde), ATENÇÃO (amarelo) ou PARE (vermelho). Sem me
mostrar código, só o laudo.

  1. CADA REGRA NO SEU CÔMODO — cada regra clínica (PHQ-9, GAD-7, CHA2DS2-VASc, MELD) mora num
     cômodo só, o do Domínio? Ou alguma está espalhada por mais de um lugar?
  2. CÔMODO FAZENDO TRABALHO ALHEIO — alguma regra clínica está escrita DENTRO de um arquivo de
     tela (apresentação) ou de orquestração (aplicação), em vez de morar no Domínio?
  3. SALA VIRANDO DEPÓSITO — algum cômodo cresceu demais e acumulou funções que deviam estar
     separadas? Se sim, qual, e o que está amontoado ali.
  4. QUANTOS LUGARES EU TOCO — se eu precisar mudar a regra de um escore hoje, em quantos lugares
     eu mexo? (Um lugar = saudável. Vários = alerta.)

Para cada linha, diga em uma frase por que está OK ou por que é risco, em linguagem de leigo.
Veredito final de uma linha: "casa arrumada" ou "tem sala virando depósito".
```

"O laudo volta. E você lê ele como leu o hemograma das outras aulas: resultado na esquerda, frase do lado.

Repara no item quatro — esse é o número que mede a saúde da casa, igual a pressão mede o coração. 'Pra mudar a regra do MELD, há um lugar a tocar.' Um. Esse 'um' é a casa arrumada falando. Se viesse 'há quatro lugares', era o depósito te avisando.

Se o laudo vier todo verde, ótimo — sua casa está arrumada, e você acabou de fazer a primeira ronda da sua vida. Se vier um amarelo ou vermelho, melhor ainda pra aprender: é o que a gente vai arrumar agora."

---

## SEÇÃO 6: A ARRUMAÇÃO — UMA SÓ VERDADE, UM SÓ LUGAR — 11 min

**Tom:** O clímax. O aluno SENTE a diferença pelo comportamento, não pelo código. Depois arruma e prova. O alívio.

"Esta parte tem quatro colagens, nesta ordem: primeiro você SENTE a diferença (um teste e uma hipótese), depois ARRUMA, depois PROVA que não quebrou. Vamos.

Antes de arrumar nada, deixa eu te mostrar por que isso importa — com um teste que você sente na barriga. Cola:"

[TELA: digitar o teste da mudança — casa modular]

```
Quero sentir, na prática, o que a organização me dá. Faça uma mudança pequena de regra clínica,
de verdade: no MELD, mude um parâmetro qualquer da regra (por exemplo o piso de creatinina
considerado, de 1,0 para 0,8 — é só pra demonstrar o gesto, não é recomendação clínica).

Faça a mudança e me diga, em prosa, SÓ uma coisa: QUANTOS arquivos você precisou tocar, e o
nome deles. Não me mostre o código — só o número e os nomes.
```

"E olha a resposta numa casa arrumada: 'Toquei um arquivo. O do MELD, no Domínio. Mais nada.'

Um. A regra estava isolada no cômodo dela, então a mudança foi cirúrgica. Você mudou a diretriz e não chegou perto da tela, nem do que salva no disco.

---

Agora o contraste — e presta atenção que isto é hipótese, não é o seu app. Pergunta pro Claude como SERIA num monolito:"

[TELA: digitar o contraste — o monólito imaginado]

```
Agora me explique, só em prosa e como hipótese: SE essa mesma regra do MELD estivesse escrita
dentro da tela, misturada com o código dos botões e da validação dos campos — como numa versão
toda amontoada do app — o que seria diferente na hora de fazer essa mesma mudança? Em quantos
lugares eu teria que mexer, e que risco eu correria? Sem código, só me descreva o cenário.
```

"O Claude te descreve o pesadelo: você teria que caçar a regra no meio do código da tela, com risco de quebrar a tela ao mexer na regra, sem conseguir testar a regra sozinha, e com chance de deixar uma cópia velha pra trás — o tal do mesmo paciente, dois resultados.

Sentiu? Casa arrumada: um lugar, uma verdade, mudança leve. Monolito: caça ao tesouro, e o risco de o app mentir. Essa é a aula inteira numa imagem.

---

Agora, SE a sua ronda lá atrás achou uma sala virando depósito, é hora de arrumar. O gesto 2. Cola:"

[TELA: digitar o Prompt 3 — a arrumação]

```
A ronda apontou que [diga aqui o que o laudo achou — por exemplo: "uma regra clínica está
escrita dentro de um arquivo de tela"]. Arrume isso: devolva cada coisa ao cômodo certo, do
jeito da nossa arquitetura em camadas.

Regra de segurança, inegociável: arrume a organização por dentro, mas o app tem que se comportar
EXATAMENTE igual depois — abrir igual, calcular o mesmo número em todo lugar. Ao terminar, RODE
os testes (pytest) e me diga se continuam todos verdes.

Me explique em português o que você moveu e de onde pra onde, em linguagem de cômodos
("tirei a regra do PHQ-9 de dentro da tela e devolvi pro cômodo do Domínio"). NÃO me mostre o
código que mudou, nem o antes e depois — só o resumo do que foi movido e o resultado dos testes.
```

"E aqui está a parte que separa o amador do profissional. A arrumação mexe no código por dentro. Como você, que não lê código, tem CERTEZA de que ela não quebrou nada?

Os testes. Aqueles guardiões que você construiu lá nas aulas de teste. Eles estavam verdes antes. Se continuarem verdes depois, a arrumação preservou o comportamento: as regras que têm guardião continuam calculando igualzinho, e essas são justamente as que importam. Se um ficar vermelho, a arrumação quebrou algo, e o guardião pegou na hora.

E olha a conexão bonita: lembra dos guardiões que você construiu lá atrás? Construir eles ficou simples porque a regra clínica estava isolada num cômodo só. Testar uma regra limpa é fácil; testar uma regra grudada na tela seria uma luta. Pois é. A organização de hoje é a mesma que deixou os testes fáceis. Uma coisa sustenta a outra.

---

Pra fechar o ciclo, a re-vistoria. Você examina, trata, e reexamina — como na clínica. Cola:"

[TELA: digitar o Prompt 4 — a prova]

```
Agora repita a ronda, depois da arrumação, e me dê a prova em uma frase por linha, sem código:
  1. O app calcula igual ao de antes? (mesma entrada, mesmo resultado, em todo lugar)
  2. Os testes continuam todos verdes?
  3. Cada regra clínica agora mora num cômodo só?

Veredito final de uma linha: "casa arrumada, e nada quebrou".
```

"Esse é o fecho. Arrumou — e não quebrou. Provado pelo comportamento, não pela minha palavra. Examinar, tratar, reexaminar. O ritmo que você já tem no sangue."

---

## SEÇÃO 7: A REGRA DA RONDA — QUANDO ARRUMAR, E QUANDO NÃO — 5 min

**Tom:** Honesto, desmistificador. Mata três ilusões perigosas. LGPD leve no fim.

"Três honestidades pra você não sair com uma régua errada na mão.

---

Primeira, e a mais perigosa de todas: arrumar a organização do app não corrige um erro de cálculo. Faxina não é remédio. Se o seu MELD está calculando errado, arrumar o cômodo só vai deixar o erro mais bem-guardado, não some com ele. Bug se conserta de outro jeito: você muda a regra e cria um teste que prova que agora está certo, do jeito que você aprendeu nas aulas de teste. Arrumar a casa facilita achar o remédio depois. Não é o remédio.

---

Segunda: arrumar demais é tão ruim quanto não arrumar. Se você sair criando um cômodo separado pra cada coisinha 'pro caso de um dia precisar', você cria uma casa com cinquenta portas pra atravessar pra fazer qualquer coisa. Pra um app de um médico só, isso é desperdício e fragiliza — mais peças, mais coisa pra quebrar.

A regra de bolso, decora essa: separe quando DÓI, não por precaução. O sinal de separar é uma dor que você sentiu — uma mudança que devia ser fácil ficou difícil, ou a mesma regra apareceu copiada. Antes da dor, deixa junto. Depois da dor, separa. Modularidade é remédio pra uma dor real, não vitamina em dose alta.

---

Terceira: esta aula não te fez arquiteto. E está ótimo assim. Você aprendeu a fazer a RONDA e a pedir a arrumação — não a redesenhar o prédio. É a diferença entre o médico que sabe pedir e ler um eco, e o especialista que faz o laudo do eco. Você é o primeiro, e isso já é muita coisa.

---

E o eixo do curso, a privacidade, ganha uma camada hoje também. Casa arrumada é casa segura. Quando cada coisa tem o seu cômodo, fica muito mais fácil garantir que dado de paciente não vaze de um lugar pro outro sem você ver. Organização não é só estética — é controle. E controle é o que protege quem confia na gente."

---

## SEÇÃO 8: ENCERRAMENTO — VOCÊ NÃO ESTÁ SOZINHO NA RONDA — 3 min

**Tom:** Síntese pelo aluno + gancho para a última aula (a constelação de agents).

"Diz na sua cabeça o que você fez hoje.

Você entendeu que organização se degrada com o tempo — a enfermaria vira depósito se ninguém vigia. Aprendeu a reconhecer o cheiro do monolito: toco vários lugares, regra espalhada, mexo aqui e quebra ali. Fez a ronda e leu o laudo. Mandou arrumar, e provou com os testes que nada quebrou. Tudo sem ler uma linha de código.

---

Mas repara numa coisa. Hoje você fez a ronda sozinho, com o Claude do seu lado. Você bancou o chefe de plantão que vistoria a enfermaria e decide o que arrumar.

E todo bom chefe de plantão sabe uma verdade: as decisões grandes não se tomam sozinho, no susto. Quando a casa precisa de uma reforma de verdade — não uma arrumação, uma reforma — você não decide na adrenalina. Você reúne o corpo clínico.

E acontece que você tem um corpo clínico inteiro à disposição, que a gente só apresentou de relance lá atrás. Um diretor-geral, um chefe de tecnologia, um chefe de segurança — cada um com a sua especialidade.

Na última aula do curso, eu te apresento o time inteiro. E te mostro o hábito que separa quem programa de quem entrega: antes de uma decisão grande, você discute com o seu time. Você nunca mais vai estar sozinho na ronda.

Hoje você arrumou a casa. Na próxima, você conhece quem te ajuda a cuidar dela. Até lá."

---

**FIM DO ROTEIRO**

---

> **NOTAS DE PRODUÇÃO (não falar — operacional):**
>
> - **Anti-padrão PROIBIDO (CRÍTICO):** NUNCA mostrar na tela conteúdo de arquivo `.py`, nenhum `class`/`def`/`import`, nenhum trecho de código, nenhum `diff`/antes-e-depois colorido. O aluno vê SÓ: (a) a planta de pastas (Prompt 1, nomes de cômodos), (b) laudos em português, (c) prosa do Claude. Proibido `cat`/`head`/`less`/`bat`/`grep` em arquivo de código durante a aula. Se precisar do conteúdo, o Claude lê internamente e descreve — nunca despeja.
> - **PARADOXO zero-código resolvido por LAUDO:** modularidade aqui NÃO é propriedade do código que o aluno lê — é (a) o número de lugares que ele toca pra uma mudança (Prompt 2 item 4 / teste do MELD) e (b) "uma só verdade, um só lugar". Ambos 100% observáveis em prosa. O skill ensinado é "pedir a vistoria e ler o laudo", não "ver código".
> - **PRÉ-REQUISITO DE GRAVAÇÃO — RESOLVIDO (Caminho A executado em 2026-06-10):** o app-piloto real foi construído em `clinmd_tribe/`. O `domain/` tem 4 calculadoras MODULARES, uma por arquivo (`meld.py`, `cha2ds2vasc.py`, `phq9.py`, `gad7.py`), e `tests/` tem 26 testes pytest VERDES (casos do CHA2DS2-VASc batem com a aula_33: 3/0/7/2). As demos das Seções 5-6 são GENUÍNAS:
>   - **Seção 5 (ronda):** o Prompt 2 lista PHQ-9, GAD-7, CHA2DS2-VASc, MELD — todos existem no `domain/`, cada um num arquivo só. O laudo dá "casa arrumada" de verdade (presentation/application/infrastructure ainda vazios = nenhuma lógica clínica vazada).
>   - **Seção 6 (clímax MELD):** mudar o piso de creatinina é alterar a constante `PISO_CREATININA` em `meld.py` = **toca 1 arquivo** de verdade. A fala "Toquei um arquivo. O do MELD, no Domínio. Mais nada." é literal. Rodar `pytest` continua verde (a mudança é localizada). Comando de teste que NÃO exige flet (evita problema de wheel): a partir de `clinmd_tribe/`, `uv run --with pytest --no-project pytest -q`. No ambiente do aluno (Python 3.11-3.13) `uv run --extra dev pytest` também serve.
>   - **Seção 5, cenário do laudo:** como a casa-piloto está limpa, o laudo virá verde. Gravar também a fala alternativa "achou um amarelo" só se o instrutor quiser demonstrar uma sala-depósito (basta, fora de gravação, colar temporariamente uma regra clínica num arquivo de presentation; reverter depois). Opcional.
> - **Honestidade sobre o que o Claude faz na auditoria:** é análise heurística/qualitativa de revisor sênior, NÃO medição objetiva de laboratório. Não vender o laudo como "número científico de modularidade". É segunda opinião fundamentada, com a falibilidade que isso tem.
> - **Tamanho ≠ diagnóstico (armadilha da métrica):** NÃO ensinar "conte linhas". Linha é febre (sinal barato e impreciso); responsabilidade é o diagnóstico. Evitar `wc -l` ao vivo como "prova" — se quiser o número, pedir no laudo do Claude ("o maior arquivo tem ~X linhas"), não fazer o aluno rodar shell.
> - **A rede de segurança é TESTE, não modularidade:** deixar explícito que refatoração PODE introduzir bug; o que prova que não quebrou são os testes verdes (aula_33/34) + app abrindo igual + o CI (aula_35/36) no push. Modularidade torna a mudança barata/localizada; o teste a torna segura. Duas coisas diferentes.
> - **Ponte de arco (S03 → S09):** a fala da Seção 6 ("você só conseguiu construir os guardiões porque a regra estava isolada") fecha o arco da arquitetura (aula_15) com os testes (aula_33). É verdadeira e forte — manter.
> - **Clímax usa MELD, não CHA2DS2-VASc:** o CHA2DS2-VASc foi o "paciente-controle" das aulas de teste (aula_33). MELD (fórmula contínua, determinística, sem RAG no caminho) evita confusão e mostra que o hábito generaliza. NÃO amarrar o clímax ao RAG (não-determinístico + débito do threshold em aberto).
> - **Armadilha bash:** zero `uv run python -c "..."` (f-string expande no bash). O Claude executa git/arquivo/pytest internamente e relata em prosa. O aluno só cola prompts.
> - **Anti-repetição da aula_15 (risco #1):** dizer em voz alta na Seção 2 "não vou reensinar arquitetura". aula_15 = montar (foto); aula_41 = manter (filme/entropia). Nunca reapresentar as 4 camadas como novidade — só reativar.
> - **Gancho de saída para aula_42:** "chefe de plantão decide sozinho no susto" → NÃO; reúne o corpo clínico (constelação de agents: Celso/CEO, Caetano/CTO, Narciso/CISO...). A decisão de refatorar é trade-off (custo × benefício) = território do Caetano/CTO. Prompt-ponte que a aula_42 desenvolve: "@caetano-cto, a ronda apontou X — vale refatorar agora ou registro como débito técnico?".
