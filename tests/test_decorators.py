import pytest
from src.decorators import my_function, log, timer

def test_my_function():
    with pytest.raises(ZeroDivisionError):
        my_function(x:2, y:0)


def test_log(capsys):
    print(my_function(x:2, y:2))
    captured = capsys.readouterr()
    assert captured.out == "2.0\n"


def test_log_exposition(capsys):
    @log(filename="")
    def func(x,y):
        return x+y
    func(x:1, y:"2")
    captured = capsys.readouterr()
    assert "TypeError: unsupported operand type(s) for +: 'int' and 'str" in captured.out