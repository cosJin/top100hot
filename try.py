a = [2,5,7,9]
b = a
a = a.pop()
print(b)
print(333333)
a = [3]
b = a
a.append(3)
print(b)
d={"name":""}
l=[]
for i in range(5):
    d["name"]=i
    l.append(d)
l[3]['name'] = 9
print(l)