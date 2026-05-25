"""
ESS Statistics Generator for LaTeX Papers
Generates publication-quality charts with English labels suitable for academic papers
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict, Counter
import seaborn as sns
import os

# Set style for publication-quality plots
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.3)
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['pdf.fonttype'] = 42  # TrueType fonts for LaTeX
plt.rcParams['ps.fonttype'] = 42

def load_ess_data(filepath):
    """Load ESS data from JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def parse_assertions(assertion_string):
    """Parse assertion string to extract assertion types and counts"""
    assertions = {
        'activity': 0,
        'exact': 0,
        'fuzzy': 0,
        'click': 0,
        'type': 0,
        'check_install': 0,
        'check_uninstall': 0
    }
    
    if not assertion_string:
        return assertions
    
    parts = assertion_string.split('|')
    for part in parts:
        if '<' in part:
            assertion_type = part.split('<')[0]
            if assertion_type in assertions:
                assertions[assertion_type] += 1
    
    return assertions

def analyze_ess_data(data):
    """Analyze ESS data to extract statistics"""
    traces = defaultdict(list)
    ess_assertions = {}
    
    for ess_file, assertion_string in data.items():
        parts = ess_file.split('/')
        if len(parts) >= 2:
            trace_id = f"{parts[0]}/{parts[1]}"
            traces[trace_id].append(ess_file)
        
        assertions = parse_assertions(assertion_string)
        ess_assertions[ess_file] = assertions
    
    stats = {
        'subgoals_per_trace': [],
        'assertions_per_ess': [],
        'ui_assertions_per_ess': [],
        'assertion_type_counts': Counter(),
        'ui_assertion_distribution': defaultdict(list),
    }
    
    for trace_id, ess_files in traces.items():
        stats['subgoals_per_trace'].append(len(ess_files))
    
    for ess_file, assertions in ess_assertions.items():
        total_assertions = sum(assertions.values())
        ui_assertions = assertions['click'] + assertions['exact'] + assertions['fuzzy']
        
        stats['assertions_per_ess'].append(total_assertions)
        stats['ui_assertions_per_ess'].append(ui_assertions)
        
        for assertion_type, count in assertions.items():
            stats['assertion_type_counts'][assertion_type] += count
            if assertion_type in ['click', 'exact', 'fuzzy']:
                stats['ui_assertion_distribution'][assertion_type].append(count)
    
    return stats, traces, ess_assertions

def plot_subgoals_distribution_latex(stats, output_dir):
    """Plot distribution of key subgoals per episode (LaTeX-ready)"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    
    data = stats['subgoals_per_trace']
    
    # Histogram with better styling
    counts, bins, patches = ax.hist(data, bins=range(1, max(data) + 2), 
                                     edgecolor='black', alpha=0.75, 
                                     color='#3498db', linewidth=1.2)
    
    ax.set_xlabel('Number of Key Subgoals per Episode', fontweight='bold')
    ax.set_ylabel('Number of Episodes', fontweight='bold')
    ax.set_title('Distribution of Key Subgoals per Episode', fontweight='bold', pad=15)
    ax.grid(True, alpha=0.25, linestyle='--')
    
    # Add statistics annotation
    mean_val = np.mean(data)
    median_val = np.median(data)
    stats_text = (f'Mean = {mean_val:.2f}\n'
                  f'Median = {median_val:.0f}\n'
                  f'Total Episodes = {len(data)}')
    ax.text(0.97, 0.97, stats_text, transform=ax.transAxes,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='gray'),
            fontsize=10, family='monospace')
    
    plt.tight_layout()
    
    # Save in multiple formats for LaTeX
    plt.savefig(os.path.join(output_dir, 'fig_subgoals_distribution.pdf'), 
                dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(output_dir, 'fig_subgoals_distribution.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Generated: fig_subgoals_distribution.[pdf|png]")

def plot_assertions_distribution_latex(stats, output_dir):
    """Plot distribution of assertions per key state (LaTeX-ready)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
    
    data_total = stats['assertions_per_ess']
    data_ui = stats['ui_assertions_per_ess']
    
    # Total assertions
    ax1.hist(data_total, bins=range(0, max(data_total) + 2), 
             edgecolor='black', alpha=0.75, color='#e74c3c', linewidth=1.2)
    ax1.set_xlabel('Total Assertions per Key State', fontweight='bold')
    ax1.set_ylabel('Number of Key States', fontweight='bold')
    ax1.set_title('Total Assertions Distribution', fontweight='bold', pad=12)
    ax1.grid(True, alpha=0.25, linestyle='--')
    
    mean_val = np.mean(data_total)
    median_val = np.median(data_total)
    stats_text = f'Mean = {mean_val:.2f}\nMedian = {median_val:.0f}'
    ax1.text(0.97, 0.97, stats_text, transform=ax1.transAxes,
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='gray'),
             fontsize=9, family='monospace')
    
    # UI assertions
    ax2.hist(data_ui, bins=range(0, max(data_ui) + 2), 
             edgecolor='black', alpha=0.75, color='#2ecc71', linewidth=1.2)
    ax2.set_xlabel('UI-related Assertions per Key State', fontweight='bold')
    ax2.set_ylabel('Number of Key States', fontweight='bold')
    ax2.set_title('UI-related Assertions Distribution', fontweight='bold', pad=12)
    ax2.grid(True, alpha=0.25, linestyle='--')
    
    mean_val = np.mean(data_ui)
    median_val = np.median(data_ui)
    stats_text = f'Mean = {mean_val:.2f}\nMedian = {median_val:.0f}'
    ax2.text(0.97, 0.97, stats_text, transform=ax2.transAxes,
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='gray'),
             fontsize=9, family='monospace')
    
    plt.tight_layout()
    
    plt.savefig(os.path.join(output_dir, 'fig_assertions_distribution.pdf'), 
                dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(output_dir, 'fig_assertions_distribution.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Generated: fig_assertions_distribution.[pdf|png]")

def plot_assertion_types_latex(stats, output_dir):
    """Plot assertion types breakdown (LaTeX-ready)"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    
    assertion_counts = stats['assertion_type_counts']
    
    # Define order and labels
    types_order = ['exact', 'activity', 'click', 'fuzzy', 'check_install', 'check_uninstall', 'type']
    type_labels = {
        'exact': 'Exact Match',
        'click': 'Click Action',
        'fuzzy': 'Fuzzy Match',
        'activity': 'Activity Check',
        'type': 'Text Input',
        'check_install': 'Install Check',
        'check_uninstall': 'Uninstall Check'
    }
    
    # Filter and prepare data
    filtered_types = [t for t in types_order if assertion_counts[t] > 0]
    labels = [type_labels[t] for t in filtered_types]
    counts = [assertion_counts[t] for t in filtered_types]
    
    # Color coding: UI-related in blue/green shades, others in gray/orange
    colors = []
    for t in filtered_types:
        if t in ['exact', 'click', 'fuzzy']:
            colors.append('#3498db')  # Blue for UI-related
        else:
            colors.append('#95a5a6')  # Gray for non-UI
    
    # Create bar chart
    bars = ax.bar(range(len(labels)), counts, color=colors, alpha=0.8, 
                   edgecolor='black', linewidth=1.2)
    
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=25, ha='right')
    ax.set_ylabel('Total Count', fontweight='bold')
    ax.set_title('Assertion Type Distribution', fontweight='bold', pad=15)
    ax.grid(True, alpha=0.25, linestyle='--', axis='y')
    
    # Add value labels on bars
    total = sum(counts)
    for i, (bar, count) in enumerate(zip(bars, counts)):
        height = bar.get_height()
        percentage = count / total * 100
        ax.text(bar.get_x() + bar.get_width()/2., height + max(counts)*0.01,
                f'{int(count)}\n({percentage:.1f}%)',
                ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#3498db', edgecolor='black', label='UI-related', alpha=0.8),
        Patch(facecolor='#95a5a6', edgecolor='black', label='Non-UI', alpha=0.8)
    ]
    ax.legend(handles=legend_elements, loc='upper right', framealpha=0.9)
    
    plt.tight_layout()
    
    plt.savefig(os.path.join(output_dir, 'fig_assertion_types.pdf'), 
                dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(output_dir, 'fig_assertion_types.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Generated: fig_assertion_types.[pdf|png]")

def plot_ui_assertions_breakdown_latex(stats, output_dir):
    """Plot UI assertion types breakdown (LaTeX-ready)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
    
    # Bar chart of UI assertion types
    ui_types = ['exact', 'click', 'fuzzy']
    type_labels = ['Exact Match', 'Click Action', 'Fuzzy Match']
    assertion_counts = stats['assertion_type_counts']
    counts = [assertion_counts[t] for t in ui_types]
    colors = ['#3498db', '#e74c3c', '#f39c12']
    
    bars = ax1.bar(type_labels, counts, color=colors, alpha=0.8, 
                   edgecolor='black', linewidth=1.2)
    ax1.set_ylabel('Total Count', fontweight='bold')
    ax1.set_title('UI Assertion Types', fontweight='bold', pad=12)
    ax1.grid(True, alpha=0.25, linestyle='--', axis='y')
    
    # Add value labels
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(count)}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Pie chart showing UI vs Non-UI proportion
    data_ui = stats['ui_assertions_per_ess']
    data_total = stats['assertions_per_ess']
    total_ui = sum(data_ui)
    total_all = sum(data_total)
    total_non_ui = total_all - total_ui
    
    sizes = [total_ui, total_non_ui]
    labels = ['UI-related', 'Non-UI']
    colors_pie = ['#3498db', '#95a5a6']
    explode = (0.05, 0)
    
    wedges, texts, autotexts = ax2.pie(sizes, explode=explode, labels=labels, 
                                        colors=colors_pie, autopct='%1.1f%%',
                                        shadow=True, startangle=90,
                                        textprops={'fontsize': 11, 'fontweight': 'bold'})
    
    # Add count in the center
    ax2.text(0, -0.15, f'Total: {total_all} assertions', 
             ha='center', va='center', fontsize=10,
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='gray'))
    
    ax2.set_title('UI vs Non-UI Assertions', fontweight='bold', pad=12)
    
    plt.tight_layout()
    
    plt.savefig(os.path.join(output_dir, 'fig_ui_assertions_breakdown.pdf'), 
                dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(output_dir, 'fig_ui_assertions_breakdown.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Generated: fig_ui_assertions_breakdown.[pdf|png]")

def generate_latex_table(stats, traces, ess_assertions, output_dir):
    """Generate LaTeX table with statistics"""
    
    table_path = os.path.join(output_dir, 'table_ess_statistics.tex')
    
    with open(table_path, 'w') as f:
        f.write("% ESS Statistics Table for LaTeX\n")
        f.write("% Include this in your paper using \\input{table_ess_statistics.tex}\n\n")
        
        f.write("\\begin{table}[ht]\n")
        f.write("\\centering\n")
        f.write("\\caption{ESS Dataset Statistics}\n")
        f.write("\\label{tab:ess_statistics}\n")
        f.write("\\begin{tabular}{lrr}\n")
        f.write("\\hline\n")
        f.write("\\textbf{Metric} & \\textbf{Value} & \\textbf{\\%} \\\\\n")
        f.write("\\hline\n")
        
        # Episode statistics
        f.write("\\multicolumn{3}{l}{\\textit{Episode Statistics}} \\\\\n")
        f.write(f"Total Episodes & {len(traces)} & -- \\\\\n")
        f.write(f"Total Key States (.ess files) & {len(ess_assertions)} & -- \\\\\n")
        
        subgoals_data = stats['subgoals_per_trace']
        f.write(f"Avg. Key Subgoals per Episode & {np.mean(subgoals_data):.2f} & -- \\\\\n")
        f.write(f"Max Key Subgoals per Episode & {max(subgoals_data)} & -- \\\\\n")
        f.write("\\hline\n")
        
        # Assertion statistics
        f.write("\\multicolumn{3}{l}{\\textit{Assertion Statistics}} \\\\\n")
        total_data = stats['assertions_per_ess']
        ui_data = stats['ui_assertions_per_ess']
        
        total_assertions = sum(total_data)
        total_ui = sum(ui_data)
        total_non_ui = total_assertions - total_ui
        
        f.write(f"Total Assertions & {total_assertions} & 100.0 \\\\\n")
        f.write(f"UI-related Assertions & {total_ui} & {total_ui/total_assertions*100:.1f} \\\\\n")
        f.write(f"Non-UI Assertions & {total_non_ui} & {total_non_ui/total_assertions*100:.1f} \\\\\n")
        f.write(f"Avg. Assertions per Key State & {np.mean(total_data):.2f} & -- \\\\\n")
        f.write("\\hline\n")
        
        # Assertion type breakdown
        f.write("\\multicolumn{3}{l}{\\textit{Assertion Type Breakdown}} \\\\\n")
        assertion_counts = stats['assertion_type_counts']
        
        types_order = [
            ('exact', 'Exact Match'),
            ('activity', 'Activity Check'),
            ('click', 'Click Action'),
            ('fuzzy', 'Fuzzy Match'),
            ('check_install', 'Install Check'),
            ('check_uninstall', 'Uninstall Check'),
            ('type', 'Text Input')
        ]
        
        for type_key, type_name in types_order:
            count = assertion_counts[type_key]
            if count > 0:
                percentage = count / total_assertions * 100
                f.write(f"{type_name} & {count} & {percentage:.1f} \\\\\n")
        
        f.write("\\hline\n")
        f.write("\\end{tabular}\n")
        f.write("\\end{table}\n")
    
    print(f"✓ Generated: table_ess_statistics.tex")

def generate_latex_summary(stats, traces, ess_assertions, output_dir):
    """Generate a comprehensive summary document for LaTeX papers"""
    
    summary_path = os.path.join(output_dir, 'ess_statistics_latex_summary.txt')
    
    with open(summary_path, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("ESS STATISTICS SUMMARY FOR LATEX PAPERS\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("GENERATED FILES:\n")
        f.write("-" * 80 + "\n")
        f.write("Figures (PDF and PNG formats):\n")
        f.write("  - fig_subgoals_distribution.[pdf|png]\n")
        f.write("  - fig_assertions_distribution.[pdf|png]\n")
        f.write("  - fig_assertion_types.[pdf|png]\n")
        f.write("  - fig_ui_assertions_breakdown.[pdf|png]\n\n")
        f.write("Tables:\n")
        f.write("  - table_ess_statistics.tex\n\n")
        
        f.write("=" * 80 + "\n")
        f.write("KEY STATISTICS\n")
        f.write("=" * 80 + "\n\n")
        
        # Episode statistics
        f.write("Episode Statistics:\n")
        f.write(f"  Total Episodes: {len(traces)}\n")
        f.write(f"  Total Key States (.ess files): {len(ess_assertions)}\n")
        
        subgoals_data = stats['subgoals_per_trace']
        f.write(f"  Average Key Subgoals per Episode: {np.mean(subgoals_data):.2f}\n")
        f.write(f"  Median: {np.median(subgoals_data):.1f}\n")
        f.write(f"  Range: {min(subgoals_data)}-{max(subgoals_data)}\n\n")
        
        # Assertion statistics
        total_data = stats['assertions_per_ess']
        ui_data = stats['ui_assertions_per_ess']
        
        f.write("Assertion Statistics:\n")
        f.write(f"  Total Assertions: {sum(total_data)}\n")
        f.write(f"  Average per Key State: {np.mean(total_data):.2f}\n")
        f.write(f"  UI-related: {sum(ui_data)} ({sum(ui_data)/sum(total_data)*100:.1f}%)\n")
        f.write(f"  Non-UI: {sum(total_data)-sum(ui_data)} ({(sum(total_data)-sum(ui_data))/sum(total_data)*100:.1f}%)\n\n")
        
        # Assertion types
        f.write("Assertion Type Distribution:\n")
        assertion_counts = stats['assertion_type_counts']
        total_assertions = sum(assertion_counts.values())
        
        sorted_items = sorted(assertion_counts.items(), key=lambda x: x[1], reverse=True)
        for assertion_type, count in sorted_items:
            if count > 0:
                percentage = count / total_assertions * 100
                ui_marker = " [UI-related]" if assertion_type in ['click', 'exact', 'fuzzy'] else ""
                f.write(f"  {assertion_type:20s}: {count:4d} ({percentage:5.1f}%){ui_marker}\n")
        
        f.write("\n" + "=" * 80 + "\n")
        f.write("LATEX USAGE INSTRUCTIONS\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("1. Figures:\n")
        f.write("   Use PDF format for vector graphics in LaTeX:\n\n")
        f.write("   \\begin{figure}[ht]\n")
        f.write("   \\centering\n")
        f.write("   \\includegraphics[width=0.8\\textwidth]{fig_subgoals_distribution.pdf}\n")
        f.write("   \\caption{Distribution of key subgoals per episode.}\n")
        f.write("   \\label{fig:subgoals_dist}\n")
        f.write("   \\end{figure}\n\n")
        
        f.write("2. Tables:\n")
        f.write("   Include the generated LaTeX table:\n\n")
        f.write("   \\input{table_ess_statistics.tex}\n\n")
        
        f.write("3. Required LaTeX packages:\n")
        f.write("   \\usepackage{graphicx}\n")
        f.write("   \\usepackage{booktabs}  % For better table formatting\n\n")
        
        f.write("=" * 80 + "\n")
        f.write("Notes:\n")
        f.write("- All figures are generated in both PDF (for LaTeX) and PNG (for preview)\n")
        f.write("- PDF figures use TrueType fonts compatible with LaTeX\n")
        f.write("- All figures use publication-quality settings (300 DPI)\n")
        f.write("- Color scheme is print-friendly and colorblind-accessible\n")
        f.write("=" * 80 + "\n")
    
    print(f"✓ Generated: ess_statistics_latex_summary.txt")

def main():
    input_file = '../all_ess_content.json'
    output_dir = '.'
    
    print("=" * 80)
    print("ESS STATISTICS GENERATOR FOR LATEX PAPERS")
    print("=" * 80)
    print()
    
    print("Loading ESS data...")
    data = load_ess_data(input_file)
    print(f"✓ Loaded {len(data)} .ess files\n")
    
    print("Analyzing data...")
    stats, traces, ess_assertions = analyze_ess_data(data)
    print(f"✓ Analyzed {len(traces)} episodes\n")
    
    print("Generating publication-quality figures...")
    plot_subgoals_distribution_latex(stats, output_dir)
    plot_assertions_distribution_latex(stats, output_dir)
    plot_assertion_types_latex(stats, output_dir)
    plot_ui_assertions_breakdown_latex(stats, output_dir)
    
    print("\nGenerating LaTeX table...")
    generate_latex_table(stats, traces, ess_assertions, output_dir)
    
    print("\nGenerating summary document...")
    generate_latex_summary(stats, traces, ess_assertions, output_dir)
    
    print("\n" + "=" * 80)
    print("All LaTeX-ready materials generated successfully!")
    print(f"Output directory: {os.path.abspath(output_dir)}")
    print("\nFiles generated:")
    print("  - 4 figures in PDF and PNG formats (8 files total)")
    print("  - 1 LaTeX table (.tex)")
    print("  - 1 summary document (.txt)")
    print("=" * 80)

if __name__ == '__main__':
    main()
