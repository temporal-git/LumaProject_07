from selenium.webdriver.remote.webelement import WebElement

from base.base_page import BasePage
from data.locators import OrdersAndReturnsPageLocators


class OrdersAndReturnsPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/sales/guest/form/"

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def order_id_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.ORDER_ID_FIELD)

    def error_msg_order_id_not_filled(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.ORDER_ID_FIELD_MESSAGE_ERROR)

    def billing_lastname_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.BILLING_LASTNAME_FIELD)

    def error_msg_billing_lastname_not_filled(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.BILLING_LASTNAME_FIELD_MESSAGE_ERROR)

    def find_order_by_dropdown(self) -> WebElement:
        return self.is_clickable(OrdersAndReturnsPageLocators.FIND_ORDER_BY_DROPDOWN)

    def email_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.EMAIL_FIELD)

    def error_msg_email_not_filled_or_incorrect_type(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.EMAIL_FIELD_MESSAGE_ERROR)

    def billing_zip_code_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.ZIP_FIELD)

    def error_msg_billing_zip_code_not_filled(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.ZIP_FIELD_MESSAGE_ERROR)

    def continue_button(self):
        return self.is_clickable(OrdersAndReturnsPageLocators.CONTINUE_BUTTON)

    def select_find_order_by_zip_code_dropdown(self):
        self.find_order_by_dropdown().click()
        return self.is_clickable(OrdersAndReturnsPageLocators.FIND_ORDER_BY_ZIP_CODE_DROPDOWN).click()

    def name_billing_zip_code_field(self):
        return self.is_visible(OrdersAndReturnsPageLocators.NAME_ZIP_CODE_FIELD)

    def select_find_order_by_email_dropdown(self):
        self.find_order_by_dropdown().click()
        return self.is_clickable(OrdersAndReturnsPageLocators.FIND_ORDER_BY_EMAIL_DROPDOWN).click()

    def name_email_field(self):
        return self.is_visible(OrdersAndReturnsPageLocators.NAME_EMAIL_FIELD)

    def fill_all_field_with_email(self, order_id, billing_lastname, email):
        self.open()
        self.order_id_field().send_keys(order_id)
        self.billing_lastname_field().send_keys(billing_lastname)
        self.email_field().send_keys(email)
        return self

    def fill_all_field_with_zip_code(self, order_id, billing_lastname, zip_code):
        self.open()
        self.order_id_field().send_keys(order_id)
        self.billing_lastname_field().send_keys(billing_lastname)
        self.select_find_order_by_zip_code_dropdown()
        self.billing_zip_code_field().send_keys(zip_code)
        return self

    def order_id_not_filled(self, billing_lastname, email):
        return self.fill_all_field_with_email(order_id='', email=email, billing_lastname=billing_lastname)

    def billing_last_name_not_filled(self, order_id, email):
        return self.fill_all_field_with_email(order_id=order_id, email=email, billing_lastname='')

    def email_not_filled(self, order_id, billing_lastname):
        return self.fill_all_field_with_email(order_id=order_id, email='', billing_lastname=billing_lastname)

    def zip_code_not_filled(self, order_id, billing_lastname):
        return self.fill_all_field_with_zip_code(billing_lastname=billing_lastname, order_id=order_id, zip_code='')

    def fill_incorrect_email_to_email_field(self, order_id, billing_lastname):
        return self.fill_all_field_with_email(order_id=order_id, email='damarewfmail.com',billing_lastname=billing_lastname)

    def text_order_number_on_check_page(self):
        return self.is_visible(OrdersAndReturnsPageLocators.ORDER_NUMBER_ON_CHECK_PAGE)
