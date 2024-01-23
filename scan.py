import requests,os
from datetime import datetime


webhook = os.getenv('WEBHOOK')

print(webhook)
date = datetime.now()
date = int(round(date.timestamp()))


try: 
    r = requests.get('https://svmnetwork.serveo.net/')
    if r.status_code == 200:
        json = {
            "content": f"<@&1194736295533084723> <t:{date}>",
            "embeds": [
                {
                "title": "<:check:1194738889500397679> Spicevm is up!",
                "description": "Spicevm website responded with **``200``** as status code!",
                "color": 65309
                }
            ],
            "attachments": []
        }
        rq = requests.post(webhook,headers={"content-type":"application/json"},json=json)
        with open('stats.json','w') as f:
            f.write('{"online":true,"responded":true,"broken":false,"statusCode":'+str(r.status_code)+',"lastChecked":'+str(date)+"}")

    else:
        if r.status_code != 502:
            json = {
                "content": f"<t:{date}>",
                "embeds": [
                    {
                    "title": "<:cross_:1194738825184935986> Spicevm is broken!",
                    "description": f"Spicevm website responded with **``{r.status_code}``** as status code!",
                    "color": 16711680
                    }
                ],
                "attachments": []
            }
            rq = requests.post(webhook,headers={"content-type":"application/json"},json=json)
            with open('stats.json','w') as f:
                f.write('{"online":true,"responded":true,"broken":true,"statusCode":'+str(r.status_code)+',"lastChecked":'+str(date)+"}")
        else:
            json = {
                "content": f"<t:{date}>",
                "embeds": [
                    {
                    "title": "<:cross_:1194738825184935986> Spicevm is down!",
                    "description": "Spicevm website didn't respond!",
                    "color": 16711680
                    }
                ],
                "attachments": []
            }
            rq = requests.post(webhook,headers={"content-type":"application/json"},json=json)
            with open('stats.json','w') as f:
                f.write('{"online":false,"responded":false,"lastChecked":'+str(date)+"}")
except:
    json = {
            "content": f"<t:{date}>",
        "embeds": [
            {
            "title": "<:cross_:1194738825184935986> Spicevm is down!",
            "description": "Spicevm website didn't respond!",
            "color": 16711680
            }
        ],
        "attachments": []
    }
    rq = requests.post(webhook,headers={"content-type":"application/json"},json=json)
    with open('stats.json','w') as f:
        f.write('{"online":false,"responded":false,"lastChecked":'+str(date)+"}")
