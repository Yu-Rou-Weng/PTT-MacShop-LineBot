import requests
from bs4 import BeautifulSoup


# Temp DB and Dic model for comparing message
topicDb = []
topicDic = dict()

# key-value Pair
productList = {"AirPods": ["Airpods", "AirPods", "airpods","Airpod2","airpods2","AirPods2","Airpods2","airpods3","Airpod","Air Pods2","Air Pods","Air pods3","Airpods2(bts)","airpods 2"],  
               "MacBook": ["MacBook", "Macbook", "macbook"],
               "iPhone": ["iPhone", "iphone","IPHONE","Iphone"],
               "iPad": ["ipad", "iPad","Ipad"],
               "Pencil": ["pencil", "Pencil"],
               "Watch": ["watch", "Watch"],
               "iMac": ["iMac", "imac"],
               }



def ptt_alert(keyword):
    global i
    global title_list
    title_list=[]
    global z
    z=1
    try:
        URL="https://www.ptt.cc/bbs/MacShop/index.html"
        for i in range(3):
            RES=requests.get(URL)
            soup = BeautifulSoup(RES.text, "html.parser")
            for article in soup.select('.r-list-container .r-ent .title a'):
                title = article.string
                href = "https://www.ptt.cc/" + article["href"] 
                # Filter: seller
                if ("[販售]" in title) and ("售出" not in title):
                    topicDic = {"title": title, "href": href}
                    # Save new topic in DB
                    if topicDic not in topicDb:
                        topicDb.append(topicDic)
                    
            URL = "https://www.ptt.cc/"+soup.find("a", string="‹ 上頁")["href"]
    
        # Check whether keyword in DB each round
        for index in topicDb: 
            for checkCorrectWord in productList[keyword]:
                if checkCorrectWord in index["title"]:
                    # For Testing can be eliminated.
                    #print(index["title"],index["href"])
                    temp="["+str(z)+"]  "+index["title"]+"\n"+index["href"]
                    title_list.append(temp)
                    #print('\n'.join(title_list))
                    index['sent'] = True
                    z+=1  
        
        
        return '\n'.join(title_list)  
    except Exception as e:
        print('執行期間錯誤：%s' %(e))
