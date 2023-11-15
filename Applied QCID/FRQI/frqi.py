from qiskit import QuantumCircuit, transpile, Aer, assemble
import numpy as np
from PIL import Image

def normalize_image(image_array):
    return image_array / 255.0  # Normalize pixel values to range [0, 1]

def encode_image(image_array, num_qubits):
    normalized_image = normalize_image(image_array)
    total_pixels = len(normalized_image)
    
    # Create a quantum circuit with the required number of qubits
    circuit = QuantumCircuit(num_qubits, num_qubits)
    
    for i, pixel_value in enumerate(normalized_image):
        # Encode each pixel value as an amplitude on the quantum state
        theta = 2 * np.arcsin(np.sqrt(pixel_value))
        circuit.ry(theta, i)
    
    return circuit

def decode_image(quantum_state, num_qubits):
    image_array = np.zeros(2 ** num_qubits)
    for i in range(2 ** num_qubits):
        # Measure the quantum state to extract amplitudes
        counts = quantum_state.data(i)["counts"]
        probability = counts / sum(counts.values())
        image_array[i] = probability
        
    # Reshape and scale the image array back to 0-255 range
    image_array = (image_array * 255).astype(np.uint8)
    image_side_length = int(np.sqrt(len(image_array)))
    image_array = image_array.reshape((image_side_length, image_side_length))
    return image_array

# Load an example image
image_path = '/Users/rohansingh/Desktop/baby_pic.png'   # Replace with your image path
original_image = np.array(Image.open(image_path).convert('L'))  # Convert to grayscale


num_pixels = original_image.size
num_qubits = int(np.ceil(np.log2(num_pixels)))+1


encoded_circuit = encode_image(original_image.flatten(), num_qubits)

# Simulate the quantum circuit to get the quantum state
simulator = Aer.get_backend('statevector_simulator')
job = assemble(transpile(encoded_circuit, simulator), backend=simulator)
quantum_state = simulator.run(job).result().get_statevector()

# Decode the quantum state back to an image
decoded_image = decode_image(quantum_state, num_qubits)

# Display the original and decoded images
original_image = Image.fromarray(original_image)
decoded_image = Image.fromarray(decoded_image)

# Displaying the images
original_image.show()
decoded_image.show()
