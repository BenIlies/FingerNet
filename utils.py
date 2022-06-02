from scapy.all import IP, TCP


def create_TCP_packet():
	return IP()/TCP()

def set_IP_dst(packet, dst):
	packet['IP'].dst = dst

def set_IP_src(packet, src):
	packet['IP'].src = src

def set_TCP_sport(packet, sport):
	packet['TCP'].sport = int(sport)

def set_TCP_dport(packet, dport):
	packet['TCP'].dport = int(dport)

def set_TCP_seq(packet, seq):
	packet['TCP'].seq = int(seq)

def set_TCP_flags(packet, flags):
	packet['TCP'].flags = flags

def set_TCP_ack(packet, ack):
    packet['TCP'].ack = int(ack)

def set_TCP_automatic_packet_seq(packet):
	increase = 0
	if packet['TCP'].flags in ['S','F','SA','FA']:
		increase =  1
	elif packet['TCP'].flags in ['P','PA']:
		increase = len(packet['TCP'].payload)
	packet['TCP'].seq = packet['TCP'].seq + increase

def set_TCP_automatic_packet_ack(ack_packet, original_packet):
	increase = 0
	if original_packet['TCP'].flags in ['S','F','SA','FA']:
		increase =  1
	elif original_packet['TCP'].flags in ['P','PA']:
		increase = len(original_packet['TCP'].payload)
	ack_packet['TCP'].ack = original_packet['TCP'].seq + increase

def set_TCP_payload(packet, payload):
	packet['TCP'].remove_payload()
	packet['TCP'].add_payload(payload)


def remove_TCP_payload(packet):
	packet['TCP'].remove_payload()



def get_safe_array(key):
    if isinstance(key, str):
        return [key]
    else:
        return key