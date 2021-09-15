import hashlib
l="access attack barely better active chance create beauty follow escape"
l=l.split()


for i in l:
    str2hash = i
    result = hashlib.md5(str2hash.encode())
    print(result.hexdigest())