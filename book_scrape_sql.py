import sqlite3
import requests
from bs4 import BeautifulSoup

def scrape_books(url):
	# Request URL
	response = requests.get(url)

	# Initialise BS
	soup = BeautifulSoup(response.text, 'html.parser')

	# Scrape data we want
	books = soup.find_all('article')
	all_books = []
	for book in books:
		book_data = (get_title(book), get_price(book), get_rating(book))
		all_books.append(book_data)
	save_books(all_books)
	
def get_title(book):
	return book.find('h3').find('a')['title']

def get_price(book):
	price = book.find(class_='price_color').get_text()
	# price = book.select('.price_color').get_text()
	return float(price.replace('Â£',''))	

def get_rating(book):
	ratings = {'Zero': 2, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
	rating = book.find(class_='star-rating').get_attribute_list('class')[1]
	return ratings[rating]

# Save data to a db
def save_books(all_books):
	conn = sqlite3.connect('C://sqlite/books.db')
	c = conn.cursor()
	#c.execute('''CREATE TABLE books
	#	(title TEXT, price REAL, rating INTEGER)''')
	c.executemany("INSERT INTO books VALUES (?, ?, ?)", all_books)
	conn.commit()
	conn.close()

# Call the main function
scrape_books('http://books.toscrape.com/catalogue/category/books/history_32/index.html')
