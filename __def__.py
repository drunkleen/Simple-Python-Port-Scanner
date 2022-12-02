import socket
from IPy import IP
from os import system, name

def clearscreen():
    if name == 'nt':
        _ = system('cls')
    elif name == 'posix':
        _ = system('clear')
    else:
        _ = system('clear')

def logo():
    print('█▀▄ █▀█ █░█ █▄░█ █▄▀ █▀ █▀▀ ▄▀█ █▄░█ █▄░█ █▀▀ █▀█')
    print('█▄▀ █▀▄ █▄█ █░▀█ █░█ ▄█ █▄▄ █▀█ █░▀█ █░▀█ ██▄ █▀▄')


def port_scanner(ip_address,ip_range_start,ip_range_end,timeout,verbose):
    open_ports = ''
    open_ports_sum = 0

    for i in range(ip_range_start,ip_range_end):    
        try:
            sck = socket.socket()
            sck.settimeout(timeout)
            sck.connect((ip_finder(ip_address),i))

            try: # Try to get Port Banner
                port_banner = get_banner(sck).decode()
                if verbose == 'Active':
                    print(f'[+] {ip_address} | Scaning port > {i} open')

                open_ports += f'+ {i} {port_banner.strip("")}\n'
            except:
                if verbose == 'Active':
                    print(f'[+] {ip_address} | Scaning port > {i} open')

                open_ports += f'+ {i}\n'
            open_ports_sum += 1

        except:
            if verbose == 'Active':
                print(f'[-] {ip_address} | Scaning port > {i} closed')

    a = f'\n----------------> {ip_address} <----------------\n{open_ports_sum} Open Port:\n{open_ports}'
    return a

def get_banner(sck_bann):
    return sck_bann.recv(1024)

def ip_finder(url_ip):
    try:
        IP(url_ip)
        return url_ip
    except ValueError:
        return socket.gethostbyname(url_ip)
