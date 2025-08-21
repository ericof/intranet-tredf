from plone import api
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.restapi.testing import RelativeSession
from zope.component.hooks import site

import pytest
import transaction


@pytest.fixture()
def request_factory(portal):
    """Fixture de pytest para chamadas à API REST do Plone."""

    def factory():
        url = portal.absolute_url()
        api_session = RelativeSession(url)
        api_session.headers.update({"Accept": "application/json"})
        return api_session

    return factory


@pytest.fixture()
def anon_request(request_factory):
    """Fixture de pytest para chamadas anônimas à API REST do Plone."""
    return request_factory()


@pytest.fixture()
def manager_request(request_factory):
    """Fixture de pytest para chamadas como Manafer à API REST do Plone."""
    request = request_factory()
    request.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
    yield request
    request.auth = ()


@pytest.fixture
def portal(functional):
    """Fixture de pytest que cria e retorna um portal Plone."""
    portal = functional["portal"]
    with site(portal), api.env.adopt_roles(["Manager"]):
        api.content.create(
            type="Document",
            id="documento",
            title="Exemplo de documento",
            container=portal,
        )
        transaction.commit()
    return portal
