#!c:/Python/python.exe
'''
This program is used to validate URL FIlters and DNS Filters for command and control
'''

import subprocess


def read_list(file_txt):
    with open(file_txt, "r") as f:
        out_file = f.read().strip().split()
    return out_file


def domain_check(d_list):
    for domains in d_list:
        try:
            #answer = subprocess.run(["nslookup", domains], capture_output = True)
            result = subprocess.Popen(f"nslookup {domains}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #print(answer)
            print(result.communicate())
        except:
            pass
            print(f"Failed {domains}")

def url_check(u_list):
    for urls in u_list:
        try:
            result = subprocess.Popen(f"curl {urls}", shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
            print(result.communicate())
        except:
            pass
        print(f"Failed {urls}")
    

def main():
    domain_check(read_list("domain_list.txt"))
    url_check(read_list("url_list.txt"))


if __name__ == "__main__":
    main()
