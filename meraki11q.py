my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
l=list(my_dict.values())
i=0
max1=0
max2=0
max3=0
while i<len(l):
    if l[i]>max1:
        max1=l[i]
    elif max1>l[i] and max2<l[i]:
        max2=l[i]
    elif max2>l[i] and max3<l[i]:
        max3=l[i]
    i+=1
print(max1)
print(max2)
print(max3)  
