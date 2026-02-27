thisset = {"apple", "banana", "cherry", False, True, 0} #false dan 0 dianggap sama, jadi cuma print false

print(thisset) 

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) #cek banana ada di set atau ga

#add item
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#remove item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)