import os
import pytest
import shutil
from extend_test import get_function

prettify_html_file = get_function()


# BEGIN (write your solution here)
def test_prettify_html_file(tmp_path):
    # Создание временной директории
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    # Создание тестового файла
    file_path = test_dir / "test.html"
    with open(file_path, "w") as f:
        f.write("<div><p>Hello, <a href='https://hexlet.io'>Hexlet</a></p></div>")

    # Вызов функции prettify_html_file()
    prettify_html_file(file_path)

    # Проверка, что файл был изменен
    with open(file_path, "r") as f:
        result = f.read()
    expected = "<div>\n <p>\n  Hello,\n  <a href='https://hexlet.io'>Hexlet</a>\n </p>\n</div>"
    assert result == expected


prettify_html_file('/path/to/file')
# END
