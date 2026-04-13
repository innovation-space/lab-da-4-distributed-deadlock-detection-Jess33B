import streamlit as st
from simulation import run_simulation

st.set_page_config(page_title="Deadlock Detection", layout="centered")

st.title("Distributed Deadlock Detection (Wait-For Graph)")

st.markdown(
    "Simulation of distributed deadlock detection using a probe-based edge-chasing algorithm.\n\n"
    "Processes are distributed across multiple sites, each maintaining a local Wait-For Graph."
)

st.success("Deadlock occurs when a cycle exists across distributed processes.")

# Input
n = st.slider("Number of Processes", 3, 10, 5)

if st.button("Run Simulation"):

    log, message_count = run_simulation(n)

    # Metrics
    st.subheader("System Metrics")
    col1, col2 = st.columns(2)

    col1.metric("Processes", n)
    col2.metric("Probe Messages", message_count)

    st.markdown("---")

    st.info(
        "The edge-chasing algorithm sends probe messages across sites. "
        "If a probe returns to the initiating process, a cycle is detected."
    )

    st.subheader("Execution Log")

    for line in log:
        if "DEADLOCK DETECTED" in line:
            st.error("[RESULT] " + line)
        elif "NO DEADLOCK" in line:
            st.success("[RESULT] " + line)
        elif "[PROBE]" in line:
            st.write(line)
        elif "[EDGE]" in line:
            st.write(line)
        elif "[CYCLE]" in line:
            st.warning(line)
        elif "[START DETECTION]" in line:
            st.subheader(line)
        else:
            st.text(line)