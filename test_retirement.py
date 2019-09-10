import pytest
import RetirementCalculator
def test_ageType():
    with pytest.raises(ValueError):
        RetirementCalculator.retirement("age","5","10","20")

def test_ageTooOld():
    with pytest.raises(Exception, match="Invalid range for age"):
        RetirementCalculator.retirement("100","5","10","20")

def test_ageTooYoung():
    with pytest.raises(Exception, match="Invalid range for age"):
        RetirementCalculator.retirement("0","5","10","20")

def test_salaryType():
    with pytest.raises(ValueError):
        RetirementCalculator.retirement("5","money","10","20")

def test_savedType():
    with pytest.raises(ValueError):
        RetirementCalculator.retirement("5","10","five","20")

def test_goalType():
    with pytest.raises(ValueError):
        RetirementCalculator.retirement("5","10","20","goal")

def test_outputAgeCorrect():
    assert RetirementCalculator.retirement("40","65000","20","250000")[1] == 55

def test_goalWontBeReached():
    assert RetirementCalculator.retirement("85","65000","20","250000")[1] == -1