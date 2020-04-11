__author__ = 'Ekaterina'

from selenium.webdriver.support import select

from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select



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
        self.change_field_value("nickname", address.nickname)
        self.change_field_value("middlename", address.middlename)
        self.change_field_value("title", address.title)
        self.change_field_value("company", address.company)
        self.change_field_value("address", address.address)
        self.change_field_value("home", address.homephone)
        self.change_field_value("homepage", address.homepage)
        self.change_field_value("address2", address.address2)
        self.change_field_value("notes", address.note)
        self.change_field_value("email", address.email)
        self.change_field_value("email2", address.email2)
        self.change_field_value("email3", address.email3)
        self.change_field_value("mobile", address.mobile)
        self.change_field_value("work", address.work)
        self.change_field_value("phone2", address.phone2)

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


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog window
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def delete_contact(self, contact_id, group_id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # wd.find_element_by_xpath("//select[@name='to_group']").click()
        # wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("//input[@name='add']").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None


    def select_contact_by_id(self, id):
        wd = self.app.wd
        # wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

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

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact(contact)
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
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(
                    Contact(last_name=last_name, first_name=first_name, id=id, address=address,
                            all_phones_from_home_page=all_phones,
                            all_emails_from_home_page=all_emails))
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
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id, address=address, homephone=homephone, mobile=mobile,
                       work=work, phone2=phone2, email=email, email2=email2, email3=email3)

    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobile=mobile, work=work, phone2=phone2)

    def contact_count(self):
        if self.app.contact.count() == 0:
            self.app.contact.redirect_to_contacts_tab()
            self.app.contact.add_contact(Contact(last_name="Ark"))
            self.app.contact.redirect_to_home_page()

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").click()
        select = Select(wd.find_element_by_name("to_group"))
        select.select_by_value(group_id)
        wd.find_element_by_xpath('//input[@value="Add to"]').click()
        wd.find_element_by_xpath('//i//*[contains(text(),"group page")]').click()

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("group").click()
        select = Select(wd.find_element_by_name("group"))
        select.select_by_value(group_id)
        # Select(wd.find_element_by_name("group")).select_by_visible_text("name")
        wd.find_element_by_name("group").click()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_name("remove").click()
        wd.find_element_by_link_text("home").click()



    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_id(id).click()

    def sort_by_group_by_id(self, group_id):
        wd = self.app.wd
        select = Select(wd.find_element_by_xpath('//select[@name="group"]'))
        select.select_by_value(group_id)

    def get_contact_info_by_id(self, contact_id):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_element_by_xpath('//td/*[@id="' + contact_id + '"]/../..')
        cells = row.find_elements_by_tag_name("td")
        id = cells[0].find_element_by_tag_name("input").get_attribute("value")
        firstname = cells[2].text
        lastname = cells[1].text
        address = cells[3].text
        all_emails = cells[4].text
        all_phones = cells[5].text
        return Contact(id=id, first_name=firstname, last_name=lastname, address=address,
                       all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones)