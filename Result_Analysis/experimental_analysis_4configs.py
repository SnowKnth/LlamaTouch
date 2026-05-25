#!/usr/bin/env python3
"""
Experimental Results Analysis for OODroid Research Paper - 4 Configurations
Analyzes four experimental configurations:
1. Baseline AutoDroid
2. OODroid (Full System)
3. Without SOD (Subgoal-Oracle-Driven)
4. Without Conflict-based Adaptation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os

# Set up plotting style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

class ExperimentalAnalyzer4Configs:
    def __init__(self, data_dir):
        self.data_dir = Path(data_dir)
        self.results = {}
        
    def load_data(self):
        """Load all experimental data from CSV files"""
        # Configuration 1: Baseline AutoDroid (3 experiments)
        autodroid_files = [
            "evaluation_metrics_TestbedEvaluator_AutoDroid_2025-10-19-21:28:41.csv",
            "evaluation_metrics_TestbedEvaluator_AutoDroid_2025-10-19-21:50:20.csv",
            "evaluation_metrics_TestbedEvaluator_AutoDroid_2025-10-19-21:52:38.csv"
        ]
        
        # Configuration 2: OODroid Full System (3 experiments)
        oodroid_files = [
            "evaluation_metrics_TestbedEvaluator_RASSDroid_FULL_09_20_2025-10-18-09:12:10.csv",
            "evaluation_metrics_TestbedEvaluator_RASSDroid_FULL_07_29_2025-10-18-07:23:46.csv",
            "evaluation_metrics_TestbedEvaluator_RASSDroid_FULL_07_09_2025-10-19-19:35:10.csv"
        ]
        
        # Configuration 3: Without SOD (1 experiment)
        without_sod_files = [
            "evaluation_metrics_TestbedEvaluator_RASSDroid_NOSUBGOAL_1025_2025-10-27-10:55:48.csv"
        ]
        
        # Configuration 4: Without Conflict-based Adaptation (3 experiments)
        without_conflict_files = [
            "evaluation_metrics_TestbedEvaluator_RASSDroid_NOUPDATE_1019_2025-10-22-22:13:16.csv",
            "evaluation_metrics_TestbedEvaluator_RASSDroid_NOUPDATE_1022_2025-10-25-15:37:39.csv",
            "evaluation_metrics_TestbedEvaluator_RASSDroid_NOUPTDATE_0630_2025-10-19-17:16:31.csv"
        ]
        
        self.results['Baseline_AutoDroid'] = self._load_experiment_group(autodroid_files)
        self.results['OODroid_Full'] = self._load_experiment_group(oodroid_files)
        self.results['Without_SOD'] = self._load_experiment_group(without_sod_files)
        self.results['Without_Conflict_Adaptation'] = self._load_experiment_group(without_conflict_files)
        
    def _load_experiment_group(self, file_list):
        """Load a group of experiment files"""
        experiments = []
        for filename in file_list:
            filepath = self.data_dir / filename
            if filepath.exists():
                df = pd.read_csv(filepath)
                experiments.append(self._parse_metrics(df))
        return experiments
    
    def _parse_metrics(self, df):
        """Parse metrics from a single experiment file"""
        metrics = {}
        for _, row in df.iterrows():
            metric_type = row['metric_type']
            metric_name = row['metric_name']
            value = row['value']
            
            if metric_type not in metrics:
                metrics[metric_type] = {}
            metrics[metric_type][metric_name] = value
            
        return metrics
    
    def create_summary_table(self):
        """Create summary table for all experiments"""
        summary_data = []
        
        # Correct Test Goal Completion Rates (provided by user)
        autodroid_goal_rates = [0.06512605, 0.095132743, 0.067833698]
        oodroid_goal_rates = [0.224669604, 0.229257642, 0.238611714]
        without_sod_goal_rates = [0.19650655]
        without_conflict_goal_rates = [0.212719298, 0.196261682, 0.199570815]
        
        # Process Baseline AutoDroid experiments
        for i, exp in enumerate(self.results['Baseline_AutoDroid'], 1):
            summary_data.append({
                'Configuration': 'Baseline AutoDroid',
                'Experiment': f'Exp {i}',
                'Test Goal Completion Rate': autodroid_goal_rates[i-1],
                'Test Subgoal Completion Rate': exp['task']['completion_rate'],
                'Page F1': exp['page']['f1_score'],
                'Page Recall': exp['page']['recall'],
                'Page Precision': exp['page']['precision'],
                'Page Accuracy': exp['page']['accuracy'],
                'Assertion F1': exp['assertion']['f1_score'],
                'Assertion Recall': exp['assertion']['recall'],
                'Assertion Precision': exp['assertion']['precision']
            })
        
        # Process OODroid Full experiments
        for i, exp in enumerate(self.results['OODroid_Full'], 1):
            summary_data.append({
                'Configuration': 'OODroid (Full)',
                'Experiment': f'Exp {i}',
                'Test Goal Completion Rate': oodroid_goal_rates[i-1],
                'Test Subgoal Completion Rate': exp['task']['completion_rate'],
                'Page F1': exp['page']['f1_score'],
                'Page Recall': exp['page']['recall'],
                'Page Precision': exp['page']['precision'],
                'Page Accuracy': exp['page']['accuracy'],
                'Assertion F1': exp['assertion']['f1_score'],
                'Assertion Recall': exp['assertion']['recall'],
                'Assertion Precision': exp['assertion']['precision']
            })
        
        # Process Without SOD experiment
        for i, exp in enumerate(self.results['Without_SOD']):
            summary_data.append({
                'Configuration': 'Without SOD',
                'Experiment': 'Exp 1',
                'Test Goal Completion Rate': without_sod_goal_rates[0],
                'Test Subgoal Completion Rate': exp['task']['completion_rate'],
                'Page F1': exp['page']['f1_score'],
                'Page Recall': exp['page']['recall'],
                'Page Precision': exp['page']['precision'],
                'Page Accuracy': exp['page']['accuracy'],
                'Assertion F1': exp['assertion']['f1_score'],
                'Assertion Recall': exp['assertion']['recall'],
                'Assertion Precision': exp['assertion']['precision']
            })
        
        # Process Without Conflict-based Adaptation experiments
        for i, exp in enumerate(self.results['Without_Conflict_Adaptation'], 1):
            summary_data.append({
                'Configuration': 'Without Conflict Adaptation',
                'Experiment': f'Exp {i}',
                'Test Goal Completion Rate': without_conflict_goal_rates[i-1],
                'Test Subgoal Completion Rate': exp['task']['completion_rate'],
                'Page F1': exp['page']['f1_score'],
                'Page Recall': exp['page']['recall'],
                'Page Precision': exp['page']['precision'],
                'Page Accuracy': exp['page']['accuracy'],
                'Assertion F1': exp['assertion']['f1_score'],
                'Assertion Recall': exp['assertion']['recall'],
                'Assertion Precision': exp['assertion']['precision']
            })
        
        return pd.DataFrame(summary_data)
    
    def calculate_averages(self, summary_df):
        """Calculate average metrics for each configuration"""
        avg_data = []
        
        for config in summary_df['Configuration'].unique():
            config_data = summary_df[summary_df['Configuration'] == config]
            
            avg_row = {
                'Configuration': config,
                'Test Goal Completion Rate': config_data['Test Goal Completion Rate'].mean(),
                'Test Subgoal Completion Rate': config_data['Test Subgoal Completion Rate'].mean(),
                'Page F1': config_data['Page F1'].mean(),
                'Page Recall': config_data['Page Recall'].mean(),
                'Page Precision': config_data['Page Precision'].mean(),
                'Page Accuracy': config_data['Page Accuracy'].mean(),
                'Assertion F1': config_data['Assertion F1'].mean(),
                'Assertion Recall': config_data['Assertion Recall'].mean(),
                'Assertion Precision': config_data['Assertion Precision'].mean(),
                'Std Dev Goal Rate': config_data['Test Goal Completion Rate'].std() if len(config_data) > 1 else 0,
                'Std Dev Page F1': config_data['Page F1'].std() if len(config_data) > 1 else 0,
                'Std Dev Assertion F1': config_data['Assertion F1'].std() if len(config_data) > 1 else 0
            }
            avg_data.append(avg_row)
        
        return pd.DataFrame(avg_data)
    
    def save_results(self, summary_df, avg_df):
        """Save results to files"""
        summary_df.to_csv('detailed_results_4configs.csv', index=False)
        avg_df.to_csv('average_results_4configs.csv', index=False)
        
        print("\n=== DETAILED EXPERIMENTAL RESULTS (4 Configurations) ===")
        print(summary_df.to_string(index=False))
        
        print("\n=== AVERAGE RESULTS BY CONFIGURATION ===")
        print(avg_df.to_string(index=False))

def main():
    # Initialize analyzer
    analyzer = ExperimentalAnalyzer4Configs('../Evaluator/dumped_stats')
    
    # Load and process data
    print("Loading experimental data for 4 configurations...")
    analyzer.load_data()
    
    # Create summary tables
    print("Creating summary tables...")
    summary_df = analyzer.create_summary_table()
    avg_df = analyzer.calculate_averages(summary_df)
    
    # Save results
    analyzer.save_results(summary_df, avg_df)
    
    print("\nAnalysis complete! Results saved to:")
    print("- detailed_results_4configs.csv")
    print("- average_results_4configs.csv")

if __name__ == "__main__":
    main()
