import friends
import getid
import datetime
import sys
import matplotlib.pyplot as plt
name=input()
#name='zhiznevsky'
today = datetime.datetime.today()
id =getid.GetId()
id=id.response_handler(id._get_data(name))
t=friends.friends()
t=t.response_handler(t._get_data(id))
a=[]
for i in t:
    if ('bdate' not in i):
        continue
    if (len(i['bdate']) > 5):
        # print(i)
        d = datetime.datetime.strptime(i['bdate'], "%d.%m.%Y")
        # t=datetime.timedelta(d.day)
        y = int((str((today - d) / 365)[0:2]))

        a.append(y)




plt.hist(
    a, # в зависимости от количества 1,2,3 строится гистограмма
   40 # а это как бы длина оси х
    )


#print(a)
b=[]
for karl in a:
    #if  karl in a:
        if karl not in b:
            b.append(karl)
#print(b)
b.sort()
#print(b)
for k1 in b:
    m1=0
    for r1 in a:
        if r1==k1:
            m1=m1+1
    sys.stdout.write(str(k1))
    sys.stdout.write(" ")
    for d1 in range(0,m1):
        sys.stdout.write("$")
    print(" ")


plt.show()