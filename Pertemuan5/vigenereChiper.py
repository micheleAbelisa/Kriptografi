# =====================================================
#  PROGRAM VIGENÈRE CIPHER GUI (TKINTER + PBO)
# =====================================================

import tkinter as tk
from tkinter import ttk, messagebox


# ====== CLASS UTAMA VIGENERE CIPHER ======
class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def huruf_ke_angka(self, h):
        return ord(h.upper()) - ord('A')

    def angka_ke_huruf(self, a):
        return chr((a % 26) + ord('A'))

    def ulangi_kunci(self, panjang):
        return (self.key * (panjang // len(self.key))) + self.key[:panjang % len(self.key)]

    def enkripsi(self, plaintext):
        plaintext = plaintext.replace(" ", "").upper()
        kunci = self.ulangi_kunci(len(plaintext))
        ciphertext = ""
        proses = []

        for i in range(len(plaintext)):
            p = self.huruf_ke_angka(plaintext[i])
            k = self.huruf_ke_angka(kunci[i])
            c = (p + k) % 26
            cipher_huruf = self.angka_ke_huruf(c)
            ciphertext += cipher_huruf
            proses.append(f"{i+1}. {plaintext[i]}({p}) + {kunci[i]}({k}) = {c} -> {cipher_huruf}")

        hasil = f"Hasil Enkripsi (Ciphertext): {ciphertext}"
        return hasil, proses

    def dekripsi(self, ciphertext):
        ciphertext = ciphertext.replace(" ", "").upper()
        kunci = self.ulangi_kunci(len(ciphertext))
        plaintext = ""
        proses = []

        for i in range(len(ciphertext)):
            c = self.huruf_ke_angka(ciphertext[i])
            k = self.huruf_ke_angka(kunci[i])
            p = (c - k + 26) % 26
            plain_huruf = self.angka_ke_huruf(p)
            plaintext += plain_huruf
            proses.append(f"{i+1}. {ciphertext[i]}({c}) - {kunci[i]}({k}) = {p} -> {plain_huruf}")

        hasil = f"Hasil Dekripsi (Plaintext): {plaintext}"
        return hasil, proses


# ====== CLASS GUI TKINTER ======
class VigenereApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Vigenère Cipher - Enkripsi & Dekripsi (PBO)")
        self.root.geometry("720x600")
        self.root.config(bg="#f4f4f4")

        self.create_widgets()

    def create_widgets(self):
        # Judul
        title = tk.Label(self.root, text="Vigenère Cipher", font=("Poppins", 20, "bold"), bg="#f4f4f4")
        title.pack(pady=10)

        # Frame input
        frame = tk.Frame(self.root, bg="#f4f4f4")
        frame.pack(pady=10)

        # Label dan input teks
        tk.Label(frame, text="Teks :", bg="#f4f4f4", font=("Poppins", 12)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_text = tk.Entry(frame, width=40, font=("Consolas", 12))
        self.entry_text.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Kunci :", bg="#f4f4f4", font=("Poppins", 12)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_key = tk.Entry(frame, width=40, font=("Consolas", 12))
        self.entry_key.grid(row=1, column=1, padx=5, pady=5)

        # Tombol
        btn_frame = tk.Frame(self.root, bg="#f4f4f4")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="🔒 Enkripsi", command=self.enkripsi_action, width=15, bg="#4CAF50", fg="white", font=("Poppins", 11, "bold")).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="🔓 Dekripsi", command=self.dekripsi_action, width=15, bg="#2196F3", fg="white", font=("Poppins", 11, "bold")).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="❌ Hapus", command=self.clear_fields, width=10, bg="#f44336", fg="white", font=("Poppins", 11, "bold")).grid(row=0, column=2, padx=10)

        # Output area
        self.text_output = tk.Text(self.root, width=80, height=20, font=("Consolas", 11), wrap="word", bg="#fff")
        self.text_output.pack(pady=15)
        self.text_output.insert(tk.END, "Hasil proses akan muncul di sini...")

    def clear_fields(self):
        self.entry_text.delete(0, tk.END)
        self.entry_key.delete(0, tk.END)
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, "Hasil proses akan muncul di sini...")

    def enkripsi_action(self):
        text = self.entry_text.get()
        key = self.entry_key.get()

        if not text or not key:
            messagebox.showwarning("Peringatan", "Teks dan kunci tidak boleh kosong!")
            return

        cipher = VigenereCipher(key)
        hasil, proses = cipher.enkripsi(text)

        self.tampilkan_output("ENKRIPSI", text, key, hasil, proses)

    def dekripsi_action(self):
        text = self.entry_text.get()
        key = self.entry_key.get()

        if not text or not key:
            messagebox.showwarning("Peringatan", "Teks dan kunci tidak boleh kosong!")
            return

        cipher = VigenereCipher(key)
        hasil, proses = cipher.dekripsi(text)

        self.tampilkan_output("DEKRIPSI", text, key, hasil, proses)

    def tampilkan_output(self, mode, text, key, hasil, proses):
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, f"=== PROSES {mode} VIGENÈRE CIPHER ===\n")
        self.text_output.insert(tk.END, f"Teks  : {text}\nKunci : {key}\n\nLangkah-langkah:\n")
        for step in proses:
            self.text_output.insert(tk.END, step + "\n")
        self.text_output.insert(tk.END, "\n" + hasil)


# ====== MAIN PROGRAM ======
if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereApp(root)
    root.mainloop()
