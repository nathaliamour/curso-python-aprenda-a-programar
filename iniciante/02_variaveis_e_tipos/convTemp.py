### Desafio 2: Conversor de Temperatura
#Crie um script que converta uma temperatura de graus Celsius para Fahrenheit.
#A fórmula é: `F = C * 1.8 + 32`
#Peça o valor em Celsius e mostre o resultado formatado com duas casas decimais.
tempC = float(input("Qual é a temperatura em graus Celcius? "))

tempF = tempC * 1.8 + 32

print(f"{tempC:.2f} graus Celcius é igual a {tempF:.2f} graus Fahrenheit.")