import pytest
from src.decorators import log, func

def test_log_exseption(capsys):
        with open(func, 'r', encoding='utf-8') as file:
            logs = file.read()
        assert "my function error: unsupported operand type(s) for +: 'int' and 'str'. inputs: (1, '2'), {}" in logs

def test_log_exposition(capsys):
    @log(filename="")
    def func(x,y):
        return x+y
    func(1, "2")
    captured = capsys.readouterr()
    assert "TypeError: unsupported operand type(s) for +: 'int' and 'str'" in captured.out