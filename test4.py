n = int(input())
num = [int(i) for i in input().split(" ") if i != ""]
counter = 0
temp = []
odd = []
if n == int((len(num)+1)):
    for i in num:
        if i not in temp:
            # print("Entered and looping "+str(i))
            temp.append(i)
            for j in range(len(num)):
                if i == num[j]:
                    counter += 1
            if counter % 2!= 0:
                odd.append(i)
            counter = 0
# print(*temp)
print(*odd)
