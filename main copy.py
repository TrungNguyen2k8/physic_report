import matplotlib.pyplot as plt
import numpy as np

# Figure 2 ----------------------------------------------------
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['mathtext.fontset'] = 'stix'
steps = np.arange(0, 13)
heights = steps * 0.15
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
ax.step(steps, heights, where='pre', color='#1B365D', linewidth=2.2, zorder=3)
ax.fill_between(steps, heights, step='pre', color='#E6F2FF', alpha=0.6, zorder=2)
ax.annotate('', xy=(11.8, 1.92), xytext=(0.4, 0.22),
            arrowprops=dict(arrowstyle='->',color='#D95319', lw=2, ls='--'), zorder=4)
bbox_orange = dict(boxstyle='round,pad=0.45',
                   facecolor='white', edgecolor='#337AB7', lw=1)
text_box_3 = ("Center of Mass Ascent Trajectory\n"
    r"$m = 68.50\,\mathrm{kg},\ g = 9.80\,\mathrm{m/s^2}$" + "\n"
    r"Gravitational Force: $P = mg = 671.30\,\mathrm{N}$")
ax.text(3.8, 1.7, text_box_3,
        fontsize=9.5, fontweight='bold', color='#1B365D', ha='center', va='center',
        rotation=0, bbox=bbox_orange, zorder=5)
bbox_dark = dict(boxstyle='round,pad=0.45', facecolor='#1B365D', edgecolor='none')
text_box_4 = r"MECHANICAL WORK: $\mathbf{W = Ph = 1,208.34\,\mathrm{J}}$"
ax.text(3.8, 1.95, text_box_4,
        fontsize=9.5, fontweight='bold', color='white', ha='center', va='center',
        bbox=bbox_dark, zorder=5)
ax.annotate('', xy=(12.6, 1.80), xytext=(12.6, 0.0),
            arrowprops=dict(arrowstyle='<->', color='#179E86', lw=2), zorder=4)
ax.text(12.9, 0.9, r"$h = 1.80\,\mathrm{m}$",
        fontsize=10.5, fontweight='bold', color='#179E86', va='center')
ax.set_xlabel(r"Step Number ($1 \rightarrow 12$)", fontsize=10.5,
              fontweight='bold', color='#1B365D')
ax.set_ylabel(r"Height, $h$ ($\mathrm{m}$)", fontsize=10.5,
              fontweight='bold', color='#1B365D')
ax.set_xlim(-0.5, 15)
ax.set_ylim(-0.08, 2.15)
ax.set_xticks(np.arange(0, 16, 1))
ax.set_yticks(np.arange(0.0, 2.15, 0.3))
ax.tick_params(axis='both', which='major', labelsize=9.5)
ax.grid(True, linestyle=':', alpha=0.5, color='#B0B0B0', zorder=1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('staircase_schematic.svg', format='svg', bbox_inches='tight')
plt.savefig('staircase_schematic.png', dpi=300, bbox_inches='tight')

# Figure 3 ----------------------------------------------------
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.9
regimes = [    'Walk Regime\n($t_{\\mathrm{avg}} = 7.812\\,\\mathrm{s}$)',
    'Run Regime\n($t_{\\mathrm{avg}} = 3.774\\,\\mathrm{s}$)',]
work_values = [1208.34, 1208.34]
power_means = [154.68, 320.17]
power_sds = [1.81, 28.20]
specific_powers = [2.26, 4.67]  # Đã sửa từ 4.70 thành 4.67 W/kg
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
ax1.axhline(
    y=1208.34,
    color='#dd6b20',
    linestyle='--',
    linewidth=1.8,
    zorder=4,
    label='Constant $W = mgh = 1208.34\\,\\mathrm{J}$',
)
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

# Figure 4 ----------------------------------------------------
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

# Figure 5 ----------------------------------------------------
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.9
trials = ['Trial 1', 'Trial 2', 'Trial 3', 'Trial 4', 'Trial 5']
x = np.arange(len(trials))
walk_time = [7.68, 7.85, 7.80, 7.93, 7.80]
run_time = [3.28, 3.67, 3.99, 3.93, 4.00]
walk_time_mean = 7.812
run_time_mean = 3.774
timing_error = 0.10
walk_power = [157.34, 153.93, 154.92, 152.38, 154.92]
run_power = [368.40, 329.25, 302.84, 307.47, 302.48]
walk_power_mean = 154.68
run_power_mean = 320.17
fig1, ax1 = plt.subplots(figsize=(7.2, 4.8), dpi=300)
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
ax1.axhline(
    walk_time_mean, color='#1f618d', linestyle=':', linewidth=1.3, alpha=0.75
)
ax1.axhline(
    run_time_mean, color='#d35400', linestyle=':', linewidth=1.3, alpha=0.75
)
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

# Figure 6 ----------------------------------------------------
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
ax2.axhline(
    walk_power_mean, color='#1f618d', linestyle='--', linewidth=1.2, alpha=0.75
)
ax2.axhline(
    run_power_mean, color='#d35400', linestyle='--', linewidth=1.2, alpha=0.75
)
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