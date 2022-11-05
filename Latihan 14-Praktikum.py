#Adrian Alfajri - 064002200009

print("Ordinal Number")
print("Ketik 0 untuk menghentikan program")

def ordinalnumber(a):
    a == angka
    if a % 10 == 1:
        return a, "st"
    elif a % 10 == 2:
        return a, "nd"
    elif a % 10 == 3:
        return a, "rd"
    elif a % 10 in range(4,21):
        return a, "th"
    elif a % 10 == 0:
        return a, "th"
    else:
        return ordinalnumber(a)
    
    
angka = ""
while angka != 0:
    angka = int(input("Masukkan Angka : "))
    print(ordinalnumber(angka))
    
print("Terimakasih telah menggunakan program ini.")