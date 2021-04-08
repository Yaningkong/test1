import os
import random
import json
import requests
ip = "http://172.16.17.31:4101"
headers = {"content-type": "application/json"}
#path = "/software/goproject/src/github.com/vearch/vearch/plugin/images/image_retrieval/test"
#windows中图片集地址
#path = "L:/ImageSet/Corel5k/1000"
path = "/itcast/Corel5k/10000"
#遍历目录文件
for file in os.listdir(path):
  #获取文件名
  idx = os.path.splitext(file)[0]

  file_path = os.path.join(path, file)
  resp = requests.post(ip+"/test/test1/"+idx, headers=headers, data=json.dumps({ "url": file_path, "feature1":{"feature": file_path}}))
  print("idx:",resp.text)
  assert resp.status_code == 200, "insert data failed, " + resp.text
