import os
import random
import re
import time
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
# @Time    : 2024/12/05 17:03
# @题目     :
# @参考     :
# 时间复杂度 :

import requests
from bs4 import BeautifulSoup

# 模拟浏览器请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def getUrlContent(book_name, chapter_title, chapter_url):
    response = requests.get(chapter_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 移除所有 <br> 标签
        for br in soup.find_all('br'):
            br.decompose()
        # Find the div containing the passage text
        passage_div = soup.find('div', class_='passage-text')
        # print(passage_div)
        print(
            "========================================================================================================================")
        # Extract the text inside the passage div
        if passage_div:

            # Get all span elements that contain the verse text
            verses = passage_div.find_all('span', class_='text')
            # 查找所有class为"chapternum"的span标签，并将其内容修改为"1"
            # 清空 class="chapternum" 的span标签内容
            for chapnum in soup.find_all('span', class_='chapternum'):
                chapnum.string = ''  # 将内容清空

            # 清空 sup 标签的内容
            for sup in soup.find_all('sup', class_='versenum'):
                sup.string = ''  # 将内容清空
            # Initialize an empty string to store the cleaned text
            cleaned_text = ""
            # 用于保存拼接内容的字典
            content_dict = {}
            title = ""
            # Process each verseclass=""
            for i in range(0, len(verses)):
                verse = verses[i]
                # # Remove any 'chapternum' span (which contains the sequence numbers)
                # for chapternum in verse.find_all(class_='chapternum'):
                #     chapternum.decompose()  # Remove the 'chapternum' element
                #
                # for chapternum in verse.find_all(class_='versenum'):
                #     chapternum.decompose()  # Remove the 'chapternum' element

                # Append the cleaned verse text
                for sup_tag in soup.find_all('sup', class_='crossreference'):
                    sup_tag.decompose()  # 完全删除 <sup> 标签及其内部内容
                # print(verse)

                for sup_tag in verse.find_all('sup', class_='footnote'):
                    sup_tag.decompose()  # 完全删除 <sup> 标签及其内部内容

                for sup_tag in verse.findAll('b', class_='inline-h3'):
                    # content_dict[str(random.randint(1, 1000)) + str(random.randint(1, 1000))] = "#" + sup_tag.get_text()
                    # sup_tag.string=''  # 完全删除 <sup> 标签及其内部内容
                    sup_tag.decompose()  # 完全删除 <sup> 标签及其内部内容

                # if i > 1 and not verse.find('sup'):
                #     verse.clear()  # 清空span标签中的所有内容
                # print(verse)

                class_name = ' '.join(verse.get('class', []))
                span_text = verse.get_text().replace("\n", "")
                # if i == 0:
                #     title = span_text
                #     continue
                if class_name in content_dict:
                    content_dict[class_name] += " " + span_text
                else:
                    if verse.find('sup', class_="versenum") or verse.findAll('span', class_="chapternum"):
                        content_dict[class_name] = span_text
                    else:
                        if span_text.startswith("Chapter "):
                            continue
                        else:
                            content_dict[class_name + str(random.randint(1, 1000)) + str(
                                random.randint(1, 1000))] = "#" + span_text
            # Create a directory for the book if it doesn't exist
            book_dir = f"./{dir}/{book_name}"
            os.makedirs(book_dir, exist_ok=True)
            # Construct the file path using the chapter title
            file_name_serial = chapter_title.split(" ")[-1]
            file_path = os.path.join(book_dir, f"{file_name_serial}.txt")
            # 先清空文件内容（以写模式打开，覆盖原内容）
            print(title)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.truncate(0)  # 清空文件内容（虽然 'w' 模式已经会清空文件，但这里是明确清空文件）
                # file.write("#" + title + "\n\n")

            index = 1
            for class_name, content in content_dict.items():
                # print(f'Class: {class_name} Content: {content}\n')
                # Save the cleaned text into the corresponding chapter file
                with open(file_path, 'a', encoding='utf-8') as file:
                    file.write(content.strip().replace(" ", ".") + "\n\n")  # Remove trailing newlines
                    index += 1

            print("Text has been saved as 'genesis_1_no_sequence_numbers.txt'.")
        else:
            print("Passage text not found.")

if __name__ == '__main__':
    # URL 地址

    # dir = "ESV"
    # url = "https://www.biblegateway.com/versions/English-Standard-Version-ESV-Bible/#booklist"

    # dir = "NRSVUE"
    # url = "https://www.biblegateway.com/versions/New-Revised-Standard-Version-Updated-Edition-NRSVue-Bible/#booklist"
    #
    # dir = "NABRE"
    # url = "https://www.biblegateway.com/versions/New-American-Bible-Revised-Edition-NABRE-Bible/#booklist"
    # dir = "NIV"
    # url = "https://www.biblegateway.com/versions/New-International-Version-NIV-Bible/#booklist"

    dir = "NLT"
    url = "https://www.biblegateway.com/versions/New-Living-Translation-NLT-Bible/#booklist"

    # dir = "LSG"
    # url = "https://www.biblegateway.com/versions/Louis-Segond-LSG/#booklist"

    # dir = "LUTH1545"
    # url = "https://www.biblegateway.com/versions/Luther-Bibel-1545-LUTH1545/#booklist"

    # NRSVUE
    # dir="NRSVUE"
    # url="https://www.biblegateway.com/versions/New-Revised-Standard-Version-Updated-Edition-NRSVue-Bible/#booklist"
    # 发送请求
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 定位包含书籍信息的<tr>标签
        book_rows = soup.find_all('tr', class_=re.compile(r'\b(ot-book|nt-book)\b'))
        index = 1
        flag = False
        for row in book_rows:
            # if index <= 1:
            #     index += 1
            #     continue
            # 提取书名
            book_name_td = row.find('td', class_='toggle-collapse2 book-name')
            if book_name_td:
                book_name = ''.join(book_name_td.find_all(text=True, recursive=False)).strip()
                chapters_count = book_name_td.find('span', class_='num-chapters').text.strip()
                # if flag or book_name != "Acts" or flag:
                #     continue
                # else:
                #     flag = True
                print(f"书名: {book_name}, 章节数: {chapters_count}")

            # 提取章节链接
            chapters_td = row.find('td', class_='chapters')
            if chapters_td:
                chapter_links = chapters_td.find_all('a')
                for link in chapter_links:
                    chapter_title = link.get('title', '未知章节')
                    chapter_url = "https://www.biblegateway.com" + link.get('href', '')
                    print(f"  {chapter_title}: {chapter_url}")
                    getUrlContent(str(index) + "-" + book_name, chapter_title, chapter_url)
                    time.sleep(1)
            index += 1
    else:
        print(f"请求失败，状态码: {response.status_code}")
