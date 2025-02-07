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
# @Time    : 2025/01/13 14:04
# @题目     :
# @参考     :  
# 时间复杂度 :

from pathlib import Path
from openai import OpenAI

speech_file_path = Path(__file__).parent / "siliconcloud-generated-speech.mp3"

client = OpenAI(
    api_key="YOUR_API_KEY", # 从 https://cloud.siliconflow.cn/account/ak 获取
    base_url="https://api.siliconflow.cn/v1"
)

with client.audio.speech.with_raw_response.create(
        model="fishaudio/fish-speech-1.5",
        voice="", # 此处传入空值，表示使用动态音色
        # 用户输入信息
        input="SiliconCloud 上提供的fish audio模型是基于 70 万小时多语言音频数据训练的领先文本到语音（TTS）模型，支持中文、英语、日语、德语、法语、西班牙语、韩语、阿拉伯语等多种语言，并能够音色克隆，具有非常好的实时性。",
        response_format="mp3",
        extra_body={"references":[
            {
                "audio": "https://sf-maas-uat-prod.oss-cn-shanghai.aliyuncs.com/voice_template/fish_audio-Alex.mp3", # 参考音频 url。也支持 base64 格式
                "text": "在一无所知中, 梦里的一天结束了，一个新的轮回便会开始", # 参考音频的文字内容
            }
        ]}
) as response:
    response.stream_to_file(speech_file_path)
