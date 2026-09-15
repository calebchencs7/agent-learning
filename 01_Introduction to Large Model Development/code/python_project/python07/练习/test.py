def main():
    print("欢迎进入系统")


main()
print("程序结束")

data = """
As your report on White Pollution indicates, regulations on the use of plastic bags have not been implemented effectively in some areas.
I am writing this letter to express my concern over the abuse of plastic bags and make some suggestions.
"""
word_counts = {}
words = data.split()
for word in words:
    # 统计每个单词出现的次数
    word_counts[word] = word_counts.get(word, 0) + 1
