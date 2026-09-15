"""
6. 图书租借管理系统
项目背景：
​ 你是云飞软件科技有限公司的一名AI开发工程师，现在公司要为蓝天社区的图书馆开发一个图书管理系统。
蓝天社区图书馆需要数字化管理其图书租借业务，蓝天社区的图书馆现在的图书管理方式均为纸质记录方式，该方式效率低下且容易出错。
为此，需要开发一个图书租借管理系统，帮助图书管理员高效管理馆藏图书和租借业务。现在公司把部分开发任务分配给了你。

开发需求如下：
1、自定义函数 add_info()。
功能: 添加书籍，让用户输入要添加的书籍的书名、价格，书籍出租状态，并将这本书的信息添加到存储图书信息的列表中。
注意事项：
编号：设置为int类型，编号必须唯一；
书名：设置为str类型；
价格：设置为float类型，默认为0；
书籍出租状态：设置为bool类型，默认为【否】。

2、自定义函数 delete_info()。
功能: 根据编号删除书籍。让用户输入要删除的书籍的编号，并根据编号从存储图书信息的列表中，删除这本书。

3、自定义函数 update_info()。
功能: 修改书籍信息。让用户输入要修改的书籍的编号，再让用户选择要修改的字段，并输入修改的信息，然后根据编号从存储图书信息的列表中修改这本书的信息。
注意事项：
根据编号修改, 只能修改: 书籍名，价格，书籍出租状态.

4、自定义函数 search_info()。
功能: 查询某个书籍信息.
注意事项: 根据书籍名查询，使用占位符格式化输出书籍信息

5、自定义函数 search_all()。
功能: 查询所有书籍的信息，并使用占位符格式化分别输出每一本书的书籍信息。

6、定义函数 print_info() ，打印提示信息。
功能：打印提示界面(1-6的数字)，以及1-6个数字分别代表的操作，如下：
①输入1:  添加书籍(书籍编号,  书籍名，书籍价格，书籍出租状态【是/否】).
②输入2: 删除书籍(根据编号删除）
【删除时，需要判断书籍出租状态，如果书籍未出租，则删除书籍；如果书籍已出租，则打印“书籍已出租，暂无法删除”】)
③输入3: 修改书籍信息(只能改书籍名，书籍出租状态)
④当管理员选择4的时候, 实现操作: 查询单个书籍信息(根据书籍名查)
⑤输入5: 查询所有书籍信息
⑥输入6: 退出系统
7、打印提示界面, 让管理员登录账号和密码。
功能:自定义for循环, 让用户输入用户名和密码，并验证输入是否正确。
注意事项：
如果账号密码正确，打印“登陆成功！”
如果账号密码错误，打印“账号或密码错误，请重试”
三次机会，三次都登录失败，提示【错误次数达上限】，并退出系统.

8、读取文件“book.txt”。
功能:文件“book.txt”中存储的是现有图书的信息，书籍信息包括【书名，价格，书籍出租状态(是否已经出租)】。
读取文件中图书信息，并使用列表(list)存放所有书籍，每本书都用一个字典(dict)来存储书籍信息。
注意事项：
编号必须唯一，编号：设置为int类型；
书名：设置为str类型。
价格：设置为float类型；
书籍出租状态：设置为bool类型。

9、自定义while True循环逻辑， 实现用户录入什么选项, 就进行相应的操作
9.1、 调用函数print_info()， 打印提示界面(1-6的数字)。
9.2 、使用输入函数，提示让管理员输入1-6的数字，选择他/她要进行的操作【注意事项: 处理一下非法值】。
①当管理员选择1的时候, 调用 add_info()函数，实现添加书籍。
②当管理员选择2的时候, 调用 delete_info() 函数，实现删除书籍。
③当管理员选择3的时候, 调用 update_info() 函数，实现修改书籍信息。
④当管理员选择4的时候, 调用 search_info() 函数，实现 查询单个书籍信息。
⑤当管理员选择5的时候, 调用 search_all() 函数，实现查询所有书籍信息。
⑥当管理员选择6的时候, 退出循环，结束程序。）
编码规范和要求
变量命名需要见名知意，且需要符合Python变量命名规范（例如：蛇形命名法等）
给代码添加注释，且要符合Python注释规范
对代码进行异常处理：明确捕获异常类型
代码及运行效果截图
"""

"""
蓝天社区图书租借管理系统
"""

BOOK_FILE = "book.txt"

# 管理员账号和密码
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "123"


def parse_rental_status(status_text):
    """
    将用户输入的出租状态转换为bool类型。

    是、1、true、已出租 -> True
    否、0、false、未出租、空字符串 -> False
    """
    status_text = status_text.strip().lower()

    if status_text in ("是", "1", "true", "已出租"):
        return True

    if status_text in ("否", "0", "false", "未出租", ""):
        return False

    raise ValueError("出租状态只能输入“是”或“否”")


def read_books(file_name):
    """
    从文件中读取图书信息。

    兼容以下两种格式：
    书名,价格,出租状态
    编号,书名,价格,出租状态
    """
    books = []
    used_ids = set()

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for default_id, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                try:
                    data = line.split(",")

                    # 兼容原来的3列格式
                    if len(data) == 3:
                        book_name, price_text, status_text = data

                        book_id = default_id

                        # 保证自动生成的编号不重复
                        while book_id in used_ids:
                            book_id += 1

                    # 新的4列格式
                    elif len(data) == 4:
                        id_text, book_name, price_text, status_text = data
                        book_id = int(id_text.strip())

                    else:
                        print("图书数据格式错误，已跳过：{}".format(line))
                        continue

                    book_name = book_name.strip()
                    book_price = float(price_text.strip())
                    status_number = int(status_text.strip())

                    if book_id <= 0:
                        raise ValueError("图书编号必须大于0")

                    if book_id in used_ids:
                        raise ValueError("图书编号重复")

                    if not book_name:
                        raise ValueError("书名不能为空")

                    if book_price < 0:
                        raise ValueError("图书价格不能小于0")

                    if status_number not in (0, 1):
                        raise ValueError("出租状态必须是0或1")

                    book = {
                        "id": book_id,
                        "name": book_name,
                        "price": book_price,
                        "is_rented": bool(status_number)
                    }

                    books.append(book)
                    used_ids.add(book_id)

                except ValueError as error:
                    print(
                        "图书数据错误，已跳过：{}，原因：{}".format(
                            line, error
                        )
                    )

    except FileNotFoundError:
        print("没有找到{}，系统将使用空图书列表。".format(file_name))

    except PermissionError:
        print("没有权限读取文件：{}".format(file_name))

    except OSError as error:
        print("读取文件失败：{}".format(error))

    return books


def save_books(books, file_name):
    """
    将图书列表保存到文件。

    保存格式：
    编号,书名,价格,出租状态
    """
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            for book in books:
                status_number = 1 if book["is_rented"] else 0

                file.write(
                    "{},{},{},{}\n".format(
                        book["id"],
                        book["name"],
                        book["price"],
                        status_number
                    )
                )

        return True

    except PermissionError:
        print("没有权限写入文件：{}".format(file_name))
        return False

    except OSError as error:
        print("保存图书信息失败：{}".format(error))
        return False


def find_book_by_id(books, book_id):
    """根据编号查找图书。"""
    for book in books:
        if book["id"] == book_id:
            return book

    return None


def print_book(book):
    """使用占位符格式化输出一本图书的信息。"""
    rental_status = "是" if book["is_rented"] else "否"

    print(
        "编号：{}，书名：{}，价格：{:.2f}元，是否出租：{}".format(
            book["id"],
            book["name"],
            book["price"],
            rental_status
        )
    )


def add_info(books):
    """添加图书，并保存到文件。"""
    print("\n========== 添加书籍 ==========")

    while True:
        book_id_text = input("请输入图书编号：").strip()

        try:
            book_id = int(book_id_text)

            if book_id <= 0:
                print("图书编号必须是大于0的整数")
                continue

            if find_book_by_id(books, book_id) is not None:
                print("该图书编号已经存在，请重新输入")
                continue

            break

        except ValueError:
            print("图书编号必须是整数")

    while True:
        book_name = input("请输入书名：").strip()

        if book_name:
            break

        print("书名不能为空")

    while True:
        price_text = input("请输入价格（直接回车默认为0）：").strip()

        try:
            if price_text == "":
                book_price = 0.0
            else:
                book_price = float(price_text)

            if book_price < 0:
                print("图书价格不能小于0")
                continue

            break

        except ValueError:
            print("图书价格必须是数字")

    while True:
        status_text = input(
            "图书是否已经出租（是/否，直接回车默认为否）："
        )

        try:
            rental_status = parse_rental_status(status_text)
            break

        except ValueError as error:
            print(error)

    new_book = {
        "id": book_id,
        "name": book_name,
        "price": book_price,
        "is_rented": rental_status
    }

    books.append(new_book)

    if save_books(books, BOOK_FILE):
        print("书籍添加成功！")
    else:
        # 保存失败时撤销本次添加
        books.remove(new_book)
        print("文件保存失败，本次添加已撤销")


def delete_info(books):
    """根据编号删除未出租的图书，并保存到文件。"""
    print("\n========== 删除书籍 ==========")

    try:
        book_id = int(input("请输入要删除的图书编号：").strip())

    except ValueError:
        print("图书编号必须是整数")
        return

    target_book = find_book_by_id(books, book_id)

    if target_book is None:
        print("未找到该编号对应的书籍")
        return

    if target_book["is_rented"]:
        print("书籍已出租，暂无法删除")
        return

    # 记录原来的位置，方便保存失败时恢复
    original_index = books.index(target_book)
    books.remove(target_book)

    if save_books(books, BOOK_FILE):
        print("书籍删除成功！")
    else:
        books.insert(original_index, target_book)
        print("文件保存失败，本次删除已撤销")


def update_info(books):
    """根据编号修改图书信息，并保存到文件。"""
    print("\n========== 修改书籍 ==========")

    try:
        book_id = int(input("请输入要修改的图书编号：").strip())

    except ValueError:
        print("图书编号必须是整数")
        return

    target_book = find_book_by_id(books, book_id)

    if target_book is None:
        print("未找到该编号对应的书籍")
        return

    print("\n当前图书信息：")
    print_book(target_book)

    print("\n请选择要修改的字段：")
    print("1. 修改书名")
    print("2. 修改价格")
    print("3. 修改出租状态")

    update_choice = input("请选择1～3：").strip()

    # 保存修改前的数据，文件写入失败时用于恢复
    old_name = target_book["name"]
    old_price = target_book["price"]
    old_status = target_book["is_rented"]

    if update_choice == "1":
        new_name = input("请输入新的书名：").strip()

        if not new_name:
            print("书名不能为空")
            return

        target_book["name"] = new_name

    elif update_choice == "2":
        try:
            new_price = float(input("请输入新的价格：").strip())

            if new_price < 0:
                print("图书价格不能小于0")
                return

            target_book["price"] = new_price

        except ValueError:
            print("图书价格必须是数字")
            return

    elif update_choice == "3":
        try:
            new_status_text = input(
                "请输入新的出租状态（是/否）："
            )

            target_book["is_rented"] = parse_rental_status(
                new_status_text
            )

        except ValueError as error:
            print(error)
            return

    else:
        print("操作选项无效，请输入1～3")
        return

    if save_books(books, BOOK_FILE):
        print("图书信息修改成功！")
    else:
        # 文件保存失败，恢复修改前的数据
        target_book["name"] = old_name
        target_book["price"] = old_price
        target_book["is_rented"] = old_status

        print("文件保存失败，本次修改已撤销")


def search_info(books):
    """根据书名查询图书信息。"""
    print("\n========== 查询书籍 ==========")

    search_name = input("请输入要查询的书名：").strip()

    if not search_name:
        print("查询的书名不能为空")
        return

    matched_books = []

    for book in books:
        if book["name"] == search_name:
            matched_books.append(book)

    if not matched_books:
        print("未查询到书名为“{}”的图书".format(search_name))
        return

    print("\n查询结果：")

    for book in matched_books:
        print_book(book)


def search_all(books):
    """查询并输出所有图书信息。"""
    print("\n========== 所有书籍 ==========")

    if not books:
        print("当前没有图书信息")
        return

    for book in books:
        print_book(book)

    print("当前共有{}本图书。".format(len(books)))


def print_info():
    """打印图书管理系统菜单。"""
    print("\n========== 图书租借管理系统 ==========")
    print("1. 添加书籍")
    print("2. 删除书籍")
    print("3. 修改书籍信息")
    print("4. 查询单个书籍信息")
    print("5. 查询所有书籍信息")
    print("6. 退出系统")
    print("====================================")


def login():
    """管理员登录，最多允许输入三次。"""
    print("========== 管理员登录 ==========")

    for attempt in range(1, 4):
        username = input("请输入管理员账号：").strip()
        password = input("请输入管理员密码：").strip()

        if (
                username == ADMIN_USERNAME
                and password == ADMIN_PASSWORD
        ):
            print("登录成功！")
            return True

        remaining_attempts = 3 - attempt

        if remaining_attempts > 0:
            print(
                "账号或密码错误，请重试，还剩{}次机会。".format(
                    remaining_attempts
                )
            )
        else:
            print("错误次数达上限")

    return False


def main():
    """运行图书租借管理系统。"""
    if not login():
        print("系统已退出")
        return

    books = read_books(BOOK_FILE)

    # 把原来的3列文件转换成带编号的4列格式
    save_books(books, BOOK_FILE)

    while True:
        print_info()

        choice = input("请输入1～6选择操作：").strip()

        if choice == "1":
            add_info(books)

        elif choice == "2":
            delete_info(books)

        elif choice == "3":
            update_info(books)

        elif choice == "4":
            search_info(books)

        elif choice == "5":
            search_all(books)

        elif choice == "6":
            print("已退出图书租借管理系统")
            break

        else:
            print("输入非法，请输入1～6之间的数字")


if __name__ == "__main__":
    main()
