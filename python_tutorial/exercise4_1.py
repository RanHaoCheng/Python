#numbers = []
#for number in range(20):
#    numbers.append(str(number))
#print ", ".join(numbers)

numbers = []
[numbers.append(str(number)) for number in range(20)]
print ", ".join(numbers)
