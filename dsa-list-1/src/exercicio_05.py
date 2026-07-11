def famous_quote(author: str, quote: str) -> str:
    """
    Retorna uma frase com autor e citação.

    Args:
        author (str): nome do autor
        quote (str): citação

    Returns:
        str: "<author> once said, '<quote>'"
    """
    return f"{author} once said, '{quote}'"
