-----

<p align="center">
  <img alt="upe" src="./img/upe-logo.png"/>
</p>

-----

# Lista 03 — Algoritmos de Ordenação e Estruturas de Dados Lineares

Disciplina dos cursos de Engenharia de Software e Licenciatura em Computação  
da Universidade de Pernambuco — Campus Garanhuns

-----

## 📌 Sobre a lista

Nesta lista você irá resolver problemas clássicos de algoritmos e estruturas de dados, utilizando as estruturas já implementadas nas listas anteriores.

O foco desta lista está no desenvolvimento do raciocínio algorítmico, na manipulação de estruturas de dados lineares e na construção de soluções corretas e eficientes.

Serão trabalhados os seguintes conceitos:

- Resolução de problemas clássicos de algoritmos
- Manipulação de arrays e listas encadeadas
- Uso de pilhas na validação de expressões
- Algoritmos de ordenação (Merge e Quick Sort)
- Análise implícita de eficiência (tempo de execução)

Todas as soluções serão validadas por **testes automatizados com pytest**.

-----

## 🎯 Objetivos de aprendizagem

Ao finalizar esta lista, você deverá ser capaz de:

- Resolver problemas clássicos utilizando estruturas de dados
- Aplicar algoritmos sobre arrays, pilhas e listas encadeadas
- Desenvolver soluções corretas para diferentes cenários e entradas
- Manipular estruturas de dados de forma eficiente
- Compreender, na prática, o comportamento de algoritmos em termos de execução

-----

## 🧠 Regras importantes

Todas as implementações devem seguir obrigatoriamente:

- ❌ Não modificar os testes
- ❌ Não utilizar funções prontas da linguagem que resolvam diretamente o problema (ex.: `.sort()`, `.reverse()`, etc.)
- ❌ Não utilizar estruturas de dados não abordadas em sala (ex.: `dict`, `set`, etc.)
- ✅ Implementar todas as funções solicitadas respeitando suas assinaturas
- ✅ Código deve passar em todos os testes automatizados
- ✅ Código deve seguir o padrão definido pelo linter (`Flake8`)
- ⚠️ Funções devem lidar corretamente com casos extremos (listas vazias, valores nulos, etc.)

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
cd lista-03
```

2. Crie o ambiente virtual:

> Exemplo em Linux/WSL

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
git checkout -b seu-nome-lista-03
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

### 1 — Reverse Array

> Implemente em `src/reverse_array.py`

Implemente uma função que receba um array e retorne o array com os elementos em ordem inversa.

A inversão deve ser feita sem utilizar funções prontas da linguagem, manipulando diretamente os elementos do array.

-----

#### ⚠️ Restrições

- ❌ Não utilizar métodos prontos como `.reverse()` ou *slicing* `([::-1])`
- ❌ Não criar uma nova lista auxiliar (a inversão deve ser *in-place*)

#### 💡 Exemplos de uso

```python
reverse_array([1, 2, 3]) -> [3, 2, 1]

reverse_array([5]) -> [5]

reverse_array([]) -> []
```

> Dica: Se você trocar os elementos das extremidades do array até atingir o centro a sua solução poderá reduzir o tempo de execução pela metade

### 2 — Two Sum

> Implemente em `src/two_sum.py`

Implemente uma função que receba um array de inteiros e um valor alvo (`target`), e retorne os índices de dois elementos cuja soma seja igual ao valor alvo. Caso não seja encontrado índice retorne `-1`.

A solução deve ser implementada sem utilizar estruturas auxiliares como dicionários (`dict`) ou conjuntos (`set`)

#### 💡 Exemplos de uso

```python
# 2 + 7 = 9
two_sum([2, 7, 11, 15], 9) -> (0, 1)

# 2 + 4 = 6
two_sum([3, 2, 4], 6) -> (1, 2)

# Não há dois números que somados retornem 7
two_sum([1, 2, 3], 7) -> (-1, -1)
```

### 3 — Validação de Parênteses

> Implemente em `src/valid_parentheses.py`

Dada uma string contendo apenas os caracteres `(`, `)`, `{`, `}`, `[` e `]`, implemente uma função que determine se a sequência de parênteses está corretamente balanceada.

Uma sequência é considerada válida quando:

- Todo símbolo de abertura possui um símbolo de fechamento correspondente
- Os símbolos estão corretamente aninhados

#### ⚠️ Restrições

- ❌ Não utilizar listas nativas (`list`) como pilha diretamente
- ❌ Não utilizar bibliotecas prontas
- ❌ Não utilizar estruturas não vistas em aula
- ✅ Utilize a classe `Stack` implementada anteriormente

#### 💡 Exemplos de uso

```python
is_valid_parentheses("()") -> True
is_valid_parentheses("()[]{}") -> True
is_valid_parentheses("(]") -> False
is_valid_parentheses("([)]") -> False
is_valid_parentheses("{[]}") -> True
```

### 4 — Inverter uma Lista Encadeada

> Implemente em `src/reverse_linked_list.py`

Dada a referência para o primeiro nó de uma lista encadeada, implemente uma função que inverta a ordem dos elementos da lista.

#### ⚠️ Restrições

- ❌ Não criar uma nova lista encadeada
- ❌ Não utilizar estruturas auxiliares (`listas`, `arrays`, etc.)
- ✅ A inversão deve ser feita apenas manipulando os ponteiros (`next`)
- ✅ A função deve retornar o novo `head` da lista

#### 💡 Exemplos de uso

```bash
1 -> 2 -> 3 -> None

reverse_linked_list

3 -> 2 -> 1 -> None
```

### 5 — Detectar Ciclo em Lista Encadeada

> Implemente em `src/has_cycle.py`

Dada a referência para o primeiro nó de uma lista encadeada, implemente uma função que determine se a lista possui um ciclo.

Um ciclo ocorre quando um nó aponta para um nó anterior na lista, formando um loop infinito.

#### ⚠️ Restrições

- ❌ Não utilizar estruturas auxiliares (`listas`, `arrays`, etc.)
- ❌ Não modificar a lista encadeada
- ✅ Utilize apenas manipulação de ponteiros
- ✅ A solução deve ter complexidade O(n)

#### 💡 Exemplos de uso

```bash
1 -> 2 -> 3 -> None # False

1 -> 2 -> 3 # True
     ↑    ↓
     ← ← ← 
```

### 6 — Remover Duplicatas em Lista Encadeada

> Implemente em `src/remove_duplicates.py`

Dada a referência para o primeiro nó de uma lista encadeada, implemente uma função que remova os elementos duplicados da lista.

A remoção deve manter apenas a primeira ocorrência de cada valor.

#### ⚠️ Restrições

- ❌ Não utilizar estruturas auxiliares (`dict`, `set`, etc.)
- ❌ Não criar uma nova lista encadeada
- ✅ Utilize apenas manipulação de ponteiros
- ✅ A solução deve retornar o `head` da lista modificada

#### 💡 Exemplos de uso

```bash
# Mantém a primeira ocorrência
1 -> 2 -> 2 -> 3 -> None
1 -> 2 -> 3 -> None

1 -> 1 -> 1 -> None
1 -> None

# Não tem duplicata
1 -> 2 -> 3 -> None
1 -> 2 -> 3 -> None
```

### 7 — Moonwalk

> Implemente em `src/kth_to_last.py`

Dada a referência para o primeiro nó de uma lista encadeada e um inteiro `k`, implemente uma função que retorne o k-ésimo elemento a partir do final da lista.

#### ⚠️ Restrições

- ❌ Não utilizar estruturas auxiliares (`dict`, `set`, etc.)
- ❌ Não criar uma nova lista encadeada
- ✅ Utilize apenas manipulação de ponteiros
- ✅ A solução deve ter complexidade O(n)

#### 💡 Exemplos de uso

```bash
Lista: 1 -> 2 -> 3 -> 4 -> 5

k = 1 → 5
k = 2 → 4
k = 5 → 1
k = 6 → -1
```

### 8 — Misturando Listas Encadeadas

> Implemente em `src/merge_lists.py`

Dada duas listas encadeadas ordenadas, implemente uma função que intercale seus elementos formando uma única lista encadeada ordenada.

#### ⚠️ Restrições

- ❌ Não utilizar estruturas auxiliares (`dict`, `set`, etc.)
- ❌ Não criar uma novos nós
- ✅ Reutilizar os nós existentes
- ✅ Manipular apenas os ponteiros

#### 💡 Exemplos de uso

```bash
lista1: 1 -> 3 -> 5
lista2: 2 -> 4 -> 6

1 -> 2 -> 3 -> 4 -> 5 -> 6 # Mistura
```

### 9 — Merge Sort

> Implemente em `src/merge_sort.py`

Implemente o algoritmo Merge Sort para ordenar um array de inteiros. O algoritmo deve seguir a abordagem de divisão e conquista:

1. Dividir o array em duas partes
2. Ordenar recursivamente cada parte
3. Intercalar as partes ordenadas

#### ⚠️ Restrições

- ❌ Não utilizar métodos prontos como `.sort()`
- ✅ Utilize recursão
- ✅ A função deve retornar o array ordenado

#### 💡 Exemplos de uso

```bash
merge_sort([3, 1, 2]) -> [1, 2, 3]

merge_sort([5, 4, 3, 2, 1]) -> [1, 2, 3, 4, 5]

merge_sort([]) -> []
```

### 10 — Quick Sort

> Implemente em `src/quick_sort.py`

Implemente o algoritmo Quick Sort para ordenar um array de inteiros. O algoritmo deve selecionar um elemento como pivô e reorganizar o array de forma que:

1. Elementos menores que o pivô fiquem à esquerda
2. Elementos maiores que o pivô fiquem à direita

Em seguida, o processo deve ser aplicado recursivamente às duas partes.

#### ⚠️ Restrições

- ❌ Não utilizar métodos prontos como `.sort()`
- ✅ Utilize recursão
- ✅ A função deve retornar o array ordenado in-place

#### 💡 Exemplos de uso

```bash
quick_sort([3, 1, 2]) -> [1, 2, 3]

quick_sort([5, 4, 3, 2, 1]) -> [1, 2, 3, 4, 5]

quick_sort([]) -> []
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
