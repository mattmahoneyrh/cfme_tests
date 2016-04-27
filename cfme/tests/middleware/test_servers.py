import pytest
from cfme.middleware.servers import Servers

from utils import testgen


def pytest_generate_tests(metafunc):
    # Filter out providers without provisioning data or hosts defined
    argnames, argvalues, idlist = testgen.middleware_providers(metafunc)
    testgen.parametrize(metafunc, argnames, argvalues, ids=idlist, scope="module")


@pytest.mark.usefixtures('setup_middleware_providers')
def test_server_details(provider):
    server = Servers(provider.name)
    # TODO
