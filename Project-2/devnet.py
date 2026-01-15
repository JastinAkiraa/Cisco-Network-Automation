from netmiko import ConnectHandler
import getpass

username = input("Masukkan Username : ")
password = getpass.getpass()

r = open('device_list.txt','r')
for ip_address in r.readlines():
    ip_address = ip_address.strip('\n')
    login = {
        'device_type' : 'cisco_ios',
        'host' : ip_address,
        'username' : username,
        'password' : password
    }
    net_connect = ConnectHandler(**login)
    backup = net_connect.send_command("show run")
    print(f"Backup Completed for {ip_address}")
    
    #Membuat File Backup dengan nama IP 
    backupname = ip_address +'.txt'
    w = open(backupname,'w')
    w.write(backup)
    w.close()