a="qwertyuiop"
b="azsxdc"
c="bnm"
count=0
for i in a:
    count+=1
print(f"{count}")
#imply funcation to opimizer
def count_1(date):
    count=0
    for i in date:
        count+=1
    print(f"{count}")
count_1(a)
count_1(b)
count_1(c)
def welcome():
    print("欢迎来到黑马课堂")
    print("请出示24小时核酸证明")
welcome()
def add(x,y):
    count=x+y
    print(f"{x}+{y}={count}")
add(5,6)
add(3,1)
add(5,8)
def temperature(v):
    if v>=37.5:
        print(f"您的体温是{v},大于37.5,温度过高,不准进入")
    else:
        print(f"您的体温是{v},小于37.5,温度正常,请进入!!!")
temperature(38)
temperature(36.4)
temperature(36)
def add2(m,n):
    result=m+n
    return result
r=add2(3,4)
print(r)
def add3(x,y):
    """
    """
    result=x+y
    print(f"两数相加的结果是{result}")
    return result
add3(4,5)
number=100

def k():
    print(f"k={number}")
def m():
    global number
    number=5000
    print(f"m={number}")
k()
m()
print(f"{number}")
print()
print()
print()
print()
print()
print()
print()
"""
import random 
money=random.randint(3000,400000)
name=input("你的名字是?")
print(f"你好，{name},欢迎来到黑马银行ATM,请选择相应的操作")
progress=input("查询余额【输入1}\n存款【输入2】\n取款【输入3】\n退出【输入4】\n")
progress=int(progress)
if progress==1:
    print(f"---------查询余额-----------\n{name},你好,您的余额剩余：{money}")
elif progress==2:
    input1=input("请问你要存款多少元")
    print(f"{name},你好,您存款{input1}元成功")
elif progress==3:
    output1=input("请问你要取出多少钱?")
    output1=int(output1)
    if money-output1>=0:
        print(f"您的余额为{money},取出后还剩下{money-output1}")
    else:
        print("不好意思,您的余额不足")
elif progress==4:
    print("欢迎您下次光临")
"""
#optimizer
import random
money=random.randint(100000,40000000)
name=input("您好,请问你叫什么?")
def check(a):
    if a==True:
        print("---------余额查询-----------")
    print(f"您好,{name},您现在的余额为{money}")
def saving(num):
     print("---------存钱-----------")
     global money
     money+=num
     print(f"{name},您好,存钱成功")
     check(False)
def get_money(num):
    global money
    money-=num
    print("---------取钱-----------")
    print(f"{name},您好,取款成功")
    check(False)
def start():
    print("---------主界面-----------")
    print("欢迎来到黑马银行,请进行选择数字进行接下来的操作")
    print("查询余额\t【1】")
    print("存钱\t\t【2】")
    print("取钱\t\t【3】")
    print("返回\t\t【4】")
    return input("请输入您的选择")
while True:
    choose=start()
    if choose=="1":
        check(True)
        continue
    elif choose=="2":
        num=int(input("您好,请问您要存入多少钱?"))
        saving(num)
        continue
    elif choose=="3":
        num=int(input("你想要取多少钱?"))
        get_money(num)
        continue
    else:
        print("程序已结束")
        break





    
    

