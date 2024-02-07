import requests

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    post_url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw': 'dog'
    }
    ''
    response = requests.post(url=post_url, data=data, headers=headers)
    page_text = response.json()
    print(page_text)
