import pytest
import RetirementCalculator
def test_CheckStringInputForAgeFails():
    with pytest.raises(ValueError):
        RetirementCalculator.retirement("age","5","10","20")

def test_AgeCannotBeGreaterThan99():
    with pytest.raises(Exception, match="Invalid range for age"):
        RetirementCalculator.retirement("100","5","10","20")

def test_AgeCannotBeZero():
    with pytest.raises(Exception, match="Invalid range for age"):
        RetirementCalculator.retirement("0","5","10","20")

def test_CheckStringInputForSalaryFails():
    with pytest.raises(ValueError):
        RetirementCalculator.retirement("5","money","10","20")

def test_CheckStringInputForSavedFails():
    with pytest.raises(ValueError):
        RetirementCalculator.retirement("5","10","five","20")

def test_CheckStringInputForGoalFails():
    with pytest.raises(ValueError):
        RetirementCalculator.retirement("5","10","20","goal")

def test_OutputAgeCorrect():
    assert RetirementCalculator.retirement("40","65000","20","250000")[1] == 55

def test_GoalCantBeReached():
    assert RetirementCalculator.retirement("85","65000","20","250000")[1] == -1
    assert RetirementCalculator.retirement("92","165000","10.5","2500000")[1] == -1

def test_CorrectOutputMessage():
    assert RetirementCalculator.retirement("40","65000","20","250000")[0] == "Savings goal will be met at age: "
    assert RetirementCalculator.retirement("85","65000","20","250000")[0] == "Savings goal will not be met in the current lifespan"