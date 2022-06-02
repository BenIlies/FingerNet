import argparse
import json

from scapy.all import *

from machine import Machine

#iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP 

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("scenario_file", help="JSON scenario file for the finite state machine", type=str)
  parser.add_argument("-v","--variables-file", help="JSON variables for the scenario", type=str)
  args = parser.parse_args()
  xstate_json = json.load(open(args.scenario_file))
  if args.variables_file:
    machine = Machine(xstate_json=xstate_json, variables=json.load(open(args.variables_file)))
  else:
    machine = Machine(xstate_json=xstate_json)
  machine.trigger('INITIALIZED')
  print(machine.current_state)