import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
import matplotlib.font_manager as fm

font_path = "/home/javad/B_NAZANIN/B-NAZANIN.TTF"
#plt.rcParams['font.family'] = 'B Nazanin'
font_prop = fm.FontProperties(fname=font_path, size=18)


# Winkler modulus values
Kw_values = [0, 4, 16, 36, 64, 100]

# Buckling data for each boundary condition and mode shape
buckling_data = {
    'SSSS': {
        '1-0-1': [0.4659, 0.4693, 0.4796, 0.4967, 0.5207, 0.5515],
        '2-1-2': [0.6561, 0.6603, 0.6732, 0.6946, 0.7245, 0.7631],
        '1-1-1': [0.8315, 0.8366, 0.8520, 0.8777, 0.9136, 0.9599],
        '1-2-1': [1.1070, 1.1139, 1.1344, 1.1687, 1.2166, 1.2782]
    },
    'SCSC': {
        '1-0-1': [0.8542, 0.8572, 0.8663, 0.8815, 0.9027, 0.9299],
        '2-1-2': [1.1848, 1.1886, 1.2000, 1.2190, 1.2456, 1.2797],
        '1-1-1': [1.4827, 1.4873, 1.5010, 1.5239, 1.5559, 1.5969],
        '1-2-1': [1.9410, 1.9471, 1.9655, 1.9961, 2.0389, 2.0938]
    },
    'CCCC': {
        '1-0-1': [1.1623, 1.1649, 1.1728, 1.1860, 1.2045, 1.2282],
        '2-1-2': [1.6032, 1.6065, 1.6165, 1.6330, 1.6561, 1.6857],
        '1-1-1': [1.9973, 2.0013, 2.0133, 2.0331, 2.0609, 2.0965],
        '1-2-1': [2.5995, 2.6048, 2.6208, 2.6473, 2.6844, 2.7318]
    }
}

# Create subplots for each boundary condition
fig, axs = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# Loop through each boundary condition
for ax, (bc, data) in zip(axs, buckling_data.items()):
    for mode, values in data.items():
        ax.plot(Kw_values, values, marker='o', label=mode)
    ax.set_title(f'{bc}')
    ax.set_xlabel('Kw')
    ax.grid(True)
    if bc == 'SSSS':
        reshaped_text = arabic_reshaper.reshape("بار بحرانی")
        display_text = get_display(reshaped_text)
        ax.set_ylabel(display_text, fontproperties=font_prop)
    ax.legend()

# Overall title and layout
#plt.suptitle('Buckling Load vs Winkler Modulus for Different Boundary Conditions', fontsize=14)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

