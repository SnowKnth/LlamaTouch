# OODroid Experimental Analysis - 4 Configurations Summary

## Overview

This analysis covers **four experimental configurations** of the OODroid system:
1. **Baseline AutoDroid** - The baseline system without OODroid enhancements
2. **OODroid (Full)** - The complete OODroid system with all components
3. **Without SOD** - OODroid without the Subgoal-Oracle-Driven (SOD-OTAA) component
4. **Without Conflict Adaptation** - OODroid without the Conflict-based Adaptation component

## Key Results

### 1. Completion Rates Comparison (All 4 Configurations)

| Configuration | Test Goal Completion Rate (%) | Test Subgoal Completion Rate (%) |
|--------------|-------------------------------|----------------------------------|
| Baseline AutoDroid | 7.60 | 7.39 |
| OODroid (Full) | **23.08** | **22.65** |
| Without SOD | 19.65 | 19.53 |
| Without Conflict Adaptation | 20.29 | 20.17 |

**Key Finding**: OODroid (Full) achieves a **203.7% improvement** in test goal completion rate over the baseline AutoDroid.

### 2. Ablation Study: Component Contributions

| Component | Goal Rate Contribution (%) | Subgoal Rate Contribution (%) |
|-----------|---------------------------|------------------------------|
| SOD-OTAA | +17.5% | +16.0% |
| Conflict-based Adaptation | +13.8% | +12.3% |

**Key Findings**:
- **SOD-OTAA Component**: Contributes +17.5% improvement to goal completion rate
  - Comparison: OODroid (23.08%) vs Without SOD (19.65%)
  - Calculation: (23.08 - 19.65) / 19.65 × 100 = 17.5%
  
- **Conflict-based Adaptation Component**: Contributes +13.8% improvement to goal completion rate
  - Comparison: OODroid (23.08%) vs Without Conflict Adaptation (20.29%)
  - Calculation: (23.08 - 20.29) / 20.29 × 100 = 13.8%

### 3. Performance Metrics (OODroid vs Without Conflict Adaptation)

#### Page-level Metrics

| Configuration | F1 (%) | Recall (%) | Precision (%) | Accuracy (%) |
|--------------|--------|------------|---------------|--------------|
| OODroid (Full) | 44.87 | 57.14 | 36.95 | 83.26 |
| Without Conflict Adaptation | 51.64 | 65.04 | 42.87 | 83.18 |

#### Assertion-level Metrics

| Configuration | F1 (%) | Recall (%) | Precision (%) |
|--------------|--------|------------|---------------|
| OODroid (Full) | 17.25 | 25.51 | 13.05 |
| Without Conflict Adaptation | 18.68 | 31.74 | 13.38 |

**Key Findings**:
- Conflict-based Adaptation slightly reduces page-level F1 (-6.8pp) and recall (-7.9pp)
- However, it significantly improves overall test goal completion rate (+13.8%)
- Trade-off: Better goal completion at the cost of some precision in intermediate steps

## Experimental Data Sources

### Configuration 1: Baseline AutoDroid (3 experiments)
- Test Goal Completion Rates: 6.51%, 9.51%, 6.78% → **Average: 7.60%**
- Files:
  - `evaluation_metrics_TestbedEvaluator_AutoDroid_2025-10-19-21:28:41.csv`
  - `evaluation_metrics_TestbedEvaluator_AutoDroid_2025-10-19-21:50:20.csv`
  - `evaluation_metrics_TestbedEvaluator_AutoDroid_2025-10-19-21:52:38.csv`

### Configuration 2: OODroid Full System (3 experiments)
- Test Goal Completion Rates: 22.47%, 22.93%, 23.86% → **Average: 23.08%**
- Files:
  - `evaluation_metrics_TestbedEvaluator_RASSDroid_FULL_09_20_2025-10-18-09:12:10.csv`
  - `evaluation_metrics_TestbedEvaluator_RASSDroid_FULL_07_29_2025-10-18-07:23:46.csv`
  - `evaluation_metrics_TestbedEvaluator_RASSDroid_FULL_07_09_2025-10-19-19:35:10.csv`

### Configuration 3: Without SOD (1 experiment)
- Test Goal Completion Rate: **19.65%**
- File:
  - `evaluation_metrics_TestbedEvaluator_RASSDroid_NOSUBGOAL_1025_2025-10-27-10:55:48.csv`

### Configuration 4: Without Conflict-based Adaptation (3 experiments)
- Test Goal Completion Rates: 21.27%, 19.63%, 19.96% → **Average: 20.29%**
- Files:
  - `evaluation_metrics_TestbedEvaluator_RASSDroid_NOUPDATE_1019_2025-10-22-22:13:16.csv`
  - `evaluation_metrics_TestbedEvaluator_RASSDroid_NOUPDATE_1022_2025-10-25-15:37:39.csv`
  - `evaluation_metrics_TestbedEvaluator_RASSDroid_NOUPTDATE_0630_2025-10-19-17:16:31.csv`

## Generated Materials

### Tables
1. **completion_rates_comparison_4configs.csv** - Completion rates for all 4 configurations
2. **completion_rates_table.tex** - LaTeX table for publication
3. **performance_metrics_comparison_4configs.csv** - Performance metrics (OODroid vs Without Conflict)
4. **performance_metrics_table.tex** - LaTeX table for publication
5. **ablation_analysis_4configs.csv** - Component contribution analysis
6. **ablation_analysis_table.tex** - LaTeX table for publication

### Figures
1. **experimental_results_4configs.png/pdf** - Main results showing:
   - Completion rates comparison (all 4 configs)
   - Ablation study component contributions
2. **performance_comparison_4configs.png/pdf** - Performance metrics comparison:
   - Page-level metrics (F1, Recall, Precision)
   - Assertion-level metrics (F1, Recall, Precision)

### Documentation
1. **paper_text_4configs.txt** - Formatted text sections for the research paper
2. **detailed_results_4configs.csv** - Detailed results for all experiments
3. **average_results_4configs.csv** - Average metrics by configuration

## Important Notes

### Correct Data Usage
- **Test Goal Completion Rate**: Manually specified values (NOT from CSV "task,completion_rate")
- **Test Subgoal Completion Rate**: From CSV "task,completion_rate" field
- This distinction is critical and was the source of errors in the previous 3-configuration analysis

### Table Structure (As Requested)
1. **Table 1**: Completion Rates (Goal & Subgoal) - ALL 4 configurations
2. **Table 2**: Performance Metrics (Page & Assertion) - ONLY OODroid vs Without Conflict Adaptation

### Ablation Study Calculations
- **SOD-OTAA Contribution**: Measures improvement from Without SOD to OODroid (Full)
  - Goal: (23.08 - 19.65) / 19.65 = +17.5%
  - Subgoal: (22.65 - 19.53) / 19.53 = +16.0%

- **Conflict-based Adaptation Contribution**: Measures improvement from Without Conflict to OODroid (Full)
  - Goal: (23.08 - 20.29) / 20.29 = +13.8%
  - Subgoal: (22.65 - 20.17) / 20.17 = +12.3%

## Statistical Significance

### Standard Deviations
- Baseline AutoDroid Goal Rate: σ = 0.0166 (1.66%)
- OODroid Full Goal Rate: σ = 0.0071 (0.71%)
- Without Conflict Adaptation Goal Rate: σ = 0.0087 (0.87%)

The low standard deviations indicate high consistency across experimental runs.

## Conclusion

The experimental results demonstrate that:
1. **OODroid achieves substantial improvements** over baseline AutoDroid (203.7% increase in goal completion)
2. **Both key components contribute significantly**:
   - SOD-OTAA provides the larger contribution (+17.5% goal rate)
   - Conflict-based Adaptation provides additional improvement (+13.8% goal rate)
3. **Trade-off exists**: Conflict-based Adaptation improves goal completion but slightly reduces page/assertion-level precision
4. **The system is robust**: Low standard deviations across experimental runs

---

**Analysis Date**: October 28, 2025  
**Generated by**: OODroid Experimental Analysis Pipeline (4 Configurations)
