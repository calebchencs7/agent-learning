print('------------------程序开始--------------------')
try:
    print(1 / 0)
except Exception as e:
    print(f"except:有异常时捕获异常,异常信息为:{e}")
else:
    print('else:没有异常执行的代码...')
finally:
    print('finally:不管有没有异常都会执行的代码...')
print('------------------程序结束--------------------')
