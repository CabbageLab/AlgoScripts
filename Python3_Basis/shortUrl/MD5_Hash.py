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
# @Time    : 2025/01/21 11:45
# @题目     :
# @参考     :  
# 时间复杂度 :

import hashlib

def generate_md5_hash(input_string):
    # 创建md5对象
    md5 = hashlib.md5()
    # 更新md5对象，输入为字节类型数据
    md5.update(input_string.encode('utf-8'))
    # 获取最终的md5 hash
    # 将MD5的十六进制字符串转为整数
    md5_int = int(md5.hexdigest(), 16)
    print(md5_int)
    return md5.hexdigest()

# 示例使用
long_url = "https://www.example.com/very/long/url"
md5_hash = generate_md5_hash(long_url)
print(f"MD5 Hash: {md5_hash}")
