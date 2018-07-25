#给出提示信息
try:
    num =int(input("请输入你的数字:"))
    rst=100/num
    print("计算结果是:{0}".format(rst))
#捕获异常后，把异常实例化，出现信息会在实例里
#注意以下写法
#以下语句是捕获ZeroDivisionError 异常并实例化实例e
except ZeroDivisionError as e:
    print("请输入正确数字：")
    print(e)
    exit()


#作业  为什么我们可以直接打印出实例e，此时实例e应该实现了哪个函数