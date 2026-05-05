thislist = ["risol", "geprek", "cendol"]
print(thislist)

print(len(thislist))

biodata = ["Arin", "18", True]
print(type(biodata))

mangan = list(("geprek", "cendol", "risol"))
print(mangan)
if "geprek" in mangan:
  print("Yes, 'geprek' is in the food list")

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist = [x for x in fruits if x != "apple"] #exclude apple

#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)