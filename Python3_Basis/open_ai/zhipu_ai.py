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
# @Time    : 2024/08/26 23:57
# @题目     :
# @参考     :  
# 时间复杂度 :


from zhipuai import ZhipuAI

if __name__ == '__main__':
    value = os.getenv("ZhipuAIKey")
    client = ZhipuAI(api_key=value)  # 请填写您自己的APIKey

    response = client.chat.completions.create(
        model="glm-4-0520",  # 填写需要调用的模型编码
        messages=[
            {
                "role": "system",
                "content": "# Role Priest\n\n## Constraints\n- "
                           "`maybeAsk`: Based on the user's question, generate 4 questions that the user may ask next."
                           "\n-The recommended questions for the output need to be concise and consistent with biblical thinking."
                           "\n- Ask questions in the first person (I-me) rather than answering in the second person (you-you)."
                           "\n\n## Format\n- output this JSON format. {\\\"maybeAsk\\\":[\\\"<maybeAsk>\\\"]}."
            },
            {
                "role": "user",
                "content": "What are some practical steps I can take to forgive someone?"
            }
        ],
    )
    print(response.choices[0].message.content)
    print(len("Verses on Fear and Worry"))
