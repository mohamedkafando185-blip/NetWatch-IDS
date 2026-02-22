from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "logs", "ids.log")
REPORT_FILE = os.path.join(BASE_DIR, "rapport_ids.txt")


def parse_log_line(line):
    """Transforme une ligne de log en tuple exploitable."""
    parts = line.strip().split(" | ")
    if len(parts) < 4:
        return None
    timestamp, event_type, src_part, dst_part = parts[:4]
    src = src_part.split("=", 1)[1]
    dst = dst_part.split("=", 1)[1]
    extra = parts[4] if len(parts) > 4 else ""
    return timestamp, event_type, src, dst, extra


def main():
    events = []

    if not os.path.exists(LOG_FILE):
        print(f"Aucun log trouvé ({LOG_FILE}). Lance d'abord mini_ids.py.")
        return

    # Lecture du log
    with open(LOG_FILE, "r") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                events.append(parsed)

    # Génération du rapport
    with open(REPORT_FILE, "w") as f:
        f.write("=" * 70 + "\n")
        f.write("RAPPORT IDS - INCIDENTS DÉTECTÉS\n")
        f.write("=" * 70 + "\n")
        f.write(f"Date de génération : {datetime.now()}\n\n")

        if not events:
            f.write("Aucun incident détecté.\n")
            return

        f.write(f"Total incidents : {len(events)}\n\n")
        f.write("-" * 70 + "\n")

        for ts, etype, src, dst, extra in events:
            f.write(f"[{ts}] {etype}\n")
            f.write(f"  Source : {src}\n")
            f.write(f"  Cible  : {dst}\n")
            f.write(f"  Détails: {extra}\n")
            f.write("-" * 70 + "\n")

    print(f"Rapport généré : {REPORT_FILE}")


if __name__ == "__main__":
    main()
