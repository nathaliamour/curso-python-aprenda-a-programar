### Desafio 2: Contagem Regressiva
#Faça um programa que use um laço (`for` ou `while`) para exibir uma contagem regressiva de 10 até 0.
#Quando chegar ao 0, imprima: `"Lançar!"`.

for i in range (10, -1, -1): 
    if i == 0: 
        print("Lançar!")
    else: 
        print(i) 