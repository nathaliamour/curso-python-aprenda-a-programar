# 03. Iteradores e Geradores

Processar dados grandes sem estourar a memória do computador é uma arte. Em Python, iteradores e geradores são a chave para o "Lazy Evaluation" (Avaliação Preguiçosa): calcule apenas o que precisa, quando precisa.

## 📖 Referência: Python Fluente
- **Capítulo 17**: Iteradores, Geradores e Corrotinas Clássicas.

## 🛠️ Desafios

### Desafio 1: O Gerador Infinito
Crie um gerador chamado `fibonacci()` que retorna os números da sequência de Fibonacci **infinitamente** (use `yield`).
Depois, use esse gerador para imprimir os primeiros 20 números da sequência.
*Nota: Se você usar uma lista para isso, eventualmente ficaria sem memória. Com geradores, você pode ir até o infinito!*

### Desafio 2: Pipeline de Processamento
Imagine que você tem uma lista gigante de números (simulada por um `range(1000000)`).
Crie um pipeline usando **Generator Expressions** (sem criar listas intermediárias) que:
1. Pegue todos os números.
2. Filtre apenas os pares.
3. Eleve esses pares ao quadrado.
4. Some tudo no final.
Verifique o consumo de memória versus fazer isso com listas.

### Desafio 3: Iterador Customizado
Crie uma classe `ContagemRegressiva` que funcione como um iterador.
Ela deve receber um número inicial e, a cada iteração (`next()`), retornar o número anterior até chegar a zero.
Quando chegar a zero, deve lançar `StopIteration`.
Teste usando um loop `for`.

---

## 🗣️ Discussão
- Qual a vantagem do `yield` sobre o `return`?
- O que acontece se você tentar iterar sobre um gerador duas vezes?
