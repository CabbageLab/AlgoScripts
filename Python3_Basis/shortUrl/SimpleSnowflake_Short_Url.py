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
# @Time    : 2025/01/21 23:23
# @题目     :
# @参考     :  
# 时间复杂度 :

from snowflake import SimpleSnowflake

# Base62 编码表
BASE62_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Base62 编码函数
def base62_encode(num):
    """
    将数字转换为 Base62 编码
    :param num: 需要转换的数字
    :return: Base62 编码后的字符串
    """
    if num == 0:
        return BASE62_ALPHABET[0]
    base62 = []
    while num:
        num, rem = divmod(num, 62)
        base62.append(BASE62_ALPHABET[rem])
    return ''.join(reversed(base62))

# 长链到短链生成器
class ShortLinkGenerator:
    def __init__(self):
        """
        初始化短链生成器
        """
        self.flake = SimpleSnowflake()
        self.link_map = {}

    def generate_short_link(self, long_url):
        """
        生成短链
        :param long_url: 长链 URL
        :return: 生成的短链
        """
        # 使用雪花算法生成唯一 ID
        unique_id = self.flake.next_id()
        # 将生成的唯一 ID 转换为 Base62 编码
        short_link = base62_encode(unique_id)
        # 保存长链与短链的映射
        self.link_map[short_link] = long_url
        return short_link

    def get_long_url(self, short_link):
        """
        根据短链获取长链
        :param short_link: 短链
        :return: 对应的长链
        """
        return self.link_map.get(short_link, "短链不存在")

# 测试
if __name__ == "__main__":
    generator = ShortLinkGenerator()
    long_url = "https://www.example.com/this-is-a-long-url"
    short_link = generator.generate_short_link(long_url)
    print(f"长链: {long_url}")
    print(f"短链: {short_link}")
    retrieved_url = generator.get_long_url(short_link)
    print(f"通过短链获取的长链: {retrieved_url}")
