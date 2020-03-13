__author__ = 'Ekaterina'

from model.address import Address


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def redirect_to_contacts_tab(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook.php") and len(wd.find_elements_by_name("selected[]")) > 0):
            wd.find_element_by_link_text("add new").click()

    def redirect_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def fill_contact(self, address):
        wd = self.app.wd
        self.change_field_value("firstname", address.first_name)
        self.change_field_value("lastname", address.last_name)
        # self.change_field_value("address", address.address)
        # self.change_field_value("mobile", address.phone)
        # self.change_field_value("address2", address.address2)
        # self.change_field_value("notes", address.note)
        # self.change_field_value("email", address.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_contact(self, address):
        wd = self.app.wd
        self.redirect_to_contacts_tab()
        self.fill_contact(address)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog window
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, address):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact(address)
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.redirect_to_home_page()
        return len(wd.find_elements_by_name('selected[]'))

    def count_edit(self):
        wd = self.app.wd
        self.redirect_to_home_page()
        return len(wd.find_element_by_xpath("//img[@alt='Edit']"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.redirect_to_home_page()
        contacts = []
        all_rows = wd.find_elements_by_css_selector("#maintable tr:not(:first-child)")

        for element in all_rows:
            cells = element.find_elements_by_tag_name("td")
            td_last_name = cells[1]
            text_last_name = td_last_name.text
            td_first_name = cells[2]
            text_first_name = td_first_name.text
            # td_address = cells[4]
            # text_address = td_address.text
            # td_email = cells[5]
            # text_email = td_email.text
            # td_phone = cells[6]
            # text_phone = td_phone.text

            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Address(last_name=text_last_name, first_name=text_first_name, id=id))
        return contacts

        # for element in all_rows:
        #     text = element.text
        #     id = element.find_element_by_name("selected[]").get_attribute("value")
        #     contacts.append(Address(last_name=text, id=id))
        # , address=text_address, phone=text_phone, address2=cells, note=cells, id=id, email=text_email)

    def add_contact_if_empty(self):
        if self.app.contact.count() == 0:
            self.app.contact.redirect_to_contacts_tab()
            self.app.contact.add_contact(Address(last_name="Ark"))
            self.app.contact.redirect_to_home_page()
