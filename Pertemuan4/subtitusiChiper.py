def subtitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext


while True:  # loop program
    plaintext = input("\nMasukkan plaintext: ").upper()

    print("\nMasukkan aturan substitusi format A=B (ketik 'selesai' untuk berhenti)")
    aturan_subtitusi = {}

    # input aturan substitusi
    while True:
        aturan_input = input("Aturan: ").upper().strip()

        if aturan_input == "SELESAI":
            break

        if "=" in aturan_input and len(aturan_input.split("=")) == 2:
            huruf_asal, huruf_tujuan = aturan_input.split("=")

            if len(huruf_asal) == 1 and len(huruf_tujuan) == 1 and huruf_asal.isalpha() and huruf_tujuan.isalpha():
                aturan_subtitusi[huruf_asal] = huruf_tujuan
            else:
                print("Format salah! Contoh A=B (satu huruf saja)")
        else:
            print("Format salah! Contoh A=B")

    # proses enkripsi
    ciphertext = subtitusi_cipher(plaintext, aturan_subtitusi)

    print("\n===== HASIL =====")
    print(f"Plaintext  : {plaintext}")
    print(f"Aturan     : {aturan_subtitusi}")
    print(f"Ciphertext : {ciphertext}")

    # Tanya mau ulang atau tidak
    ulang = input("\nIngin mengulang? (y/n): ").lower()
    if ulang != "y":
        print("\nProgram selesai. Terima kasih!\n")
        break
