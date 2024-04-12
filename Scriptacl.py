aclnum = int(input("¿Cual es el numero de ACL IPv4? "))
if aclnum >= 1 and aclnum <=99:
    print("Esta es un ACL IPv4 estandar.")
elif aclnum >=100 and aclnum <=199:
    print("Esta es una ACL IPv4 extendida. ")
else:
    print("Esto no es una ACL IPV4 estandar o extendida")