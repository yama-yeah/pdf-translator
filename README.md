# PDFを翻訳するSlack bot

```shell
git clone https://github.com/yama-yeah/pdf-translator
cd pdf-translator/bot/src/
nano slackbot_settings.py
```
で`slackbot_settings.py`を以下のようにトークンをコピペして編集
```
SLACK_BOT_TOKEN='xoxb-xxxxxxxxxxxxxxxxxxxx'
SLACK_APP_TOKEN='xapp-xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
SLACK_SIGNING_SECRET='xxxxxxxxxxxxxxxxx'
```

`docker-compose up`で起動