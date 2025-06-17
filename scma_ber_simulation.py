import numpy as np
import matplotlib.pyplot as plt

def generate_codebook(N, M, L):
    codebook = np.zeros((N, M, L), dtype=int)
    for n in range(N):
        for m in range(M):
            indices = np.random.choice(L, size=M, replace=False)
            codebook[n, m, indices] = 1
    return codebook

def scma_encode(message, codebook):
    N, M, L = codebook.shape
    encoded_message = np.zeros((N,))
    for n in range(N):
        encoded_symbol = np.zeros((L,))
        for m in range(M):
            encoded_symbol += message[m] * codebook[n, m, :]
        encoded_message[n] = np.argmax(encoded_symbol)
    return encoded_message

def scma_decode(received_symbol, codebook):
    N, M, L = codebook.shape
    decoded_message = np.zeros((M,))
    for m in range(M):
        sum_correlations = np.zeros((L,))
        for n in range(N):
            sum_correlations += received_symbol[n] * codebook[n, m, :]
        decoded_message[m] = np.argmax(sum_correlations)
    return decoded_message

def calculate_ber(original_message, decoded_message):
    errors = np.sum(original_message != decoded_message)
    return errors / len(original_message)

# Parameters
N = 4   # Number of users
M = 3   # Number of bits per user
L = 8   # Length of codebook
SNR_values = np.arange(-5, 15, 2)  # SNR values for simulation

# Generate random message for each user
messages = np.random.randint(2, size=(N, M))

# Generate codebook
codebook = generate_codebook(N, M, L)

# Initialize BER array to store results
bers = np.zeros((len(SNR_values), N))

# Simulation loop
for i, snr in enumerate(SNR_values):
    for j in range(N):
        # Encode messages
        encoded_message = scma_encode(messages[j], codebook)

        # Simulate transmission (adding noise)
        noise_power = 10 ** (-snr / 10)
        received_symbol = encoded_message + np.random.normal(0, np.sqrt(noise_power), size=(N,))  

        # Decode received symbols
        decoded_message = scma_decode(received_symbol, codebook)

        # Calculate BER
        bers[i, j] = calculate_ber(messages[j], decoded_message)

# Average BER over all users
avg_ber = np.mean(bers, axis=1)

# Plot BER vs SNR
plt.figure()
plt.plot(SNR_values, avg_ber, marker='o')
plt.xlabel('SNR (dB)')
plt.ylabel('Bit Error Rate (BER)')
plt.title('Bit Error Rate vs Signal-to-Noise Ratio')
plt.grid(True)
plt.show()
