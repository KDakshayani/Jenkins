import pytest
from EmployeeSalary import calculate_salary


def test_default_salary_calculation():
    # Test with basic salary of 50,000 as specified in the problem
    result = calculate_salary(50000)

    assert result["basic_salary"] == 50000
    assert result["hra"] == 10000.0
    assert result["da"] == 5000.0
    assert result["gross_salary"] == 65000.0


def test_zero_salary():
    # Test edge case with 0 basic salary
    result = calculate_salary(0)

    assert result["hra"] == 0.0
    assert result["da"] == 0.0
    assert result["gross_salary"] == 0.0


pytest.mark.parametrize(
    "basic, expected_gross",
    [
        (10000, 13000.0),
        (25000, 32500.0),
        (100000, 130000.0),
    ],
)
def test_various_salaries(basic, expected_gross):
    # Test multiple salary inputs
    result = calculate_salary(basic)
    assert result["gross_salary"] == expected_gross