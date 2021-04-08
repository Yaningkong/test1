import os
import random
import json
import requests
import re
import jieba
ip = "http://172.16.17.31:4102"
headers = {"content-type": "application/json"}
#path = "/software/goproject/src/github.com/vearch/vearch/plugin/images/image_retrieval/test"
#windows文本集地址
path = "L:/ImageSet/复旦大学中文文本分类数据集/text_set/C41-test_onetext/"
#Linux文本集地址
#path = "/itcast/text_set/C41-test_onetext/"


def cut_sentences(content):
  # 结束符号，包含中文和英文的
  end_flag = ['?', '!', '.', '？', '！', '。', '…']

  content_len = len(content)
  sentences = []
  tmp_char = ''
  for idx, char in enumerate(content):
    # 拼接字符
    tmp_char += char

    # 判断是否已经到了最后一位
    if (idx + 1) == content_len:
      sentences.append(tmp_char)
      break

    # 判断此字符是否为结束符号
    if char in end_flag:
      # 再判断下一个字符是否为结束符号，如果不是结束符号，则切分句子
      next_idx = idx + 1
      if not content[next_idx] in end_flag:
        sentences.append(tmp_char)
        tmp_char = ''

  return sentences


#遍历目录文件
for file in os.listdir(path):
  #获取文件名
  #idx = os.path.splitext(file)[0]
  #fd = os.open(file,os.O_RDWR)
  #print(fd)
  fd = open(os.path.join(path, file),encoding='gb18030',errors='ignore')
  content = fd.read()
  string1 = str(content).replace(" ", "")
  string2 = string1.replace("\n","")
  string = string2.replace("\t", "")
  #print(string)
 # print(fd.name)

  id = 0
  texts = cut_sentences(list(string))
  #print(texts)
  for text in texts:  #str类型

    file_path = os.path.join(path, file)
    #data = dict(text=ret,feature1=ret)
    #id = str(idx) //不加id 因为数据被切分了

    #resp = requests.post(ip+"/test/test2/"+id, headers=headers, data=json.dumps(data))
    # resp = requests.post(ip + "/test/test2/" + id, headers=headers,
    #                      data=json.dumps({"text":text , "feature1": {"feature":text}}))
    # print("id:",resp.text)
    # id += 1
    # assert resp.status_code == 200, "insert data failed, " + resp.text

    #分词 精确模式
    seg_text = jieba.cut(text)
    print('/'.join(seg_text))
  fd.close()



