import time
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
# @Time    : 2025/01/13 13:41
# @题目     :
# @参考     :  
# 时间复杂度 :

import requests
import base64

url = "https://api.siliconflow.cn/v1/uploads/audio/voice"
start = time.time()

# 将音频文件转换为 base64 编码
with open("../mp3/haimian.MP3", "rb") as audio_file:
    audio_base64 = base64.b64encode(audio_file.read()).decode("utf-8")

ref_text = """I'm late if I'm gonna be early Oh Do don't worry, Garbe, I'll be back before you can say why did he cruelly abandon me like that and isn't it a lovely morning Okay swimmer?Youve worked with her for years, She's the a burner grill in the kitchen Anyway, to fire her up, you've got to spark her flint manually and then jgle a yes Yes just a little and then read her favorite story, the little gridddle who could.Chapter 2, but we are fresh from the freezer, said the patties. and we're cococo cold. Don't worry, I'll get you nice and warm, said the little grid what you say squidwardt, Sidwardt. Okay, squidward doesn't matter. I'll always be here anyway.
"""

# 构造请求体
data = {
    "model": "fishaudio/fish-speech-1.5",
    "customName": "SpongeBob_2",
    "audio": f"data:audio/mpeg;base64,{audio_base64}",  # base64 编码的音频数据
    "text": ref_text,  # 参考文本
}

headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

# 发起 POST 请求
response = requests.post(url, json=data, headers=headers)

# 打印响应状态码和返回内容
print(response.status_code)
print(response.text)
end = time.time()
print(int(end - start))
# {"uri":"speech:christmas_intro_3:gajnvg92ff:fejyntscplwugpawgzwa"}
# {"uri":"speech:childenVoice:9qb2ao1x88:xkqzcxrhssfdfexkesge"}
# {"uri":"speech:christmas_intro_3:9qb2ao1x88:ngytucioztyroqfrreud"}
# {"uri":"speech:christmas_intro_3:9qb2ao1x88:biptavkfcdwqwebxuaxw"}
# uncle {"uri":"speech:uncle:9qb2ao1x88:gcfarhnkujaohsxicsud"}
# {"uri":"speech:SpongeBob_2:9qb2ao1x88:lggvggptwzfyjbgysvvj"}
# {"uri":"speech:SpongeBob_2:9qb2ao1x88:ilohfrohfjxebdyvscjs"}