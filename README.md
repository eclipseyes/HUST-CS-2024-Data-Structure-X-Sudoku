# 基于SAT的对角线数独游戏求解程序

## 简介课程设计
这是我完成的2024年秋季数据结构课设。课设使用PyQt5实现了界面设计，并成功完成了对角线数独问题的程序，同时设计了SAT问题的求解器（包含初始版本和优化版）。验收时1-7算例能够用基础求解器解出，1-8、11能够用优化求解器解出。最后我使用相关代码和文件均已经上传到github上（用户eclipseyes）。

## 关于优化求解器的额外使用说明
对于DPLL算法，我仅从变元选择的逻辑上进行了不同方式的优化，以下是几种优化求解器的变元选择策略：
| 优化策略       | 方案1                         | 方案2               | 方案3                                |
|----------------|-------------------------------|---------------------|--------------------------------------|
| 变元选择逻辑   | 选择出现次数最多的变元         | 选择下一个变元      | 为所在子句较短的变元分配较大权重     |


对于不同的算例，选择的最佳优化策略不同。以下给出助教提供的算例包中算例编号对应的选择策略：
| 算例序号 | 优化策略 |
|----------|----------|
| 1        | 三        |
| 2        | 三        |
| 3        | 一        |
| 4        | 二        |
| 5        | 二        |
| 6        | 一        |
| 7        | 一        |
| 8        | 三        |
| 11       | 三        |

