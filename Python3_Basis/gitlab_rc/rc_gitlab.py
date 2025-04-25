import re
from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys

from openai import OpenAI
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
# @Time    : 2025/02/10 14:59
# @题目     :
# @参考     :  
# 时间复杂度 :

from typing import List, Any
import gitlab
import os
from itertools import dropwhile
from openai import OpenAI
import openai
from dataclasses import dataclass
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

@dataclass
class Diff:
    path: str
    diff: str

# 从环境变量读取 GitLab 基础 URL 和私有 token
gitlab_base_url = "https://xxxx"
private_token = "xxx-xxx"
gl = gitlab.Gitlab(url=gitlab_base_url, private_token=private_token)

# openai.api_key = os.environ["OPENAI_API_KEY"]

def main():
    diffs, mr = get_diffs_from_mr()
    user_message_line = ["Review the following code:"]
    # 遍历差异列表，构建完整的审查信息
    for d in diffs:
        user_message_line.append(f"PATH: {d.path}; DIFF: {d.diff}")
    print(f'user_message: {user_message_line}')
    # 获取代码审查反馈
    # response = get_review(diffs)
    # # 记录审查反馈的日志
    # print(f'chatgpt: {response}')
    # # 在合并请求中创建一条讨论，包含审查反馈
    # mr.discussions.create({"body": response})

def get_diffs_from_mr() -> (List[Diff], Any):
    project = gl.projects.get(id=2)
    mr = project.mergerequests.get(id=1264)
    print(mr)
    changes = mr.changes()
    print(changes)
    diffs = [Diff(c['new_path'], sanitize_diff_content(c['diff'])) for c in changes['changes']]
    return diffs, mr

def sanitize_diff_content(diff: str):
    return "".join(list(dropwhile(lambda x: x != "@", diff[2:]))[2:])

def filter_diff_content(diff_content):
    filtered_content = re.sub(r'(^-.*\n)|(^@@.*\n)', '', diff_content, flags=re.MULTILINE)
    processed_code = '\n'.join([line[1:] if line.startswith('+') else line for line in filtered_content.split('\n')])
    return processed_code

def get_review(diffs):
    # 初始化用户消息，告知模型将进行代码审查
    user_message_line = ["Review the following code:"]
    # 遍历差异列表，构建完整的审查信息
    for d in diffs:
        user_message_line.append(f"PATH: {d.path}; DIFF: {d.diff}")
    # 将差异信息转换为字符串
    user_message = "\n".join(user_message_line)
    # 打印换行
    print(f'user_message: {user_message}')
    # 创建OpenAI ChatCompletion请求
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_TOKEN"),
    )
    message = client.chat.completions.create(
        model="gpt-4o-mini",  # 指定使用的模型
        messages=[  # 构建对话消息
            {
                "role": "system",  # 系统角色信息，定义模型的行为
                "content": gpt_message,
            },
            {"role": "user", "content": user_message},  # 用户角色信息，提供审查的具体内容
        ],
    )
    # 从模型响应中提取审查反馈
    response = message.choices[0].message.content
    return response

# Prompt
gpt_message = """
你是一位资深编程专家，gitlab的分支代码变更将以git diff 字符串的形式提供，
请你帮忙review本段代码。然后你review内容的返回内容必须严格遵守下面的格式，
包括标题内容。模板中的变量内容解释：变量5是代码中的优点儿 变量1是给review打分，分数区间为0~100分。 
变量2 是code review发现的问题点。  变量3是具体的修改建议。变量4是你给出的修改后的代码。 
必须要求：
    1. 以精炼的语言、严厉的语气指出存在的问题。
    2. 你的反馈内容必须使用严谨的markdown格式 
    3. 不要携带变量内容解释信息。
    4. 有清晰的标题结构。有清晰的标题结构。有清晰的标题结构。
返回格式严格如下：

### 😀代码评分：{变量1}

#### ✅代码优点：
{变量5}

#### 🤔问题点：
{变量2}

#### 🎯修改建议：
{变量3}

#### 💻修改后的代码：
```python
{变量4}

         """

if __name__ == "__main__":
    main()
