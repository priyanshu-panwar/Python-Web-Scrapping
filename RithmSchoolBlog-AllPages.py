# https://www.rithmschool.com/blog
# We will find the following things of articles on blog:
# Title
# Date
# href link
# Save all of it to a csv file
# We will collect 

import requests
from bs4 import BeautifulSoup
from csv import writer

i = 1
with open('RithmSchoolBlog-AllPages.csv', 'w') as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(['Title', 'Link', 'Date'])
	while True:
		link = 'https://www.rithmschool.com/blog?page=' + str(i)
		response = requests.get(link)
		if response.status_code != 200:
			break
		soup = BeautifulSoup(response.text, "html.parser")
		articles = soup.find_all('article')
		for article in articles:
			a_tag = article.find('a')
			title = a_tag.get_text()
			url = a_tag['href']
			date = article.find('time')['datetime']
			csv_writer.writerow([title, url, date])
		i=i+1