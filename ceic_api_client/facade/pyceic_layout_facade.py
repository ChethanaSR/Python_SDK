from ceic_api_client.apis.layout_api import LayoutApi


class CeicLayoutFacade(object):

    def __init__(self, ceic_configuration, ceic_requets_facade):
        self._ceic_configuration = ceic_configuration
        self._ceic_requests_facade = ceic_requets_facade

        self._layouts_api = LayoutApi(api_client=self._ceic_configuration.api_client)

    def get_layout_databases(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._layouts_api.get_layout_databases,
            **kwargs
        )

        return result

    def get_layout_database_topics(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._layouts_api.get_layout_topics,
            **kwargs
        )

        return result

    def get_layout_topic_sections(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._layouts_api.get_layout_sections,
            **kwargs
        )

        return result

    def get_layout_section_tables(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._layouts_api.get_layout_tables,
            **kwargs
        )

        return result

    def get_layout_table_series(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._layouts_api.get_layout_series,
            **kwargs
        )

        return result
