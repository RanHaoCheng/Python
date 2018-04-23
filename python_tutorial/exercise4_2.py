# Using for comprehension to find out a right triangle
# which r+a+b = 24
# 0 > r, a, b <= 10
# r**2 = a**2 + b**2
import sys

cnt = range(1,11)

print [[a,b,r] for a in cnt for b in cnt for r in cnt if (r**2 == a**2 + b**2) if (r+a+b==24) ]

for i in cnt:
    for j in cnt:
        for k in cnt:
            if (i**2 + j**2 == k **2):
                if (i+j+k == 24):
                    print i , j , k
                    sys.exit()

