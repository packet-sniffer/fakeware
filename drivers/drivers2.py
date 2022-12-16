#!c:/Python/python.exe

'''
This program is used to validate DNS filter for test-c2.panw.com
'''

import socket
from time import sleep


def dns_checker(domain_list):
    for domain in domain_list:
        print(f'Trying to resolve {domain}', end = '')
        for i in range(4):
            print('!', end = '')
            sleep(1)
        try:
            result = socket.gethostbyname(domain)
            if result == '72.5.65.115':
                print(f'\nDNS Resolution to {domain} succeeded')
            else:
                print(f'\nDNS Resolution to {domain} failed')
        except:
            print(f'\nFailed DNS resolution for {domain}')


def main():
    dns_list = ["test-c2.testpanw.com",
            "test-dnstun.testpanw.com",
            "test-malware.testpanw.com"
    ]
    dns_checker(dns_list)
    input('press enter to close the window')


if __name__ == "__main__":
    main()
    
        
