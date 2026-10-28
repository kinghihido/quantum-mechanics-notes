# 第24章 · 路径积分与Feynman表述

> 量子力学有三种等价表述：波动力学（薛定谔）、矩阵力学（海森堡）、路径积分（费曼）。前两种我们在前面章节已经见过。路径积分提供了第三种视角——粒子不是沿一条确定轨迹运动，而是**同时探索所有可能的路径**，每条路径贡献一个相位 $e^{iS/\hbar}$。这种表述不仅优美，而且是量子场论和统计物理的标准工具。

---

## 24.1 从双缝到路径积分

### 24.1.1 双缝干涉的启示

双缝实验中，电子从源 $A$ 出发，经过屏上两条缝 $1,2$，到达屏幕 $B$。概率幅：

$$\langle B|A\rangle=\langle B|1\rangle\langle 1|A\rangle+\langle B|2\rangle\langle 2|A\rangle$$

如果有 $N$ 条缝，就加 $N$ 项。当缝的数目趋于无穷（屏上开无数个缝），就变成对**所有路径**积分。

### 24.1.2 核心思想

Feynman（1948）的假设：

> 粒子从 $A$ 到 $B$ 的概率幅 = 对所有连接 $A,B$ 的路径求和，每条路径贡献 $e^{iS[\text{path}]/\hbar}$

$$\langle x_f,t_f|x_i,t_i\rangle=\int\mathcal{D}[x(t)]\,e^{iS[x(t)]/\hbar}$$

其中 $S[x(t)]=\int_{t_i}^{t_f}L(x,\dot x,t)dt$ 是路径的**经典作用量**，$L$ 是拉格朗日量。

---

## 24.2 路径积分的构造

### 24.2.1 时间切片

把时间区间 $[t_i,t_f]$ 分成 $N$ 小段，每段 $\epsilon=(t_f-t_i)/N$。粒子在每段可以走任意直线路径，对所有中间位置积分。

$$\langle x_f,t_f|x_i,t_i\rangle=\lim_{N\to\infty}\left(\frac{m}{2\pi i\hbar\epsilon}\right)^{N/2}\int dx_1\cdots dx_{N-1}\exp\left[\frac{i\epsilon}{\hbar}\sum_{k=0}^{N-1}L\left(\frac{x_{k+1}+x_k}{2},\frac{x_{k+1}-x_k}{\epsilon}\right)\right]$$

### 24.2.2 自由粒子

对自由粒子 $L=\frac{1}{2}m\dot x^2$，路径积分可以精确计算（高斯积分）：

$$\langle x_f,t_f|x_i,t_i\rangle=\sqrt{\frac{m}{2\pi i\hbar(t_f-t_i)}}\exp\left[\frac{im(x_f-x_i)^2}{2\hbar(t_f-t_i)}\right]$$

这正是自由粒子的传播子（与薛定谔方程的解一致）。

### 24.2.3 测度问题

$\mathcal{D}[x(t)]$ 的严格数学定义需要泛函分析（Wiener测度的解析延拓）。物理上，时间切片构造给出了明确的计算规则。

---

## 24.3 经典极限

### 24.3.1 驻相原理

当 $\hbar\to 0$（或作用量 $S\gg\hbar$），$e^{iS/\hbar}$ 快速振荡，不同路径的贡献互相抵消——**除了**作用量取极值的路径附近。

作用量极值条件：$\delta S=0$，正是**经典运动方程**（Euler-Lagrange方程）！

$$\frac{d}{dt}\frac{\partial L}{\partial\dot x}-\frac{\partial L}{\partial x}=0$$

**物理意义**：经典力学是量子力学在 $S\gg\hbar$ 时的极限。经典轨迹之所以"特殊"，不是因为其他路径不存在，而是因为它们的相位互相抵消了。

### 24.3.2 量子修正

对经典路径附近做小涨落展开（鞍点近似），可以得到 $\hbar$ 的逐阶修正——这就是**半经典近似**。

---

## 24.4 路径积分的应用

### 24.4.1 谐振子

谐振子的路径积分可以精确计算（因为作用量是二次型）：

$$\langle x_f,t_f|x_i,t_i\rangle=\sqrt{\frac{m\omega}{2\pi i\hbar\sin\omega T}}\exp\left[\frac{im\omega}{2\hbar\sin\omega T}\left((x_f^2+x_i^2)\cos\omega T-2x_fx_i\right)\right]$$

其中 $T=t_f-t_i$。

从传播子可以读出全部能级 $E_n=\hbar\omega(n+1/2)$（极点对应能量本征值）。

### 24.4.2 Aharonov-Bohm效应

带电粒子绕过一个磁通量管（管内 $\mathbf{B}\neq 0$，管外 $\mathbf{B}=0$ 但 $\mathbf{A}\neq 0$），两条路径的相位差：

$$\Delta\phi=\frac{q}{\hbar}\oint\mathbf{A}\cdot d\mathbf{l}=\frac{q\Phi_B}{\hbar}$$

即使粒子从未进入 $\mathbf{B}\neq 0$ 的区域，干涉图样也会移动！

路径积分自然包含这个效应——每条路径的贡献中有 $e^{iq\int\mathbf{A}\cdot d\mathbf{l}/\hbar}$ 因子。1986年 Aharonov-Bohm 效应被实验精确验证。

### 24.4.3 瞬子与量子隧穿

在欧几里得时间（$\tau=it$）下，路径积分变成：

$$\int\mathcal{D}[x(\tau)]\,e^{-S_E[x(\tau)]/\hbar}$$

其中 $S_E=\int[\frac{1}{2}m\dot x^2+V(x)]d\tau$ 是欧几里得作用量。

**瞬子**（instanton）：连接两个简并真空的经典欧几里得路径。它给出了量子隧穿概率的指数因子：

$$P\sim e^{-S_E^{\text{instanton}}/\hbar}$$

应用：假真空衰变、宇宙学中的宇宙隧穿、磁化反转的量子效应。

---

## 24.5 从路径积分到量子场论

### 24.5.1 场的路径积分

把粒子坐标 $x(t)$ 推广到场构型 $\phi(\mathbf{x},t)$：

$$Z=\int\mathcal{D}[\phi]\,e^{iS[\phi]/\hbar}$$

$S[\phi]=\int\mathcal{L}(\phi,\partial_\mu\phi)d^4x$ 是场的作用量，$\mathcal{L}$ 是拉格朗日密度。

### 24.5.2 生成泛函与Feynman图

外源 $J(x)$ 下的生成泛函：

$$Z[J]=\int\mathcal{D}[\phi]\,e^{i(S[\phi]+\int J\phi\,d^4x)/\hbar}$$

对 $J$ 求泛函导数，得到各种**关联函数**（Green函数）——它们对应粒子散射的振幅。

微扰展开（把相互作用项当微扰）给出**Feynman图**——每条图对应一个积分，所有图之和就是散射振幅。

### 24.5.3 标准模型

粒子物理标准模型（QED + QCD + 电弱统一）的拉格朗日密度包含：
- 费米子场（夸克、轻子）
- 规范场（光子、胶子、W/Z玻色子）
- Higgs场

所有计算都基于场的路径积分。Feynman 图的精度（如电子 $g-2$）达到 $10^{-12}$，是物理学中最精确的理论预言。

---

## 24.6 路径积分与统计力学

### 24.6.1 Wick转动

把时间做解析延拓 $t\to-i\tau$（Wick rotation），量子路径积分变成：

$$Z=\int\mathcal{D}[x(\tau)]\,e^{-S_E/\hbar}$$

这与统计力学的**配分函数**形式完全相同：$Z=\sum e^{-E_n/k_BT}$。

对应关系：$\hbar\leftrightarrow k_BT$，欧几里得时间 $\tau$ 的周期 $\beta=\hbar/k_BT$。

### 24.6.2 量子-经典对应

$d$ 维量子系统 $\leftrightarrow$ $(d+1)$ 维经典统计系统。

这意味着：
- 一维量子粒子 $\leftrightarrow$ 二维经典统计模型（如 Ising 模型）
- 量子相变（$T=0$）$\leftrightarrow$ 经典相变（额外维度是虚时间）

这个对应是凝聚态物理和统计物理之间最深刻的联系之一。

---

## 24.7 本章小结

| 概念 | 要点 |
|---|---|
| 路径积分 | $\langle x_f|x_i\rangle=\int\mathcal{D}x\,e^{iS/\hbar}$ |
| 经典极限 | $S\gg\hbar$ 时驻相原理给出经典轨迹 |
| 传播子 | 自由粒子、谐振子可精确计算 |
| AB效应 | 磁矢势影响相位，即使 $\mathbf{B}=0$ |
| 瞬子 | 欧几里得经典路径，描述量子隧穿 |
| 量子场论 | 场的路径积分，Feynman图 |
| 统计力学对应 | Wick转动，量子-经典对应 |

---

> **下一步**：量子力学不仅是微观世界的理论，它还引出了关于**实在本质**的深刻哲学问题：测量到底发生了什么？两个遥远的粒子可以"瞬时关联"吗？量子力学是"完备"的吗？第25章讨论量子纠缠、EPR佯谬和Bell不等式——物理学中最引人深思的内容。
