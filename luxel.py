import requests
import config

from bs4 import BeautifulSoup

from utils import get_user_agent

from bin.offer import Offer
from base_client import BaseClient


class ClientLuxel(BaseClient):
	"""
	
	"""
	category_link_list = config.LUXEL_CATEGORIES
	site = config.LUXEL_SITE

	def parser_categories_link(self, url, limit=100):
		r = self.get('{}?limit={}'.format(url,limit))
		s = BeautifulSoup(r.text, 'html.parser')

		pages = s.select('.pages ul li a')

		title_category = s.find('h1',{'class':'heading_titleh1'}).getText()
		page_count = int(pages[-1].getText()) if pages else 1
		offers = [ offer.find("a").get('href') for offer in s.findAll('div',{'class':'gred-slide'}) ]
	
		if page_count == 1:
			return {
				'title_category':title_category,
				'product_link_list':offers,
				'page_count':1
			}
		# парсим все товари з оствавшигся сторінках 
		for i in range(2,page_count+1):
			r = self.get('{}?limit={}&page={}'.format(url,limit,str(i)))
			s = BeautifulSoup(r.text, 'html.parser')
			offers += [ offer.find("a").get('href') for offer in s.findAll('div',{'class':'gred-slide'}) ]
		return {
			'title_category':title_category,
			'product_link_list':offers,
			'page_count':page_count
			}

	def parser_product(self, url):
		r = self.get(url)
		
		s = BeautifulSoup(r.text,'html.parser')
		offer = Offer(
			title=s.find('h1',{'class':'heading_titleh1'}).getText(),
			url= url, 
			price=s.select_one('.price').getText().replace("₴","").replace('\n',''),
			currency=config.LUXEL_CURRENCY_ID_DEFAULT,
			sku=s.select_one('.code_prod p').getText().replace('Артикул',"").replace(':',""),
			description=str(s.select_one('.tab-content .tab-pane')),
			category=config.LUXEL_CATEGORY_ID_DEFAULT,			
			)

		offer.pictures = [a.get("href") for a in s.select('.flexslider li a')]
		if 0 == len(offer.pictures):
			offer.pictures = [s.select_one('.large-image a').get('href'),]

		for tr in s.select('table.refactor tr'):
			tds = tr.findAll("td")
			if len(tds) == 2: 
				offer.params.append([
					tds[0].getText(),
					tds[1].getText(),
					])
		return offer

def test_parser_categories_link():
	luxel = LuxelParser()
	print(luxel.site)
	print(luxel.headers)
	offer_list_link = luxel.parser_categories_link(config.LUXEL_CATEGORIES[0],limit=50)
	print(offer_list_link)

# test_parser_categories_link()
def test_parser_product():
	url  = 'https://luxel.ua/svetodiodnoe--led--osveshhenie/led-ulichnie-svetilniki/ulichnij-svetilnik-lxsl-100c'
	luxel = LuxelParser()
	product = luxel.parser_product(url)
	print(product)
# test_parser_product()