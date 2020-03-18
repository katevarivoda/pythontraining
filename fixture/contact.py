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
        self.change_field_value("address", address.address)
        self.change_field_value("homephone", address.homephone)
        self.change_field_value("address2", address.address2)
        self.change_field_value("notes", address.note)
        self.change_field_value("email", address.email)
        self.change_field_value("mobile", address.mobile)
        self.change_field_value("work", address.work)
        self.change_field_value("fax", address.fax)

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
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog window
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.redirect_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.redirect_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def edit_contact_by_index(self, index, address):
        wd = self.app.wd
        # self.select_contact_by_index(index)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact(address)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.redirect_to_home_page()
        return len(wd.find_elements_by_name('selected[]'))

    def count_edit(self):
        wd = self.app.wd
        self.redirect_to_home_page()
        return len(wd.find_element_by_xpath("//img[@alt='Edit']"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.redirect_to_home_page()
            self.contact_cache = []
            all_rows = wd.find_elements_by_name("entry")
            # wd.find_elements_by_css_selector("#maintable tr:not(:first-child)")
            for element in all_rows:
                cells = element.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                # element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(
                    Address(last_name=last_name, first_name=first_name, id=id, homephone=all_phones[0],
                            mobile=all_phones[1], work=all_phones[2]))
        return list(self.contact_cache)

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        return Address(first_name=firstname, last_name=lastname, id=id, homephone=homephone, mobile=mobile,
                       work=work, fax=fax)

    def contact_count(self):
        if self.app.contact.count() == 0:
            self.app.contact.redirect_to_contacts_tab()
            self.app.contact.add_contact(Address(last_name="Ark"))
            self.app.contact.redirect_to_home_page()
