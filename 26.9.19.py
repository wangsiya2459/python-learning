# 我将认真学习黑马程序员的python视频
"""
今天是第一天日期为2026年9月14日,今天学习内容为变量和数据类型
变量相当于一个盒子来储存数据用的,特点是可变

加油
"""

# 变量 变量名=变量值
money =50
print("当前钱包余额为： ",money)
money =money - 5
print("购买冰淇淋花费了： ",5)
print("当前钱包余额为： ",money)
print("购买了可乐花费: ",10)
money =money -10
print("当前钱包余额为： ",money)

# 数据类型：整型、浮点型、字符型
# 1.type(变量)就可以输出类型
# 2.变量没有类型
print(type(100),type(1.55),type("你好"))
int_type=type(100)
print(int_type)
str_type=type("我喜欢你")
print(str_type)
float_type=type(5.20)
print(float_type)
apple=100
apple_type=type(apple)
print(apple_type)
#中午2个小时学习结束，晚上我将从数据类型转换开始！！！

#晚上开始了(数字和浮点型是可以转换成字符串的，但是字符串如果想要转化成数字，则要求该字符串里面全部都是数字类型)
#数字类型转换成浮点型
num_str=str(100)
print(type(num_str),num_str)
float_str=str(56.22)
print(type(float_str),float_str)
#字符串类型转化成数字类型
str_int=int("99")
print(type(str_int),str_int)
str_float=float("3.121")
print(type(str_float),str_float)
#整数转浮点数
num_float=float(88)
print(type(num_float),num_float)
#浮点数转整数（可以转成功，但是会丢失精度）
num2=int(3.1415926)
print(type(num2),num2)
#标识符：我们给变量、方法等一些东西所起的名字叫标识符
#1.内容限定：只能存在中文、英文、数字、和下划线_（开头不可以是数字）
#2.大小写敏感，可以精准区分大小写
#3.不可以使用关键字eg：and class .ect
#变量的命名规范：1.清晰明了2.英文字母全小写3.写英文时用下划线把单词分开

#运算符
#1算数运算符

print("1+1=",1+1)
print("5-2=",5-2)
print("3*2=",3*2)
print("4/2=",4/2)
print("6//2=",6//2)
print("4%3=",4%3)
print("2**2=",2**2)
#赋值运算符
num=5
num+=1
print("num+=1=",num)
num-=2
print("num-=1=",num)
num*=2
print("num*=2=",num)
num/=2
print("num/=2=",num)
num//=3
print("num//=3=",num)
num%=1
print("num%=1=",num)
#字符串的三种定义法
name ='黑马程序员'
print(type(name))
name2="""你好哈哈哈哈"""
print(type(name2))
name3='"hhhhh"'
print(name3)
name4="'mmmm'"
print(name4)
name5="\"hhhh"
print(name5)
#字符串的拼接
print("今天军训好累" +"我好想休息")
name="王思雅"
address="江西财经大学"
tel=15222222
print("我的名字叫" +name,",我的大学叫" +address,"我的电话是")#拼接只能适用于字符串本身，其他类型的不可以和字符串一起拼接
print(11111+tel)
#字符串的格式化
age=18
height=168
a="我的年龄是%d,我的身高为%s" %  (age,height)
print(a)#常用占位符有三种分别为%s:表示将变量变成字符串；%d:表示吧变量变成整型；%f:表示把变量变成浮点型
#字符串格式化精度控制
num1=15.56
num2=66.6666
print("数字15.56设置宽度4,精度为1的数字为:%4.1f"% num1)#%m.n去生效，其中m为宽度，n为精度，当m小于数字本身宽度时，则不生效，且.n会对小数进行四舍五入
print("设置数字66.666的宽度为7,精度为2的数字为%7.2f" % num2)
#字符串快速格式化
name="周佳宇"
age=18
print(f"我的朋友叫{name},她的年龄是{age}")
#对表达式进行格式化
print(f"1+8={1+8}")
print(f"字符串的类型是{type('222')}")
print("1*1=%d" %(1*1))
#练习
name="数智公司"
stock_price=14
stock_code="0041"
stock_price_daily_growth_factor=2.6
growth_days=5
print(f"公司{name},股票代码{stock_code},当前股价：{stock_price}")
print("每日的增长系数是%s,经过%d天,股价达到了:%.2f" %(stock_price_daily_growth_factor,growth_days,(14*2.6**5)))
#input语句
name=input("请告诉我你是谁？")
print(f"我知道了,你是{name}")#input获取到的类型都是字符串
#练习
user_name=input("你的用户名是什么？")
user_type=input("请问你今天坚持学习了吗?")
print(f"你好：{user_name},我知道你一定是最棒的对吗?{user_type}!!!继续加油呀")
#布尔类型bool
age=18
print(f"你是00后吗,我说{age==18},回答正确！！！")
number1=45
number2=33
print(f"45!=33的结果是:{number1!=number2}")
name1="asdfg"
name2="zxcvb"
print(f"name1和name2相等吗?答案是：{name1==name2}")
date1=45
date2=6
print(f"date>=date2的结果是:{date1>=date2}")
new=5>4
print(f"5>4的结果是:{new}")
#if语句的基本格式和使用
"""
age=19
if age >=18:#判断语句if后面的结果一定要是布尔类型
    print("恭喜你,成年了")
else:
    print("未成年人不准入内")
current_age=input("请问你多少岁了？")
if int(current_age)>=18:
    print("欢迎进入")
else:
    print("禁止入内")
print("欢迎来到黑马儿童游乐场,儿童免费,成人收费")
now_age=input("请问你的年龄是？")
if int(now_age)>=18:
    print("你已经成年,请补票")
else:
    print("玩的愉快,小朋友")
print("欢迎来到黑马动物园!!!")
height=input("请输入你的身高__cm")
if int(height)>=120:
    print("您的身高超出120cm,请购票")
else:
    print("祝您游玩愉快！！！")

print("欢迎来到黑马动物园！！！")
height=input("你的身高是多少?(cm)")
vip_leve=input("您的会员级别是多少?")
if int(height)<=120:
    print("你的身高低于120c,欢迎免费进入")
elif int(vip_leve)>=3:
    print("欢迎入内")
else:
    print("请额外补钱")
number=5
number1=input("猜想一个数字")
if int(number1)==number:
    print("恭喜你,第一次就猜对了")
elif int(input("猜错了，再次猜想一个数字"))==number:
    print("猜对了,真棒!")
else:
    print(f"最终数字为{number},又猜错了")

print("欢迎来到黑马动物园")
if int(input("你的身高是多少？"))>=120:
    print("不好意思,你的身高大于120cm,不可以免费进入")
    print("如果你的会员级别达到了3以上那可以免费进入")
    if int(input("您的会员级别是多少?"))>=4:
        print("欢迎你的进入")
    else:
        print("请补票10元")
else:
    print("欢迎进入,小朋友")

print("公司要发礼物啦!!!")
if 18<=int(input("你的年龄是多少？"))<30:
    print("恭喜你,年龄条件符合!!!")
    if int(input("你的入职时间是多久???"))>2:
        print("恭喜你,可以领取奖品!!!")
    elif int(input("不好意思,那么请问你的级别是多少呢?"))>3:
        print("恭喜你,可以领取到奖品!!!")
else:
    print("不好意思,你的年龄没达到要求,不可以领取奖品")
"""
import random
num = random.randint(1,10)
guss_num=input("1到10,猜测一个数字吧")
if int(guss_num)==num:
    print("恭喜你,猜中了！！！")
else:
    if int(input("不对，再输入一次吧"))>num:
        print("不好意思,你的数字猜大了")
    else:
        print("不好意思,你的数字猜小了")
guss_num=input("不对，再猜一个数字吧")
if int(guss_num)==random:
    print("恭喜猜中了")
else:
    if int(guss_num)<num:
        print("猜小了")
    else:
        print("猜大了")
guss_num=input("不对，再猜一次")
if int(guss_num)==num:
    print("恭喜你,猜中啦")
else:
    print("你运气也太差了,回家种田吧")
#今天是2026年，9月20日，11点07分，今日python结束，明天将开始学习while
    