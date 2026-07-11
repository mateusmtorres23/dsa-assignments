from src.exercicio_11 import modify_guest_list


def test_modify_guest_list():
    guests = ["Ana", "João", "Carlos"]
    result = modify_guest_list(guests, "João", "Maria")
    assert "Maria" in result
    assert "João" not in result
