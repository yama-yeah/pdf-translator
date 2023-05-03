import slackbot_settings as settings
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from time import sleep
from slack_sdk import WebClient
import requests
import trans as translator
import translator_status as tlr_status
app = App(
        token=settings.SLACK_BOT_TOKEN,
        signing_secret=settings.SLACK_SIGNING_SECRET
)
@app.message("hello")
def message_hello(message, say):
    print(message)
    user = message["user"]
    say(f"Hello <@{user}>!")

@app.message("translate")
def translate(message, say):
    print(message)
    file = message["files"][0]
    url = file["url_private_download"]
    name = file["name"]
    if name.split(".")[-1] != "pdf":
        say("Please upload a pdf file")
        return
    headers = {
        'Authorization': 'Bearer ' + settings.SLACK_BOT_TOKEN
    }
    with requests.get(url, headers=headers, stream=True) as r:
        r.raise_for_status()
        with open('temp.pdf', 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    say("I'm translating your file, please wait a moment")
    status=translator.run("./temp.pdf")
    if tlr_status.Error == type(status):
        say(status.message)
        return
    with open(status.message+"/temp.pdf", "rb") as f:
        res = app.client.files_upload_v2(
            channels=message["channel"],
            file=f,
            filename="translated"+name,
            filetype="pdf",
            initial_comment="Here is your translated file"
        )
        print(res)


    

@app.event("app_mention")
def event_test(body, say, logger):
    logger.info(body)
    say("Don't talk to me! I'm busy!")

if __name__ == "__main__":
    SocketModeHandler(app, settings.SLACK_APP_TOKEN).start()
    