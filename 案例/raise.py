try:
    print("我爱方雅君")
    print(123456.5)
    # 手动引发ValueError异常
    #注意语法: raise  ErrorClassName
    raise ValueError
    print("还没完")

except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")

finally:
    print("我肯定会被 执行的")