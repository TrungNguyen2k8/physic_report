import matplotlib.pyplot as plt
import numpy as np

# Cấu hình phông chữ Times New Roman và bộ ký hiệu toán học chuẩn LaTeX (STIX)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['mathtext.fontset'] = 'stix'

# Khởi tạo dữ liệu 12 bậc thang (mỗi bậc 0.15m)
steps = np.arange(0, 13)
heights = steps * 0.15

fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

# 1. Vẽ đường bậc thang và tô màu vùng dưới
ax.step(steps, heights, where='pre', color='#1B365D', linewidth=2.2, zorder=3)
ax.fill_between(steps, heights, step='pre', color='#E6F2FF', alpha=0.6, zorder=2)

# 2. Mũi tên nét đứt màu cam (Quỹ đạo khối tâm)
ax.annotate('', xy=(11.8, 1.92), xytext=(0.4, 0.22),
            arrowprops=dict(arrowstyle='->', color='#D95319', lw=2, ls='--'), zorder=4)

# 3. Khung chữ thông số vật lý (Chuẩn LaTeX: biến in nghiêng, đơn vị in đứng)
bbox_orange = dict(boxstyle='round,pad=0.45', facecolor='white', edgecolor='#337AB7', lw=1)
text_box_3 = (
    "Center of Mass Ascent Trajectory\n"
    r"$m = 68.50\,\mathrm{kg},\ g = 9.80\,\mathrm{m/s^2}$" + "\n"
    r"Gravitational Force: $P = mg = 671.30\,\mathrm{N}$"
)
ax.text(3.8, 1.7, text_box_3,
        fontsize=9.5, fontweight='bold', color='#1B365D', ha='center', va='center',
        rotation=0, bbox=bbox_orange, zorder=5)

# 4. Khung chữ nền xanh đậm phía trên (Dùng \mathbf cho công thức in đậm trên nền tối)
bbox_dark = dict(boxstyle='round,pad=0.45', facecolor='#1B365D', edgecolor='none')
text_box_4 = r"MECHANICAL WORK: $\mathbf{W = Ph = 1,208.34\,\mathrm{J}}$"
ax.text(3.8, 1.95, text_box_4,
        fontsize=9.5, fontweight='bold', color='white', ha='center', va='center',
        bbox=bbox_dark, zorder=5)

# 5. Mũi tên 2 đầu màu xanh ngọc bên phải
ax.annotate('', xy=(12.6, 1.80), xytext=(12.6, 0.0),
            arrowprops=dict(arrowstyle='<->', color='#179E86', lw=2), zorder=4)
ax.text(12.9, 0.9, r"$h = 1.80\,\mathrm{m}$",
        fontsize=10.5, fontweight='bold', color='#179E86', va='center')

# 6. Định dạng trục và lưới
ax.set_xlabel(r"Step Number ($1 \rightarrow 12$)", fontsize=10.5, fontweight='bold', color='#1B365D')
ax.set_ylabel(r"Height, $h$ ($\mathrm{m}$)", fontsize=10.5, fontweight='bold', color='#1B365D')

ax.set_xlim(-0.5, 15)
ax.set_ylim(-0.08, 2.15)
ax.set_xticks(np.arange(0, 16, 1))
ax.set_yticks(np.arange(0.0, 2.15, 0.3))
ax.tick_params(axis='both', which='major', labelsize=9.5)

ax.grid(True, linestyle=':', alpha=0.5, color='#B0B0B0', zorder=1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# Xuất file PNG nét cao hoặc SVG (vector không vỡ nét khi zoom trong Word)
plt.savefig('staircase_schematic.svg', format='svg', bbox_inches='tight')
plt.savefig('staircase_schematic.png', dpi=300, bbox_inches='tight')