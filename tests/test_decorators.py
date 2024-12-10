import logging
import os
import sys

import pytest

from src.decorators import log


@pytest.fixture
def clear_log_file(request):
    filename = request.node.get_closest_marker('log_file').args[0]
    if os.path.exists(filename):
        os.remove(filename)

@pytest.mark.parametrize("filename, expected_output", [
    (None, "my_function ok\n"),
    ("mylog.txt", "my_function ok\n")
])
def test_log_decorator_success(clear_log_file, filename, expected_output):
    @log(filename=filename)
    def my_function(x, y):
        return x + y

    if filename:
        my_function(1, 2)
        with open(filename, 'r') as f:
            assert f.read() == expected_output
    else:
        captured = capsys.readouterr()
        assert captured.out == expected_output

@pytest.mark.parametrize("filename, expected_output", [
    (None, "my_function error: ZeroDivisionError. Inputs: (1, 0), {}\n"),
    ("mylog.txt", "my_function error: ZeroDivisionError. Inputs: (1, 0), {}\n")
])
def test_log_decorator_error(clear_log_file, filename, expected_output):
    @log(filename=filename)
    def my_function(x, y):
        return x / y

    if filename:
        with pytest.raises(ZeroDivisionError):
            my_function(1, 0)
        with open(filename, 'r') as f:
            assert f.read() == expected_output
    else:
        with pytest.raises(ZeroDivisionError):
            my_function(1, 0)
        captured = capsys.readouterr()
        assert captured.out == expected_output
