from abc import ABC, abstractmethod


class Array(ABC):
    """
    Interface para um TAD de Array.

    Este TAD define uma coleção ordenada de números inteiros,
    acessível por índice e que permite inserção, remoção e
    atualização de elementos.
    """

    @abstractmethod
    def append(self, value: int) -> None:
        """
        Adiciona elemento ao final do array
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, index: int) -> int:
        """
        Retorna o elemento no índice, deve lançar
        IndexError se o índice for inválido
        """
        raise NotImplementedError

    @abstractmethod
    def set(self, index: int, value: int) -> None:
        """
        Atualiza o valor de um elemento no índice.
        Deve lançar IndexError se o índice for inválido.
        """
        raise NotImplementedError

    @abstractmethod
    def remove(self, value: int) -> None:
        """
        Remove a primeira ocorrência do valor no array.
        Deve lançar ValueError se o valor não existir.
        """
        raise NotImplementedError

    @abstractmethod
    def insert(self, index: int, value: int) -> None:
        """
        Insere um elemento no índice especificado,
        deslocando os elementos à direita.

        Deve lançar IndexError se o índice for inválido.
        """
        raise NotImplementedError
