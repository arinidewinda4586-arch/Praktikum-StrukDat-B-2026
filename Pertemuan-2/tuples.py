mytuple = ("roti bakar", "sambel ijo", "cendol")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) #tuple gabisa diubah, jadi harus diconvert kelist dulu kalau mau ubah
