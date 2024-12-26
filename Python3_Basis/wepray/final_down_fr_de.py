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
# @Time    : 2024/12/25 10:27
# @题目     :
# @参考     :  
# 时间复杂度 :

import os
import requests

def download_audio_files():
    # 创建保存文件的文件夹
    save_dir = "bible_in_a_year_audio_fr"
    os.makedirs(save_dir, exist_ok=True)

    for i in range(116, 117):
        url = f'https://hakusai.com/wepray_business/reading_plan/fr/bible_year/bible_in_a_year_content_final_thoughts_{i}.mp3'
        local_filename = os.path.join(save_dir, f'content_final_thoughts_{i}.mp3')

        try:
            # 下载文件
            print(f"Downloading {url}...")
            response = requests.get(url, stream=True)
            response.raise_for_status()  # 检查请求是否成功

            # 将文件保存到本地
            with open(local_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):  # 分块写入
                    f.write(chunk)

            print(f"Saved: {local_filename}")

        except requests.RequestException as e:
            print(f"Failed to download {url}. Error: {e}")

if __name__ == '__main__':
    download_audio_files()



