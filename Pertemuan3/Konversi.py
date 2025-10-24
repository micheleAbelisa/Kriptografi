# ==========================================
#     Program Konversi Bilangan
# ==========================================
# 1. Biner → Desimal, Hexadesimal
# 2. Oktal → Desimal, Biner, Hexadesimal
# 3. Hexadesimal → Desimal, Biner, Oktal
# ==========================================

def biner_ke_desimal(biner):
    return int(biner, 2)

def biner_ke_hexadesimal(biner):
    desimal = int(biner, 2)
    return hex(desimal)[2:].upper()

def oktal_ke_desimal(oktal):
    return int(oktal, 8)

def oktal_ke_biner(oktal):
    desimal = int(oktal, 8)
    return bin(desimal)[2:]

def oktal_ke_hexadesimal(oktal):
    desimal = int(oktal, 8)
    return hex(desimal)[2:].upper()

def hexadesimal_ke_desimal(hexa):
    return int(hexa, 16)

def hexadesimal_ke_biner(hexa):
    desimal = int(hexa, 16)
    return bin(desimal)[2:]

def hexadesimal_ke_oktal(hexa):
    desimal = int(hexa, 16)
    return oct(desimal)[2:]

# ==========================================
# Menu Utama
# ==========================================
while True:
    print("\n==========================================")
    print("      Program Konversi Bilangan")
    print("==========================================")
    print("1. Konversi dari Biner")
    print("2. Konversi dari Oktal")
    print("3. Konversi dari Hexadesimal")
    print("4. Keluar")
    print("==========================================")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        biner = input("Masukkan bilangan Biner: ")
        try:
            print(f"Desimal      : {biner_ke_desimal(biner)}")
            print(f"Hexadesimal  : {biner_ke_hexadesimal(biner)}")
        except ValueError:
            print(" INPUT TIDAK VALID UNTUK BILANGAN BINER!!!")

    elif pilihan == '2':
        oktal = input("Masukkan bilangan Oktal: ")
        try:
            print(f"Desimal      : {oktal_ke_desimal(oktal)}")
            print(f"Biner        : {oktal_ke_biner(oktal)}")
            print(f"Hexadesimal  : {oktal_ke_hexadesimal(oktal)}")
        except ValueError:
            print("INPUT TIDAK VALID UNTUK BILANGAN OKTAL!!!")

    elif pilihan == '3':
        hexa = input("Masukkan bilangan Hexadesimal: ")
        try:
            print(f"Desimal      : {hexadesimal_ke_desimal(hexa)}")
            print(f"Biner        : {hexadesimal_ke_biner(hexa)}")
            print(f"Oktal        : {hexadesimal_ke_oktal(hexa)}")
        except ValueError:
            print("INPUT TIDAK VALID UNTUK BILANGAN HEXADESIMAL!!!")

    elif pilihan == '4':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid! Coba lagi.")
