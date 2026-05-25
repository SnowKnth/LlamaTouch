# ESS Statistics Analysis

This directory contains statistical analysis and visualizations of the ESS (Episode SubgoalS) data from the LlamaTouch dataset.

## Generated Files

### 📊 Charts

1. **`subgoals_per_trace_distribution.png`**
   - Distribution of the number of key subgoals (.ess files) per episode (trace)
   - Includes histogram and box plot
   - Shows that most episodes have 1-2 key subgoals

2. **`assertions_per_ess_distribution.png`**
   - Distribution of assertions per key state (.ess file)
   - Compares total assertions vs UI-related assertions
   - Includes histograms, box plots, and a pie chart showing the proportion of UI vs Non-UI assertions

3. **`ui_assertion_types_distribution.png`**
   - Detailed breakdown of UI component-related assertions: `click`, `exact`, and `fuzzy`
   - Individual histograms for each type
   - Comparison bar chart showing total counts

4. **`overall_assertion_types.png`**
   - Overall distribution of all assertion types
   - Bar chart and pie chart showing the proportion of each assertion type

### 📄 Reports

- **`ess_statistics_summary.txt`**: Comprehensive text summary with all statistics

### 🔧 Code

- **`generate_ess_statistics.py`**: Python script to generate all statistics and charts

## Key Findings

### Episode Statistics
- **Total Episodes**: 495
- **Total Key States (.ess files)**: 552
- **Average Key Subgoals per Episode**: 1.12
- **Median**: 1.0
- **Range**: 1-3 key subgoals per episode

### Assertion Statistics
- **Total Assertions**: 1,379
- **Average per Key State**: 2.50
- **UI-related Assertions**: 878 (63.7% of total)
- **Non-UI Assertions**: 501 (36.3% of total)

### Assertion Type Breakdown

#### UI-Related Assertions (63.7% total)
1. **`exact`**: 698 assertions (50.6%) - Exact match on UI components
2. **`click`**: 98 assertions (7.1%) - Click actions
3. **`fuzzy`**: 82 assertions (5.9%) - Fuzzy match on UI components

#### Non-UI Assertions (36.3% total)
1. **`activity`**: 490 assertions (35.5%) - Activity-level checks
2. **`check_install`**: 7 assertions (0.5%) - Installation checks
3. **`check_uninstall`**: 3 assertions (0.2%) - Uninstallation checks
4. **`type`**: 1 assertion (0.1%) - Text input

## How to Regenerate

To regenerate the statistics and charts:

```bash
cd /data/wxd/LlamaTouch/ess_statistics
python generate_ess_statistics.py
```

### Requirements
- Python 3.x
- matplotlib
- numpy
- seaborn

## Data Source

The analysis is based on `all_ess_content.json` in the parent directory, which contains ESS data from various task categories:
- `generated/` - Generated tasks
- `install/` - Installation tasks
- `webshopping/` - Web shopping tasks
- `general/` - General tasks
- `googleapps/` - Google apps tasks

## Understanding ESS Format

Each .ess file path maps to an assertion string with the format:
```
assertion_type<value>|assertion_type<value>|...
```

Example: `"activity<0>|exact<28>|exact<19>"` means:
- 1 activity assertion at index 0
- 2 exact match assertions at indices 28 and 19

---

Generated on: October 28, 2025
