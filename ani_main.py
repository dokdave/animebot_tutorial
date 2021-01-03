import bs4
import requests
from bs4 import BeautifulSoup
import telebot

main_link = "https://www.animevost.org/"

def link_block(main_link):
	page = requests.get(main_link)
	soup = BeautifulSoup(page.content, 'html.parser')
	soups = soup.find_all('li')

	zhanr_dict = {}
	
	for i in soups:
		for j in i.find_all('a'):
			if ('/zhanr/' in j['href']) and (not j['href'].endswith('/zhanr/')):
				zhanr_dict[j.text] = main_link + j['href'][1:]
	return zhanr_dict
	
dict1 = link_block(main_link)
#zhanr_names = list(dict1.keys())
#zhanr_links = list(dict1.values())

#print(zhanr_names, zhanr_links)

def by_zhanr(searched_genre, genre_link):
	returned_dict = {}
	for i in range(1,10):
		try:
			page = requests.get(genre_link + 'page/' + str(i) + '/')
			soup = BeautifulSoup(page.content, 'html.parser')
			soups = soup.find_all('div', class_ = 'shortstoryHead')
			for j in soups:
				for k in j.find_all('a'):
					returned_dict[k.text] =  k['href']
		except:
			continue
	
	return returned_dict, searched_genre
		

#print(by_zhanr(zhanr_names[0], zhanr_links[0]))
