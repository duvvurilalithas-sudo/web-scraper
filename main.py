import requests
from bs4 import BeautifulSoup

print("Fetching headlines...")

url = "https://news.ycombinator.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("span", class_="titleline")

    file = open("headlines.txt", "w", encoding="utf-8")

    count = 1

    for headline in headlines:
        text = headline.text
        print(str(count) + ". " + text)
        file.write(str(count) + ". " + text + "\n")
        count += 1

    file.close()

    print("\nDone!")
    print("Headlines saved in headlines.txt")

else:
    print("Could not fetch website.")