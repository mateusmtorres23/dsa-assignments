from src.exercicio_05 import famous_quote


RESULTS = [
    "Einstein once said, ",
    "'Imagination is more important than knowledge'",
    "Steve Jobs once said, ",
    "'The only way to do great work is to love what you do'"
]


def test_famous_quote():
    result = famous_quote(
        "Einstein",
        "Imagination is more important than knowledge"
        )
    assert result == RESULTS[0] + RESULTS[1]
    result = famous_quote(
        "Steve Jobs",
        "The only way to do great work is to love what you do")
    assert result == RESULTS[2] + RESULTS[3]
