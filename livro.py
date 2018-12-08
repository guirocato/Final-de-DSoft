# -*- coding: utf-8 -*-
import scrapy
import pprint
from urllib.parse import urljoin
import numpy as np
#from scrapy.http import Request

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
        start_urls = ['https://busca.saraiva.com.br/pages/livros/']
        
        #pagina = 1
    
        #for i in range(1,11):
            #start_urls.append('https://www.empregos.com.br/vagas/{0}/p{1}'.format(emprego, i))
        
        
        custom_settings = {'FEED_URI': 'Livros.csv'}
        
        #def start_requests(self):
        #    for url in self.start_urls:
        #       yield SplashRequest(
        #         url = 'https://www.kickante.com.br/animais',
        #         callback = self.parse,
        #         #endpoint = 'render.html',
        #         args = {'wait':0.5}m
        #            )
        
        
        def parse(self,response):
            categorias = response.xpath("//ul[contains(@class, 'neemu-category-filter-level neemu-category-filter-level-1 display-block')]/li/a/span[contains(@class,'neemu-filter-text')]//text()").extract()
            categorias = [i[45:] for i in categorias]
            cat = []
            n = 0
            print()
            print()
            print('             Selecione a categoria do livro que procura        '.upper())
            print()
            print()
            for i in categorias:
                opcoes = i
                cat.append(opcoes)
                print('                     {0} - {1}'.format(n, opcoes))
                n+=1
            #print(cat)
            decisao = int(input('\n\n\nDigite o número da categoria escolhida:'))
            link = response.xpath("//ul[contains(@class, 'neemu-category-filter-level neemu-category-filter-level-1 display-block')]/li/a[contains(@class,'neemu-filter-link')]//@href").extract()[decisao]
            link = link[42:]
            print(link)
            l_url = []
            base = 'https://busca.saraiva.com.br/pages/livros/'
            url1 = base+link
            print(url1)
            n = np.arange(1,5)
            for n in n:
            #url1 = response.urljoin(href1)
                url =  url1+'?page={0}'.format(n)
                l_url.append(url)
                
            print(l_url)
            for i in l_url:
                request = scrapy.Request(i, callback = self.parse_page_contents)
                yield request
            #request = scrapy.Request(url, callback = self.parse_page_contents, dont_filter =True)
            #yield request
            
       
        def parse_page_contents(self,response):
            
            link1 = response.xpath("//h2[@class='nm-product-name']//@href").extract()
            
            
            for href1 in link1:
                url = response.urljoin(href1)
                
                request = scrapy.Request(url, callback = self.parse_dir_contents)
                yield request
        
        def parse_dir_contents(self, response):
            
            titulo = response.xpath("//section[contains(@id, 'pdp-info')]/h1//text()").extract()
            
            preco = response.css("span::attr(data-price)").extract()
            
            #codigo = response.xpath("//span[@class='title_note']/text()").extract()
            #codigo = [i[6:-1] for i in codigo]
            
            intervalo = np.arange(1,15)
            
            codigo = 'X'
            for i in intervalo:
                c = response.xpath("//div[@class='overflow_container']/ul/li["+str(i)+"]/dl/dt/text()").extract()
                #print(p)
                if c==['Cód. Barras']:
                    codigo = response.xpath("//div[@class='overflow_container']/ul/li["+str(i)+"]/dl/dd/text()").extract()
                    codigo = [i[:-57] for i in codigo]
                    break
                else:
                    pagina= 'X'
                
        #    while "\n" in titulo: titulo.remove("\n")
        #    
        #    arrecadado = response.css(".funding-raised.text-kickante::text").extract()
        #   
        
            idioma = 'X'
            for i in intervalo:
                p = response.xpath("//div[@class='overflow_container']/ul/li["+str(i)+"]/dl/dt/text()").extract()
                #print(p)
                if p==['Idioma']:
                    idioma = response.xpath("//div[@class='overflow_container']/ul/li["+str(i)+"]/dl/dd/text()").extract()
                    idioma = [i[:-57] for i in idioma]
                    break
                else:
                    idioma= 'X'
        
            
            pagina = 'X'
            for i in intervalo:
                p = response.xpath("//div[@class='overflow_container']/ul/li["+str(i)+"]/dl/dt/text()").extract()
                #print(p)
                if p==['Número de Páginas']:
                    pagina = response.xpath("//div[@class='overflow_container']/ul/li["+str(i)+"]/dl/dd/text()").extract()
                    pagina = [i[:-57] for i in pagina]
                    break
                else:
                    pagina= 'X'
            
            editora = 'X'
            for i in intervalo:
                e = response.xpath("//div[@class='overflow_container']/ul/li["+str(i)+"]/dl/dt/text()").extract()
                #print(e)
                if e==['Marca']:
                    editora = response.xpath("//div[@class='overflow_container']/ul/li["+str(i)+"]/dl/dd/text()").extract()
                    editora = [i[:-57] for i in editora]
                    break
                else:
                    editora='X'
            
            autor = response.xpath("//div[@class='overflow_container content']/h3//text()").extract()
            #at = ''.join(autor)
            #autor1 = at.partition(",")[0]
            #autor2 = at.partition(",")[2]
            #autor = at
            
            
            #autor = [i[:-66] for i in autor]
            #autor = [i[61:-58] for i in autor]
       
        #    
          #  l = response.url
          #  l = [i[:] for i in l]
          #  link = ''.join(l)
          #  link = str(link)
          #  print(l)
          #  print(link)
        #    
            for item in zip (titulo,autor, editora, preco, pagina, idioma, codigo):
                scraped_info = {'Titulo': item[0],
                                'Autor': item[1], 
                                'Editora': item[2],
                                'Preço': item[3],
                                'Páginas':item[4],
                                'Idioma':item[5],
                                'Código de Barras': item[6],
                                #'Link': item[6],
                                }
            #    print(scraped_info)
            #    
                yield scraped_info