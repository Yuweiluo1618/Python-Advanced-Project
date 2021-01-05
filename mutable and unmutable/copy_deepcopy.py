import copy
def test1():
    list1=[1,3]
    list2 = copy.copy(list1)
    list3 = copy.deepcopy(list1)
    print("list1=", list1, id(list1))
    print("list2=", list2, id(list2))
    print("list2=", list3, id(list3))

def test2():
    list1 = [1,2,3]
    list2 = [11,22,33]
    list3 = [list1, list2]
    list4 = copy.copy(list3)
    print("list3", id(list3), "list4", id(list4))
    print("list3[0]", id(list3[0]), "list4[0]", id(list4[0]))
    list5 =copy.deepcopy(list3)
    print("list3", id(list3), "list5", id(list5))
    print("list3[0]", id(list3[0]), "list5[0]", id(list5[0]))

def test3():
    t1 = (1,2,3)
    t2 = copy.copy(t1)
    print("t1",id(t1),"t2",id(t2))

    t3 = copy.deepcopy(t1)
    print("t1",id(t1),"t3",id(t3))

def test4():
    list1 = [1,2,3]
    list2 = [11,22,33]
    t1 = (list1, list2)
    t2 = copy.copy(t1)
    print("t1",id(t1),'t2',id(t2))

    t3 = copy.deepcopy(t1)
    print("t1", id(t1), 't3', id(t3))
    print("t1[0]",id(t1[0]),'t3[0]',id(t3[0]))
test4()