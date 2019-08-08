# Python-Web-Scrapping
- Python Web Scrapping Projects with ```requests``` and ```BeautifulSoup```
## Quotes_Game.py
- This program extracts all the quotes from http://quotes.toscrape.com.
- Then it stores all the quotes of all pages in a list.
- Then a random quote is chosen from the list.
- User is asked to guess the author of it.
- User gets 4 chances and hints at every wrong guess.
- GamePlay: ![image](https://user-images.githubusercontent.com/51286676/62729929-97da9700-ba3c-11e9-8256-7f692f66dcb0.png)
- Quotes_Game_csv.py and Quotes_Scraper_csv.py does the same thing but they save all the quotes locally in a csv file first ```books.csv```

**********************************************************************************************************************************

# PROJECT - Scrape Books
- Modules Used : ```BeautifulSoup(from bs4)```, ```requests```, ```sqlite3``` 
- With ```requests``` and ```BeautifulSoup```, I extracted data from 'books.toscrape.com'.
- With ```sqlite3```, I stored all the data in a books.db database.
- Site used: http://books.toscrape.com/catalogue/category/books/history_32/index.html
- Screenshots:
![image](https://user-images.githubusercontent.com/51286676/62729332-5eedf280-ba3b-11e9-807e-ad3da49ad97d.png)
![image](https://user-images.githubusercontent.com/51286676/62729409-83e26580-ba3b-11e9-9195-2e35ac1fd4c9.png)


**********************************************************************************************************************************
## RithmSchoolBlog.py
- This program extracts data from http://rithmschool.com/blog.
- It extracts all the blogs titles, date, url.
- It stores all the data in a csv file - RithmSchoolBlog.csv

## RithmSchoolBlog-AllPages.py
- This program extracts data from http://rithmschool.com/blog OF ALL THE PAGES ON THE WHOLE WEBSITE.
- It extracts all the blogs titles, date, url.
- It stores all the data in a csv file - RithmSchoolBlog-AllPages.csv

**********************************************************************************************************************************
