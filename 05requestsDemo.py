import requests
import re

if __name__ == "__main__":
    url = 'https://top.baidu.com/board?tab=realtime&sa=fyb_realtime_31065'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    ex = '<div class="category-wrap_iQLoo horizontal_1eKyQ">(.*?)--> </div> </div>'
    info_list = re.findall(ex, response.text, re.S)
    for infovo in info_list:
        hot_pattern = '<div class="hot-index_1Bl1a"> (.*?) </div>'
        hot_info = re.findall(hot_pattern, infovo, re.S)
        title_pattern = '<div class="c-single-text-ellipsis"> (.*?) </div>'
        title_info = re.findall(title_pattern, infovo, re.S)
        detail_pattern = '<div class="hot-desc_1m_jR .*"> (.*?) <a href="'
        detail_info = re.findall(detail_pattern, infovo, re.S)
        print("小标题：" + title_info[0])
        print("热度" + hot_info[0])
        print("详细介绍：" + detail_info[0])
        print("-------------------------------------------------")