import random

jumlah = int(input("Masukan Jumlah n : "))
a = 0

for i in range(jumlah):
    a +=1
    b = random.uniform(.0,.5)
    print('data ke :',a,'==>',b)
print("******SELESAI*********")