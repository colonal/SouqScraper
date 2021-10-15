from robobrowser import RoboBrowser
import json
import csv

browser = RoboBrowser(parser="lxml")

url = r"https://jo.opensooq.com/ar/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%88%D9%85%D8%B1%D9%83%D8%A8%D8%A7%D8%AA/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%84%D9%84%D8%A8%D9%8A%D8%B9?page=1"


file = open("ScraperCarsInOpenSouq.json", "w", encoding="utf-8")
filecsv = open('OpenSouqnew.csv', 'w', encoding='utf-8')
file.write("[\n")
dataj = {}
csv_columns = ['title','name','type','year', 'price',  'img']

for page in range(1,10):
    print("#"*15 + f"  page {page} " + "#"*15)
    browser.open(url=url+str(page))
    
    datas = browser.find_all("li", {"class":"rectLi relative mb15"})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    writer.writeheader()
    
    for i in datas:
        img = i.find("img")
        title = i.find("h2", {"class":"fRight mb15"})
        
        data = i.find("div", {"class":"rectCatesLinks mb15 mt15 clear"})
        price = i.find("span", {"class":"inline ltr"})
        
        if img and title and data and price:
            print("#"*15)
            print(str(title.text).strip())
            print(img.get("src"))
            data = data.find_all("span", {"class":"font-12 inline"})
            for I in data:
                print(I.get("title"))
            
            if len(data) > 3 :
                Title = str(title.text).strip()
                Name = str(data[1].text).replace("|", "").strip()
                Type = str(data[2].text).replace("|", "").strip()
                Year = data[3].text
                Price =  str(price.text).replace(",","")
                Img = img.get("src")
                ##############################
                dataj["title"] = Title
                dataj["name"] = Name
                dataj["Type"] = Type
                dataj["year"] = Year
                dataj["price"] = Price
                dataj["img"]  = Img
                json_data = json.dumps(dataj, ensure_ascii=False)
                file.write(json_data)
                file.write(",\n")
                try:
                    writer.writerow({'title': Title,
                                    'name': Name,
                                    'type':  Type,
                                    'year': Year,
                                    'price':Price,
                                    'img': Img
                                    })
                except:
                    pass
    print("#"*15 + f"  page {page} " + "#"*15)
            
print("Finsh")
file.write("\n]")
file.close()
filecsv.close()            
            
            
                
    
    