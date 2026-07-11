from src.exercicio_12 import add_guests


def test_add_guests():
    guests = ["Ana"]
    new_guests = ["João", "Carlos"]
    result = add_guests(guests, new_guests)
    assert result == ["Ana", "João", "Carlos"]
