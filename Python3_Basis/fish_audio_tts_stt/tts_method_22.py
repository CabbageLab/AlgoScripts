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
# @Time    : 2025/01/10 14:01
# @题目     :
# @参考     :  
# 时间复杂度 :

from fish_audio_sdk import Session, TTSRequest, ReferenceAudio
var_name = "FishKey"  # 替换为你需要查询的环境变量名称
value = os.getenv(var_name)
session = Session(value)

# Option 1: Using a reference_id
# with open("output1.mp3", "wb") as f:
#     for chunk in session.tts(TTSRequest(
#             reference_id="MODEL_ID_UPLOADED_OR_CHOSEN_FROM_PLAYGROUND",
#             text="Hello, world!"
#     )):
#         f.write(chunk)

# 打印起始时间和结束时间
import time
word50 = "Welcome to StoryAI, where your voice brings stories to life! Whether it's bedtime or playtime, StoryAI lets you accompany your child on exciting adventures, nurturing their imagination and creativity. Share moments of joy and learning through interactive storytelling that grows with your child."

text_use = "After reading Philippians 4:4-9, you might have noticed that Paul, despite his difficult circumstances, doesn’t ask for escape—he asks for peace. It’s amazing to think that Paul wrote this letter while he was in prison, and yet, his focus wasn’t on his suffering but on encouraging others to rejoice in the Lord and not to be anxious. The key here is in the advice he gives: instead of worrying, we’re told to bring our concerns to God in prayer. It’s not a promise that life will be free of troubles, but a reminder that peace doesn’t come from the absence of problems—it comes from God’s presence in our lives. One verse that really stands out is verse 7, where Paul talks about the peace of God guarding our hearts and minds. Imagine that—God’s peace is like a shield, protecting you from anxiety’s grip. Have you ever noticed how, when you take your worries to God, your problems may not immediately disappear, but your perspective shifts? What if you made it a habit to turn to God with everything, both big and small? Reflect on how this might change your daily life. As we close today's session, remember this: God's peace is available to you right now, in whatever situation you’re facing. Let's carry that peace with us as we move forward."
text_use_v2 = "After reading Philippians 4:4-9, you might have noticed that Paul, despite his difficult circumstances, doesn’t ask for escape—he asks for peace. After reading Philippians 4:4-9, you might have noticed that Paul, despite his difficult circumstances, doesn’t ask for escape—he asks for peace."
ref_text = """I'm late if I'm gonna be early Oh Do don't worry, Garbe, I'll be back before you can say why did he cruelly abandon me like that and isn't it a lovely morning Okay swimmer?Youve worked with her for years, She's the a burner grill in the kitchen Anyway, to fire her up, you've got to spark her flint manually and then jgle a yes Yes just a little and then read her favorite story, the little gridddle who could.Chapter 2, but we are fresh from the freezer, said the patties. and we're cococo cold. Don't worry, I'll get you nice and warm, said the little grid what you say squidwardt, Sidwardt. Okay, squidward doesn't matter. I'll always be here anyway.
"""
print(len(text_use))
print(len(text_use.split(" ")))
start = time.time()
print(start)
# Option 2: Using reference audio
with open("./mp3/haimian.MP3", "rb") as audio_file:
    with open("./spongeBob_word50_v2.mp3", "wb") as f:
        for chunk in session.tts(TTSRequest(
                text=word50,
                references=[
                    ReferenceAudio(
                        audio=audio_file.read(),
                        text=ref_text
                    )
                ]
        )):
            f.write(chunk)
end = time.time()
print(end)
print(int(end - start))
