import os
import random
import json
import requests
ip = "http://172.16.17.31:4102"
headers = {"content-type": "application/json"}
#path = "/software/goproject/src/github.com/vearch/vearch/plugin/images/image_retrieval/test"
#windows文本集地址
#path = "L:/ImageSet/复旦大学中文文本分类数据集/text_set/C7-History/"
#图片集

path = "/itcast/text_set/C7-History"

#遍历目录文件
for file in os.listdir(path):
  #获取文件名
  idx = os.path.splitext(file)[0]
  #fd = os.open(file,os.O_RDWR)
  # file = open(file)
  fd = open(os.path.join(path, file),encoding='gb18030',errors='ignore')
  #print(fd.read())

  ret = fd.read()
  #print(ret)
  file_path = os.path.join(path, file)
  data = dict(text=ret,feature1=ret)
  id = str(idx)
  #resp = requests.post(ip+"/test/test2/"+id, headers=headers, data=json.dumps(data))
  resp = requests.post(ip + "/test/test2/" + id, headers=headers,
                       data=json.dumps({"text": file_path, "feature1": {"feature": file_path}}))
  print("idx:",resp.text)
  assert resp.status_code == 200, "insert data failed, " + resp.text

  fd.close()



