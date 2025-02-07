import pandas as pd
import requests

# 读取 Excel 文件
file_path = './player.xlsx'  # 替换为你的 Excel 文件路径
df = pd.read_excel(file_path)

# 输出读取的 DataFrame（查看文件内容）
# print(df.head())

# 创建一个映射字典，将 level.id 映射到角色名称
level_mapping = {
    "103": "雀杰",
    "104": "雀豪",
    "105": "雀圣",
    "107": "魂天"
}

# 定义一个函数来调用 API 获取 level.id 和角色名称
def get_level_id_and_role(nickname):
    url = f"https://5-data.amae-koromo.com/api/v2/pl4/search_player/{nickname}?limit=20&tag=all"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # 假设返回的第一个玩家对象里包含 level 信息
        if data and isinstance(data, list):
            player = data[0]
            level_id = player.get('level', {}).get('id')
            if level_id:
                # 获取 level 的前缀（例如 103, 104, 105, 107）
                level_prefix = str(level_id)[:3]
                role_name = level_mapping.get(level_prefix, "雀士/初心")  # 默认“未知角色”
                print(f"请求成功，昵称：{nickname}，level_id：{level_id} , role_name: {role_name}")
                return level_id, role_name
    else:
        print(f"请求失败，昵称：{nickname}，状态码：{response.status_code}")
        return None, None

# 对于每个昵称调用 API 获取 level.id 和角色名称，并填入新的列
df[['level_id', 'role_name']] = df['昵称'].apply(lambda x: pd.Series(get_level_id_and_role(x)))

# 输出修改后的 DataFrame
# print(df.head())

# 保存结果到新的 Excel 文件
df.to_excel('players_with_role.xlsx', index=False)
