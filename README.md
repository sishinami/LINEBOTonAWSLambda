# LINE BOT on AWSLambda

2017/02/07 時点での動作確認済み。

<https://devdocs.line.me/ja/#reply-message>

を平文で実装したものです。


# 使い方
```
mkdir linebot
cd !*
wget https://raw.githubusercontent.com/sishinami/LINEBOTonAWSLambda/master/lambda_function.py
pip install request -t .
zip -r linebot *
```

Lambda function に 上記で作ったzip をUPします。

AWS の画面上から
Environment variables に 
ACCESS_TOKEN 
を設定してください。

中身は
<https://developers.line.me/>
で取得できる Channel Access Token をいれます。

<http://sysop.hatenablog.com/entry/2017/02/05/224817>

でも一応解説してます

# なんか動かない時

* LINE Developer画面で WebHookを Verify しても 502 Bad Gateway が帰ってくる

きにせず実機で動作確認してみると動いてます。。。  
多分 ChannelSercretの設定がないせい


* URLに :443 とか必要なの？

2017/02/03時点では不要でした。

* メッセージは帰ってくるけど、なんか 入れた覚えの無いメッセージが勝手にでる

あれだろ？ 

「メッセージありがとうございます 申し訳ございませんが、このアカウントでは個別のご返信ができないのです 次の配信をお楽しみに」

とかいうやつ。

てっきり Verify通してないからかと思ったら、全然違って。  
Manager アカウントの方にデフォルトで入ってるんだよこのメッセージ。  

LINE Manger > メッセージ ＞ 自動応答メッセージ

に入ってるので、削除しましょう。


