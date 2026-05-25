# ESS统计分析总结

## 生成的文件

### 📊 统计图表

1. **`subgoals_per_trace_distribution.png`**
   - 每个episode（trace）的key subgoals（.ess文件）数量分布
   - 包含直方图和箱线图
   - 显示大多数episode有1-2个key subgoals

2. **`assertions_per_ess_distribution.png`**
   - 每个key state（.ess文件）的assertion数量分布
   - 对比总assertions vs UI相关assertions
   - 包含直方图、箱线图和饼图，显示UI vs 非UI assertions的占比

3. **`ui_assertion_types_distribution.png`**
   - UI组件相关assertions的详细分布：`click`、`exact`和`fuzzy`
   - 每种类型的独立直方图
   - 对比柱状图显示总数

4. **`overall_assertion_types.png`**
   - 所有assertion类型的整体分布
   - 柱状图和饼图显示各类型的占比

5. **`comprehensive_overview_cn.png`** ⭐
   - 综合概览图（中文标签）
   - 包含所有关键统计信息的一页式总结

### 📄 报告

- **`ess_statistics_summary.txt`**: 详细的文本统计摘要

### 🔧 代码

- **`generate_ess_statistics.py`**: 生成所有统计图表的Python脚本（英文版）
- **`generate_ess_statistics_cn.py`**: 生成综合概览图的Python脚本（中文版）

## 核心发现

### Episode统计
- **Episode总数**: 495
- **Key State总数（.ess文件）**: 552
- **平均每个Episode的Key Subgoals**: 1.12个
- **中位数**: 1.0
- **范围**: 1-3个key subgoals

### Assertion统计
- **Assertion总数**: 1,379
- **平均每个Key State**: 2.50个
- **UI相关Assertions**: 878个（63.7%）
- **非UI Assertions**: 501个（36.3%）

### Assertion类型详细分布

#### UI相关Assertions（占总数的63.7%）

1. **`exact`**: 698个（50.6%）
   - 精确匹配UI组件
   - 最常用的assertion类型
   - 平均每个.ess文件1.26个
   - 451个.ess文件包含此类型

2. **`click`**: 98个（7.1%）
   - 点击操作
   - 平均每个.ess文件0.18个
   - 97个.ess文件包含此类型

3. **`fuzzy`**: 82个（5.9%）
   - 模糊匹配UI组件
   - 平均每个.ess文件0.15个
   - 77个.ess文件包含此类型

#### 非UI Assertions（占总数的36.3%）

1. **`activity`**: 490个（35.5%）
   - Activity级别的检查
   - 第二常用的assertion类型

2. **`check_install`**: 7个（0.5%）
   - 安装检查

3. **`check_uninstall`**: 3个（0.2%）
   - 卸载检查

4. **`type`**: 1个（0.1%）
   - 文本输入

## 关键洞察

### 1. Episode结构简单
- 大多数episode只包含1个key subgoal（中位数=1）
- 平均1.12个，标准差0.33
- 最多3个key subgoals

### 2. UI相关Assertions占主导
- 63.7%的assertions与UI组件相关（click, exact, fuzzy）
- 表明测试重点在UI交互验证

### 3. Exact匹配最常用
- `exact`类型占所有assertions的50.6%
- 超过80%的.ess文件（451/552）包含exact assertions
- 表明精确UI元素定位是主要验证方式

### 4. 每个Key State包含适度数量的Assertions
- 平均2.50个assertions每个.ess文件
- 中位数2.0
- 范围1-7个

## 数据来源

分析基于`all_ess_content.json`，包含来自不同任务类别的ESS数据：
- `generated/` - 生成的任务
- `install/` - 安装任务
- `webshopping/` - 网购任务
- `general/` - 通用任务
- `googleapps/` - Google应用任务

## 如何重新生成

### 生成英文版图表
```bash
cd /data/wxd/LlamaTouch/ess_statistics
python generate_ess_statistics.py
```

### 生成中文版综合概览图
```bash
cd /data/wxd/LlamaTouch/ess_statistics
python generate_ess_statistics_cn.py
```

### 依赖包
- Python 3.x
- matplotlib
- numpy
- seaborn

## ESS格式说明

每个.ess文件路径映射到一个assertion字符串，格式为：
```
assertion_type<value>|assertion_type<value>|...
```

示例: `"activity<0>|exact<28>|exact<19>"` 表示：
- 1个activity assertion（在索引0）
- 2个exact match assertions（在索引28和19）

---

**生成日期**: 2025年10月28日
**分析的.ess文件数**: 552
**分析的Episode数**: 495
