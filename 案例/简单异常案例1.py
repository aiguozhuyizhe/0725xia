try:
    num =int(input("请输入你的数字:"))
    rst=100/num
    print("计算结果是:{0}".format(rst))
except:
    print("请输入正确数字：")
    exit()