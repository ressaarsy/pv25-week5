import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox,
    QPushButton, QMessageBox, QVBoxLayout, QFormLayout,
    QShortcut, QHBoxLayout
)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Validasi Formulir - PyQt5")
        self.setGeometry(100, 100, 600, 500) 
        self.tampil_ui()

    def tampil_ui(self):
        layout = QVBoxLayout()
        form = QFormLayout()

        self.nama = QLineEdit()
        self.email = QLineEdit()
        self.umur = QLineEdit()
        self.hp = QLineEdit()
        self.hp.setInputMask('+62 000 0000 0000;_')
        self.alamat = QLineEdit()

        self.jk = QComboBox()
        self.jk.addItems(["", "Laki-laki", "Perempuan"])

        self.pdd = QComboBox()
        self.pdd.addItems(["", "SMA", "D3", "S1", "S2", "S3"])

        form.addRow("Nama", self.nama)
        form.addRow("Email", self.email)
        form.addRow("Umur", self.umur)
        form.addRow("No. HP", self.hp)
        form.addRow("Alamat", self.alamat)
        form.addRow("Jenis Kelamin", self.jk)
        form.addRow("Pendidikan", self.pdd)

        layout.addLayout(form)

        tombol_layout = QHBoxLayout()
        self.btn_simpan = QPushButton("Simpan")
        self.btn_simpan.clicked.connect(self.validasi)

        self.btn_clear = QPushButton("Clear")
        self.btn_clear.clicked.connect(self.kosongkan)

        tombol_layout.addWidget(self.btn_simpan)
        tombol_layout.addWidget(self.btn_clear)

        layout.addLayout(tombol_layout)

        self.ttd = QLabel("Nama: MUH. RESSA ARSY MA'RIF\nNIM: F1D022137")
        self.ttd.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.ttd)

        tombol_q = QShortcut(QKeySequence("Q"), self)
        tombol_q.activated.connect(self.close)

        self.setLayout(layout)

    def validasi(self):
        nama = self.nama.text()
        email = self.email.text()
        umur = self.umur.text()
        hp = self.hp.text().replace(" ", "")
        alamat = self.alamat.text()
        jk = self.jk.currentText()
        pdd = self.pdd.currentText()

        if nama == "":
            self.pesan("Nama tidak boleh kosong.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.pesan("Email tidak valid.")
        elif not umur.isdigit():
            self.pesan("Umur harus angka.")
        elif not (17 <= int(umur) <= 60):
            self.pesan("Umur harus 17-60 tahun.")
        elif len(hp) < 14:
            self.pesan("Nomor HP harus 13 digit.")
        elif alamat == "":
            self.pesan("Alamat wajib diisi.")
        elif jk == "":
            self.pesan("Pilih jenis kelamin.")
        elif pdd == "":
            self.pesan("Pilih pendidikan.")
        else:
            self.pesan("Data berhasil disimpan!", True)
            self.kosongkan()

    def pesan(self, isi, sukses=False):
        kotak = QMessageBox(self) 
        if sukses:
            kotak.setIcon(QMessageBox.Information)
            kotak.setWindowTitle("Sukses")
        else:
            kotak.setIcon(QMessageBox.Warning)
            kotak.setWindowTitle("Peringatan")
        kotak.setText(isi)
        kotak.exec_()

    def kosongkan(self):
        self.nama.clear()
        self.email.clear()
        self.umur.clear()
        self.hp.clear()
        self.alamat.clear()
        self.jk.setCurrentIndex(0)
        self.pdd.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jendela = Form()
    jendela.show()
    sys.exit(app.exec_())
