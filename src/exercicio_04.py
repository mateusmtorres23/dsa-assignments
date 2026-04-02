def format_name(name: str) -> tuple[str, str, str]:
    """
    Retorna o nome em diferentes formatos.

    Args:
        name (str): nome de entrada

    Returns:
        tuple[str, str, str]: (lowercase, uppercase, titlecase)
    """
    return (name.lower(), name.upper(), name.title())
