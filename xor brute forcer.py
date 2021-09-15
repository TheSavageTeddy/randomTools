#taken from https://therokdaba.github.io/2021/08/02/RTL.html
import string
def hex_xor(hex_a, hex_b):
    return hex(int(hex_a, 16) ^ int(hex_b, 16))[2:]

def xor_solver(string, string_key):
    new_key = '' 
    decryption = ''

    # Repeat key in new_key for as long as hex_string is
    for i in range(0, round(len(string)/2), 1):
        new_key += hex(ord(string_key[i % len(string_key)]))[2:]

        # Perform xor on both hex
        xor_result = hex_xor(string, new_key)

    # Convert the hex to char
    for j in range(0, len(xor_result)-1, 2):
        decryption += chr(int(xor_result[j]+xor_result[j+1], 16))

    return decryption

value = '133f29027034094a33253126395b3704'#ciphertext
flags = []
posc="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"#0123456789" #possible chars the key can be
totamount=len(posc)**4 #total amount of keys
count=0
for i in posc:#4 byte key
    for j in posc:#3 byte key
        for k in posc:#2 byte key 
            for l in posc:#1 byte key 
                #print(f"Trying: {i}{j}{k}{l}", str(count/100000000*100) , "possible flags: "+str(flags))
                result = xor_solver(value, f"{i}{j}{k}{l}")
                if "RTL{" in result:#checks if flag format is in result
                    print(f"\n{result} is a possible flag!!!!\n")
                    flags.append(result + " with key" + f" {i}{j}{k}{l}")
                count+=1
                print(str(count/(totamount)*100))
print(flags)