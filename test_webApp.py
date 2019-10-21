import pytest
import WebApp

app=WebApp.app.test_client()

def test_bmi_request_response():
    result=app.get('/bmi')
    assert result.status_code==200

def test_distances_request_response():
    result=app.get('/distances')
    assert result.status_code==200

