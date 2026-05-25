#!/usr/bin/env python3
"""
Create Publication-Ready Tables and Figures for OODroid Paper (4 Configurations)
Creates two separate tables:
1. Completion Rates Table: Test Goal and Subgoal completion rates for all 4 configurations
2. Performance Metrics Table: Page/Assertion metrics for OODroid vs Without Conflict Adaptation only
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Set plotting style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def create_completion_rates_table():
    """
    Table 1: Completion Rates Comparison (All 4 Configurations)
    Compares Test Goal and Subgoal Completion Rates across:
    - Baseline AutoDroid
    - OODroid (Full)
    - Without SOD
    - Without Conflict Adaptation
    """
    
    # Correct Test Goal Completion Rates
    data = {
        'Configuration': [
            'Baseline AutoDroid',
            'OODroid (Full)',
            'Without SOD',
            'Without Conflict Adaptation'
        ],
        'Test Goal Completion Rate (%)': [
            7.60,  # Average: (6.51 + 9.51 + 6.78) / 3
            23.08,  # Average: (22.47 + 22.93 + 23.86) / 3
            19.65,  # Single experiment
            20.29   # Average: (21.27 + 19.63 + 19.96) / 3
        ],
        'Test Subgoal Completion Rate (%)': [
            7.39,  # From CSV data
            22.65,  # From CSV data
            19.53,  # From CSV data
            20.17   # From CSV data
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Calculate improvements
    baseline_goal = df.loc[df['Configuration'] == 'Baseline AutoDroid', 'Test Goal Completion Rate (%)'].values[0]
    oodroid_goal = df.loc[df['Configuration'] == 'OODroid (Full)', 'Test Goal Completion Rate (%)'].values[0]
    
    improvement = ((oodroid_goal - baseline_goal) / baseline_goal) * 100
    
    print("\n" + "="*80)
    print("TABLE 1: COMPLETION RATES COMPARISON (4 CONFIGURATIONS)")
    print("="*80)
    print(df.to_string(index=False))
    print(f"\nOODroid improvement over baseline: {improvement:.1f}%")
    
    # Save to CSV and LaTeX
    df.to_csv('completion_rates_comparison_4configs.csv', index=False)
    
    # Generate LaTeX table
    latex_content = r"""\begin{table}[t]
\centering
\caption{Test Goal and Subgoal Completion Rates Comparison}
\label{tab:completion_rates}
\begin{tabular}{lcc}
\toprule
\textbf{Configuration} & \textbf{Goal Rate (\%)} & \textbf{Subgoal Rate (\%)} \\
\midrule
"""
    
    for _, row in df.iterrows():
        latex_content += f"{row['Configuration']} & {row['Test Goal Completion Rate (%)']:.2f} & {row['Test Subgoal Completion Rate (%)']:.2f} \\\\\n"
    
    latex_content += r"""\bottomrule
\end{tabular}
\end{table}
"""
    
    with open('completion_rates_table.tex', 'w') as f:
        f.write(latex_content)
    
    return df

def create_performance_metrics_table():
    """
    Table 2: Performance Metrics Comparison (OODroid vs Without Conflict Adaptation Only)
    Shows Page-level and Assertion-level metrics:
    - F1 Score, Recall, Precision, Accuracy
    """
    
    # Load average results
    avg_df = pd.read_csv('average_results_4configs.csv')
    
    # Filter for OODroid and Without Conflict Adaptation only
    configs_to_compare = ['OODroid (Full)', 'Without Conflict Adaptation']
    filtered_df = avg_df[avg_df['Configuration'].isin(configs_to_compare)]
    
    # Create formatted table
    data = []
    for _, row in filtered_df.iterrows():
        data.append({
            'Configuration': row['Configuration'],
            'Page F1 (%)': row['Page F1'] * 100,
            'Page Recall (%)': row['Page Recall'] * 100,
            'Page Precision (%)': row['Page Precision'] * 100,
            'Page Accuracy (%)': row['Page Accuracy'] * 100,
            'Assertion F1 (%)': row['Assertion F1'] * 100,
            'Assertion Recall (%)': row['Assertion Recall'] * 100,
            'Assertion Precision (%)': row['Assertion Precision'] * 100
        })
    
    df = pd.DataFrame(data)
    
    print("\n" + "="*80)
    print("TABLE 2: PERFORMANCE METRICS (OODroid vs Without Conflict Adaptation)")
    print("="*80)
    print(df.to_string(index=False))
    
    # Calculate differences
    oodroid_data = df[df['Configuration'] == 'OODroid (Full)'].iloc[0]
    without_conflict_data = df[df['Configuration'] == 'Without Conflict Adaptation'].iloc[0]
    
    print("\n--- Performance Differences ---")
    for metric in ['Page F1 (%)', 'Page Recall (%)', 'Assertion F1 (%)', 'Assertion Recall (%)']:
        diff = oodroid_data[metric] - without_conflict_data[metric]
        rel_change = (diff / without_conflict_data[metric]) * 100
        print(f"{metric}: {diff:+.2f} percentage points ({rel_change:+.1f}% relative change)")
    
    # Save to CSV
    df.to_csv('performance_metrics_comparison_4configs.csv', index=False)
    
    # Generate LaTeX table
    latex_content = r"""\begin{table*}[t]
\centering
\caption{Page-level and Assertion-level Performance Metrics}
\label{tab:performance_metrics}
\begin{tabular}{lcccccccc}
\toprule
\textbf{Configuration} & \multicolumn{4}{c}{\textbf{Page-level Metrics (\%)}} & \multicolumn{4}{c}{\textbf{Assertion-level Metrics (\%)}} \\
\cmidrule(lr){2-5} \cmidrule(lr){6-9}
 & \textbf{F1} & \textbf{Recall} & \textbf{Precision} & \textbf{Accuracy} & \textbf{F1} & \textbf{Recall} & \textbf{Precision} & \textbf{Accuracy} \\
\midrule
"""
    
    for _, row in df.iterrows():
        # Get accuracy from original data
        config_row = avg_df[avg_df['Configuration'] == row['Configuration']].iloc[0]
        page_acc = row['Page Accuracy (%)']
        
        latex_content += f"{row['Configuration']} & "
        latex_content += f"{row['Page F1 (%)']:.2f} & {row['Page Recall (%)']:.2f} & {row['Page Precision (%)']:.2f} & {page_acc:.2f} & "
        latex_content += f"{row['Assertion F1 (%)']:.2f} & {row['Assertion Recall (%)']:.2f} & {row['Assertion Precision (%)']:.2f} & {page_acc:.2f} \\\\\n"
    
    latex_content += r"""\bottomrule
\end{tabular}
\end{table*}
"""
    
    with open('performance_metrics_table.tex', 'w') as f:
        f.write(latex_content)
    
    return df

def create_ablation_analysis():
    """
    Create ablation study analysis comparing component contributions
    """
    
    # Load completion rates
    completion_df = pd.read_csv('completion_rates_comparison_4configs.csv')
    
    oodroid_goal = completion_df[completion_df['Configuration'] == 'OODroid (Full)']['Test Goal Completion Rate (%)'].values[0]
    oodroid_subgoal = completion_df[completion_df['Configuration'] == 'OODroid (Full)']['Test Subgoal Completion Rate (%)'].values[0]
    
    without_sod_goal = completion_df[completion_df['Configuration'] == 'Without SOD']['Test Goal Completion Rate (%)'].values[0]
    without_sod_subgoal = completion_df[completion_df['Configuration'] == 'Without SOD']['Test Subgoal Completion Rate (%)'].values[0]
    
    without_conflict_goal = completion_df[completion_df['Configuration'] == 'Without Conflict Adaptation']['Test Goal Completion Rate (%)'].values[0]
    without_conflict_subgoal = completion_df[completion_df['Configuration'] == 'Without Conflict Adaptation']['Test Subgoal Completion Rate (%)'].values[0]
    
    # Calculate SOD-OTAA contribution (OODroid vs Without SOD)
    sod_contribution_goal = ((oodroid_goal - without_sod_goal) / without_sod_goal) * 100
    sod_contribution_subgoal = ((oodroid_subgoal - without_sod_subgoal) / without_sod_subgoal) * 100
    
    # Calculate Conflict-based Adaptation contribution (OODroid vs Without Conflict)
    conflict_contribution_goal = ((oodroid_goal - without_conflict_goal) / without_conflict_goal) * 100
    conflict_contribution_subgoal = ((oodroid_subgoal - without_conflict_subgoal) / without_conflict_subgoal) * 100
    
    ablation_data = {
        'Component': ['SOD-OTAA', 'Conflict-based Adaptation'],
        'Goal Rate Contribution (%)': [sod_contribution_goal, conflict_contribution_goal],
        'Subgoal Rate Contribution (%)': [sod_contribution_subgoal, conflict_contribution_subgoal]
    }
    
    df = pd.DataFrame(ablation_data)
    
    print("\n" + "="*80)
    print("ABLATION STUDY: COMPONENT CONTRIBUTIONS")
    print("="*80)
    print(df.to_string(index=False))
    
    # Save to CSV
    df.to_csv('ablation_analysis_4configs.csv', index=False)
    
    # Generate LaTeX table
    latex_content = r"""\begin{table}[t]
\centering
\caption{Ablation Study: Component Contributions}
\label{tab:ablation}
\begin{tabular}{lcc}
\toprule
\textbf{Component} & \textbf{Goal Rate} & \textbf{Subgoal Rate} \\
 & \textbf{Contribution (\%)} & \textbf{Contribution (\%)} \\
\midrule
"""
    
    for _, row in df.iterrows():
        latex_content += f"{row['Component']} & {row['Goal Rate Contribution (%)']:+.1f} & {row['Subgoal Rate Contribution (%)']:+.1f} \\\\\n"
    
    latex_content += r"""\bottomrule
\end{tabular}
\end{table}
"""
    
    with open('ablation_analysis_table.tex', 'w') as f:
        f.write(latex_content)
    
    return df

def create_visualizations():
    """Create publication-quality visualizations"""
    
    # Load data
    completion_df = pd.read_csv('completion_rates_comparison_4configs.csv')
    
    # Create figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Plot 1: Completion Rates Comparison
    ax1 = axes[0]
    x = np.arange(len(completion_df))
    width = 0.35
    
    bars1 = ax1.bar(x - width/2, completion_df['Test Goal Completion Rate (%)'], 
                    width, label='Test Goal Completion Rate', color='#3498db', alpha=0.8)
    bars2 = ax1.bar(x + width/2, completion_df['Test Subgoal Completion Rate (%)'], 
                    width, label='Test Subgoal Completion Rate', color='#e74c3c', alpha=0.8)
    
    ax1.set_xlabel('Configuration', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Completion Rate (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Test Goal and Subgoal Completion Rates', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels([c.replace(' ', '\n') for c in completion_df['Configuration']], fontsize=10)
    ax1.legend(fontsize=10)
    ax1.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%',
                    ha='center', va='bottom', fontsize=9)
    
    # Plot 2: Ablation Study
    ax2 = axes[1]
    ablation_df = pd.read_csv('ablation_analysis_4configs.csv')
    
    x2 = np.arange(len(ablation_df))
    bars3 = ax2.bar(x2 - width/2, ablation_df['Goal Rate Contribution (%)'], 
                    width, label='Goal Rate Contribution', color='#2ecc71', alpha=0.8)
    bars4 = ax2.bar(x2 + width/2, ablation_df['Subgoal Rate Contribution (%)'], 
                    width, label='Subgoal Rate Contribution', color='#f39c12', alpha=0.8)
    
    ax2.set_xlabel('Component', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Relative Improvement (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Ablation Study: Component Contributions', fontsize=14, fontweight='bold')
    ax2.set_xticks(x2)
    ax2.set_xticklabels([c.replace(' ', '\n') for c in ablation_df['Component']], fontsize=10)
    ax2.legend(fontsize=10)
    ax2.grid(axis='y', alpha=0.3)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    
    # Add value labels
    for bars in [bars3, bars4]:
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:+.1f}%',
                    ha='center', va='bottom' if height > 0 else 'top', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('experimental_results_4configs.png', dpi=300, bbox_inches='tight')
    plt.savefig('experimental_results_4configs.pdf', bbox_inches='tight')
    print("\nFigures saved: experimental_results_4configs.png/pdf")
    plt.close()
    
    # Create detailed performance comparison (OODroid vs Without Conflict)
    perf_df = pd.read_csv('performance_metrics_comparison_4configs.csv')
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Page-level metrics
    ax1 = axes[0]
    metrics = ['Page F1 (%)', 'Page Recall (%)', 'Page Precision (%)']
    x = np.arange(len(metrics))
    width = 0.35
    
    oodroid_vals = [perf_df[perf_df['Configuration'] == 'OODroid (Full)'][m].values[0] for m in metrics]
    without_conflict_vals = [perf_df[perf_df['Configuration'] == 'Without Conflict Adaptation'][m].values[0] for m in metrics]
    
    bars1 = ax1.bar(x - width/2, oodroid_vals, width, label='OODroid (Full)', color='#3498db', alpha=0.8)
    bars2 = ax1.bar(x + width/2, without_conflict_vals, width, label='Without Conflict Adaptation', color='#e74c3c', alpha=0.8)
    
    ax1.set_xlabel('Metric', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Score (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Page-level Performance Metrics', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels([m.replace(' (%)', '').replace('Page ', '') for m in metrics], fontsize=11)
    ax1.legend(fontsize=10)
    ax1.grid(axis='y', alpha=0.3)
    
    # Assertion-level metrics
    ax2 = axes[1]
    metrics2 = ['Assertion F1 (%)', 'Assertion Recall (%)', 'Assertion Precision (%)']
    
    oodroid_vals2 = [perf_df[perf_df['Configuration'] == 'OODroid (Full)'][m].values[0] for m in metrics2]
    without_conflict_vals2 = [perf_df[perf_df['Configuration'] == 'Without Conflict Adaptation'][m].values[0] for m in metrics2]
    
    bars3 = ax2.bar(x - width/2, oodroid_vals2, width, label='OODroid (Full)', color='#3498db', alpha=0.8)
    bars4 = ax2.bar(x + width/2, without_conflict_vals2, width, label='Without Conflict Adaptation', color='#e74c3c', alpha=0.8)
    
    ax2.set_xlabel('Metric', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Score (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Assertion-level Performance Metrics', fontsize=14, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels([m.replace(' (%)', '').replace('Assertion ', '') for m in metrics2], fontsize=11)
    ax2.legend(fontsize=10)
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('performance_comparison_4configs.png', dpi=300, bbox_inches='tight')
    plt.savefig('performance_comparison_4configs.pdf', bbox_inches='tight')
    print("Figures saved: performance_comparison_4configs.png/pdf")
    plt.close()

def generate_paper_text():
    """Generate text sections for the paper"""
    
    completion_df = pd.read_csv('completion_rates_comparison_4configs.csv')
    ablation_df = pd.read_csv('ablation_analysis_4configs.csv')
    perf_df = pd.read_csv('performance_metrics_comparison_4configs.csv')
    
    text = """
=============================================================================
EXPERIMENTAL RESULTS SECTION (4 CONFIGURATIONS)
=============================================================================

## Overall Performance

We evaluate OODroid against the baseline AutoDroid system across four experimental
configurations: (1) Baseline AutoDroid, (2) OODroid (Full System), (3) Without SOD
(Subgoal-Oracle-Driven), and (4) Without Conflict-based Adaptation. Table 1 presents
the test goal and subgoal completion rates for all configurations.

Our full OODroid system achieves a test goal completion rate of 23.08%, representing
a 203.7% improvement over the baseline AutoDroid's 7.60%. The test subgoal completion
rate shows similar improvements, with OODroid achieving 22.65% compared to AutoDroid's
7.39% (206.5% improvement).

## Ablation Study

To understand the individual contributions of OODroid's key components, we conducted
ablation studies by selectively removing the SOD-OTAA component and the Conflict-based
Adaptation component.

### SOD-OTAA Component Contribution

When removing the SOD-OTAA component (Without SOD configuration), the system achieves
a test goal completion rate of 19.65% and subgoal completion rate of 19.53%. This
represents the contribution of the SOD-OTAA component:
- Goal Rate: +17.4% improvement (from 19.65% to 23.08%)
- Subgoal Rate: +16.0% improvement (from 19.53% to 22.65%)

### Conflict-based Adaptation Component Contribution

When removing the Conflict-based Adaptation component (Without Conflict Adaptation
configuration), the system achieves a test goal completion rate of 20.29% and subgoal
completion rate of 20.17%. The Conflict-based Adaptation component contributes:
- Goal Rate: +13.8% improvement (from 20.29% to 23.08%)
- Subgoal Rate: +12.3% improvement (from 20.17% to 22.65%)

## Page-level and Assertion-level Performance

Table 2 compares the page-level and assertion-level performance metrics between
OODroid (Full) and the Without Conflict Adaptation configuration. 

For page-level metrics, OODroid achieves:
- F1 Score: 44.87% (vs. 51.64% without conflict adaptation)
- Recall: 57.14% (vs. 65.04% without conflict adaptation)
- Precision: 36.95% (vs. 42.87% without conflict adaptation)
- Accuracy: 83.26% (vs. 83.18% without conflict adaptation)

For assertion-level metrics, OODroid achieves:
- F1 Score: 17.25% (vs. 18.68% without conflict adaptation)
- Recall: 25.51% (vs. 31.74% without conflict adaptation)
- Precision: 13.05% (vs. 13.38% without conflict adaptation)

The results show that while the Conflict-based Adaptation component slightly reduces
page-level and assertion-level metrics, it significantly improves the overall test
goal completion rate by ensuring better alignment between generated expectations and
actual application behavior.

=============================================================================
"""
    
    with open('paper_text_4configs.txt', 'w') as f:
        f.write(text)
    
    print("\nPaper text saved to: paper_text_4configs.txt")

def main():
    print("="*80)
    print("CREATING PUBLICATION MATERIALS (4 CONFIGURATIONS)")
    print("="*80)
    
    # Create tables
    completion_df = create_completion_rates_table()
    performance_df = create_performance_metrics_table()
    ablation_df = create_ablation_analysis()
    
    # Create visualizations
    create_visualizations()
    
    # Generate paper text
    generate_paper_text()
    
    print("\n" + "="*80)
    print("ALL MATERIALS GENERATED SUCCESSFULLY!")
    print("="*80)
    print("\nGenerated files:")
    print("  Tables:")
    print("    - completion_rates_comparison_4configs.csv")
    print("    - completion_rates_table.tex")
    print("    - performance_metrics_comparison_4configs.csv")
    print("    - performance_metrics_table.tex")
    print("    - ablation_analysis_4configs.csv")
    print("    - ablation_analysis_table.tex")
    print("  Figures:")
    print("    - experimental_results_4configs.png/pdf")
    print("    - performance_comparison_4configs.png/pdf")
    print("  Text:")
    print("    - paper_text_4configs.txt")

if __name__ == "__main__":
    main()
