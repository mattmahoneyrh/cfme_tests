from cfme.fixtures import pytest_selenium as sel
from cfme.web_ui.menu import nav
from . import list_tbl

nav.add_branch(
    'middleware_servers',
    {
        'middleware_servers_details':
            lambda ctx: list_tbl.click_cell('Provider', ctx['provider'].name)
    }
)


class Server(object):

    def __init__(self, name, provider):
        self.name = name
        self.provider = provider
        self.detail_page_suffix = 'servers_detail'

    def nav_to_server_view(self):
        sel.force_navigate('middleware_servers', context={
            'server': self, 'provider': self.provider})

    def nav_to_detailed_view(self):
        if not self._on_server_details_page():
            sel.force_navigate('middleware_servers_details', context={
                'provider': self})

    def _on_server_details_page(self):
        sel.ensure_browser_open()
        return sel.is_displayed_text('Local (Summary)')

    def validate_server_details(self):
        print("Server Detail Validation TBD")
