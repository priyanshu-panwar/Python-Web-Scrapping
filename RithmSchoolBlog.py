# https://www.rithmschool.com/blog
# We will find the following things of articles on blog:
# Title
# Date
# href link
# Save all of it to a csv file

import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.rithmschool.com/blog')
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all('article')

with open('RithmSchoolBlog.csv', 'w') as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(['Title', 'Link', 'Date'])

	for article in articles:
		a_tag = article.find('a')
		title = a_tag.get_text()
		url = a_tag['href']
		date = article.find('time')['datetime']
		csv_writer.writerow([title, url, date])

