import datetime
import requests


# - 获取当前日期
def get_current_date():
    return datetime.datetime.now().month


# - 查询节假日
def search_holidays(month):
    holidays = {
        "1月": ["元旦: 1月1日-3日"],
        "2月": ["春节: 2月15日-23日"],
        "3月": [],
        "4月": ["清明节: 4月4日-6日"],
        "5月": ["劳动节: 5月1日-5日"],
        "6月": ["端午节: 6月19日-21日"],
        "7月": [],
        "8月": [],
        "9月": ["中秋节: 9月25日-27日"],
        "10月": ["国庆节: 10月1日-7日"],
        "11月": [],
        "12月": [],
    }
    # 根据传入的月份获取对应节假日列表
    month_holidays = holidays.get(str(month) + "月")
    print(month_holidays)


def get_weather(city):
    with requests.Session() as session:
        session.trust_env = False  # 不读取环境变量中的代理设置
        response = session.get(
            f"https://wttr.in/{city}",
            params={"format": "j1"},
            timeout=10,
        )
        response.raise_for_status()
        print(f"{city}的天气为:", response.json())


if __name__ == '__main__':
    # 测试工具函数
    month = get_current_date()
    # 测试
    search_holidays(month)
    # 测试天气
    get_weather('深圳')
