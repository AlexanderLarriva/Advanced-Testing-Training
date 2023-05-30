import os
import pytest
import shutil
from extend_test.extend_test import get_function

prettify_html_file = get_function()


# Получаем путь до файла before
@pytest.fixture
def before_html_path():
    return os.path.join("tests", "fixtures", "before.html")


# Получаем путь до файла after
@pytest.fixture
def after_html_path():
    return os.path.join("tests", "fixtures", "after.html")


# Тестируем
def test_prettify_html_file(before_html_path, after_html_path):

    # Копируем исходный файл before.html для тестирования
    tmp_file_path = os.path.join("tests", "fixtures",
                                 "tmp", "prettify_test.html")
    shutil.copyfile(before_html_path, tmp_file_path)

    # Применяем функцию для форматирования и изменения файла
    prettify_html_file(tmp_file_path)

    # Проверяем, что файл был успешно изменен
    assert os.path.isfile(tmp_file_path)

    # Сравниваем содержимое измененного файла с
    # ожидаемым результатом (after.html)
    with open(tmp_file_path, "r") as f:
        result = f.read()
        with open(after_html_path, "r") as expected_file:
            expected_result = expected_file.read()
            assert result == expected_result
