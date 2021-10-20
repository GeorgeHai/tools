import time
import requests
import conn_tools
from datetime import datetime


def current_time():
    now = datetime.now()
    return now.strftime("%D %H:%M:%S")


def connection_check(url, timeout, ip_table):
    flag = True
    while (flag):
        try:
            request = requests.get(url, timeout=timeout)
            print('{} Internet-connction active.'.format(current_time()))
        except (requests.ConnectionError, requests.Timeout):
            for ip in ip_table:
                print('\n {} Check ip-adress: {}'.format(current_time(), ip))
                conn_tools.ping(ip)
            flag = False
            print("Programm stops now")
        time.sleep(10)


if __name__ == '__main__':
    ip_table = '192.168.178.1', '192.168.178.45'
    connection_check(url='http://google.com', timeout=5, ip_table=ip_table)
