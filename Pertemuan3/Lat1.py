# ==========================================
#     Konversi Biner ke Desimal & Hexadesimal
# ==========================================

print("====================================")
print("  Konversi Bilangan Biner ke Desimal & Hexadesimal")
print("====================================")

while True:
    biner = input("Masukkan bilangan biner (atau ketik 'exit' untuk keluar): ")

    if biner.lower() == "exit":
        print("Program selesai. Terima kasih!")
        break

    # Validasi: pastikan hanya berisi angka 0 dan 1
    if not all(bit in '01' for bit in biner):
        print("❌ Error: Input bukan bilangan biner! Coba lagi.\n")
        continue

    # Konversi ke desimal dan hexadesimal
    desimal = int(biner, 2)
    heksa = hex(desimal)[2:].upper()

    # Tampilkan hasil
    print("------------------------------------")
    print(f"Biner       : {biner}")
    print(f"Desimal     : {desimal}")
    print(f"Hexadesimal : {heksa}")
    print("------------------------------------\n")
