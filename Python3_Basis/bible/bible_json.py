import pandas as pd
import json

# 定义 Excel 文件路径
file_path = 'bible_sort.xlsx'  # 替换为你的文件路径

# 读取 Excel 文件
excel_data = pd.ExcelFile(file_path)

# 选择对应的 sheet
sheet_name = 'Bible_book_list'  # 替换为实际 sheet 名称
data = excel_data.parse(sheet_name)

# 收集所有书名与排序 ID 的映射
bible_books_index = {}

# 将 KJV	NIV	NLT	NABRE	ESV	NKJV	NRSV	NRSVUE	NASB	ASV	LUTH1545	HAF	SCH2000	LSG	SG21	BDS2015 生成数组
columns_to_merge = ['KJV', 'NIV', 'NLT', 'NABRE', 'ESV', 'NKJV', 'NRSV', 'NRSVUE', 'NASB', 'ASV', 'LUTH1545', 'HAF', 'SCH2000', 'LSG', 'SG21', 'BDS2015']
# 遍历所有版本的列
# columns_to_merge = ['KJV', 'NIV', 'NLT', 'NABRE']
for column in columns_to_merge:
    if column in data.columns:
        # 添加到字典，过滤 NaN 和空值
        for name, book_id in zip(data[column], data['排序ID']):
            if pd.notna(name) and pd.notna(book_id) and name.strip():
                if name not in bible_books_index:
                    bible_books_index[name] = book_id

# 按 value (排序 ID) 排序
sorted_bible_books_index = dict(sorted(bible_books_index.items(), key=lambda item: item[1]))

# 保存为 JSON 文件
output_file_path = 'bible_books_index_1213.json'
with open(output_file_path, 'w') as json_file:
    json.dump(sorted_bible_books_index, json_file, indent=4, ensure_ascii=False)

print(f"去重、过滤空值并按排序 ID 排序的字典已保存为 JSON 文件：{output_file_path}")
