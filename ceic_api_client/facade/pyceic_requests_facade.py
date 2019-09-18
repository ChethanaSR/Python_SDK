from time import sleep
import six
import warnings

from ceic_api_client.rest import ApiException

import ceic_api_client.facade.pyceic_exception as ceic_exception_module


# TODO: Need unit tests
class CeicRequestsFacade(object):

    _MAX_REQUEST_COUNT = 4
    _PROGRESSIVE_DELAY_SECONDS_STEP = 2

    def make_request(self, api_call, *args, **kwargs):
        if six.PY3 or six.PY34:
            warnings.simplefilter("ignore", ResourceWarning)

        return self._make_api_call_recursively(api_call, 0, *args, **kwargs)

    def _make_api_call_recursively(self, api_call, count=0, *args, **kwargs):
        count += 1

        try:
            return api_call(*args, **kwargs)
        except ApiException as api_exception:
            try:
                ceic_exception = self._try_build_ceic_exception_from(api_exception)
            except ApiException as ae:
                if count >= self._MAX_REQUEST_COUNT:
                    ae.__suppress_context__ = True
                    raise ae

                delay_seconds = count * self._PROGRESSIVE_DELAY_SECONDS_STEP
                sleep(delay_seconds)

                return self._make_api_call_recursively(api_call, count, *args, **kwargs)

            ceic_exception.__suppress_context__ = True
            raise ceic_exception

    @staticmethod
    def _try_build_ceic_exception_from(api_exception):
        try:
            return ceic_exception_module.CeicException.build_ceic_exception_from(api_exception)
        except TypeError:
            raise api_exception
