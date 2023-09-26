# before installing mypy


def sum_of_two_number(a: int, b: int) -> int:
    return a + b


ans1 = sum_of_two_number(1, 2)  # both integers
ans2 = sum_of_two_number(1.0, 2.0)  # both float
print(ans1, ans2)
# both are working fine.

# Now let's install mypy using pip; pip install mypy
# Now try running above code again
# using mypy static_type_test.py
# Got error right? Yes.
