# --coding:utf-8--
print("Enter the number of blocks")
n = int(input())
print("Enter the number of blocks for 1 tower")
k = int(input())
t = n // k  # Maximum number of towers
b = t * k  # Number of blocks
print(f"From {n} blocks, you can build a maximum of {t} towers")
print(f"This will take {b} blocks.")
