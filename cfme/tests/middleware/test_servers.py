import pytest
from cfme.middleware.servers import Servers

from utils import testgen


def pytest_generate_tests(metafunc):
    # Filter out providers without provisioning data or hosts defined
    argnames, argvalues, idlist = testgen.middleware_providers(metafunc)
    testgen.parametrize(metafunc, argnames, argvalues, ids=idlist, scope="module")



def test_server_details(provider, setup_provider):
    server = Servers(provider.name)
    # TODO

#    server.nav_to_detailed_view()

#    assert server.get_Properties_From_UI == server.get_Properties_From_Provider
#    assert server.get_Relationships_From_UI == server.get_Relationships_From_Provider
#    assert server.get_SmartManagement_From_UI == server.get_SmartManagement_From_Provider

