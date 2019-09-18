import urllib3
import json
import six
import warnings

import ceic_api_client.version as Version


class OutputColor(object):
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class PackageUpdateWarning(object):

    _WARNING_MESSAGE_TEMPLATE = OutputColor.YELLOW + \
                                "\n" + OutputColor.BOLD + "WARNING: " + OutputColor.END + \
                                OutputColor.YELLOW + "A new version of the CEIC Python SDK is available - {0}\n" \
                                "Current version is: {1}\n" \
                                "To get the latest features and bug-fixes, " \
                                "please consider updating your package with the following command:\n" \
                                "pip install --extra-index-url https://{2}/python ceic_api_client --upgrade" + \
                                OutputColor.END

    def __init__(self, configuration):
        self._configuration = configuration
        self._http = urllib3.PoolManager()

        self._latest_version = None

    def show_update_warning_if_needed(self):
        if not self._is_current_version_the_latest():
            self._show_update_warning()

    def _show_update_warning(self):
        warning_message = self._WARNING_MESSAGE_TEMPLATE.format(
            self._latest_version, Version.VERSION, self._configuration.python_package_url
        )

        warnings.warn(message=warning_message, category=UserWarning)

    def _is_current_version_the_latest(self):
        current_version = Version.VERSION.strip()
        self._latest_version = self._get_latest_package_version().strip()

        return current_version == self._latest_version

    def _get_latest_package_version(self):
        downloads_file = self._get_downloads_file()
        downloads_file = json.loads(downloads_file)

        return downloads_file["downloads"][2]["documentation"][0]["version"]

    def _get_downloads_file(self):
        if six.PY3 or six.PY34:
            warnings.simplefilter("ignore", ResourceWarning)
            warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)

        url = self._configuration.downloads_file_url

        response = self._http.request('GET', url)
        downloads_file = response.data.decode('UTF-8')

        return downloads_file


class AbuseWarning(object):

    _WARNING_MESSAGE = OutputColor.YELLOW + \
                       "\n" + OutputColor.BOLD + "WARNING: " + OutputColor.END + \
                       OutputColor.YELLOW + "The PyCEIC package is designed as direct\n" \
                       "interaction interface to CEIC macroeconomic data and\n" \
                       "any data usage abuse attempt will be recorded." + \
                       OutputColor.END

    def show_warning(self):
        warnings.warn(message=self._WARNING_MESSAGE, category=UserWarning)
