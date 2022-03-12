my_dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
a={}
max1=0
max2=0
max3=0
for i in my_dict:
    if my_dict[i]>max1:
        max1=my_dict[i]
        max_key=i
    elif max1>my_dict[i] and max2>my_dict[i]:
        max2=my_dict[i]
        max2_key=i
    elif max2>my_dict[i] and max3>my_dict[i]:
        max3=my_dict[i]
        max3_key=i
print(max1)
print(max2)
print(max3)



