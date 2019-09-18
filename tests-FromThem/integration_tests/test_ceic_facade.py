import unittest
import os
import json

from ceic_api_client.pyceic import Ceic
from ceic_api_client.facade.pyceic_exception import *


class TestCeicFacade(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        self._valid_username = "sdk-integration-tests@apiqatest1.com"
        self._valid_password = "4P11nTegr4t10nTests"

        self._sessions_file_location = Ceic()._sessions_facade.get_sessions_file_path()

        # Count = 117
        self._series_ids_list = [
            "405092227", "405092257", "405092267", "17625901", "17626201", "17626301", "17626401", "17626701",
            "17626801", "17630901", "17631001", "17631101", "17631201", "17631301", "17631401", "17631501", "17631601",
            "17631701", "17631801", "17631901", "17632001", "17632101", "17632201", "17632301", "17632401", "17632501",
            "17632601", "17632701", "17632801", "17632901", "17633001", "17633101", "17633201", "17633301", "17633401",
            "17633501", "17633601", "17633701", "17633801", "17633901", "17634001", "17634101", "17634201", "17634301",
            "17634401", "17634501", "17634601", "17634701", "17634801", "17634901", "17635001", "17635101", "17635201",
            "17635401", "17635501", "17635601", "17635701", "17635801", "17635301", "17635901", "17636001", "17636101",
            "17636201", "17636401", "17636501", "17636601", "17636701", "17636801", "17636301", "17636901", "17637001",
            "405092237", "405092247", "17626001", "17626101", "17626501", "17626601", "17626901", "17627001",
            "17627101", "17627201", "17627301", "17627401", "17627501", "17627601", "17627701", "17627801", "17627901",
            "17628001", "17628101", "17628201", "17628301", "17628401", "17628501", "17628601", "17628701", "17628801",
            "17628901", "17629001", "17629101", "17629201", "17629301", "17629401", "17629501", "17629601", "17629701",
            "17629801", "17629901", "17630001", "17630101", "17630201", "17630301", "17630401", "17630501", "17630601",
            "17630701", "17630801"
        ]
        self._max_series_per_request = 20

    def tearDown(self):
        try:
            Ceic.logout()
        except CeicException:
            pass

    def test_set_server(self):
        new_server = "MY_TEST_SERVER"

        ceic = Ceic()
        original_server = ceic._ceic_configuration.server

        self.assertNotEqual(new_server, original_server)

        ceic.set_server(new_server)
        self.assertEqual(new_server, ceic.get_server())
        self.assertEqual(new_server, Ceic.get_server())

        Ceic.set_server(original_server)
        self.assertEqual(original_server, ceic.get_server())
        self.assertEqual(original_server, Ceic.get_server())

    def test_set_proxy(self):
        proxy_url = "MY_PROXY_URL"
        proxy_username = "MY_PROXY_USERNAME"
        proxy_password = "MY_PROXY_PASSWORD"

        ceic = Ceic()

        original_url = ceic._ceic_configuration.api_client.configuration.proxy_url
        original_username = ceic._ceic_configuration.api_client.configuration.proxy_username
        original_password = ceic._ceic_configuration.api_client.configuration.proxy_password

        self.assertNotEqual(proxy_url, original_url)
        self.assertNotEqual(proxy_username, original_username)
        self.assertNotEqual(proxy_password, original_password)

        ceic.set_proxy(proxy_url, proxy_username, proxy_password)
        self.assertEqual(proxy_url, ceic._ceic_configuration.api_client.configuration.proxy_url)
        self.assertEqual(proxy_username, ceic._ceic_configuration.api_client.configuration.proxy_username)
        self.assertEqual(proxy_password, ceic._ceic_configuration.api_client.configuration.proxy_password)
        self.assertEqual(proxy_url, Ceic._get_instance()._ceic_configuration.api_client.configuration.proxy_url)
        self.assertEqual(proxy_username, Ceic._get_instance()._ceic_configuration.api_client.configuration.proxy_username)
        self.assertEqual(proxy_password, Ceic._get_instance()._ceic_configuration.api_client.configuration.proxy_password)

        Ceic.set_proxy(original_url, original_username, original_password)
        self.assertEqual(original_url, ceic._ceic_configuration.api_client.configuration.proxy_url)
        self.assertEqual(original_username, ceic._ceic_configuration.api_client.configuration.proxy_username)
        self.assertEqual(original_password, ceic._ceic_configuration.api_client.configuration.proxy_password)
        self.assertEqual(original_url, Ceic._get_instance()._ceic_configuration.api_client.configuration.proxy_url)
        self.assertEqual(
            original_username, Ceic._get_instance()._ceic_configuration.api_client.configuration.proxy_username
        )
        self.assertEqual(
            original_password, Ceic._get_instance()._ceic_configuration.api_client.configuration.proxy_password
        )
        
    def test_successful_login(self):
        ceic = Ceic(username=self._valid_username, password=self._valid_password)
        self._assert_sessions_file_exist()
        self._assert_session_is_saved_in_file()

        ceic.logout()
        self._assert_sessions_file_exist()
        self._assert_sessions_file_does_not_contain_session()

        Ceic.login(username=self._valid_username, password=self._valid_password)
        self._assert_sessions_file_exist()
        self._assert_session_is_saved_in_file()

        Ceic.logout()
        self._assert_sessions_file_exist()
        self._assert_sessions_file_does_not_contain_session()

    def test_failed_login_invalid_details(self):
        self._reset_login_details()
        self.assertRaises(
            CeicInvalidLoginDetailsException, Ceic,
            **{"username": self._valid_username, "password": "INVALID_PASSWORD"}
        )
        self.assertRaises(
            CeicInvalidLoginDetailsException, Ceic().login,
            **{"username": self._valid_username, "password": "INVALID_PASSWORD"}
        )
        self.assertRaises(
            CeicInvalidLoginDetailsException, Ceic.login,
            **{"username": self._valid_username, "password": "INVALID_PASSWORD"}
        )

        self._reset_login_details()
        self.assertRaises(
            CeicInvalidLoginDetailsException, Ceic,
            **{"username": "INVALID_USERNAME", "password": "INVALID_PASSWORD"}
        )
        self.assertRaises(
            CeicInvalidLoginDetailsException, Ceic().login,
            **{"username": "INVALID_USERNAME", "password": "INVALID_PASSWORD"}
        )
        self.assertRaises(
            CeicInvalidLoginDetailsException, Ceic.login,
            **{"username": "INVALID_USERNAME", "password": "INVALID_PASSWORD"}
        )

        self._reset_login_details()
        
    def test_failed_login_active_session(self):
        self._reset_login_details()
        Ceic.login(self._valid_username, self._valid_password)
        session_id = self._get_session_id_from_file()
        self._remove_session_id_from_file()
        Ceic()._sessions_facade._sessions_file = {}
        Ceic()._sessions_facade._last_successful_session = None

        self.assertRaises(
            CeicActiveSessionException, Ceic,
            **{"username": self._valid_username, "password": self._valid_password}
        )
        self.assertRaises(
            CeicActiveSessionException, Ceic().login,
            **{"username": self._valid_username, "password": self._valid_password}
        )
        self.assertRaises(
            CeicActiveSessionException, Ceic.login,
            **{"username": self._valid_username, "password": self._valid_password}
        )

        self._set_session_id_in_file(session_id)
        Ceic()._sessions_facade._sessions_file = {"session": session_id}
        Ceic()._sessions_facade._last_successful_session = session_id
        Ceic.logout()
        self._reset_login_details()

    def test_get_series_single_series(self):
        Ceic.login(self._valid_username, self._valid_password)
        ceic = Ceic()

        series_id = int(self._series_ids_list[0])
        self.assertEqual(series_id, Ceic.series(series_id).data[0].metadata.id)
        self.assertEqual(series_id, ceic.series(series_id).data[0].metadata.id)

        for series_result in Ceic.series(series_id):
            self.assertEqual(series_id, series_result.data[0].metadata.id)

        for series_result in ceic.series(series_id):
            self.assertEqual(series_id, series_result.data[0].metadata.id)

        series_id = [series_id]
        self.assertEqual(int(series_id[0]), Ceic.series(series_id).data[0].metadata.id)
        self.assertEqual(int(series_id[0]), ceic.series(series_id).data[0].metadata.id)

        for series_result in Ceic.series(series_id):
            self.assertEqual(int(series_id[0]), series_result.data[0].metadata.id)

        for series_result in ceic.series(series_id):
            self.assertEqual(int(series_id[0]), series_result.data[0].metadata.id)

    def test_get_series_multiple_series(self):
        Ceic.login(self._valid_username, self._valid_password)
        ceic = Ceic()

        actual_series_result = Ceic.series(self._series_ids_list)
        self._compare_series_results(actual_series_result)

        actual_series_result = ceic.series(self._series_ids_list)
        self._compare_series_results(actual_series_result)

    def test_get_series_throws_exception(self):
        Ceic.login(self._valid_username, self._valid_password)
        ceic = Ceic()

        series_ids = ','.join(self._series_ids_list)
        self.assertRaises(ValueError, Ceic.series, [series_ids])
        self.assertRaises(ValueError, ceic.series, [series_ids])

        series_ids = {id: self._series_ids_list}
        self.assertRaises(ValueError, Ceic.series, [series_ids])
        self.assertRaises(ValueError, ceic.series, [series_ids])

        series_ids = {id: ','.join(self._series_ids_list)}
        self.assertRaises(ValueError, Ceic.series, [series_ids])
        self.assertRaises(ValueError, ceic.series, [series_ids])

    @staticmethod
    def _reset_login_details():
        Ceic()._sessions_facade._username = None
        Ceic()._sessions_facade._password = None

    def _assert_sessions_file_exist(self):
        self.assertTrue(
            os.path.exists(self._sessions_file_location)
        )
        self.assertTrue(
            os.path.isfile(self._sessions_file_location)
        )

    def _assert_session_is_saved_in_file(self):
        with open(self._sessions_file_location, 'r') as file_content:
            sessions_file = json.load(file_content)

        self.assertTrue("session" in sessions_file)
        self.assertIsNotNone(sessions_file["session"])

    def _assert_sessions_file_does_not_contain_session(self):
        with open(self._sessions_file_location, 'r') as file_content:
            sessions_file = json.load(file_content)

        self.assertTrue("session" not in sessions_file)

    def _get_session_id_from_file(self):
        with open(self._sessions_file_location, 'r') as file_content:
            sessions_file = json.load(file_content)

        return sessions_file["session"]

    def _remove_session_id_from_file(self):
        with open(self._sessions_file_location, 'w+') as file_content:
            json.dump({}, file_content)

    def _set_session_id_in_file(self, session_id):
        with open(self._sessions_file_location, 'w+') as file_content:
            json.dump({"session": session_id}, file_content)

    def _compare_series_results(self, series_results):
        self.assertEqual(self._max_series_per_request, len(series_results.data))
        for series_result in series_results:
            for series in series_result.data:
                self.assertTrue(series.entity_id in self._series_ids_list)
