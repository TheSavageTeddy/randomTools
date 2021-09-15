c="315,324,363,294,294,363"
c=c.split(",")
cf=[]

for i in c: cf.append(int(i))

print(cf)
for i in range(0, 100):

    t=""
    for c in range(6):
        t+=chr(cf[c]-i)
    print(t)
#its actually /3 lol