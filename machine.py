import time
from action_interpreter import ActionInterpreter
from utils import *
from scapy.all import send, AsyncSniffer, Ether
import hashlib

class Machine:
    def __init__(self, xstate_json, variables = {}):
        self.__id = xstate_json['id']
        self.__initial = xstate_json['initial']
        self.__states = xstate_json['states']
        self.__current_state = self.__initial
        self.__variables = variables
        self.__sniffer = AsyncSniffer(prn=self.__handle_sniffer(), lfilter=lambda pkt: pkt[Ether].src != Ether().src)
        self.__sniffer_stack = 'ans'
        self.__variables[self.__sniffer_stack] = []
        self.__complete_chain_states = [{self.__initial: hashlib.sha256(repr(time.time()).encode()).hexdigest()}]
        self.__chain_states = [self.__complete_chain_states[0]]

    def start(self):
        self.trigger('STARTED')

    def get_id(self):
        return self.__id

    def get_chain(self):
        return self.__chain_states

    def get_full_chain(self):
        return self.__complete_chain_states
    
    def get_state(self):
        return self.__current_state

    def start_sniffer(self):
        self.__sniffer.start()

    def stop_sniffer(self):
        self.__sniffer.stop()

    def set_stack(self, stack):
        self.__sniffer_stack = stack

    def get_stack(self):
        return self.__variables[self.__sniffer_stack]

    def get_stack_top(self):
        return self.__variables[self.__sniffer_stack][0]

    def discard_stack_packet(self, stack):
        stack.pop(0)

    def get_variable(self, name):
        return self.__variables[name]

    def set_variable(self, name, new_value):
        self.__variables[name] = new_value

    def return_to_previous_state(self):
        if len(self.__chain_states) > 1:
            self.__chain_states.pop(len(self.__chain_states) - 1)
            self.__complete_chain_states.append(self.__chain_states[len(self.__chain_states) - 1])
            self.__current_state = list(self.__chain_states[len(self.__chain_states) - 1].keys())[0]
            self.__enter_current_state()
        else:
            print('DEBUG: Cannot go back from initial state ' + self.__initial + '.')

    def trigger(self, event):
        if event in self.__states[self.__current_state]['on']:
            self.__transition(self.__states[self.__current_state]['on'][event]['target'])
        else:
            print('SKIPPED: ' + event + ' triggered in state: ' + self.__current_state + '. No matching event.')

    def __handle_sniffer(self):
        def pkt_callback(packet):
            if 'TCP' in packet:
                self.__variables[self.__sniffer_stack].append(packet)
        return pkt_callback

    def __transition(self, state):
        if state in self.__states:
            self.__exit_current_state()
            self.__current_state = state
            self.__complete_chain_states.append({self.__current_state: hashlib.sha256(repr(time.time()).encode()).hexdigest()})
            self.__chain_states.append(self.__complete_chain_states[len(self.__complete_chain_states) - 1])
            self.__enter_current_state()

    def __enter_current_state(self):
        if 'entry' in self.__states[self.__current_state]:
            for action in get_safe_array(self.__states[self.__current_state]['entry']):
                ActionInterpreter(self).onecmd(action)

    def __exit_current_state(self):
        if 'exit' in self.__states[self.__current_state]:
            for action in get_safe_array(self.__states[self.__current_state]['exit']):
                ActionInterpreter(self).onecmd(action)