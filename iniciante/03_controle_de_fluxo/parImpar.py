### Desafio 1: Par ou Ímpar?
#Peça um número inteiro ao usuário.
#O programa deve dizer se o número é **Par** ou **Ímpar**.
num = int(input("Digite um número inteiro: "))

resto = num%2

if resto == 0:
    print(f"O número escolhido ({num}) é par")
else: 
    print(f"O número escolhido ({num}) é ímpar")

