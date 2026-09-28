new=(1,"黑马程序员","你好",49)
print(f"元组new,它的内容是{new},它的类型是{type(new)}")
new=(1,"黑马程序员","你好",49,49,"黑马程序员","黑马程序员")
num=new.count("黑马程序员")
print(f"在元组new中，黑马程序员一共出现了{num}次")
num=len(new)
print(f"new元组一共包含{num},个元素")
num=new.index("黑马程序员")
print(f"new元组中，第一个黑马程序员元素的位置是{num}")
new=(1,"黑马程序员","你好",49,49,"黑马程序员","黑马程序员",(55,49))
num=new[7][0]
print(f"new[6][0]的元素是{num}")

#for
for x in new:
    print(x)

#while
a=0
while a<len(new):
    print(f"{new[a]}")
    a+=1
message=('周杰伦',11,['football','music'])
age=message.index(11)
print(f"该学生的年龄下标为{age}")
print(f"该学生的姓名为{message[0]}")
del message[2][0]
message[2].append('coding')
print(f"更改之后，message元组内容变成了{message}")