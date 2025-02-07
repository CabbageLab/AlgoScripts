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

import requests
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
# 打印起始时间和结束时间
import time

start1 = time.time()
print(start1)

name = "Uncle"
var_name = "FishKey"  # 替换为你需要查询的环境变量名称
value = os.getenv(var_name)
response = requests.post(
    "https://api.fish.audio/model",
    files=[
        ("voices", open("mp3/da_1.MP3", "rb")),
    ],
    data=[
        ("visibility", "private"),
        ("type", "tts"),
        ("title", name),
        ("train_mode", "fast"),
        # Enhance audio quality will remove background noise
        ("enhance_audio_quality", "true"),
        # Texts are optional, but if you provide them, they must match the number of audio samples
    ],
    headers={
        "Authorization": value,
    },
)
print(response.json())
reference_id = response.json()['_id']
start2 = time.time()
print("upload model time: " + str(int(start2 - start1)))

word10 = "Welcome to storyAI, use your voice to accompany your child during story time!"
word50 = "Welcome to StoryAI, where your voice brings stories to life! Whether it's bedtime or playtime, StoryAI lets you accompany your child on exciting adventures, nurturing their imagination and creativity. Share moments of joy and learning through interactive storytelling that grows with your child."
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
word1000 = """The Adventure of Timmy the Brave Little Tiger
Once upon a time in the heart of a vast and beautiful jungle, there lived a young tiger named Timmy. Timmy was not like the other tigers in the jungle. While most of the older tigers were strong and fierce, Timmy was small, but he had something even more special—he was full of curiosity and bravery.
One sunny morning, Timmy woke up to the sound of birds singing and the wind rustling through the leaves. Today felt like an adventure day, he thought. He decided to explore a part of the jungle he had never been to before: the Whispering Woods.
Timmy’s friends, a playful monkey named Max and a wise old owl named Olivia, were already up and playing near the edge of the jungle. Timmy bounded over to them, his tail twitching with excitement.
“Hey, Max! Olivia!” Timmy called. “I’m going on an adventure to the Whispering Woods! Want to come with me?”
Max swung down from a tree, hanging by his tail. “The Whispering Woods? I’ve heard strange things about that place,” he said with a little shiver. “It’s full of mysteries and hidden paths. Are you sure you want to go there, Timmy?”
Olivia, who was perched on a low branch, blinked her large eyes. “The Whispering Woods can be tricky. It’s easy to get lost if you don’t pay attention. But, if you’re determined, Timmy, you’ll find your way. Just remember to be brave and trust your heart.”
Timmy smiled. “I’m not scared! I’ve always wanted to see what’s in the woods. I’ll be careful, and I’ll come back with a great story!”
With that, Timmy set off toward the edge of the jungle, Max following closely behind and Olivia flying overhead. The path to the Whispering Woods was narrow and winding, but Timmy’s eyes sparkled with excitement.
As they entered the woods, the trees grew taller and the air cooler. The branches twisted together, making the sunlight filter through in beams. Strange sounds echoed around them—the soft rustling of leaves, the distant call of birds, and even a faint whispering that seemed to come from the trees themselves.
“This place is magical!” Timmy said, his voice full of awe. “Do you hear that? It’s like the trees are talking to us!”
Max’s eyes widened. “Maybe they’re telling us secrets! Or warning us to leave.”
Olivia hooted from above. “The Whispering Woods have been around for a long time. They hold many secrets, but they are not to be feared. Just listen closely, and you’ll understand.”
The trio ventured deeper into the woods, following the winding trail. The path grew more and more mysterious, with vines creeping down from the trees and strange flowers blooming along the edges. Timmy couldn’t help but feel a little nervous, but his curiosity pushed him forward.
Suddenly, the path split into two. On the left, the trail looked clear and sunny, while on the right, the path was dark and shadowy, with a thick fog swirling around the ground.
“What should we do?” Timmy asked, his voice shaking a little. “Which way should we go?”
Olivia perched on a nearby branch, deep in thought. “The path on the left looks safe, but sometimes, the best adventures lie in the unknown. The fog is a sign of something magical. If you feel brave, Timmy, go that way.”
Timmy hesitated for a moment, then nodded. “I’ll go down the foggy path. I’m not afraid!”
Max swung onto Timmy’s back. “I’m with you, buddy! Let’s go!”
With a deep breath, Timmy led the way into the foggy path. The air was cool and damp, and the fog clung to their fur. They could hardly see more than a few steps ahead, but Timmy was determined. He trusted his instincts and kept moving forward, his friends right behind him.
After what seemed like hours, the fog began to lift, and they found themselves standing in a small clearing. In the center of the clearing was a large stone circle, covered in moss and glowing faintly with an eerie blue light.
“What is this place?” Timmy whispered in awe.
Max examined the stones. “It looks like a forgotten temple or a magical circle. Do you think it’s safe to go inside?”
Before Timmy could answer, a soft voice echoed in the air. “Welcome, brave travelers.”
The three friends jumped back, startled. From the center of the stone circle, a figure emerged—an old, wise lion with a golden mane that shimmered in the dim light. His eyes twinkled with kindness.
“Who are you?” Timmy asked, his voice full of wonder.
“I am the Guardian of the Whispering Woods,” the lion replied. “I watch over these woods and protect its secrets. Only those with a brave heart can find this place. And only those who are pure of spirit may ask for a wish.”
Timmy’s heart raced. A wish! He had never even thought about asking for one. What would he wish for? Would it be for strength like the other tigers? Or for something else?
“What should I wish for?” Timmy asked the lion.
The lion smiled gently. “A wish made with a kind heart will always lead to the best path.”
Timmy thought for a moment. Then, with a bright smile, he spoke. “I wish to always be brave and to help others who are afraid, just like I did today.”
The lion nodded, his eyes full of pride. “Your wish is granted, young tiger. Your bravery will inspire others, and your kindness will light the way.”
Timmy felt a warm glow fill his chest, and he knew that his wish had come true.
“Thank you, Guardian,” Timmy said with a bow.
The lion stepped back into the stone circle, which began to glow brightly. “Remember, Timmy, the greatest strength lies not in physical power, but in the bravery of the heart.”
With that, the light faded, and the fog began to clear. Timmy, Max, and Olivia found themselves back at the edge of the Whispering Woods, where the jungle sun shone brightly.
“Wow,” Max said, “that was incredible! You’re really brave, Timmy.”
Olivia nodded. “You did exactly what you needed to do. You didn’t just face the unknown—you embraced it.”
Timmy smiled, feeling proud and happy. He had gone on an adventure and discovered that bravery wasn’t just about being strong—it was about being kind and helping others.
As they made their way back home, Timmy knew that he had made a difference in the world that day. And no matter what adventures lay ahead, he would always be ready to face them with a brave heart."""

arr = [word10, word50, word200, word500, word1000]
arr_name = ["word10", "word50", "word200", "word500", "word1000"]
for w, w_n in zip(arr, arr_name):
    start = time.time()
    with open(f"{name}_{w_n}.mp3", "wb") as f:
        for chunk in session.tts(TTSRequest(
                reference_id=reference_id,
                text=w,
        )):
            f.write(chunk)

    end = time.time()
    print(f"{w_n} time " + str(int(end - start)))
