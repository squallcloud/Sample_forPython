import yaml
import chardet #エンコード判別のため
# import os
from os import path

def CheckEncoding(input_file_path):
  retval = None
  with open(input_file_path, "rb") as f:
    retval = chardet.detect(f.read())
  return retval


file_path = './Sample_forPython/EasySample/test.yaml'
encode_info = CheckEncoding(file_path)



if path.exists(file_path) == True:
  print("{}は存在します".format(file_path))
  enc = encode_info['encoding']
  # enc = enc.replace("-","_").lower()
  with open(file_path, encoding=enc) as stream:
    data = yaml.load(stream)
    print(data)