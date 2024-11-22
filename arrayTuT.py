# approach 1
# n = int(input("Enter a no: "))
# l = [int(input("Enter list member: ")) for x in range(n)]
# print(l)

# approach 2
# n = int(input("Enter a no: "))
# l = []
# for i in range(n):
#     l.append(int(input("Enter list member: ")))
# print(l)

# approach 3
l = list(map(int,input("Enter list member : ").split()))
print(l)