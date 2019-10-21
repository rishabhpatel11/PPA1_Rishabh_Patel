import pytest
import math
import DistanceCalculator

def test_CheckStringInputForX1Fails():
    with pytest.raises(ValueError):
        DistanceCalculator.distance("xs","2","1","3")

def test_CheckStringInputForY1Fails():
    with pytest.raises(ValueError):
        DistanceCalculator.distance("2","ylocation","1","3")

def test_CheckStringInputForX2Fails():
    with pytest.raises(ValueError):
        DistanceCalculator.distance("1","2","x2","3")

def test_CheckStringInputForY2Fails():
    with pytest.raises(ValueError):
        DistanceCalculator.distance("1","2","3","y6.7")

def test_CheckForFiveDecimalPlaces():
    assert len(DistanceCalculator.distance("23.34","34234.43","334","4334.3")[4].split('.')[1]) == 5
    assert len(DistanceCalculator.distance("6","2","5","2")[4].split('.')[1]) == 5

def test_correctDistance():
    assert DistanceCalculator.distance("10.4","7.2","82.3","-10.2")[4] == "73.97547"
    assert DistanceCalculator.distance("645.23","18.50","98","178")[4] == "570.00081"
    assert DistanceCalculator.distance(".45","63.5","42.23","9")[4] == "68.67182"

def test_variousNegativeInputs():
    assert DistanceCalculator.distance("-5.8","92","18.5","72.5")[4] == "31.15670"
    assert DistanceCalculator.distance("-5.8","92","18.5","-72.5")[4] == "166.28512"
    assert DistanceCalculator.distance("-5.8","-92","18.5","-72.5")[4] == "31.15670"
    assert DistanceCalculator.distance("-5.8","-92","-18.5","-72.5")[4] == "23.27101"

