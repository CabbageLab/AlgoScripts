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
    # prosody object | null  prosody.speed number default:  prosody.volume number default: 0
    prosody: dict[str, float] | None = None
    # Normalize text for en & zh, this increase stability for numbers
    normalize: bool = True
    # Balance mode will reduce latency to 300ms, but may decrease stability
    latency: Literal["normal", "balanced"] = "normal"

text_use = """
Once upon a time in the magical land of Pupperdale, there was a special school called the Magical College of Friendship. Here, puppies and lambs learned how to be the best friends they could be. In this delightful school, there lived a bouncy little puppy named Buster and a fluffy, friendly lamb named Lila. Buster had soft, brown fur and a wiggly tail that never stopped wagging. Lila was creamy white with a sprinkle of curly wool that made her look like she had just come out of a cloud. Every day, they attended fun classes like ‘How to Share Your Toys’ and ‘The Art of Listening.’ But one sunny morning, something unusual happened! The school announced its biggest event of the year: *The Great Friendship Race*! It was an exciting race where pairs of friends would work together to complete wild and silly challenges. Buster was overjoyed! “Lila, we have to be partners!” he barked, wagging his tail so hard that he almost spun around. But Lila frowned a little. “Oh Buster, I’m not sure. You’re so fast, and I… well, I’m just a bit slow,” she said, looking down at her hooves. Buster felt a pang of disappointment. He didn’t want to race without Lila! But instead of giving up, he remembered what they had learned in school about friendship and cooperation. “That’s okay, Lila! We can practice together! We can win as a team!” Lila looked up and smiled, feeling happier. “Alright, let's do it, Buster!” The two friends practiced every day after school. They ran through flower fields and around giant trees. They leaped over logs and crawled under bushes. Buster would zoom ahead while Lila took her sweet time, but when Buster noticed Lila struggling, he would always run back and encourage her. “You can do it, Lila! Just believe in yourself!” As they practiced, Lila discovered she could jump higher than she thought, and Buster learned to slow down and give his friend a chance. They grew stronger and faster together, and their bond deepened like the roots of a great tree. Finally, the day of The Great Friendship Race arrived. Excitement buzzed in the air! Puppies wagged their tails, and lambs bounced on their hooves, ready for fun. Buster and Lila stood at the starting line, hearts pounding with anticipation. When the whistle blew, it was chaos! Puppies dashed like lightning, but Buster stayed close to Lila. They tackled each challenge side by side. They climbed over mountains made of marshmallows, scooted under rainbow arches, and even solved a riddle from a wise old owl professor! At one point, they came across a sticky, gooey obstacle that no one had completed yet. All the other teams were stuck! Lila looked worried, but Buster cheered her on. “Let’s think together! You can help me get through!” Together, they huddled, put their heads together, and devised a plan. With teamwork and laughter, they made it through! Finally, they crossed the finish line—cheering and giggling all the way. To everyone’s surprise, they didn’t come in first, but at that moment, it didn’t matter. They realized they had a special prize: they had built their friendship stronger than ever! All the students cheered, “Hooray for Buster and Lila!” With big smiles, Buster and Lila hugged. They learned that winning isn’t everything; true friendship and teamwork are what really matter. From that day on, they were always seen together, exploring new adventures in the magical land of Pupperdale. And they lived happily ever after, side by side, learning and laughing every step of the way!	
"""
import time

print(len(text_use))
start = time.time()
print(start)

request = ServeTTSRequest(
    text=text_use,
    reference_id="xxx"
)
var_name = "FishKey"  # 替换为你需要查询的环境变量名称
value = os.getenv(var_name)
with (
    httpx.Client() as client,
    open("xxx.mp3", "wb") as f,
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
