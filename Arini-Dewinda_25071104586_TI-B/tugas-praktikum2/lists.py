#python list -akses item
lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
print(lunch)

lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
print(lunch[2]) #akses indeks ke-2, berarti outputnya naspad

lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
print(lunch[-1]) #indeks negatif berarti dimulai dari belakang, jadi outputnya seblak

lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
print(lunch[1:3]) #akses dimulai dari indeks 1 sampai 3, tapi indekss ke 3 ga termasuk

"""
note : perlu diingat bahwa indeks selalu dimulai dari 0
"""
#ubah value
lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
lunch[3] = "ayam penyet" #indeks ke-3 ayamm geprek akan diganti jadi ayam penyet
print(lunch)

lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
lunch[1:3] = ["batagor", "sushi"] #kalau mau ubah value dengan range
print(lunch) 

lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
lunch.insert(1, "cilok") #nambah value ke indeks tertentu 
print(lunch)

#nambah item
lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
lunch.append("cibay") #item baru bakal ditambah ke akhir list
print(lunch)

lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
lunch.insert(1, "cilok") #nambah item ke indeks tertentu 
print(lunch)

#gabungin list (extend)
lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
dinner = ["bakso", "mie ayam", "patty bun"]
lunch.extend(dinner) #gabungin list lunch dan dinner jadi satu list
print(lunch)

#hapus item
lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
lunch.remove("gacoan") #item yang ditunjuk akan dihapus dari list
print(lunch)

lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
lunch.pop(1) #gehapus pakai rujukan indeks, kalau nomor indeks ga ditulis last item yg bkl khps
print(lunch)

lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
 del lunch[2] #mirip mirip lah sm pop(), bisa jga buat hapus seluruh list
print(lunch)

#loop list
lunch = ["ayam geprek", "gacoan", "naspad", "ayam geprek", "seblak"]
for x in lunch :
    print(lunch)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#urutin list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #berdasarkan alpabet

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) #berdasarkan numerik

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True) #ini kalau mau urutannya dibalik (descending)
print(thislist)

#salin list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)