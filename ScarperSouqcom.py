from robobrowser import RoboBrowser
from  urllib.request import urlretrieve
import json

data = {}

browser = RoboBrowser(parser="lxml", history=True)

txt = open("ipple.txt", "w")
js = open("SouqDataApple.json", "w", encoding="utf8")
js.write("[\n")
pwd = "img"


for i in range(1,2):
    url = "https://egypt.souq.com/eg-ar/apple/s/?as=1&page="+str(i)
    print(url)
    browser.open(url)
    form = browser.find_all("div",{"class":"column column-block block-list-large single-item"})
    c = 0
    for i in form:
        c += 1
        img = i.find("img")
        Title = img.get('data-src')
        if Title:
            #urlretrieve(Title, f'{pwd}/{Title.split("/")[-1]}')
            ##########################
            title = i.find("a", {"class":"itemLink sk-clr2 sPrimaryLink"})

            #############################################
            price = i.find("h3",{"class":"itemPrice"})
            

            txt.write(title.text+"\t\t"+price.text+"\t\t"+Title+"\n\n")
            data["name"] = title.text.strip()
            data["price"] = price.text.strip()
            data["img"] = Title
            json_data = json.dumps(data, ensure_ascii=False)
            js.write(json_data)
            js.write(",\n")
            ############################################################
            print("Den: ",c)
js.write("\n]")
txt.close()
js.close()
# urlretrieve(_img, f'{pwd}/{Title}.jpg')
