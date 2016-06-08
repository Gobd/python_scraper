from scrapy.spiders import Spider
from bs4 import BeautifulSoup
from craigslist_sample.items import CraigslistSampleItem

class MySpider(Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        # print(soup.prettify())
        entries = soup.select('span.pl')
        items = []
        for entry in entries:
            item = CraigslistSampleItem()
            item["title"] = entry.find('span', attrs={'id': 'titletextonly'}).get_text().encode("utf-8")
            item["link"] = 'http://sfbay.craigslist.org' + entry.find('a').get('href').encode("utf-8")
            items.append(item)
            print items

# var str = '\xe2\x9d\x80Bee Part of the Solution\xe2\x9d\x80Work W/Environment CA\xe2\x9d\x80 $10-15/hr';
#
# function decode_utf8(s) {
#   return decodeURIComponent(escape(s));
# }
#
# decode_utf8(str);