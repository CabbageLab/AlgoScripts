import uuid
from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys
from uuid import UUID

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
# @Time    : 2025/01/13 16:19
# @题目     :
# @参考     :  
# 时间复杂度 :

import hashlib

class ConsistentHashing:
    def __init__(self, nodes, replica_count=100):
        """
        初始化一致性哈希环
        :param nodes: 分片节点列表
        :param replica_count: 每个节点的虚拟节点数量
        """
        self.replica_count = replica_count
        self.ring = {}
        self.sorted_keys = []

        for node in nodes:
            self.add_node(node)

    def add_node(self, node):
        """
        添加节点到哈希环
        """
        for i in range(self.replica_count):
            key = self._hash(f"{node}:{i}")
            self.ring[key] = node
            self.sorted_keys.append(key)
        self.sorted_keys.sort()

    def remove_node(self, node):
        """
        从哈希环中移除节点
        """
        for i in range(self.replica_count):
            key = self._hash(f"{node}:{i}")
            del self.ring[key]
            self.sorted_keys.remove(key)

    def get_node(self, key):
        """
        根据 key 获取对应的节点
        """
        if not self.ring:
            return None
        hash_val = self._hash(key)
        for ring_key in self.sorted_keys:
            if hash_val <= ring_key:
                return self.ring[ring_key]
        return self.ring[self.sorted_keys[0]]

    def _hash(self, key):
        """
        计算 key 的哈希值
        """
        return int(hashlib.md5(key.encode()).hexdigest(), 16)


def decimal_to_base62(num):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if num == 0:
        return chars[0]
    base62 = []
    while num > 0:
        num, remainder = divmod(num, 62)
        base62.append(chars[remainder])
    return ''.join(reversed(base62))

def base62_to_decimal(s):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    char_to_value = {char: idx for idx, char in enumerate(chars)}
    num = 0
    for char in s:
        num = num * 62 + char_to_value[char]
    return num


# 十进制转 62 进制
decimal_num = 2341234234
base62_num = decimal_to_base62(decimal_num)
print(f"十进制 {decimal_num} 转 62 进制: {base62_num}")

base62_num="KtzINRt"
# 62 进制转十进制
converted_decimal_num = base62_to_decimal(base62_num)
print(f"62 进制 {base62_num} 转十进制: {converted_decimal_num}")

# 初始化分片节点
nodes = ["shard1", "shard2", "shard3", "shard4"]
consistent_hashing = ConsistentHashing(nodes)

def get_shard_for_short_url(short_url):
    """
    根据短域名获取分片节点
    """
    # 将 62 进制短域名转换为十进制
    decimal_value = base62_to_decimal(short_url)
    # 使用一致性哈希获取分片节点
    shard = consistent_hashing.get_node(str(decimal_value))
    return shard

# 示例：写入和读取
short_url = "8M0kX"  # 62 进制短域名
shard = get_shard_for_short_url(short_url)
print(f"短域名 {short_url} 对应的分片节点: {shard}")



print(uuid.uuid4())