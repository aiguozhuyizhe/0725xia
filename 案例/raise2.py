#自己定义异常
#需要注意：自定义异常必须是系统异常的子类

class XiaoJia(ValueError):#XiaoJia是继承自ValueError的
    pass
try:
    print("我爱方雅君")
    print(123456.5)
    # 手动引发ValueError异常
    #注意语法: raise  ErrorClassName
    raise XiaoJia
    print("还没完")

except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")

finally:
    print("我肯定会被 执行的")