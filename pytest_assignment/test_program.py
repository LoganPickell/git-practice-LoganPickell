import pytest
from program import divide_numbers, reverse_string, get_list_element

# divide_numbers tests
def test_divide_numbers():
    result = divide_numbers(10, 2)
    assert result == 5.00, "Expected result to be 5.00"

def test_divide_numbers_negative():
    result = divide_numbers(-10, 2)
    assert result == -5.00, "Expected result to be -5.00"

def test_divide_by_one():
    result = divide_numbers(10, 1)
    assert result == 10.00, "Expected result to be 10.00"

def test_result_is_float():
    result = divide_numbers(10, 4)
    assert isinstance(result, float), "Expected result to be a float"

def test_divide_by_zero():
    result = divide_numbers(10, 0)
    assert result == "Error: Division by zero"


#reverse_string tests
def test_normal_string():
    result = reverse_string("Hello")
    assert reverse_string("Hello") == "OLLEh", "Expected 'OLLEh'"

def test_all_caps_string():
    result = reverse_string("HELLO")
    assert reverse_string("HELLO") == "olleh", "Expected 'olleh'"

def test_empty_string():
    result = reverse_string("")
    assert reverse_string("") == "Error: Empty string", "Expected 'Error: Empty string'"

def test_camel_case_string():
    result = reverse_string("hElLoWoRlD")
    assert reverse_string("hElLoWoRlD") == "dLrOwOlLeH", "Expected 'dLrOwOlLeH'"


# get_list_element tests
def test_get_list_element_normal():
    result = get_list_element([1, 2, 3, 4], 2)
    assert result == 3, "Expected to get the value at index 2"


def test_get_list_element_edge():
    result = get_list_element([1, 2, 3, 4], 4)
    assert result == "Error: Index out of range", "Expected 'Error: Index out of range' for out-of-bounds index"


def test_get_list_element_corner():
    result = get_list_element([], 0)
    assert result == "Error: No list found", "Expected 'Error: No list found' for an empty list"



    