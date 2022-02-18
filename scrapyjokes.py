import scrapy

class JokesSpider(scrapy.Spider):
	name = "JokesSpider"
	start_urls = ['https://www.piadasnet.com/']
	categoriesname = []

	def parse(self, response):
		categoriesname = response.xpath("*//td[@class='menuEsq']/p[not(@class)]/a/text()").getall()

		categoriesurls = response.xpath("*//td[@class='menuEsq']/p[not(@class)]/a/@href").getall()


		for idx, category in enumerate(categoriesname):
			next_page = categoriesurls[category]

			if category is not None and next_page is not None:
				yield {
					category 		:  scrapy.Request(response.urljoin(next_page), callback=self.parsecategory),
				# 'category'  : response.xpath("*//h1/text()").get()
				}


	def parsecategory(self, response):
		yield {
		'joke' 		: response.xpath("*//p[@class='piada']/text()").get(),
		# 'category'  : response.xpath("*//h1/text()").get()
		}
		next_page = response.xpath("*//td/div[@class='seg']/a/@href").get()

		if next_page is not None:
			yield scrapy.Request(response.urljoin(next_page), callback=self.parsecategory)
