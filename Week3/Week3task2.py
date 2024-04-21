import urllib.request as req
import ssl
import csv

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE

everything=[]
def getData(url):
    request = req.Request(url, headers={
    "cookie": "over18=1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })
    with req.urlopen(request, context=context) as response:
        data = response.read().decode("utf-8")
    import bs4 
    root=bs4.BeautifulSoup(data,"html.parser")
# getting likes and title and time --------------------------------------------------------------------------------------------------
    def getTime(subURL):
        subRequest = req.Request(subURL, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        })
        with req.urlopen(subRequest, context=context) as subResponse:
            subData = subResponse.read().decode("utf-8")
        subRoot = bs4.BeautifulSoup(subData, "html.parser")
        time = subRoot.find(string="時間")
        if time:
            time = time.findNext("span").string.split()[1:]
            rightTime = " ".join(time)
        else:
            rightTime = "Unknown"  # need placeholder otherwise runinto error
        return rightTime

    likes = root.find_all("div", class_="nrec")
    titles = root.find_all("div", class_="title")

    #putthing things together-----------------------------------------------------------------------------------------
    def getAll(title_text, like_count):
        all_data=[]
        for title, like in zip(titles, likes):
            title_text = title.a.string.strip() if title.a else ""  
            like_count = like.span.string.strip() if like.span else "" 
            if title.a:
                fullurl = "http://www.ptt.cc" + title.a["href"]
                theTime = getTime(fullurl)
            else:
                theTime="this is an empty string"
            # print(f"{title_text}, {like_count}", theTime)
            if title_text:
                all_data.append((title_text, like_count, theTime))
        return all_data

    all_data=getAll(likes,titles)
    # for item in all_data:
    #     title_text, like_count, theTime = item
    #     print(f"{title_text}, {like_count}, {theTime}")
    for item in all_data:
        everything.append(item)



#----------the page part---------------------------------------------------------------------------
    nextLink=root.find("a",string="‹ 上頁") 
    return nextLink["href"]

pageurl = "https://www.ptt.cc/bbs/Lottery/index.html"
count = 0
while count < 3:
    pageurl = "http://www.ptt.cc" + getData(pageurl)
    count += 1

#write into csv.-------------------------------------------------------------------------------------
with open("article.csv","wt",encoding='utf8',newline="") as fp:
    writer = csv.writer(fp,delimiter=",")
    writer.writerows(everything)

# csv_filename = "article.csv"

# with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(getData(pageurl))
#     count=0
#     while count<3:
#         pageurl="http://www.ptt.cc"+ getData(pageurl)
#         count+=1
    # # Write each attraction group to the CSV file
    # for mrt_station, attractions in attraction_groups.items():
    #     if len(mrt_station) !=0:
    #         csv_writer.writerow([f"{mrt_station}: {', '.join(attractions)}"])



