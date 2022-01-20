import scrapy

class JokesSpider(scrapy.Spider):
	name = "JokesSpider"
	start_urls = ['https://www.piadasnet.com/piada1928curtas.htm']

	def parse(self, response):
		yield {
		'joke' 		: response.xpath("*//p[@class='piada']/text()").get(),
		'category'  : response.xpath("*//h1/text()").get()
		}

		# quotes = response.xpath('*//div[@class="quote"]')
		# for q in quotes:
		# 	yield {
		# 	'title': q.xpath(".//span[@class='text']/text()").get(),
		# 	'author': q.xpath('.//small[@class="author"]/text()').get(),
		# 	'tags': q.xpath(".//div[@class='tags']/a[@class='tag']/text()").getall()
		# 	}

		next_page = response.xpath("*//td/div[@class='seg']/a/@href").get()

		if next_page is not None:
			yield scrapy.Request(response.urljoin(next_page), callback=self.parse)