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
# @Time    : 2025/01/09 16:49
# @题目     :
# @参考     :  
# 时间复杂度 :

import asyncio
import random
import time

async def process_item(item):
    process_time = random.uniform(0.5, 2.0)
    print(f"处理中：{item}，预计耗时 {process_time:.2f} 秒")
    try:
        # 设置1秒超时
        await asyncio.wait_for(
            asyncio.sleep(process_time),
            timeout=1.0
        )
        return f"处理完成：{item}，耗时 {process_time:.2f} 秒"
    except asyncio.TimeoutError:
        return f"处理超时：{item}"

async def main():
    items = ["任务A", "任务B", "任务C", "任务D"]
    tasks = [
        asyncio.create_task(process_item(item))
        for item in items
    ]

    start = time.time()
    results = await asyncio.gather(*tasks, return_exceptions=True)
    end = time.time()

    print("\n".join(results))
    print(f"总耗时：{end - start:.2f} 秒")

if __name__ == "__main__":
    asyncio.run(main())
