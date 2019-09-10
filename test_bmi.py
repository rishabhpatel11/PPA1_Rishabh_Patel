import pytest
import BMICalculator
# Use pytest -rA to see names of tests

def test_feet():
    with pytest.raises(ValueError):
        BMICalculator.bmi("sde","2","130.5")

def test_inches():
    with pytest.raises(ValueError):
        BMICalculator.bmi("1","twoo","32")

def test_weight():
    with pytest.raises(ValueError):
        BMICalculator.bmi("1","2","thwe") 

def test_UnderWeight():
    assert BMICalculator.bmi("5","10","100.0")[1] == "Underweight"

def test_NormalWeight():
    assert BMICalculator.bmi("5","3","125")[1] == "Normal weight"

def test_OverWeight():
    assert BMICalculator.bmi("5","10","200.1")[1] == "Overweight"

def test_Obese():
    assert BMICalculator.bmi("6","1","300")[1] == "Obese"

def test_accurateBMI():
    assert BMICalculator.bmi("5","3","125")[0] == 22.7
