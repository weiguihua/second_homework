#第八题：字典根据键从小到大排序
dict1={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
list1=sorted(dict1.items(),key=lambda i:i[0],reverse=False)
a=dict(list1)
print(a)