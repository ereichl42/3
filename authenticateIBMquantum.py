from qiskit_ibm_runtime import QiskitRuntimeService
 
# Save an IBM Quantum account and set it as your default account.
QiskitRuntimeService.save_account(
    channel="ibm_quantum",
    token="f1a7609653080fcb7d44f505fedf34c6ef4c26fac498d1483701ab4b78ad1b714397022f34dc1d3ecfe319bc957548581c4df554c637496db14a80359fda005b",
    set_as_default=True,
    # Use `overwrite=True` if you're updating your token.
    overwrite=True,
)
 
# Load saved credentials
service = QiskitRuntimeService()
 