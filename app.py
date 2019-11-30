##練習
# ctrl+~ 叫出TERMINAL 控制端
# 先選取一段文字 再ctrl+/ 可以把選取的文字加上#
# cls>表示清除

# 在打python 檔名.py
# 在 TERMINAL 打 python 可顯示版本

# #while 迴圈
# result=0
# n=1
# while n<=10:
#     result+=n
#     n+=1
# print(result)

# #for 迴圈
# result=0
# for n in range(1,11):
#     result+=n
# print(result)
# #for 變數 in 列表:
# result-0
# for n in [5,7,2]:
#     result+=n
# print(result)

# #函式
# def test(n1,n2):
#     return n1+n2
# result=test(3,4)
# print(result)

# #讀取檔案
# file=open("data.txt", mode="r")#mode是模式的意思 r是read
# data=file.read()#讀取檔案(file)匯入data裡面
# file.close()#檔案已經到data裡面了,要把file關起來,不然站記憶體
# print(data)


#準備資料
import json
file=open("data.txt", mode="r", encoding="utf-8")
data=json.load(file)
file.close()
#每更新一次 按ctrl+c 就可以重新跑出位置 再打python 檔名.py
# 安裝flask (在TERMINAL打) pip still flask
from flask import * # 載入 flask 模組
app=Flask("My Website") # 建立一個網站應用程式物件

#網站的網址:http://主機名稱/路徑?參數名稱=資料&參出名稱=資料&........  (主機>下面打的程式)
#例如:https://test2019-11-30.herokuapp.com//
#如果打http://127.0.0.1:5000/jdosfkolja 會跑出404 因為沒連到主機
@app.route("/") # 指定對應的網址路徑
def home(): # 對應的處理函
    return render_template("home.html") # 回應給前端的訊息
    #在原本的資料夾中 新增一個資料夾 "templates"
    #在HTML中 用"!+Tab"可以跑出上面的東西<!DOCTYPE html>

#例如:https://test2019-11-30.herokuapp.com/test.php?keyword=關鍵字
@app.route("/test.php") # 指定對應的網址路徑
def test(): # 對應的處理函式
    #取得網址列上的參數:requst.args.get(參數名稱,預設值)
    keyword=request.args.get("keyword", None)
    if keyword==None:
        return redirect("/")#如果使用者沒打後面的部分(test.php?keyword=關鍵字) 則導向路徑首頁/
    else:
        if keyword in data: # 回應給前端的訊息
            return render_template("result.html", result=data[keyword])
        else:
            return render_template("result.html", result="沒有翻譯")

if __name__=="__main__": # 如果以主程式執行，立即啟動伺服器
    app.run() # 啟動伺服器
#建立一個 "runtime.txt" 告訴它 Python的版本
#建立一個 "requirements.txt"
#建立一個 "Procfile" 用綠色獨角獸(gunucorn)打開app
#TWEMINAL 會出現一個網址 複製貼上GOOGLE裡面 就可以出現一個網站