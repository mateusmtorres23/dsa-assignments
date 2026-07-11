-----

<p align="center">
  <img alt="upe" src="./img/upe-logo.png"/>
</p>

-----

# Lista 02 — Estruturas de Dados

Disciplina dos cursos de Engenharia de Software e Licenciatura em Computação  
da Universidade de Pernambuco — Campus Garanhuns

-----

## 📌 Sobre a lista

Nesta lista você irá implementar uma estrutura de dados baseada em um Tipo Abstrato de Dados (TAD) e aplicar algoritmos clássicos sobre ela.

Serão trabalhados os seguintes conceitos:

- Implementação de estruturas de dados
- Separação entre interface e implementação
- Manipulação de arrays
- Busca e ordenação
- Introdução a nós e listas encadeadas

Todas as soluções serão validadas por **testes automatizados com pytest**.

-----

## 🎯 Objetivos de aprendizagem

Ao finalizar esta lista, você deverá ser capaz de:

- Implementar uma estrutura de dados a partir de um contrato
- Manipular dados através de operações básicas (inserção, remoção, acesso)
- Implementar algoritmos de busca e ordenação
- Compreender o comportamento dos algoritmos na prática

-----

## 🧠 Regras importantes

Todas as implementações devem seguir obrigatoriamente:

- ❌ Não alterar a interface fornecida (`Array`)
- ❌ Não modificar os testes
- ✅ Implementar a classe `MyArray`
- ✅ Implementar os algoritmos solicitados
- ✅ Código deve passar nos testes e no linter

-----

## 📦 Entregáveis

<details>
  <summary><strong>📤 Como entregar</strong></summary><br />

### 🔹 Passo a passo da entrega

1. Faça um **fork** deste repositório para sua conta no GitHub  
2. Desenvolva a solução no **seu repositório (fork)**  
3. Ao finalizar, copie o link do seu repositório  
4. Envie o link como resposta no *Classroom* da disciplina  

### ⚠️ Importante

- A lista deve ser desenvolvida individualmente  
- Não é necessário abrir Pull Request neste repositório original, mas sim no seu `Fork`  
- A correção será feita a partir do link enviado

</details>

-----

## ⚙️ Configuração do ambiente

<details>
  <summary><strong>🚀 Passo a passo</strong></summary><br />

1. Faça o fork do repositório e clone o seu fork:

```bash
git clone <url-do-seu-fork>
cd lista-02
```

2. Crie o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
python3 -m pip install -r dev-requirements.txt
```

</details>

## Fluxo de desenvolvimento

<details> <summary><strong>🔧 Antes de começar</strong></summary><br />

1. Verifique se está na *branch* `main`:

```bash
git checkout main
```

2. Crie sua própria *branch*:

```bash
git checkout -b seu-nome-lista-02
```

</details> <details> <summary><strong>💻 Durante o desenvolvimento</strong></summary><br />

- Faça commits frequentes
- Use mensagens claras
- Execute os testes constantemente

Comandos mais usados:

```bash
git status
git add .
git commit -m "mensagem"
git push
```

</details>

## Estrutura da Lista de Exercícios

```bash
.
├── img
├── README.md
├── dev-requirements.txt
├── src
│   ├── exercicio_01.py
│   ├── exercicio_02.py
│   └── ...
├── tests
│   ├── test_exercicio_01.py
│   ├── test_exercicio_02.py
│   └── ...
```

## 🧪 Testes

Para executar os testes:

```bash
python3 -m pytest
```

Modo detalhado:

```bash
python3 -m pytest -s -vv
```

Executar teste específico:

```bash
python3 -m pytest tests/test_exercicio_01.py
```

## 🎛 Linter

Esta lista de exercícios utiliza Flake8 para padronização do código.

Execute:

```bash
python3 -m flake8
```

⚠️ Código fora do padrão não será considerado válido.

## 🧩 Exercícios

### 1 — Implementação do Array

> Implemente em `src/my_array.py`

Implemente a classe `MyArray`, que deve seguir o contrato definido na classe `Array`.

A estrutura deve armazenar **inteiros** e permitir operações básicas de manipulação de dados, como inserção, remoção, acesso e atualização.

📌 Requisitos

- A classe `MyArray` já está definida
- Todos os métodos da interface devem ser implementados
- Utilize a lista `self.data` como estrutura interna

-----

#### ⚠️ Restrições

- ❌ Não alterar a interface `Array` em `src/array.py`

-----

#### 🔧 Métodos obrigatórios

A classe deve implementar os seguintes métodos:

| Método                 | Descrição                  |
| ---------------------- | -------------------------- |
| `append(value)`        | Adiciona elemento ao final |
| `get(index)`           | Retorna elemento no índice |
| `set(index, value)`    | Atualiza valor no índice   |
| `remove(value)`        | Remove primeira ocorrência |
| `insert(index, value)` | Insere elemento no índice  |

-----

#### 🧠 Métodos Mágicos adicionais

Além dos métodos acima, implemente:

| Método                      | Descrição                                     |
| --------------------------- | --------------------------------------------- |
| `__len__()`                 | Permite uso de `len(array)`                   |
| `__getitem__(index)`        | Permite acesso com `array[index]`             |
| `__setitem__(index, value)` | Permite atribuição com `array[index] = value` |
| `__repr__()`                | Retorna representação do array                |

-----

#### Exemplo

```python
arr = MyArray()

arr.append(1)
arr.append(2)

len(arr) # 2
arr[0] # 1

arr[1] = 5
print(arr) # [1, 5]

arr.insert(1, 3)
print(arr) # [1, 3, 5]

arr.remove(3)
print(arr) # [1, 5]
```

### 2 — Busca Linear

> Implemente em `src/linear_search.py`

Implemente uma função de busca sobre a estrutura `MyArray`.

A função deve localizar um valor no array e retornar o índice correspondente.

-----

#### 📌 Requisitos

- A função deve se chamar `linear_search`
- Deve receber um `MyArray` e um valor inteiro como entrada
- Deve retornar o índice do elemento, caso encontrado e `-1` caso não o encontre

-----

#### 🔧 Assinatura esperada

```python
def linear_search(array: MyArray, target: int) -> int:
```

#### Exemplo

```python
arr = MyArray()

arr.append(10)
arr.append(20)
arr.append(30)

linear_search(arr, 20) # 1
linear_search(arr, 99) # -1
```

### 3 — Busca Binária

> Implemente em `src/binary_search.py`

Implemente uma função de busca binária sobre a estrutura `MyArray`.

A busca binária deve ser realizada sobre um array **ordenado em ordem crescente**.

#### 📌 Requisitos

- A função deve se chamar `binary_search`
- Deve receber um `MyArray` e um valor inteiro como entrada
- Deve retornar o índice do elemento, caso encontrado e `-1` caso contrário

#### 🔧 Assinatura esperada

```python
def binary_search(array: MyArray, target: int) -> int:
```

#### Exemplo

```python
arr = MyArray()

arr.append(1)
arr.append(3)
arr.append(5)
arr.append(7)

binary_search(arr, 5) # 2
binary_search(arr, 2) # -1
```

### 4 — Nó

> Implemente em `src/node.py`

Implemente a classe `Node`, que representa um elemento de uma estrutura encadeada.

Cada nó deve armazenar um valor inteiro e uma referência para o próximo nó.

-----

#### 📌 Requisitos

- A classe deve se chamar `Node`
- Deve possuir dois atributos:
  - `value`: valor armazenado no nó
  - `next`: referência para o próximo nó (ou `None`)

#### Exemplo

```python
n1 = Node(1)
n2 = Node(2)

n1.next = n2

n1.value # 1
n1.next.value # 2
```

### 🧠 Observações finais

- Leia os testes com atenção — eles definem o comportamento esperado
- Pequenos erros de lógica podem quebrar vários testes
- Pense sempre em: entrada → processamento → saída
- Não é permitido alterar os arquivos em `tests/`
- Alterações nos testes irão reprovar automaticamente no CI

📚 Referência

- [Entendendo Algoritmos — Aditya Bhargava](https://www.amazon.com.br/Entendendo-Algoritmos-Ilustrado-Programadores-Curiosos/dp/8575225634/)
- [Material da disciplina](https://github.com/casm3/algoritmos-e-estruturas-de-dados)
