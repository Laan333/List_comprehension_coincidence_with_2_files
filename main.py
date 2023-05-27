with open("file1.txt", mode="r") as file:
    a = file.readlines()
with open("file2.txt",mode="r")as data:
    b = data.readlines()

# comp = []

# for i in my_first_list_int:
#     if i in my_second_list_int:
#         comp.append(i)

comp = [int(i) for i in a if i in b]

print(comp)