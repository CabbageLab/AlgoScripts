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
# @Time    : 2025/04/18 17:48
# @题目     :
# @参考     :  
# 时间复杂度 :

#!/usr/bin/env python3
"""
usage:
    python count_by_type.py data.json  > result.tsv

说明：
    1. 传入的 JSON 文件格式应与示例文件一致，顶层包含 "header" 与 "data" 两个字段。
    2. 脚本会忽略同一 (userId, type, finishDate) 的重复记录，只累计一次。
"""

import json
from collections import defaultdict

def main():
    with open("./export_result.json", "r", encoding="utf-8") as fp:
        raw = json.load(fp)
    records = raw.get("data", [])

    # 记录已经出现过的 (userId, type, finishDate) 组合
    seen = set()
    # 结果：counts[userId][type] = distinct_date_count
    counts = defaultdict(lambda: defaultdict(int))

    for r in records:
        try:
            uid   = r["userId"]
            tp    = r["type"]
            fdate = r["finishDate"]          # 2025-3-5  等格式
        except KeyError:
            # 字段缺失就跳过
            continue

        key = (uid, tp, fdate)
        if key not in seen:                 # 当天同 type 只记一次
            seen.add(key)
            counts[uid][tp] += 1

    # 输出：userId <TAB> type <TAB> count
    for uid in sorted(counts):
        for tp in sorted(counts[uid]):
            print(f"{uid}\t{tp}\t{counts[uid][tp]}")

if __name__ == "__main__":
    main()
