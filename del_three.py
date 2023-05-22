#第三题：删除键，合并两个字典
dict={'name':'Tim','height':187,'age':18}
dict1={'name':'Ani','weight':45,'score':90}
#删除dict中的name
del dict['name']
print(dict)
#合并两个字典
dict.update(dict1)
print(dict)