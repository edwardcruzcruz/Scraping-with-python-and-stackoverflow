from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


class Preguntas(Item):
    tag=Field()
    pregunta = Field()
    votos = Field()
    respuestas = Field()
    vistas = Field()

class StackOverFlow(Spider):
    name='stackoverflow'
    allowed_domains =['stackoverflow.com']
    start_urls=[
	"https://es.stackoverflow.com/?tab=active",
	"https://es.stackoverflow.com/?tab=featured",
	"https://es.stackoverflow.com/?tab=hot",
	"https://es.stackoverflow.com/?tab=week",
	"https://es.stackoverflow.com/?tab=month",
    ]
#//*[@id="question-mini-list"]
#//*[@id="question-summary-229718"]/div[2]/h3/a
    def parse(self,response):
	        
	sel = Selector(response)
        preguntas = sel.xpath('//div[@id="question-mini-list"]/div/div')
	#i=-1
    	for pregunta in preguntas:
            item = Preguntas()
	    string = response.request.url#obtengo la direccion desde la que estoy haciendo la solicitud con mi objeto respuesta
 	    item['tag'] = string.split('=')[1]
            item['pregunta'] = pregunta.xpath(
                './/h3/a/text()').extract()[0]
            item['votos'] = pregunta.xpath(
                './/div/span/text()').extract()[0]
	    item['respuestas'] = pregunta.xpath(
                './/div/span/text()').extract()[1]
	    item['vistas'] = pregunta.xpath(
                './/div/span/text()').extract()[2]
            yield item
	
