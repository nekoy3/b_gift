from bs4 import BeautifulSoup
import requests

def get_data(data_num):
  url = "https://beterugift.jp/home/load/" + str(data_num)
 
  response = requests.get(url)
  response.encoding = response.apparent_encoding
  contents = response.content
  t_list = []

  bs = BeautifulSoup(contents, "html.parser")
  for tr in bs.select("tr")[1:]:
    #空白の削除
    text = tr.getText().replace(' ', '')
    #余分な改行コードの削除
    text = '\n'.join(filter(lambda x: x.strip(), text.split('\n')))
    #行ごとにリスト化
    t_l = text.split("\n")
    #\rを削除
    t_l = [s.rstrip() for s in t_l]
    #直近取引履歴のテーブルは読まない
    if t_l[0] == '直近取引履歴':
        break
    #商品がないと直近取引履歴が読み込まれるので、読み込まれたら空
    if t_l[0] == 'ギフト券種別':
         break
    #不要な要素の削除
    t_l = [s for s in t_l if s != '|' and s != '買\xa0\xa0う']

    # import random
    # value = random.uniform(70, 90)
    # t_l[3] = f"{value:.1f}%"

    t_l = t_l[:int(len(t_l)/2)]
    t_list.append(t_l)
  return t_list