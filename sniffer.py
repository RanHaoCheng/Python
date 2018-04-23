import socket
import struct
import textwrap

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW , socket.ntohs(3))
    pkg_count = 0
    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac , src_mac , eth_proto , data = ethernet_frame(raw_data)
        pkg_count = pkg_count + 1
        #print('\nEthernet frame: {}'.format(pkg_count))
        print('Cnt : {} Destination : {} , Source : {} , Protocol : {} \n\r data : {}'.format(pkg_count, dest_mac,src_mac,eth_proto , data))



# unpack ethernet frame
def ethernet_frame(data):
    dest_mac , src_mac , proto = struct.unpack('! 6s 6s H' , data[:14])
    return get_mac_addr(dest_mac) , get_mac_addr(src_mac) , socket.htons(proto) , data[14:]



# Return properly formatted MAC address
def get_mac_addr(bytes_addr):
    bytes_string = map('{:02x}'.format , [int(i) for i in bytes_addr])
    return ':'.join(bytes_string).upper()


main()
