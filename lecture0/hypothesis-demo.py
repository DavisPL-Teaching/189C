"""
Hypothesis demo

From:
https://pypi.org/project/hypothesis/

For more, see the documentation:
https://hypothesis.readthedocs.io/en/latest/quickstart.html

Question:
Is the average of a list always between the minimum and maximum values?
"""

from hypothesis import given
from hypothesis import strategies as st

def average(l):
    return sum(l) / len(l)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_average(xs):
    assert min(xs) <= average(xs) <= max(xs)

if __name__ == "__main__":
    test_average()
