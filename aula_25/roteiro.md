# Aula 25 — Dashboard Financeiro: Entrada de Dados

**Formato:** Gravada no OBS Studio, editada no Kdenlive
**Duração:** ~48 min
**Tom:** Ortopedista que fecha o mês e quer entender o que está acontecendo com as glosas
**Módulo:** S06.01 — Dashboard Financeiro

---

## 📋 ANTES DE COMEÇAR (preparo de bastidor)

> Marque cada item antes de gravar. Nada aqui é falado na aula; é só o seu setup de bastidor. No HTML desta página as caixas são clicáveis: vá marcando durante a gravação para não se perder.

**Já preparado em `resources/` (é só usar):**

- [ ] `resources/dados_3_meses_bastidor.csv` : os três meses fictícios do ortopedista (junho, julho, agosto de 2025), com receita bruta, glosas e consultas. Cola de bastidor para você digitar os valores certos na Seção 5; o app NÃO importa esse arquivo, você digita campo a campo no formulário.

**Aberto e pronto:**

- [ ] Claude Code aberto no terminal, na pasta do projeto ClinMd-Tribe.
- [ ] Sessão limpa, sem conversa anterior carregada.
- [ ] Projeto ClinMd-Tribe com as features das aulas anteriores (as seis calculadoras do S05) já funcionando.
- [ ] Pasta `data/` ainda SEM o arquivo `clinmd.db` (apague um `data/clinmd.db` de testes anteriores, se existir, para a Seção 6 mostrar o banco nascendo do zero).

**Confira antes de gravar:**

- [ ] `uv run python main.py` abre o app no navegador sem erro (estado pré-aula).
- [ ] As 4 camadas existem como pastas: `domain/`, `application/`, `infrastructure/`, `presentation/`.
- [ ] Você sabe onde fica a pasta `data/` para mostrá-la no explorador de arquivos na Seção 6.
- [ ] Os três valores da cola batem com a tabela da Seção 2 do roteiro (jun: 28000 / 4200 / 95; jul: 31000 / 3800 / 108; ago: 27500 / 5100 / 91).

**Navegador:** nenhum site é necessário nesta aula. O navegador só abre para exibir o app Flet (via `uv run python main.py`).

---

## SEÇÃO 1: ABERTURA — 4 min

**Tom:** Contraste direto com S05 — o app que esquece vs o app que lembra

**[Aviso rápido dos óculos, antes de mergulhar]**

"Antes de começar: se os óculos de perto andam na mesa, é agora que eles entram em campo. Hoje a gente abre arquivo de banco de dados, e o terminal escreve em corpo de exame de rotina, daquele tamanho que ninguém pediu. Põe os óculos e bora."

"Nas últimas quatro aulas você construiu seis calculadoras.

Cada uma delas fazia a mesma coisa:
você digitava os valores, clicava calcular, recebia o resultado.

E quando você fechava o app?

Tudo sumia.

Bilirrubina 4,5. INR 1,8. Score 20. Mortalidade 19,6%.
Fecha. Abre de novo. Nada.

Isso é uma calculadora.
Útil — mas sem memória.

---

Hoje o ClinMd-Tribe ganha memória.

Não memória de paciente.
Memória de consultório.

Você vai registrar receita, glosas e consultas mês a mês.
E quando você fechar o app e abrir amanhã,
os dados vão estar lá.

---

O personagem de hoje é um ortopedista.

Consultório próprio.
Vários convênios.
E um problema que muitos especialistas conhecem:
as glosas estão subindo.

Agosto foi o pior mês em seis meses.
Mas é tendência ou coincidência?

Sem os dados anteriores, você não sabe.
Com o app que você vai construir hoje, você sabe."

---

## SEÇÃO 2: REGISTROMENSAL COMO ESPECIFICAÇÃO — 6 min

**Tom:** Clínico e técnico — transformar o registro financeiro em dado antes de escrever o prompt

"Antes de escrever o prompt, você precisa saber o que o app vai guardar.

O dado de cada mês tem cinco campos:

| Campo | Tipo | Exemplo |
|---|---|---|
| Mês | número inteiro (1-12) | 8 |
| Ano | número inteiro | 2025 |
| Receita bruta | número decimal | 27.500,00 |
| Glosas | número decimal | 5.100,00 |
| Número de consultas | número inteiro | 91 |

Isso é o `RegistroMensal`.
Um objeto simples.
Cinco campos.
Um por mês.

---

Agora os três meses mais recentes do nosso ortopedista.

[mostrar na tela]

| Mês | Receita bruta | Glosas | Consultas |
|---|---|---|---|
| Junho/2025 | R$ 28.000 | R$ 4.200 | 95 |
| Julho/2025 | R$ 31.000 | R$ 3.800 | 108 |
| Agosto/2025 | R$ 27.500 | R$ 5.100 | 91 |

Agosto: receita caiu, glosas subiram, consultas caíram.

Esses são os valores que você vai digitar no app quando ele estiver pronto.
E quando você fechar e reabrir — eles vão estar lá.

---

Mas onde o app vai guardar isso?

Não na memória RAM — ela some quando o programa fecha.
Não na internet — dado financeiro do consultório não sobe pra lugar nenhum.

Em um arquivo, na sua máquina.
Um arquivo de banco de dados.
Dentro da pasta `data/` do projeto.

Essa é a camada de infraestrutura que você conheceu na aula_15 —
e que as calculadoras nunca precisaram usar.

Hoje ela entra em cena."

---

## SEÇÃO 3: PROMPT ENTRADA DE DADOS — 5 min

**Tom:** Professor conduz — três destaques antes de digitar: Path, CREATE TABLE IF NOT EXISTS, camadas

"Três destaques antes de digitar o prompt.

Primeiro: o caminho do banco de dados.

O app vai criar um arquivo chamado `clinmd.db` dentro da pasta `data/`.
O Claude precisa saber que esse caminho é relativo à localização do código —
não à pasta onde você está quando roda o programa.

Se você usar `'data/clinmd.db'` como texto simples,
o arquivo vai aparecer em lugares diferentes dependendo de onde você rodou o app.
Você vai 'perder' seus dados sem entender por quê.

A forma correta usa `Path(__file__)` — que sempre aponta para onde o arquivo de código está.

Segundo: `CREATE TABLE IF NOT EXISTS`.

Toda vez que o app abre, ele verifica se a tabela existe.
Se não existe, cria.
Se já existe, não faz nada.
Idempotente.

Terceiro: as camadas.

O banco fica em `infrastructure/`.
A lógica fica em `domain/` e `application/`.
A tela fica em `presentation/`.
Cada camada faz uma coisa."

---

[digitar no terminal — ler cada parte em voz alta]

```
Implemente o módulo financeiro do ClinMd-Tribe
respeitando a Clean Architecture das 4 camadas:

domain/financeiro/registro_mensal.py
  - Classe RegistroMensal com campos:
    mes (int 1-12), ano (int),
    receita_bruta (float), glosas (float), n_consultas (int)

infrastructure/repositorio_financeiro.py
  - Conexão SQLite em data/clinmd.db
    (caminho absoluto: Path(__file__).parent.parent / "data" / "clinmd.db")
  - CREATE TABLE IF NOT EXISTS registros_mensais
  - Método salvar(registro: RegistroMensal) -> None
  - Método listar_todos() -> list[RegistroMensal]

application/servicos/financeiro_service.py
  - salvar_registro(dados: dict) -> None
  - listar_registros() -> list[dict]

presentation/telas/formulario_mensal.py
  - 5 campos: Mês (1-12), Ano, Receita bruta, Glosas, Nº consultas
  - Botão "Salvar registro"
  - Tabela abaixo mostrando todos os registros salvos
    (colunas: Mês, Ano, Receita bruta, Glosas, Consultas)
```

---

[enviar o prompt ao Claude Code]

---

## SEÇÃO 4: CLAUDE IMPLEMENTA + LEITURA SUPERVISIONADA — 10 min

**Tom:** Aguardar + auditar — quatro perguntas, primeira é crítica

[aguardar o Claude Code processar]

[mostrar na tela os arquivos sendo criados e modificados]

"Três arquivos novos.
Um modificado.

`domain/financeiro/registro_mensal.py` — criado.
`infrastructure/repositorio_financeiro.py` — criado.
`application/servicos/financeiro_service.py` — criado.
`presentation/telas/formulario_mensal.py` — criado.

Agora você lê antes de rodar.

Quatro perguntas."

---

**Pergunta 1:** ← crítica

"Abra `infrastructure/repositorio_financeiro.py`.

O caminho do banco usa `Path(__file__)` — não uma string como `'data/clinmd.db'`?

Você está procurando algo assim no topo do arquivo:

```python
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "clinmd.db"
```

Se o caminho for uma string simples — `sqlite3.connect('data/clinmd.db')` —
o banco vai aparecer em lugares diferentes dependendo de onde você rodar o app.
Você vai salvar dados, fechar, abrir de outra pasta, e os dados vão ter sumido.

Esse é o erro mais traiçoeiro desta aula.
Silencioso. Difícil de debugar.

[mostrar o código]

Correto — `Path(__file__)` com caminho absoluto relativo ao código."

---

**Pergunta 2:**

"O `CREATE TABLE IF NOT EXISTS` roda toda vez que o app abre — não só na primeira vez?

Procure o método que cria a tabela.
Ele deve ser chamado na inicialização do repositório — não só uma vez na instalação.

Se a tabela já existe, o `IF NOT EXISTS` garante que não vai tentar criar de novo.
Se não existe, cria.

[mostrar onde é chamado]

Correto — roda na inicialização, idempotente."

---

**Pergunta 3:**

"O `repositorio_financeiro.py` está em `infrastructure/` — não em `domain/` nem em `application/`?

Abra o explorador de arquivos.
O arquivo deve estar dentro da pasta `infrastructure/`.

O banco de dados é infraestrutura.
Assim como um servidor de e-mail é infraestrutura.
O domínio não sabe que existe SQLite — ele só sabe que existe um RegistroMensal.

[confirmar a localização do arquivo]

Correto — em `infrastructure/`."

---

**Pergunta 4:**

"A tela chama o serviço — não acessa o repositório diretamente?

Abra `presentation/telas/formulario_mensal.py`.

Quando o botão 'Salvar registro' é clicado,
o código deve chamar `salvar_registro` do `financeiro_service`.
Não deve chamar o repositório diretamente.
Não deve ter `sqlite3` na tela.

[mostrar a chamada ao serviço]

Está chamando o serviço. A arquitetura está respeitada."

---

**Frase-âncora:**

"O banco está em `infrastructure/`.
O domínio não sabe que é SQLite.
A tela não sabe que tem banco.
Cada camada faz uma coisa."

---

## SEÇÃO 5: APP AO VIVO — SALVAR 3 MESES — 5 min

**Tom:** Demo funcional — preencher, salvar, ver na tabela

[no terminal]

```
uv run python main.py
```

[aguardar o Flet abrir no browser]

---

"Aqui está o formulário.

Cinco campos.
Um botão.

Vamos cadastrar junho.

[preencher os campos]

- Mês: 6
- Ano: 2025
- Receita bruta: 28000
- Glosas: 4200
- Consultas: 95

[clicar Salvar registro]

Apareceu na tabela.

---

Julho.

- Mês: 7 / Ano: 2025 / Receita: 31000 / Glosas: 3800 / Consultas: 108

[clicar Salvar]

Na tabela.

---

Agosto.

- Mês: 8 / Ano: 2025 / Receita: 27500 / Glosas: 5100 / Consultas: 91

[clicar Salvar]

Três meses na tabela.

Receita caiu. Glosas subiram. Consultas caíram.

O app está vendo o que você viu."

---

## SEÇÃO 6: CLÍMAX — FECHAR E REABRIR — 4 min

**Tom:** O momento mais importante da aula — silêncio dramático antes de reabrir

"Agora vem a diferença.

[pausar]

Feche o app.

[fechar o browser do Flet]

Feche o terminal.

[fechar o terminal]

---

[abrir novo terminal]

```
uv run python main.py
```

[aguardar o Flet abrir]

---

[mostrar na tela]

Os três meses estão lá.

Junho. Julho. Agosto.

---

As calculadoras do S05 esqueciam.
Esse app lembra.

Isso é persistência.
O dado mora num arquivo.
O arquivo sobrevive ao fechar o programa.

E onde está esse arquivo?

[abrir o explorador de arquivos, navegar até a pasta data/]

`data/clinmd.db`

Está aqui.
Na sua máquina.
Não na nuvem.
Não no Claude.
Aqui."

---

## SEÇÃO 7: .GITIGNORE — DATA/*.DB NÃO VAI AO GIT — 4 min

**Tom:** Reforço LGPD — dado financeiro não sobe ao repositório

"Antes de encerrar, um passo de segurança.

Você vai commitar o projeto no Git.
Mas o `clinmd.db` não deve ir junto.

Dado financeiro do consultório é sensível.
Receita, glosas, número de consultas — esses dados não devem estar num repositório.
Mesmo que seja privado.

[abrir o `.gitignore`]

Verificar se `data/*.db` está na lista.

Se não estiver, o Claude adiciona:

```
Adicione data/*.db ao .gitignore do projeto
```

[confirmar que aparece no .gitignore]

Agora o banco fica local.
O código vai ao Git.
O dado fica na sua máquina."

---

## SEÇÃO 8: ENCERRAMENTO + GANCHO AULA_26 — 3 min

**Tom:** Consolidar + criar tensão para o próximo

"O que ficou pronto hoje.

Um formulário que salva registros financeiros mensais.
Um banco SQLite que mora na pasta `data/`.
Uma tabela que mostra os dados salvos.
E o mais importante: o app que lembra quando você fecha e abre de novo.

---

Mas olhe para os três meses na tabela.

Junho: R$ 28.000 brutos, R$ 4.200 de glosa.
Julho: R$ 31.000, R$ 3.800 de glosa.
Agosto: R$ 27.500, R$ 5.100 de glosa.

O que você está vendo?

Receita caindo. Glosas subindo. Consultas caindo.

Mas é tendência ou coincidência?

Olhar para uma tabela de números não responde essa pergunta.
Para responder, você precisa de uma curva.

Na próxima aula: o dashboard.

Os mesmos dados que você salvou hoje
vão virar um gráfico de barras e uma linha de tendência.

E agosto vai aparecer em vermelho."

---

## SEÇÃO 9: DEVER DE CASA — 3 min

**Tom:** Prático — usar o app com dados reais

"Dever de casa.

Abra o ClinMd-Tribe.
Cadastre os últimos três meses do seu próprio consultório.

Não precisa ser exato.
Estimativas funcionam.

- Receita bruta média mensal
- Quanto foi glosado (se souber)
- Número de consultas

Se não tiver os valores precisos: use estimativas.
O exercício é o fluxo — cadastrar, fechar, reabrir, ver os dados.

Na próxima aula você vai transformar esses dados num gráfico.

Até lá."

---

**FIM DO ROTEIRO**
