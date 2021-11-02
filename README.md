# web-scraping-indeed
Python program that scrapes indeed.com using BeautifulSoup and returns >100 job entries,
including the job title, its location, the hiring or recruiting company, and its pay/salary range.

Comments cover much of the idiosyncrasies present in the code itself.

Presently, urls list is hard-coded and non-variable, though the outputs vary slightly
each time the program is run because of how indeed web pages are generated.

All data has been output in the form of strings (text) to .csv and .xlsx files,
but it should be relatively easy to split it and change its type to match your needs.


![Screenshot (141)](https://user-images.githubusercontent.com/75468526/139594039-5bb4d3ba-5959-44e3-82c7-50653b2db169.png)
.xlsx sample output
