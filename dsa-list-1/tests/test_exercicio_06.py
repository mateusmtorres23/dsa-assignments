from src.exercicio_06 import clean_name


def test_clean_name():
    assert clean_name("  Carlos  ") == "Carlos"
    assert clean_name("Maria") == "Maria"
    assert clean_name(" Pedro") == "Pedro"
    assert clean_name("João ") == "João"
