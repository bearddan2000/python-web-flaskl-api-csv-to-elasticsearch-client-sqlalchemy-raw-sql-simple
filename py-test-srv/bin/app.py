import requests
import testify

from const import *

def fun_call(url: str, fun):
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 
    
    return fun(url, headers=headers)

def assert_url(url: str, fun_ptr):
    """assert that endpoint is valid"""
    
    resp = fun_call(url, fun_ptr)

    testify.assert_equal(resp.status_code, 200)

    return 0

class TestSmoke(testify.TestCase):
    """docstring for TestSmoke."""

    def test_smoke_url(self):
        return assert_url(SMOKE_URL, requests.get)

    def test_smoke_output(self):
        resp = fun_call(SMOKE_URL, requests.get)
        testify.assert_equal(resp.json(), SMOKE)

class TestGet(testify.TestCase):
    """docstring for TestGet."""

    def test_get_all_url(self):
        return assert_url(GET_ALL_URL, requests.get)
    
    def test_get_all_equal_output(self):
        resp = fun_call(GET_ALL_URL, requests.get)
        testify.assert_equal(resp.json(), GET_ALL)

class TestDelete(testify.TestCase):
    """docstring for TestDelete."""

    def test_delete_value(self):
        resp = fun_call(DELETE_URL, requests.delete)
        testify.assert_equal(resp.json(), UNSUPPORTED)

class TestInsert(testify.TestCase):
    """docstring for TestInsert."""

    def test_insert_value(self):
        resp = fun_call(INSERT_URL, requests.put)
        testify.assert_equal(resp.json(), UNSUPPORTED)

class TestUpdate(testify.TestCase):
    """docstring for TestUpdate."""

    def test_update_value(self):
        resp = fun_call(UPDATE_URL, requests.post)
        testify.assert_equal(resp.json(), UNSUPPORTED)

if __name__ == '__main__':
    testify.run()
