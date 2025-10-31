import itertools

# --- Fungsi Permutasi ---
def permutasi_sebagian(arr, k):
    return list(itertools.permutations(arr, k))

def permutasi_menyeluruh(arr):
    return list(itertools.permutations(arr))

def permutasi_keliling(arr):
    if len(arr) == 1:
        return [arr]
    pertama = arr[0]
    permutasi_penuh = list(itertools.permutations(arr[1:]))
    return [[pertama] + list(perm) for perm in permutasi_penuh]

def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil

# --- Fungsi Latihan 2: Atur Buku ---
def atur_buku(n, r):
    """
    Menghitung semua cara mengatur n buku di r rak/ bagian
    Setiap buku bisa masuk ke rak mana pun
    """
    return list(itertools.product(range(1, r+1), repeat=n))

# --- Menu Interaktif ---
def main():
    while True:
        print("\nPILIH JENIS PERMUTASI / PERHITUNGAN:")
        print("1. Permutasi Sebagian")
        print("2. Permutasi Menyeluruh")
        print("3. Permutasi Keliling")
        print("4. Permutasi Kelompok")
        print("5. Atur Buku di Rak")
        print("6. Keluar")
        
        pilihan = input("Masukkan pilihan (1-6): ").strip()

        if pilihan in ['1','2','3']:
            arr = input("Masukkan data (pisahkan dengan spasi): ").strip().split()
            arr = [int(x) for x in arr]  # konversi ke integer
            
            if pilihan == '1':
                k = int(input("Masukkan jumlah elemen yang dipermutasi (k): "))
                hasil = permutasi_sebagian(arr, k)
            elif pilihan == '2':
                hasil = permutasi_menyeluruh(arr)
            elif pilihan == '3':
                hasil = permutasi_keliling(arr)
            
            print("\nHasil Permutasi:")
            for h in hasil:
                print(h)
        
        elif pilihan == '4':
            grup_input = input(
                "Masukkan grup, pisahkan elemen tiap kelompok dengan koma dan grup dengan titik koma:\nContoh: 1,2;3,4\n"
            )
            grup = [[int(x) for x in g.split(',')] for g in grup_input.split(';')]
            hasil = permutasi_berkelompok(grup)
            print("\nHasil Permutasi Berkelompok:")
            for h in hasil:
                print(h)
        
        elif pilihan == '5':
            n = int(input("Jumlah buku (n): "))
            r = int(input("Jumlah rak/ bagian (r): "))
            hasil = atur_buku(n, r)
            print(f"\nSemua cara mengatur {n} buku di {r} rak:")
            for h in hasil:
                print(h)
        
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
