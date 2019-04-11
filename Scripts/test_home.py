from time import sleep

from Page.page import Page


class TestHome:
    def setup(self):
        self.action = Page().init_page_home

    def teardown(self):
        self.action.driver.quit()

    def test_enter_page(self):
        self.action.into_page()
        sleep(2)
