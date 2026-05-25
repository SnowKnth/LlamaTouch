# ESS Statistics for LaTeX Papers

This directory contains publication-ready figures and tables for LaTeX papers, with professional English labels and formatting.

## Generated Files for LaTeX

### 📊 Figures (PDF + PNG)

All figures are available in both **PDF** (vector graphics for LaTeX) and **PNG** (raster for preview):

1. **`fig_subgoals_distribution.pdf/.png`**
   - Distribution of key subgoals per episode
   - Shows histogram with statistics (mean, median, total)
   
2. **`fig_assertions_distribution.pdf/.png`**
   - Side-by-side comparison of total assertions vs UI-related assertions
   - Two histograms with statistics

3. **`fig_assertion_types.pdf/.png`**
   - Bar chart showing all assertion types with counts and percentages
   - Color-coded: blue for UI-related, gray for non-UI
   
4. **`fig_ui_assertions_breakdown.pdf/.png`**
   - Detailed UI assertion analysis: bar chart + pie chart
   - Shows exact/click/fuzzy breakdown and UI vs Non-UI proportion

### 📑 Tables

- **`table_ess_statistics.tex`**: Ready-to-use LaTeX table with all statistics

### 📄 Documentation

- **`ess_statistics_latex_summary.txt`**: Complete statistics and usage instructions

## LaTeX Usage

### Including Figures

Use the PDF versions for best quality in your LaTeX document:

```latex
\begin{figure}[ht]
\centering
\includegraphics[width=0.8\textwidth]{fig_subgoals_distribution.pdf}
\caption{Distribution of key subgoals per episode in the ESS dataset.}
\label{fig:subgoals_dist}
\end{figure}
```

For two-column layout (e.g., in IEEE or ACM templates):

```latex
\begin{figure}[ht]
\centering
\includegraphics[width=\columnwidth]{fig_assertion_types.pdf}
\caption{Assertion type distribution across the ESS dataset.}
\label{fig:assertion_types}
\end{figure}
```

For wide figures spanning both columns:

```latex
\begin{figure*}[ht]
\centering
\includegraphics[width=0.9\textwidth]{fig_assertions_distribution.pdf}
\caption{Comparison of total and UI-related assertion distributions.}
\label{fig:assertions_comp}
\end{figure*}
```

### Including the Table

Simply use `\input{}` to include the pre-formatted table:

```latex
\input{table_ess_statistics.tex}
```

Or reference it in text:

```latex
Table~\ref{tab:ess_statistics} shows the comprehensive statistics 
of the ESS dataset, which contains 495 episodes with 552 key states.
```

### Required LaTeX Packages

Add these to your preamble:

```latex
\usepackage{graphicx}  % For including figures
\usepackage{booktabs}  % For better table formatting (optional but recommended)
```

## Key Statistics Summary

### Dataset Overview
- **495 episodes** across 5 task categories
- **552 key states** (.ess files)
- Average **1.12 key subgoals** per episode
- Average **2.50 assertions** per key state

### Assertion Distribution
- **1,379 total assertions**
- **63.7% UI-related** (click, exact, fuzzy)
- **36.3% Non-UI** (activity, type, check_install/uninstall)

### Assertion Types (in order of frequency)
1. **Exact Match** - 698 (50.6%) - UI-related
2. **Activity Check** - 490 (35.5%)
3. **Click Action** - 98 (7.1%) - UI-related
4. **Fuzzy Match** - 82 (5.9%) - UI-related
5. **Install Check** - 7 (0.5%)
6. **Uninstall Check** - 3 (0.2%)
7. **Text Input** - 1 (0.1%)

## Example Paper Text

Here's sample text you can adapt for your paper:

```
We evaluate our approach on the ESS dataset, which comprises 495 episodes 
spanning 5 task categories: generated tasks, installation tasks, web shopping 
tasks, general tasks, and Google app tasks. The dataset contains 552 key 
states with 1,379 assertions in total. As shown in Figure~\ref{fig:assertion_types}, 
63.7\% of assertions are UI-related (exact match, click actions, and fuzzy 
match), indicating the importance of UI component interaction in mobile task 
automation. The remaining 36.3\% are non-UI assertions such as activity checks.

Table~\ref{tab:ess_statistics} presents detailed statistics of the dataset. 
On average, each episode contains 1.12 key subgoals, and each key state is 
verified by 2.50 assertions. The exact match assertion is the most frequently 
used (50.6\%), followed by activity checks (35.5\%).
```

## Figure Quality

- **Resolution**: 300 DPI for both PDF and PNG
- **Format**: PDF uses vector graphics (scalable without quality loss)
- **Fonts**: TrueType fonts compatible with LaTeX (Type 42)
- **Colors**: Print-friendly and colorblind-accessible palette
- **Style**: Publication-quality with serif fonts

## Regenerating Files

If you need to regenerate all LaTeX-ready materials:

```bash
cd /data/wxd/LlamaTouch/ess_statistics
python generate_ess_statistics_latex.py
```

## File Sizes

- PDF figures: ~22-23 KB each (vector graphics)
- PNG figures: ~128-225 KB each (300 DPI raster)
- LaTeX table: ~1 KB

## Notes

1. **Use PDF for LaTeX**: Always use the PDF versions in your LaTeX document for best quality
2. **PNG for Preview**: Use PNG files to preview in presentations or Word documents
3. **Color Printing**: The color scheme works well in both color and grayscale printing
4. **Font Compatibility**: All figures use fonts compatible with standard LaTeX distributions
5. **Table Customization**: You can modify `table_ess_statistics.tex` to match your paper's style

## Citation Template

If you use these statistics in your paper, consider including a data statement:

```latex
The ESS dataset statistics presented in this work are computed from the 
LlamaTouch benchmark dataset, which contains 495 mobile task episodes with 
manually annotated key states and assertions for automated testing.
```

---

**Generated**: October 28, 2025  
**Generator**: `generate_ess_statistics_latex.py`  
**Data Source**: `all_ess_content.json`
