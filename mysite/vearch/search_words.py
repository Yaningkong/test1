#搜索
# 选定一个句子查重
import os
import random
import json
import requests
ip = "http://172.16.17.31:4102"
headers = {"content-type": "application/json"}
#path = "/itcast/text_set/C41-test_onetext/"
#windows文本集地址
path = "L:/ImageSet/复旦大学中文文本分类数据集/text_set/C41-test_onetext/"
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

for file in os.listdir(path):
  fd = open(os.path.join(path, file),encoding='gb18030',errors='ignore')
  content = fd.read()
  string1 = str(content).replace(" ", "")
  string2 = string1.replace("\n","")
  string = string2.replace("\t", "")
  texts = cut_sentences(list(string))

#目标句子
text = random.choice(texts)
print(text)
resp = requests.post(ip+"/test/test2/_search", headers=headers, data=json.dumps({ "query": { "sum": [{"feature":text, "field": "feature1"}]},"is_brute_search":1}))
assert resp.status_code == 200, "search data failed, " + resp.text
print(resp.json()) #这里就会返回与传入的图片相似的图片地址及得分