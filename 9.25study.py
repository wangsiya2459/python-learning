current_list=[111,789,"hellow",True,[1,2,3]]
print(current_list)
#index=reseach
a=current_list.index(111)
print(a)

#insert=add
current_list.insert(2,666)
print(current_list)

# append=end_add
current_list.append("加油")
print(current_list)

# extend=more_end_add
my_list=[4,6,7,8,12]
current_list.extend(my_list)
print(current_list)

#delete
del my_list[4]
print(my_list)
element=current_list.pop(1)
print(element)
list_1=["你好呀","我很好",111,222,111,989]
list_1.remove(111)
print(list_1)
#list_1.clear()
#print(list_1)
count=list_1.count(989)
print(count)
count1=len(list_1)
print(count1)
list_2=[21,25,21,23,22,20]
list_2.append(31)
list_3=[29,33,30]
list_2.extend(list_3)
get1=list_2.pop(0)
get_num=list_2.index(30)
list_2.pop(get_num)
search=list_2.index(31)
print(list_2)
print(search)
While_list=[1,2,2,3,39]
a=0
while a<len(While_list):
    print(While_list[a])
    a+=1
b=0
for b in While_list:
    print(b)
list_3=[1,2,3,4,5,6,7,8,9,10]
list_4 = []
for i in list_3:
    if i%2==0:
        list_4.append(i)
print(f"通过for循环，从列表：{list_3}中，取出偶数，组成新列表为:{list_4}")
t=0
list_5=[]
while t<len(list_3):
    if list_3[t]%2==0:
        list_5.append(list_3[t])
    t+=1
print(f"通过while循环，从列表{list_3}中，取出偶数，组成的新列表：{list_5}")






