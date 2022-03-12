s="MISSISSIPPI"
d=list(s)
i=0
l={}
while i<len(d):
    c=0
    j=0
    while j<len(d):
        if d[i]==d[j]:
            c+=1
        j+=1
    l.update({d[i]:c})
    i+=1
print(l)
 #    (or)
a="mississippi"
b=list(a)
c={}
for i in a:
	if i in c:
		c[i]+=1
	else:
		c[i]=1
print(c)