# README — Sistema de Multas (Verificação de Velocidade)

## Visão geral

Este projeto é um script em Python que recebe dados simples de um veículo (placa, motorista, velocidade registrada, velocidade máxima permitida e se já houve multa anterior) e avalia se houve infração de trânsito, qual o tipo (leve, grave ou gravíssima), calcula o valor da multa, acrescenta pontos na CNH quando necessário e trata reincidência (multa dobrada) e desconto para pagamento imediato.

O objetivo foi fazer um programa direto, fácil de entender e executar no terminal, sem depender de bibliotecas externas.

---

## Como eu pensei para chegar na solução (minha linha de raciocínio)

1. **Definir regras de negócio** — comecei listando claramente os intervalos de velocidade que correspondem a cada infração:

   * sem infração: `velocidade_registrada <= velocidade_maxima_permitida`.
   * infração leve: até 20% acima do limite (`<= 1.2 * limite`).
   * infração grave: até 50% acima do limite (`<= 1.5 * limite`).
   * infração gravíssima: acima de 50% do limite (`> 1.5 * limite`).

2. **Valores e penalidades** — defini constantes (no topo do script) com os valores das multas e os pontos correspondentes.

3. **Reincidência** — se o motorista já foi multado antes, a multa deve ser dobrada. Pensei também em permitir pagamento à vista com desconto de 20% (aplicado sobre o valor já dobrado, se houver reincidência).

4. **Interação com o usuário** — pedir os inputs em uma ordem simples: placa, nome, velocidade registrada, velocidade máxima e se já foi multado antes. Como `lower()` não podia ser usado (restrição do projeto), tratei todas as variações comuns de "Sim"/"Não" (`'Sim'`, `'sim'`, `'SIM'`, `'Nao'`, `'nao'`, etc.) nos `if`.

5. **Saídas legíveis** — sempre imprimir o resumo (placa, motorista e velocidades) e depois as mensagens de infração, detalhando multa, pontos, suspensão da CNH e instruções (ex.: comparecer ao Detran).

6. **Testes rápidos** — criei exemplos de entrada/saída para verificar cada caminho do código (sem infração, leve, grave com e sem reincidência, gravíssima com e sem reincidência e com pagamento à vista).

---

## Funcionalidades principais

* Identifica o tipo de infração a partir da velocidade registrada.
* Calcula o valor da multa conforme tabela do script.
* Aplica multa dobrada se houver reincidência.
* Oferece opção de pagamento imediato com 20% de desconto (paga-se sobre o valor atual da multa — já dobrado se for o caso).
* Imprime mensagens específicas para infração gravíssima (suspensão, curso de reciclagem, etc.).

---

## Regras de negócio e constantes (valores usados)

* `infracao_leve = R$ 130.16` (0 pontos)
* `infracao_grave = R$ 195.23` (5 pontos)
* `infracao_gravissima = R$ 880.41` (7 pontos e suspensão)

Lembre-se: caso de reincidência a multa é **dobrada**. Se o usuário pagar imediatamente, recebe **20% de desconto** sobre o valor atual (multado x2 quando houver reincidência).

---

## Ordem dos inputs

O script espera as entradas nessa ordem (cada `input()` em uma linha):

```
placa_do_veiculo
nome_do_motorista
velocidade_registrada
velocidade_maxima_permitida
multado_anteriorment  # Sim / Não (variações de caixa são tratadas no código)
```

Se o caso envolver reincidência e for necessário, o script pedirá também:

```
Deseja pagar a multa agora (Sim/Não):
```

---

## Exemplo (entrada e saída esperada)

**Entrada** (cada linha representando um `input()`):

```
ABC-1234
João Silva
121
80
Sim
Sim
```

**Saída esperada**:

```
Placa: ABC-1234
Motorista: João Silva
Velocidade registrada: 121 km/h
Velocidade máxima permitida: 80 km/h
Infração: Gravíssima - Multa de R$ 880.41, 7 pontos na CNH e suspensão da carteira.
Atenção: Multa DOBRADA por reincidência!
Atenção: CNH suspensa! Compareça ao Detran.
Atenção: Você precisa fazer um curso de reciclagem no Detran.
Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$ 1408.66
```

> Observação: o valor final `R$ 1408.66` vem de `infracao_gravissima * 2 * 0.8 = 880.41 * 2 * 0.8` (dobro por reincidência e 20% de desconto sobre o dobro).

---

## Estrutura do código — explicado passo a passo

1. **Leitura dos inputs** — o script faz `input()` para cada informação. As velocidades são convertidas para `float`.
2. **Impressão do cabeçalho** — imprime placa, motorista e as velocidades para clareza.
3. **Verificação das faixas de velocidade** — sequência de `if/elif/else` que compara `velocidade_registrada` com limites calculados (`limite`, `1.2*limite`, `1.5*limite`).
4. **Tratamento de reincidência** — em infrações grave e gravíssima, o código checa se `multado_anteriorment` indica `Sim` (verificando variações de caixa) e, se for o caso, anuncia multa dobrada e pergunta sobre pagamento.
5. **Cálculo do desconto** — se o usuário optar por pagar agora, aplica `valor_atual * 0.8` e imprime o valor final formatado com duas casas decimais.
6. **Mensagens específicas** — para gravíssima, além do valor e do desconto, o script imprime avisos sobre suspensão e curso de reciclagem.

---

## Testes sugeridos (casos que você deve checar)

1. **Sem infração** — `velocidade_registrada` menor ou igual ao limite.
2. **Leve** — `velocidade_registrada` entre `limite+1` e `1.2*limite`.
3. **Grave sem reincidência** — `<= 1.5*limite` e `multado_anteriorment = Não`.
4. **Grave com reincidência** — `<= 1.5*limite` e `multado_anteriorment = Sim`, testar pagar `Sim` e `Não`.
5. **Gravíssima sem reincidência** — `> 1.5*limite` e `multado_anteriorment = Não`.
6. **Gravíssima com reincidência** — testar pagar `Sim` e `Não`.
7. **Entradas inválidas** — testar textos em campos numéricos, velocidades negativas, cadeias vazias.

---

## Limitações conhecidas e melhorias sugeridas

* **Validação de entrada**: atualmente o script assume que o usuário digita corretamente — seria bom validar entradas (e.g. `try/except` para conversão para `float`).
* **Padronização de respostas**: se for permitido, usar `lower()` reduz muito o código repetitivo (mas aqui respeitamos sua restrição de não usar `lower()`).
* **Modularização**: separar lógica em funções (`calcula_multa`, `imprime_resultado`) melhora legibilidade e testabilidade.
* **Formatar valores monetários**: usar `locale` ou `format` para garantir separador decimal correto para pt-BR.
* **Persistência**: salvar registros em arquivo CSV para histórico.
* **Testes automatizados**: criar testes unitários com `unittest` e casos parametrizados.

---

## Como executar

No terminal, execute:

```bash
python3 multas.py
```

ou, para testar com um arquivo de entrada (`inputs.txt`) contendo as linhas de `input()` em sequência:

```bash
python3 multas.py < inputs.txt
```

---

## Autor

Feito por você — um script simples e direto para entender a lógica de infrações e praticar condicionais em Python.

---

## Licença

MIT

---

Se quiser, eu posso também:

* Gerar uma versão mais técnica (com funções e validações).
* Traduzir esse README para inglês ou espanhol.
* Criar um arquivo `inputs.txt` de exemplo com as entradas do caso de teste.

Quer que eu gere algum desses agora?
