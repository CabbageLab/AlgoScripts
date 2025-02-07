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
# @Time    : 2025/01/13 17:11
# @题目     :
# @参考     :  
# 时间复杂度 :

import mmh3  # MurmurHash 库
from pybloom_live import BloomFilter  # 布隆过滤器库

def decimal_to_base62(num):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if num == 0:
        return chars[0]
    base62 = []
    while num > 0:
        num, remainder = divmod(num, 62)
        base62.append(chars[remainder])
    return ''.join(reversed(base62))

# 初始化布隆过滤器 布隆过滤器容量设置为 1000000 和误差率 0.001
bloom_filter = BloomFilter(capacity=1000000, error_rate=0.001)
# 保存已生成的短链映射
generated_short_urls = {}

def generate_short_url(long_url):
    # 如果该长链已经生成过短链，直接返回
    if long_url in generated_short_urls:
        return generated_short_urls[long_url]
    """
    根据长链接生成短链
    """
    while True:
        # 使用 MurmurHash 生成哈希值
        hash_val = mmh3.hash(long_url)
        print(f"hash 值: {hash_val}")
        # 将哈希值转换为 62 进制
        short_url = decimal_to_base62(hash_val)[:7]  # 取前 7 位
        # 检查是否冲突
        if short_url not in bloom_filter:
            bloom_filter.add(short_url)
            generated_short_urls[long_url] = short_url  # 记录长链与短链的映射
            return short_url
        # 如果冲突，重新生成
        long_url += "salt11"  # 加盐避免冲突

# 测试
long_url = "https://www.example.com/very/long/url"
short_url = generate_short_url(long_url)
print(f"长链接: {long_url} -> 短链: {short_url}")
short_url = generate_short_url(long_url)
print(f"长链接: {long_url} -> 短链: {short_url}")
long_url2 = "https://www.example.com/very/long/url2"
short_url2 = generate_short_url(long_url2)
print(f"长链接: {long_url2} -> 短链: {short_url2}")
