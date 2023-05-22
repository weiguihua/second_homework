#第四题：列表去重
list1=[1,2,3,4,2,3,45,23,12]
a=set(list1)
list1=[x for x in a]
print(list1)