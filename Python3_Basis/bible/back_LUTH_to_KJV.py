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
# @Time    : 2024/12/11 11:11
# @题目     :
# @参考     :  
# 时间复杂度 :

# KJV mapping from the user
kjv_mapping = {
    "Genesis": 33, "Exodus": 29, "Leviticus": 50, "Numbers": 58, "Deuteronomy": 25,
    "Joshua": 45, "Judges": 47, "Ruth": 66, "1 Samuel": 7, "2 Samuel": 16,
    "1 Kings": 4, "2 Kings": 13, "1 Chronicles": 1, "2 Chronicles": 10, "Ezra": 31,
    "Nehemiah": 57, "Esther": 28, "Job": 41, "Psalms": 63, "Proverbs": 62,
    "Ecclesiastes": 26, "Song of Solomon": 68, "Isaiah": 38, "Jeremiah": 40,
    "Lamentations": 49, "Ezekiel": 30, "Daniel": 24, "Hosea": 37, "Joel": 42,
    "Amos": 21, "Obadiah": 59, "Jonah": 44, "Micah": 55, "Nahum": 56,
    "Habakkuk": 34, "Zephaniah": 73, "Haggai": 35, "Zechariah": 72, "Malachi": 52,
    "Matthew": 54, "Mark": 53, "Luke": 51, "John": 43, "Acts": 20,
    "Romans": 65, "1 Corinthians": 2, "2 Corinthians": 11, "Galatians": 32,
    "Ephesians": 27, "Philippians": 61, "Colossians": 23, "1 Thessalonians": 8,
    "2 Thessalonians": 17, "1 Timothy": 9, "2 Timothy": 18, "Titus": 69,
    "Philemon": 60, "Hebrews": 36, "James": 39, "1 Peter": 6, "2 Peter": 15,
    "1 John": 3, "2 John": 12, "3 John": 19, "Jude": 46, "Revelation": 64
}

# LUTH1545 books in order
luth_books = [
    "1 Mose", "2 Mose", "3 Mose", "4 Mose", "5 Mose", "Josua", "Richter", "Rut",
    "1 Samuel", "2 Samuel", "1 Koenige", "2 Koenige", "1 Chronik", "2 Chronik",
    "Esra", "Nehemia", "Ester", "Hiob", "Psalm", "Sprueche", "Prediger",
    "Hohelied", "Jesaja", "Jeremia", "Klagelieder", "Hesekiel", "Daniel",
    "Hosea", "Joel", "Amos", "Obadja", "Jona", "Mica", "Nahum", "Habakuk",
    "Zephanja", "Haggai", "Sacharja", "Maleachi", "Matthaeus", "Markus", "Lukas",
    "Johannes", "Apostelgeschichte", "Roemer", "1 Korinther", "2 Korinther",
    "Galater", "Epheser", "Philipper", "Kolosser", "1 Thessalonicher",
    "2 Thessalonicher", "1 Timotheus", "2 Timotheus", "Titus", "Philemon",
    "Hebraeer", "Jakobus", "1 Petrus", "2 Petrus", "1 Johannes", "2 Johannes",
    "3 Johannes", "Judas", "Offenbarung"
]

# Corresponding KJV books in order of LUTH1545
kjv_books = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua",
    "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings",
    "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther", "Job",
    "Psalms", "Proverbs", "Ecclesiastes", "Song of Solomon", "Isaiah",
    "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos",
    "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai",
    "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts",
    "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
    "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians",
    "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James",
    "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"
]

# Generate LUTH1545 mapping
luth_mapping = {luth: kjv_mapping[kjv] for luth, kjv in zip(luth_books, kjv_books)}

print(luth_mapping)
print(len(luth_mapping))
