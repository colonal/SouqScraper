from robobrowser import RoboBrowser, browser
import json
import csv


js = open("ScraperMemes.json", "w", encoding="utf8")
js.write("[\n")


browser = RoboBrowser(parser="lxml", history=True)

 
rang = int(input(": "))
csv_columns = ['name', 'category', 'price', 'img']
for i in range(1,rang+1):
    browser.open(f"https://imgflip.com/?page={i}")
    mem = browser.find_all("div",{"class":"base-unit clearfix"})
    
    for i in mem:
        img = i.find("img")
        if img:
            title = i.find("h2", {"class":"base-unit-title"})
            if title:
                print(img.get("src"))
                
                print(title.text)
                data = {"name":f"{title.text}", "img":f"{img.get('src')}"}   
                json_data = json.dumps(data, ensure_ascii=False)
                js.write(json_data)
                js.write(",\n")
            
js.write("\n]")
js.close()