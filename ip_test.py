from ip_address.ip_pack.ip_addr import get_ip_address
import time

if __name__ == '__main__':
    start_time = time.time()
    print(get_ip_address('www.google.com'))
    print(time.time() - start_time)