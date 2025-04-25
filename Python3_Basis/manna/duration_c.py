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
# @Time    : 2025/03/25 09:46
# @题目     :
# @参考     :  
# 时间复杂度 :


import re

def extract_key(entry):
    parts = entry.split()
    book, chapter1, chapter2 = parts[0].split('_')[:3]
    return (book, int(chapter1), int(chapter2))

def extract_key_value(entry):
    parts = entry.split()
    key = '_'.join(parts[0].split('_')[:3])  # acts_1_2 作为 key
    value = int(parts[1])  # 136 作为 value
    return key, value

if __name__ == '__main__':
    data_map = {}

    # 处理 ft__durations.txt
    with open('./ft__durations.txt', 'r') as f:
        lines_ft = f.readlines()
    sorted_lines_ft = sorted(lines_ft, key=extract_key)

    for line in sorted_lines_ft:
        key, value = extract_key_value(line)
        data_map[key] = value

    # 处理 pr__durations.txt
    with open('./pr__durations.txt', 'r') as f:
        lines_pr = f.readlines()
    sorted_lines_pr = sorted(lines_pr, key=extract_key)

    for line in sorted_lines_pr:
        key, value = extract_key_value(line)
        data_map[key] = data_map[key] + value

    # for key, value in data_map.items():
    #     print(f"{key}: {value}")

    with open("./course__durations.txt", 'r') as f:
        lines = f.readlines()
    sorted_lines_cs = sorted(lines, key=extract_key)
    # sorted_lines_cs 转成map 按照空格切分
    data_map_cs = {}
    for line in sorted_lines_cs:
        parts = line.split()
        key = parts[0].strip().split("_")[0] + "_" + parts[0].strip().split("_")[1]
        value = int(parts[1])
        data_map_cs[key] = data_map_cs.get(key, 0) + value

    for x in sorted_lines_cs:
        print(x.strip())
    for key, value in data_map_cs.items():
        print(f"{key}: {value}")

    # data_map 的数据 acts_1_2 拆分为 acts_1和 acts_2 去查找data_map_cs 将value加到acts_1_2上面
    for key, value in data_map.items():
        parts = key.split('_')
        book, chapter1, chapter2 = parts[:3]
        key1 = f"{book}_{chapter1}"
        key2 = f"{book}_{chapter2}"
        data_map[key] = data_map[key] + data_map_cs.get(key1, 0)
        data_map[key] = data_map[key] + data_map_cs.get(key2, 0)

    print("result:")
    for key, value in data_map.items():
        print(f"{key}: {value}")
    # 将结果写入文件
    with open("./result_time.txt", 'w') as f:
        for key, value in data_map.items():
            f.write(f"{key} {value}\n")
