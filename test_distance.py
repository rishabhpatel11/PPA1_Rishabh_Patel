import pytest
import math
import DistanceCalculator

def test_x1type():
    with pytest.raises(ValueError):
        DistanceCalculator.distance("xs","2","1","3")

def test_y1type():
    with pytest.raises(ValueError):
        DistanceCalculator.distance("2","ylocation","1","3")

def test_x2type():
    with pytest.raises(ValueError):
        DistanceCalculator.distance("1","2","x2","3")

def test_y2type():
    with pytest.raises(ValueError):
        DistanceCalculator.distance("1","2","3","y6.7")

def test_correctDistance():
    assert DistanceCalculator.distance("10.4","7.2","82.3","-10.2") == 73.97547

def test_variousNegativeInputs():
    assert DistanceCalculator.distance("-5.8","92","18.5","72.5") == 31.15670
    assert DistanceCalculator.distance("-5.8","92","18.5","-72.5") == 166.28512
    assert DistanceCalculator.distance("-5.8","-92","18.5","-72.5") == 31.15670
    assert DistanceCalculator.distance("-5.8","-92","-18.5","-72.5") == 23.27101

