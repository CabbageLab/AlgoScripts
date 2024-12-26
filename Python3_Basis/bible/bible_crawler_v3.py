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

path = './NRSV/'

def scrape_chapter():
    section_num = 1
    for section_name in sections:
        section_full_name = str(section_num) + '-' + section_name
        if not os.path.exists(path + section_full_name):
            os.makedirs(path + section_full_name)

        section_num += 1

        print('section_name==============' + str(section_name))

        for chapter_name in range(1, sections[section_name] + 1):
            print('chapter_name==============' + str(chapter_name))

            scrape_bible(section_name, section_full_name, chapter_name)

        time.sleep(1)

def scrape_bible(section_name, section_full_name, chapter_name):
    base_url = 'https://www.bible.com/bible/2016/' + get_fixed_section_name(section_name) + '.' + str(
        chapter_name) + '.NRSV.json'

    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    div_list = soup.find_all("div", class_=re.compile(r"^ChapterContent_[a-zA-Z]?\d?__\w+$"))
    content = ''
    # 用于保存拼接内容的字典
    content_dict = {}
    for div in div_list:
        verse_list = div.find_all("span", class_="ChapterContent_verse__57FIw")

        title = None
        # 查找第一个 class 为 ChapterContent_it__p_cmC 的 span 标签
        inner_span = div.find('span', class_='ChapterContent_heading__xBDcs')
        # 在该 span 标签内查找第二个 class 为 ChapterContent_heading__xBDcs 的 span 标签
        if inner_span:
            title = inner_span.get_text()
            print(inner_span.get_text())  # 输出：The Creation
        if title:
            print(title)
            content_dict["title" + str(random.randint(1, 1000))] = "#" + title
            # content += "#" + title + '\n\n'
        # last_verse_num = 0
        for verse_tags in verse_list:
            # 获取 data-usfm 属性的值
            usfm_value = verse_tags.get('data-usfm')
            print(usfm_value)
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
    with open(path + section_full_name + '/' + str(chapter_name) + '.txt', 'w', encoding='utf-8') as f:
        f.write(content)
        f.close()

sections = {
    'Genesis': 50,
    'Exodus': 40,
    'Leviticus': 27,
    'Numbers': 36,
    'Deuteronomy': 34,
    'Joshua': 24,
    'Judges': 21,
    'Ruth': 4,
    '1 Samuel': 31,
    '2 Samuel': 24,
    '1 Kings': 22,
    '2 Kings': 25,
    '1 Chronicles': 29,
    '2 Chronicles': 36,
    'Ezra': 10,
    'Nehemiah': 13,
    'Tobit': 14,
    'Judith': 16,
    'Esther': 10,
    '1 Maccabees': 16,
    '2 Maccabees': 15,
    'Job': 42,
    'Psalms': 150,
    'Proverbs': 31,
    'Ecclesiastes': 12,
    'Song of Solomon': 8,
    'Wisdom': 19,
    'Sirach': 51,
    'Isaiah': 66,
    'Jeremiah': 52,
    'Lamentations': 5,
    'Baruch': 6,
    'Ezekiel': 48,
    'Daniel': 14,
    'Hosea': 14,
    'Joel': 3,
    'Amos': 9,
    'Obadiah': 1,
    'Jonah': 4,
    'Micah': 7,
    'Nahum': 3,
    'Habakkuk': 3,
    'Zephaniah': 3,
    'Haggai': 2,
    'Zechariah': 14,
    'Malachi': 3,
    'Matthew': 28,
    'Mark': 16,
    'Luke': 24,
    'John': 21,
    'Acts': 28,
    'Romans': 16,
    '1 Corinthians': 16,
    '2 Corinthians': 13,
    'Galatians': 6,
    'Ephesians': 6,
    'Philippians': 4,
    'Colossians': 4,
    '1 Thessalonians': 5,
    '2 Thessalonians': 3,
    '1 Timothy': 6,
    '2 Timothy': 4,
    'Titus': 3,
    'Philemon': 1,
    'Hebrews': 13,
    'James': 5,
    '1 Peter': 5,
    '2 Peter': 3,
    '1 John': 5,
    '2 John': 1,
    '3 John': 1,
    'Jude': 1,
    'Revelation': 22
}

def get_fixed_section_name(section_name):
    if section_name == 'Genesis':
        return 'GEN'
    if section_name == 'Exodus':
        return 'EXO'
    if section_name == 'Leviticus':
        return 'LEV'
    if section_name == 'Numbers':
        return 'NUM'
    if section_name == 'Deuteronomy':
        return 'DEU'
    if section_name == 'Joshua':
        return 'JOS'
    if section_name == 'Judges':
        return 'JDG'
    if section_name == 'Ruth':
        return 'RUT'
    if section_name == '1 Samuel':
        return '1SA'
    if section_name == '2 Samuel':
        return '2SA'
    if section_name == '1 Kings':
        return '1KI'
    if section_name == '2 Kings':
        return '2KI'
    if section_name == '1 Chronicles':
        return '1CH'
    if section_name == '2 Chronicles':
        return '2CH'
    if section_name == 'Ezra':
        return 'EZR'
    if section_name == 'Nehemiah':
        return 'NEH'
    if section_name == 'Tobit':
        return 'TOB'
    if section_name == 'Judith':
        return 'JUD'
    if section_name == 'Esther':
        return 'EST'
    if section_name == '1 Maccabees':
        return '1MA'
    if section_name == '2 Maccabees':
        return '2MA'
    if section_name == 'Job':
        return 'JOB'
    if section_name == 'Psalms':
        return 'PSA'
    if section_name == 'Proverbs':
        return 'PRO'
    if section_name == 'Ecclesiastes':
        return 'ECC'
    if section_name == 'Song of Solomon':
        return 'SNG'
    if section_name == 'Wisdom':
        return 'WIS'
    if section_name == 'Sirach':
        return 'SIR'
    if section_name == 'Isaiah':
        return 'ISA'
    if section_name == 'Jeremiah':
        return 'JER'
    if section_name == 'Lamentations':
        return 'LAM'
    if section_name == 'Baruch':
        return 'BAR'
    if section_name == 'Ezekiel':
        return 'EZK'
    if section_name == 'Daniel':
        return 'DAN'
    if section_name == 'Hosea':
        return 'HOS'
    if section_name == 'Joel':
        return 'JOL'
    if section_name == 'Amos':
        return 'AMO'
    if section_name == 'Obadiah':
        return 'OBA'
    if section_name == 'Jonah':
        return 'JON'
    if section_name == 'Micah':
        return 'MIC'
    if section_name == 'Nahum':
        return 'NAM'
    if section_name == 'Habakkuk':
        return 'HAB'
    if section_name == 'Zephaniah':
        return 'ZEP'
    if section_name == 'Haggai':
        return 'HAG'
    if section_name == 'Zechariah':
        return 'ZEC'
    if section_name == 'Malachi':
        return 'MAL'
    if section_name == 'Matthew':
        return 'MAT'
    if section_name == 'Mark':
        return 'MRK'
    if section_name == 'Luke':
        return 'LUK'
    if section_name == 'John':
        return 'JHN'
    if section_name == 'Acts':
        return 'ACT'
    if section_name == 'Romans':
        return 'ROM'
    if section_name == '1 Corinthians':
        return '1CO'
    if section_name == '2 Corinthians':
        return '2CO'
    if section_name == 'Galatians':
        return 'GAL'
    if section_name == 'Ephesians':
        return 'EPH'
    if section_name == 'Philippians':
        return 'PHP'
    if section_name == 'Colossians':
        return 'COL'
    if section_name == '1 Thessalonians':
        return '1TH'
    if section_name == '2 Thessalonians':
        return '2TH'
    if section_name == '1 Timothy':
        return '1TI'
    if section_name == '2 Timothy':
        return '2TI'
    if section_name == 'Titus':
        return 'TIT'
    if section_name == 'Philemon':
        return 'PHM'
    if section_name == 'Hebrews':
        return 'HEB'
    if section_name == 'James':
        return 'JAS'
    if section_name == '1 Peter':
        return '1PE'
    if section_name == '2 Peter':
        return '2PE'
    if section_name == '1 John':
        return '1JN'
    if section_name == '2 John':
        return '2JN'
    if section_name == '3 John':
        return '3JN'
    if section_name == 'Jude':
        return 'JUD'
    if section_name == 'Revelation':
        return 'REV'
    else:
        return ''

if __name__ == '__main__':
    scrape_chapter()
#   scrape_bible('Hosea', '35-Hosea', 8)
