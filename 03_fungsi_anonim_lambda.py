# Penggunaan Lambda Function (Fungsi Anonim)

# Lambda satu argumen
double = lambda x: x * 2

# Lambda dua argumen
perkalian = lambda a, b: a * b
jumlah = lambda arg1, arg2: arg1 + arg2

if __name__ == "__main__":
    print("double(5) =", double(5))
    print("perkalian(5, 6) =", perkalian(5, 6))
    print("jumlah(5, 10) =", jumlah(5, 10))
    print("jumlah(15, 22) =", jumlah(15, 22))

    # Penggunaan lambda bersama map() dan filter()
    angka = [1, 2, 3, 4, 5, 6]
    genap = list(filter(lambda x: x % 2 == 0, angka))
    kuadrat = list(map(lambda x: x ** 2, angka))
    
    print("Filter angka genap:", genap)
    print("Map angka kuadrat:", kuadrat)
