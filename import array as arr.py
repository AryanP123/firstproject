def sort1(numberlist):
    for i in range(len(numberlist)-1):
        if numberlist[i] > numberlist[i + 1]:
            temp = numberlist[i]
            numberlist[i]=numberlist[i+1]
            numberlist[i+1]= temp
            i = 0
    return numberlist  


def sort2(numberlist):
    for _ in range(len(numberlist)):
        for i in range(len(numberlist)-1):
            if numberlist[i] > numberlist[i+1]:
                temp = numberlist[i]
                numberlist[i]=numberlist[i+1]
                numberlist[i+1]= temp
    return numberlist  
               



n=[10,9,4,6,7,8,9,7,8]

s=sort1(n)
print(s)
s=sort2(n)
print(s)