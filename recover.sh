#!/bin/bash

# https://juejin.cn/post/7325372794720960549  参考这个博客 进行没有提交的代码恢复

# 定义 Git 对象存放的根目录
GIT_OBJECTS_DIR="/Users/yinpeng/GoWorkSpace/AlgoScripts/.git/objects"
OUTPUT_DIR="./objects"  # 定义输出目录

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 遍历所有文件夹（排除 info 和 pack 文件夹）
for folder in "$GIT_OBJECTS_DIR"/*; do
  # 检查是否是目录
  if [ -d "$folder" ] && [[ "$(basename "$folder")" != "info" && "$(basename "$folder")" != "pack" ]]; then
    folder_name=$(basename "$folder") # 提取目录名
    # 创建对应的输出子目录
    mkdir -p "$OUTPUT_DIR/$folder_name"

    # 遍历该目录下的所有文件
    for file in "$folder"/*; do
      file_name=$(basename "$file") # 提取文件名
      # 拼接 Git 对象的完整哈希值
      object_hash="${folder_name}${file_name}"
      # 使用 git cat-file -p 读取内容并保存到文件
      git cat-file -p "$object_hash" > "$OUTPUT_DIR/$folder_name/$file_name"
      echo "Processed object: $object_hash -> $OUTPUT_DIR/$folder_name/$file_name"
    done
  fi
done
