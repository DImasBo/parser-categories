# -*- coding: utf-8 -*-
import requests
import config

def formater_csv_write(text):
	if text:
		return str(text).replace(","," ")
	return ""

def get_user_agent(url, headers={}):
	list_user_agent = []
	with open(config.USER_AGENT_FILE) as f:
		list_user_agent = f.read().split("\n")

	for user_agent in list_user_agent:
		headers['User-Agent'] = user_agent
		r = requests.get(url,headers=headers)
		if r.status_code==200:
			return user_agent

def write_file_result(offer):
	with open(config.LUXEL_RESULT_FILE,"a") as f:

		f.write("{},{},{},{},{},{}".format(
			offer.title.replace(",","|"),
			offer.price.replace(",","|"),
			offer.currency,
			offer.sku.replace(",","|"),
			offer.status,
			offer.url.replace(",","|") if offer.url else "Not found",
			))
		
		f.write("," + " | ".join(offer.pictures))
		
		f.write(",")
		for param in offer.params:
			f.write("[" + "|".join(param)+ " ]")
		
		
		f.write("\n")