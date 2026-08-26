import os          # 操作系统相关
import sys         # Python 解释器相关
import json        # JSON 序列化/反序列化
import time        # 时间相关
import re          # 正则表达式
import argparse    # 命令行参数解析
import logging     # 日志
import os

# 文件路径
os.path.join("dir", "file.txt")
os.path.exists(path)
os.makedirs(path, exist_ok=True)
os.listdir(path)
os.remove(path)

# 环境变量
os.getenv("HOME")

import sys

sys.argv           # 命令行参数列表
sys.path           # 模块搜索路径
sys.exit()         # 退出程序

import json

# Python 对象转 JSON 字符串
data = {"name": "Tom", "age": 20}
json_str = json.dumps(data)
print(json_str)   # '{"name": "Tom", "age": 20}'

# JSON 字符串转 Python 对象
obj = json.loads(json_str)
print(obj["name"])  # Tom

import time

time.time()        # 当前时间戳
time.sleep(1)      # 暂停 1 秒

import re

pattern = r"\d+"   # 匹配数字
result = re.findall(pattern, "a1b2c3")
print(result)      # ['1', '2', '3']

import argparse

parser = argparse.ArgumentParser(description="示例")
parser.add_argument("--input", type=str, required=True)
parser.add_argument("--size", type=int, default=640)
args = parser.parse_args()
print(args.input, args.size)

import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("这是一条日志")