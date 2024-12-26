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
# @Time    : 2024/11/07 15:36
# @题目     :
# @参考     :  
# 时间复杂度 :

import boto3
import os

def upload_file_to_s3(s3_client, bucket_name, file_path, key_name, content_type):
    try:
        with open(file_path, 'rb') as data:
            s3_client.put_object(
                Bucket=bucket_name,
                Key=key_name,
                Body=data,
                ContentType=content_type
            )
        file_url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{key_name}"
        print(f"Uploaded {file_path} to {file_url}")
        return file_url
    except Exception as e:
        print(f"Failed to upload {file_path}: {e}")
        return None

def upload_directory_files(base_dir, bucket_name, access_key_id, secret_access_key, region_name):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name=region_name
    )

    for first_level_dir in os.listdir(base_dir):
        first_level_path = os.path.join(base_dir, first_level_dir)

        # 检查是否为一级目录
        if os.path.isdir(first_level_path):
            # 上传 mind/book_mind 目录下的 PNG 文件
            mind_dir = os.path.join(first_level_path, "mind", "book_mind_new")
            if os.path.exists(mind_dir):
                for filename in os.listdir(mind_dir):
                    if filename.endswith(".png"):
                        local_path = os.path.join(mind_dir, filename)
                        print(filename)
                        s3_key = f"blinkup/book/mind/{filename}"
                        file_url = upload_file_to_s3(s3_client, bucket_name, local_path, s3_key, "image/png")
                        print(file_url)

            # # 上传 mp3 目录下的 MP3 文件
            # mp3_dir = os.path.join(first_level_path, "mp3")
            # if os.path.exists(mp3_dir):
            #     for filename in os.listdir(mp3_dir):
            #         if filename.endswith(".mp3"):
            #             local_path = os.path.join(mp3_dir, filename)
            #             s3_key = f"blinkup/book/audio/{filename}"
            #             file_url = upload_file_to_s3(s3_client, bucket_name, local_path, s3_key, "audio/mpeg")
            #             print(file_url)

            # # 上传 text 目录下的 MD 文件
            # text_dir = os.path.join(first_level_path, "text")
            # if os.path.exists(text_dir):
            #     for filename in os.listdir(text_dir):
            #         if filename.endswith(".md"):
            #             local_path = os.path.join(text_dir, filename)
            #             s3_key = f"blinkup/book/chapter/{filename}"
            #             file_url = upload_file_to_s3(s3_client, bucket_name, local_path, s3_key, "text/markdown")
            #             print(file_url)


# 配置
bucket_name = "xxx"
access_key_id = "xxxx"
secret_access_key = "xxxx"
region_name = "xxx"
base_dir = "./AlgoScripts/Python3_Basis/file_rename/data_ai_book_new"

# 上传文件
upload_directory_files(base_dir, bucket_name, access_key_id, secret_access_key, region_name)

