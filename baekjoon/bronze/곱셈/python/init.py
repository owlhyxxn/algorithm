A = int(input())
B = int(input())
for i in reversed(str(B)):
    print(A * int(i))
print(A * B)