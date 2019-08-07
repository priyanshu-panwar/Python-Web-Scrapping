'''
This is a Quote Guessing Game.
Quotes are scraped from :
http://quotes.toscrape.com
'''

import requests
from bs4 import BeautifulSoup
from time import sleep # To give time lag between requests
from random import choice

BASE_URL = 'http://quotes.toscrape.com'

def scrape_quotes():
	all_quotes = []
	url = '/page/1'
	while url:
		response = requests.get(f'{BASE_URL}{url}')
		soup = BeautifulSoup(response.text, "html.parser")
		quotes = soup.find_all(class_ = 'quote')
		for quote in quotes:
			all_quotes.append({
				'text': quote.find(class_ = 'text').get_text(),
				'author': quote.find(class_ = 'author').get_text(),
				'bio-link': quote.find('a')['href'],
				})

		next_btn = soup.find(class_ = 'next')
		url = next_btn.find('a')['href'] if next_btn else None
		# sleep(2)
	return all_quotes

def start_game(quotes):
	quote = choice(quotes)
	remaining_guesses = 4
	print("Here's a quote: ")
	print(quote['text'])
	guess = ''
	while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
		guess = input(f'Who said this quote? Guesses remaining : {remaining_guesses} ---> ')
		remaining_guesses -= 1

		if guess.lower() == quote['author'].lower():
			print("****Hey you got it right ****")
			break

		if remaining_guesses == 3:
			res = requests.get(f"{BASE_URL}{quote['bio-link']}")
			soup = BeautifulSoup(res.text, "html.parser")
			birth_date = soup.find(class_="author-born-date").get_text()
			birth_place = soup.find(class_="author-born-location").get_text()
			print(f"Here's a hint: The author was born on {birth_date} {birth_place}")

		elif remaining_guesses == 2:
			print(f"Here's a hint: The author first name starts with {quote['author'][0]}")

		elif remaining_guesses == 1:
			last_initial = quote['author'].split(' ')[-1][0]
			print(f"Here's a hint: The author last name starts with {last_initial}")

		else:
			print(f"Sorry you ran out of guesses. The answer is {quote['author']}")

	again = ''
	while again.lower() not in ('y', 'yes', 'n', 'no'):
		again = input('Would you like to play again (y/n)?')
	if again.lower() in ('yes', 'y'):
		print("OK let's play again")
		return start_game(quotes)
	else:
		print("OK, GOODBYE")

quotes = scrape_quotes()
start_game(quotes)
input('*****THANK YOU******')