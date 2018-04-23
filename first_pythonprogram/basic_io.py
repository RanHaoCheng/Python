import sys
file = open(sys.argv[1],'w')
file.write('test')
file.close()

file2 = open(sys.argv[2],'r')
while True:
    line = file2.readline()
    if not line:
        break
    print line

file2.close()
