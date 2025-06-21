from src.decorators import log


def test_log(capsys):
    """Тестирует логирование в консоль"""

    @log()
    def add(a, b):
        return a + b
    result = add(2, 3)
    captured = capsys.readouterr()
    assert "add started" in captured.out
    assert "add finished" in captured.out
    assert "Result: 5" in captured.out
    assert result == 5


def test_log2(tmp_path):
    """Тестирует логирование в файл"""
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b
    result = multiply(3, 4)
    assert log_file.exists()
    with open(log_file, 'r') as f:
        content = f.read()
        assert "multiply started" in content
        assert "multiply finished" in content
        assert "Result: 12" in content
    assert result == 12
