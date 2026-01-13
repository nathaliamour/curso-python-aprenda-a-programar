### Desafio 1: O Contador de Caracteres
#Crie um programa que peça uma frase ao usuário e diga:
#1. Quantos caracteres a frase tem.
#2. Quantas vezes a letra "a" aparece (dica: procure por `.count()`).
frase = input ("Digite a sua frase:")

quant = len(frase)
letraA = frase.count("a")


print(f"A sua frase tem {quant} caracteres.")
print(f"Além disso, ela possui {letraA} letra(s) A.")