
ism = input("Ism kiriting: ")

letters = []

for i in ism:
    letters.append(i)
    
print("Natija: ",letters)



# foydalanuvchi kiritgan takrorlanuchi va o'xshash harflarni 'chirib tashlovchi code



lst = [1,2,2,3,3,4,4,5,5,]

new_list = []

for i in lst:
    if i in new_list == False:
        new_list.append(i)
print("Natija: ",new_list)