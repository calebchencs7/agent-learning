"""
我们需要统计一个源文本文件中每个单词出现的次数，并将结果写入另一个目标文件。
源文件input.txt内容如下:
"""

import os

import os

# 1. 获取当前脚本所在路径，安全拼接文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, "input.txt")
output_file = os.path.join(current_dir, "output.txt")

# 2. 统计单词频率（保留首次出现的顺序）
word_counts = {}

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        # 按空格/换行切分单词
        words = line.split()
        for word in words:
            # 统计每个单词出现的次数
            word_counts[word] = word_counts.get(word, 0) + 1
            """
            上面的简介的计数方法等效于
            if word in word_counts:
                word_counts[word] = word_counts[word] + 1  # 已经有了，直接加 1
            else:
                word_counts[word] = 1                      # 还没有，设为 1
            """

# 3. 将结果按指定格式写入 output.txt
with open(output_file, "w", encoding="utf-8") as f:
    for word, count in word_counts.items():
        f.write(f"{word}: {count}\n")

print("统计完成！已成功写入 output.txt")
