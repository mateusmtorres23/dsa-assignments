def clean_name(name: str) -> str:
    """
    Remove espaços em branco no início e no fim da string.

    Args:
        name (str): nome com possíveis espaços extras

    Returns:
        str: nome sem espaços nas extremidades
    """
    return name.strip()
