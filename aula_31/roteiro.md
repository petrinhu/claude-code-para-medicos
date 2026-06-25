# Aula 31 — Cirurgia Segura: o Checklist que Não Esquece

**Formato:** Gravada no OBS Studio, editada no Kdenlive
**Duração:** ~55 min
**Tom:** Cirurgião construindo, dentro do app, o ritual de segurança que ele já vive na sala
**Módulo:** S08 — Checklists de Segurança (condensa S08.01 + S08.02)

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Já preparado em `resources/` (é só usar):**

- [ ] `resources/checklist_oms_19_itens.md` : folha de conferência com os 19 itens da OMS nas 3 fases (7 / 7 / 5), idênticos aos do Prompt 1. Use para conferir na Seção 5 que o app semeou a contagem certa e para localizar o item 10 (antibiótico), usado no clímax da Seção 7. Só o instrutor vê; não aparece na aula.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] O ClinMd-Tribe nas 4 camadas (domain, application, infrastructure, presentation) e o banco local `data/clinmd.db` já em uso pelas calculadoras das aulas anteriores. O checklist desta aula é semeado nesse mesmo banco.
- [ ] O app abrindo com `uv run flet run main.py`.

**Confira antes de gravar:**

- [ ] Tenha os dois prompts à mão (Prompt 1 do motor na Seção 4, Prompt 2 da tela na Seção 6) para colar de uma vez.
- [ ] Antes de gravar a Seção 4, garanta que o checklist ainda NÃO foi semeado (ou que a semeadura é idempotente), para o aluno ver os 19 itens nascerem do zero. Se já rodou na pré-gravação, parta de um `data/clinmd.db` sem o checklist semeado.
- [ ] Na Seção 5, confirme que a contagem responde 7 / 7 / 5 (total 19), batendo com `resources/checklist_oms_19_itens.md`. Comando forense opcional: `sqlite3 data/clinmd.db "SELECT fase, COUNT(*) FROM item_checklist GROUP BY fase;"`.
- [ ] Na pré-gravação, ensaie os três experimentos do clímax (Seção 7) com o item 10: marcar gera horário; fechar e reabrir mantém o horário; tocar de novo NÃO altera o horário. Os três devem se comportar como descrito antes de gravar.

**Navegador:** o app Flet abre no navegador local (`uv run flet run main.py`); nenhum site externo é necessário.

---

## SEÇÃO 1: ABERTURA — TRÊS PAUSAS QUE SALVAM VIDAS — 4 min

**Tom:** Grave, quase ritualístico. O cirurgião sente o peso da pausa cirúrgica. Sem humor aqui — o humor entra depois.

**[Aviso rápido dos óculos, antes de mergulhar]**

"Um pedido antes de começar, e depois fico sério: ponha os óculos de perto. A gente vai conferir item por item de um checklist no terminal, e errar a leitura ali é o tipo de coisa que esse checklist existe justamente pra evitar. Foco ajustado? Então vamos com calma."

"Antes da indução.

Antes da incisão.

Antes de sair da sala.

---

Três momentos. Três pausas. Três vezes em que a sala inteira para — e confere.

---

Você conhece esse ritual. A enfermeira lê em voz alta. A equipe responde. Ninguém avança até o último item estar confirmado.

O checklist cirúrgico da OMS não foi inventado por burocrata. Foi inventado porque cirurgião erra lado. Porque compressa fica dentro. Porque o antibiótico não entrou na hora certa. E porque uma lista lida em voz alta, três vezes, reduz isso de forma mensurável.

---

Hoje você vai construir esse ritual dentro do ClinMd-Tribe.

Não um checklist genérico. O checklist da OMS. Dezenove itens. As três fases que você já conhece de cor.

---

E tem uma coisa que esse app vai fazer que o papel não faz.

Quando você marcar um item, ele vai registrar o horário. Sozinho. No instante exato.

E esse horário — você não vai conseguir mudar. Nem se quiser.

---

Por que isso importa, eu mostro no final da aula. Guarde a pergunta:

*por que um sistema impediria o próprio médico de editar um horário?*"

---

## SEÇÃO 2: O MAPA MENTAL — TRÊS PEÇAS QUE VOCÊ JÁ CONHECE — 5 min

**Tom:** Didático e tranquilo. O cirurgião monta a maquete mental ANTES de qualquer prompt. Três peças, nenhuma linha de código.

"Antes de pedir qualquer coisa ao Claude Code, deixa eu te dar o mapa. Três peças. Três ideias. Você já conhece todas elas — só não com esses nomes.

---

**Peça um: um checklist tem muitos itens.**

Pense no prontuário. Um prontuário, muitas evoluções penduradas nele. Você nunca tem uma evolução solta no ar — ela sempre pertence a um prontuário.

Aqui é igual. Um checklist — 'Cirurgia Segura OMS'. Pendurados nele, dezenove itens. Um para muitos.

Isso tem nome em TI: relação um-para-muitos. Mas você pode esquecer o nome. Lembre do prontuário e das evoluções.

---

**Peça dois: como o item sabe a que checklist pertence.**

No prontuário de papel, como uma folha solta sabe de quem ela é? Pelo número de registro carimbado nela. Toda folha carrega o registro do dono.

Cada item do nosso checklist vai carregar o número do checklist a que pertence. É um vínculo. Item sem vínculo é folha perdida no arquivo — não serve para nada.

Em TI isso se chama chave estrangeira. De novo: esqueça o nome. Lembre da folha com o registro do paciente.

---

**Peça três — e essa é a estrela da aula: o horário-testemunha.**

Quando um bebê nasce, alguém anota a hora. Onze e quarenta e dois. Essa hora vira parte do registro. E ninguém — ninguém — chega depois e 'edita' a hora do nascimento. Ela foi registrada no instante. É testemunha.

Cada item que você marcar no app vai ganhar um horário desses. Gerado pelo sistema. No segundo em que você marca. E imutável.

---

Três peças. Prontuário e evoluções. Folha com registro. Hora do nascimento.

Guarde essas três imagens. Tudo o que o app fizer hoje, você vai conseguir explicar com elas — sem olhar uma linha de código sequer."

---

## SEÇÃO 3: VOCÊ É O ARQUITETO — DUAS DECISÕES ANTES DE GERAR — 8 min

**Tom:** Colaborativo e instigante. O professor faz o cirurgião pensar como arquiteto do próprio app — decidir o comportamento ANTES de a máquina existir. Humor leve volta.

"Antes de a gente pedir o app, vamos decidir como ele deve se comportar. Porque quem decide o comportamento é você — o Claude Code só obedece.

E a melhor forma de decidir o comportamento certo é imaginar o app já pronto e se perguntar: *'o que eu QUERO que aconteça quando...?'*

Vou te fazer duas perguntas. Não são pegadinha. Não tem código nenhum para você olhar. É raciocínio clínico — o mesmo que você usa para antecipar uma intercorrência antes dela acontecer.

---

**PERGUNTA UM — a da memória.**

Imagine: você está numa cirurgia. Abre o app, marca os sete itens da fase 'antes da indução anestésica'. Tudo verde. Aí o app fecha — acabou a bateria do tablet, alguém esbarrou, sei lá.

Você reabre o app.

*O que você ESPERA encontrar? Os sete itens ainda marcados? Ou a lista zerada, como se você nunca tivesse começado?*

Pensa um segundo antes de eu responder. O que faria sentido para um registro cirúrgico?

---

Claro que você espera encontrar tudo como deixou. Um checklist cirúrgico que esquece o que você marcou quando a tela apaga não é um checklist — é uma piada de mau gosto. Seria como um prontuário que apaga a evolução toda vez que você fecha a pasta.

Então a decisão é: **o app tem que LEMBRAR.** Os itens marcados ficam gravados. Fechar e reabrir não pode apagar nada.

Esse 'lembrar mesmo desligado' tem nome — persistência. É o mesmo motivo de a gente ter usado um banco de dados local lá atrás no curso, em vez de guardar tudo só na tela. Tela esquece. Banco lembra.

---

**PERGUNTA DOIS — a do horário.**

Agora a mais importante. Imagine que você marcou o item 'antibiótico administrado' às oito e quinze. O app registrou: oito e quinze.

Meia hora depois, por qualquer razão, você toca naquele item de novo. Talvez sem querer. Talvez achando que precisa 'reconfirmar'.

*O que você acha que deve acontecer com o horário? Ele atualiza para o horário de agora — oito e quarenta e cinco? Ou ele fica congelado nos oito e quinze originais?*

Pensa como cirurgião, não como usuário de app. O que esse horário REPRESENTA?

---

Ele representa o instante real em que o antibiótico entrou. Esse instante aconteceu uma vez. Às oito e quinze. Tocar na tela de novo não faz o antibiótico entrar de novo.

E se você ainda hesita, faz a pergunta do auditor: amanhã, alguém abre esse registro. O que ele precisa ver — a hora real em que o antibiótico entrou, ou a última vez que alguém encostou na tela?

A hora real. Sempre.

Então a decisão é: **o horário é gravado UMA vez — na primeira marcação — e nunca mais muda.** É a hora do nascimento. Aconteceu uma vez, fica para sempre.

---

Olha o que a gente acabou de fazer. Sem escrever nada, sem olhar código, você acabou de especificar duas regras de comportamento do app:

Um: ele lembra mesmo desligado.

Dois: o horário da primeira marcação é definitivo.

Essas duas decisões são SUAS. Na próxima seção, a gente só vai pedir ao Claude Code que construa um app que se comporte assim. Ele escreve o código. Você já sabe o que o código tem que fazer — porque você é quem decidiu."

---

## SEÇÃO 4: PROMPT 1 — O MOTOR DO CHECKLIST — 12 min

**Tom:** Mãos à obra, ritmo de produção. O professor narra a intenção de cada parte em linguagem clínica, depois cola o prompt e deixa o Claude Code trabalhar.

"Decidido o comportamento, agora a gente pede o app. Em uma frase, o que esse prompt faz: ele constrói o esqueleto do checklist e já o entrega com os dezenove itens dentro — como uma bandeja cirúrgica que chega montada.

Vou organizar o pedido nas quatro camadas que você já conhece desde a aula quinze. Cada camada cuida do que é dela — como num centro cirúrgico, onde anestesista, instrumentador e cirurgião têm papéis que não se misturam.

---

Deixa eu narrar o que vou pedir, em português de gente, antes de colar:

O miolo — o domínio: o que é um checklist e o que é um item. Só a definição, pura.

A regra de negócio — a aplicação: listar os itens e marcar um item. E é aqui que mora a regra do horário-testemunha que você decidiu.

O arquivo — a infraestrutura: cria o banco local, já semeia os dezenove itens da OMS, e amarra cada item ao seu checklist pelo vínculo — a tal folha com o número de registro.

---

Sobre o banco em si eu vou ser breve: é o mesmo tipo de banco local que a gente já usou no curso, aquele `data/clinmd.db` que guarda tudo na sua máquina sem servidor nenhum. Já vimos, não vou re-explicar. O que importa: nada disso sai do seu computador.

---

Aqui vai o prompt. Cola inteiro no Claude Code:"

[TELA: digitar o Prompt 1 no Claude Code]

```
Você é meu par de programação. Vou construir, no app ClinMd-Tribe, um checklist
de segurança cirúrgica no padrão da OMS (WHO Surgical Safety Checklist). Gere o
código respeitando a arquitetura em 4 camadas que já usamos (domain, application,
infrastructure, presentation). NÃO escreva a tela agora — só o "motor" por trás
dela. Descrevo o que o sistema precisa fazer, em linguagem clínica:

CONCEITO
Um checklist cirúrgico tem um nome ("Checklist de Segurança Cirúrgica - OMS") e é
dividido em 3 fases, nesta ordem:
  1. "Antes da indução anestésica"
  2. "Antes da incisão da pele"
  3. "Antes do paciente sair da sala"
Cada item pertence a UMA fase, tem um texto, pode estar concluído ou não, e —
quando concluído — guarda a hora exata em que foi marcado.

CAMADA domain (regras puras, SEM banco de dados, SEM import de sqlite)
  - Dataclass ItemChecklist: id, a qual checklist pertence, a fase, o texto,
    se está concluído, e o horário de conclusão (vazio enquanto não concluído).
  - Dataclass Checklist: id e nome.
  - São apenas estruturas de dados. Nenhuma lógica de banco aqui.

CAMADA infrastructure (o "arquivo de prontuário" — onde os dados ficam guardados)
  - Banco SQLite local em data/clinmd.db, no MESMO padrão de caminho ancorado na
    raiz do projeto que já usamos (Path(__file__) subindo até a raiz). É o mesmo
    banco que já guarda os outros dados do app.
  - Crie as tabelas se ainda não existirem (migration na primeira execução).
    Nomeie as tabelas exatamente "checklist" e "item_checklist".
  - O id de cada registro é um número inteiro gerado automaticamente pelo banco
    (INTEGER PRIMARY KEY AUTOINCREMENT). Eu nunca vou digitar id à mão.
  - Cada item DEVE estar ligado ao seu checklist por uma chave estrangeira
    (FOREIGN KEY do item para o checklist). Ative a integridade do SQLite com
    PRAGMA foreign_keys = ON, executado ANTES de qualquer outra operação na
    conexão (senão o SQLite ignora a chave estrangeira silenciosamente).
  - Na criação inicial do banco, SEMEIE exatamente estes 19 itens, nas 3 fases,
    nesta ordem. Semeie só uma vez: se o checklist já existir, não duplique.

    FASE "Antes da indução anestésica":
      1. Paciente confirmou identidade, sítio cirúrgico, procedimento e consentimento
      2. Sítio cirúrgico demarcado / demarcação não se aplica
      3. Checagem de anestesia e medicação completa
      4. Oxímetro de pulso instalado e funcionando
      5. Paciente possui alergia conhecida? (equipe ciente)
      6. Via aérea difícil ou risco de aspiração avaliado, equipamento e auxílio disponíveis
      7. Risco de perda sanguínea > 500 mL (7 mL/kg em crianças): acesso e fluidos planejados

    FASE "Antes da incisão da pele":
      8. Toda a equipe se apresentou pelo nome e função
      9. Confirmados em voz alta: nome do paciente, procedimento e local da incisão
      10. Antibiótico profilático administrado nos últimos 60 minutos / não se aplica
      11. Cirurgião revisou: etapas críticas, duração e perda sanguínea prevista
      12. Anestesista revisou: preocupações específicas do paciente
      13. Equipe de enfermagem confirmou: esterilização, instrumental e equipamentos
      14. Exames de imagem essenciais estão disponíveis e expostos / não se aplica

    FASE "Antes do paciente sair da sala":
      15. Enfermagem confirmou em voz alta o nome do procedimento realizado
      16. Contagem de instrumentais, compressas e agulhas conferida e correta
      17. Peças cirúrgicas / amostras identificadas (incluindo nome do paciente)
      18. Problemas com equipamentos identificados e comunicados / não houve
      19. Equipe revisou as principais preocupações para a recuperação do paciente

CAMADA application (o serviço que a tela vai chamar)
  - Função para listar todos os itens, já agrupados/ordenados por fase.
  - Função marcar_item(id) que registra a conclusão de um item.
    REGRA CRÍTICA (imutabilidade do horário): o horário de conclusão é gerado
    AQUI, com datetime.now() do computador, e SOMENTE quando o item AINDA NÃO
    estava concluído. Se o item já estava concluído, NÃO toque no horário — ele é
    definitivo, como uma anotação de prontuário não se reescreve.
  - Guarde data e hora completas; para exibir, devolva também o horário no
    formato hora:minuto:segundo (HH:MM:SS).

REGRAS DE ARQUITETURA (valem para tudo)
  - import de sqlite3 SÓ pode aparecer na camada infrastructure. Nunca em domain,
    application ou presentation.
  - A camada domain não importa nada das outras camadas.

Ao final, me explique em 2 frases simples (sem mostrar código) como eu rodo o app
e confirme que os 19 itens foram semeados.
```

"Cola, dá enter, e deixa ele trabalhar.

---

Enquanto ele trabalha, repara numa coisa só, sem olhar o código: ele está criando arquivos em pastas diferentes. Domínio, aplicação, infraestrutura. Cada papel no seu lugar. Isso não é firula — é o que vai te deixar trocar uma peça amanhã sem quebrar o resto. Mas isso é assunto pra depois. Por agora, deixa ele cozinhar."

---

## SEÇÃO 5: VERIFICAÇÃO — A BANDEJA CHEGOU MONTADA? — 4 min

**Tom:** Alívio e confirmação. O momento "deu certo". Curto e satisfatório. Sem abrir nenhum arquivo de código.

"O Claude terminou. Vamos confirmar que deu certo — sem abrir nenhum arquivo de código. Eu não vou LER o banco. Eu vou PERGUNTAR a ele, em português:"

[TELA: digitar no Claude Code]

```
Sem me mostrar código: conte quantos itens existem no banco em data/clinmd.db,
separados por fase, e me diga o total. Liste só os textos dos itens de cada fase,
como uma checklist impressa.
```

"E o Claude responde em texto limpo, como uma lista de parede de centro cirúrgico:

Antes da indução anestésica — sete itens.

Antes da incisão da pele — sete itens.

Antes do paciente sair da sala — cinco itens.

Total: dezenove.

---

Dezenove. Sete, sete e cinco. Exatamente o checklist da OMS. A bandeja chegou montada.

Olha o que você está vendo: a lista impressa, em português, igual ao quadro que fica na parede do centro cirúrgico. Você RECONHECE esses itens. Você os lê em voz alta toda semana. Eles estão dentro do app agora.

---

Se você é do tipo que só acredita vendo o dado no arquivo — e cirurgião costuma ser desse tipo — tem uma prova forense opcional. Um comando que pergunta direto ao arquivo do banco quantos itens tem em cada fase:"

[TELA: comando opcional no terminal — só se quiser ver o dado no arquivo]

```bash
sqlite3 data/clinmd.db "SELECT fase, COUNT(*) FROM item_checklist GROUP BY fase;"
```

"Sete, sete, cinco. O dado está gravado no arquivo, na sua máquina.

Mas atenção: isso aqui é só para você ver com seus próprios olhos que o dado existe. Você nunca vai precisar fazer isso para usar o app — o app já mostra tudo na tela. E é a tela que a gente constrói agora.

Porque a prova que importa de verdade não é eu te dizer que tem dezenove itens no banco. É você VER os dezenove na tela, nas três fases, e poder clicar."

---

## SEÇÃO 6: PROMPT 2 — A TELA QUE O CIRURGIÃO TOCA — 10 min

**Tom:** Produção de novo, agora com expectativa crescente — a tela é onde tudo fica visível.

"Backend pronto e conferido. Agora a cara do app — a tela que o cirurgião vai tocar.

Em uma frase: essa tela mostra os dezenove itens como caixas de marcar, agrupados nas três fases, e quando você marca uma caixa o horário aparece do lado dela.

Você já construiu várias telas neste curso. Essa segue o mesmo molde — lista, caixa de marcar, interação. O que muda é o que aparece quando você marca: um horário, gerado na hora.

---

Tem duas armadilhas clássicas de tela que eu vou pedir explicitamente ao Claude para evitar. Não em linguagem de programação — em linguagem de comportamento:

A primeira: a tela não pode mentir. Quando você marca um item, o horário tem que aparecer na mesma hora — não na próxima vez que você abrir.

A segunda: abrir a tela não pode reescrever o passado. Quando você reabre o app e ele mostra os itens que já estavam marcados de antes, isso não pode disparar um horário novo por cima do horário verdadeiro.

As duas estão escritas dentro do prompt, em português. Cola inteiro:"

[TELA: digitar o Prompt 2 no Claude Code]

```
Agora crie a TELA do checklist cirúrgico, em
presentation/telas/tela_checklist.py, no app ClinMd-Tribe. Siga o mesmo padrão
visual das outras telas do projeto e use as cores padrão do app.

O que o cirurgião precisa ver e fazer na tela:
  - Os itens aparecem como caixas de marcação (checkboxes), SEPARADOS POR FASE,
    com o título de cada fase acima do seu grupo:
      "Antes da indução anestésica", "Antes da incisão da pele",
      "Antes do paciente sair da sala".
  - Ao lado de cada item, quando ele estiver concluído, aparece o horário em que
    foi marcado, no formato hora:minuto:segundo. Enquanto não estiver marcado,
    não aparece horário.
  - Ao marcar uma caixa, o sistema registra a conclusão chamando o serviço
    marcar_item do checklist (que persiste no banco) e o horário daquele item
    aparece na tela na hora.

A tela busca os dados chamando o serviço da camada application (listar itens e
marcar_item). A tela NUNCA acessa o banco SQLite diretamente — não pode existir
import de sqlite3 neste arquivo.

DOIS COMPORTAMENTOS QUE NÃO PODEM FALHAR (previna os dois):

  COMPORTAMENTO 1 - a tela não pode "mentir".
  Depois de marcar um item e registrar o horário, atualize a tela explicitamente
  (chame page.update()) para que o horário recém-gravado apareça na mesma hora.
  Se esquecer de atualizar, o dado foi salvo no banco mas a tela continua
  mostrando o estado antigo — a tela estaria mentindo sobre o que já aconteceu.

  COMPORTAMENTO 2 - carregar a tela NÃO pode reescrever horários antigos.
  Quando a tela abre e monta os checkboxes a partir dos itens que vêm do banco,
  alguns já podem estar concluídos (de uma cirurgia anterior). O ato de
  montar/exibir esses checkboxes JÁ marcados NÃO pode disparar uma nova gravação
  de horário. Só conta como "marcar" a ação real do cirurgião clicando agora.
  O horário antigo tem que continuar exatamente o mesmo depois de reabrir a tela.

Adicione esta tela ao menu de navegação do app, com o item de menu
"Cirurgia Segura", seguindo o padrão dos outros itens de menu.
```

"Cola, enter, deixa ele construir. Quando terminar, a gente sobe o app:"

[TELA: rodar o app]

```bash
uv run flet run main.py
```

"O app abre. Você clica em 'Cirurgia Segura' no menu.

E ali está. Três blocos. Sete caixas no primeiro, sete no segundo, cinco no terceiro. Cada caixa com o texto de um item da OMS.

Repara que está tudo desmarcado. Limpo. Como uma sala preparada antes de o paciente entrar.

---

Agora a pergunta que vale a aula: o que acontece quando eu marco a primeira caixa?

Você já PREVIU lá atrás, na Seção três. Vamos ver se você estava certo. É o que vem agora — e é a parte mais importante de tudo."

---

## SEÇÃO 7: O CLÍMAX — A TESTEMUNHA QUE NÃO MENTE — 7 min

**Tom:** O ápice. Ritmo desacelera, cada ação é deliberada, quase teatral. O professor está provando uma tese. Silêncios propositais. É o momento que o aluno vai lembrar da aula inteira.

"Três experimentos. Preste atenção na tela. Cada um responde uma pergunta que você já se fez hoje.

---

**EXPERIMENTO UM — o horário nasce.**

Vou marcar o item 'Antibiótico profilático administrado nos últimos 60 minutos'.

[marca a caixa]

Olha. Eu marquei. E surgiu um horário do lado: oito, quinze, quarenta e dois.

Eu não digitei esse horário. Eu não escolhi esse horário. Não tem um campo onde eu digito a hora. Eu só marquei a caixa — e o sistema carimbou o instante exato.

Esse é o segundo em que, na vida real, o antibiótico entrou. O app testemunhou.

---

**EXPERIMENTO DOIS — o horário sobrevive à morte do app.**

Lembra a primeira pergunta da Seção três? 'Você fecha e reabre, o que espera encontrar?'

Vamos testar. Vou fechar o app. Fechar mesmo — janela fechada, programa encerrado. Como se a bateria tivesse acabado no meio da cirurgia.

[fecha o app por completo]

Morto. Não tem nada rodando.

Agora eu reabro.

[reabre com uv run flet run main.py e navega até Cirurgia Segura]

E... ali está. O item continua marcado. O horário continua oito e quinze e quarenta e dois. Não evaporou.

Você disse que esperava encontrar tudo como deixou. Você estava certo. Isso é a persistência. O prontuário guardado na gaveta, reaberto amanhã, com a evolução intacta.

---

**EXPERIMENTO TRÊS — a tentativa de fraude.**

Agora o mais importante. Vou tentar trapacear.

São, digamos, oito e quarenta e cinco agora. Vou tocar naquele item de novo — como se eu quisesse 'atualizar' o horário para agora.

[toca no item já marcado]

Nada. Continua oito e quinze e quarenta e dois.

[toca de novo, insiste]

Nada. O sistema não deixa.

Por quê? Porque você decidiu isso na Seção três. O horário marca o instante REAL em que o antibiótico entrou. Aquilo aconteceu uma vez, às oito e quinze. Tocar na tela de novo não fez o antibiótico entrar de novo — então o horário não tem por que mudar.

O app gera o horário UMA vez, na primeira marcação, e trava. Você não consegue editar nem se quiser.

---

E é aqui que está a diferença entre uma testemunha e um diário.

Um diário, você escreve o que quiser, quando quiser, e edita depois. Um diário é a sua versão.

Uma testemunha registra o que viu, no instante em que viu, e não muda a história depois — nem sob pressão.

---

Esse horário não foi digitado. Foi gerado pelo sistema no instante em que você marcou. E não pode ser editado.

É uma testemunha. Não um diário.

---

Pensa no que isso significa numa cirurgia que vira processo. Numa auditoria. Numa sindicância. O horário no seu app não é a sua memória do que aconteceu — sujeita a erro, a pressão, a 'eu acho que foi mais cedo'. É o registro do que o sistema viu, no segundo em que viu.

Isso é o que separa um registro clínico sério de uma anotação qualquer.

E você acabou de construir isso. Você."

---

## SEÇÃO 8: ENCERRAMENTO — O QUE VOCÊ CONSTRUIU E O QUE VEM AÍ — 3 min

**Tom:** Síntese conduzida pelo aluno, fechamento caloroso, abertura de tensão para a próxima aula. LGPD entra natural, não panfletário.

"Recapitula o que você construiu hoje — e quero que seja você dizendo, na sua cabeça, não eu.

Um checklist da OMS, dezenove itens, três fases, dentro do seu app. Caixas que você marca. E um horário-testemunha em cada uma — gerado pelo sistema, imutável, que sobrevive a fechar e reabrir.

---

E onde tudo isso mora? Na sua máquina. Só na sua máquina.

O banco com os horários das suas cirurgias não foi para nuvem nenhuma. Não passou por servidor de terceiro. Não pediu login na internet. Você pode arrancar o cabo de rede agora e o checklist funciona igual — marca, registra o horário, lembra amanhã.

Para um registro de procedimento cirúrgico, isso não é detalhe. Um horário que prova quando o antibiótico entrou é dado sensível. E ele fica onde tem que ficar: com você, sob seu controle, fora do alcance de qualquer um que não devia ver. Esse é o eixo do curso inteiro — o dado do seu paciente não viaja.

---

Agora, uma confissão. Esse app que a gente construiu hoje — eu te disse que ele se comporta de um certo jeito. O horário trava na primeira marcação. Os dados persistem.

Mas eu PROVEI isso clicando, na mão, na frente de vocês. Três experimentos.

E se eu te dissesse que existe um jeito de a própria máquina provar isso sozinha — toda vez, sem eu precisar clicar?

Porque amanhã você vai pedir uma melhoria no app. O Claude Code vai mexer no código. E como você garante que, ao mexer, ele não quebrou a regra do horário-testemunha sem ninguém perceber?

---

Isso tem nome: testes automatizados. É a próxima fronteira do curso.

Na aula trinta e três, você vai aprender a fazer o app testar a si mesmo. A criar guardiões que avisam na hora em que uma regra que importa for quebrada — antes de chegar perto de um paciente.

O cirurgião confere a contagem de compressas antes de fechar. O app vai aprender a conferir as próprias regras antes de rodar.

Vejo você na próxima aula."

---

**FIM DO ROTEIRO**
