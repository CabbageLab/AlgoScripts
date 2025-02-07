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
# @Time    : 2025/01/10 14:44
# @题目     :
# @参考     :  
# 时间复杂度 :

from typing import Annotated, AsyncGenerator, Literal

import httpx
import ormsgpack
from pydantic import AfterValidator, BaseModel, conint

class ServeReferenceAudio(BaseModel):
    audio: bytes
    text: str

class ServeTTSRequest(BaseModel):
    text: str
    chunk_length: Annotated[int, conint(ge=100, le=300, strict=True)] = 200
    # Audio format
    format: Literal["wav", "pcm", "mp3"] = "mp3"
    mp3_bitrate: Literal[64, 128, 192] = 128
    # References audios for in-context learning
    references: list[ServeReferenceAudio] = []
    # Reference id
    # For example, if you want use https://fish.audio/m/7f92f8afb8ec43bf81429cc1c9199cb1/
    # Just pass 7f92f8afb8ec43bf81429cc1c9199cb1
    reference_id: str | None = None
    # Normalize text for en & zh, this increase stability for numbers
    normalize: bool = True
    # Balance mode will reduce latency to 300ms, but may decrease stability
    latency: Literal["normal", "balanced"] = "normal"

text_use = "After reading Philippians 4:4-9, you might have noticed that Paul, despite his difficult circumstances, doesn’t ask for escape—he asks for peace. It’s amazing to think that Paul wrote this letter while he was in prison, and yet, his focus wasn’t on his suffering but on encouraging others to rejoice in the Lord and not to be anxious. The key here is in the advice he gives: instead of worrying, we’re told to bring our concerns to God in prayer. It’s not a promise that life will be free of troubles, but a reminder that peace doesn’t come from the absence of problems—it comes from God’s presence in our lives. One verse that really stands out is verse 7, where Paul talks about the peace of God guarding our hearts and minds. Imagine that—God’s peace is like a shield, protecting you from anxiety’s grip. Have you ever noticed how, when you take your worries to God, your problems may not immediately disappear, but your perspective shifts? What if you made it a habit to turn to God with everything, both big and small? Reflect on how this might change your daily life. As we close today's session, remember this: God's peace is available to you right now, in whatever situation you’re facing. Let's carry that peace with us as we move forward."

import time

print(len(text_use))
start = time.time()
print(start)

request = ServeTTSRequest(
    text=text_use,
    reference_id="536b85cafa3542c6860bb8a189d20308"
)
var_name = "FishKey"  # 替换为你需要查询的环境变量名称
value = os.getenv(var_name)
with (
    httpx.Client() as client,
    open("hello_world22222.mp3", "wb") as f,
):
    with client.stream(
            "POST",
            "https://api.fish.audio/v1/tts",
            content=ormsgpack.packb(request, option=ormsgpack.OPT_SERIALIZE_PYDANTIC),
            headers={
                "authorization": value,
                "content-type": "application/msgpack",
            },
            timeout=None,
    ) as response:
        for chunk in response.iter_bytes():
            f.write(chunk)
end = time.time()
print(end)
print(int(end - start))
