### Desafio 3: Manipulando Preços
#Imagine que você tem um produto que custa `R$ 100.50`.
#O usuário recebeu um desconto de `15%`.
#Calcule o valor final e exiba uma mensagem:
#`"O produto custava R$ 100.50, com desconto foi para R$ [VALOR_FINAL]."`

preco = 100.50

valorFinal = preco - (15/100*preco)

print (f"O produto custava R$ 100.50, com desconto foi para R$ {valorFinal}.")