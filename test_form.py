import unittest
import mock

from classform import Form

class test_form(unittest.unittest):
    def test_request_question():
        with mock.patch('builtins.input',return_value = "what is your age")