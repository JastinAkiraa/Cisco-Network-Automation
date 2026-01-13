# Network Automation Router Connection

Proyek ini adalah implementasi awal network automation menggunakan Python untuk terhubung ke router Cisco secara virtual di sandbox environment. Script ini akan membaca daftar IP address dari file `ip_list.txt` dan menampilkan informasi IP interface untuk setiap router yang berhasil dihubungkan.

## Deskripsi

Script Python ini menggunakan library Netmiko untuk melakukan koneksi SSH ke router Cisco virtual. Setelah terhubung, script akan menjalankan perintah `show ip int brief` untuk menampilkan status dan alamat IP dari semua interface pada router tersebut.

## Fitur

- Koneksi otomatis ke multiple router berdasarkan daftar IP
- Menampilkan informasi IP interface untuk setiap router
- Penanganan error untuk koneksi yang gagal
- Input username dan password secara aman menggunakan getpass

## Prasyarat

- Python 3.x
- Library Netmiko (`pip install netmiko`)
- Akses ke router Cisco virtual di sandbox environment
- File `ip_list.txt` berisi daftar IP address router (satu IP per baris)

## Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. Install dependencies:
   ```bash
   pip install netmiko
   ```

3. Pastikan file `ip_list.txt` ada di direktori yang sama dengan script, berisi IP address router yang ingin dihubungkan.

## Penggunaan

1. Jalankan script:
   ```bash
   python dev.py
   ```

2. Masukkan username dan password ketika diminta.

3. Script akan mencoba menghubungkan ke setiap IP di `ip_list.txt` dan menampilkan informasi IP interface.

## Contoh Output

```
Menghubungkan ke 131.226.217.182...
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     192.168.1.1     YES manual up                    up
GigabitEthernet0/1     unassigned      YES unset  administratively down down
Loopback0              10.0.0.1        YES manual up                    up
```

## Struktur File

- `dev.py`: Script utama untuk koneksi dan automation
- `ip_list.txt`: File berisi daftar IP address router
- `README.md`: Dokumentasi proyek

## Kontribusi

Kontribusi sangat diterima! Silakan buat issue atau pull request untuk perbaikan dan peningkatan.

## Lisensi

Proyek ini menggunakan lisensi MIT. Lihat file LICENSE untuk detail lebih lanjut.

## Catatan

- Pastikan router virtual di sandbox dapat diakses melalui SSH
- Username dan password default mungkin 'cisco' tergantung konfigurasi sandbox
- Script ini dirancang untuk environment testing, gunakan dengan hati-hati di production