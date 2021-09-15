#possible flag chars
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]\\;',./<>?:\"{}|`~"
#the ciphertext
ct=""
#generating dictionary
d={}
for i in alphabet:
    d[encrypt(i)]=i

#solve
flag=""
for i in ct:
    flag+=d[i]
print(flag)