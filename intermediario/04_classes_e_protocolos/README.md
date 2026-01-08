# 04. Classes e Protocolos

Python não é apenas orientado a objetos, ele é orientado a protocolos. Entender "Duck Typing" (se grasna como pato, é um pato) é essencial. Além disso, as novas Data Classes simplificam muito a criação de classes de dados.

## 📖 Referência: Python Fluente
- **Capítulo 13**: Interfaces, Protocolos e ABCs.
- **Capítulo 5**: Data Class Builders.

## 🛠️ Desafios

### Desafio 1: DataClass, a Salvadora
Antigamente, para criar uma classe simples para guardar dados de um "Livro" (titulo, autor, paginas), precisávamos de `__init__`, `__repr__`, `__eq__`, etc.
**Missão**: Crie uma classe `Livro` usando o decorador `@dataclass`.
Mostre como ela já vem com uma representação bonita (`print(livro)`) e comparação de igualdade (`livro1 == livro2`) "de graça".

### Desafio 2: O Poder do __len__ e __getitem__
Crie uma classe `Baralho` que representa um baralho de cartas.
Implemente os métodos especiais (dunder methods) `__len__` e `__getitem__`.
Ao fazer isso, mostre que agora você pode:
- Usar `len(baralho)`
- Acessar cartas com `baralho[0]`
- Iterar com `for carta in baralho`
- Escolher uma carta aleatória com `random.choice(baralho)`
Tudo isso sem herdar de nenhuma classe especial, apenas implementando o protocolo de sequência!

### Desafio 3: Classes Abstratas
Crie uma classe abstrata (ABC) chamada `Pagamento` com um método abstrato `processar()`.
Crie duas subclasses: `PagamentoCartao` e `PagamentoPix` que implementam esse método de formas diferentes.
Tente instanciar `Pagamento` diretamente e veja o que acontece.

---

## 🗣️ Discussão
- O que significa "Duck Typing" em Python?
- Por que dataclasses são preferíveis a tuplas ou dicionários para estruturar dados complexos?
