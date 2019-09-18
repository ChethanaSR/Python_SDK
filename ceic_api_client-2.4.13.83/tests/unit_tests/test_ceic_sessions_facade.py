import os
import shutil
import json
import unittest

from ceic_api_client.facade.pyceic_configuration import CeicConfiguration
from ceic_api_client.facade.pyceic_sessions_facade import CeicSessionsFacade
from ceic_api_client.facade.pyceic_exception import CeicSessionExpiredException
from ceic_api_client.facade.pyceic_exception import CeicInvalidLoginDetailsException
from ceic_api_client.facade.pyceic_exception import CeicNoActiveSessionsException


class CeicSessionsFacadeMock(CeicSessionsFacade):

    OS_IS_WINDOWS = False

    VALID_USERNAME_A = "VALID_USERNAME_A"
    VALID_PASSWORD_A = "VALID_PASSWORD_A"

    VALID_USERNAME_B = "VALID_USERNAME_B"
    VALID_PASSWORD_B = "VALID_PASSWORD_B"

    INVALID_USERNAME = "INVALID_USERNAME"
    INVALID_PASSWORD = "INVALID_PASSWORD"

    EXPIRED_SESSION_USERNAME = "EXPIRED_SESSION_USERNAME"
    EXPIRED_SESSION_PASSWORD = "EXPIRED_SESSION_PASSWORD"

    NO_ACTIVE_SESSION_USERNAME = "NO_ACTIVE_SESSION_USERNAME"
    NO_ACTIVE_SESSION_PASSWORD = "NO_ACTIVE_SESSION_PASSWORD"

    def __init__(self):
        super(CeicSessionsFacadeMock, self).__init__(CeicConfiguration())

        self._logout_is_called = False

    @property
    def session_id(self):
        return self._sessions_file["session"] if "session" in self._sessions_file else None

    @property
    def logout_is_called(self):
        return self._logout_is_called

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @staticmethod
    def sessions_dir_name():
        return CeicSessionsFacade._SESSIONS_DIR_NAME

    @staticmethod
    def sessions_file_name():
        return CeicSessionsFacade._SESSIONS_FILE_NAME

    @staticmethod
    def _os_is_windows():
        return CeicSessionsFacadeMock.OS_IS_WINDOWS

    @staticmethod
    def _get_user_home_dir():
        return CeicSessionsFacadeMock._build_current_directory_path()

    @staticmethod
    def _build_current_directory_path():
        return os.path.join(
            os.path.dirname(__file__)
        )

    def _call_api_login(self, username, password):
        self._check_login_details_are_valid(username, password)

        return "{}{}".format(username, password)

    def _call_api_logout(self, session_id):
        self._logout_is_called = True
        self._check_session_expired(self._username, self._password)
        self._check_active_sessions(self._username, self._password)

    def _check_login_details_are_valid(self, username, password):
        if (username == self.INVALID_USERNAME or username is None) or \
                (password == self.INVALID_PASSWORD or password is None):
            raise CeicInvalidLoginDetailsException()

    def _check_session_expired(self, username, password):
        if username == self.EXPIRED_SESSION_USERNAME or password == self.EXPIRED_SESSION_PASSWORD:
            raise CeicSessionExpiredException()

    def _check_active_sessions(self, username, password):
        if username == self.NO_ACTIVE_SESSION_USERNAME or password == self.NO_ACTIVE_SESSION_PASSWORD:
            raise CeicNoActiveSessionsException()


class TestCeicSessionsFacade(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestCeicSessionsFacade, self).__init__(*args, **kwargs)

        self._sessions = None

    def tearDown(self):
        self._sessions = None
        CeicSessionsFacadeMock.OS_IS_WINDOWS = False

        self._delete_sessions_file(CeicSessionsFacadeMock.get_sessions_file_path())

    def test_get_sessions_file_path_linux_os(self):
        expected = "{}/{}/{}".format(
            os.environ["HOME"],
            CeicSessionsFacadeMock.sessions_dir_name(),
            CeicSessionsFacadeMock.sessions_file_name()
        )
        actual = CeicSessionsFacadeMock.get_sessions_file_path()

        self.assertEqual(expected, actual)

    def test_get_sessions_file_path_windows_os(self):
        os.environ["LOCALAPPDATA"] = os.environ["HOME"]
        CeicSessionsFacadeMock.OS_IS_WINDOWS = True

        expected = "{}/{}/{}".format(
            os.environ["LOCALAPPDATA"],
            CeicSessionsFacadeMock.sessions_dir_name(),
            CeicSessionsFacadeMock.sessions_file_name()
        )
        actual = CeicSessionsFacadeMock.get_sessions_file_path()

        self.assertEqual(expected, actual)

        os.environ.pop("LOCALAPPDATA")

    def test_init_object_creates_file_no_previous_session(self):
        self._sessions = CeicSessionsFacadeMock()

        sessions_file_path = self._sessions.get_sessions_file_path()

        self.assertTrue(os.path.exists(sessions_file_path))
        self.assertTrue(os.path.isfile(sessions_file_path))

    def test_init_object_creates_empty_json_no_previous_session(self):
        self._sessions = CeicSessionsFacadeMock()

        sessions_file_path = self._sessions.get_sessions_file_path()

        expected = "{}"
        actual = self._read_file_as_string(sessions_file_path)

        self.assertIsNotNone(actual)
        self.assertEqual(expected, actual.strip())

    def test_init_object_session_id_returns_none_no_previous_session(self):
        self._sessions = CeicSessionsFacadeMock()

        self.assertIsNone(self._sessions.session_id)

    def test_login_returns_self(self):
        username = CeicSessionsFacadeMock.VALID_USERNAME_A
        password = CeicSessionsFacadeMock.VALID_PASSWORD_A

        expected = CeicSessionsFacadeMock()
        actual = expected.login(username, password)

        self.assertEqual(expected, actual)

    def test_login_creates_new_session_successful_login_no_active_session(self):
        self._sessions = CeicSessionsFacadeMock()

        username = CeicSessionsFacadeMock.VALID_USERNAME_A
        password = CeicSessionsFacadeMock.VALID_PASSWORD_A

        self._sessions.login(username, password)

        expected = "{}{}".format(username, password)
        actual_from_prop = self._sessions.session_id
        actual_from_file = self._get_session_id_from_file()

        self.assertEqual(expected, actual_from_prop)
        self.assertEqual(expected, actual_from_file)

        self.assertEqual(username, self._sessions.username)
        self.assertEqual(password, self._sessions.password)

    def test_login_does_not_save_session_failed_login_invalid_details_no_active_session(self):
        self._sessions = CeicSessionsFacadeMock()

        username = CeicSessionsFacadeMock.INVALID_USERNAME
        password = CeicSessionsFacadeMock.INVALID_PASSWORD

        self.assertRaises(CeicInvalidLoginDetailsException, self._sessions.login, *[username, password])

        actual_prop = self._sessions.session_id
        actual_file = self._read_file_as_string(self._sessions.get_sessions_file_path())

        self.assertIsNone(actual_prop)
        self.assertEqual("{}", actual_file)

        self.assertIsNone(self._sessions.username)
        self.assertIsNone(self._sessions.password)

    def test_login_creates_new_session_successful_login_active_session(self):
        self._sessions = CeicSessionsFacadeMock()

        username_a = CeicSessionsFacadeMock.VALID_USERNAME_A
        password_a = CeicSessionsFacadeMock.VALID_PASSWORD_A
        expected_session_id_a = "{}{}".format(username_a, password_a)
        actual_session_id_prop_a = self._sessions.login(username_a, password_a).session_id
        actual_session_id_file_a = self._get_session_id_from_file()

        username_b = CeicSessionsFacadeMock.VALID_USERNAME_B
        password_b = CeicSessionsFacadeMock.VALID_PASSWORD_B
        expected_session_id_b = "{}{}".format(username_b, password_b)
        actual_session_id_prop_b = self._sessions.login(username_b, password_b).session_id
        actual_session_id_file_b = self._get_session_id_from_file()

        self.assertNotEqual(expected_session_id_a, expected_session_id_b)
        self.assertNotEqual(actual_session_id_prop_a, actual_session_id_prop_b)
        self.assertNotEqual(actual_session_id_file_a, actual_session_id_file_b)

        self.assertEqual(expected_session_id_b, actual_session_id_prop_b)
        self.assertEqual(expected_session_id_b, actual_session_id_file_b)

        self.assertEqual(username_b, self._sessions.username)
        self.assertEqual(password_b, self._sessions.password)

    def test_login_calls_logout_active_session(self):
        self._sessions = CeicSessionsFacadeMock()

        username_a = CeicSessionsFacadeMock.VALID_USERNAME_A
        password_a = CeicSessionsFacadeMock.VALID_PASSWORD_A
        self._sessions.login(username_a, password_a)

        self.assertFalse(self._sessions.logout_is_called)

        username_b = CeicSessionsFacadeMock.VALID_USERNAME_B
        password_b = CeicSessionsFacadeMock.VALID_PASSWORD_B
        self._sessions.login(username_b, password_b)

        self.assertTrue(self._sessions.logout_is_called)

    def test_login_does_not_save_session_failed_login_invalid_details_active_session(self):
        self._sessions = CeicSessionsFacadeMock()

        username = CeicSessionsFacadeMock.VALID_USERNAME_A
        password = CeicSessionsFacadeMock.VALID_PASSWORD_A
        self._sessions.login(username, password)

        invalid_username = CeicSessionsFacadeMock.INVALID_USERNAME
        invalid_password = CeicSessionsFacadeMock.INVALID_PASSWORD
        self.assertRaises(CeicInvalidLoginDetailsException, self._sessions.login, *[invalid_username, invalid_password])

        actual_prop = self._sessions.session_id
        actual_file = self._read_file_as_string(CeicSessionsFacadeMock.get_sessions_file_path())

        self.assertIsNone(actual_prop)
        self.assertEqual("{}", actual_file)

        self.assertEqual(username, self._sessions.username)
        self.assertEqual(password, self._sessions.password)

    def test_login_creates_new_session_successfully_expired_session(self):
        self._sessions = CeicSessionsFacadeMock()

        username_a = CeicSessionsFacadeMock.VALID_USERNAME_A
        password_a = CeicSessionsFacadeMock.VALID_PASSWORD_A
        session_id_prop_a = self._sessions.login(username_a, password_a).session_id
        session_id_file_a = self._get_session_id_from_file()

        username_b = CeicSessionsFacadeMock.EXPIRED_SESSION_USERNAME
        password_b = CeicSessionsFacadeMock.EXPIRED_SESSION_USERNAME
        session_id_prop_b = self._sessions.login(username_b, password_b).session_id
        session_id_file_b = self._get_session_id_from_file()

        expected_session_id_a = "{}{}".format(username_a, password_a)
        expected_session_id_b = "{}{}".format(username_b, password_b)

        self.assertEqual(expected_session_id_a, session_id_prop_a)
        self.assertEqual(expected_session_id_a, session_id_file_a)
        self.assertEqual(expected_session_id_b, session_id_prop_b)
        self.assertEqual(expected_session_id_b, session_id_file_b)

        self.assertNotEqual(session_id_prop_a, session_id_prop_b)
        self.assertNotEqual(session_id_file_a, session_id_file_b)

        self.assertTrue(self._sessions.logout_is_called)

        self.assertEqual(username_b, self._sessions.username)
        self.assertEqual(password_b, self._sessions.password)

    def test_logout_raises_no_active_sessions_exception_no_session(self):
        self._sessions = CeicSessionsFacadeMock()

        self.assertRaises(CeicNoActiveSessionsException, self._sessions.logout)

    def test_logout_returns_self_active_session(self):
        username = CeicSessionsFacadeMock.VALID_USERNAME_A
        password = CeicSessionsFacadeMock.VALID_PASSWORD_B

        self._sessions = CeicSessionsFacadeMock().login(username, password)
        actual_sessions = self._sessions.logout()

        self.assertEqual(self._sessions, actual_sessions)

    def test_logout_removes_session_id_valid_session(self):
        username = CeicSessionsFacadeMock.VALID_USERNAME_A
        password = CeicSessionsFacadeMock.VALID_PASSWORD_A

        self._sessions = CeicSessionsFacadeMock().login(username, password).logout()

        expected_session_id_prop = None
        expected_session_id_file = "{}"

        actual_session_id_prop = self._sessions.session_id
        actual_session_id_file = self._read_file_as_string(self._sessions.get_sessions_file_path())

        self.assertTrue(self._sessions.logout_is_called)
        self.assertEqual(expected_session_id_prop, actual_session_id_prop)
        self.assertEqual(expected_session_id_file, actual_session_id_file)

        self.assertEqual(username, self._sessions.username)
        self.assertEqual(password, self._sessions.password)

    def test_logout_raises_no_active_sessions_exception_session_expired(self):
        username = CeicSessionsFacadeMock.EXPIRED_SESSION_USERNAME
        password = CeicSessionsFacadeMock.EXPIRED_SESSION_PASSWORD

        self._sessions = CeicSessionsFacadeMock().login(username, password)

        self.assertRaises(CeicSessionExpiredException, self._sessions.logout)

    def test_second_init_restores_session_id_no_session(self):
        self._sessions = CeicSessionsFacadeMock()
        second_sessions = CeicSessionsFacadeMock()
        session_file = self._read_file_as_string(self._sessions.get_sessions_file_path())

        self.assertIsNone(self._sessions.session_id)
        self.assertIsNone(second_sessions.session_id)
        self.assertEqual("{}", session_file)

    def test_second_init_restores_session_id_active_session(self):
        username = CeicSessionsFacadeMock.VALID_USERNAME_A
        password = CeicSessionsFacadeMock.VALID_PASSWORD_A

        self._sessions = CeicSessionsFacadeMock().login(username, password)
        second_sessions = CeicSessionsFacadeMock()

        self.assertEqual(self._sessions.session_id, second_sessions.session_id)
        self.assertEqual(self._sessions.session_id, self._get_session_id_from_file())

        self.assertIsNone(second_sessions.username)
        self.assertIsNone(second_sessions.password)

        # TODO: Handle this case. It belongs in integration tests:
        #  second_sessions.login(username, password)
        #  self._sessions.get_series()
        #  OR
        #  second_sessions.logout()
        #  self._sessions.get_series()
        #  These cases could be solved, with a more complex handling of a shared sessions file.
        #  For no we will ignore them, but should think about handling them.
        #  This is not exactly a borderline case, as it has some probability of happening, depending on the developer.
        #  The SessionFacade should try to get the session id from the file,
        #  if the session is expired.
        #  If the session id in the file is the same as the expired one, then login again. If not then just use it.

    def _get_session_id_from_file(self):
        file_path = CeicSessionsFacadeMock.get_sessions_file_path()
        file_as_str = self._read_file_as_string(file_path)
        json_file = json.loads(file_as_str)

        return json_file["session"]

    @staticmethod
    def _delete_sessions_file(file_path):
        file_directory = os.path.dirname(file_path)

        if os.path.exists(file_directory):
            shutil.rmtree(file_directory)

    @staticmethod
    def _read_file_as_string(file_path):
        if not os.path.exists(file_path):
            return None

        with open(file_path, 'r') as f:
            return f.read()
