
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Menghubungkan tombol Simpan dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)

        # Memuat data buku saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan isi tabel sebelum memuat data baru
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data buku dari Model
        data_buku = self.model.get_all_buku()

        # Memasukkan data buku ke tabel View
        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def simpan_data(self):
        # Mengambil input dari form View
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Memeriksa apakah semua kolom sudah diisi
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Menyimpan data melalui Model
        berhasil = self.model.create_buku(judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )

            # Mengosongkan form setelah data berhasil disimpan
            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")

            # Memperbarui tabel agar data baru langsung terlihat
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Terjadi kesalahan saat menyimpan data."
            )

    def run(self):
        # Menjalankan jendela aplikasi
        self.view.mainloop()
