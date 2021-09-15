import re
a=input('input: ')

regex = re.compile('[^a-zA-Z0-9_{}]')#also doesnt remove numbers and _ for sake of ctfs
#First parameter is the replacement, second parameter is your input string
print(regex.sub('', a))
