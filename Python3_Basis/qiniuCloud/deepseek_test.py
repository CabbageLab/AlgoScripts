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
# @Time    : 2025/02/07 16:17
# @题目     :
# @参考     :  
# 时间复杂度 :


from openai import OpenAI

url = 'https://api.qnaigc.com/v1/'
api_key = "sk-8e3e993c729ed35527d7e822887302d7db87f295495c78145cb491695f895133"

client = OpenAI(
    base_url=url,
    api_key=api_key
)

# 发送非流式输出的请求
messages = [
    {"role": "user", "content": "七牛云提供 GPU 云产品能用于哪些场景？"}
]
response = client.chat.completions.create(
    model="deepseek-v3",
    messages=messages,
    stream=False,
    max_tokens=4096
)
content = response.choices[0].message.content
reasoning_content = response.choices[0].message.reasoning_content
print(content)
