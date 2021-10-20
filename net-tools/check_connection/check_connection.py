import time
import requests
import conn_tools
from datetime import datetime

"""
current_time() returns based on datetime the current time and returns it for further usage
"""


def current_time():
    now = datetime.now()
    return now.strftime("%D %H:%M:%S")


"""
The Method connection_check is used to check your server-connection in the background.
The the given url isn't available, it starts to check the ip-addresses from the provided ip_table.
The results are written to a specified file.

After the connection-check the method takes a break for 10 seconds and restarts. This can be deactivated by 
uncommenting the line 31. 
"""


def connection_check(url, timeout, ip_table, log_file=True, path='./'):
    flag = True
    while (flag):
        try:
            request = requests.get(url, timeout=timeout)
            print('{} Internet-connction active.'.format(current_time()))
        except (requests.ConnectionError, requests.Timeout):
            for ip in ip_table:
                print('\n {} Check ip-adress: {}'.format(current_time(), ip))
                conn_tools.ping(ip, log_file=log_file, path=path)
            # flag = False          # you can deactivate reactivation in this line
            if (flag == False):
                print("Programm stops in 10 sec.")
        time.sleep(10)


"""
The ip_table contains the provided ip-addresses you would like to check, if the connection is timed-out.
"""
if __name__ == '__main__':
    ip_table = '192.168.178.1', '192.168.178.45'
    connection_check(url='http://google.com',
                     timeout=5,
                     ip_table=ip_table,
                     log_file=False,
                     path='./logs/')
