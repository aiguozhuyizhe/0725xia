#给出提示信息
try:
    num =int(input("请输入你的数字:"))
    rst=100/num
    print("计算结果是:{0}".format(rst))
# 如果是多种error的情况
#需要把越具体的 错误，越放前面
#在异常类继承关系中，越是子类的异常，越往前面放，
#越是父类的异常，越往后放

#在处理异常的时候，一旦拦截到某个异常，则不再继续往下查看，
#直接进行下一个代码，即有finally则执行finally语句块，否则就执行下一个打语句块
except ZeroDivisionError as e:
    print("请输入正确数字：")
    print(e)
    exit()
except NameError as e:
    print("名字起错了")

    print(e)
    exit()
except AttributeError as e:
    print("好像属性哟问题")
    print(e)
    exit()
#所有异常都是继承自Exception
#如果写上下面这句话，任何异常都会拦截到
#而且下面这句话一定是最后一个exception
except Exception as e:
    print("不知道哪里错误")
    print(e)

