# 📘 Assignment: Automated Testing with pytest

## 🎯 Objetivo

Practice writing automated tests with pytest, checking expected behavior and edge cases for small Python functions.

## 📝 Tarefa

### 🛠️ Write Your First Tests

#### Descrição
Use the provided `text_utils.py` module. Create a file named `test_text_utils.py` and write tests for `count_words()`. The function counts words separated by whitespace; an empty or whitespace-only string has zero words.

#### Requisitos
O programa concluído deve:

- Include at least three tests for `count_words()`, including an empty string and a sentence with multiple words
- Use `assert` statements to check the expected results
- Run successfully with `python -m pytest`

### 🛠️ Test Text Behavior

#### Descrição
Add tests for `is_palindrome()`. It ignores letter case and whitespace, but punctuation remains part of the text. An empty or whitespace-only string counts as a palindrome.

#### Requisitos
O programa concluído deve:

- Test a palindrome with mixed letter case
- Test a palindrome that includes whitespace
- Test a string that is not a palindrome
- Check the documented behavior for an empty or whitespace-only string

### 🛠️ Cover Multiple Cases with Parametrization

#### Descrição
Use `pytest.mark.parametrize` to check several inputs and expected results with a single test function. Include ordinary inputs and edge cases for both utility functions.

#### Requisitos
O programa concluído deve:

- Use `pytest.mark.parametrize` for at least one function
- Include multiple input-and-expected-result pairs
- Keep the tests passing when run with `python -m pytest`

To install pytest if it is not already available, run `python -m pip install pytest`.