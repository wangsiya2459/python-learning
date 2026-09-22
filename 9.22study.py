number=822
count=0
for x in range(1,number):
    if x%2==0:
        count+=1
print(f"1到{number}之间,一共有{count}个偶数")

for i in range(4):
    print(i)
print(i)
j=1
for j in range(1,101):
    print(f"这是我向小美表白的第{j}天")
    for n in range(1,11):
        print(f"这是我送的第{n}朵玫瑰花")
    print("小美,我喜欢你")
print(f"表白第{j}天,我终于成功了")
#combine for and while
c=1
for c in range(1,101):
    print(f"今天是我向小美表白的第{c}天")
    d=1
    while d<=10:
        print(f"这是我送给小美的第{d}朵玫瑰花")
        d+=1
    print("小美,我喜欢你")
print(f"表白第{c}天,我终于成功了!!!")
#anthor mean
v=1
while v<=100:
    print(f"这是我向小美表白的第{v}天")
    for l in range(1,11):
        print(f"这是我送给小美的第{l}朵玫瑰花")
    v+=1
    print("小美,我喜欢你!!!")
print(f"表白第{v-1}天,我终于成功了!!!")
#print 9*9
f=1
m=1
for f in range(1,10):
    for m in range(1,f+1):
        print(f"{m}*{f}={f*m}  ",end="")
    print()
#continue and break
k=1
for k in range(1,4):
    print("111")
    break
    print("666")
    print(888)
print(444)
h=1
for h in range(1,4):
    print("哈哈哈")
    for g in range(1,5):
        print("你好")
        break
        print(111)
    print("yeyeye")
print("666")
#receive salary
import random
kpi=random.randint(1,10)
total=10000
for people in range(1,21):
    if total>=1000:
        if kpi<=5:
            print(f"员工{people},绩效{kpi},绩效小于5,不发工资")
        elif kpi>5:
            print(f"员工{people},绩效合格,发放1000元")
            total-=1000
    else:
        print("钱不够了,下个月再说吧")

