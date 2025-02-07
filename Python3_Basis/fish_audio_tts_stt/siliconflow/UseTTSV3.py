from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from io import BytesIO
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys

import boto3
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
# @Time    : 2025/01/13 14:08
# @题目     :
# @参考     :  
# 时间复杂度 :
import requests
import time

start = time.time()

url = "https://api.siliconflow.cn/v1/audio/speech"

word200 = """The Little Lost Bunny

Once upon a time, there was a little bunny named Benny who loved to explore the woods. One sunny morning, Benny decided to hop further into the forest than ever before. He bounced along, sniffing flowers and chasing butterflies, until he realized he was lost.

Benny felt a bit scared. The trees seemed taller, and the path wasn’t the same anymore. But just as he began to feel worried, he heard a soft voice from behind a bush. "Hello, little bunny! Are you lost?"

It was a wise old owl named Ollie. "I’m lost," Benny said, his ears drooping. Ollie smiled and said, "Don’t worry. I can help you find your way home."

Ollie led Benny through the forest, pointing out the landmarks they passed. Soon, Benny could recognize the trees and flowers he had seen earlier. They reached Benny’s home, where his family was waiting for him.

“Thank you, Ollie!” Benny said, hopping happily. "I’m so glad to be home."

From that day on, Benny always remembered to stay close to home and ask for help when needed. He also made a new friend in Ollie the wise owl.

And they both lived happily ever after!"""

word500 = """The Adventure of Sunny the Squirrel
Once upon a time, in a large forest, there lived a young squirrel named Sunny. Sunny was very curious and loved exploring the forest, always hopping from tree to tree. She was small, with soft brown fur, a fluffy tail, and bright, shiny eyes that sparkled with wonder.
One bright and sunny morning, Sunny woke up with a big idea. She decided to go on a grand adventure to find the fabled Golden Acorn, a legendary treasure that everyone in the forest whispered about. The Golden Acorn was said to have magical powers, and whoever found it would be granted a special gift.
"Today is the day!" Sunny squeaked excitedly as she scurried out of her cozy nest. She packed a little bag with her favorite snacks—acorns, berries, and nuts—and set off into the deeper parts of the forest.
As she ventured further, Sunny met many animals. First, she came across Benny the bunny, who was hopping around in a field of wildflowers.
"Good morning, Benny!" Sunny called. "Have you seen any sign of the Golden Acorn?"
Benny twitched his nose and smiled. "I’ve heard stories, but no one has ever found it. Are you sure you want to go searching? The forest can be tricky."
Sunny nodded. "I’m not afraid! I’ll find it!"
Benny wished her luck and hopped off, leaving Sunny to continue her journey.
Next, Sunny reached the edge of the forest, where a fast-flowing river rushed by. She paused, looking at the water. The river was wide, and the current looked strong.
"How will I cross this?" Sunny wondered aloud. Just then, she saw a friendly beaver named Bella working nearby. Bella was busy building a dam.
"Hello, Bella!" Sunny called. "I need to cross the river. Can you help me?"
Bella smiled and nodded. "Of course! I can build a little bridge for you."
Within minutes, Bella had constructed a sturdy bridge, and Sunny carefully crossed over it, thanking Bella for her help.
As Sunny walked deeper into the forest, she felt a little nervous. The trees here were much taller, and the shadows grew darker. But she wasn’t about to give up. After all, she had a goal to reach.
Suddenly, she spotted something glowing in the distance. It was a soft golden light coming from under a large oak tree. Sunny's heart raced with excitement. Could it be the Golden Acorn?
She hurried over and saw something shining beneath the tree. It was an acorn, but not just any acorn—it was the Golden Acorn! It sparkled in the sunlight, and Sunny couldn’t believe her eyes.
"I found it!" she squeaked in delight.
Just then, the acorn began to glow even brighter, and a gentle voice echoed from the tree.
"Sunny, you have found the Golden Acorn. Because of your bravery and determination, you will be granted a gift."
Sunny closed her eyes, feeling the magic surround her. When she opened them again, she saw that she now had the ability to understand the language of all the animals in the forest. She could talk to everyone, from the tiniest ants to the biggest bears.
Sunny jumped up and down with joy. She couldn’t wait to share her new gift with her friends. From that day on, Sunny was known as the wisest and most helpful squirrel in the forest.
And so, Sunny’s adventure turned into a new journey of making friends, helping others, and learning even more about the world around her."""


payload = {
    "model": "fishaudio/fish-speech-1.5",
    "input": word500,
    "voice": "speech:SpongeBob_2:9qb2ao1x88:ilohfrohfjxebdyvscjs",
    "response_format": "mp3",
    "sample_rate": 32000,
    "stream": True,
    "speed": 1,
    "gain": 0
}
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

with requests.post(url, json=payload, headers=headers, stream=True) as resp:
    with open("SpongeBob_word500.mp3", "ab") as f:
        for chunk in resp.iter_content(chunk_size=8192):  # 每次读取 8192 字节
            if chunk:
                f.write(chunk)
        f.flush()
end = time.time()
print(end - start)



# 配置
bucket_name = "xxx"
access_key_id = "xxxx"
secret_access_key = "xxxx"
region_name = "xxx"
# 检查请求是否成功
# if response.status_code == 200:
#     # 初始化 boto3 客户端
#     s3_client = boto3.client(
#         's3',
#         aws_access_key_id=access_key_id,
#         aws_secret_access_key=secret_access_key
#     )
#
#     # 使用 BytesIO 将音频流上传到 S3
#     audio_stream = BytesIO(response.content)  # 将响应流保存到 BytesIO
#
#     s3_key = f"blinkup/test.mp3"  # S3 key
#     # 将音频文件上传到 S3
#     s3_client.upload_fileobj(audio_stream, bucket_name, s3_key)
#     print("音频文件已成功上传到 S3！")
# else:
#     print(f"请求失败，状态码: {response.status_code}")
