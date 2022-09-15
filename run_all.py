from multiprocessing import Pool
import os
import socket


# gets Wireless LAN IP Address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP_address = s.getsockname()[0]
    except:
        IP_address = '127.0.0.1'
    finally:
        s.close()
    return IP_address


def run_process(process):
    os.system('python {}'.format(process))


if __name__ == '__main__':
    processes = ('main.py',
                 './web_server/manage.py runserver {}:80'.format(get_ip()))
    pool = Pool(processes=len(processes))
    pool.map(run_process, processes)

