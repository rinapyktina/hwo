a = "bcdfghjklmnpqrstvwxzабвджзйклмнпрстфхцчшщ"
st = input().split()
k = 1
for i in st :
    ii = i.lower()
    for j in range(1, len(i)) :
        if ii[j] == ii[j - 1] and ii[j] in a :
            print(i,ii[j-1],ii[j])
            k = 0
if k :
    print('удвоенных согласных нет')