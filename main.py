from urllib.request import urlopen
from bs4 import BeautifulSoup

class TvProgram:
    def getchannels(self):
        html = urlopen("http://www.cn.ru/tv/")
        bsobj = BeautifulSoup(html, 'html.parser')
        allch = bsobj.find_all("div", {"class": "mtv-lastrec tdr"})
        return allch

    def getprogram(self, ch):
        pass


class TvList:
    pass


tvl = TvList()
tvp = TvProgram()

html = urlopen("http://www.cn.ru/tv/")
bsobj = BeautifulSoup(html, 'html.parser')
allch = bsobj.find_all("div", {"class": "mtv-lastrec tdr"})

