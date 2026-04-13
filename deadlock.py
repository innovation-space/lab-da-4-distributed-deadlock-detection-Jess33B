import random

message_count = 0

class Process:
    def __init__(self, pid, site, log):
        self.pid = pid
        self.site = site
        self.waiting_for = []
        self.log = log

    def add_dependency(self, other):
        self.waiting_for.append(other)
        self.log.append(
            f"[EDGE] P{self.pid} (Site {self.site}) → waits for → P{other.pid} (Site {other.site})"
        )


# -------------------------
# DISTRIBUTED PROBE SYSTEM
# -------------------------

def send_probe(initiator, sender, receiver, visited, log):
    global message_count

    message_count += 1
    log.append(
        f"[PROBE] (Initiator=P{initiator.pid}) P{sender.pid} (Site {sender.site}) → P{receiver.pid} (Site {receiver.site})"
    )

    # DEADLOCK condition
    if receiver.pid == initiator.pid:
        log.append(f"[CYCLE] Probe returned to P{initiator.pid} → DEADLOCK")
        return True

    if receiver in visited:
        return False

    visited.add(receiver)

    # Forward probe
    for next_proc in receiver.waiting_for:
        if send_probe(initiator, receiver, next_proc, visited, log):
            return True

    return False


def detect_deadlock(processes, log):
    global message_count
    message_count = 0

    for p in processes:
        visited = set()
        log.append(f"\n[START DETECTION] Initiator = P{p.pid}")

        for neighbor in p.waiting_for:
            if send_probe(p, p, neighbor, visited, log):
                return True, message_count

    return False, message_count