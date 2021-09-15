import string
c=input("Input ciphertext: ")
#c=""
#use above for weird unicode chars etc
l=input("How long is each char? ")
if l == "":
    l=1
alpha=[]
for i in c:
    if not i in alpha:
        alpha.append(i)
print("Cipher Alphabet: ", alpha)
print("Alphabet length: ", len(alpha))
alphabet=string.ascii_lowercase+string.ascii_uppercase
repc=""
repcl=[]
for i in c:
    repc+=alphabet[alpha.index(i)]
    repcl.append(alphabet[alpha.index(i)])

print("Replaced with alphabet: ", repc)
print("Replaced most frequent with space: ", repc.replace(max(repcl, key= repcl.count), " "))