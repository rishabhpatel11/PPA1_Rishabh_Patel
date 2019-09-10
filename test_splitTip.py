import pytest
import SplitTipCalculator

def test_CheckStringInputForTotalFails():
    with pytest.raises(ValueError):
        SplitTipCalculator.splitTip("djswi","3")

def test_CheckStringInputForGuestsFails():
    with pytest.raises(ValueError):
        SplitTipCalculator.splitTip("520.85","2.5")

def test_TooManyDecimalsInput():
    with pytest.raises(Exception, match="Expected only up to 2 decimal places for the total"):
        SplitTipCalculator.splitTip("520.8556","5")

def test_AlwaysTwoDecimalsOutput():
    out=SplitTipCalculator.splitTip("584.29","82")
    for x in range(len(out)):
        assert len(out[x].split('.')[1]) == 2

def test_UnevenSplitStartsAtFirstGuestAndGoesInOrder():
    out=SplitTipCalculator.splitTip("13.18","3")
    correctA=0
    correctB=0
    for i in range(len(out)):
        if(out[i] > out[i+1]):
            correctA=1
        if(i+1 == len(out)-1):
            break
    out=SplitTipCalculator.splitTip("78.00","14")
    for i in range(len(out)):
        if(out[i] > out[i+1]):
            correctB=1
        if(i+1 == len(out)-1):
            break
    assert correctA and correctB

def test_TotalIsEvenlyDividedV1():
    assert SplitTipCalculator.splitTip("13.18","3")[3] == "15.16"
    assert SplitTipCalculator.splitTip("13.18","3")[0] == "5.06"
    assert SplitTipCalculator.splitTip("13.18","3")[1] == "5.05"
    assert SplitTipCalculator.splitTip("13.18","3")[2] == "5.05"

def test_TotalIsEvenlyDividedV2():
    assert SplitTipCalculator.splitTip("78.00","14")[14] == "89.70"
    assert SplitTipCalculator.splitTip("78.00","14")[0] == "6.41"
    assert SplitTipCalculator.splitTip("78.00","14")[1] == "6.41"
    assert SplitTipCalculator.splitTip("78.00","14")[2] == "6.41"
    assert SplitTipCalculator.splitTip("78.00","14")[3] == "6.41"
    assert SplitTipCalculator.splitTip("78.00","14")[4] == "6.41"
    assert SplitTipCalculator.splitTip("78.00","14")[5] == "6.41"
    assert SplitTipCalculator.splitTip("78.00","14")[6] == "6.41"
    assert SplitTipCalculator.splitTip("78.00","14")[7] == "6.41"
    assert SplitTipCalculator.splitTip("78.00","14")[8] == "6.41"
    assert SplitTipCalculator.splitTip("78.00","14")[9] == "6.41"
    assert SplitTipCalculator.splitTip("78.00","14")[10] == "6.40"
    assert SplitTipCalculator.splitTip("78.00","14")[11] == "6.40"
    assert SplitTipCalculator.splitTip("78.00","14")[12] == "6.40"
    assert SplitTipCalculator.splitTip("78.00","14")[13] == "6.40"




