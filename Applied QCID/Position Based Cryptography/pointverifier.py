"""
Qiskit Code for Position-Verification in the No Pre-shared Entanglement (No-PE) Model
Author: Rohan Singh
"""



# imports
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
import numpy as np



def position_verification():

    qc = QuantumCircuit(1, 1)
    
    # step 1
    x = np.random.randint(2)  # random bit
    theta = np.random.randint(2)  # random basis

    # setting the qubit to |1> if x is |1>
    if x == 1:
        qc.x(0)
    
    qc.barrier()

    # step 2
    # applying H^theta on x
    if theta == 1:
        qc.h(0)  
    qc.barrier()
    
    # step 3
    # doesn't need to be done bcuz of teleoprtation
    #qc.measure(0, 0)  
    #qc.barrier()
    
    # step 4
    # measuring it in the basis of theta
    if theta == 1:
        qc.h(0)
    qc.measure(0, 0)
    
    # simulating the circuit
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1).result()
    counts = result.get_counts(qc)

    # printing the circuit
    print(qc)
    
    # verifying the results
    x_prime = int(list(counts.keys())[0])
    print(f"measured: {x_prime}")
    print(f"actual: {x}")
    if x_prime == x:
        print("Verification successful :)")
    else:
        print("Verification failed :/")




# main function to run the protocol
def main():
    for _ in range(10):
        position_verification()


if __name__ == "__main__":
    main()
