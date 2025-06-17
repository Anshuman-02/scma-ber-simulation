# 📶 SCMA BER Simulation in 5G using Python

This project simulates the **Bit Error Rate (BER)** of **Sparse Code Multiple Access (SCMA)** — a key non-orthogonal multiple access technique proposed for 5G networks. The simulation evaluates how signal-to-noise ratio (SNR) affects the BER using custom-designed SCMA codebooks and noise models.

---

## 📚 Background

**Sparse Code Multiple Access (SCMA)** is a code-domain NOMA technique where user data is mapped to sparse codewords spread across multiple carriers. It offers:
- High spectral efficiency
- Low complexity decoding
- Better performance in crowded wireless environments

This simulation demonstrates the BER variation with SNR using Python and NumPy.

---

## 💡 Features

- Custom SCMA codebook generation
- Encoding and decoding of sparse codewords
- Noise simulation with varying SNR
- BER calculation for each user
- Graphical plot of BER vs SNR

---

## 🧪 How to Run

### 🛠 Requirements
- Python 3.7+
- NumPy
- Matplotlib

### ▶️ Run the Simulation

```bash
python scma_ber_simulation.py
```
This will generate a BER vs SNR plot.


---

### 📈 Output
The final output is a graph showing Bit Error Rate (BER) vs Signal-to-Noise Ratio (SNR). This helps visualize the performance of SCMA encoding and decoding under various noise levels.
