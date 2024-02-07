import requests
import json

if __name__ == "__main__":
    # itemId是演出id，dataId是场次id
    url = 'https://detail.damai.cn/subpage?itemId=763755105403&apiVersion=2.0&dmChannel=pc@damai_pc&bizCode=ali.china.damai&scenario=itemsku&dataType=&dataId=&privilegeActId=&callback=__jp0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Encoding': '',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,et;q=0.7',
        'Referer': 'https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.78d44d152qhOlt&id=763755105403',
        'Cookie': 'cna=N7SFHPAQqG0CARsQpUlvx/3o; _samesite_flag_=true; cookie2=1468f388b79ce203b51d5924e6199c8c; t=1109b0a0d1aca63eaf3ca6f2044ac3af; _tb_token_=e33e0355536ed; _hvn_login=18; damai.cn_nickName=%E6%B0%B8%E6%81%92an; user_id=138760828; xlly_s=1; munb=2202473123549; mtop_partitioned_detect=1; _m_h5_tk=6cee37bc662571c7f3e3471ffb099a28_1707210778692; _m_h5_tk_enc=3c04ab099f0f9b2fa453016e01007e3e; csg=ea3bf9b6; damai.cn_user=2VD3jNMLOQkgNWiYF+Etu2B0BOMXNjSgTRNX46xivtHFoQtONZQz0TIReXX5l4dhGxb2+Rjuqig=; damai.cn_user_new=2VD3jNMLOQkgNWiYF%2BEtu2B0BOMXNjSgTRNX46xivtHFoQtONZQz0TIReXX5l4dhGxb2%2BRjuqig%3D; h5token=384e10e3fca34423b26cfa50284de04e_1_1; damai_cn_user=2VD3jNMLOQkgNWiYF%2BEtu2B0BOMXNjSgTRNX46xivtHFoQtONZQz0TIReXX5l4dhGxb2%2BRjuqig%3D; loginkey=384e10e3fca34423b26cfa50284de04e_1_1; destCity=%u6B66%u6C49; isg=BMzMn5Cqxd7DN9FMv9FVwVFunSr-BXCvrT95tiaN2HcasWy7ThVAP8JCUbmJ-agH; tfstk=echwU41n_CdZZW_SQJV4Ld1AxbVTa7KW0jZboq005lqMDFU0gci3nj9t5SR4YmebjAZfgjrEjswsgqC4oqmvWoT9dV3TMSxWVSRSWVFVTti2NTuy28VDV3OCdw29fSD6-p3lYVqJ-LR7h308xXz0UItlxTrCiscHMRrrSt1ciXzaQj0gYPzZTPyaqgyFDy0HbjHNmtygJyrW8ezm7g7_njZbhtBYK7UUVFa1Hteg7s6Za_WAHJqL8uT_5'
    }
    daMai_text = requests.get(url=url, headers=headers).text
    clean_json_string = daMai_text[6:-1]
    json_object = json.loads(clean_json_string)
    itemBasicInfo = json_object["itemBasicInfo"]
    print("演出id", itemBasicInfo["itemId"], "演出名称：", itemBasicInfo["projectTitle"], "城市",
          itemBasicInfo["cityName"], "\n")

    # 场次信息
    perform_view_list = json_object["performCalendar"]["performViews"]
    for perform_view in perform_view_list:
        print("场次id", perform_view["performId"], "场次名称", perform_view["performName"])
    print("\n")
    # 票挡信息
    perform_sku_list = json_object["perform"]["skuList"]
    for sku in perform_sku_list:
        print("票档id", sku["skuId"], "票档名称", sku["priceName"], "价格：", sku["price"], "购买状态：",
              "可以购买" if "true" == sku["skuSalable"] else "不可购买")

#下订单页面https://mtop.damai.cn/h5/mtop.damai.trade.order.build.h5/1.0/?jsv=2.7.2&appKey=12574478&t=1707210738787&sign=c091ec91010998520b2e0bb682a7cb89&type=originaljson&dataType=json&v=1.0&H5Request=true&AntiCreep=true&AntiFlood=true&api=mtop.damai.trade.order.build.h5&method=POST&ttid=%23t%23ip%23%23_h5_2014&globalCode=ali.china.damai&tb_eagleeyex_scm_project=20190509-aone2-join-test&requestStart=1707210738785
