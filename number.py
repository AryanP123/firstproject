import sys
import array as arr
number = ""
def ascending():
    numberlist.sort()
    print (numberlist)
def descending():
    numberlist.sort(reverse=True)
    print (numberlist)
#initialize an array
numberlist = []
amount = input("How many numbers you want in your array: ")
if not amount.isdigit():
    print("%s  is not a digit" % amount)
    sys.exit(1)
amount = int(amount)
for i in range(amount):
    number = int(input("Type a number and hit enter: "))
    numberlist.append(number)
print (numberlist)
ascending()
descending()
