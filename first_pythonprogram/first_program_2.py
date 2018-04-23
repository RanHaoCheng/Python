# coding=UTF-8
filename = raw_input('filename: ')

f = open(filename , 'r')
b_str = f.read()
f.close

print b_str.decode('utf-8')
print b_str.decode('utf-8').encode('utf-8')
