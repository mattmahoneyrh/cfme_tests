from cfme.fixtures import pytest_selenium as sel
from cfme.web_ui.menu import nav
from . import list_tbl

nav.add_branch(
    'middleware_deployments',
    {
        'middleware_deployments_details':
            lambda ctx: list_tbl.click_cell('Deployment Name', ctx['deployment'].deployment_name)
    }
)


class Deployment(object):

    def __init__(self, name, provider, deployment_name):
        self.name = name
        self.provider = provider
        self.deployment_name = deployment_name

    def nav_to_deployments_view(self):
        sel.force_navigate('middleware_deployments', context={
            'deployments': self, 'provider': self.provider})

    def nav_to_deployments_detailed_view(self, deployment_name):
        sel.force_navigate('middleware_deployments_details', context={
                'deployment': self})