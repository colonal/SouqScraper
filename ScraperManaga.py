from robobrowser import RoboBrowser
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os
from requests import get
from selenium.webdriver.chrome.options import Options

browser = RoboBrowser(parser="html.parser", timeout=(5,10))

m = input("Enter name : ")
m = m.strip().replace(" ","+")
url = f"https://3asq.org/?s={m}&post_type=wp-manga"
print(url)
browser.open(url)

sersh = browser.find_all("div", {"class": "row c-tabs-item__content"})
s= {}
count = 1
for i in sersh:
    name = i.find("h3",{"class":"h4"}).find("a").text
    url = i.find("h3",{"class":"h4"}).find("a").get("href")
    s[name] = url
    print(f"{count}- {name}")
    count += 1
if count < 2:
    exit()   
index = int(input("Enter your nmber: "))

Name = ""
count = 1
for i in s:
    if count == index:
        Name = i
    count += 1
print(Name)

Name = Name.strip().replace(" ", "-")
url = f"https://3asq.org/manga/{Name}"
print(url)

WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)


browser1 = webdriver.Chrome(
                            chrome_options=chrome_options
                            )

browser1.get(url)
time.sleep(5)
html = browser1.page_source
soup = BeautifulSoup(html, 'lxml')


page = soup.find("ul",{"class","main version-chap"}).find_all("li")

browser1.close()
pages = []
for i in page:

    nam = i.find("a").text

    nam = nam.strip().split("-")[0].strip()
    pages.append(nam)

if os.path.exists(f"{Name}") == False :
    os.mkdir(f"{Name}")
for i in pages:
    print("\n")
    print(i)
    url1 = url+"/"+str(i)
    print(url1)
    browser.open(url1)
    img_ = browser.find_all("div", {"class":"page-break"})

    for I in img_:

        src = I.find("img").get("src")

        N = str(src).strip().split("/")[-1]
        N1 = f"{Name}\\page{i}_{N}"
        u = str(src).strip()
        print(u)
        B = get(u)
        with open(N1, "wb") as T:
            T.write(B.content)
        print("\n")