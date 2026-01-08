# 01. Código Pythonico e Idiomas

Escrever Python como se fosse C ou Java funciona, mas ignora o poder da linguagem. Código Pythonico é conciso, claro e expressivo.

## 📖 Referência: Python Fluente
- **Capítulo 2**: Uma coleção de sequências (foco em List Comprehensions e Generator Expressions).
- **Capítulo 8**: Referências, Mutabilidade e Reciclagem (foco em cópias e identidade).

## 🛠️ Desafios

### Desafio 1: Adeus Loop C-style
Você encontrou este código legado em um projeto:
```python
numeros = [1, 2, 3, 4, 5]
quadrados = []
for i in range(len(numeros)):
    quadrados.append(numeros[i] ** 2)
```
**Missão**: Refatore este código usando **List Comprehension**. Torne-o uma única linha elegante.
**Extra**: E se quisermos apenas os quadrados dos números pares? Adicione essa condição na sua comprehension.

### Desafio 2: Desempacotamento Inteligente
Temos uma lista de tuplas representando produtos: `produtos = [("Maçã", 5.00), ("Banana", 3.50), ("Laranja", 4.20)]`.
Use um loop `for` com **desempacotamento de tuplas** (tuple unpacking) para imprimir apenas os nomes e preços, sem usar índices como `produto[0]`.

### Desafio 3: O Mistério da Mutabilidade
Analise e execute o seguinte código:
```python
lista_a = [1, 2, 3]
lista_b = lista_a
lista_a.append(4)
print(lista_b)
```
Por que a `lista_b` mudou?
**Missão**: Crie uma versão onde `lista_b` seja uma **cópia independente** de `lista_a`. Mostre duas formas de fazer isso.

---

## 🗣️ Discussão
- List Comprehensions são sempre melhores? Quando elas podem prejudicar a legibilidade?
- O que é *Shallow Copy* vs *Deep Copy*?
