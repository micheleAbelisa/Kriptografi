import re

print("====================================")
print("           Tugas Praktikum 2        ")
print("====================================")
print("Buat Kalkulator Hybrid")
print("====================================\n")

while True:
    # Bagian 1: ekspresi tanpa spasi
    while True:
        print("Contoh Input Ekspresi tanpa spasi:")
        ekspresi = input("Input (Ekspresi): ")

        if " " in ekspresi:
            print("❌ Error: Ekspresi ini mengandung spasi!")
            print("Silakan masukkan ulang ekspresi tanpa spasi.")
            print("------------------------------------")
            continue

        try:
            # Pisahkan angka dan operator
            token = re.findall(r'\d+|[\+\-\*\/]', ekspresi)

            if len(token) < 3:
                raise ValueError("Ekspresi tidak lengkap!")

            # Hitung dari kiri ke kanan
            hasil = float(token[0])
            i = 1
            while i < len(token) - 1:
                op = token[i]
                angka = float(token[i + 1])

                if op == '+':
                    hasil += angka
                elif op == '-':
                    hasil -= angka
                elif op == '*':
                    hasil *= angka
                elif op == '/':
                    hasil /= angka
                i += 2

            print("Output >", int(hasil) if hasil.is_integer() else hasil)
            print("------------------------------------")
            break

        except Exception as e:
            print(f"❌ Terjadi kesalahan: {e}")
            print("Silakan input ulang ekspresi yang benar.")
            print("------------------------------------")

    # Bagian 2: ekspresi dengan spasi
    while True:
        print("\nContoh Input Ekspresi dengan spasi:")
        ekspresi2 = input("Input (Ekspresi): ")

        if " " not in ekspresi2:
            print("❌ Error: Ekspresi ini tidak mengandung spasi!")
            print("Silakan masukkan ulang ekspresi dengan spasi.")
            print("------------------------------------")
            continue

        try:
            ekspresi_bersih2 = ekspresi2.replace(" ", "")
            token2 = re.findall(r'\d+|[\+\-\*\/]', ekspresi_bersih2)

            if len(token2) < 3:
                raise ValueError("Ekspresi tidak lengkap!")

            hasil2 = float(token2[0])
            i = 1
            while i < len(token2) - 1:
                op = token2[i]
                angka = float(token2[i + 1])

                if op == '+':
                    hasil2 += angka
                elif op == '-':
                    hasil2 -= angka
                elif op == '*':
                    hasil2 *= angka
                elif op == '/':
                    hasil2 /= angka
                i += 2

            print("Output >", int(hasil2) if hasil2.is_integer() else hasil2)
            print("------------------------------------")
            break

        except Exception as e:
            print(f"❌ Terjadi kesalahan: {e}")
            print("Silakan input ulang ekspresi yang benar.")
            print("------------------------------------")

    # Tanya lanjut
    lanjut = input("Ingin menghitung lagi? (y/n): ").lower()
    if lanjut != 'y':
        print("\nProgram selesai.")
        break
