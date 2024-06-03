# https://qiita.com/76r6qo698/items/751966168d2e0e8daa31

from lxml import html
import requests
from bs4 import BeautifulSoup

def main():
    response = requests.get("https://beterugift.jp/")
    soup = BeautifulSoup(response.content, "html.parser")
    # 一度'lxml.html.HtmlElement'に変換する
    lxml_data = html.fromstring(str(soup))
    # XPathが指定できる
    u_ranks  = lxml_data.xpath("//div[contains(@class, 'u_rankBox')]/span[contains(@class, 'evaluateNumber')]")
    
    for u_rank in u_ranks:
        print(u_rank.text)

if __name__ == '__main__':
    main()