from src.exercicio_07 import calculate_eight


def test_calculate_eight_structure():
    result = calculate_eight()

    assert isinstance(result, list), "O retorno deve ser uma lista"
    assert len(result) == 4, "A lista deve conter exatamente 4 elementos"

    for expr in result:
        assert isinstance(expr, str), "Cada elemento deve ser uma string"


def test_calculate_eight_result():
    result = calculate_eight()

    for expr in result:
        try:
            value = eval(expr)
        except Exception:
            assert False, f"Expressão inválida: {expr}"

        assert value == 8, f"A expressão '{expr}' não resulta em 8"


def test_calculate_eight_operators():
    result = calculate_eight()

    operators_found = set()

    for expr in result:
        if "+" in expr:
            operators_found.add("+")
        if "-" in expr:
            operators_found.add("-")
        if "*" in expr:
            operators_found.add("*")
        if "/" in expr:
            operators_found.add("/")

    assert len(operators_found) == 4, (
        "Deve haver pelo menos duas operações diferentes entre as expressões"
    )
