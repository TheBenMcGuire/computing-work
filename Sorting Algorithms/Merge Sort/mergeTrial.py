import random as r

numbers = []

for i in range(1,65):
    numbers.append(i)

r.shuffle(numbers)

print(numbers)

print()

for i in range(6):
    
    for j in range(0,64,2**(i+1)):

        numbCheck = numbers
        sort1 = []
        sort2 = []
        
        k = j
        
        while k < j+(2**i):
            sort1.append(numbers[k])
            k += 1
            
        while k < j+(2**(i+1)):
            sort2.append(numbers[k])
            k += 1
            

        sortedList = []
        
        while sort1 and sort2:
            
            if sort1[0] > sort2[0]:
                sortedList.append(sort2[0])
                sort2.remove(sort2[0])

            else:
                sortedList.append(sort1[0])
                sort1.remove(sort1[0])

        for item in sort1:
            sortedList.append(item)
        for item in sort2:
            sortedList.append(item)
            
        l = 0
        
        for item in sortedList:
            numbers[j+l] = item
            l+=1

        for item in numbers:
            print(item, end=',')
        print()

        
