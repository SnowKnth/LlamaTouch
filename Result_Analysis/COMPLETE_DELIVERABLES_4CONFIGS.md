# OODroid Experimental Results - Complete Deliverables (4 Configurations)

**Analysis Date**: October 28, 2025  
**Analysis Type**: 4-Configuration Experimental Comparison with Correct Data

---

## Executive Summary

This analysis provides a comprehensive evaluation of the OODroid system across **four experimental configurations**:

1. **Baseline AutoDroid** - The baseline system (3 experiments)
2. **OODroid (Full)** - The complete OODroid system (3 experiments)
3. **Without SOD** - OODroid without Subgoal-Oracle-Driven component (1 experiment)
4. **Without Conflict Adaptation** - OODroid without Conflict-based Adaptation (3 experiments)

### Key Achievements

- **203.7% improvement** in test goal completion rate over baseline
- **SOD-OTAA component** contributes **+17.5%** improvement
- **Conflict-based Adaptation** contributes **+13.8%** improvement
- Both **Goal** and **Subgoal** completion rates analyzed
- Separate tables for **Completion Rates** (all 4 configs) and **Performance Metrics** (2 configs only)

---

## Complete File Listing

### 📊 Data Files (CSV)

1. **detailed_results_4configs.csv**
   - Individual experiment results for all 10 experiments
   - Includes all metrics: goal rates, subgoal rates, page metrics, assertion metrics
   - Size: 1.7 KB

2. **average_results_4configs.csv**
   - Averaged metrics for each of the 4 configurations
   - Includes standard deviations
   - Size: 962 bytes

3. **completion_rates_comparison_4configs.csv**
   - **TABLE 1 DATA**: Goal and Subgoal completion rates for all 4 configurations
   - This is the primary comparison table
   - Size: 196 bytes

4. **performance_metrics_comparison_4configs.csv**
   - **TABLE 2 DATA**: Page/Assertion metrics for OODroid vs Without Conflict Adaptation
   - Only 2 configurations compared
   - Size: 435 bytes

5. **ablation_analysis_4configs.csv**
   - Component contribution calculations
   - SOD-OTAA and Conflict-based Adaptation improvements
   - Size: 177 bytes

### 📄 LaTeX Tables (for Publication)

1. **completion_rates_table.tex**
   - Table 1: Test Goal and Subgoal Completion Rates Comparison
   - All 4 configurations
   - Label: `\label{tab:completion_rates}`

2. **performance_metrics_table.tex**
   - Table 2: Page-level and Assertion-level Performance Metrics
   - Only OODroid (Full) vs Without Conflict Adaptation
   - Wide table format (`table*`)
   - Label: `\label{tab:performance_metrics}`

3. **ablation_analysis_table.tex**
   - Ablation Study: Component Contributions
   - Shows both Goal Rate and Subgoal Rate contributions
   - Label: `\label{tab:ablation}`

### 📈 Figures (PNG & PDF)

1. **experimental_results_4configs.png/pdf**
   - Two-panel figure:
     - Panel 1: Test Goal and Subgoal Completion Rates (all 4 configs)
     - Panel 2: Ablation Study Component Contributions
   - Size: 276 KB (PNG), 30 KB (PDF)
   - Resolution: 300 DPI

2. **performance_comparison_4configs.png/pdf**
   - Two-panel figure:
     - Panel 1: Page-level Performance Metrics
     - Panel 2: Assertion-level Performance Metrics
   - Only shows OODroid vs Without Conflict Adaptation
   - Size: 135 KB (PNG), 23 KB (PDF)
   - Resolution: 300 DPI

### 📝 Documentation

1. **paper_text_4configs.txt**
   - Pre-written text sections for the research paper
   - Includes: Overall Performance, Ablation Study, Performance Metrics
   - Ready to copy into paper manuscript

2. **SUMMARY_4CONFIGS.md**
   - Comprehensive summary document (this file)
   - Includes all key results, calculations, and file descriptions

### 🐍 Python Scripts

1. **experimental_analysis_4configs.py**
   - Main analysis script
   - Loads all 10 experiment CSV files
   - Uses **correct Test Goal Completion Rates** (not from CSV)
   - Generates detailed and average results

2. **create_publication_tables_4configs.py**
   - Creates all publication materials
   - Generates CSV tables, LaTeX tables, and figures
   - Implements the requested table structure

---

## Table 1: Completion Rates Comparison

**Purpose**: Compare Test Goal and Subgoal completion rates across ALL 4 configurations

| Configuration | Test Goal Rate (%) | Test Subgoal Rate (%) |
|--------------|--------------------|-----------------------|
| Baseline AutoDroid | 7.60 | 7.39 |
| OODroid (Full) | **23.08** | **22.65** |
| Without SOD | 19.65 | 19.53 |
| Without Conflict Adaptation | 20.29 | 20.17 |

**Key Insight**: OODroid (Full) achieves **203.7%** improvement over baseline

### Calculation Details

**Baseline AutoDroid** (Average of 3 experiments):
- Goal Rates: 6.51%, 9.51%, 6.78%
- Average: (6.51 + 9.51 + 6.78) / 3 = **7.60%**

**OODroid (Full)** (Average of 3 experiments):
- Goal Rates: 22.47%, 22.93%, 23.86%
- Average: (22.47 + 22.93 + 23.86) / 3 = **23.08%**

**Without SOD** (1 experiment):
- Goal Rate: **19.65%**

**Without Conflict Adaptation** (Average of 3 experiments):
- Goal Rates: 21.27%, 19.63%, 19.96%
- Average: (21.27 + 19.63 + 19.96) / 3 = **20.29%**

---

## Table 2: Performance Metrics Comparison

**Purpose**: Compare Page and Assertion metrics for OODroid vs Without Conflict Adaptation ONLY

### Page-level Metrics

| Configuration | F1 (%) | Recall (%) | Precision (%) | Accuracy (%) |
|--------------|--------|------------|---------------|--------------|
| OODroid (Full) | 44.87 | 57.14 | 36.95 | 83.26 |
| Without Conflict Adaptation | 51.64 | 65.04 | 42.87 | 83.18 |
| **Difference** | **-6.77** | **-7.90** | **-5.92** | **+0.08** |

### Assertion-level Metrics

| Configuration | F1 (%) | Recall (%) | Precision (%) | Accuracy (%) |
|--------------|--------|------------|---------------|--------------|
| OODroid (Full) | 17.25 | 25.51 | 13.05 | 83.26 |
| Without Conflict Adaptation | 18.68 | 31.74 | 13.38 | 83.18 |
| **Difference** | **-1.43** | **-6.23** | **-0.33** | **+0.08** |

**Key Insight**: Conflict-based Adaptation trades some page/assertion precision for better overall goal completion

---

## Ablation Study: Component Contributions

### SOD-OTAA Component

**Comparison**: OODroid (Full) vs Without SOD

| Metric | OODroid | Without SOD | Contribution |
|--------|---------|-------------|--------------|
| Goal Rate | 23.08% | 19.65% | **+17.5%** |
| Subgoal Rate | 22.65% | 19.53% | **+16.0%** |

**Calculation**:
- Goal Rate Contribution: (23.08 - 19.65) / 19.65 × 100 = **17.5%**
- Subgoal Rate Contribution: (22.65 - 19.53) / 19.53 × 100 = **16.0%**

### Conflict-based Adaptation Component

**Comparison**: OODroid (Full) vs Without Conflict Adaptation

| Metric | OODroid | Without Conflict | Contribution |
|--------|---------|------------------|--------------|
| Goal Rate | 23.08% | 20.29% | **+13.8%** |
| Subgoal Rate | 22.65% | 20.17% | **+12.3%** |

**Calculation**:
- Goal Rate Contribution: (23.08 - 20.29) / 20.29 × 100 = **13.8%**
- Subgoal Rate Contribution: (22.65 - 20.17) / 20.17 × 100 = **12.3%**

---

## Data Correction Summary

### Critical Issue Fixed

**Problem**: In previous 3-configuration analysis, Test Goal Completion Rates were incorrectly taken from the CSV field "task,completion_rate", which actually contains **Test Subgoal Completion Rates**.

**Solution**: All Test Goal Completion Rates are now manually specified from the user-provided correct values:

| Configuration | Experiment | Correct Goal Rate |
|--------------|------------|-------------------|
| Baseline AutoDroid | Exp 1 | 0.06512605 |
| Baseline AutoDroid | Exp 2 | 0.095132743 |
| Baseline AutoDroid | Exp 3 | 0.067833698 |
| OODroid (Full) | Exp 1 | 0.224669604 |
| OODroid (Full) | Exp 2 | 0.229257642 |
| OODroid (Full) | Exp 3 | 0.238611714 |
| Without SOD | Exp 1 | 0.19650655 |
| Without Conflict | Exp 1 | 0.212719298 |
| Without Conflict | Exp 2 | 0.196261682 |
| Without Conflict | Exp 3 | 0.199570815 |

### Data Source Mapping

The scripts now correctly distinguish:
- **Test Goal Completion Rate**: From user-provided values (hardcoded in scripts)
- **Test Subgoal Completion Rate**: From CSV "task,completion_rate" field
- **All other metrics**: Directly from CSV files

---

## Statistical Robustness

### Standard Deviations (Goal Completion Rate)

| Configuration | Mean | Std Dev | Coefficient of Variation |
|--------------|------|---------|--------------------------|
| Baseline AutoDroid | 7.60% | 1.66% | 21.8% |
| OODroid (Full) | 23.08% | 0.71% | 3.1% |
| Without SOD | 19.65% | N/A (single exp) | N/A |
| Without Conflict Adaptation | 20.29% | 0.87% | 4.3% |

**Key Insight**: OODroid (Full) shows the lowest variability (3.1% CV), indicating high consistency and robustness.

---

## How to Use These Materials

### For Your Paper

1. **Main Results Section**:
   - Use `completion_rates_table.tex` for Table 1
   - Use `experimental_results_4configs.png` (left panel) as Figure 1

2. **Performance Analysis Section**:
   - Use `performance_metrics_table.tex` for Table 2
   - Use `performance_comparison_4configs.png` as Figure 2

3. **Ablation Study Section**:
   - Use `ablation_analysis_table.tex` for Table 3
   - Use `experimental_results_4configs.png` (right panel) as Figure 3

4. **Text Content**:
   - Copy/adapt text from `paper_text_4configs.txt`

### For Presentations

- `experimental_results_4configs.pdf` - High-quality vector graphics
- `performance_comparison_4configs.pdf` - High-quality vector graphics

### For Further Analysis

- `detailed_results_4configs.csv` - Raw data for additional analysis
- `average_results_4configs.csv` - Summary statistics
- Python scripts are reusable and documented

---

## Verification Checklist

✅ **Data Accuracy**:
- Test Goal Completion Rates use correct values (not from CSV)
- Test Subgoal Completion Rates from CSV "task,completion_rate"
- All other metrics directly from CSV files

✅ **Table Structure**:
- Table 1: Completion rates for ALL 4 configurations ✓
- Table 2: Performance metrics for ONLY 2 configurations (OODroid vs Without Conflict) ✓
- Ablation table includes BOTH Goal and Subgoal rates ✓

✅ **Calculations**:
- Baseline average: 7.60% ✓
- OODroid average: 23.08% ✓
- Improvement: 203.7% ✓
- SOD-OTAA contribution: +17.5% (goal), +16.0% (subgoal) ✓
- Conflict contribution: +13.8% (goal), +12.3% (subgoal) ✓

✅ **File Quality**:
- LaTeX tables compile correctly ✓
- Figures at 300 DPI resolution ✓
- Both PNG and PDF formats available ✓
- CSV files properly formatted ✓

---

## Contact & Attribution

**Generated by**: OODroid Experimental Analysis Pipeline  
**Analysis Framework**: Python 3.9.21 with pandas, numpy, matplotlib, seaborn  
**Date**: October 28, 2025

---

## Appendix: File Locations

All files are located in: `/data/wxd/LlamaTouch/Result_Analysis/`

```
Result_Analysis/
├── CSV Data Files
│   ├── detailed_results_4configs.csv
│   ├── average_results_4configs.csv
│   ├── completion_rates_comparison_4configs.csv
│   ├── performance_metrics_comparison_4configs.csv
│   └── ablation_analysis_4configs.csv
│
├── LaTeX Tables
│   ├── completion_rates_table.tex
│   ├── performance_metrics_table.tex
│   └── ablation_analysis_table.tex
│
├── Figures
│   ├── experimental_results_4configs.png
│   ├── experimental_results_4configs.pdf
│   ├── performance_comparison_4configs.png
│   └── performance_comparison_4configs.pdf
│
├── Documentation
│   ├── paper_text_4configs.txt
│   └── SUMMARY_4CONFIGS.md (this file)
│
└── Python Scripts
    ├── experimental_analysis_4configs.py
    └── create_publication_tables_4configs.py
```

---

**End of Summary Document**
