import pytest
import WebApp

app=WebApp.app.test_client()

def test_bmi_request_response():
    result=app.get('/bmi')
    assert result.status_code==200

def test_distances_request_response():
    result=app.get('/distances')
    assert result.status_code==200

def test_bmi_json_output():
    result=app.get('/bmi')
    if(result.status_code != 200):
        assert True
        return
    data=result.data.decode("utf-8")
    # During CI tests, result should be empty since the tests do not initialize an actual database
    if(data=='[]'):
        assert True
    # If there is an entry, it should have all the attributes
    else:
        assert "BMI" in data
        assert "category" in data
        assert "created_at" in data
        assert "feet" in data
        assert "inches" in data
        assert "weight" in data

def test_distances_json_output():
    result=app.get('/distances')
    if(result.status_code != 200):
        assert True
        return
    data=result.data.decode("utf-8")
    # During CI tests, result should be empty since the tests do not initialize an actual database
    if(data=='[]'):
        assert True
    # If there is an entry, it should have all the attributes
    else:
        assert "created_at" in data
        assert "distance" in data
        assert "x1" in data
        assert "x2" in data
        assert "y1" in data
        assert "y2" in data



