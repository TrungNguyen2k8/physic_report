import matplotlib.pyplot as plt
import numpy as np

# Cấu hình phông chữ và đường viền chuẩn báo cáo khoa học
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.9

# Dữ liệu 5 lần thử khớp 100% với bảng số liệu trong báo cáo
trials = ['Trial 1', 'Trial 2', 'Trial 3', 'Trial 4', 'Trial 5']
x = np.arange(len(trials))

# Thời gian (s) và sai số bấm giờ phản xạ (±0.10 s)
walk_time = [7.68, 7.85, 7.80, 7.93, 7.80]
run_time = [3.28, 3.67, 3.99, 3.93, 4.00]
walk_time_mean = 7.812
run_time_mean = 3.774
timing_error = 0.10

# Công suất (W) - Đã sửa Trial 5 của Run thành 302.48 W và Mean thành 154.68 W / 320.17 W
walk_power = [157.34, 153.93, 154.92, 152.38, 154.92]
run_power = [368.40, 329.25, 302.84, 307.47, 302.48]
walk_power_mean = 154.68
run_power_mean = 320.17

# ==========================================================
# HÌNH 1 (FIGURE 5): COMPLETION TIME ACROSS 5 TRIALS
# ==========================================================
fig1, ax1 = plt.subplots(figsize=(7.2, 4.8), dpi=300)

# Vẽ đường biểu diễn kèm thanh sai số ±0.10 s
ax1.errorbar(
    x,
    walk_time,
    yerr=timing_error,
    fmt='-o',
    color='#1f618d',
    linewidth=2.2,
    markersize=7,
    capsize=4,
    elinewidth=1.3,
    label='Walk (Mean: $7.812\\,\\mathrm{s}$, $\\mathrm{CV} = 1.16\\%$)',
    zorder=4,
)
ax1.errorbar(
    x,
    run_time,
    yerr=timing_error,
    fmt='-s',
    color='#d35400',
    linewidth=2.2,
    markersize=7,
    capsize=4,
    elinewidth=1.3,
    label='Run (Mean: $3.774\\,\\mathrm{s}$, $\\mathrm{CV} = 8.13\\%$)',
    zorder=4,
)

# Đường trung bình nét chấm
ax1.axhline(
    walk_time_mean, color='#1f618d', linestyle=':', linewidth=1.3, alpha=0.75
)
ax1.axhline(
    run_time_mean, color='#d35400', linestyle=':', linewidth=1.3, alpha=0.75
)

# Gắn nhãn số liệu từng điểm
for i, txt in enumerate(walk_time):
  ax1.text(
      x[i],
      walk_time[i] + 0.22,
      f'{txt:.2f} s',
      ha='center',
      va='bottom',
      fontsize=9,
      fontweight='bold',
      color='#1a365d',
  )

for i, txt in enumerate(run_time):
  ax1.text(
      x[i],
      run_time[i] - 0.26,
      f'{txt:.2f} s',
      ha='center',
      va='top',
      fontsize=9,
      fontweight='bold',
      color='#9c2b1b',
  )

# Hộp chú thích xu hướng mỏi cơ (Fatigue Trend)
ax1.annotate(
    'Progressive Fatigue Trend\n($3.28\\,\\mathrm{s} \\rightarrow'
    ' 4.00\\,\\mathrm{s}$, $+22.0\\%$ time)',
    xy=(2, 3.99),
    xytext=(1.9, 5.45),
    ha='center',
    va='center',
    fontsize=9,
    fontweight='bold',
    color='#9c2b1b',
    bbox=dict(
        boxstyle='round,pad=0.4',
        facecolor='#fffaf0',
        edgecolor='#d35400',
        linewidth=1.2,
    ),
    arrowprops=dict(arrowstyle='->', color='#d35400', lw=1.6),
)

ax1.set_title(
    'Completion Time Across 5 Trials ($\\pm 0.10\\,\\mathrm{s}$ Timing Error)\n'
    'High Repeatability in Walk vs. Progressive Slowing in Run',
    fontsize=11.5,
    fontweight='bold',
    color='#1a365d',
    pad=12,
)
ax1.set_ylabel(
    'Completion Time, $t_i$ (s)',
    fontsize=10.5,
    fontweight='bold',
    color='#2d3748',
)
ax1.set_xticks(x)
ax1.set_xticklabels(trials, fontsize=10, fontweight='bold')
ax1.set_ylim(2.2, 9.2)
ax1.grid(True, linestyle='-', alpha=0.25)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.legend(loc='upper right', frameon=True, fontsize=9.5)

plt.tight_layout()
plt.savefig('Figure_5_Trial_Time.png', dpi=300)

# ==========================================================
# HÌNH 2 (FIGURE 6): MECHANICAL POWER OUTPUT ACROSS 5 TRIALS
# ==========================================================
fig2, ax2 = plt.subplots(figsize=(7.2, 4.8), dpi=300)

ax2.plot(
    x,
    walk_power,
    '-o',
    color='#1f618d',
    linewidth=2.2,
    markersize=7,
    label=(
        'Walk (Mean $P_{\\mathrm{avg}} = 154.68\\,\\mathrm{W} \\pm'
        ' 1.81\\,\\mathrm{W}$)'
    ),
    zorder=4,
)
ax2.plot(
    x,
    run_power,
    '-s',
    color='#d35400',
    linewidth=2.2,
    markersize=7,
    label=(
        'Run (Mean $P_{\\mathrm{avg}} = 320.17\\,\\mathrm{W} \\pm'
        ' 28.20\\,\\mathrm{W}$)'
    ),
    zorder=4,
)

# Đường trung bình nét đứt
ax2.axhline(
    walk_power_mean, color='#1f618d', linestyle='--', linewidth=1.2, alpha=0.75
)
ax2.axhline(
    run_power_mean, color='#d35400', linestyle='--', linewidth=1.2, alpha=0.75
)

# Gắn nhãn số liệu từng điểm (hiển thị chuẩn 302.5 W ở Trial 5)
for i, val in enumerate(walk_power):
  ax2.text(
      x[i],
      walk_power[i] + 7,
      f'{val:.1f} W',
      ha='center',
      va='bottom',
      fontsize=9,
      fontweight='bold',
      color='#1a365d',
  )

for i, val in enumerate(run_power):
  offset = -16 if i == 0 else 9
  ax2.text(
      x[i],
      run_power[i] + offset,
      f'{val:.1f} W',
      ha='center',
      va='bottom',
      fontsize=9,
      fontweight='bold',
      color='#9c2b1b',
  )

# Hộp chú thích sự suy giảm công suất do cạn kiệt ATP-CP
ax2.annotate(
    'Peak Output in Trial 1: $368.40\\,\\mathrm{W}$\nPlateaus at'
    ' $\\sim\\!302.5\\,\\mathrm{W}$ in Trials 3–5 ($-17.9\\%$)',
    xy=(0, 368.40),
    xytext=(1.9, 400),
    ha='center',
    va='center',
    fontsize=9,
    fontweight='bold',
    color='#9c2b1b',
    bbox=dict(
        boxstyle='round,pad=0.4',
        facecolor='#fffaf0',
        edgecolor='#d35400',
        linewidth=1.2,
    ),
    arrowprops=dict(arrowstyle='->', color='#d35400', lw=1.6),
)

ax2.set_title(
    'Trial-by-Trial Mechanical Power Output ($P_i = W / t_i$)\nAcute'
    ' Phosphocreatine (ATP-CP) Depletion Signature in Running',
    fontsize=11.5,
    fontweight='bold',
    color='#1a365d',
    pad=12,
)
ax2.set_ylabel(
    'Mechanical Power, $P_i$ (W)',
    fontsize=10.5,
    fontweight='bold',
    color='#2d3748',
)
ax2.set_xticks(x)
ax2.set_xticklabels(trials, fontsize=10, fontweight='bold')
ax2.set_ylim(115, 445)
ax2.grid(True, linestyle='-', alpha=0.25)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.legend(loc='lower right', frameon=True, fontsize=9.5)

plt.tight_layout()
plt.savefig('Figure_6_Trial_Power.png', dpi=300)