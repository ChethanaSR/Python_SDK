import sys
import inspect
import json


class CeicException(Exception):
    _STATUS = None
    _CODE = None
    _MESSAGE = None

    @property
    def status(self):
        if self._STATUS is None:
            raise NotImplementedError()

        return self._STATUS

    @property
    def code(self):
        if self._CODE is None:
            raise NotImplementedError()

        return self._CODE

    @property
    def message(self):
        if self._MESSAGE is None:
            raise NotImplementedError()

        return self._MESSAGE

    def __str__(self):
        return "\nStatus: {}\nCode: {}\nMessage: {}\n".format(
            self.status,
            self.code,
            self.message
        )

    @staticmethod
    def _str_is_null_or_empty(str_obj):
        return str_obj is None or str_obj.strip() == ""

    @classmethod
    def build_ceic_exception_from(cls, api_exception):
        exception_classes = cls._list_exception_classes()
        for exception_class in exception_classes:
            if cls._class_matches_api_exception(exception_class, api_exception):
                return exception_class()

        raise TypeError("Could not convert ApiException to CeicException")

    @classmethod
    def _class_matches_api_exception(cls, exception_class, api_exception):
        status = cls._get_ceic_exception_status_from(api_exception)
        code = cls._get_ceic_exception_code_from(api_exception)
        message = cls._get_ceic_exception_message_from(api_exception)

        return cls._exception_statuses_match(status, exception_class._STATUS) and \
               cls._exception_codes_match(code, exception_class._CODE) and \
               cls._exception_messages_match(message, exception_class._MESSAGE)

    @classmethod
    def _list_exception_classes(cls):
        classes = []
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj) and name != cls.__name__:
                classes.append(obj)

        return classes

    @classmethod
    def _get_ceic_exception_status_from(cls, api_exception):
        if api_exception.status is not None:
            status = api_exception.status if isinstance(api_exception.status, int) else int(api_exception.status)

            return status

        raise KeyError("ApiException does not have a valid status property value")

    @classmethod
    def _get_ceic_exception_code_from(cls, api_exception):
        if api_exception.body is not None:
            body = json.loads(api_exception.body)
            if "errors" in body and "code" in body["errors"] and body["errors"]["code"] is not None:
                return body["errors"]["code"]

        raise KeyError("ApiException body does not have a valid code")

    @classmethod
    def _get_ceic_exception_message_from(cls, api_exception):
        if api_exception.body is not None:
            body = json.loads(api_exception.body)
            if "errors" in body and "message" in body["errors"] and body["errors"]["message"] is not None:
                return body["errors"]["message"]

        raise KeyError("ApiException body does not have a valid message")

    @classmethod
    def _exception_statuses_match(cls, left_status, right_status):
        return left_status is not None and \
               right_status is not None and \
               left_status == right_status

    @classmethod
    def _exception_codes_match(cls, left_code, right_code):
        return not cls._str_is_null_or_empty(left_code) and \
               not cls._str_is_null_or_empty(right_code) and \
               left_code.strip() == right_code.strip()

    @classmethod
    def _exception_messages_match(cls, left_message, right_message):
        return not cls._str_is_null_or_empty(left_message) and \
               not cls._str_is_null_or_empty(right_message) and \
               left_message.strip() == right_message.strip()


class CeicInvalidLoginDetailsException(CeicException):
    _STATUS = 401
    _CODE = "ERR_INVALID_USER_PASSWORD"
    _MESSAGE = "Invalid Username/Password. Please try your email address as username."


class CeicSessionExpiredException(CeicException):
    _STATUS = 401
    _CODE = "ERR_SESSION_EXPIRED"
    _MESSAGE = "Session expired"


class CeicNotLoggedIn(CeicException):
    _STATUS = 401
    _CODE = "MISSED_API_TOKEN"
    _MESSAGE = "Please use access token to get data"


class CeicSessionTerminatedException(CeicException):
    _STATUS = 401
    _CODE = "ERR_SESSION_TERMINATED"
    _MESSAGE = "Session terminated"


class CeicActiveSessionException(CeicException):
    _STATUS = 401
    _CODE = "ERR_USER_ID_ALREADY_ACTIVE_SESSION"
    _MESSAGE = "A user with this username is already logged in. Please wait until the login expires or try to log in from the original device."


class CeicNoActiveSessionsException(CeicException):
    _STATUS = 500
    _CODE = "ERR"
    _MESSAGE = "ERR_NO_ACTIVE_SESSIONS"


