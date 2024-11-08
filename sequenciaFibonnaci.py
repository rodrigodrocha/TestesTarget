"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1
e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando
se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada
de sua preferência ou pode ser previamente definido no código;
"""

numero = int(input("Informe um número inteiro: "))
fibonacci = [0, 1]
ultimoNumero = 1
while  ultimoNumero <= numero:
    if ultimoNumero == numero:
        print("Esse número pertence a sequência de Fibonacci")
        break
    penultimoNumero = len(fibonacci)
    penultimoNumero = fibonacci[penultimoNumero - 2]
    ultimoNumero += penultimoNumero
    if ultimoNumero > numero:
        print("Esse número NÃO pertence a sequência de Fibonacci")
        break
    fibonacci.append(ultimoNumero)
print(fibonacci)