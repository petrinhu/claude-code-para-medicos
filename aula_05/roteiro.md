# Aula 05 — Instagram: Carrossel + Newsletter

**Formato:** Gravada no OBS Studio, editada no Kdenlive  
**Duração:** ~45 min  
**Tom:** Colega com humor leve e didático  

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Você providencia:**

- [ ] Conta no Canva já logada (gratuita serve): [canva.com](https://www.canva.com). Necessária para a Seção 5 (design do carrossel). Faça o login antes de gravar para não mostrar tela de senha.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta desta aula.
- [ ] Sessão limpa, sem conversa anterior carregada (a demo nasce do zero).
- [ ] Canva aberto e logado em outra aba, pronto para a montagem ao vivo.

**Confira antes de gravar:**

- [ ] Os arquivos `carrossel_triadeinflamacao.txt` e `newsletter_semana01.md` são criados ao vivo pelo Claude; saiba em que pasta eles caem para abri-los na tela.
- [ ] Localize de antemão um template de carrossel limpo no Canva (busca 'carrossel instagram médico' ou 'carrossel educativo'), para não perder tempo procurando durante a gravação.

**Navegador:** abra a aba: https://www.canva.com

---

## SEÇÃO 1: ABERTURA (2 min)

**Tom:** Direto, conectando com aula_04, revelando a virada

**[Aviso rápido dos óculos, antes de mergulhar]**

"Antes da gente começar, um lembrete rápido: hoje tem terminal e tem Canva, e em ambos a letra às vezes fica do tamanho daquele rodapé de termo de consentimento que ninguém lê. Quem usa óculos pra perto, coloca agora, que diagnóstico a gente até arrisca de longe, mas design a gente faz de perto. Beleza? Vamos."

"Na aula passada você montou um briefing automático que roda todo dia às 7h
e já chega com as novidades do diabetes tipo 2 resumidas.

Você está se atualizando sem esforço.

Mas tem uma pergunta que provavelmente os seus pacientes já fizeram:
'Doutora, você tem Instagram?'

Hoje a gente pega exatamente esse conhecimento que você tem —
e transforma em carrossel do Instagram.

Do PubMed pro feed. Em 20 minutos.

Vamos lá."

---

## SEÇÃO 2: O CENÁRIO (4 min)

**Tom:** Situação real, identificação imediata, dois problemas claros

"Cenário.

Você é metabologista. Três anos de consultório, agenda cheia,
referência na sua área.

Seus pacientes te perguntam o tempo todo:
'Doutora, você tem Instagram?'

E a resposta é não.

Não porque você não quer. Mas porque toda vez que você tenta criar um post,
acontece a mesma coisa:

Você abre o Canva. Fica 40 minutos escolhendo template.
Você começa a escrever o texto. Fica mais 30 minutos tentando ser
'acessível' sem parecer superficial.
Você desiste. Fecha o Canva. Vai ver um artigo no PubMed porque você entende de medicina,
não de copy.

O problema não é tempo. O problema é que criar conteúdo tem dois lados:

**Lado 1:** o conteúdo clínico — você manda aqui.
Você sabe de metabolismo mais do que 99% das pessoas.

**Lado 2:** o formato digital — copy, estrutura de post, CTA, linguagem de leigo.
Aqui você não foi treinado.

O Claude resolve o lado 2. E hoje você vai ver isso acontecendo ao vivo."

---

## SEÇÃO 3: ESTRATÉGIA DE CONTEÚDO MÉDICO DIGITAL (5 min)

**Tom:** Didático, rápido, pragmático — contextualizar antes de executar

"Antes de criar, preciso te dar um framework.

**Os 3 tipos de conteúdo médico que funcionam:**

Tipo 1 — **Educar:** 'O que é resistência à insulina?'
O paciente aprende algo que não sabia. Ele salva o post, manda pra alguém.

Tipo 2 — **Alertar:** 'Esses 5 sintomas podem indicar pré-diabetes.'
O paciente se reconhece. Ele marca um amigo. Ele agenda uma consulta.

Tipo 3 — **Empoderar:** 'O que fazer agora para melhorar sua sensibilidade à insulina?'
O paciente sente que pode agir. Ele te segue porque você deu autonomia a ele.

Rotacione entre os 3. Nunca só um tipo.

**Por que carrossel?**

Carrossel costuma gerar bem mais salvamentos do que um post de imagem única.
E salvamento é um dos sinais que o algoritmo do Instagram mais valoriza:
quando alguém salva, é porque o conteúdo vale a pena guardar.
O carrossel também segura o usuário na plataforma por mais tempo, que é outro sinal positivo.

**LGPD no digital — regra de ouro:**

Nunca foto de paciente. Nunca caso real com qualquer detalhe identificável.
Todo conteúdo é educativo genérico, baseado em evidência.

Isso não é só lei — é ética médica. E é o que diferencia o conteúdo médico
de qualidade do sensacionalismo de saúde.

**Frequência realista:**
2 a 3 posts por semana é sustentável. Antes do Claude, isso era 4 a 6 horas semanais.
Com o Claude, são 30 minutos. Vamos ver por quê."

---

## SEÇÃO 4: DEMO — SCRIPT DO CARROSSEL (12 min)

**Tom:** Focado, mostrando a construção do prompt passo a passo

"O tema de hoje é este:

**A tríade invisível: como obesidade, inflamação e depressão se alimentam.**

É um tema sofisticado. A hipótese inflamatória da depressão, o papel das citocinas,
o ciclo entre cortisol e compulsão. Você sabe isso de memória.

Mas como você explica para um paciente que mal sabe o que é citocina?

> [CONFERIR CLÍNICO: o prompt abaixo cita biomarcadores específicos da hipótese inflamatória da depressão (IL-6, TNF-alfa, PCR, adipocinas) e o eixo cortisol-compulsão. Validar se a redação final do carrossel descreve esses mecanismos de forma cientificamente correta e sem afirmar causalidade além da evidência.]

Vou construir o prompt ao vivo.

```
Você é uma metabologista especialista em obesidade e síndrome metabólica.
Crie um carrossel de Instagram com 7 slides sobre a inter-relação entre
obesidade, inflamação crônica e depressão.

Regras:
- Slide 1: capa — título impactante + subtítulo (exemplo: 'Não é fraqueza. É biologia.')
- Slide 2: obesidade → inflamação (citocinas, adipocinas, PCR) — 3 linhas, linguagem de leigo
- Slide 3: inflamação → depressão (hipótese inflamatória, IL-6, TNF-alfa) — 3 linhas
- Slide 4: depressão → obesidade (cortisol, sedentarismo, compulsão alimentar) — 3 linhas
- Slide 5: o ciclo vicioso — como os três se retroalimentam, em 4 linhas
- Slide 6: o que a ciência diz sobre quebrar esse ciclo — 3 linhas, tom esperançoso
- Slide 7: call-to-action empático e não-alarmista

Linguagem: acessível para leigo, sem jargão médico.
Zero dado de paciente. Conteúdo baseado em evidência.

Formato de saída — para cada slide:
SLIDE X — [título em maiúsculas]
Texto: [copy completo]
```

[executar e mostrar resultado]

Olha o que saiu.

Slide 1: capa impactante. 'Não é fraqueza. É biologia.' — esse título já é um post.
Slides 2, 3 e 4: cada elo da tríade explicado em 3 linhas sem jargão.
Slide 5: o ciclo vicioso em linguagem que qualquer pessoa entende.
Slide 6: tom esperançoso — muito importante, não pode assustar o paciente.
Slide 7: CTA que não parece propaganda.

Reviso com olho clínico: está correto? Está acessível? Está no tom certo?

[comentário ao vivo sobre a revisão — ajustar o que não ficou bom]

Agora salvo o script em arquivo:

```
Salve o carrossel acima em um arquivo chamado carrossel_triadeinflamacao.txt na pasta atual.
```

[executar]

Pronto. Script completo, salvo, pronto para usar no Canva."

---

## SEÇÃO 5: DEMO — DESIGN NO CANVA (10 min)

**Tom:** Prático, mostrando o fluxo do Canva passo a passo

"Agora a parte visual.

O Claude deu o conteúdo. O Canva vai dar o design.

[abrir Canva — canva.com]

Passo 1: buscar um template de carrossel.
Barra de busca: 'carrossel instagram médico' ou 'carrossel educativo'.
Escolher um template limpo — fundo branco ou escuro, tipografia legível.

[mostrar a seleção de template]

Passo 2: editar o slide 1 — a capa.
Copiar do arquivo: 'A tríade invisível: como obesidade, inflamação e depressão se alimentam.'
Colar no título do Canva. Ajustar o tamanho da fonte se necessário.

[mostrar a edição ao vivo]

Passo 3: duplicar o slide 1 para criar os demais.
Copiar o texto de cada slide do arquivo e colar no Canva.
Você repete esse processo 6 vezes — são 6 minutos de trabalho mecânico.

[mostrar 2-3 slides montados para dar a ideia]

Passo 4: exportar.
Baixar → PNG ou PDF → salvo na pasta de redes sociais.
Pronto para publicar.

[mostrar o carrossel final]

Perceba o que aconteceu:
O Claude gerou o conteúdo. O Canva gerou o design.
Você fez a curadoria clínica — validou se estava correto — e montou as peças.

Sem escrever uma palavra do zero. Sem criar um design do zero.

Para quem quer automatizar ainda mais: existe uma integração experimental
chamada Canva MCP que conecta o Claude Code diretamente ao Canva.
Ainda está em evolução — mas se quiser explorar, busque 'Canva MCP Claude Code'
para ver o estado atual.

A versão de hoje — manual, confiável, 10 minutos — já resolve 90% dos casos."

---

## SEÇÃO 6: DEMO — NEWSLETTER EM 5 MIN (8 min)

**Tom:** Prático, mostrando reaproveitamento de conteúdo sem esforço dobrado

"Agora um bônus que muda o jogo.

Você acabou de criar um carrossel sobre a tríade obesidade-inflamação-depressão.
O conteúdo está fresco, organizado, revisado.

E se eu te dissesse que com mais um prompt você sai daqui
com a newsletter da semana pronta?

Mesmo tema. Formato diferente. Sem começar do zero.

Esse é o conceito de reaproveitamento de conteúdo — e é como criadores
profissionais produzem tanto em tão pouco tempo.

Prompt:

```
Com base no tema do carrossel que acabamos de criar
(tríade obesidade-inflamação-depressão),
escreva uma newsletter clínica semanal para pacientes e seguidores.

Estrutura obrigatória:
- Assunto do e-mail: curioso, não clickbait (máx. 60 caracteres, sem ponto de exclamação)
- Intro (2 linhas): gancho — uma pergunta ou observação do dia a dia clínico
- Corpo: 3 tópicos em bullets expandidos — o que é, por que importa, o que fazer
- Encerramento: 1 insight da dra. + chamada para consulta ou link (sem pressão)
- Tom: próximo e humano — como e-mail de colega, não marketing agressivo
- Máx. 300 palavras. Pronto para colar no Substack ou Mailchimp.
- Zero dado de paciente. Zero jargão médico.
```

[executar e mostrar resultado]

Olha o assunto do e-mail: curioso, sem clickbait.
Olha a intro: começa com uma cena clínica — já puxa a leitura.
Os 3 bullets: conteúdo do carrossel em formato de e-mail.
O encerramento: próximo, não vendedor.

Salvo em arquivo:

```
Salve a newsletter acima em um arquivo chamado newsletter_semana01.md na pasta atual.
```

[executar]

Dois arquivos criados: carrossel e newsletter.
Mesmo tema. Duas plataformas. Um trabalho intelectual só.

Isso é o que os criadores de conteúdo profissionais chamam de
'pilar de conteúdo' — você cria uma vez e distribui em vários formatos."

---

## SEÇÃO 7: ENCERRAMENTO + DEVER DE CASA (4 min)

**Tom:** Motivador, resumo rápido, desafio concreto

"Resumo do que a gente fez hoje.

A metabologista que não tinha Instagram saiu daqui com:
— Script de carrossel completo sobre um tema clínico sofisticado
— Layout visual pronto no Canva para publicar amanhã
— Newsletter da semana pronta para o Substack

Em menos de 40 minutos. Sem escrever copy do zero. Sem designer.

E aprendeu que um tema vira dois formatos — carrossel + newsletter —
sem esforço dobrado.

Agora o dever de casa.

Pegue um tema da sua especialidade que você domina e faça isso:

```
Você é especialista em [SUA ESPECIALIDADE].
Crie um carrossel de Instagram com 6 slides sobre [SEU TEMA].
- Slide 1: capa com título impactante
- Slides 2-5: um ponto por slide, linguagem de leigo, máx. 3 linhas cada
- Slide 6: call-to-action empático
- Zero jargão médico. Zero dado de paciente.
```

Monte no Canva. Publique ou guarde — o exercício é criar.

Na aula_06 a gente entra em território diferente:
pôster de congresso no formato ABNT, slides científicos,
e análise de dados de pesquisa com gráficos para publicação.

Você vai sair com material pronto para submeter em congresso.

Até lá."

---

**FIM DO ROTEIRO**
