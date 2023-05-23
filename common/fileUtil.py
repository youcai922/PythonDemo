import yaml
import os

yaml_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"test.yml")

def read_yaml(n,k):
    # 打开文件
    with open(yaml_path,"r",encoding="utf-8") as f:
        data=yaml.load(f,Loader=yaml.FullLoader)
        try:
            #判断传入的n是否在存在
            if n in data.keys():
                return data[n][k]
            else:
                print(f"n：{n}不存在")
        except Exception as e :
            print(f"key值{e}不存在")
