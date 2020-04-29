### Flask AI Webservice
執行python3 app.py來啟動伺服器<br/>
Webservice包含三個功能：<br/>
<ul>
  <li>/plus:簡單的加法<br>
    Sample:/plus/a/b 結果：a+b
  </li>
  <li>/predictJson:按照已建立好的model進行回歸分析並做出預測.<br>
    POST JSON Sample:{"rate":5,"sale1":200,"sale2":1000}
  </li>
  <li>/detectImage:使用Yolo3對照片裡面的物件進行物件辨識<br>
    Method:POST a file to <yoururl>/detectImage</li>
</ul>
