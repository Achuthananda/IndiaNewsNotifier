from configparser import ConfigParser
import os
import requests,json
import telebot

devKeys = os.environ.get('DevKeys')
config = ConfigParser()
config.read(devKeys)

telegramToken=config['telegram']['accessToken']
tb = telebot.TeleBot(telegramToken)


ChatIds= {
    "GiddyUp":"-1001428866192"
}

def getIndiaNews():
    params = {
      "country":"in",
      "apiKey": config['newsAPI']['accessToken']
    }
    response = requests.get('https://newsapi.org/v2/top-headlines', params=params)
    indianews = response.json()
    article = indianews["articles"]
    results = []
    newsmessage = ''

    count = 0
    for ar in article:
        count = count + 1
        if count == 6:
            break
        results.append(ar["title"])
        newsmessage = newsmessage + '\n\n' +str(count) +':'+ ar["title"]
    return newsmessage
 

def notifyIndiaNews():
    newsmessage = getIndiaNews()
    tb.send_message(ChatIds['GiddyUp'], newsmessage)

if __name__ == '__main__':
    notifyIndiaNews()
    
    


