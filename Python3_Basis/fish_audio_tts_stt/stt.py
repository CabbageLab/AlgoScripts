import os
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
# @Time    : 2025/01/15 11:15
# @题目     :
# @参考     :  
# 时间复杂度 :

import httpx
import ormsgpack

# Read the audio file
with open("mp3/haimian.MP3", "rb") as audio_file:
    audio_data = audio_file.read()

# Prepare the request data
request_data = {
    "audio": audio_data,
    "language": "en",  # Optional: specify the language
    "ignore_timestamps": False  # Optional: set to True to ignore precise timestamps
}
var_name = "FishKey"  # 替换为你需要查询的环境变量名称
value = os.getenv(var_name)
# Send the request
with httpx.Client() as client:
    response = client.post(
        "https://api.fish.audio/v1/asr",
        headers={
            "Authorization": value,
            "Content-Type": "application/msgpack",
        },
        content=ormsgpack.packb(request_data),
    )

# Parse the response
result = response.json()

print(f"Transcribed text: {result['text']}")
print(f"Audio duration: {result['duration']} seconds")

result_rr = ""
for segment in result['segments']:
    print(f"Segment: {segment['text']}")
    result_rr += segment['text']
    print(f"Start time: {segment['start']}, End time: {segment['end']}")

print(result_rr)
