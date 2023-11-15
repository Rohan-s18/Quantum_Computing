from PIL import Image
import numpy as np
from qiskit import QuantumCircuit, transpile, Aer, assemble
from qiskit.visualization import array_to_latex
from qiskit.visualization import plot_histogram

# Step 1: Read the RGB image file
image_path = '/Users/rohansingh/Desktop/baby_pic.png'  
image = Image.open(image_path)
image = image.resize((64, 64))  # Resizing the image to a manageable size

# Step 2: Converting the image into a quantum state using FRQI
"""
def rgb_to_quantum(image):
    data = np.array(image)
    qubits = QuantumCircuit(6)

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = data[i, j]
            normalized_pixel = [p / 255.0 for p in pixel]  # Normalize pixel values
            qubits.ry(normalized_pixel[0] * np.pi, i * 3)
            qubits.ry(normalized_pixel[1] * np.pi, i * 3 + 1)
            qubits.ry(normalized_pixel[2] * np.pi, i * 3 + 2)

    return qubits
"""


def rgb_to_quantum(image):
    data = np.array(image)
    qubits = QuantumCircuit(64)

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = data[i, j]
            normalized_pixel = [p / 255.0 for p in pixel]  # Normalize pixel values
            if i * image.size[1] + j < 8:  # Consider only the first 8 pixels for simplicity
                qubits.ry(normalized_pixel[0] * np.pi, (i * image.size[1] + j) * 3)
                qubits.ry(normalized_pixel[1] * np.pi, (i * image.size[1] + j) * 3 + 1)
                qubits.ry(normalized_pixel[2] * np.pi, (i * image.size[1] + j) * 3 + 2)

    return qubits



# Step 3: Apply compression techniques (example: applying Hadamard gates for simplicity)
def apply_compression(qc):
    for qubit in range(6):
        qc.h(qubit)
    return qc

# Step 4: Reconstructing the compressed quantum state
def reconstruct_compressed_state(qc):
    for qubit in range(6):
        qc.h(qubit)
    return qc


"""
# Step 5: Convert the compressed quantum state back into an RGB image
def quantum_to_rgb(qc, image_size):
    job = assemble(qc, backend=Aer.get_backend('statevector_simulator'))
    result = Aer.get_backend('statevector_simulator').run(job).result()
    statevector = result.get_statevector()

    reconstructed_image = np.zeros((image_size[0], image_size[1], 3), dtype=np.uint8)

    for i in range(image_size[0]):
        for j in range(image_size[1]):
            index = (i * image_size[0] + j) * 3
            pixel = statevector[index: index + 3]
            pixel = [int(round(p * 255)) for p in pixel]  # Convert back from normalized values
            reconstructed_image[i, j] = pixel

    return reconstructed_image
"""


def quantum_to_rgb(qc, image_size):
    job = assemble(qc, backend=Aer.get_backend('statevector_simulator'))
    result = Aer.get_backend('statevector_simulator').run(job).result()
    statevector = result.get_statevector()

    reconstructed_image = np.zeros((image_size[0], image_size[1], 3), dtype=np.uint8)

    for i in range(image_size[0]):
        for j in range(image_size[1]):
            index = (i * image_size[1] + j) * 3
            if index + 2 < len(statevector):
                pixel = statevector[index: index + 3]
                pixel = [int(round(p * 255)) for p in pixel]  # Convert back from normalized values
                reconstructed_image[i, j] = pixel

    return reconstructed_image




# Convert image to quantum state
quantum_state = rgb_to_quantum(image)

# Apply compression techniques

compressed_state = apply_compression(quantum_state)


# Reconstruct compressed state
reconstructed_state = reconstruct_compressed_state(compressed_state)

"""
# Convert compressed quantum state back to RGB image
reconstructed_image = quantum_to_rgb(reconstructed_state, image.size)


# Display reconstructed image
reconstructed_image = Image.fromarray(reconstructed_image)
reconstructed_image.show()
"""

print(compressed_state)
print("hello world")