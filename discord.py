#https://qiita.com/iroiro_bot/items/48e8a8a9754aacaf7ec9
import requests, json
from datetime import datetime

from file_io import get_webhook

def sent_discord(s):
  # 現在の時刻を取得
  current_time = datetime.now()

  # 指定された形式で時刻を表示
  formatted_time = current_time.strftime("%Y-%m-%dT%H:%M:%S%z")
  try:
    webhook_url  = get_webhook()
  except Exception as e:
    print(str(e))
  payload2 = {
    "payload_json" : {
        "username"      :"ギフト監視bot",
        "avatar_url"    : "https://beterugift.jp/assets/img/logo.png",
        "embeds": [
            {
                "title"         : "ギフト監視bot",
                "description"   : s,
                "timestamp"     : formatted_time,
                "color"         : 11027200,
            }
        ]
    }
  }
  payload2['payload_json'] = json.dumps( payload2['payload_json'], ensure_ascii=False )
  res = requests.post(webhook_url, data = payload2 )

def sent_discord_embed(name, value, id):
  url = "https://beterugift.jp/assets/img/icon/" + str(id) +".jpg"
  # 現在の時刻を取得
  current_time = datetime.now()

  # 指定された形式で時刻を表示
  formatted_time = current_time.strftime("%Y-%m-%dT%H:%M:%S%z")
  try:
    webhook_url  = get_webhook()
  except Exception as e:
    print(str(e))
  #print(url)
  payload2 = {
    "payload_json" : {
        "username"      :"ギフト監視bot",
        "avatar_url"    : "https://beterugift.jp/assets/img/logo.png",
        "embeds": [
            {
                "title"         : "ギフト監視bot",
                "timestamp"     : formatted_time,
                "color"         : 7419530,
                "image"         : {
                      "url" : url         
                },
                "footer": {
                    "text" : "ベテルギフト",
                },
                "fields": [
                    {
                        "name"  : name,
                        "value" : value,
                        "inline": True,
                    }
                ]
            }
        ]
      }
    }

  ### embed付き
  payload2['payload_json'] = json.dumps( payload2['payload_json'], ensure_ascii=False )
  res = requests.post(webhook_url, data = payload2 )

