from scapy.all import sniff, IP, TCP, ICMP
from collections import defaultdict
from datetime import datetime
import time
import os

# Compteurs par IP source
icmp_count = defaultdict(int)
tcp_syn_count = defaultdict(int)

# Paramètres de détection
WINDOW = 60          # fenêtre en secondes
TH_ICMP = 5          # seuil ICMP (tests)
TH_SYN  = 5          # seuil SYN (tests)

start_time = time.time()

# Fichier de log
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, logs, ids.log)


def log_event(event_type, src, dst, extra=)
    Écrit une alerte dans le fichier de log + affiche en console.
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    timestamp = datetime.now().strftime(%Y-%m-%d %H%M%S)
    line = f{timestamp}  {event_type}  src={src}  dst={dst}  {extra}n
    print(line.strip())
    with open(LOG_FILE, a) as f
        f.write(line)


def analyse(pkt)
    Analyse chaque paquet capturé et met à jour les compteurs.
    global start_time, icmp_count, tcp_syn_count

    now = time.time()

    # Réinitialiser les compteurs après WINDOW secondes
    if now - start_time  WINDOW
        icmp_count = defaultdict(int)
        tcp_syn_count = defaultdict(int)
        start_time = now

    if IP not in pkt
        return

    src = pkt[IP].src
    dst = pkt[IP].dst

    # --- Détection ping flood (ICMP) ---
    if ICMP in pkt
        icmp_count[src] += 1
        print(f[ICMP] {src} - {dst} (total={icmp_count[src]}))
        if icmp_count[src] == TH_ICMP
            log_event(ICMP_FLOOD, src, dst, fcount={icmp_count[src]})

    # --- Détection scan de ports (TCP SYN) ---
    if TCP in pkt
        flags = pkt[TCP].flags
        # Bit SYN actif 
        if flags & 0x02
            tcp_syn_count[src] += 1
            print(f[SYN] {src} - {dst} (total={tcp_syn_count[src]}))
            if tcp_syn_count[src] == TH_SYN
                log_event(PORT_SCAN_SUSPECT, src, dst,
                          fsyn_count={tcp_syn_count[src]})


if __name__ == __main__
    # Si besoin, remplace iface par ton interface (ex eth0)
    sniff(prn=analyse, store=0)
