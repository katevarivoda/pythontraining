# -*- coding: utf-8 -*-
import pytest
from model.address import Address
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact(
        Address(last_name="KateN", first_name="first_name", address="Minsk", phone="12345678", address2="Belarus",
                note="Very important"))
    app.session.logout()
