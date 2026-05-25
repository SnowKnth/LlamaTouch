# 📋 OODroid 4-Configuration Analysis - File Index

**Location**: `/data/wxd/LlamaTouch/Result_Analysis/`  
**Analysis Date**: October 28, 2025  
**Status**: ✅ Complete and Verified

---

## 🎯 I Need... (Quick Navigation)

| I Need... | Use This File |
|-----------|---------------|
| **A quick overview** | `QUICK_REFERENCE_4CONFIGS.md` |
| **Complete documentation** | `COMPLETE_DELIVERABLES_4CONFIGS.md` |
| **Summary of key results** | `SUMMARY_4CONFIGS.md` |
| **LaTeX table for completion rates** | `completion_rates_table.tex` |
| **LaTeX table for performance metrics** | `performance_metrics_table.tex` |
| **LaTeX table for ablation study** | `ablation_analysis_table.tex` |
| **Main results figure** | `experimental_results_4configs.png` or `.pdf` |
| **Performance comparison figure** | `performance_comparison_4configs.png` or `.pdf` |
| **Paper text sections** | `paper_text_4configs.txt` |
| **Raw data for all experiments** | `detailed_results_4configs.csv` |
| **Average metrics by configuration** | `average_results_4configs.csv` |
| **To reproduce the analysis** | `experimental_analysis_4configs.py` |

---

## 📊 Data Files (CSV)

### 1. `detailed_results_4configs.csv` (1.7 KB)
- **Contains**: Individual results for all 10 experiments
- **Columns**: Configuration, Experiment, Goal Rate, Subgoal Rate, Page metrics, Assertion metrics
- **Use for**: Detailed analysis, statistical tests, examining individual runs

### 2. `average_results_4configs.csv` (962 bytes)
- **Contains**: Averaged metrics for each of the 4 configurations
- **Includes**: Standard deviations for configurations with multiple experiments
- **Use for**: Summary statistics, table creation, main comparisons

### 3. `completion_rates_comparison_4configs.csv` (196 bytes)
- **Contains**: **TABLE 1 DATA** - Goal and Subgoal rates for all 4 configurations
- **Use for**: Main results table, completion rate comparisons
- **Key Result**: OODroid 23.08% vs Baseline 7.60% (203.7% improvement)

### 4. `performance_metrics_comparison_4configs.csv` (435 bytes)
- **Contains**: **TABLE 2 DATA** - Page/Assertion metrics for 2 configurations only
- **Compares**: OODroid (Full) vs Without Conflict Adaptation
- **Use for**: Performance metrics table, showing trade-offs

### 5. `ablation_analysis_4configs.csv` (177 bytes)
- **Contains**: Component contribution calculations
- **Shows**: SOD-OTAA (+17.5% goal) and Conflict Adaptation (+13.8% goal)
- **Use for**: Ablation study table, component analysis

---

## 📄 LaTeX Tables (Publication-Ready)

### 1. `completion_rates_table.tex` (423 bytes)
```latex
\caption{Test Goal and Subgoal Completion Rates Comparison}
\label{tab:completion_rates}
```
- **Table Type**: Regular table (`\begin{table}[t]`)
- **Rows**: 4 (one per configuration)
- **Columns**: Configuration, Goal Rate, Subgoal Rate
- **Use in**: Results section, main findings

### 2. `performance_metrics_table.tex` (710 bytes)
```latex
\caption{Page-level and Assertion-level Performance Metrics}
\label{tab:performance_metrics}
```
- **Table Type**: Wide table (`\begin{table*}[t]`)
- **Rows**: 2 (OODroid Full and Without Conflict Adaptation)
- **Columns**: 8 metrics (4 page-level + 4 assertion-level)
- **Use in**: Performance analysis section

### 3. `ablation_analysis_table.tex` (378 bytes)
```latex
\caption{Ablation Study: Component Contributions}
\label{tab:ablation}
```
- **Table Type**: Regular table (`\begin{table}[t]`)
- **Rows**: 2 (SOD-OTAA and Conflict-based Adaptation)
- **Columns**: Component, Goal Rate Contribution, Subgoal Rate Contribution
- **Use in**: Ablation study section

**LaTeX Requirements**: All tables need `\usepackage{booktabs}` in your document preamble.

---

## 🎨 Figures (High-Resolution)

### 1. `experimental_results_4configs.png` (276 KB) / `.pdf` (30 KB)
- **Resolution**: 300 DPI
- **Format**: Two-panel figure (side by side)
- **Left Panel**: 
  - Bar chart showing Goal and Subgoal rates for all 4 configurations
  - X-axis: Configurations, Y-axis: Completion Rate (%)
  - Two bars per configuration (Goal in blue, Subgoal in red)
- **Right Panel**: 
  - Ablation study component contributions
  - X-axis: Components (SOD-OTAA, Conflict Adaptation)
  - Y-axis: Relative Improvement (%)
  - Two bars per component (Goal in green, Subgoal in orange)
- **Use in**: Main results figure (Figure 1 or 2)

### 2. `performance_comparison_4configs.png` (135 KB) / `.pdf` (23 KB)
- **Resolution**: 300 DPI
- **Format**: Two-panel figure (side by side)
- **Left Panel**: 
  - Page-level metrics comparison
  - Shows F1, Recall, Precision for OODroid vs Without Conflict
- **Right Panel**: 
  - Assertion-level metrics comparison
  - Shows F1, Recall, Precision for OODroid vs Without Conflict
- **Use in**: Performance analysis figure (Figure 3 or 4)

**Recommendation**: Use PDF versions for LaTeX papers (vector graphics), PNG for presentations.

---

## 📝 Documentation Files

### 1. `COMPLETE_DELIVERABLES_4CONFIGS.md` (12 KB)
- **Most comprehensive documentation**
- **Contains**: 
  - Executive summary
  - Complete file listing with descriptions
  - All tables with full data
  - Calculation details
  - Data correction summary
  - Statistical robustness analysis
  - Usage instructions
- **Read this when**: You need complete understanding of the analysis

### 2. `QUICK_REFERENCE_4CONFIGS.md` (6.2 KB)
- **Quick reference guide**
- **Contains**:
  - Key results at a glance
  - File recommendations for each use case
  - Understanding the 4 configurations
  - Critical data distinctions
  - Calculation formulas
  - Troubleshooting tips
- **Read this when**: You need quick answers or reminders

### 3. `SUMMARY_4CONFIGS.md` (6.9 KB)
- **Results-focused summary**
- **Contains**:
  - Key results tables
  - Experimental data sources
  - Generated materials list
  - Important notes on correct data usage
  - Ablation study calculations
  - Statistical significance
- **Read this when**: You need results and context without implementation details

### 4. `paper_text_4configs.txt` (2.9 KB)
- **Pre-written paper text sections**
- **Contains**:
  - Overall Performance section
  - Ablation Study section (with subsections)
  - Page-level and Assertion-level Performance section
- **Use when**: Writing your paper manuscript
- **Note**: Text is ready to copy/paste, may need minor adjustments for your paper style

---

## 🐍 Python Scripts (Reproducible)

### 1. `experimental_analysis_4configs.py` (9.6 KB)
- **Purpose**: Main analysis script
- **Input**: 10 CSV files from `../Evaluator/dumped_stats/`
- **Output**: 
  - `detailed_results_4configs.csv`
  - `average_results_4configs.csv`
- **Key Feature**: Correctly uses user-provided Test Goal Completion Rates
- **Run**: `conda run --name llamatouch python experimental_analysis_4configs.py`

### 2. `create_publication_tables_4configs.py` (19 KB)
- **Purpose**: Generate all publication materials
- **Input**: Results from `experimental_analysis_4configs.py`
- **Output**: 
  - 3 LaTeX tables
  - 5 CSV files
  - 4 figure files (2 PNG + 2 PDF)
  - Paper text file
- **Key Feature**: Creates separate tables as requested (Table 1 with 4 configs, Table 2 with 2 configs)
- **Run**: `conda run --name llamatouch python create_publication_tables_4configs.py`

**Dependency**: Must run `experimental_analysis_4configs.py` first!

---

## 🔍 Key Data Points Reference

### Completion Rates (%)
| Configuration | Goal | Subgoal | n |
|--------------|------|---------|---|
| Baseline AutoDroid | 7.60 | 7.39 | 3 |
| OODroid (Full) | 23.08 | 22.65 | 3 |
| Without SOD | 19.65 | 19.53 | 1 |
| Without Conflict | 20.29 | 20.17 | 3 |

### Component Contributions (%)
| Component | Goal | Subgoal |
|-----------|------|---------|
| SOD-OTAA | +17.5 | +16.0 |
| Conflict-based Adaptation | +13.8 | +12.3 |

### Individual Experiment Data
**Baseline AutoDroid**: 6.51%, 9.51%, 6.78% → 7.60%  
**OODroid (Full)**: 22.47%, 22.93%, 23.86% → 23.08%  
**Without Conflict**: 21.27%, 19.63%, 19.96% → 20.29%

---

## ⚠️ Important Notes

### Critical Data Distinction
- ❌ **WRONG**: Test Goal Rate from CSV "task,completion_rate"
- ✅ **RIGHT**: Test Goal Rate from user-provided values (hardcoded in scripts)
- ℹ️ CSV "task,completion_rate" contains **Test Subgoal Completion Rate**

### Table Structure Requirements
1. **Table 1**: Must show all 4 configurations with Goal + Subgoal rates
2. **Table 2**: Must show only 2 configurations (OODroid vs Without Conflict) with Page + Assertion metrics
3. **Ablation Table**: Must show both Goal and Subgoal contributions

### File Naming Convention
- Files ending in `_4configs`: Part of the 4-configuration analysis
- Files with `4configs` in name but not ending: Mixed legacy/new content
- Files without `4configs`: Old 3-configuration analysis (superseded)

---

## 🎓 For Your Paper

### Recommended Table Order
1. **Table 1**: `completion_rates_table.tex` - Show overall improvements
2. **Table 2**: `performance_metrics_table.tex` - Show detailed metrics
3. **Table 3**: `ablation_analysis_table.tex` - Show component contributions

### Recommended Figure Order
1. **Figure 1**: `experimental_results_4configs.pdf` (left panel) - Main completion rates
2. **Figure 2**: `experimental_results_4configs.pdf` (right panel) - Ablation study
3. **Figure 3**: `performance_comparison_4configs.pdf` - Performance metrics

### Text Flow
1. Start with overall performance (use text from `paper_text_4configs.txt`)
2. Reference Table 1 and Figure 1
3. Discuss ablation study (use text from `paper_text_4configs.txt`)
4. Reference Table 3 and Figure 2
5. Analyze performance metrics (use text from `paper_text_4configs.txt`)
6. Reference Table 2 and Figure 3

---

## 📞 Support & Troubleshooting

### If you can't find a file:
- All files are in `/data/wxd/LlamaTouch/Result_Analysis/`
- Use `ls *4configs*` to list all 4-config files

### If results look wrong:
- Verify Test Goal Rates match: 7.60%, 23.08%, 19.65%, 20.29%
- Check that scripts use hardcoded goal rates, not CSV values

### If figures don't display:
- PNG files: 300 DPI, should work in any viewer
- PDF files: Vector graphics, best for LaTeX
- Try opening with different viewer if one fails

### If you need to regenerate:
```bash
cd /data/wxd/LlamaTouch/Result_Analysis
conda run --name llamatouch python experimental_analysis_4configs.py
conda run --name llamatouch python create_publication_tables_4configs.py
```

---

## 📊 Change Log

### Version 2.0 (4-Configuration Analysis) - October 28, 2025
- ✅ Added 4th configuration (Without SOD)
- ✅ Split original baseline into separate "Baseline AutoDroid" 
- ✅ Renamed "NoUpdate" to "Without Conflict Adaptation"
- ✅ Created separate tables for completion rates (4 configs) and performance (2 configs)
- ✅ Added both Goal and Subgoal rates to ablation study
- ✅ All files clearly marked with `4configs` suffix

### Version 1.0 (3-Configuration Analysis) - October 2025
- Original analysis with incorrect Test Goal Completion Rates
- Files without `4configs` suffix
- Superseded by Version 2.0

---

**Last Updated**: October 28, 2025  
**Maintained by**: OODroid Experimental Analysis Pipeline  
**File Version**: 2.0 (4-Configuration)

---

*This index file helps you navigate all materials generated for the 4-configuration OODroid experimental analysis. For quick answers, see `QUICK_REFERENCE_4CONFIGS.md`. For comprehensive documentation, see `COMPLETE_DELIVERABLES_4CONFIGS.md`.*
