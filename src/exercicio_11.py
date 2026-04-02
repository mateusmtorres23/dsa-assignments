def modify_guest_list(
    guests: list[str],
    unavailable: str,
    new_guest: str
) -> list[str]:
    """
    Substitui um convidado indisponível por outro.

    Args:
        guests (list[str]): lista original
        unavailable (str): convidado a ser removido
        new_guest (str): novo convidado

    Returns:
        list[str]: lista atualizada
    """
    if unavailable in guests:
        index = guests.index(unavailable)
        guests[index] = new_guest
    return guests
