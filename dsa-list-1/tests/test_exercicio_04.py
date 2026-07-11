from src.exercicio_04 import format_name


def test_format_name():
    assert format_name("carlos") == ("carlos", "CARLOS", "Carlos")
    assert format_name("maria") == ("maria", "MARIA", "Maria")
