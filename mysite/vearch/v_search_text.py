#搜索
# 从插入的文档中随机选一张进行搜索
import os
import random
import json
import requests
ip = "http://172.16.17.31:4102"
headers = {"content-type": "application/json"}
path = "/itcast/text_set/C7-History"
file = random.choice(os.listdir(path))
print(file)
file_path = os.path.join(path, file)
resp = requests.post(ip+"/test/test2/_search", headers=headers, data=json.dumps({ "query": { "sum": [{"feature": file_path, "field": "feature1"}]},"is_brute_search":1}))
assert resp.status_code == 200, "search data failed, " + resp.text
print(resp.json()) #这里就会返回与传入的图片相似的图片地址及得分