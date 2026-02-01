### Desafio 1: Saudação Personalizada
#Crie uma função chamada `saudacao(nome, hora)` que receba um nome e uma hora (0-23).
#- Se for entre 5 e 11, imprima "Bom dia, [nome]!".
#- Se for entre 12 e 17, imprima "Boa tarde, [nome]!".
#- Senão, imprima "Boa noite, [nome]!"./

def saudacao(nome, hora): 
    if 5 <= hora <= 11:
        print(f"Bom dia, {nome}!")
    elif 12 <= hora <= 17:
        print(f"Boa tarde, {nome}!")
    else: 
        print(f"Boa noite, {nome}!")

nome = input("Qual o seu nome?")
hora = int(input("Entre somente com o valor da hora atual (0-23): "))


if 0 <= hora <= 23: 
    saudacao(nome,hora)
else: 
    print("Hora inválida! Use um valor entre 0 e 23.")


