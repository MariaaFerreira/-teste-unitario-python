# Calculadora em Python

Este projeto é uma calculadora simples feita em Python para aprendizado de testes unitários.

A atividade faz parte da aula prática de teste unitário com Python e PyUnit, utilizando o módulo `unittest` no VS Code, com orientação do professor Johnatan.

Neste projeto, criei a função de potência e, como desafio proposto, a função de cálculo de média.

## Funções

A calculadora possui as seguintes funções:

- Somar
- Subtrair
- Multiplicar
- Dividir
- Potência
- Calcular média

## Como usar

Exemplo:

```python
from calculadora import somar, calcular_media

print(somar(2, 3))
print(calcular_media([10, 20, 30]))


## Atividade com o uso de IA - PARTE 2
Essa tabela é dos teste para função dividir

| ID do teste | Cenário | Entrada | Resultado esperado | Tipo de cenário | Observação |
|---|---|---|---|---|---|
| TD01 | Divisão exata | `dividir(10, 2)` | `5.0` | Caso normal | Verifica uma divisão sem resto. |
| TD02 | Divisão com resultado decimal | `dividir(5, 2)` | `2.5` | Caso normal | Verifica se a função retorna corretamente valores decimais. |
| TD03 | Divisão de número negativo | `dividir(-10, 2)` | `-5.0` | Caso normal | Verifica o comportamento com dividendo negativo. |
| TD04 | Divisão de dois números negativos | `dividir(-10, -2)` | `5.0` | Caso normal | Verifica se dois sinais negativos resultam em valor positivo. |
| TD05 | Divisão de zero por outro número | `dividir(0, 5)` | `0.0` | Caso de borda | Zero dividido por número diferente de zero deve retornar zero. |
| TD06 | Divisão por zero | `dividir(10, 0)` | `ZeroDivisionError` | Caso de erro | Verifica se a função gera erro ao tentar dividir por zero. |

Essa tabela é dos teste para função multiplicar
| ID do teste | Cenário | Entrada | Resultado esperado | Tipo de cenário | Observação |
|---|---|---|---|---|---|
| TM01 | Multiplicação de dois inteiros positivos | `multiplicar(3, 4)` | `12` | Caso normal | Verifica uma multiplicação simples entre dois números positivos. |
| TM02 | Multiplicação com zero | `multiplicar(5, 0)` | `0` | Caso de borda | Todo número multiplicado por zero deve resultar em zero. |
| TM03 | Multiplicação de número positivo por negativo | `multiplicar(6, -2)` | `-12` | Caso normal | Verifica o resultado com sinais diferentes. |
| TM04 | Multiplicação de dois números negativos | `multiplicar(-3, -4)` | `12` | Caso normal | Verifica se dois números negativos resultam em valor positivo. |
| TM05 | Multiplicação com número decimal | `multiplicar(2.5, 4)` | `10.0` | Caso normal | Verifica se a função trabalha corretamente com valores decimais. |
| TM06 | Multiplicação de dois zeros | `multiplicar(0, 0)` | `0` | Caso de borda | Verifica o menor caso possível envolvendo zero. |
| TM07 | Multiplicação por número muito grande | `multiplicar(10**10, 10**5)` | `10**15` | Caso de borda | Verifica se a função lida com números grandes. |
| TM08 | Multiplicação de string por número | `multiplicar("abc", 2)` | `"abcabc"` | Caso de borda | Em Python, string multiplicada por inteiro repete o texto. |