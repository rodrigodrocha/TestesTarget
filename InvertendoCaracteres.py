"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada
de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""

palavra = str(input("Digite uma palavra: "))
i = 0
palavraInvertida = ""
while i < len(palavra):
    i += 1
    letra = palavra[(len(palavra) - i)]
    palavraInvertida += letra
print(palavraInvertida)