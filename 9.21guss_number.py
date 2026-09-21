import random
num = random.randint(1,100)
flag= True
i=0
while flag:
    guess_num=int(input("1到100,随机猜一个数字吧"))
    if guess_num==num:
        i+=1
        print(f"恭喜你猜对了!!!,第{i}次下,你终于猜中了")
        flag=False
    else:
        if guess_num>num:
            print("不好意思,你猜大了")
            i+=1
            flag=True
        elif guess_num<num:
            print("不好意思，你猜小了")
            i+=1
            flag=True
            

