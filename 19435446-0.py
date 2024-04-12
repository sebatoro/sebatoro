vlan = {
    "SW1": {"VLANs": [10, 20, 30], "Native_VLAN": 99},
    "SW2": {"VLANs": [40, 50, 60], "Native_VLAN": 200}
 }

print("VLAN-Switch:")
print() 
 
for switch, info in vlan.items():
    print("- Switch:", switch)
    print("  VLANS:", info["VLANs"])
    print("  Native VLAN:", info["Native_VLAN"])  
    print() 