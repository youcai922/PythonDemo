import requests

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    print(page_text)
