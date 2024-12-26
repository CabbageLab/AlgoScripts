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
# @Time    : 2024/11/07 15:24
# @题目     :
# @参考     :  
# 时间复杂度 :

import os

def generate_file_urls(base_dir):
    urls = {"mind": [], "mp3": [], "text": []}

    for first_level_dir in os.listdir(base_dir):
        first_level_path = os.path.join(base_dir, first_level_dir)

        # 检查是否为一级目录
        if os.path.isdir(first_level_path):
            # 定义 mind/book_mind、mp3 和 text 目录路径
            book_mind_path = os.path.join(first_level_path, "mind", "book_mind")
            mp3_path = os.path.join(first_level_path, "mp3")
            text_path = os.path.join(first_level_path, "text")

            # 生成 mind/book_mind 目录下的文件 URL
            if os.path.exists(book_mind_path) and os.path.isdir(book_mind_path):
                for filename in sorted(os.listdir(book_mind_path)):
                    if filename.endswith(".png"):
                        file_url = f"https://hakusai.com/blinkup/book/mind/{filename}"
                        urls["mind"].append(file_url)

            # 生成 mp3 目录下的文件 URL
            if os.path.exists(mp3_path) and os.path.isdir(mp3_path):
                for filename in sorted(os.listdir(mp3_path)):
                    if filename.endswith(".mp3"):
                        file_url = f"https://hakusai.com/blinkup/book/audio/{filename}"
                        urls["mp3"].append(file_url)

            # 生成 text 目录下的文件 URL
            if os.path.exists(text_path) and os.path.isdir(text_path):
                for filename in sorted(os.listdir(text_path)):
                    if filename.endswith(".md"):
                        file_url = f"https://hakusai.com/blinkup/book/chapter/{filename}"
                        urls["text"].append(file_url)

    return urls

def save_urls_to_files(urls):
    # 将链接分别写入三个文件，每个链接换行
    with open("mind_urls2.txt", "w") as mind_file:
        mind_file.write("\n".join(urls["mind"]) + "\n")

    with open("mp3_urls2.txt", "w") as mp3_file:
        mp3_file.write("\n".join(urls["mp3"]) + "\n")

    with open("text_urls2.txt", "w") as text_file:
        text_file.write("\n".join(urls["text"]) + "\n")

# 使用时将 base_dir 替换为你的一级目录路径
base_dir = "./AlgoScripts/Python3_Basis/file_rename/data_ai_book"
file_urls = generate_file_urls(base_dir)
save_urls_to_files(file_urls)

print("URLs have been saved to mind_urls.txt, mp3_urls.txt, and text_urls.txt.")
