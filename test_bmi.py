import pytest
import BMICalculator
# Use pytest -rA to see names of tests

def test_CheckStringInputForFeetFails():
    with pytest.raises(ValueError):
        BMICalculator.bmi("sde","2","130.5")

def test_CheckDecimalInputForFeetFails():
    with pytest.raises(ValueError):
        BMICalculator.bmi(".23","2","130.5")

def test_CheckStringInputForInchesFails():
    with pytest.raises(ValueError):
        BMICalculator.bmi("1","twoo","32")

def test_CheckDecimalInputForInchesFails():
    with pytest.raises(ValueError):
        BMICalculator.bmi("2","2.3","130.5")

def test_CheckStringInputForWeightFails():
    with pytest.raises(ValueError):
        BMICalculator.bmi("1","2","thwe") 

def test_CheckWeightZeroInputFails():
    with pytest.raises(Exception,match="Weight cannot be equal to 0"):
        BMICalculator.bmi("5","2","0.0")

def test_UnderWeightCategoryWorks():
    assert BMICalculator.bmi("5","10","100.0")[1] == "Underweight"

def test_NormalWeightCategoryWorks():
    assert BMICalculator.bmi("5","3","125")[1] == "Normal weight"

def test_OverWeightCategoryWorks():
    assert BMICalculator.bmi("5","10","200.1")[1] == "Overweight"

def test_ObeseCategoryWorks():
    assert BMICalculator.bmi("6","1","300")[1] == "Obese"

def test_AccurateBMI():
    assert BMICalculator.bmi("5","3","125")[0] == 22.7
    assert BMICalculator.bmi("5","3","250")[0] == 45.4
    assert BMICalculator.bmi("5","10","180")[0] == 26.4
    assert BMICalculator.bmi("6","2","178.5")[0] == 23.5
    assert BMICalculator.bmi("4","10","92.5")[0] == 19.8
