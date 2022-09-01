# PTT-MacShop-LineBot

###### *暑假與@jieyu891225協作的簡易小專案 —— 爬蟲+Line Bot實作。*

## 專案內容
 透過Line-Bot聊天機器人訂閱PTT-Macshop版上的特定產品(如：AirPods、iPhone、MacBook等)。使用者輸入搜尋關鍵字，機器人會爬取PTT-Macshop前三頁該產品的販售資訊，立即回覆給使用者文章標題、網址(手機板可看到文章內圖片縮圖)

## 使用教學
### 使用須知
* 一般使用者：加入我們 LineBot ID:**```@771ngxtr```** 即可使用該服務<br /><br />
* 自行創建LineBot: 依照指示跑此專案，需先在本機下載最新版本的**Python**、**Git套件**、**創建Heroku帳號**、**創建LineBot帳號**<br /><br />

一、創建Line Bot 帳號
-------------
1. 進入**Line Developer**官方網站，使用自己的Line帳號登入**👉網址:https://developers.line.biz/zh-hant/**<br /><br />
2. 進入**Provider**頁面，點選**Create**按鈕，依照要求為**Provider Name**輸入名字，這就會是你LineBot機器人的名字，填完按**Create**儲存<br />
3. 點選我們剛創完的Provider，點擊畫面的**Create a Messaging API channel**<br /><br />
4. 接著會進到**Create a new channel**畫面，這裡僅需把必填的欄位給入正確資訊即可，頭像的圖片(**icon**)可以依自身喜好新增，按**create**後屬於你自己的LineBot就建好啦!<br /><br />

二、創建Heroku服務空間
-------------
1. 首先到**Heroku官網**註冊帳號**👉網址:https://www.heroku.com/**<br /><br />
2. 創建完畢後點選網頁右上方的**New**底下**Create New APP**<br /><br />
3. **App Name**填入自己取的名字(ex:oreo-linebot)、**Choose a region**按照預設的**United States**即可，填完後按**Create app**<br /><br />

三、程式碼編輯
-------------
1. Git Clone此專案到本機上，在此資料夾下開啟**Visual Studio Code**<br /><br />(記得先刪除**README.md與圖片檔案**，否則稍後push專案到Heroku上可能會失敗)<br /><br />
2. 打開app.py檔，這裡須將程式碼中標記**My Channel Access Token**與**My Channel Secret**換成你剛才創好LineBot的Channel Access Token和Channel Secret<br /><br />
3. 進到Line Develop網站上剛才創好的PTT-Macshop-Bot<br /><br />
4. 進入**Basic Settings**頁籤中，看見**Channel secret**點選Issue後並把圖中代碼複製後貼到app.py對應的程式碼裡<br /><br />
5. 接著進入**Messaging API**頁籤，點選**Channel access token**旁的**Reissue**後，隨意給個24 hr，把跳出的一串代碼一樣複製到app.py對應的程式碼裡<br /><br />

四、連動Heroku與LineBot設定
-------------
1. 進到Heroku上你創建好的App裡(譬如我的叫做oreo-linebot)<br /><br />
2. 點選**Settings**頁籤，複製圖中**Your app can be found at**後的網址<br /><br /> 
3. 進入你的Line Developer在**Webhook URL**複製剛才的網址並在後面加上```/callback```後儲存<br /><br />
4. 下方有個**Use webhook**要按開啟<br /><br />
5. 下方有**Auto-reply messages**(Line Bot自動回覆訊息功能)必須設為停用<br /><br />
6. **Greeting messages**可自行設定一開始加入LineBot好友所接收的歡迎訊息<br /><br />

五、上傳專案到Heroku
-------------
#### 登入Heroku
```
heroku login
```
#### 建立Git資料夾
```
git init
```
#### 綁定Heroku APP服務空間
```
heroku git:remote -a APP Name
```
#### 資料夾下已建好heroku_push.bat檔案
##### 上傳檔案指令
```
git add .
git commit -m "your message"
git push heroku master
```

#### 在cmd下指令即可將專案上傳到Heroku伺服器上運行
```
heroku_push.bat
```
<br /><br />

六、使用APP
-------------
#### <br />🎉回到Line Developer掃描Line Bot的QRcode就可以和機器人互動了!<br /><br />

七、點選影片以跳轉到Youtube觀看Demo影片
-------------
[![IMAGE ALT TEXT](https://github.com/Yu-Rou-Weng/PTT-MacShop-LineBot/blob/master/%E9%A0%90%E8%A6%BD.jpg)](https://youtu.be/BAt43ldx5pA "PTT-MacShop-LineBot成果展示")

八、參考教學網址:
-------------
* [Maso萬事屋LineBot教學系列文章]https://ithelp.ithome.com.tw/users/20121176/ironman/3023
