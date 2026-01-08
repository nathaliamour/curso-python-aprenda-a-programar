# 04. Funções

Repetir código é ruim. Funções permitem agrupar lógica e reutilizá-la, tornando seus programas organizados e modulares.

## 📖 Leitura Recomendada

- [Definindo Funções](https://docs.python.org/pt-br/3.14/tutorial/controlflow.html#defining-functions)
- [Mais sobre Funções](https://docs.python.org/pt-br/3.14/tutorial/controlflow.html#more-on-defining-functions)

## 🛠️ Desafios

### Desafio 1: Saudação Personalizada
Crie uma função chamada `saudacao(nome, hora)` que receba um nome e uma hora (0-23).
- Se for entre 5 e 11, imprima "Bom dia, [nome]!".
- Se for entre 12 e 17, imprima "Boa tarde, [nome]!".
- Senão, imprima "Boa noite, [nome]!".

### Desafio 2: Calculadora Modular
Relembra da calculadora? Agora crie funções para cada operação: `soma`, `subtracao`, `multiplicacao`, `divisao`.
Peça ao usuário os números e a operação desejada, e chame a função correspondente.

### Desafio 3: Verificador de Palíndromos
Um palíndromo é uma palavra que se lê igual de trás para frente (ex: "ovo", "arara").
Crie uma função `eh_palindromo(palavra)` que retorne `True` se for palíndromo e `False` caso contrário.
Teste com a palavra "python" e com "anilina".

---

## 🧘 Reflexão
- Qual a diferença entre imprimir um valor (`print`) e retornar um valor (`return`) em uma função?
- O que são parâmetros padrões em funções?
