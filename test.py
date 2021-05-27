lenght = input()
num = [int(x) for x in input().split(" ") if x != ""]
if int(lenght) == len(num):
    val = input()
    num = [int(x) for x in num if x == int(val)]
print(*num)
