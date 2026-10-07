import matplotlib.pyplot as plt
import numpy as np

# Set global publication styling
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Comparative Cryptographic Benchmark: Proposed Quantum-OTP vs. Standard Paradigms', 
             fontsize=14, fontweight='bold', y=0.98)

algorithms = ['LCG (PRNG)', 'RSA-2048', 'AES-256', 'Proposed Q-OTP']
colors = ['#b0bec5', '#ef5350', '#ffa726', '#2e7d32']

# -------------------------------------------------------------------------
# Subplot 1: Shannon Entropy (Max theoretical = 8.0)
# -------------------------------------------------------------------------
entropy_values = [7.124, 7.942, 7.982, 7.9995]
bars1 = axs[0, 0].bar(algorithms, entropy_values, color=colors, width=0.55, edgecolor='#222222')
axs[0, 0].axhline(8.0, color='black', linestyle='--', linewidth=1.2, label='Theoretical Ceiling (8.0)')
axs[0, 0].set_ylim(6.5, 8.15)
axs[0, 0].set_ylabel('Shannon Entropy (bits/byte)', fontweight='bold')
axs[0, 0].set_title('(a) Ciphertext Randomness Uniformity', fontweight='bold', pad=10)
axs[0, 0].legend(loc='lower left')
axs[0, 0].grid(axis='y', linestyle=':', alpha=0.6)

for bar in bars1:
    yval = bar.get_height()
    axs[0, 0].text(bar.get_x() + bar.get_width()/2.0, yval + 0.02, f'{yval:.4f}', 
                   ha='center', va='bottom', fontsize=9, fontweight='bold')

# -------------------------------------------------------------------------
# Subplot 2: NIST SP 800-22 Test Suite Pass Rate (%)
# -------------------------------------------------------------------------
nist_pass_rates = [46.7, 80.0, 93.3, 100.0]
bars2 = axs[0, 1].bar(algorithms, nist_pass_rates, color=colors, width=0.55, edgecolor='#222222')
axs[0, 1].set_ylim(0, 115)
axs[0, 1].set_ylabel('NIST SP 800-22 Pass Rate (%)', fontweight='bold')
axs[0, 1].set_title('(b) Cryptographic Randomness Compliance', fontweight='bold', pad=10)
axs[0, 1].grid(axis='y', linestyle=':', alpha=0.6)

for bar in bars2:
    yval = bar.get_height()
    axs[0, 1].text(bar.get_x() + bar.get_width()/2.0, yval + 2, f'{yval:.1f}%', 
                   ha='center', va='bottom', fontsize=9, fontweight='bold')

# -------------------------------------------------------------------------
# Subplot 3: Tamper Detection (FIXED: Zero-value indicators + Adjusted Legend)
# -------------------------------------------------------------------------
metrics = ['Accuracy', 'Precision', 'F1-Score']
x = np.arange(len(metrics))
width = 0.22

# Plot the 0-value bars with a slight bottom offset so outline is visible
bars_rsa = axs[1, 0].bar(x - width, [0.01, 0.01, 0.01], width, label='RSA-2048 (Raw)', 
                         color='#ffcdd2', edgecolor='#d32f2f', linestyle=':')
bars_aes = axs[1, 0].bar(x, [0.01, 0.01, 0.01], width, label='AES-256 (No MAC)', 
                         color='#ffe0b2', edgecolor='#f57c00', linestyle=':')
bars_prop = axs[1, 0].bar(x + width, [1.0, 1.0, 1.0], width, label='Proposed (SHA-256 Gate)', 
                          color='#2e7d32', edgecolor='#1b5e20')

axs[1, 0].set_ylim(0, 1.3)
axs[1, 0].set_xticks(x)
axs[1, 0].set_xticklabels(metrics, fontweight='bold')
axs[1, 0].set_ylabel('Verification Score (0.0 - 1.0)', fontweight='bold')
axs[1, 0].set_title('(c) Zero-Trust Tamper Detection Gate', fontweight='bold', pad=10)
axs[1, 0].legend(loc='upper right', framealpha=0.95)
axs[1, 0].grid(axis='y', linestyle=':', alpha=0.6)

# Explicit zero labels so the audience clearly sees they failed
for idx in x:
    axs[1, 0].text(idx - width, 0.04, '0.00\n(0%)', ha='center', va='bottom', 
                   fontsize=8, fontweight='bold', color='#c62828')
    axs[1, 0].text(idx, 0.04, '0.00\n(0%)', ha='center', va='bottom', 
                   fontsize=8, fontweight='bold', color='#ef6c00')
    axs[1, 0].text(idx + width, 1.03, '1.00\n(100%)', ha='center', va='bottom', 
                   fontsize=8, fontweight='bold', color='#1b5e20')

# -------------------------------------------------------------------------
# Subplot 4: Effective Security Bit-Strength Under Quantum Attack
# -------------------------------------------------------------------------
security_bits = [0, 0, 128, 256]
bars4 = axs[1, 1].bar(algorithms, security_bits, color=colors, width=0.55, edgecolor='#222222')
axs[1, 1].set_ylim(0, 300)
axs[1, 1].set_ylabel('Effective Security Strength (Bits)', fontweight='bold')
axs[1, 1].set_title('(d) Post-Quantum Computational Resistance', fontweight='bold', pad=10)
axs[1, 1].grid(axis='y', linestyle=':', alpha=0.6)

labels = ['0 (Broken)', '0 (Shor: Broken)', '128 (Grover: Halved)', r'$\infty$ (Perfect Secrecy)']
for bar, label in zip(bars4, labels):
    yval = bar.get_height()
    axs[1, 1].text(bar.get_x() + bar.get_width()/2.0, yval + 5, label, 
                   ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('quantum_cryptosystem_benchmarks.png', dpi=300)
plt.show()