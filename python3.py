#lst = list()
lst = [1, 7, 9,'hello', True, 12,9,1,9]
print(lst)
print(lst[2])
print(lst[2:5])
print(lst[2:-1])
print(lst[::2])
print(lst[::-1])
#print(lst[10])

lst.append(15)
lst.insert(2,False)
print(lst)
lst.remove(12)
print(lst)
#lst.clear()
#print(lst)
#del lst
#print(lst)
lst_idx=lst.index('hello')
print(lst_idx)
#lst.pop=lst.pop()
#print(lst)
#print(lst_pop)
lst.pop=lst.pop(1)
print(lst)
print(lst_pop)
lst_cnt = lst.count(9)
print(lst_cnt)

lst=["a","add","hello","hel","acc"]
lst.sort()
print(lst)
lst.sort(key=len)
print(lst)

#lst=[15,12,10,7,90,1]
#lst.sort()
#print(lst)

lst.reverse()
print(lst)
sorted