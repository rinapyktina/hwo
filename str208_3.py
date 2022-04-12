max1=0
out=[]
with open("text1.txt") as f:
    s=f.readlines()
    s=[c.rstrip() for c in s]
    for c in s:
            s.sort()
            max1=max(len(c),max1)
    for c in s:
            if len(c)==max1:
                out.append(c)
for i in out:
    print(i)




