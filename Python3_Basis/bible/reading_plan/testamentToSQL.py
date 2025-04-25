import json
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
# @Time    : 2025/02/25 11:41
# @题目     :
# @参考     :  
# 时间复杂度 :

# 生成 SQL 插入语句的 Python 脚本

def generate_sql(start, end):
    sql_statements = []

    for i in range(start, end + 1):
        str11 = ["testament_intro_" + str(i), "", "testament_final_" + str(i)]
        sql_statements.append(str11)
    # '["testament_intro_{i}", "", "testament_final_{i}"]');

    return sql_statements

# 生成 SQL 语句，从 61 到 260
sql_statements = generate_sql(61, 260)

# 打印所有生成的 SQL 语句
for statement in sql_statements:
    with open('testament_to_SQL22.sql', 'a') as f:
        f.write(json.dumps(statement) + "\n")
