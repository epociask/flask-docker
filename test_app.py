
# coding=utf-8
import pytest
import os 
import requests
from pytest_bdd import (
    scenarios,
    then,
    when,
)

DEV_URL: str = "http://dev-empociask-1234596866.us-west-2.elb.amazonaws.com"
assert DEV_URL != ""

scenarios('app.feature', example_converters=dict(string=str))


@pytest.fixture
@when('the API is queried with name: "<string>"')
def shout_response(string):
    params = {"Content-Type": "application/json"}
    response = requests.get(DEV_URL + f"/?name={string}", headers=params)
    return response


@then('the response has the prefix bye with "<string>" as output')
def shout_response_upper_cased(shout_response, string):
    print(shout_response)
    assert "Goodbye" in str(shout_response.content) and string in str(shout_response.content)


@then('the response status code is 200')
def shout_response_code(shout_response):
    assert shout_response.status_code == 200