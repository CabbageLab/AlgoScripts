import json
import random
import re

import requests
from bs4 import BeautifulSoup
import time
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

path = 'BDS2015'

def scrape_bible(section_name, book_name, chapter_name, index):
    base_url = 'https://www.bible.com/bible/21/' + section_name + '.' + str(
        chapter_name) + '.BDS'
    print(base_url)
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    div_list = soup.find_all("div", class_=re.compile(r"^ChapterContent_[a-zA-Z]{1,2}\d?__\w+$"))
    content = ''
    # 用于保存拼接内容的字典
    content_dict = {}
    for div in div_list:
        verse_list = div.find_all("span", class_="ChapterContent_verse__57FIw")

        for sup_tag in div.findAll('span', class_='ChapterContent_note__YlDW0'):
            sup_tag.decompose()  # 完全删除 <sup> 标签及其内部内容

        title = ""
        # 查找第一个 class 为 ChapterContent_it__p_cmC 的 span 标签
        inner_spans = div.find_all('span', class_='ChapterContent_heading__xBDcs')
        # 在该 span 标签内查找第二个 class 为 ChapterContent_heading__xBDcs 的 span 标签
        for inner_span in inner_spans:
            if inner_span:
                title += inner_span.get_text()
                print(inner_span.get_text())  # 输出：The Creation
        if title and len(title) > 0:
            print(title)
            content_dict["title" + str(random.randint(1, 1000)) + str(random.randint(1, 1000))] = "#" + title
            # content += "#" + title + '\n\n'
        # last_verse_num = 0
        for verse_tags in verse_list:
            # 获取 data-usfm 属性的值
            usfm_value = verse_tags.get('data-usfm')
            # print(usfm_value)
            # 序号
            # label = verse_tags.find("span", class_="ChapterContent_label__R2PLt")
            #     print('label==============' + str(label))
            #     verse_num = 0
            #     if label and label.get_text().isdigit() and int(label.get_text()) > last_verse_num:
            #       last_verse_num = int(label.get_text())
            #       verse_num = int(label.get_text())
            #     if verse_num > 0:
            #       content += '\n<bmstyle>' + str(verse_num) + '</bmstyle> '

            # verse
            verse = ''
            for verse_tag in verse_tags.find_all("span", class_="ChapterContent_content__RrUqA"):
                verse += verse_tag.get_text()
                if (verse_tag.get_text().endswith(',') or verse_tag.get_text().endswith(
                        '.') or verse_tag.get_text().endswith(':') or verse_tag.get_text().endswith(
                    ';') or verse_tag.get_text().endswith('!') or verse_tag.get_text().endswith('?')):
                    verse += ' '
            if verse.strip():
                # if not content.endswith(' ') and not content.endswith('—') and not verse.startswith(' '):
                #     content += ' '
                # content += verse.strip() + "\n\n"
                if usfm_value in content_dict:
                    content_dict[usfm_value] += " " + verse.strip()
                else:
                    content_dict[usfm_value] = verse.strip()

        # content = content.replace('</bmstyle>  ', '</bmstyle> ').replace('[', '').replace(']', '')

    # print(content_dict)
    for class_name, content2 in content_dict.items():
        content += content2 + "\n\n"

    # print('content==============\n' + content)
    # with open(path + section_full_name + '/' + str(chapter_name) + '.txt', 'w', encoding='utf-8') as f:
    #     f.write(content)
    #     f.close()
    #   print('content==============' + content)
    book_name = str(index) + "-" + book_name
    book_dir = f"./{path}/{book_name}"
    os.makedirs(book_dir, exist_ok=True)
    file_path = os.path.join(book_dir, f"{chapter_name}.txt")
    # print(content)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.truncate(0)  # 清空文件内容（虽然 'w' 模式已经会清空文件，但这里是明确清空文件）

    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content)
        f.close()

if __name__ == '__main__':
    # scrape_chapter()
    # 读取jsonLoadBible.json文件
    with open('./BDS.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        index = 1
        for vv in data["books"]:
            if index < 6:
                index += 1
                continue
            print(vv["human"], vv["usfm"], len(vv["chapters"]))
            for chapter_name in range(1, len(vv["chapters"]) + 1):
                print('chapter_name==============' + str(chapter_name))
                scrape_bible(vv["usfm"], vv["human"], chapter_name, index)
            index += 1
            time.sleep(1)

#   scrape_bible('Hosea', '35-Hosea', 8)
