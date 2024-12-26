import json
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
# @Time    : 2024/12/11 10:51
# @题目     :
# @参考     :  
# 时间复杂度 :

import os

def read_and_sort_subdirectories_by_number(base_dir):
    # 存储二级目录名
    second_level_dirs = []

    # 遍历目录
    for root, dirs, files in os.walk(base_dir):
        # 检查是否是第一级目录
        if root == base_dir:
            for dir_name in dirs:
                second_level_dirs.append(dir_name)
            break  # 只需要第一级子目录

    # 自定义排序，按照 '-' 前的数字
    sorted_dirs = sorted(second_level_dirs, key=lambda name: int(name.split('-')[0]))

    return sorted_dirs

# 使用示例
base_directory = "NRSVUE"  # 替换为实际路径
sorted_dirs = read_and_sort_subdirectories_by_number(base_directory)
print("Sorted Second-Level Directories by Number:")
# 读取bible_book_unique_id.json文件
with open('bible_book_unique_id.json', 'r') as json_file:
    book_unique_id = json.load(json_file)

dict = {}
for dir_name in sorted_dirs:
    # print(dir_name)
    print(dir_name.split('-')[-1])
    # print(book_unique_id.get(dir_name.split('-')[-1]))
    dict[dir_name.split('-')[-1]] = book_unique_id.get(dir_name.split('-')[-1])

print(json.dumps(dict))
# # 写入bible_book_kjv_unique_id.json文件
# with open('bible_book_' + str(base_directory) + '_unique_id.json', 'w') as json_file:
#     json.dump(dict, json_file)
