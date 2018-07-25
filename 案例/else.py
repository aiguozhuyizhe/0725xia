try:
    num=int(input("请输入你的num："))
    rst=100/num
    print("计算结果是:  {0}".format(rst))
except Exception as e:
    print("Exception")
else:
    print("No Exception")
finally:
    print("反正我会被执行")