#第六题：s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
s=set(s)
s=list(s)
s.sort(reverse=False)
res="".join(s)
print(res)