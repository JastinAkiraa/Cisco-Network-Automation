# Network Automation - Devnet Projects

Repository ini berisi kumpulan script Python untuk network automation menggunakan Netmiko untuk terhubung ke router Cisco secara virtual di sandbox environment. Terdapat dua project dengan fungsionalitas berbeda.

## Struktur Folder

```
Devnet/
├── Project-1/           # Show IP Interface Information
│   ├── dev.py          # Script untuk menampilkan info IP interface
│   ├── ip_list.txt     # Daftar IP address router
│   └── Show/           # Folder untuk menyimpan output
├── Project-2/          # Router Configuration Backup
│   ├── devnet.py       # Script untuk backup konfigurasi router
│   ├── device_list.txt # Daftar IP address device
│   └── *.txt           # File backup konfigurasi per device
└── README.md           # Dokumentasi utama
```

## Project-1: Show IP Interface Information

**Deskripsi**: Script ini menghubungkan ke multiple router Cisco dan menampilkan informasi IP interface dari setiap router.

### Fitur

- Membaca daftar IP dari file `ip_list.txt`
- Koneksi otomatis ke setiap router menggunakan SSH
- Menjalankan perintah `show ip int brief` untuk menampilkan status interface
- Penanganan error untuk koneksi yang gagal
- Input username dan password secara aman menggunakan getpass

### Cara Penggunaan

```bash
cd Project-1
python dev.py
```

Masukkan username dan password ketika diminta.

### Contoh Output

```
Menghubungkan ke 131.226.217.182...
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     192.168.1.1     YES manual up                    up
GigabitEthernet0/1     unassigned      YES unset  administratively down down
Loopback0              10.0.0.1        YES manual up                    up
```

## Project-2: Router Configuration Backup

**Deskripsi**: Script ini menghubungkan ke multiple router Cisco dan melakukan backup konfigurasi running configuration ke file dengan nama sesuai IP address.

### Fitur

- Membaca daftar IP dari file `device_list.txt`
- Koneksi otomatis ke setiap router menggunakan SSH
- Menjalankan perintah `show run` untuk mengambil running configuration
- Menyimpan backup ke file dengan nama `<IP_ADDRESS>.txt`
- Otomatis membuat file backup untuk setiap device

### Cara Penggunaan

```bash
cd Project-2
python devnet.py
```

Masukkan username dan password ketika diminta. File backup akan dibuat otomatis dengan nama IP address.

### Contoh Output

```
Backup Completed for 131.226.217.182
```

File backup akan tersimpan sebagai `131.226.217.182.txt` berisi seluruh konfigurasi running dari router.

## Prasyarat

- Python 3.x
- Library Netmiko: `pip install netmiko`
- Akses SSH ke router Cisco virtual di sandbox environment
- Username dan password yang valid untuk router

## Instalasi

1. Clone atau download repository ini

2. Install dependencies:
   ```bash
   pip install netmiko
   ```

3. Persiapkan file daftar IP address:
   - Untuk Project-1: buat file `ip_list.txt` berisi daftar IP (satu IP per baris)
   - Untuk Project-2: buat file `device_list.txt` berisi daftar IP (satu IP per baris)

## Catatan Penting

- Pastikan router virtual di sandbox dapat diakses melalui SSH (port 22)
- Username dan password default biasanya 'cisco' tergantung konfigurasi sandbox
- Script ini dirancang untuk environment testing/lab
- Gunakan dengan hati-hati di production environment
- Pastikan file list berisi IP yang valid dan terpisah per baris (tanpa spasi)

## Kontribusi

Kontribusi sangat diterima! Silakan buat improvement dan perbaikan untuk project ini.

## Lisensi

Proyek ini menggunakan lisensi MIT.