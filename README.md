# SDN Firewall using POX and Mininet

## Objective
This project blocks traffic from h1 to h3 using POX SDN controller.

## Topology
Single switch with 3 hosts.

## Test Cases
1. h1 ping h2 -> success
2. h1 ping h3 -> blocked

## Performance
Ping latency + flow statistics

## Tools Used
- Ubuntu VM
- Mininet
- POX
- Open vSwitch

## Screenshots

### Allowed Ping
![Allowed Ping](allowed_ping.png)

### Blocked Ping
![Blocked Ping](blocked_ping.png)

### Flow Table
![Flow Table](flow_table.png)

### Controller Logs
![Controller Logs](controller_logs.png)

###topology_and_ping.png
![topology_and_ping](topology_and_ping.png)

