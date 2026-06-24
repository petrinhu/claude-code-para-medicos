# Prompts e itens da aula 20 (cola de bastidor)

So o instrutor ve isto; nao aparece na aula. Pronto para copiar, para nao errar ao vivo.

## Secao 4 - criar a tabela
```
/tab_pendencias --create
```

Quando a skill pedir os itens, forneca estas seis calculadoras (texto pronto):

```
CHA2DS2-VASc - escore de risco de AVC em fibrilacao atrial
HAS-BLED - escore de risco de sangramento na anticoagulacao
PHQ-9 - escala de rastreio de depressao (Patient Health Questionnaire)
GAD-7 - escala de rastreio de ansiedade generalizada
MELD - formula de gravidade da doenca hepatica terminal
MMSE - mini-exame do estado mental
```

## Secao 7 - atualizar pendencias
```
/tab_pendencias
```

## Checagem antes de gravar
- Confirme que `/tab_pendencias` aparece ao digitar `/`.
- A tabela `TODO.md` e gerada/atualizada ao vivo; saiba onde ela cai para mostrar o topo (CHA2DS2-VASc esperado na primeira linha apos a triagem WSJF).
- O CHA2DS2-VASc deve subir ao topo: alto custo de atraso, baixo esforco. Se nao subir, refaca o `--create` conferindo a descricao dos itens.
