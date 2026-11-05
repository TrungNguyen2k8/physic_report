import matplotlib.pyplot as plt
import numpy as np

# Cấu hình font chữ chuẩn báo cáo khoa học
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.9

# Dữ liệu thực nghiệm chuẩn (đã hiệu chỉnh khớp 100% với Table 3)
regimes = [
    'Walk Regime\n($t_{\\mathrm{avg}} = 7.812\\,\\mathrm{s}$)',
    'Run Regime\n($t_{\\mathrm{avg}} = 3.774\\,\\mathrm{s}$)',
]
work_values = [1208.34, 1208.34]
power_means = [154.68, 320.17]
power_sds = [1.81, 28.20]
specific_powers = [2.26, 4.67]  # Đã sửa từ 4.70 thành 4.67 W/kg

# ==========================================
# TẠO FIGURE 3: GRAVITATIONAL POTENTIAL WORK
# ==========================================
fig3, ax1 = plt.subplots(figsize=(6.5, 4.8), dpi=300)

bars1 = ax1.bar(
    regimes,
    work_values,
    width=0.45,
    color=['#2b6cb0', '#009688'],
    edgecolor='#1a365d',
    linewidth=1.2,
    zorder=3,
)

# Đường nét đứt thể hiện công không đổi
ax1.axhline(
    y=1208.34,
    color='#dd6b20',
    linestyle='--',
    linewidth=1.8,
    zorder=4,
    label='Constant $W = mgh = 1208.34\\,\\mathrm{J}$',
)

# Nhãn số liệu trên đỉnh cột
for bar in bars1:
  yval = bar.get_height()
  ax1.text(
      bar.get_x() + bar.get_width() / 2.0,
      yval + 35,
      f'{yval:.2f} J\n(100%)',
      ha='center',
      va='bottom',
      fontsize=10,
      fontweight='bold',
      color='#1a365d',
  )

ax1.set_title(
    'Gravitational Potential Work ($W = mgh$)\nIdentical Mechanical Work Across'
    ' Walk & Run',
    fontsize=11.5,
    fontweight='bold',
    color='#1a365d',
    pad=14,
)
ax1.set_ylabel(
    'Mechanical Work, $W$ (Joules)',
    fontsize=10.5,
    fontweight='bold',
    color='#2d3748',
)
ax1.set_ylim(0, 1550)
ax1.grid(axis='y', linestyle=':', alpha=0.6, zorder=0)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(axis='x', labelsize=10)
ax1.legend(loc='upper right', frameon=True, fontsize=9.5)

plt.tight_layout()
plt.savefig('Figure_3_Mechanical_Work.png', dpi=300)
plt.show()

# ==========================================
# TẠO FIGURE 4: MECHANICAL POWER SURGE
# ==========================================
fig4, ax2 = plt.subplots(figsize=(6.5, 4.8), dpi=300)

bars2 = ax2.bar(
    regimes,
    power_means,
    yerr=power_sds,
    width=0.45,
    color=['#2b6cb0', '#dd5124'],
    edgecolor='#1a365d',
    linewidth=1.2,
    capsize=7,
    error_kw={'elinewidth': 1.6, 'ecolor': '#1a365d'},
    zorder=3,
)

# Nhãn chi tiết trên cột Walk
ax2.text(
    bars2[0].get_x() + bars2[0].get_width() / 2.0,
    power_means[0] + power_sds[0] + 12,
    f'{power_means[0]:.2f} W (±{power_sds[0]:.2f} W)\n'
    f'{specific_powers[0]:.2f} W/kg (Baseline 1.00×)',
    ha='center',
    va='bottom',
    fontsize=9.5,
    fontweight='bold',
    color='#1a365d',
)

# Nhãn chi tiết trên cột Run (đã sửa 4.67 W/kg)
ax2.text(
    bars2[1].get_x() + bars2[1].get_width() / 2.0,
    power_means[1] + power_sds[1] + 12,
    f'{power_means[1]:.2f} W (±{power_sds[1]:.2f} W)\n'
    f'{specific_powers[1]:.2f} W/kg (+107.0% / 2.07×)\n'
    '$p = 1.01 \\times 10^{-6}$',
    ha='center',
    va='bottom',
    fontsize=9.5,
    fontweight='bold',
    color='#9c2b1b',
)

ax2.set_title(
    'Mechanical Power Surge from Walk to Run\nMean Power $\\pm$ 1 SD (+107.0%,'
    ' $t(8) = 13.24$)',
    fontsize=11.5,
    fontweight='bold',
    color='#1a365d',
    pad=14,
)
ax2.set_ylabel(
    'Mean Mechanical Power, $P_{\\mathrm{avg}}$ (Watts)',
    fontsize=10.5,
    fontweight='bold',
    color='#2d3748',
)
ax2.set_ylim(0, 440)
ax2.grid(axis='y', linestyle=':', alpha=0.6, zorder=0)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.tick_params(axis='x', labelsize=10)

plt.tight_layout()
plt.savefig('Figure_4_Mechanical_Power.png', dpi=300)
plt.show()