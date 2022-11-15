n = int(input("Размер массива: "))
list = [0]*n
for j in range(n):
    list[j] = int(input("Эллменет массива: "))
print(min(list))