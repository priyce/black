import sys

# setting path
sys.path.append('../black')

# importing
from src import black
from tokenize_rt import Token
import pytest

def test_base_case1():
    expected = "if not (a and b):\n    pass"
    result = black.remove_redundant_parentheses("if not ((a and b)):\n    pass")
    assert result == expected
    print (result)

def test_base_case2():
    expected = "if (a and b) or c:\n    pass"
    input1 = "if (((a and b) or c)):\n    pass"
    input2 = "if (((a and b)) or c):\n    pass"
    result1 = black.remove_redundant_parentheses(input1)
    result2 = black.remove_redundant_parentheses(input2)
    assert result1 == result2
    assert result2 == expected

def test_base_case3():
    expected = "funct()"
    result = black.remove_redundant_parentheses("funct()")
    assert result == expected

def test_base_case4():
    expected = "funct(a)"
    result = black.remove_redundant_parentheses("funct(a)")
    assert result == expected

def test_instruction_with_line_break():
    expected = "if (a and \n    b):\n    pass"
    input = "if ((a and \n    b)):\n    pass"
    result = black.remove_redundant_parentheses(input)
    assert result == expected

def test_mixed_parenthesis():
    expected = "funct(l=[1,2,3])"
    input = "funct((l=([(1),(2),(3)])))"
    result = black.remove_redundant_parentheses(input)
    assert result == expected

def test_remove_redundant_parentheses_wrong_input_type():
    with pytest(TypeError):
        black.remove_redundant_parentheses(5)

def test_fully_flatten_expected_return():
    input = black.src_to_tokens("funct((l=[1,2,3]))")
    result = black.fully_flatten(input)
    assert result is list
    for i in result:
        assert i is Token
    assert len(result) == (len(input) - 2)
    
def test_fully_flatten_wrong_input_type():
    with pytest.raises(TypeError):
        black.fully_flatten("This is not a list of tokens")

def test_recursively_clean_expected_return():
    input = black.src_to_tokens("funct((l=[1,2,3]))")
    result = black.recursively_clean(input)
    assert result is list
    for i in result:
        assert i is Token
    assert len(result) == (len(input) - 2)

def test_recursively_clean_wrong_input_type():
    with pytest.raises(TypeError):
        black.recursively_clean("This is not a list of tokens")

def test_is_redundant_wrong_input_type():
    with pytest.raises(TypeError):
        black.is_redundant("This is not a list of tokens")

def test_is_redundant_positive_case1():
    input = black.src_to_tokens("(a and b)")
    assert black.is_redundant(input)

def test_is_redundant_positive_case2():
    input = black.src_to_tokens("()")
    assert black.is_redundant(input)

def test_is_redundant_negative_case1():
    input = black.src_to_tokens("param, *args")
    assert not black.is_redundant(input)

def test_is_redundant_negative_case2():
    input = black.src_to_tokens("(a and b) or c")
    assert not black.is_redundant(input)

def test_find_matching_input_type_error():
    with pytest.raises(TypeError):
        black.find_matching(3,3,"(",")")

def test_find_matching_base_case1():
    input = black.src_to_tokens("funct(a)")
    result = black.find_matching(input, 1, "(",")")
    assert result == 3

def test_find_matching_base_case():
    input = black.src_to_tokens("funct(l=[1,2,3])")
    result = black.find_matching(input, 4, "[","]")
    assert result == 10

def test_find_matching_mistake():
    input = black.src_to_tokens("this will not work")
    result = black.find_matching(input, 0, "(", ")")
    assert result is None





if __name__ == "__main__":
    input = black.src_to_tokens("funct(a)")
    print(input)
