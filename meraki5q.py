list1=["one","two","three","four","five"]
list2=[1,2,3,4,5]
list={}
for key in list1:
    for value in list2:
        list[key]=value
        list2.remove(value)
        break
print(list)
        