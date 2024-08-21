from decorators import log, my_function

def test_log_er():
    with pytest.raises(ZeroDivisionError):
        my_function(x:2, y:0)


def test_log(capsys):
    print(my_function(x:2, y:2))
    captured = capsys.readouterr()
    assert captured.out == "2.0\n"