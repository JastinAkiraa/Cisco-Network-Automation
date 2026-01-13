from netmiko import ConnectHandler
import getpass

def DeviceCisco(username, password, ip_address):

    cisco_router = {
    'device_type' : 'cisco_ios',
    'host'        : ip_address,
    'username' : username,
    'password' : password,
    'secret' : 'cisco',
    }
    try:
        print(f"\nMenghubungkan ke {ip_address}...")
        net_connect = ConnectHandler(**cisco_router)
        net_connect.enable()
        get_Ip = net_connect.send_command('show ip int brief')
        print(get_Ip)

        net_connect.disconnect()
    except Exception as e:
        print(f"Gagal terhubung ke {ip_address}: {e}")

# MAIN SCRIPT 
username = input("Masukkan username : ")
password = getpass.getpass("Masukkan Password : ")

#Membaca File Ip
try:
    with open("ip_list.txt","r") as file:
        #Melakukan loop untuk setiap baris di file
        for line in file:
            ip = line.strip()
            DeviceCisco(username, password, ip)
except FileNotFoundError:
    print("File ip list.txt tidak ditemukan!")

# Memanggil Fungsi 
#GiU_-kwD57Xr4U

