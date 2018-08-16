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
for ch in tvp.getchannels():
    for child in ch.find("a", {"href": True}):
        print(child)
#html = urlopen("http://www.pythonscraping.com/pages/page3.html")
#bsObj = BeautifulSoup(html, 'html.parser')
#print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
