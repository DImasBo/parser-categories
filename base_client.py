import requests
import config
from utils import get_user_agent
from bs4 import BeautifulSoup

class BaseClient:
	"""
	Base class parser 
	
	"""
	headers = {}
	category_link_list = None
	site = None

	def set_user_agent(self):
		""" if the site is 403 Forbidden request then we change User-Agent"""
		self.headers['User-Agent'] = get_user_agent(self.site)		

	def __init__(self, *args, **kwargs):
		self.set_user_agent()
		self.headers=kwargs.get("headers",{})
		self.category_link_list = kwargs.get("category_link_list")

	def get(self,url):
		""" 
		client get request GET method 
		if status is 403  call method set_user_agent 
		if status is 200 to return result request
		else other status return request
		"""
		r = requests.get(url, headers=self.headers)
		if r.status_code == 200:
			return r
		elif r.status_code==403:
			self.set_user_agent()
			return self.get(url)
		return r

	def parser_categories_link(self, url, limit=100):
		"""
			search product links and title category

			return {
				'title_category':title_category,
				'product_link_list':offers,
				'page_count':page_count
			}
		"""
		pass

	def parser_product(self, url):
		"""
		It collects information for product
		return object Offer 
		"""
		pass