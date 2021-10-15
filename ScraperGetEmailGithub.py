from robobrowser import RoboBrowser
import re
browser = RoboBrowser(parser="lxml", history=True)



browser.open("https://github.com/login")
form = browser.get_form()

form["login"] = input("Enter your name in github: ")
form["password"] = input("Enter your password in github: ")

browser.submit_form(form)
###################################################

Email = []
page = input("Enter your namber range in page: ")
for i in range(1,int(page)+1):
    browser.open("https://github.com/search?p=1&q=python&type=Users")

    get = browser.find_all("div",{"class":"d-flex flex-wrap text-small color-text-secondary"})

    for i in get:
        x = i.find('a', attrs={'href': re.compile("^mailto:")})

        if x != None:
            E = x.get('href')
            if E not in Email:
                Email.append(E)
    
print(Email)

    
    
