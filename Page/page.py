from Base.get_dirver import driver
from Page.page_address import PageAddress
from Page.page_home import PageHome
from Page.page_myself import PageMyself


class Page:

    def __init__(self):
        self.driver = driver()

    @property
    def init_page_home(self):
        return PageHome(self.driver)

    @property
    def init_page_myself(self):
        return PageMyself(self.driver)

    @property
    def init_page_address(self):
        return PageAddress(self.driver)



