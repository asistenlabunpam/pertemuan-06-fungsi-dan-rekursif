# Fungsi Rekursif: Faktorial dan Fibonacci

def fib(n):
    """Menghitung nilai Fibonacci ke-n secara rekursif."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def faktorial(n):
    """Menghitung nilai faktorial n! secara rekursif."""
    if n < 0:
        return "Angka tidak boleh negatif"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

if __name__ == "__main__":
    print("=== Deret Fibonacci Rekursif ===")
    n_fib = 7
    print(f"Fibonacci ke-{n_fib} = {fib(n_fib)}")
    print("Deret Fibonacci hingga 7:", [fib(i) for i in range(n_fib + 1)])

    print("\n=== Faktorial Rekursif ===")
    n_fact = 5
    print(f"{n_fact}! = {faktorial(n_fact)}")
