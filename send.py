import socket
import json
import struct
from struct import pack
from uuid import getnode as get_mac

rasp_wlan0 = b'\xb8\x27\xeb\x2a\x5e\xf7'
rasp_eth0 = b'\xb8\x27\xeb\x7f\x0b\xa2'
broadcast = b'\xff\xff\xff\xff\xff\xff'


def send_commands(target_mac, data):
    interface = 'ens33'
    BOMB_PROT_ID = 0xC4C4
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_DGRAM, 0x0800)
    BOMB_FRAME = [
        bytes(json.dumps(data), 'utf-8')
    ]
    print(BOMB_FRAME)
    print(b''.join(BOMB_FRAME))
    addr = (interface, BOMB_PROT_ID, socket.PACKET_HOST, 0x0, target_mac)
    sock.sendto(b''.join(BOMB_FRAME), addr)
    sock.close()


local_mac = [int("{0:012x}".format(get_mac())[i:i + 2], 16) for i in range(0, 12, 2)]
rasp = [184, 39, 235, 42, 94, 247]
send_commands(broadcast, {'msg': "Explode"})
