#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:00:02 2018

@author: roger
"""

# Para rodar o programa no Prompt:

#  scrapy runspider scraper.py


from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.item import Item, Field
from scrapy.http.request import Request

class Produto(Item):
    titulo = Field()
    preco = Field()



'''

f0 = estado (dar o .upper)
f1 = preco
f2 = quartos
f3 = suites
f4 = vagas
f5 = area (maximo 700)
f6 = bairro
f7 = zona
f8 = cidade
f9 = estado
f10 = ordem (dataAtualizacao)

'''

class ProcuraImoveis(CrawlSpider):
    name = "busca_apartamentos"
    allowed_domains = ['zapimoveis.com.br']
    produto = input('\n\n1 - Comprar\n2 - Alugar: \n\nSua escolha: ')
    
    if produto=='1' or produto=='comprar' or produto=='Comprar':
        estado = input('Digite a sigla do Estado: ')
        preco = input('Digite o preço máximo que deseja gastar: ')                    
        url =["""https://www.zapimoveis.com.br/venda/casas/{0}/#{{"precomaximo":"{1}","filtrodormitorios":"","filtrosuites":"","filtrovagas":"","areautilmaxima":"","parametrosautosuggest":[{{"Bairro":"","Zona":"","Cidade":"","Agrupamento":"","Estado":"{2}"}}],"pagina":1,"ordem":"","paginaOrigem":"ResultadoBusca","semente":"1612983926","formato":"Lista"}}""".format(estado, int(preco), estado.upper())]
        print(url)
        #print(url2)
    
    
    
    elif produto=='2' or produto=='alugar' or produto=='Alugar':
        estado = input('Digite a sigla do Estado: ')
        preco = input('Digite o preço máximo que deseja gastar: ')
        url = ["""https://www.zapimoveis.com.br/aluguel/casas/{0}/#{{"precomaximo":"{1}","filtrodormitorios":"","filtrosuites":"","filtrovagas":"","areautilmaxima":"","parametrosautosuggest":[{{"Bairro":"","Zona":"","Cidade":"","Agrupamento":"","Estado":"{2}"}}],"pagina":1,"ordem":"","paginaOrigem":"ResultadoBusca","semente":"1612983926","formato":"Lista"}}""".format(estado, int(preco), estado.upper())]
        print(url)
    
    def parse(self, response):
        s = Selector(response)
        pass
        #produtos = s.xpath(".//h2[contains(@class,'item__title list-view-item-title')]")
        #OL_SELECTOR = '.item__title list-view-item-title'
        #items = []
        #for produto in produtos:            
        #    item = {}
        #    item['titulo']= produto.xpath(".//span[contains(@class,'main-title')]/text()").extract()
            
            #NAME_SELECTOR = ".//a/span[contains(@class,'main-title')]/text()"
       #     items.append(item)
        
        
        
        #precos = s.xpath(".//div[contains(@class,'item__price')]")
        #prices = []
        #for preco in precos:
         #   prec = {}
          #  prec['preço em R$ '] = preco.xpath(".//span[contains(@class, 'price_fraction')]/text()").extract()
          #  prices.append(prec)
            
        
        #for item in items:
        #    yield item
        #for preco in prices:
         #   yield preco

#PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
