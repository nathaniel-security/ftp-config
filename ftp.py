import os
import shutil

os.system("sudo apt-get install vsftpd")


os.system("rm /etc/vsftpd.conf")

shutil.copy2("/home/groot/Documents/projects/windows_virus/vsftpd.conf", "etc/vsftpd.conf")
#hhave to change directory

os.system("sudo service vsftpd restart")


#
name = input("Username for ftp:- ")
#
command = "sudo useradd -m " +  name  + " -s /usr/sbin/nologin" 
os.system(command)
command = 'sudo passwd ' + name
os.system(command)
#
#
f=open("/etc/shells","a")
f.write('\n/usr/sbin/nologin')
f.close
#print(data)