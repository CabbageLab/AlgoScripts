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
# @Time    : 2024/12/16 16:37
# @题目     :
# @参考     :  
# 时间复杂度 :

if __name__ == '__main__':
    # 读取bible_book_unique_id.json 文件
    with open('./bible_book_unique_id.json', 'r') as f:
        bible_book_unique_id = json.load(f)

    # 读取chapter.txt文件 每一行都是[]
    with open('chapters.txt', 'r') as file:
        for line in file:
            chapters = json.loads(line)
            # ["Psalm 46", "Matthew 6:25-34", "Philippians 4:4-9"]
            result = []
            for c in chapters:
                # 使用空格分割字符串
                parts = c.split(" ")
                ss = ""
                # 如果长度大于等于3 1+2的字符串作为book_name 比如 1 Thessalonians 5:16-18
                if len(parts) >= 3:
                    book_name = " ".join(parts[:2])
                    ss = " ".join(parts[2:])
                else:
                    book_name = parts[0]
                    ss = " ".join(parts[1:])
                # 在bible_book_unique_id 找到对应的id
                book_id = bible_book_unique_id.get(book_name)
                # boo_id 加剩下的字符串 拼接起来 放到result里面
                result.append(str(book_id) + " " + ss)

                # result 写入追加到新的txt文件 直接一行json
            with open('chapter_new.txt', 'a') as f:
                f.write(json.dumps(result) + '\n')
