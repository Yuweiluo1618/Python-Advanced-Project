list1 = [1,2,3]
list2 = list1[:]
print("list1", id(list1), "list2", id(list2))

list3 = [11, 22, 33]
t1 = (list1, list3)
t2 = t1[:]
print("t1", id(t1), "t2", id(t2))

dict1 = {"a":[1,2]}
dict2 = dict1.copy()
print('dict1', id(dict1), 'dict2', id(dict2))
print('dict1[a]', id(dict1['a']), 'dict2[a]', id(dict2['a']))