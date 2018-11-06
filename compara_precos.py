# -*- coding: utf-8 -*-
import scrapy

#scrapy runspider compara_precos.py

class ComparaPrecosSpider(scrapy.Spider):
    name = 'compara_precos'
    print("\nO programa mostra os preços das camisetas de uma marca específica")
    print('\nSe a marca tiver mais de uma palavra, digite o traço (-) como espaço')
    marca = input("\n\nDigie a marca: ")

    allowed_domains = ['https://www.dafiti.com.br/roupas-masculinas/camisetas/{0}/'.format(marca)]
    print(allowed_domains)
    start_urls = ['http://https://www.dafiti.com.br/roupas-masculinas/camisetas/{0}//'.format(marca)]
    print(start_urls)
    custom_settings = {'FEED_URI': 'camiseta/compara_precos.xlsx'}
    
    def parse(self, response):
        produto = response.css("img::attr(alt)").extract()
        preco = response.css(".product-box-price-from::text").extract()
        
        for item in zip (produto, preco):
            scraped_info = {'Produto': item[0], 'Preço': item[1]}
            
            yield scraped_info