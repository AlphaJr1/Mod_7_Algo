def bil_prima(x = 0):
    x = int(input("Masukkan Bilangan : "))
    if x > 1:
        for i in range(2 , x):
            if (x % i) == 0:
                print(x, "bukan bilangan prima")
                break
            else:
                print(x, "adalah bilangan prima")
                break
    else:
        print(x, "bukan bilangan prima")
        
prims = bil_prima()
print(prims)