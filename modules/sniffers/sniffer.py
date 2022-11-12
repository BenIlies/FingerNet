import codecs
import pickle
import logging
import json

from modules.utils import *
from scapy.all import AsyncSniffer, Ether, sniff

from modules.controllers.messages import JSONLOGMessage, JSONMessage

class Sniffer(AsyncSniffer):
    def __init__(self, machine, filter=''):
        super().__init__(prn=self.__handle_sniffer(), lfilter=lambda pkt: self.__filter_packet(pkt))
        self.machine = machine 
        self.__filter = filter

        
    def __handle_sniffer(self):
        def pkt_callback(packet):
            print("Packet received", packet)
        return pkt_callback
    
    def __filter_packet(self, packet):
        if 'Ether' in packet:
            if (packet[Ether].src != Ether().src):
                filtered_packets = sniff(offline=packet, filter=self.__filter)
                if packet in filtered_packets:
                    return True
        return False
    
    def set_filter(self, filter):
        self.__filter = filter
    
    def get_packet_layers(self, packet):
        layers = []
        counter = 0
        while True:
            layer = packet.getlayer(counter)
            if layer is None:
                break
            else:
                layers.append(layer)
            counter += 1
        return layers