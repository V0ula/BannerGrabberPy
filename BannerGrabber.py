#!/usr/bin/python3

import socket
import sys
import time

def validate_timeout(timeout_insec):
    try:
        timeout_insec = int(timeout_insec)
    except ValueError:
        print("[+] The " + timeout_insec + " is not a valid input for timeout.")
        print("[+] Input should be a number.")
        sys.exit(1)


def validate_ip(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
        print("[+] It seems like you have entered an legit IP adrress.")
    except socket.error:
        print("[+] That input does not match a legit IP address.")
        sys.exit(1)
        

def validate_port(port):
    try:
        port = int(port)
        if 1<= port <= 65535:
            print("[+] It seems like you have entered a legit port number.")
            print("[+] Let's try grab some banners, shall we?")
            time.sleep(1)
        else:
            print("[+] Error! " + port + " is not a valid port number. Input should between 1 and 65535.")
            sys.exit(1)

    except ValueError:
        print("[+] Error! " + port + " is not a valid port number. Input should between 1 and 65535.")
        sys.exit(1)

def banner(ip, port, timeout_insec):
    try:
        s = socket.socket()
        s.connect((ip, int(port)))
        s.settimeout(int(timeout_insec))
        print("[+] It seems that we got something interesting for you!")
        time.sleep(1)
        print("[+] Here is the banner: " + s.recv(1024).decode("utf-8").rstrip())
    except ConnectionError:
        print("[+] Oops, it seems like the service is not running on the target!")

def main():
    timeout_insec = input("[+] Please specify timeout (in secs) for your request: ")
    validate_timeout(timeout_insec)
    ip = input("[+] Please enter target's IP address: ")
    validate_ip(ip)
    port = str(input("[+] Please enter target's port: "))
    validate_port(port)
    banner(ip, port, timeout_insec)

main()