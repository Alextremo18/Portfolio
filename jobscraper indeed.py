import requests
from bs4 import BeautifulSoup




URL = "https://au.indeed.com/jobs?q=developer&l&vjk=b566180b933c103c"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


results = soup.find(id="resultsCol")
mosaic = results.find(id="mosaic-zone-jobcards")

jobs = mosaic.find_all(class_="tapItem")

filename = "developerjobs.csv"

file = open(filename, "w")

headers = "Job Title, Company, Location, Date \n"

file.write(headers)

for job in jobs:
    jobtitle = job.find("h2", class_="jobTitle")
    jobcompany = job.find("span", class_="companyName")
    joblocation = job.find("div", class_="companyLocation")
    jobdate = job.find("span", class_="date")
    

    
    if jobtitle is None:
        jobtitleT = str("No job title")
    else:
        jobtitleT = jobtitle.text
        
    if jobcompany is None:
        jobcompanyT = str("No job company")
    else:
        jobcompanyT = jobcompany.text
        
    if joblocation is None:
        joblocationT = str("No job location")
    else:
        joblocationT = joblocation.text
        
    if jobdate is None:
        jobdateT = str("No job date")
    else:
        jobdateT = jobdate.text
        
    print('"' + str(jobtitleT) + '"' + " , " + '"' + str(jobcompanyT) + '"' + " , " + '"' + str(joblocationT) + '"' + " , " + '"' + str(jobdateT) + '"' + "\n")
    file.write('"' + str(jobtitleT) + '"' + " , " + '"' + str(jobcompanyT) + '"' + " , " + '"' + str(joblocationT) + '"' + " , " + '"' + str(jobdateT) + '"' + "\n")
    

print("done")
file.close

