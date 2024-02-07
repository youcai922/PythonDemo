import requests

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    total_url = 'https://www.uniqlo.cn/public/bin/data/json/L4JsonData.json'
    response = requests.get(url=total_url, headers=headers)
    product_map = response.json()['CustomerHeart'][0]
    product_info_url_template = 'https://www.uniqlo.cn/data/products/spu/zh_CN/{product_id}.json'
    detail_url_template = 'https://d.uniqlo.cn/p/product/i/product/spu/pc/query/{product_id}/zh_CN'

    file = open("youyiku_info.txt", "w", encoding="utf-8")

    for key, value in product_map.items():
        product_info_url = product_info_url_template.format(product_id=value)
        response = requests.get(url=product_info_url, headers=headers).json()
        product_info_rows = response["rows"]
        product_info_summary = response["summary"]
        product_info_summary_fullName = product_info_summary["fullName"]
        file.write("货号:%s\t对应的产品编号:%s\t商品名称：%s\n" % (key, value, product_info_summary_fullName))

        detail_url = detail_url_template.format(product_id=value)
        product_detail_info = requests.get(url=detail_url, headers=headers).json()
        try:
            product_detail_info_rows = product_detail_info["resp"][0]["rows"]
        except:
            product_detail_info_rows = []
        for sizeinfo in product_info_rows:
            result = list(filter(lambda row: row['productId'] == sizeinfo["productId"], product_detail_info_rows))
            if not result:
                file.write("\t子产品编号：%s\t款式：%s\t大小：%s\n" % (
                    sizeinfo["productId"], sizeinfo["style"], sizeinfo["sizeText"]))
            else:
                file.write("\t子产品编号：%s\t款式：%s\t大小：%s\t价格：%s\n" % (
                    sizeinfo["productId"], sizeinfo["style"], sizeinfo["sizeText"], result[0]["price"]))
    file.close()
    print("同步消息结束")
