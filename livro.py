# -*- coding: utf-8 -*-
import scrapy
import pprint

class LivroSpider(scrapy.Spider):
    name = 'livro'
    #allowed_domains = ['https://busca.saraiva.com.br/pages/']
    #start_urls = ['http://https://busca.saraiva.com.br/pages//']

    #marca = input("\n\nDigie a marca: ".upper())

    #allowed_domains = ['https://www.kickante.com.br']
    #print(allowed_domains)
    print()
    print('1 - Livro')
    print('2 - E-Book')
    
    print()
    categoria = input('Digite uma das opções de categoria acima: ')
    print()
    
    if categoria=='1':
        start_urls = ['https://busca.saraiva.com.br/pages/livros']
        
        #pagina = 1
    
        #for i in range(1,11):
            #start_urls.append('https://www.empregos.com.br/vagas/{0}/p{1}'.format(emprego, i))
        
        
        #custom_settings = {'FEED_URI': 'Campanhas_animais.csv'}
        
        #def start_requests(self):
        #    for url in self.start_urls:
        #       yield SplashRequest(
        #         url = 'https://www.kickante.com.br/animais',
        #         callback = self.parse,
        #         #endpoint = 'render.html',
        #         args = {'wait':0.5}
        #            )
        
        
        def parse(self,response):
            for href in response.xpath("//h2[@class='nm-product-name']//@href").extract():
                url = response.urljoin(href)
                request = scrapy.Request(url, callback = self.parse_dir_contents, dont_filter =True)
                yield request
            
            
        def parse_dir_contents(self, response):
            
            titulo = response.xpath("//section[contains(@id, 'pdp-info')]/h1//text()").extract()
        #    while "\n" in titulo: titulo.remove("\n")
        #    
        #    arrecadado = response.css(".funding-raised.text-kickante::text").extract()
        #    
        #    meta = response.css("div::attr(data-goal)").extract()
        #    meta = [i[:-2] for i in meta]
        #   meta = [int(i) for i in meta]
        #    meta = [("R${:,}".format(i).replace(',', '.')+",00") for i in meta]
            
            #porcentagem = response.css(".progress-text::text").extract()
            
        #    data = response.css("div::attr(data-deadline-counter)").extract()
        #    data = [i[:-17] for i in data]
        #    
        #    link = response.xpath("//meta[@property='og:url']/@content").extract()
        #    
            for item in zip (titulo):
                scraped_info = {'Titulo': item[0]
        #                        'Meta': item[1], 
        #                        'Data Limite': item[2],
        #                        'Link':item[3],
        #                        'Arrecadado':item[4]
                               # '%': item[2]
                                }
            #    print(scraped_info)
            #    
                yield scraped_info
    
    
    