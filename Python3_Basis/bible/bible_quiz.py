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
# @Time    : 2024/10/16 17:11
# @题目     :
# @参考     :
# 时间复杂度 :

if __name__ == '__main__':
    import pandas as pd

    file_path = '/Users/yinpeng/GoWorkSpace/AlgoScripts/Golang_Basis/tts/reading_plan/bible_in_a_year/quiz/output3.xlsx'
    df = pd.read_excel(file_path, sheet_name="Sheet1", engine='openpyxl')
    # print(df['chapter3'])
    columns = df['chapters3']
    questions = []
    flag = False
    flagD=False
    current_question = {}
    for data_str in columns:
        # 解析原始字符串
        lines = data_str.strip().splitlines()

        for line in lines:
            line = line.strip()
            if line is None:
                continue
            print(line)
            print("=============")
            if "Referenced Chapter:" in line:
                flagD=True
            if flag:
                current_question = {"Question": line.strip()}
                flag = False
            if line.startswith("Question"):
                flag = True
                current_question = {"Question_Number": line.strip()}

            elif line.startswith("A)"):
                current_question["Option_A"] = line[3:].strip()
            elif line.startswith("B)"):
                current_question["Option_B"] = line[3:].strip()
            elif line.startswith("C)"):
                current_question["Option_C"] = line[3:].strip()
            elif line.startswith("D)"):
                current_question["Option_D"] = line[3:].strip()

            elif line.startswith("Correct Answer:"):
                current_question["Correct_Answer"] = line.split(":")[1].strip()[0]
            elif line.startswith("Referenced Chapter:"):
                current_question["Referenced_Chapter"] = line.split(":")[1].strip()

            # 添加最后一个问题
            if flagD:
                questions.append(current_question)
                current_question={}
                flagD=False

    print(questions)
    df = pd.DataFrame(questions)
    df.to_excel("questions_output3.xlsx", index=False)
    print(df)
