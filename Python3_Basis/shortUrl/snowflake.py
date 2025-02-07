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
# @Time    : 2025/01/21 23:12
# @题目     :
# @参考     :  
# 时间复杂度 :

import time
import random

# SimpleSnowflake 类（用于生成唯一ID）
class SimpleSnowflake:
    def __init__(self, datacenter_id=1, worker_id=1):
        """
        初始化 SimpleSnowflake 配置
        :param datacenter_id: 数据中心ID
        :param worker_id: 工作机器ID
        """
        self.datacenter_id = datacenter_id
        self.worker_id = worker_id
        self.sequence = 0
        self.last_timestamp = -1
        self.sequence_mask = 0xFFF  # 序列号掩码
        self.worker_id_shift = 12  # 工作ID的位移量
        self.datacenter_id_shift = 17  # 数据中心ID的位移量
        self.timestamp_shift = 22  # 时间戳的位移量
        self.epoch = int(time.mktime(time.strptime("2020-01-01", "%Y-%m-%d")))  # 定义纪元时间为 2020-01-01

    def _current_timestamp(self):
        """
        获取当前时间戳（以毫秒为单位）
        :return: 当前时间戳
        """
        return int(time.time() * 1000) - self.epoch

    def _next_timestamp(self, last_timestamp):
        """
        获取下一个有效的时间戳，避免雪花算法中时间倒退
        :param last_timestamp: 上一次生成的时间戳
        :return: 下一个有效的时间戳
        """
        timestamp = self._current_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self._current_timestamp()
        return timestamp

    def next_id(self):
        """
        生成下一个唯一ID
        :return: 生成的唯一ID
        """
        timestamp = self._current_timestamp()

        if timestamp == self.last_timestamp:
            # 如果当前时间戳和上一次时间戳相同，则序列号递增
            self.sequence = (self.sequence + 1) & self.sequence_mask
            if self.sequence == 0:
                timestamp = self._next_timestamp(self.last_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        # 生成雪花ID
        return (timestamp << self.timestamp_shift) | (self.datacenter_id << self.datacenter_id_shift) | (
                    self.worker_id << self.worker_id_shift) | self.sequence

snowflake = SimpleSnowflake()
print(snowflake.next_id())
