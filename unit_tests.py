import unittest
from calculator import returnone

def test_run_stuff():
    result = returnone()
    assert result == 1
