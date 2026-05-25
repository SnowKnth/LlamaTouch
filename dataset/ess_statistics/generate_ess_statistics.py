"""
ESS Statistics Generator
Analyzes ESS (Episode SubgoalS) data and generates statistical charts:
1. Distribution of key subgoals per episode (trace)
2. Distribution of assertions per key state (.ess file)
3. Distribution of UI component-related assertions (click, exact, fuzzy)
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict, Counter
import seaborn as sns
import os

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

def load_ess_data(filepath):
    """Load ESS data from JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def parse_assertions(assertion_string):
    """
    Parse assertion string to extract assertion types and counts
    Example: "activity<0>|exact<28>|exact<19>" -> {'activity': 1, 'exact': 2, 'fuzzy': 0, 'click': 0, 'type': 0, 'check_install': 0, 'check_uninstall': 0}
    """
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
    """
    Analyze ESS data to extract statistics:
    1. Number of key subgoals per episode
    2. Number of assertions per key state
    3. UI component-related assertions
    """
    # Extract episode (trace) information
    traces = defaultdict(list)  # trace_id -> list of ess files
    ess_assertions = {}  # ess_file -> assertion counts
    
    for ess_file, assertion_string in data.items():
        # Extract trace information: e.g., "generated/trace_59/5.ess" -> "generated/trace_59"
        parts = ess_file.split('/')
        if len(parts) >= 2:
            trace_id = f"{parts[0]}/{parts[1]}"
            traces[trace_id].append(ess_file)
        
        # Parse assertions
        assertions = parse_assertions(assertion_string)
        ess_assertions[ess_file] = assertions
    
    # Calculate statistics
    stats = {
        'subgoals_per_trace': [],  # Number of .ess files per trace
        'assertions_per_ess': [],  # Total assertions per .ess file
        'ui_assertions_per_ess': [],  # UI-related (click, exact, fuzzy) per .ess file
        'assertion_type_counts': Counter(),  # Overall count of each assertion type
        'ui_assertion_distribution': defaultdict(list),  # Distribution of each UI assertion type
    }
    
    # Analyze traces
    for trace_id, ess_files in traces.items():
        stats['subgoals_per_trace'].append(len(ess_files))
    
    # Analyze assertions
    for ess_file, assertions in ess_assertions.items():
        total_assertions = sum(assertions.values())
        ui_assertions = assertions['click'] + assertions['exact'] + assertions['fuzzy']
        
        stats['assertions_per_ess'].append(total_assertions)
        stats['ui_assertions_per_ess'].append(ui_assertions)
        
        # Count assertion types
        for assertion_type, count in assertions.items():
            stats['assertion_type_counts'][assertion_type] += count
            if assertion_type in ['click', 'exact', 'fuzzy']:
                stats['ui_assertion_distribution'][assertion_type].append(count)
    
    return stats, traces, ess_assertions

def plot_subgoals_per_trace(stats, output_dir):
    """Plot distribution of key subgoals per episode (trace)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    data = stats['subgoals_per_trace']
    
    # Histogram
    ax1.hist(data, bins=range(1, max(data) + 2), edgecolor='black', alpha=0.7, color='skyblue')
    ax1.set_xlabel('Number of Key Subgoals (.ess files) per Episode', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Frequency (Number of Episodes)', fontsize=13, fontweight='bold')
    ax1.set_title('Distribution of Key Subgoals per Episode', fontsize=15, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Add statistics text
    mean_val = np.mean(data)
    median_val = np.median(data)
    max_val = max(data)
    min_val = min(data)
    stats_text = f'Mean: {mean_val:.2f}\nMedian: {median_val:.1f}\nMax: {max_val}\nMin: {min_val}\nTotal Episodes: {len(data)}'
    ax1.text(0.98, 0.97, stats_text, transform=ax1.transAxes, 
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
             fontsize=11)
    
    # Box plot
    ax2.boxplot(data, vert=True, patch_artist=True,
                boxprops=dict(facecolor='lightblue', alpha=0.7),
                medianprops=dict(color='red', linewidth=2),
                whiskerprops=dict(linewidth=1.5),
                capprops=dict(linewidth=1.5))
    ax2.set_ylabel('Number of Key Subgoals (.ess files)', fontsize=13, fontweight='bold')
    ax2.set_title('Box Plot: Key Subgoals per Episode', fontsize=15, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.set_xticklabels(['Episodes'])
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'subgoals_per_trace_distribution.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Generated: subgoals_per_trace_distribution.png")

def plot_assertions_per_ess(stats, output_dir):
    """Plot distribution of assertions per essential state (.ess file)"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    data_total = stats['assertions_per_ess']
    data_ui = stats['ui_assertions_per_ess']
    
    # Total assertions histogram
    ax1 = axes[0]
    ax1.hist(data_total, bins=range(0, max(data_total) + 2), edgecolor='black', alpha=0.7, color='lightcoral')
    ax1.set_xlabel('Total Assertions per Essential State', fontsize=15, fontweight='bold')
    ax1.set_ylabel('Frequency (Number of .ess files)', fontsize=15, fontweight='bold')
    ax1.set_title('Distribution of Total Assertions per Essential State', fontsize=17, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    mean_val = np.mean(data_total)
    median_val = np.median(data_total)
    stats_text = f'Mean: {mean_val:.2f}\nMedian: {median_val:.1f}\nMax: {max(data_total)}\nTotal .ess files: {len(data_total)}'
    ax1.text(0.98, 0.97, stats_text, transform=ax1.transAxes,
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
             fontsize=13)
    
    # UI assertions histogram
    ax2 = axes[1]
    ax2.hist(data_ui, bins=range(0, max(data_ui) + 2), edgecolor='black', alpha=0.7, color='lightgreen')
    ax2.set_xlabel('UI-related Assertions (click, exact, fuzzy) per Essential State', fontsize=15, fontweight='bold')
    ax2.set_ylabel('Frequency (Number of .ess files)', fontsize=15, fontweight='bold')
    ax2.set_title('Distribution of UI-related Assertions per Essential State', fontsize=17, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    mean_val = np.mean(data_ui)
    median_val = np.median(data_ui)
    stats_text = f'Mean: {mean_val:.2f}\nMedian: {median_val:.1f}\nMax: {max(data_ui)}'
    ax2.text(0.98, 0.97, stats_text, transform=ax2.transAxes,
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
             fontsize=13)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'assertions_per_ess_distribution.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Generated: assertions_per_ess_distribution.png")

def plot_ui_assertion_types(stats, output_dir):
    """Plot detailed distribution of UI assertion types (click, exact, fuzzy)"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    ui_types = ['click', 'exact', 'fuzzy']
    colors = ['#FF6B6B', '#4ECDC4', '#FFD93D']
    
    # Individual histograms for each UI assertion type
    for idx, (ui_type, color) in enumerate(zip(ui_types, colors)):
        if idx < 3:
            row = idx // 2
            col = idx % 2
            ax = axes[row, col]
            
            data = stats['ui_assertion_distribution'][ui_type]
            if data:
                ax.hist(data, bins=range(0, max(data) + 2), edgecolor='black', alpha=0.7, color=color)
                ax.set_xlabel(f'Number of "{ui_type}" assertions per Essential State', fontsize=15, fontweight='bold')
                ax.set_ylabel('Frequency (Number of .ess files)', fontsize=15, fontweight='bold')
                ax.set_title(f'Distribution of "{ui_type}" Assertions', fontsize=17, fontweight='bold')
                ax.grid(True, alpha=0.3)
                
                mean_val = np.mean(data)
                median_val = np.median(data)
                total = sum(data)
                stats_text = f'Total: {total}\nMean: {mean_val:.2f}\nMedian: {median_val:.1f}\nMax: {max(data)}'
                ax.text(0.98, 0.97, stats_text, transform=ax.transAxes,
                       verticalalignment='top', horizontalalignment='right',
                       bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                       fontsize=13)
    
    # Comparison bar chart
    ax = axes[1, 1]
    assertion_counts = stats['assertion_type_counts']
    ui_counts = {k: assertion_counts[k] for k in ui_types}
    
    bars = ax.bar(ui_counts.keys(), ui_counts.values(), color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
    ax.set_xlabel('Assertion Type', fontsize=15, fontweight='bold')
    ax.set_ylabel('Total Count', fontsize=15, fontweight='bold')
    ax.set_title('Total Count of UI Assertion Types', fontsize=17, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'ui_assertion_types_distribution.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Generated: ui_assertion_types_distribution.png")

def plot_overall_assertion_types(stats, output_dir):
    """Plot overall distribution of all assertion types"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    assertion_counts = stats['assertion_type_counts']
    
    # Sort by count
    sorted_items = sorted(assertion_counts.items(), key=lambda x: x[1], reverse=True)
    types = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]
    
    # Define colors: UI-related in green shades, others in blue/gray shades
    color_map = {
        'exact': '#4ECDC4',
        'click': '#FF6B6B',
        'fuzzy': '#FFD93D',
        'activity': '#95E1D3',
        'type': '#A8E6CF',
        'check_install': '#C7CEEA',
        'check_uninstall': '#FFDAC1'
    }
    colors = [color_map.get(t, '#CCCCCC') for t in types]
    
    # Bar chart
    bars = ax1.bar(types, counts, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax1.set_xlabel('Assertion Type', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Total Count', fontsize=13, fontweight='bold')
    ax1.set_title('Overall Distribution of All Assertion Types', fontsize=15, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.tick_params(axis='x', rotation=45)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Pie chart with percentages
    total = sum(counts)
    # Only show types with > 1% for cleaner pie chart
    significant_items = [(t, c) for t, c in zip(types, counts) if c/total > 0.01]
    other_count = sum([c for t, c in zip(types, counts) if c/total <= 0.01])
    
    if other_count > 0:
        significant_items.append(('Other', other_count))
    
    pie_labels = [f'{t}\n{c} ({c/total*100:.1f}%)' for t, c in significant_items]
    pie_counts = [c for t, c in significant_items]
    pie_colors = [color_map.get(t, '#CCCCCC') for t, c in significant_items]
    
    ax2.pie(pie_counts, labels=pie_labels, colors=pie_colors, autopct='',
            shadow=True, startangle=90, textprops={'fontsize': 11})
    ax2.set_title('Proportion of Assertion Types', fontsize=15, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'overall_assertion_types.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Generated: overall_assertion_types.png")

def generate_summary_report(stats, traces, ess_assertions, output_dir):
    """Generate a text summary report"""
    report_path = os.path.join(output_dir, 'ess_statistics_summary.txt')
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("ESS STATISTICS SUMMARY REPORT\n")
        f.write("=" * 80 + "\n\n")
        
        # Episode statistics
        f.write("1. EPISODE (TRACE) STATISTICS\n")
        f.write("-" * 80 + "\n")
        f.write(f"Total number of episodes: {len(traces)}\n")
        f.write(f"Total number of key states (.ess files): {len(ess_assertions)}\n\n")
        
        subgoals_data = stats['subgoals_per_trace']
        f.write("Key Subgoals per Episode:\n")
        f.write(f"  Mean: {np.mean(subgoals_data):.2f}\n")
        f.write(f"  Median: {np.median(subgoals_data):.1f}\n")
        f.write(f"  Std Dev: {np.std(subgoals_data):.2f}\n")
        f.write(f"  Min: {min(subgoals_data)}\n")
        f.write(f"  Max: {max(subgoals_data)}\n\n")
        
        # Assertion statistics
        f.write("2. ASSERTION STATISTICS\n")
        f.write("-" * 80 + "\n")
        
        total_data = stats['assertions_per_ess']
        f.write("Total Assertions per Key State:\n")
        f.write(f"  Mean: {np.mean(total_data):.2f}\n")
        f.write(f"  Median: {np.median(total_data):.1f}\n")
        f.write(f"  Std Dev: {np.std(total_data):.2f}\n")
        f.write(f"  Min: {min(total_data)}\n")
        f.write(f"  Max: {max(total_data)}\n")
        f.write(f"  Total assertions across all .ess files: {sum(total_data)}\n\n")
        
        ui_data = stats['ui_assertions_per_ess']
        f.write("UI-related Assertions per Key State (click, exact, fuzzy):\n")
        f.write(f"  Mean: {np.mean(ui_data):.2f}\n")
        f.write(f"  Median: {np.median(ui_data):.1f}\n")
        f.write(f"  Std Dev: {np.std(ui_data):.2f}\n")
        f.write(f"  Min: {min(ui_data)}\n")
        f.write(f"  Max: {max(ui_data)}\n")
        f.write(f"  Total UI assertions: {sum(ui_data)}\n")
        f.write(f"  Percentage of total: {sum(ui_data)/sum(total_data)*100:.1f}%\n\n")
        
        # Assertion type breakdown
        f.write("3. ASSERTION TYPE BREAKDOWN\n")
        f.write("-" * 80 + "\n")
        assertion_counts = stats['assertion_type_counts']
        total_assertions = sum(assertion_counts.values())
        
        sorted_items = sorted(assertion_counts.items(), key=lambda x: x[1], reverse=True)
        for assertion_type, count in sorted_items:
            percentage = count / total_assertions * 100
            ui_marker = " [UI-related]" if assertion_type in ['click', 'exact', 'fuzzy'] else ""
            f.write(f"  {assertion_type:20s}: {count:6d} ({percentage:5.1f}%){ui_marker}\n")
        
        f.write(f"\n  {'TOTAL':20s}: {total_assertions:6d} (100.0%)\n\n")
        
        # UI assertion details
        f.write("4. UI ASSERTION TYPE DETAILS\n")
        f.write("-" * 80 + "\n")
        for ui_type in ['click', 'exact', 'fuzzy']:
            data = stats['ui_assertion_distribution'][ui_type]
            if data:
                f.write(f"\n{ui_type.upper()} assertions:\n")
                f.write(f"  Total count: {sum(data)}\n")
                f.write(f"  Mean per .ess file: {np.mean(data):.2f}\n")
                f.write(f"  Median per .ess file: {np.median(data):.1f}\n")
                f.write(f"  Max in single .ess file: {max(data)}\n")
                f.write(f"  .ess files with this assertion: {len([x for x in data if x > 0])}\n")
        
        f.write("\n" + "=" * 80 + "\n")
        f.write("Report generated successfully!\n")
        f.write("=" * 80 + "\n")
    
    print(f"✓ Generated: ess_statistics_summary.txt")

def main():
    # Configuration
    input_file = '../all_ess_content.json'
    output_dir = '.'
    
    print("=" * 80)
    print("ESS STATISTICS GENERATOR")
    print("=" * 80)
    print()
    
    # Load data
    print("Loading ESS data...")
    data = load_ess_data(input_file)
    print(f"✓ Loaded {len(data)} .ess files\n")
    
    # Analyze data
    print("Analyzing data...")
    stats, traces, ess_assertions = analyze_ess_data(data)
    print(f"✓ Analyzed {len(traces)} episodes\n")
    
    # Generate plots
    print("Generating charts...")
    plot_subgoals_per_trace(stats, output_dir)
    plot_assertions_per_ess(stats, output_dir)
    plot_ui_assertion_types(stats, output_dir)
    plot_overall_assertion_types(stats, output_dir)
    
    # Generate summary report
    print("\nGenerating summary report...")
    generate_summary_report(stats, traces, ess_assertions, output_dir)
    
    print("\n" + "=" * 80)
    print("All statistics and charts generated successfully!")
    print(f"Output directory: {os.path.abspath(output_dir)}")
    print("=" * 80)

if __name__ == '__main__':
    main()
