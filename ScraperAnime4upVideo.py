from robobrowser import RoboBrowser
from colorama import init 
from termcolor import colored 


def main():
    browser = RoboBrowser(parser="lxml", history=True)


    site = "https://ww.anime4up.com/?search_param=animes&s="


    try:
        animes = input("Einter your name anime :")
        if animes == "999":
            exit()
        s = site+animes
        print(s)
        
        
        browser.open(s)
            
        name = browser.find_all("div",{"class":"col-lg-2 col-md-4 col-sm-6 col-xs-6 col-no-padding col-mobile-no-padding"})
        data = {}
        #print(len(name))
        if len(name )  == 0:
            print("Sorry,no contents found")
            main()
        
        
        for i in name:
            url = i.find("h3").find("a").get("href")
            titil = i.find("h3").find("a").text
            data[titil] = url
            
        c = 1
        for i in data:
            print(f"{c}- {i}")
            c += 1
        index = input("Enter your namber anime: ")
        if index == "999":
            exit()
        
        AName = None
        c = 1
        for i in data:
            if int(index) == c:
                AName  = i
            c += 1
        print(AName, "\t\t", data[AName])
    except Exception as E:
        print(E)

    url = []


    try:
        browser.open(data[AName])
        a = browser.find_all("div", {"class":"col-lg-3 col-md-3 col-sm-12 col-xs-12 col-no-padding col-mobile-no-padding DivEpisodeContainer"})
        #print(a)
        if a == 0:
            print("Sorry, no contents found!")
        for i in a:
            url.append(i.find("a").get("href"))
                    

    except Exception as E:
        print(E)
    ################################################################

    browser = RoboBrowser(parser="lxml", history=True)
    linkes = [] 
    c = 1       
    for u in url:
        try:
            browser.open(u)
            
            li = browser.select('iframe', attrs={})
            for link in li:
                linkes.append(link.get('src'))
                print(f"Episode:{c}\t url: ",link.get('src'))
            c += 1
        except Exception as E:
            print("Error ", E)
        
    print("finsh :: ",len(linkes))

if __name__ == "__main__":
    init()
    s = colored("\033[96m {}\033[00m" .format("ww.anime4up"))
    w = colored("WELCOME", "green")
    e = colored("Exit: 999","red")
    print(f"""site: {s}\t\t  {w} \t\t\t {e}""")
    main()