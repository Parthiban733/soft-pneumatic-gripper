"""
Experimental Kinematics and Force Plotting Script
Paper: A Soft, Multi-finger Pneumatic Gripper for Versatile and Safe Object Handling
Authors: R. Sarvesh, M. Parthiban, K. Vijitha, S. Udhayamathi, V. Vishwa Priya, S. Prabhakaran
PSG College of Technology, Department of Robotics and Automation Engineering
"""

import os
import matplotlib.pyplot as plt
import numpy as np

def generate_plots(output_dir="media"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Global styling
    plt.rcParams.update({
        'font.size': 11,
        'font.family': 'sans-serif',
        'axes.labelsize': 12,
        'axes.titlesize': 13,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.titlesize': 14,
        'figure.dpi': 200
    })

    # 1. Actuation Pressure vs. Kinematics (Bending Angle & Tip Displacement)
    pressure = [0.10, 0.15, 0.20, 0.25]
    bending_angle = [12.5, 18.6, 24.8, 30.5]
    tip_disp = [4.7, 7.1, 9.5, 12.1]

    fig, ax1 = plt.subplots(figsize=(7, 4.5))
    color1 = '#0066cc'
    ax1.set_xlabel('Actuation Pressure (bar)', fontweight='bold')
    ax1.set_ylabel('Bending Angle (deg)', color=color1, fontweight='bold')
    line1 = ax1.plot(pressure, bending_angle, 'o-', color=color1, linewidth=2.5, markersize=8, label='Bending Angle (°)')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, linestyle='--', alpha=0.5)

    ax2 = ax1.twinx()
    color2 = '#ff6600'
    ax2.set_ylabel('Tip Displacement (mm)', color=color2, fontweight='bold')
    line2 = ax2.plot(pressure, tip_disp, 's--', color=color2, linewidth=2.5, markersize=8, label='Tip Displacement (mm)')
    ax2.tick_params(axis='y', labelcolor=color2)

    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', frameon=True, facecolor='white', framealpha=0.9)
    plt.title('Pneumatic Pressure vs. Finger Kinematics', fontweight='bold', pad=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'kinematics_plot.png'))
    plt.close()

    # 2. Actuation Pressure vs. Gripping Force & Payload Capacity
    weight = [43, 69, 86, 110]
    force = [0.39, 0.64, 0.80, 1.03]

    fig, ax1 = plt.subplots(figsize=(7, 4.5))
    color1 = '#107c41'
    ax1.set_xlabel('Actuation Pressure (bar)', fontweight='bold')
    ax1.set_ylabel('Gripping Force (N)', color=color1, fontweight='bold')
    line1 = ax1.plot(pressure, force, 'd-', color=color1, linewidth=2.5, markersize=8, label='Gripping Force (N)')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, linestyle='--', alpha=0.5)

    ax2 = ax1.twinx()
    color2 = '#d83b01'
    ax2.set_ylabel('Max Held Weight (g)', color=color2, fontweight='bold')
    line2 = ax2.plot(pressure, weight, '^--', color=color2, linewidth=2.5, markersize=8, label='Max Held Payload (g)')
    ax2.tick_params(axis='y', labelcolor=color2)

    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', frameon=True, facecolor='white', framealpha=0.9)
    plt.title('Pneumatic Pressure vs. Gripping Force & Payload Capacity', fontweight='bold', pad=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'gripping_force_plot.png'))
    plt.close()

    # 3. Performance Benchmark Comparison
    categories = ['Bending Angle (°)\n(at ≤60 kPa)', 'Bending Efficiency\n(°/kPa × 10)']
    existing = [50.0, 0.83 * 10]
    current = [63.8, 1.28 * 10]

    x = np.arange(len(categories))
    width = 0.35

    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    rects1 = ax.bar(x - width/2, existing, width, label='Existing Design (Rectangular)', color='#a0aab2')
    rects2 = ax.bar(x + width/2, current, width, label='Current Bio-inspired Design', color='#0078d4')

    ax.set_ylabel('Performance Value', fontweight='bold')
    ax.set_title('Performance Comparison: Existing vs. Bio-inspired Soft Gripper', fontweight='bold', pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontweight='semibold')
    ax.legend(frameon=True, facecolor='white')
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    for rect in rects1:
        h = rect.get_height()
        ax.annotate(f'{h:.1f}', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3),
                    textcoords='offset points', ha='center', va='bottom', fontsize=10, fontweight='bold')
    for rect in rects2:
        h = rect.get_height()
        ax.annotate(f'{h:.1f}', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3),
                    textcoords='offset points', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#004578')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'performance_comparison.png'))
    plt.close()

    print(f"Validation plots successfully generated in '{output_dir}/'")

if __name__ == '__main__':
    generate_plots()
