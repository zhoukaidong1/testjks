import allure

from iInterface_python.api.search import Search

@allure.feature('test 豆瓣')
class TestSearch:

    def setup_class(self):
        self.search = Search()

    @allure.story('速度与激情')
    def test_search(self):
        r = self.search.searchmov('速度与激情')

    @allure.story('变形金刚')
    def test_search1(self):
        r = self.search.searchmov('变形金刚')

    @allure.story('新世界')
    def test_search2(self):
        r = self.search.searchmov('新世界')