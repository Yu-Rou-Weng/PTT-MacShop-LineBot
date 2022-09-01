# PTT-MacShop-LineBot
**暑假與@jieyu891225自學的簡易PTT Macshop版Line Bot**
****  
  **[使用須知]:<br />User：掃描我們的QRcode即可使用該服務<br />如果想下載此專案並自行創建LineBot請依下面指示<br />跑此專案需在本機下載最新版本的Python、Git套件、創建Heroku帳號、創建LineBot帳號**
****
一、創建Line Bot 帳號
=============
1.進入Line Developer官方網站，使用自己的Line帳號登入<br />網址:https://developers.line.biz/zh-hant/<br />
2.進入Provider頁面，點選Create按鈕，依照要求為自己的Provider Name輸入名字，這個就會是你LineBot機器人的名字，填完按Create儲存<br />
3.點選我們剛創完的Provider，點擊畫面的"Create a Messaging API channel"<br />
4.接著會進到Create a new channel畫面，這裡僅需把必填的欄位給入正確資訊即可，另外頭像的圖片(icon)可以依自身喜好新增，按create後屬於你自己的LineBot就建好啦!<br />
****
二、創建Heroku服務空間
=============
1.首先到Heroku官網註冊帳號<br />網址:https://www.heroku.com/<br />
2.創建完畢後點選網頁右上方的New底下Create New APP<br />
3.App Name填入自己取的名字(ex:oreo-linebot)、Choose a region按照預設的United States即可，填完後按Create app<br />
****
三、使用
=============
1.git Clone此專案到本機上，在此資料夾下開啟Visual Studio Code(記得先刪除README.md，否則稍後push專案到Heroku上可能會失敗)<br />
2.打開app.py，這裡須將程式碼中標記My Channel Access Token與My Channel Secret換成你剛才創好LineBot的Channel Access Token和Channel Secret<br />
3.進到Line Develop網站上剛才創好的PTT-Macshop-Bot<br />
4.進入Basic Settings頁籤中，看見Channel secret點選Issue後並把圖中代碼複製後貼到app.py對應的程式碼裡<br />
5.接著進入Messaging API頁籤，點選Channel access token旁的Reissue後，隨意給個24 hr，把跳出的一串代碼一樣複製到app.py對應的程式碼裡<br />
****
三、使用
=============
1.進到Heroku上你創建好的App裡(譬如我的叫做oreo-linebot)<br /> 
2.點選Settings頁籤，複製圖中Your app can be found at後的網址<br /> 
3.
****
四、上傳專案到Heroku
=============
1.打開VScode的Terminal進入cmd模式，接著打"heroku login"並登入自己的Heroku帳號<br />
2.登入完後下git init<br />
3.接著下heroku git:remote -a 你的app名稱(ex:oreo-linebot)<br /> 
4.在專案的資料夾底下已建好一個heroku_push.bat的檔案裡<br />
5.在heroku_push.bat已寫好下方指令:<br /><br />
git add . (把所有檔案加入)<br />
git commit -m "Final Success Version" (填寫commit資訊)<br />
git push heroku master (push到heroku上)<br /><br />
6.直接在cmd下heroku_push.bat指令即可將專案上傳到Heroku伺服器上運行
****
**A line notify bot that can instantly notify yourself the latest page of AirPods selling articles on the PTT-MacShop board**
****
**Click this picture to turn to the youtube vedio👇**

[![IMAGE ALT TEXT](https://github.com/Emily-Weng/PTT-MacShop-Notifier/blob/main/line-notify.jpg)](https://www.youtube.com/watch?v=yw8b3av3hro "PTT-MacShop-Notifier成果展示")]
****
參考教學網址:
=============
