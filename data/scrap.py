import requests, re, os, bs4

img,judul,genre,author,chapter,status = [],[],[],[],[],[]
data = {}
info = {}

class Main:

    def __init__(self,key):
        self.key = key

    def tampil(self):
        return {"hello world!"}

class serachKomik(Main):

    def modol(self,url):
        r = bs4.BeautifulSoup(requests.Session().get(url, headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; SM-M115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36","referer":"https://mgkomik.com/","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","host":"mgkomik.com"}).text, "html.parser")
        #####################################################
        #scraping BeautifulSoup
        for d in r.find_all("div", {"class":"row c-tabs-item__content"}):
            #scraping images
            for i in d.find_all("div", {"class":"col-4 col-12 col-md-2"}):
                img.append(i.find("div").find("a").find("img").get("src"))

            #content data
            content = d.find_all("div", {"class":"col-8 col-12 col-md-10"})

            #scraping judul
            for i in content:
                judul.append(
                    i.find("div",{"class":"tab-summary"}).find("div",{"class":"post-title"}).find("h3").find("a").string
                )
            
            ####################################
            post_content = i.find("div", {"class":"tab-summary"}).find("div", {"class":"post-content"})

            #scraping author
            for i in content:
                for j in post_content.find_all("div",{"class":"post-content_item mg_author"}):
                    author.append(j.find("div",{"class":"summary-content"}).find("a").string)
            #scraping genre
            for i in content:
                for j in post_content.find_all("div",{"class":"post-content_item mg_genres"}):
                    b = []
                    for a in j.find_all("a"):b.append(a.string)
                    genre.append(b)

            #scraping status
            for i in content:
                for j in post_content.find_all("div",{"class":"post-content_item mg_status"}):
                    status.append(re.findall("(\w+)", j.find("div",{"class":"summary-content"}).string)[0])
            ####################################

            for i in content:
                for j in i.find_all("div", {"class":"tab-meta"}):
                    chapter.append(j.find("div", {"class":"meta-item latest-chap"}).find("span", {"class":"font-meta chapter"}).find("a").string)
        #####################################################

        for a,i,j,g,c,s in zip(author,img,judul,genre,chapter,status):
            data.update({
                j : {
                    "author":a,
                    "img":i,
                    "judul":j,
                    "genre":g,
                    "chapter":c,
                    "status":s
                }
            })
        info.update(
            {
                "data-info":data,
                "jumlah-hasil-pencarian":len(judul), "test":str(r)
            }
        )
        return info
