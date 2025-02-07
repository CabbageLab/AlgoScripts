import os
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
# @Time    : 2025/01/10 14:26
# @题目     :
# @参考     :  
# 时间复杂度 :

import requests

var_name = "FishKey"  # 替换为你需要查询的环境变量名称
value = os.getenv(var_name)
start = time.time()
response = requests.post(
    "https://api.fish.audio/model",
    files=[
        ("voices", open("mp3/E63A56C4-349C-4B08-A3F3-D9F043846E3C.m4a", "rb")),
    ],
    data=[
        ("visibility", "private"),
        ("type", "tts"),
        ("title", "spongeBob"),
        ("train_mode", "fast"),
        # Enhance audio quality will remove background noise
        ("enhance_audio_quality", "true"),
        # Texts are optional, but if you provide them, they must match the number of audio samples
        # ("texts", "text1"),
    ],
    headers={
        "Authorization": value,
    },
)

print(response.json())
end = time.time()
print(int(end - start))
# {'_id': '536b85cafa3542c6860bb8a189d20308', 'type': 'tts', 'title': 'christmas', 'description': '', 'cover_image': 'coverimage/536b85cafa3542c6860bb8a189d20308', 'train_mode': 'fast', 'state': 'trained', 'tags': [], 'samples': [], 'created_at': '2025-01-10T06:27:24.411065Z', 'updated_at': '2025-01-10T06:27:24.410616Z', 'languages': ['en'], 'visibility': 'private', 'lock_visibility': False, 'like_count': 0, 'mark_count': 0, 'shared_count': 0, 'task_count': 0, 'unliked': False, 'liked': False, 'marked': False, 'author': {'_id': 'd314c23ee1f243559bf06a81dc647eeb', 'nickname': '尹鹏（hakusai）', 'avatar': 'avatars/d314c23ee1f243559bf06a81dc647eeb.jpg'}}
