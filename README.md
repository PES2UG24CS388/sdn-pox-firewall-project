# SDN Path Tracing Tool using POX and Mininet

## Problem Statement
Identify and display the path taken by packets in an SDN network. Track flow rules, identify forwarding path, display route, and validate using tests.

## Tools Used
- Mininet
- POX Controller
- Open vSwitch
- Ubuntu

## Setup Steps
1. Install Mininet and POX
2. Run POX controller:
   ./pox.py log.level --DEBUG openflow.of_01 misc.firewall_controller
3. Run Mininet:
   sudo mn --topo single,3 --mac --switch ovsk --controller remote,ip=127.0.0.1,port=6633

## Functionality
- Controller handles PacketIn events
- Installs flow rules dynamically
- Displays packet path in logs
- Blocks specific traffic (h1 → h3)

## Test Cases

### Test 1: Allowed Traffic
h1 ping h2 → Success

### Test 2: Blocked Traffic
h1 ping h3 → 100% Packet Loss

## Output
- Packet path displayed in controller
- Flow rules visible in switch
- Network behavior validated using ping

## Screenshots
(Add images here)
