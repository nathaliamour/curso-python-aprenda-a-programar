### Desafio 3: Verificador de Palíndromos
#Um palíndromo é uma palavra que se lê igual de trás para frente (ex: "ovo", "arara").
#Crie uma função `eh_palindromo(palavra)` que retorne `True` se for palíndromo e `False` caso contrário.
#Teste com a palavra "python" e com "anilina".
def eh_palindromo(palavra):
    invertida = ""

    for letra in palavra:
        invertida = letra + invertida

    if palavra == invertida:
        return True
    else:
        return False
    
palavra = input("Digite a palavra a ser verificada: ")
print (eh_palindromo(palavra))


