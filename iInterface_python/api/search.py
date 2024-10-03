from iInterface_python.api.base_api import BaseApi


class Search(BaseApi):

    def searchmov(self,movname):
        data = {
            "url":"https://search.douban.com/movie/subject_search",
            "method":"get",
            "params":{
                "search_text":movname,
                "cat":"1002"
            }
        }
        r = self.request(data)
        return r