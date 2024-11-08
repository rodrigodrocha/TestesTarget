"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.

"""
def Porcentual(estado, faturamento):
    porcentual = faturamento / total * 100
    print ( estado, "teve", round(porcentual, 2), "% do faturamento total.")

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros
Porcentual("São Paulo", sp)
Porcentual("Rio de Janeiro", rj)
Porcentual("Minas Gerais", mg)
Porcentual("Espírito Santo", es)
Porcentual("Outros", outros)