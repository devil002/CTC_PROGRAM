num = int(input())
temp = []
even = [int(i) for i in range(2,(num*2)+2) if i % 2 == 0]
for i in range(0,num):
    foo = (6*(i+1)**2)+i*even[i]
    temp.append(foo)
# print(*even)
print(*temp)

