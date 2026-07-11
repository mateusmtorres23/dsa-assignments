-----

<p align="center">
  <img alt="upe" src="./img/upe-logo.png"/>
</p>

-----

# Lista 01 — Algoritmos e Estruturas de Dados

Disciplina dos cursos de Engenharia de Software e Licenciatura em Computação  
da Universidade de Pernambuco — Campus Garanhuns

-----

## 📌 Sobre a lista

Nesta lista você irá implementar funções em Python com foco nos conceitos iniciais de algoritmos:

- Entrada → processamento → saída
- Manipulação de *strings*
- Operações com números
- Listas
- Estruturas básicas de repetição e decisão
- Escrita de funções

Além disso, todas as soluções serão validadas por **testes automatizados com pytest**.

-----

## 🎯 Objetivos de aprendizagem

Ao finalizar esta lista, você deverá ser capaz de:

- Escrever funções em Python
- Resolver problemas de forma algorítmica
- Manipular diferentes tipos de dados
- Interpretar e corrigir testes automatizados
- Organizar código seguindo boas práticas

-----

## 🧠 Regras importantes

Todas as implementações devem seguir obrigatoriamente:

- ❌ Não utilizar `input()`
- ❌ Não utilizar `print()`
- ✅ Utilizar funções
- ✅ Retornar valores
- ✅ Código deve passar nos testes

-----

## 📦 Entregáveis

<details>
  <summary><strong>📤 Como entregar</strong></summary><br />

- A lista deve ser desenvolvida individualmente
- Você deverá criar uma branch no repositório
- A entrega será feita via **Pull Request (PR)**
- O link do seu repositório deve ser disponibilizado como resposta na *thread* da lista de exercícios no classroom da disciplina

</details>

-----

## ⚙️ Configuração do ambiente

<details>
  <summary><strong>🚀 Passo a passo</strong></summary><br />

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd lista-01
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
git checkout -b seu-nome-lista-01
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

### 🟢 Básico

#### 1 - Hello World

Implemente a função `hello_world()`

> Retorne a string padrão de saudação.

**Saída esperada:**

```bash
"Hello, World!"
```

#### 2 - Mensagem simples

> Recebe uma string e retorna exatamente a mesma string.

**Exemplo:**

> Para a entrada: "Hello, World!"

**Saída esperada:**

```bash
"Hello, World!"
```

#### 3 - Mensagem personalizada

> Recebe um nome e retorna uma saudação.

**Exemplo:**

> Para a entrada: "Carlos"

**Saída esperada:**

```bash
"Hello, Carlos!"
```

#### 4 - Formatação de nome

> Retorne o nome em três formatos:
>> minúsculo
>> maiúsculo
>> capitalizado

**Exemplo:**

> Para a entrada: "Carlos"

**Saída esperada:**

```bash
("carlos", "CARLOS", "Carlos")
```

### 🟡 Intermediário

#### 5 - Citação famosa

> Monte uma frase com autor e citação.

**Exemplo:**

> Para a entrada: ("Einstein", "Imagination is more important than knowledge")

**Saída esperada:**

```bash
"Einstein once said, 'Imagination is more important than knowledge'"
```

#### 6 - Limpeza de nome

> Remova espaços em branco no início e no fim da string.

**Exemplo:**

> Para a entrada: " Carlos "

**Saída esperada:**

```bash
"Carlos"
```

#### 7 - Operações que resultam em 8

> Retorne uma lista com quatro resultados iguais a 8 usando operações diferentes.

**Saída esperada:**

```bash
[8, 8, 8, 8]
```

#### 8 - Número favorito

> Retorne uma frase com o número favorito.

**Exemplo:**

> Para a entrada: 7

**Saída esperada:**

```bash
"Your favorite number is 7"
```

#### 9 - Número par

> Retorne True se o número for par, False caso contrário.

**Exemplo:**

> Para a entrada: 4

**Saída esperada:**

```bash
True
```

### 🔵 Listas

#### 10 - Saudações

> Recebe uma lista de nomes e retorna uma nova lista com mensagens.

**Exemplo:**

> Para a entrada: ["Ana", "João"]

**Saída esperada:**

```bash
["Hello, Ana!", "Hello, João!"]
```

### 🟣 Manipulação de listas

#### 11 - Modificar lista de convidados

> Substitua um convidado indisponível por outro.

**Exemplo:**

> Para a entrada: (["Ana", "João", "Pedro"], "Ana", "Maria")

**Saída esperada:**

```bash
["Maria", "João", "Pedro"]
```

#### 12 - Adicionar convidados

> Implemente a função que permite adicionar multiplos convidados à lista

**Exemplo:**

> Para a entrada: (["Ana", "João", "Pedro"], ["Thiago", "Maria"])

**Saída esperada:**

```bash
["Ana", "João", "Pedro", "Thiago", "Maria"]
```

#### 13 - Reduza a lista de convidados

> Reduza a lista para apenas 2 elementos e retorne o resultado.

**Exemplo:**

> Para a entrada: ["Ana", "João", "Pedro"]

**Saída esperada:**

```bash
["Ana", "João"]
```

### 🔴 Lógica e repetição

#### 14 - Gerar números

> Retorne uma lista de 1 até n.

**Exemplo:**

> Para a entrada: 5

**Saída esperada:**

```bash
[1, 2, 3, 4, 5]
```

#### 15 - Soma de números

> Retorne a soma dos números de 1 até n.

**Exemplo:**

> Para a entrada: 5

**Saída esperada:**

```bash
15
```

#### 16 - Números ímpares

> Retorne uma lista com os números ímpares até n.

**Exemplo:**

> Para a entrada: 7

**Saída esperada:**

```bash
[1, 3, 5, 7]
```

### 🧠 Observações finais

- Leia os testes com atenção — eles definem o comportamento esperado
- Pequenos erros de lógica podem quebrar vários testes
- Pense sempre em: entrada → processamento → saída
- Não é permitido alterar os arquivos em `tests/`
- Alterações nos testes irão reprovar automaticamente no CI

📚 Referência

- [Python Crash Course — Eric Matthes](https://www.amazon.com.br/Python-Crash-Course-Eric-Matthes/dp/1718502702/)
- [Material da disciplina](https://github.com/casm3/algoritmos-e-estruturas-de-dados)
