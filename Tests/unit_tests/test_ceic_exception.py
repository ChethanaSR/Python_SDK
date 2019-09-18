import unittest
import json

from ceic_api_client.rest import ApiException
from ceic_api_client.facade.pyceic_exception import CeicException
from ceic_api_client.facade.pyceic_exception import CeicInvalidLoginDetailsException
from ceic_api_client.facade.pyceic_exception import CeicSessionExpiredException
from ceic_api_client.facade.pyceic_exception import CeicNoActiveSessionsException


class TestCeicException(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCeicException, self).__init__(*args, **kwargs)

        self._exception_class = CeicException
        self._exception = None

    def setUp(self):
        self._exception = self._exception_class()

    def tearDown(self):
        self._exception = None

    def test_status_raises_exception(self):
        def prop_getter_call():
            return self._exception.status

        self.assertRaises(NotImplementedError, prop_getter_call)

    def test_code_raises_exception(self):
        def prop_getter_call():
            return self._exception.code

        self.assertRaises(NotImplementedError, prop_getter_call)

    def test_message_raises_exception(self):
        def prop_getter_call():
            return self._exception.message

        self.assertRaises(NotImplementedError, prop_getter_call)

    def test_factory_method_returns_correct_object_type_invalid_login(self):
        status = 401
        code = "ERR_INVALID_USER_PASSWORD"
        message = "Invalid Username/Password. Please try your email address as username."
        expected_exception_string = self._build_exception_string(status, code, message)
        api_exception = self._build_api_exception(status, code, message)

        result = self._exception_class.build_ceic_exception_from(api_exception)

        expected = CeicInvalidLoginDetailsException
        actual = type(result)
        actual_exception_string = str(result)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_exception_string, actual_exception_string)

    def test_factory_method_returns_correct_object_expired_session(self):
        status = 401
        code = "ERR_SESSION_EXPIRED"
        message = "Session expired"
        expected_exception_string = self._build_exception_string(status, code, message)
        api_exception = self._build_api_exception(status, code, message)

        result = self._exception_class.build_ceic_exception_from(api_exception)

        expected = CeicSessionExpiredException
        actual = type(result)
        actual_exception_string = str(result)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_exception_string, actual_exception_string)

    def test_factory_method_returns_correct_object_no_active_session(self):
        status = 500
        code = "ERR"
        message = "ERR_NO_ACTIVE_SESSIONS"
        expected_exception_string = self._build_exception_string(status, code, message)
        api_exception = self._build_api_exception(status, code, message)

        result = self._exception_class.build_ceic_exception_from(api_exception)

        expected = CeicNoActiveSessionsException
        actual = type(result)
        actual_exception_string = str(result)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_exception_string, actual_exception_string)

    @staticmethod
    def _build_api_exception_body(status, code, message):
        body = {
            "errors": {
                "status": str(status),
                "code": code,
                "message": message
            }
        }
        body = json.dumps(body)

        return body

    @staticmethod
    def _build_exception_string(status, code, message):
        return "\nStatus: {}\nCode: {}\nMessage: {}\n".format(status, code, message)

    def _build_api_exception(self, status, code, message):
        api_exception = ApiException()
        api_exception.status = status
        api_exception.body = self._build_api_exception_body(status, code, message)

        return api_exception
