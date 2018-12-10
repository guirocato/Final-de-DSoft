# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LivrosItem(scrapy.Item):
    titulo= scrapy.Item()
    preco = scrapy.Item()
    codigo = scrapy.Item()
    pagina = scrapy.Item()
    editora = scrapy.Item()
    autor = scrapy.Item()
    link = scrapy.Item()