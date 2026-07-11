from src.exercicio_13 import shrink_guest_list


def test_shrink_guest_list():
    guests = ["Ana", "João", "Carlos", "Maria"]
    result = shrink_guest_list(guests)
    assert len(result) == 2
    guests = ["Ana", "João"]
    result = shrink_guest_list(guests)
    assert len(result) == 2
    guests = ["Ana", "João", "Maria"]
    result = shrink_guest_list(guests)
    assert len(result) == 2
