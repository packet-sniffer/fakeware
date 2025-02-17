#!c:/Python/python.exe


'''
This program is used to validate URL FIlters and DNS Filters for command and control
'''


import requests
import socket


def dns_checker(domain_list):
    my_list = []
    for domains in domain_list:
        try:
            new_item = socket.gethostbyname(domains)
            #print(new_item)
        except:
            pass
    return None


def url_filter(url_list):
    for urls in url_list:
        try:
            x = requests.get(urls)
            #print(x.text)
        except:
            pass
    return None
                

def main():
    dns_list = ["test-c2.testpanw.com",
                "test-dnstun.testpanw.com",
                "test-malware.testpanw.com"
        ]


    url_list = ["https://urlfiltering.paloaltonetworks.com/test-malware",
              "https://urlfiltering.paloaltonetworks.com/test-command-and-control",
              "https://urlfiltering.paloaltonetworks.com/test-ransomware"]


    dns_checker(dns_list)
    url_filter(url_list)
    return None

if __name__ == "__main__":
    main()
