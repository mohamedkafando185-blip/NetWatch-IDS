from scapy.all import sniff, IP


def analyse(pkt):
    if IP in pkt:
        print(pkt[IP].src, "->", pkt[IP].dst)


if __name__ == "__main__":
    # Si besoin, ajoute iface="eth0" ou autre
    sniff(prn=analyse, store=0)
