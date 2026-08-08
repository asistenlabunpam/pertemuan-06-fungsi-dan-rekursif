# Mekanisme Passing Reference vs Reassignment pada Python

def mutasi_list(listku):
    """Mengubah objek list yang dilewatkan (mutasi in-place)."""
    listku.append([5, 6, 7, 8])
    print("Nilai di dalam fungsi mutasi:", listku)
    return

def timpa_reference(listku):
    """Menimpa variabel lokal listku dengan referensi objek baru."""
    listku = [5, 6, 7, 8]
    print("Nilai di dalam fungsi timpa:", listku)
    return

if __name__ == "__main__":
    my_list1 = [50, 60, 70]
    print("--- Sebelum mutasi ---", my_list1)
    mutasi_list(my_list1)
    print("--- Setelah mutasi (di luar fungsi) ---", my_list1)

    print()
    my_list2 = [50, 60, 70]
    print("--- Sebelum timpa ---", my_list2)
    timpa_reference(my_list2)
    print("--- Setelah timpa (di luar fungsi) ---", my_list2)
