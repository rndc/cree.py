#!/usr/bin/env python
from justestlib import scanport

def main():
    tgt=raw_input('> tgt ip/url > ')

    try:
        while True:
            if tgt is not '':
                if 'http://' in tgt:
                    if 'www' in tgt:
                        tgt='http://'+tgt
            else:
                if tgt.isdigit == True:
                    tgt=tgt

            scanport(tgt)
    except KeyboardInterrupt:
        print 'interrupted by user'
        

if __name__ == '__main__':
    main()
