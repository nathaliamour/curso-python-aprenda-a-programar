num1 = float (input("Digite o primeiro numero: "))
num2 = float (input("Digite o segundo numero: "))

soma = num1 + num2 
subtracao = num1 - num2
multiplicacao = num1 * num2

if num2 != 0:
    divisao = num1 / num2
else:
     divisao = "Denominador zero!"

print("A soma dos números é ", soma)
print("A subtração dos números é ", subtracao)
print("A multiplicação dos números é ", multiplicacao)
print("A divisão dos números é ", divisao)