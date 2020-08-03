#this is a tool to generate either completely random strings with alphabetical characters in them, or
#for people who cant think of a name for something and want inspiration! (me)
#                           - TheSavageTeddy


import random

length=input(
'''
range of length of string: 
(5 7 for 5 to 7)
''')
length=length.split()
option=input('''
(1) completely random
(2) readable/sayable words
''')

amount=int(input("amount to generate: "))
#consenents
c=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
#vowels
v=['a','e','i','o','u']
#alphabet
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#consenent sounds
cs=['p','b','t','d','c','ck','g','f','v','th','s','z','sh','ch','ng','ll','tt']
if option == '1':
    for i in range(0, amount):
        string=""
        for i in range(0, random.randint(int(length[0]), int(length[1]))):
            string=string+random.choice(alphabet)
        print(string)
elif option == '2':
    for i in range(0, amount):
        string=""
        o=random.randint(0,1)
        rand= random.randint(int(length[0]),int(length[1]))
        while len(string)<rand:
            if o == 0:
                string=string+random.choice(v)
                o=1
            elif o == 1:
                if random.randint(0,2) == 2 and not len(string)+2 > rand:
                    string=string+random.choice(cs)
                else:
                    string=string+random.choice(c)
                o=0

        print(string)
            
        
    