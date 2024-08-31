import pytest
from src.decorators import log, func

def test_log_exseption(capsys):
        with open(func, 'r', encoding='utf-8') as file:
            logs = file.read()
        assert logs.out == "TypeError: expected str, bytes or os.PathLike object, not function\n"

def test_log_exposition(capsys):
    @log(filename="")
    def func(x,y):
        return x+y
    func(1, "2")
    captured = capsys.readouterr()
    assert captured.out == "TypeError: unsupported operand type(s) for +: 'int' and 'str'\n"