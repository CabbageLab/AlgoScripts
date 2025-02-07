from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys

from sortedcontainers import SortedList, SortedDict, SortedSet

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')  # 负无穷
INFMAX = float('inf')  # 正无穷
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

# @Author  : https://github.com/hakusai22
# @Time    : 2025/01/13 13:53
# @题目     :
# @参考     :  
# 时间复杂度 :

import requests
import io

url = "https://api.siliconflow.cn/v1/uploads/audio/voice"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

# 远程音频文件 URL
audio_url = "https://xxxxxx.com/wepray_business/reading_plan/en/christmas/christmas_intro_1.mp3"

# 从远程 URL 下载音频文件内容
response = requests.get(audio_url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用 io.BytesIO 将文件内容转为内存中的文件对象
    audio_file = io.BytesIO(response.content)
    files = {
        "file": ("christmas_intro_1.mp3", audio_file, "audio/mpeg")
    }

    # 表单其他字段
    data = {
        "model": "fishaudio/fish-speech-1.5",
        "customName": "christmas_intro_3222",
        "text": "在一无所知中, 梦里的一天结束了，一个新的轮回便会开始"
    }

    # 发送 POST 请求
    upload_response = requests.post(url, headers=headers, files=files, data=data)

    # 打印响应状态码和内容
    print(upload_response.status_code)
    try:
        print(upload_response.json())  # 如果响应是 JSON 格式，尝试解析并打印
    except ValueError:
        print("响应内容不是 JSON 格式")
else:
    print(f"无法下载文件, 错误代码: {response.status_code}")

# {'uri': 'speech:christmas_intro_3222:gajnvg92ff:farkkotbjvuhgjnionmw'}