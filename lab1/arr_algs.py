a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
x = min (a)
print (x)
def avg(mass):
    s=0
    z= len(mass)
    l = 0
    while l<z:
        s=s+mass[l]
        l+=1
    y = s/z
    print (y)
avg(a)


