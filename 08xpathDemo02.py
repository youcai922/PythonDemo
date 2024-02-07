import requests
from lxml import etree

if __name__ == "__main__":
    url = 'https://www.txt80.cc/hot/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    hot_list = tree.xpath('//div[@class="list_l_box"]/div[@class="slist"]')
    for item in hot_list:
        title = item.xpath('./div[@class="info"]/h4/a/text()')[0]
        print(title)
