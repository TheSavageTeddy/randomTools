def xor_two_str(a,b):
    xored = []
    for i in range(max(len(a), len(b))):
        xored_value = ord(a[i%len(a)]) ^ ord(b[i%len(b)])
        xored.append(hex(xored_value)[2:])
    return ''.join(xored)
    
print(xor_two_str("Rick", "2506110631060d103c5a15582036045b3c075734640015580d10531e0d1c134a2f"))