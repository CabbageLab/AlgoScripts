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
# @Time    : 2024/12/12 10:10
# @题目     :
# @参考     :  
# 时间复杂度 :

import re

text = """
(24:2) Lorsque Saül fut revenu de la poursuite des Philistins, on vint lui dire: Voici, David est dans le désert d'En Guédi.

(24:3) Saül prit trois mille hommes d'élite sur tout Israël, et il alla chercher David et ses gens jusque sur les rochers des boucs sauvages.

(24:4) Il arriva à des parcs de brebis, qui étaient près du chemin; et là se trouvait une caverne, où il entra pour se couvrir les pieds. David et ses gens étaient au fond de la caverne.

(24:5) Les gens de David lui dirent: Voici le jour où l'Éternel te dit: Je livre ton ennemi entre tes mains; traite-le comme bon te semblera. David se leva, et coupa doucement le pan du manteau de Saül.
"""

# Remove the (x:x) pattern from the text
cleaned_text = re.sub(r'\(\d+:\d+\)', '', text)

print(cleaned_text)