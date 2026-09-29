import sys
print(sys.platform)
print(2**100)
x='Hack!'
print(x*8)
new_set={"itheima","friend","kid","itheima","come"}
print(f"new_set include{new_set},its type is {type(new_set)}")
new_set.add("woderful")
new_set.add("amazing")
new_set.remove("itheima")
print(f"new_set is change,you can get{new_set}")
element=new_set.pop()
print(f"Randomly sampling one element from Set1,this element is {element}")
new_set.clear()
print(f"Through clearing all new_set,we can get a {new_set}")
set1={1,4,5,6,9}
set2={1,9,8,3}
set3=set1.difference(set2)
print(f"if we construct set3 from set1 that are not present set2,set3 include{set3} ")
set1.difference_update(set2)
print(f"if we delete set1's some element that set2 have benn include,we can get new set1{set1}")
set4=set1.union(set2)
print(f"If we combine set1 and set2,we could get a new set4{set4}")
number=len(set4)
print(f"set4 have {number} element")
x=0
for x in set4:
    print(x)
#test
my_list=['name','age','sex','number''name','diffusion','evolutionary']
set77=set()
for y in my_list:
    print(y)
    set77.add(y)
print(set77)
dir1={"aima":88,"cici":99,"mark":77}
dir2={}
dir3=dir()
message=dir1["aima"]
print(message)
dir4={"mike":{
    "Chinese":120,
    "math":144,
    "English":133
},"gena":{
    "Chinese":105,
    "math":144,
    "English":149
}}
score=dir4["mike"]["math"]
print(f"mike's score is {score}")
dir1["aima"]=99
dir1["gegewu"]=100
number=dir1.pop("cici")
print(f"Dir1 become {dir1}")
dir1.clear()
print(dir1)
keys=dir1.keys()
print(f"keys={keys}")
dir8={"aimal":88,"cici":99,"mark":77}
for key in dir8:
    print(f"在字典dir1中的key是{key}")
    print(f"在字典dir1中的value是{dir8[key]}")
message={"王力宏":{"部门":"科技部","工资":3000,"级别":1},
         "周杰伦":{"部门":"市场部","工资":5000,"级别":1,
        "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
         "张学友":{"部门":"科技部","工资":4000,"级别":1},
          "刘德华":{"部门":"市场部","工资":6000,"级别":2}}}
print(f"在还没有修改之前，message为{message}")
for key in message:
    if message[key]["级别"]==1:
        message[key]["工资"]=message[key]["工资"]+1000
        message[key]["级别"]=message[key]["级别"]+1

        print(f"增加工资后，message变成{message}")

