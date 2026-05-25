"""
ESS统计图表生成器（中文版）
分析ESS数据并生成统计图表（带中文标签）
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict, Counter
import seaborn as sns
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.figsize'] = (14, 9)
plt.rcParams['font.size'] = 11

sns.set_style("whitegrid")

def load_ess_data(filepath):
    """加载ESS数据"""
    with open(filepath, 'r') as f:
        return json.load(f)

def parse_assertions(assertion_string):
    """解析assertion字符串"""
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
    """分析ESS数据"""
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

def plot_comprehensive_overview_cn(stats, output_dir):
    """生成综合概览图（中文）"""
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # 1. 每个episode的key subgoals分布
    ax1 = fig.add_subplot(gs[0, :2])
    data = stats['subgoals_per_trace']
    ax1.hist(data, bins=range(1, max(data) + 2), edgecolor='black', alpha=0.7, color='#5DADE2')
    ax1.set_xlabel('每个Episode的Key Subgoals数量', fontsize=13, fontweight='bold')
    ax1.set_ylabel('频次 (Episodes数量)', fontsize=13, fontweight='bold')
    ax1.set_title('每个Episode的Key Subgoals分布', fontsize=15, fontweight='bold', pad=15)
    ax1.grid(True, alpha=0.3)
    
    mean_val = np.mean(data)
    median_val = np.median(data)
    stats_text = f'平均值: {mean_val:.2f}\n中位数: {median_val:.1f}\n最大值: {max(data)}\n最小值: {min(data)}\nEpisode总数: {len(data)}'
    ax1.text(0.98, 0.97, stats_text, transform=ax1.transAxes,
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9),
             fontsize=11)
    
    # 2. Box plot
    ax2 = fig.add_subplot(gs[0, 2])
    bp = ax2.boxplot(data, vert=True, patch_artist=True,
                     boxprops=dict(facecolor='#5DADE2', alpha=0.7),
                     medianprops=dict(color='red', linewidth=2.5),
                     whiskerprops=dict(linewidth=1.5),
                     capprops=dict(linewidth=1.5))
    ax2.set_ylabel('Key Subgoals数量', fontsize=12, fontweight='bold')
    ax2.set_title('分布箱线图', fontsize=13, fontweight='bold', pad=10)
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.set_xticklabels(['Episodes'])
    
    # 3. 每个key state的assertions分布
    ax3 = fig.add_subplot(gs[1, 0])
    data_total = stats['assertions_per_ess']
    ax3.hist(data_total, bins=range(0, max(data_total) + 2), edgecolor='black', alpha=0.7, color='#EC7063')
    ax3.set_xlabel('每个Key State的Assertions总数', fontsize=12, fontweight='bold')
    ax3.set_ylabel('频次', fontsize=12, fontweight='bold')
    ax3.set_title('Assertions总数分布', fontsize=13, fontweight='bold', pad=10)
    ax3.grid(True, alpha=0.3)
    
    mean_val = np.mean(data_total)
    stats_text = f'平均: {mean_val:.2f}\n中位数: {np.median(data_total):.1f}'
    ax3.text(0.95, 0.95, stats_text, transform=ax3.transAxes,
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9),
             fontsize=10)
    
    # 4. UI相关assertions分布
    ax4 = fig.add_subplot(gs[1, 1])
    data_ui = stats['ui_assertions_per_ess']
    ax4.hist(data_ui, bins=range(0, max(data_ui) + 2), edgecolor='black', alpha=0.7, color='#58D68D')
    ax4.set_xlabel('每个Key State的UI相关Assertions', fontsize=12, fontweight='bold')
    ax4.set_ylabel('频次', fontsize=12, fontweight='bold')
    ax4.set_title('UI相关Assertions分布', fontsize=13, fontweight='bold', pad=10)
    ax4.grid(True, alpha=0.3)
    
    mean_val = np.mean(data_ui)
    stats_text = f'平均: {mean_val:.2f}\n中位数: {np.median(data_ui):.1f}'
    ax4.text(0.95, 0.95, stats_text, transform=ax4.transAxes,
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9),
             fontsize=10)
    
    # 5. UI vs 非UI占比
    ax5 = fig.add_subplot(gs[1, 2])
    total_ui = sum(data_ui)
    total_all = sum(data_total)
    total_non_ui = total_all - total_ui
    
    sizes = [total_ui, total_non_ui]
    labels = [f'UI相关\n{total_ui}\n({total_ui/total_all*100:.1f}%)',
              f'非UI\n{total_non_ui}\n({total_non_ui/total_all*100:.1f}%)']
    colors = ['#58D68D', '#F8B739']
    explode = (0.05, 0)
    
    ax5.pie(sizes, explode=explode, labels=labels, colors=colors,
            shadow=True, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
    ax5.set_title('UI vs 非UI Assertions占比', fontsize=13, fontweight='bold', pad=10)
    
    # 6. UI assertion类型详细分布
    ax6 = fig.add_subplot(gs[2, :])
    assertion_counts = stats['assertion_type_counts']
    
    # 按类别分组
    ui_types = ['click', 'exact', 'fuzzy']
    non_ui_types = ['activity', 'type', 'check_install', 'check_uninstall']
    
    type_names_cn = {
        'exact': 'exact\n(精确匹配)',
        'click': 'click\n(点击)',
        'fuzzy': 'fuzzy\n(模糊匹配)',
        'activity': 'activity\n(活动)',
        'type': 'type\n(输入)',
        'check_install': 'check_install\n(安装检查)',
        'check_uninstall': 'check_uninstall\n(卸载检查)'
    }
    
    all_types = ui_types + non_ui_types
    type_names = [type_names_cn[t] for t in all_types]
    counts = [assertion_counts[t] for t in all_types]
    colors_list = ['#E74C3C', '#3498DB', '#F39C12'] + ['#95A5A6', '#9B59B6', '#1ABC9C', '#E67E22']
    
    bars = ax6.bar(range(len(all_types)), counts, color=colors_list, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax6.set_xticks(range(len(all_types)))
    ax6.set_xticklabels(type_names, fontsize=11)
    ax6.set_ylabel('总数', fontsize=13, fontweight='bold')
    ax6.set_title('各类Assertion类型的总数分布', fontsize=15, fontweight='bold', pad=15)
    ax6.grid(True, alpha=0.3, axis='y')
    
    # 添加数值标签
    for i, (bar, count) in enumerate(zip(bars, counts)):
        height = bar.get_height()
        percentage = count / sum(counts) * 100
        ax6.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(count)}\n({percentage:.1f}%)',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # 添加UI相关区域标注
    ax6.axvspan(-0.5, 2.5, alpha=0.1, color='green', label='UI相关')
    ax6.axvspan(2.5, len(all_types)-0.5, alpha=0.1, color='orange', label='非UI')
    ax6.legend(loc='upper right', fontsize=11)
    
    plt.savefig(os.path.join(output_dir, 'comprehensive_overview_cn.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ 已生成: comprehensive_overview_cn.png")

def main():
    input_file = '../all_ess_content.json'
    output_dir = '.'
    
    print("=" * 80)
    print("ESS统计分析（中文版）")
    print("=" * 80)
    print()
    
    print("正在加载数据...")
    data = load_ess_data(input_file)
    print(f"✓ 已加载 {len(data)} 个.ess文件\n")
    
    print("正在分析数据...")
    stats, traces, ess_assertions = analyze_ess_data(data)
    print(f"✓ 已分析 {len(traces)} 个episodes\n")
    
    print("正在生成综合统计图...")
    plot_comprehensive_overview_cn(stats, output_dir)
    
    print("\n" + "=" * 80)
    print("统计图表生成完成！")
    print(f"输出目录: {os.path.abspath(output_dir)}")
    print("=" * 80)

if __name__ == '__main__':
    main()
