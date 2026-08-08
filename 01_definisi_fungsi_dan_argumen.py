# Definisi Fungsi dan Jenis Argumen di Python

# 1. Fungsi Sederhana dan Positional Argument
def printme(str_input):
    """Mencetak sebuah string ke layar standar."""
    print("Output printme:", str_input)
    return

# 2. Keyword Argument & Default Argument
def printinfo(nama, umur=25):
    """Mencetak nama dan umur dengan default argument pada umur."""
    print("Nama:", nama)
    print("Umur:", umur)
    return

# 3. Variable-Length Arguments (*args)
def print_variabel(arg1, *vartuple):
    """Menerima jumlah argumen variabel yang tidak terbatas."""
    print("Argumen pertama:", arg1)
    print("Argumen tambahan:")
    for var in vartuple:
        print(" -", var)
    return

if __name__ == "__main__":
    printme("Ini panggilan pertama untuk fungsi user defined!")
    printme("Memanggil kembali untuk fungsi yang sama")

    print("\n--- Keyword & Default Arguments ---")
    printinfo(umur=20, nama="Emi")
    printinfo(nama="Emi")

    print("\n--- Variable-Length Arguments ---")
    print_variabel(20)
    print_variabel(90, 80, 70)
