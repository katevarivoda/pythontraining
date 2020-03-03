# -*- coding: utf-8 -*-
from model.address import Address


def test_add_contact(app):
    app.contact.add_contact(
        Address(last_name="KateN", first_name="Nikitina", address="Minsk", phone="12345678", address2="Belarus",
                note="Very important"))
