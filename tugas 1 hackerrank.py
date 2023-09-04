pemain_a, pemain_b = input().split()

if pemain_a == pemain_b:
    hasil = "Draw"
elif (pemain_a == "[]" and pemain_b == "8<") or (pemain_a == "[]" and pemain_b == "()") or (pemain_a == "8<" and pemain_b == "()"):
    hasil = "Pemain B menang"
else:
    hasil = "Pemain A menang"

print(hasil)

