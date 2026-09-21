from pathlib import Path
import re

# 脚本所在的文件夹
folder = Path(__file__).parent

for file_path in folder.glob("*.py"):
    # 匹配文件名开头的数字和剩余内容
    result = re.match(r"^(\d+)(.*)$", file_path.name)

    if result is None:
        continue

    number = result.group(1)
    remaining = result.group(2)

    # 已经有横线的不再处理
    if remaining.startswith("-"):
        continue

    new_name = f"{number}-{remaining}"
    new_path = file_path.with_name(new_name)

    # 防止覆盖同名文件
    if new_path.exists():
        print(f"跳过，目标已存在：{new_name}")
        continue

    print(f"{file_path.name}  ->  {new_name}")
    file_path.rename(new_path)
