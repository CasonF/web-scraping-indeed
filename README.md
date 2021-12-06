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


1. This data consists of 4 rows–Title, Location, Company, and Pay/Salary–and they are all currently Strings (or char(255), maybe, if you pass them to SQL).


2. Each column consists of ~100 entries, where each row is directly related to its neighbor columns. The ~100 entries is somewhat variable depending on who runs the code, but it should provide >100 if nothing else.


3. As it currently stands, this data sink scrapes from several iterations of the indeed.com website. I have a urls list that is passed through a for loop, and each of those urls is scraped using BeautifulSoup and appended to lists containing information relevant to each aforementioned row (Title, Location, Company, Pay), and finally the data is put into a data frame before getting exported as a .csv and .xlsx.


4. A quick breakdown of each column:
Title–This is the job title shown on the job card. This could range form software developer to analyst to data scientist, etc.
Company–This is the company that is hiring OR it is the recruiting agency that is hiring for another company.
Location–This is roughly where the company is hiring out of. If there are several locations listed, it is most likely a recruiting agency.
Pay/Salary–This is the expected pay grade you would receive if you started at this position. It is currently a String (like the rest of the data, or a char(), but it should be easy to split or parse it).


5. A couple ways this data could be used might be to:
A) Compare pay grades with job titles, as well as pay within specific cities or states.
B) Generate comparisons between companies/recruitment agencies to determine who is doing the most hiring for these positions, where they are stations out of, and what they're willing to pay.


6. Comma Separated Values (csv) and Excel Worksheet (.xlsx).
Let me know if you need it exported to SQL and I'll see what I can do in a few days' time.
