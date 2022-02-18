import scrapy
from scrapy.http.request import Request

class JokesSpider(scrapy.Spider):
	name = "JokesSpider"
	start_urls = ['https://www.piadasnet.com/']
	categoriesname = []
	jokes=[]
	categories=[]
	def parse(self, response):
		categoriesname = response.xpath("*//td[@class='menuEsq']/p[not(@class)]/a/text()").getall()

		categoriesurls = response.xpath("*//td[@class='menuEsq']/p[not(@class)]/a/@href").getall()

		print(categoriesurls)
		print(categoriesname)

		for idx, category in enumerate(categoriesname):
			next_page = categoriesurls[idx]
			# print('next_page = '+next_page)


			if category is not None and next_page is not None:
				yield Request(response.urljoin(next_page), meta={'category':category},callback=self.parsecategory)
				# yield {
				# 	category 		:  ,
				# # 'category'  : response.xpath("*//h1/text()").get()
				# }
		# 		self.categories[category]=self.jokes
		# 		self.jokes=[]
		# yield self.categories		


	def parsecategory(self, response):
		category=response.meta['category']
		# self.jokes.append(response.xpath("*//p[@class='piada']/text()").get())
		yield {
			'joke' 		:  response.xpath("*//p[@class='piada']/text()").get(),
			'category'  : category
		}
		next_page = response.xpath("*//td/div[@class='seg']/a/@href").get()

		if next_page is not None:
			yield scrapy.Request(response.urljoin(next_page), meta={'category':category}, callback=self.parsecategory)
