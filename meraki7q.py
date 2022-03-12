l=[
  {"first":1}, 
  {"second": 2}, 
  {"third": 1}, 
  {"four": 5}, 
  {"five":5}, 
  {"six":9},
  {"seven":7}
]
p=[]
for i in range(len(l)):
    for j in l[i]:
        p.append(l[i][j])
a=[]
i=0
for i in range(len(p)):
    if p[i] not in a:
        a.append(p[i])
    i=i+1
print(a)  
