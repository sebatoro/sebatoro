
switch1_native_vlan = int(input("Ingrese la VLAN nativa del switch1: "))
switch1_vlans_str = input("Ingrese las VLANs del switch1 separadas por comas: ")
switch1_vlans = [int(vlan) for vlan in switch1_vlans_str.split(",")]


if switch1_native_vlan == switch1_vlans[0]:
    print("Las VLANs son iguales y cumplen con el requerimiento para el switch1.")
else:
    print("Las VLANs son diferentes y no cumplen con el requerimiento para el switch1.")


if switch1_native_vlan == 99:
    print("La VLAN nativa es igual a la VLAN nativa del switch1 según el diagrama.")
else:
    print("La VLAN nativa no es igual a la VLAN nativa del switch1 según el diagrama.")


required_vlans_switch1 = [10, 20, 30]
if set(switch1_vlans) == set(required_vlans_switch1):
    print("Las VLANs son iguales y cumplen con el requerimiento para el switch1.")
else:
    print("Las VLANs son diferentes y no cumplen con el requerimiento para el switch1.")


switch2_native_vlan = int(input("Ingrese la VLAN nativa del switch2: "))
switch2_vlans_str = input("Ingrese las VLANs del switch2 separadas por comas: ")
switch2_vlans = [int(vlan) for vlan in switch2_vlans_str.split(",")]


if switch2_native_vlan == switch2_vlans[0]:
    print("Las VLANs son iguales y cumplen con el requerimiento para el switch2.")
else:
    print("Las VLANs son diferentes y no cumplen con el requerimiento para el switch2.")


if switch2_native_vlan == 200:
    print("La VLAN nativa es igual a la VLAN nativa del switch2 según el diagrama.")
else:
    print("La VLAN nativa no es igual a la VLAN nativa del switch2 según el diagrama.")


required_vlans_switch2 = [40, 50, 60]
if set(switch2_vlans) == set(required_vlans_switch2):
    print("Las VLANs son iguales y cumplen con el requerimiento para el switch2.")
else:
    print("Las VLANs son diferentes y no cumplen con el requerimiento para el switch2.")