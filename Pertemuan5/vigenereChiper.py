# =====================================================
#  PROGRAM VIGENÈRE CIPHER GUI (TKINTER + PBO CLEAN CODE)
# =====================================================

import tkinter as tk
from tkinter import messagebox


# =====================================================
# CLASS MODEL: VigenereCipher (logika enkripsi & dekripsi)
# =====================================================
class VigenereCipher:
    """Kelas yang mengatur proses enkripsi dan dekripsi Vigenere Cipher."""

    def __init__(self, key: str):
        self.key = key.upper()

    @staticmethod
    def huruf_ke_angka(h):
        return ord(h.upper()) - ord('A')

    @staticmethod
    def angka_ke_huruf(a):
        return chr((a % 26) + ord('A'))

    def ulangi_kunci(self, panjang):
        return (self.key * (panjang // len(self.key))) + self.key[:panjang % len(self.key)]

    def enkripsi(self, plaintext: str):
        plaintext = plaintext.replace(" ", "").upper()
        kunci = self.ulangi_kunci(len(plaintext))
        ciphertext, proses = "", []

        for i, p_huruf in enumerate(plaintext):
            p = self.huruf_ke_angka(p_huruf)
            k = self.huruf_ke_angka(kunci[i])
            c = (p + k) % 26
            cipher_huruf = self.angka_ke_huruf(c)
            ciphertext += cipher_huruf
            proses.append(f"{i+1}. {p_huruf}({p}) + {kunci[i]}({k}) = {c} → {cipher_huruf}")

        return f"Hasil Enkripsi: {ciphertext}", proses

    def dekripsi(self, ciphertext: str):
        ciphertext = ciphertext.replace(" ", "").upper()
        kunci = self.ulangi_kunci(len(ciphertext))
        plaintext, proses = "", []

        for i, c_huruf in enumerate(ciphertext):
            c = self.huruf_ke_angka(c_huruf)
            k = self.huruf_ke_angka(kunci[i])
            p = (c - k + 26) % 26
            plain_huruf = self.angka_ke_huruf(p)
            plaintext += plain_huruf
            proses.append(f"{i+1}. {c_huruf}({c}) - {kunci[i]}({k}) = {p} → {plain_huruf}")

        return f"Hasil Dekripsi: {plaintext}", proses


# =====================================================
# CLASS VIEW: Tampilan GUI (Tkinter)
# =====================================================
class VigenereApp(tk.Tk):
    """Kelas GUI utama untuk program Vigenere Cipher."""

    def __init__(self):
        super().__init__()
        self.title("🔐 Vigenère Cipher - PBO Edition")
        self.geometry("720x600")
        self.config(bg="#f9fafb")

        self.create_widgets()

    # ------------------------
    # Membuat elemen GUI
    # ------------------------
    def create_widgets(self):
        # Judul
        tk.Label(
            self,
            text="Vigenère Cipher",
            font=("Poppins", 22, "bold"),
            bg="#f9fafb",
            fg="#222"
        ).pack(pady=15)

        # Frame Input
        input_frame = tk.Frame(self, bg="#f9fafb")
        input_frame.pack(pady=5)

        self.create_label_entry(input_frame, "Teks :", 0)
        self.create_label_entry(input_frame, "Kunci :", 1)

        # Tombol aksi
        btn_frame = tk.Frame(self, bg="#f9fafb")
        btn_frame.pack(pady=10)

        self.create_button(btn_frame, "🔒 Enkripsi", "#4CAF50", self.enkripsi_action, 0)
        self.create_button(btn_frame, "🔓 Dekripsi", "#2196F3", self.dekripsi_action, 1)
        self.create_button(btn_frame, "❌ Hapus", "#f44336", self.clear_fields, 2)

        # Output area
        self.text_output = tk.Text(
            self, width=80, height=20,
            font=("Consolas", 11),
            wrap="word", bg="#ffffff",
            relief="flat", bd=2
        )
        self.text_output.pack(pady=15)
        self.reset_output()

    # ------------------------
    # Komponen bantu GUI
    # ------------------------
    def create_label_entry(self, parent, text, row):
        tk.Label(
            parent, text=text, bg="#f9fafb",
            font=("Poppins", 12), anchor="e", width=8
        ).grid(row=row, column=0, padx=5, pady=5)

        entry = tk.Entry(parent, width=45, font=("Consolas", 12), relief="solid", bd=1)
        entry.grid(row=row, column=1, padx=5, pady=5)

        if text.startswith("Teks"):
            self.entry_text = entry
        else:
            self.entry_key = entry

    def create_button(self, parent, text, color, command, col):
        tk.Button(
            parent, text=text, command=command,
            width=15, bg=color, fg="white",
            font=("Poppins", 11, "bold"),
            relief="flat", cursor="hand2", activebackground=color
        ).grid(row=0, column=col, padx=10)

    def reset_output(self):
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, "💡 Hasil proses akan tampil di sini...")

    # ------------------------
    # Fungsi tombol
    # ------------------------
    def clear_fields(self):
        self.entry_text.delete(0, tk.END)
        self.entry_key.delete(0, tk.END)
        self.reset_output()

    def enkripsi_action(self):
        self.proses_cipher("ENKRIPSI")

    def dekripsi_action(self):
        self.proses_cipher("DEKRIPSI")

    def proses_cipher(self, mode):
        text = self.entry_text.get()
        key = self.entry_key.get()

        if not text or not key:
            messagebox.showwarning("⚠️ Peringatan", "Teks dan kunci tidak boleh kosong!")
            return

        cipher = VigenereCipher(key)
        hasil, proses = (
            cipher.enkripsi(text) if mode == "ENKRIPSI" else cipher.dekripsi(text)
        )

        self.tampilkan_output(mode, text, key, hasil, proses)

    def tampilkan_output(self, mode, text, key, hasil, proses):
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, f"=== PROSES {mode} VIGENÈRE CIPHER ===\n")
        self.text_output.insert(tk.END, f"Teks  : {text}\nKunci : {key}\n\nLangkah-langkah:\n\n")
        for step in proses:
            self.text_output.insert(tk.END, f"{step}\n")
        self.text_output.insert(tk.END, "\n" + hasil)


# =====================================================
# MAIN PROGRAM
# =====================================================
if __name__ == "__main__":
    app = VigenereApp()
    app.mainloop()
