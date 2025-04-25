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

import time
import httpx
import ormsgpack
from pydantic import BaseModel, conint
from typing import Annotated, AsyncGenerator, Literal
from concurrent.futures import ThreadPoolExecutor


class ServeReferenceAudio(BaseModel):
    audio: bytes
    text: str


class ServeTTSRequest(BaseModel):
    text: str
    chunk_length: Annotated[int, conint(ge=100, le=300, strict=True)] = 200
    format: Literal["wav", "pcm", "mp3"] = "mp3"
    mp3_bitrate: Literal[64, 128, 192] = 128
    references: list[ServeReferenceAudio] = []
    reference_id: str | None = None
    prosody: dict[str, float] | None = None
    normalize: bool = True
    latency: Literal["normal", "balanced"] = "normal"


text_use = """Cinderella
Once upon a time, in a faraway kingdom, there lived a kind and gentle girl named Cinderella. After her father passed away, she was left with a harsh stepmother and two unkind stepsisters. They made Cinderella do all the chores—sweeping the floors, washing the dishes, and even tending to the garden. Despite her hardships, Cinderella remained warm-hearted and hopeful.
One bright morning, the King announced that a grand ball would be held at the palace, inviting every maiden in the kingdom. The ball was meant to help the Prince choose a bride, and every girl was excited to attend. Cinderella dreamed of going to the ball, but her stepmother laughed and said, “You have too many chores. You cannot go.”
"""

var_name = "FishKey"  # 替换为你需要查询的环境变量名称
value = os.getenv(var_name)


def send_request(request: ServeTTSRequest, request_id: int):
    start = time.time()

    with (
        httpx.Client() as client,
        open(f"SpongeBob_Story_Cinderella_batch_{request_id}.mp3", "wb") as f,
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
    print(f"Request {request_id} duration: {int(end - start)} seconds")


# 创建 20 个并发请求
request = ServeTTSRequest(
    text=text_use,
    reference_id="xxx",
    prosody={"speed": 1},
)

with ThreadPoolExecutor(max_workers=20) as executor:
    # 将 20 个任务提交给线程池执行
    futures = [executor.submit(send_request, request, i) for i in range(20)]

    # 等待所有线程完成
    for future in futures:
        future.result()  # 这里会阻塞，直到线程执行完成


