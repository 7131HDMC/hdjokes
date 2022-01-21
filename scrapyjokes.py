import scrapy

class JokesSpider(scrapy.Spider):
	name = "JokesSpider"
	start_urls = ['https://www.piadasnet.com/piada1928curtas.htm']

	def parse(self, response):
		yield {
		'joke' 		: response.xpath("*//p[@class='piada']/text()").get(),
		'category'  : response.xpath("*//h1/text()").get()
		}
		next_page = response.xpath("*//td/div[@class='seg']/a/@href").get()

		if next_page is not None:
			yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
