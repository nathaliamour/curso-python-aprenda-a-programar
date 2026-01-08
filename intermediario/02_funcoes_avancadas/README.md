# 02. Funções Avançadas

Em Python, funções são "Cidadãos de Primeira Classe". Elas podem ser atribuídas a variáveis, passadas como argumentos e retornadas por outras funções.

## 📖 Referência: Python Fluente
- **Capítulo 7**: Funções como objetos de primeira classe.
- **Capítulo 9**: Decoradores e Closures.

## 🛠️ Desafios

### Desafio 1: Ordenação Customizada
Temos uma lista de dicionários:
```python
pessoas = [
    {"nome": "João", "idade": 25},
    {"nome": "Maria", "idade": 30},
    {"nome": "Pedro", "idade": 20}
]
```
**Missão**: Use a função `sorted` ou o método `.sort()` com o parâmetro `key` e uma função **lambda** para ordenar essa lista pela **idade**.

### Desafio 2: Factory de Funções
Crie uma função chamada `criador_multiplicador(n)`.
Ela deve retornar **uma nova função** que sempre multiplica o argumento por `n`.
Exemplo de uso:
```python
dobrar = criador_multiplicador(2)
triplicar = criador_multiplicador(3)
print(dobrar(5))  # Deve imprimir 10
print(triplicar(5)) # Deve imprimir 15
```

### Desafio 3: O Decorador de Tempo
Crie um **decorador** chamado `@timer` que mede o tempo que uma função leva para executar e imprime esse tempo no console.
Aplique-o em uma função que demora um pouco (use `time.sleep` para simular).

---

## 🗣️ Discussão
- Quando usar uma função normal (def) e quando usar uma lambda?
- Como funcionam os *decorators* "por baixo dos panos"? (Dica: pesquise sobre closures).
