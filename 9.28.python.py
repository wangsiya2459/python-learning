#string can not change,just add new string or list
current_string=("  itheima and itcast  ")
new_string=current_string.replace("it","hhh")
print(f"将current_string字符串{current_string}替换一些内容变成{new_string}")
new_string_list=current_string.split(" ")
print(f"将字符串{current_string}切分变成新列表{new_string_list},它的类型属于{type(new_string_list)}")
new_string=current_string.strip()
print(f"将字符串{current_string}通过strip的方式去掉前后空格变成新的字符串{new_string}")
current_string1=("12itheima and itcast21")
new_string=current_string.strip("12")
print(f"将new_string1字符串{current_string1},去除12，变成新的字符串{new_string}")
current_string=("itheima and itcast")
new_string=current_string.strip("it")
print(f"把字符串current_string{current_string},去除字母t,变成一个新的字符串{new_string}")
current_string=("  itheima and itcast  ")
number=current_string.count("t")
print(f"在字符串current_string中一共有{number}个t")
test_string="itheima itcast boxuegu"
number=test_string.count("it")
print(f"字符串{test_string}有:{number}个it字符")
new_test_string=test_string.replace(" ","|")
print(f"字符串{test_string}, 被替换空格后，结果是：{new_test_string}")
new_test_string1=new_test_string.split("|")
print(f"字符串{new_test_string},按照|分隔后，得到{new_test_string1}")
homework_string="学python，来黑马程序员，月薪过万"
purple=homework_string[::-1]
print(purple)
first_step=purple[9:4:-1]
print(first_step)