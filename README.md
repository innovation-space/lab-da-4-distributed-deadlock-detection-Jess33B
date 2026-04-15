
# Distributed Deadlock Detection — Wait-For Graph

> **Course:** Distributed Systems Lab &nbsp;|&nbsp; **Lab:** DA-4 — Distributed Deadlock Detection  
> **Due:** 15th April 2026

---

## Overview

This project simulates **distributed deadlock detection** using the **Wait-For Graph (WFG)** model and a **probe-based edge-chasing algorithm**, built with Python, SimPy, and Streamlit.

Processes are distributed across multiple sites. Each site maintains a local Wait-For Graph. Deadlocks — represented as cycles spanning distributed processes — are detected by passing probe messages across sites.

---

## How It Works

### Wait-For Graph (WFG)

Each node in the graph represents a process. A directed edge from `Pi → Pj` means **process Pi is waiting for process Pj** to release a resource.

A **deadlock** occurs when there is a cycle in this graph, for example:

```
P1 → P2 → P3 → P1
```

### Edge-Chasing (Probe) Algorithm

Detection uses a probe message of the form `Probe(initiator, sender, receiver)`:

1. A process initiates a probe to each of its dependents
2. Each receiving process forwards the probe to its own dependents
3. If the probe returns to the **initiating process**, a cycle is confirmed → **deadlock detected**

Each forwarded probe is counted as one message, reflecting real distributed communication overhead.

---

## Project Structure

```
deadlock-sim/
│
├── app.py            # Streamlit UI — controls, metrics, execution log
├── deadlock.py       # Core logic — WFG construction, probe algorithm
├── simulation.py     # Simulation controller — SimPy environment, process setup
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## Technologies

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| SimPy | Discrete-event simulation environment |
| Streamlit | Interactive web UI |

---

## Setup & Running

### 1. Clone the repository

```bash
git clone https://github.com/innovation-space/lab-da-4-distributed-deadlock-detection-Jess33B.git
cd lab-da-4-distributed-deadlock-detection-Jess33B
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

### 4. Open in browser

```
http://localhost:8501
```

---

## Usage

1. Use the **slider** to select the number of processes (3–10)
2. Click **Run Simulation**
3. View the results:
   - **Metrics panel** — process count and total probe messages sent
   - **Execution log** — step-by-step trace of edges, probes, cycles, and the final result

---

## System Model

- Processes are randomly assigned to one of **3 sites**
- Each process gets **1–2 random outgoing edges** (wait-for dependencies)
- Detection is initiated from every process; the first cycle found halts the search
- All probe forwards are counted as messages, measuring communication cost

---

## Sample Output

### Deadlock detected

```
[EDGE] P0 (Site 2) → waits for → P2 (Site 1)
[EDGE] P2 (Site 1) → waits for → P3 (Site 3)
[EDGE] P3 (Site 3) → waits for → P0 (Site 2)

--- WAIT-FOR GRAPH BUILT ---

[START DETECTION] Initiator = P0
[PROBE] (Initiator=P0) P0 (Site 2) → P2 (Site 1)
[PROBE] (Initiator=P0) P2 (Site 1) → P3 (Site 3)
[PROBE] (Initiator=P0) P3 (Site 3) → P0 (Site 2)
[CYCLE] Probe returned to P0 → DEADLOCK

--- RESULT ---
DEADLOCK DETECTED
```

### No deadlock

```
--- RESULT ---
NO DEADLOCK
```

---

## Message Complexity

| Scenario | Approx. Messages |
|---|---|
| No cycle found | O(E) where E = number of edges |
| Cycle found early | Fewer messages (halts on first cycle) |
| Dense graph | Higher message count |

Total probe messages are displayed in the UI after each run.

---

## Key Concepts

**Why is distributed deadlock detection hard?**  
In a centralised system, a single coordinator can inspect the full graph. In a distributed system, no single node has a global view — processes must cooperate by passing messages. This makes detection inherently more complex and costlier in communication.

**Why edge-chasing?**  
The probe-based approach is decentralised: any process can initiate detection, and no coordinator is needed. It scales naturally with the number of processes and sites.

---

## Repository

```
https://github.com/innovation-space/lab-da-4-distributed-deadlock-detection-Jess33B.git
```

---

## Submission Checklist

- [ ] Push all files to GitHub
- [ ] Paste repository link for evaluation
- [ ] Record and submit video walkthrough
- [ ] Upload PDF version of this README to VTOP

---

## Conclusion

This project demonstrates a practical implementation of distributed deadlock detection using the Wait-For Graph model and edge-chasing probe algorithm. It highlights the communication overhead inherent in distributed coordination and the challenge of detecting global conditions (cycles) without a centralised view.
