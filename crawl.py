
import scrapy
from bs4 import BeautifulSoup


class CityhHiveSpider(scrapy.Spider):
    name = 'City Hive spider'
    start_urls = ['https://www.cityhive.net/our-portfolio/']
    addresses = []

    def parse(self, response):
        # sel = scrapy.Selector(response)
        # results = sel.xpath("//*[contains(@id, 'photos-1')]")
        for next_page in response.css('a.gg-link'):
            yield response.follow(next_page, self.getAddress)

    def getAddress(self, response):
        sel = scrapy.Selector(response)
       

        results = sel.xpath("//*[contains(@class, 'media-text')]")[0]
        address = BeautifulSoup(results.extract(), 'html.parser').get_text()
        address = address.replace("A wine and liquor store located in ","")
        address = address.replace("A store located at ","")
        if address.find("USA") >= 0:
            addresses = open('addresses.txt', 'a')
            addresses.write("%s\n" % address)

            appname = sel.xpath("//*[contains(@class, 'media-heading text-center')]")[0] 
            appname = BeautifulSoup(appname.extract(), 'html.parser').get_text()
            appname = appname.replace('\' mobile app',"")
            appname = appname.replace('\'s mobile app',"")        

            appnames = open('appnames.txt', 'a')
            appnames.write("%s\n" % appname)
            
        else:
            other = open('other.txt', 'a')
            other.write("%s\n" % address)



        
