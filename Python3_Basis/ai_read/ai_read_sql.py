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
# @Time    : 2024/11/08 11:08
# @题目     :
# @参考     :  
# 时间复杂度 :


import pandas as pd

# 书籍名称到bookId的映射
book_id_mapping = {
    "The 7 Habits of Highly Effective People": 1,
    "Atomic Habits": 2,
    "Boundaries": 3,
    "168 Hours": 4,
    "How to Win Friends and Influence People in the Digital Age": 5,
    "The 5 Love Languages": 6,
    "Daring Greatly": 7,
    "The Now Habit": 8,
    "I Will Teach You to Be Rich": 9,
    "Colorful Management": 10,
    "MicroSkills": 11,
    "The Art of Reading Minds": 12,
    "How to Get On with Anyone": 13,
    "Attached": 14,
    "Who Rules the World?": 15,
    "The High 5 Habit": 16,
    "The Book of Hope": 17,
    "Don't Sweat the Small Stuff and It's All Small Stuff": 18,
    "The Lemonade Life": 19,
    "Emotional Labor": 20,
    "High Output Management": 21,
    "Winners": 22,
    "Attitude is Everything": 23,
    "Tiny Habits": 24,
    "Beginners": 25,
    "The Education of Millionaires": 26,
    "How to Make People Like You in 90 Seconds": 27,
    "13 Things Mentally Strong People Don't Do": 28,
    "Ego is the Enemy": 29,
    "An Economist Walks into a Brothel": 30,
    "The Psychology of Money": 31,
    "Know Yourself, Know Your Money": 32,
    "Manage Your Money Like a F*cking Grownup": 33,
    "Shoe Dog": 34,
    "Get Out of Your Head": 35,
    "Switch on Your Brain": 36,
    "Fervent": 37,
    "Narcissists and You": 38,
    "The Untethered Soul": 39,
    "Boy Erased": 40,
    "Act Like a Success, Think Like a Success": 41,
    "The Great CEO Within": 42,
    "Built to Last": 43,
    "High_Road_Leadership": 44,
    "The First-Time Manager": 45,
    "Unbroken": 46,
    "The 1% Rule": 47,
    "This Is Me Letting You Go": 48,
    "Codependent No More": 49,
    "Single On Purpose": 50,
    "Men Are from Mars, Women Are from Venus": 51,
    "Taking Charge of Your Fertility": 52,
    "The Science of Happily Ever After": 53,
    "This Is How Your Marriage Ends": 54,
    "Hidden Potential": 55,
    "The 4-Hour Workweek": 56,
    "Getting to Zero - How to Work through Conflict in Your High-Stakes Relationships": 57,
    "How to Talk So Kids Will Listen & Listen So Kids Will Talk": 58,
    "Outliers": 59,
    "Conversations with Myself": 60,
    "The Relationship Cure": 61,
    "You Will Own Nothing": 62,
    "The End of the Myth": 63,
    "The Case for Trump": 64,
    "Get Good with Money": 65,
    "Never Enough": 66,
    "The Upside of Your Dark Side": 67,
    "The Happiness Project": 68
}

# 读取Excel文件
file_path = '/Users/yinpeng/GoWorkSpace/AlgoScripts/Python3_Basis/file_rename/ai_read_book_chapter.xlsx'  # 替换为你的Excel文件路径
df = pd.read_excel(file_path)

# 存储SQL语句
sql_statements = []

# 遍历Excel的每一行
for index, row in df.iterrows():
    book_name = row['书籍名称'].strip()
    chapter_name = row['章节名'].strip()
    chapter_content_url = row['章节内容url'].strip()
    audio_url = row['音频url'].strip()
    quote_count = int(row['章节名言数量'])
    duration = int(row['音频时长 s'])
    chapter_id_counter = int(row['书籍章节序号'])

    # 获取当前书籍的bookId
    if book_name in book_id_mapping:
        print(book_name)
        book_id = book_id_mapping[book_name]
    else:
        print(f"警告: 找不到书籍名称 {book_name} 对应的 bookId")
        continue  # 如果找不到对应的书籍名称，则跳过这一行

    chapter_name = chapter_name.replace("'", "\'")
    # 构建SQL语句
    sql = (chapter_id_counter, book_id, chapter_name, chapter_content_url, audio_url,duration, quote_count)

    # 添加到SQL语句列表
    sql_statements.append(sql)


# 对SQL语句按bookId和chapterId进行排序
sql_statements.sort(key=lambda x: (x[1], x[0]))  # 按book_id和chapter_id排序

# 将所有SQL语句输出到文件
output_file = 'insert_statements.sql'  # 输出文件名
with open(output_file, 'w', encoding='utf-8') as f:
    for statement in sql_statements:
        sql = f"INSERT INTO `ai_read_book_chapter` (`chapterId`, `bookId`, `chapterName`, `textUrl`, `mp3Url`, `duration`, `quoteCount`) VALUES {statement};"
        f.write(sql + '\n')

print(f"SQL语句已经写入到 {output_file}")

