# Aula 19 — BigTech Virtual: Montando o Time Completo

**Formato:** Gravada no OBS Studio, editada no Kdenlive  
**Duração:** ~38 min  
**Tom:** Colega com humor leve e didático — revelar que o residente de plantão tem um hospital inteiro atrás dele

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Já preparado em `resources/` (é só usar):**

- [ ] `resources/prompts_aula19.md` : cola com todos os prompts da aula (`/bigtech`, `@narciso-ciso`, `@caetano-cto`, o pedido do ADR-001 e `/tab_pendencias`), prontos para copiar e não errar a digitação ao vivo. Apoio das Seções 3 a 7.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] A constelação de agents da BigTech Virtual disponível: a skill `/bigtech` e os agents `@narciso-ciso` e `@caetano-cto` devem aparecer no autocomplete.

**Confira antes de gravar:**

- [ ] Digite `/` e confirme que `/bigtech` e `/tab_pendencias` aparecem na lista de skills.
- [ ] Digite `@` e confirme que `narciso-ciso` e `caetano-cto` autocompletam.
- [ ] O arquivo `docs/decisoes/ADR-001-persistencia-local.md` é criado ao vivo pelo Claude na Seção 6; saiba em que pasta ele cai para abri-lo na tela.

**Navegador:** nenhum site é necessário nesta aula.

---

## SEÇÃO 1: RECONEXÃO — O HOSPITAL INTEIRO (4 min)

**Tom:** Promessa cumprida — conectar diretamente com o que o aluno acabou de aprender

**[Aviso rápido dos óculos, antes de mergulhar]**

"Antes de chamar a junta inteira: cola os óculos no nariz. Hoje vamos abrir o organograma do hospital no terminal, e nome de especialista em fonte pequena some que nem residente na hora da visita. Ajusta o zoom também, que a gente não perde ninguém de vista."

"Na aula passada você equipou seu residente.

Maleta completa: plugin com skills, MCPs e hooks.
POP institucional: a skill que qualquer residente lê e segue.
Checklist automático: o hook que dispara antes que você precise lembrar.

Mas tudo isso era sobre um residente.

Um residente excelente — incansável, rápido, sem reclamar do plantão duplo.

Só que você sabe o que acontece quando um caso ultrapassa o residente.

Você não pede para ele resolver.
Você pede interconsulta.

[mostrar a tabela na tela]

O residente é brilhante em tudo.
Mas quando a dúvida é de cardiologia, você quer o cardiologista.
Quando é de neurocirurgia, você quer o neurocirurgião.
Quando é de segurança jurídica, você quer o advogado do hospital.

Hoje você vai conhecer o hospital inteiro que existe por trás do seu residente.

E vai aprender a pedir interconsulta."

---

## SEÇÃO 2: O ORGANOGRAMA — QUEM É QUEM (5 min)

**Tom:** Catálogo ágil — não listar 65 nomes, mostrar o que importa para o ClinMd-Tribe

"Existe uma constelação de especialistas disponível dentro do Claude Code.

Não são 65 médicos diferentes.
São 65 arquivos de texto com personas especializadas.

[mostrar a tabela de C-levels]

| Especialista | Cargo | Para que serve no ClinMd-Tribe |
|---|---|---|
| Cósimo | Chief of Staff | Convoca a junta certa para o porte do seu projeto |
| Caetano | CTO | Decisões de stack, arquitetura, código |
| Narciso | CISO | Segurança, privacidade, LGPD |
| Cláudio | CLO | Jurídico, compliance, contratos |
| Capitolino | CPO | O que construir, escopo, MVP |
| Celso | CEO | Decisões estratégicas de alto impacto |

Além dos C-levels, existem mais de cinquenta especialistas operacionais:
backend-engineer, frontend-engineer, qa-engineer, security-engineer,
devops-sre, mobile-engineer, e muitos outros.

Você não precisa decorar nenhum deles.

Quem decora é o Cósimo.

O trabalho do Cósimo é exatamente esse: você descreve o caso,
ele convoca os especialistas certos para o porte do seu projeto.

E o comando que invoca o Cósimo é:

```
/bigtech
```"

---

## SEÇÃO 3: DEMO — /BIGTECH MONTA O TIME (8 min)

**Tom:** Revelar — o aluno vê o Cósimo em ação no projeto real

"Vamos ver isso no ClinMd-Tribe.

[entrar na pasta do projeto e abrir o Claude Code]

```
cd Documents\projetos\clinmd-tribe
claude
```

Prompt:

```
/bigtech
```

[aguardar e mostrar o resultado]

---

Olha o que o Cósimo fez.

Ele classificou o porte do projeto: solo ou early-stage.
Projeto de um médico, uma máquina, sem equipe.

E montou um time enxuto — que é a resposta certa para esse porte.

Mas repara numa coisa específica.

O Narciso está ativo. O Cláudio está ativo.

Mesmo sendo um projeto pequeno, mesmo sendo solo —
esses dois especialistas foram mantidos.

Por que?

Porque o ClinMd-Tribe lida com dado de paciente.

Esse é o critério que muda a regra:
projeto pequeno em saúde não é projeto pequeno em termos de risco.
Quando existe PII — Informação de Identificação Pessoal —
o CISO e o CLO não são cortados.
São obrigatórios.

Isso não é burocracia.
É a mesma lógica que faz você checar a identificação do paciente
antes de qualquer procedimento, independente de ser UTI ou ambulatório.

O Cósimo sabe disso.
E agora você também sabe."

---

## SEÇÃO 4: DEMO — @NARCISO-CISO (7 min)

**Tom:** Especialista em ação — o titular de segurança respondendo sobre dado clínico local

"Agora vamos consultar o Narciso diretamente.

Prompt:

```
@narciso-ciso O ClinMd-Tribe vai salvar evoluções clínicas
no computador do médico. Como protejo esses dados?
```

[aguardar e mostrar o resultado]

---

Olha o que o Narciso trouxe.

Não foi uma resposta genérica sobre segurança.
Foi um modelo de ameaça para o contexto específico:
dado que não sai da máquina, criptografia em repouso,
privacidade por design, secrets fora do repositório.

E tudo isso referenciado ao contexto do ClinMd-Tribe — dado de paciente, app local, médico solo.

Isso é o que diferencia o generalista do titular.

O residente generalista teria dado uma resposta plausível.
O Narciso respondeu como o chefe do serviço de segurança
que já viu esse cenário antes:
dado de saúde, dispositivo pessoal, sem infra corporativa.

Lembra o que você aprendeu na aula_18?

Skill é um arquivo de texto.
Agent também é um arquivo de texto — com uma persona especializada escrita.
Não é magia. É protocolo.

O Narciso leu dezenas de milhares de cases de segurança em saúde
e agora responde com o viés certo para esse tipo de decisão."

---

## SEÇÃO 5: DEMO — @CAETANO-CTO (7 min)

**Tom:** Contraste — a mesma questão de persistência recebe ênfase diferente do CTO

"Agora vamos consultar o Caetano.

Sobre o mesmo projeto. Sobre a mesma decisão de guardar dados.
Mas com uma pergunta técnica diferente.

Prompt:

```
@caetano-cto O ClinMd-Tribe precisa guardar dados localmente.
SQLite ou arquivo JSON — qual você recomenda?
```

[aguardar e mostrar o resultado]

---

O Caetano respondeu sobre viabilidade.

SQLite nativo em Python, zero configuração, consultas SQL quando o projeto crescer,
custo de manutenção baixo para projeto solo.

Olha o contraste.

Você acabou de perguntar sobre persistência para dois especialistas.

O Narciso focou em segurança: como proteger, como criptografar, como garantir privacidade.
O Caetano focou em viabilidade: qual a ferramenta certa para o porte, qual o custo de manutenção.

A mesma pergunta. O mesmo projeto.
Duas respostas com ênfases completamente diferentes.

Isso não é o mesmo Claude com dois nomes diferentes.
É o titular de segurança e o titular de tecnologia
olhando para o mesmo problema com lentes diferentes.

E isso é exatamente o que você quer numa interconsulta real.

Você não quer que o cardiologista responda como se fosse o infectologista.
Você quer a especialidade certa para cada dimensão do problema."

---

## SEÇÃO 6: ARTEFATO — ADR-001 (4 min)

**Tom:** Instalar o hábito — consultou, registrou

"Você consultou dois especialistas.
Recebeu dois pareceres valiosos.

Agora faz o que qualquer bom plantonista faz depois de uma interconsulta:

Registra no prontuário.

Prompt:

```
Com base nas consultas ao @narciso-ciso e ao @caetano-cto,
cria o arquivo docs/decisoes/ADR-001-persistencia-local.md
resumindo a decisão de persistência do ClinMd-Tribe.
Formato simples: contexto, decisão, justificativa, consequências.
```

[aguardar o Claude criar o arquivo]

---

ADR é Architecture Decision Record — Registro de Decisão de Arquitetura.

É o padrão profissional de engenharia para registrar: por que essa decisão foi tomada,
com quais informações, quais as consequências.

No hospital: é a nota de interconsulta no prontuário.
Você documenta o parecer do especialista, não só a conduta final.

No ClinMd-Tribe: é o registro de que você consultou o CISO e o CTO
e chegou a uma decisão fundamentada.

Consultou → registrou.

Esse é o hábito que separa o projeto profissional do projeto que ninguém consegue manter depois."

---

## SEÇÃO 7: TABELA + ENCERRAMENTO (3 min)

**Tom:** Consolidação e ponte — fechar com chave e abrir a próxima

"Tabela de bolso — quando chamar quem.

[mostrar a tabela na tela]

| Tipo de decisão | Especialista |
|---|---|
| Stack, arquitetura, código | `@caetano-cto` |
| Segurança, LGPD, privacidade | `@narciso-ciso` |
| O que construir / escopo / MVP | `@capitolino-cpo` |
| Montar o time para o projeto | `/bigtech` |

---

Antes de fechar, atualiza as pendências:

```
/tab_pendencias
```

[mostrar a tabela — aula_19 concluída, aula_20 como próxima]

---

Dever de casa.

A junta dos três pareceres.

Pensa em três decisões pendentes do ClinMd-Tribe.
Podem ser decisões técnicas, de escopo, de segurança — qualquer uma que você sabe que vai precisar tomar.

Para cada uma, escreve:
1. A decisão, em uma frase.
2. Qual titular você convocaria.
3. O prompt que você usaria — `/bigtech` ou `@especialista`.

Não executa. Só escreve.
Traga as três para a próxima aula.

---

Resumo do que ficou claro hoje.

Você não está sozinho no plantão.
Existe um hospital inteiro atrás do seu residente —
e `/bigtech` é o pedido de interconsulta multidisciplinar.

Cósimo classifica o porte e monta o time certo.
Narciso responde com a lente da segurança.
Caetano responde com a lente da tecnologia.
Ênfases diferentes para a mesma decisão — isso é o valor da especialização.

E quando a interconsulta chega, você registra no prontuário.
Consultou → registrou. ADR-001 está no projeto.

---

Na próxima aula: `/tab_pendencias`.

Você vai aprender como usar o mesmo time que montou hoje
para ordenar as tarefas do ClinMd-Tribe por prioridade —
usando o critério que os times de engenharia profissional usam:
custo de atraso versus esforço.

Até lá."

---

**FIM DO ROTEIRO**
