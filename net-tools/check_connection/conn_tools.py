import platform
import subprocess

"""
The method ping uses provided data to create a subprocess-call.
The results can be written to a file.
"""
def ping(host, log_file=True, path='./'):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '5', host]
    if log_file:
        result_file = '{}{}.txt'.format(path, host)
        f = open(result_file, 'w')
        return subprocess.call(command, stdout=f) == 0
    else:
        return subprocess.call(command) == 0


if __name__ == '__main__':
    ping('192.168.1.1', log_file=True, path='./')
