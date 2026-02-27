from tabulate import tabulate
from kurs import kurs
from konverter import konversi

def tampilkan_kurs():
    data = []
    for kode, nilai in kurs.items():
        data.append([kode, nilai])

    print("=== KONVERTER MATA UANG ===")
    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
    tampilkan_kurs()

    dari = input("Dari (IDR/USD/EUR/SGD/JPY): ")
    ke = input("Ke   (IDR/USD/EUR/SGD/JPY): ")
    jumlah = float(input("Jumlah: "))

    hasil = konversi(dari, ke, jumlah)

    if hasil is not None:
        print(f"\nHasil: {hasil:.2f} {ke.upper()}")
    else:
        print("Kode mata uang tidak valid.")

if __name__ == "__main__":
    main()