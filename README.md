# web-scraping-indeed
Python program that scrapes indeed.com using BeautifulSoup and returns >100 job entries,
including the job title, its location, the hiring or recruiting company, and its pay/salary range.

Comments cover much of the idiosyncrasies present in the code itself.

Presently, urls list is hard-coded and non-variable, though the outputs vary slightly
each time the program isrun because of how indeed web pages are generated.

All data has been output in the form of strings (text) to .csv and .xlsx files,
but it should be relatively easy to split it and change its type to match your needs.

![Screenshot (140)](https://user-images.githubusercontent.com/75468526/139593968-49ebd303-1569-46ff-b713-1768b0df4a94.png)
.xlsx sample output
