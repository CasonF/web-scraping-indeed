import pandas as pd
from bs4 import BeautifulSoup as bs
import openpyxl #Though this is not actively used, it is necesssary to output the .xlsx file
import requests

# List of urls pertaining to software development, including data scientist, mathematics, web and app development, etc.
urls = ["https://www.indeed.com/jobs?q=software%20developer&explvl=entry_level&start=",
        "https://www.indeed.com/jobs?q=programmer%20entry%20level&l&vjk=b8846c0e319304b7",
        "https://www.indeed.com/jobs?q=game%20development&l&vjk=31546babe1f4361e",
        "https://www.indeed.com/jobs?q=game%20developer&explvl=entry_level&vjk=4a0b43f7367fdc00",
        "https://www.indeed.com/jobs?q=app%20development&l&vjk=ceda273c03361b4c",
        "https://www.indeed.com/jobs?q=app%20developer&explvl=entry_level&vjk=1fb806041e570f00",
        "https://www.indeed.com/jobs?q=data%20scientist&l&vjk=bbe9c1b053eb2c04",
        "https://www.indeed.com/jobs?q=data%20scientist%20entry%20level&l&vjk=bbe9c1b053eb2c04",
        "https://www.indeed.com/jobs?q=software%20tester&l&vjk=f12c19c528950259",
        "https://www.indeed.com/jobs?q=software%20tester&explvl=entry_level&vjk=e243fd48902ee956",
        "https://www.indeed.com/jobs?q=web%20developer&l&vjk=6e29a176002ed1f5",
        "https://www.indeed.com/jobs?q=web%20developer%20entry%20level&l&vjk=4790f93c363dc96e",
        "https://www.indeed.com/jobs?q=mathematics&l&vjk=36e81d08789491ee",
        "https://www.indeed.com/jobs?q=mathematics&explvl=entry_level&vjk=f30ecb8015e54dae"]

titles = []  # List of job titles
locations = []  # List of locations where jobs are posted
companies = []  # List of companies hiring for the job
salaries = []  # List of salaries for jobs

# Parses each url in the above list and appends more data to corresponding list
for url in urls:
    link = requests.get(url)
    soup = bs(link.text, 'html.parser')

    # On the indeed website, each job card item has the same information in the same relative place
    # For example, the job title can be found in the h2 tag where one of its classes contains "jobTitle"
    # Then, for each of these elements found on the page, we take the text where it's stored
    # in the <span title=></span> child of the h2 tag and return the text using .text
    title = soup.find_all('h2', attrs={'class': 'jobTitle'})
    for t in title:
        nt = t.find('span', attrs={'title': True})
        print(nt.text)  # Debug
        titles.append(nt.text)

    location = soup.find_all('div', attrs={'class': 'companyLocation'})
    for l in location:
        print(l.text)  # Debug
        locations.append(l.text)

    company = soup.find_all('span', attrs={'class': 'companyName'})
    for c in company:
        print(c.text)  # Debug
        companies.append(c.text)

    jobs_divs = soup.find_all('div', attrs={'class': 'salary-snippet'})
    for div in jobs_divs:
        salary = div.find('span')
        print(salary.text)  # Debug
        if salary:
            salaries.append(salary.text)
        else:
            salaries.append('Not shown')

# Tried numpy but it ran into issues with concatenation length, so now we're using list(zip()) to stack the lists
dataframe = pd.DataFrame(list(zip(titles, locations, companies, salaries)),
                         columns=['Title', 'Location', 'Company', 'Salary/Pay'])

dataframe.to_csv("indeed.csv", index=False) # Outputs the .csv file (can be viewed in Python)
dataframe.to_excel("indeed.xlsx", index=False) # Outputs the .xslx file (need Excel to open it)
