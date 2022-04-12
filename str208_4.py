max1=0
with open("text1.txt") as f:
    s=f.readlines()
    s=[c.rstrip() for c in s]
    for c in s:
            s.sort()
            max1=max(len(c),max1)


for i in range(1,max1+1):
    for c in s:
        if len(c)==i:
            print(c)


                #out.append(c)
#for i in out:
   # print(i)