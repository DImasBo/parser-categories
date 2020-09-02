
import os	
from datetime import datetime
import config 
from luxel import ClientLuxel
from multiprocessing import Pool

from utils import write_file_result


def luxel_map(link):
	offer = ClientLuxel().parser_product(link)
	print("--------------")
	print(offer.title)
	print(offer.url)
	print(offer.price)
	print("--------------")
	write_file_result(offer)

if __name__ == '__main__':
	with open(config.LUXEL_RESULT_FILE, "w")as f:
		pass

	luxel = ClientLuxel()
	for category in config.LUXEL_CATEGORIES:
		data_category = luxel.parser_categories_link(category)
		
		with Pool(config.LUXEL_FLOWS) as p:
			p.map(luxel_map, data_category['product_link_list'])