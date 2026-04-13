import simpy
import random
import deadlock

def run_simulation(n):

    env = simpy.Environment()
    log = []

    NUM_SITES = 3

    # Create processes distributed across sites
    processes = []
    for i in range(n):
        site = random.randint(1, NUM_SITES)
        processes.append(deadlock.Process(i, site, log))

    # Create dependencies (Wait-For Graph)
    for p in processes:
        num_edges = random.randint(1, 2)

        for _ in range(num_edges):
            other = random.choice(processes)
            if other != p:
                p.add_dependency(other)

    log.append("\n--- WAIT-FOR GRAPH BUILT ---\n")

    # Run detection
    deadlock_found, message_count = deadlock.detect_deadlock(processes, log)

    log.append("\n--- RESULT ---")

    if deadlock_found:
        log.append("DEADLOCK DETECTED")
    else:
        log.append("NO DEADLOCK")

    return log, message_count