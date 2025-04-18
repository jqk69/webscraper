from bs4 import BeautifulSoup
import requests
import csv
import os

url="https://www.scrapethissite.com/pages/forms/"
response=requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
teams = soup.find_all("tr",class_="team")
os.makedirs("../data",exist_ok=True)
filepath=os.path.join("../data","hockey_data.csv")
with open(filepath,mode="w", newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["Name", "Year", "Wins", "Losses", "PCT"])

    for team in teams:
        name=team.find("td",class_="name").text.strip()
        year=team.find("td",class_="year").text.strip()
        wins=team.find("td",class_="wins").text.strip()
        losses=team.find("td",class_="losses").text.strip()
        pct_win=team.find("td",class_="pct").text.strip()

        writer.writerow([name, year, wins, losses, pct_win])