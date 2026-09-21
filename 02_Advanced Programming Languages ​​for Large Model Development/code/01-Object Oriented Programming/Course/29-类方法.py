class Phone:
    brand = "联想"  # 类属性的私有，限制不住

    @classmethod
    def set_new_brand(cls, new_brand):
        cls.brand = new_brand


# 修改类属性
Phone.set_new_brand("联不想")
print(Phone.brand)
