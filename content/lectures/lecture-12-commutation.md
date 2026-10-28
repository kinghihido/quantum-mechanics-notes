# 第12章 对易关系与相容观测量

> **本章导读**：对易关系是量子力学的"宪法条款"。正则对易关系 $[\hat{x}, \hat{p}] = i\hbar$ 定义了位置和动量的基本关系，由此导出不确定关系、角动量代数、谐振子代数等一系列重要结果。两个算符对易意味着它们有共同本征态，对应的力学量可以同时精确测量。本章系统讨论对易关系的数学性质和物理应用。

---

## 12.1 对易子的基本性质

### 12.1.1 定义

两个算符 $\hat{A}$ 和 $\hat{B}$ 的**对易子**（commutator）定义为：

$$[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$$

如果 $[\hat{A}, \hat{B}] = 0$，称 $\hat{A}$ 和 $\hat{B}$ **对易**。

### 12.1.2 对易子的代数性质

**反对称性**：

$$[\hat{A}, \hat{B}] = -[\hat{B}, \hat{A}]$$

**线性**：

$$[a\hat{A} + b\hat{B}, \hat{C}] = a[\hat{A}, \hat{C}] + b[\hat{B}, \hat{C}]$$

**莱布尼茨法则**（类似乘积求导）：

$$[\hat{A}, \hat{B}\hat{C}] = [\hat{A}, \hat{B}]\hat{C} + \hat{B}[\hat{A}, \hat{C}]$$

$$[\hat{A}\hat{B}, \hat{C}] = [\hat{A}, \hat{C}]\hat{B} + \hat{A}[\hat{B}, \hat{C}]$$

**雅可比恒等式**：

$$[\hat{A}, [\hat{B}, \hat{C}]] + [\hat{B}, [\hat{C}, \hat{A}]] + [\hat{C}, [\hat{A}, \hat{B}]] = 0$$

### 12.1.3 常用对易关系

**位置-动量对易关系**：

$$[\hat{x}, \hat{p}_x] = i\hbar$$

$$[\hat{x}, \hat{p}_y] = 0, \quad [\hat{x}, \hat{y}] = 0, \quad [\hat{p}_x, \hat{p}_y] = 0$$

**角动量对易关系**（将在第15章详细讨论）：

$$[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$$

$$[\hat{L}_y, \hat{L}_z] = i\hbar\hat{L}_x$$

$$[\hat{L}_z, \hat{L}_x] = i\hbar\hat{L}_y$$

---

## 12.2 正则对易关系

### 12.2.1 一维情况

$$[\hat{x}, \hat{p}] = i\hbar$$

**验证**：作用在任意波函数 $\psi(x)$ 上：

$$[\hat{x}, \hat{p}]\psi = \hat{x}\hat{p}\psi - \hat{p}\hat{x}\psi$$

$$= x(-i\hbar\psi') - (-i\hbar)(x\psi)'$$

$$= -i\hbar x\psi' + i\hbar(\psi + x\psi')$$

$$= i\hbar\psi$$

所以 $[\hat{x}, \hat{p}] = i\hbar$。

### 12.2.2 三维情况

$$[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$$

$$[\hat{x}_i, \hat{x}_j] = 0$$

$$[\hat{p}_i, \hat{p}_j] = 0$$

其中 $i, j \in \{x, y, z\}$，$\delta_{ij}$ 是克罗内克δ。

### 12.2.3 物理意义

正则对易关系 $[\hat{x}, \hat{p}] = i\hbar$ 是量子力学的**基本假设**之一，它：

1. **定义了量子力学**：经典力学中 $x$ 和 $p$ 是对易的（普通数），量子力学中它们不对易。

2. **导致不确定关系**：由罗伯逊不等式，$\sigma_x \sigma_p \geq \hbar/2$。

3. **决定动力学**：海森堡运动方程 $d\hat{A}/dt = (i/\hbar)[\hat{H}, \hat{A}] + \partial\hat{A}/\partial t$。

---

## 12.3 对易与共同本征态

### 12.3.1 定理

**定理**：如果两个厄米算符 $\hat{A}$ 和 $\hat{B}$ 对易，则它们有共同的本征态完备集。

**证明**（非简并情况）：

设 $\hat{A}|a\rangle = a|a\rangle$，且 $a$ 非简并。

由 $[\hat{A}, \hat{B}] = 0$：

$$\hat{A}(\hat{B}|a\rangle) = \hat{B}(\hat{A}|a\rangle) = \hat{B}(a|a\rangle) = a(\hat{B}|a\rangle)$$

所以 $\hat{B}|a\rangle$ 也是 $\hat{A}$ 的本征态，本征值为 $a$。

由于 $a$ 非简并，$\hat{A}$ 的本征值为 $a$ 的本征态只有一个（差一个常数倍），所以：

$$\hat{B}|a\rangle = b|a\rangle$$

即 $|a\rangle$ 也是 $\hat{B}$ 的本征态，本征值为 $b$。$\blacksquare$

### 12.3.2 简并情况

如果 $a$ 是简并的，$\hat{B}|a\rangle$ 仍在简并子空间中，但不一定与 $|a\rangle$ 成正比。

解决方法：在简并子空间中对角化 $\hat{B}$，得到 $\hat{A}$ 和 $\hat{B}$ 的共同本征态。

### 12.3.3 物理意义

**对易 = 可同时测量**：

如果 $[\hat{A}, \hat{B}] = 0$，则 $\hat{A}$ 和 $\hat{B}$ 有共同本征态。在共同本征态中，$\hat{A}$ 和 $\hat{B}$ 都有确定的值，可以同时精确测量。

**不对易 = 不可同时测量**：

如果 $[\hat{A}, \hat{B}] \neq 0$，则 $\hat{A}$ 和 $\hat{B}$ 没有共同本征态完备集。一般不能同时精确测量（不确定关系）。

---

## 12.4 相容观测量

### 12.4.1 定义

两个力学量 $A$ 和 $B$ 是**相容的**（compatible），如果它们的算符对易：$[\hat{A}, \hat{B}] = 0$。

相容的力学量可以同时精确测量，有共同本征态。

### 12.4.2 不相容观测量

如果 $[\hat{A}, \hat{B}] \neq 0$，称 $A$ 和 $B$ 是**不相容的**（incompatible）。

不相容的力学量不能同时精确测量，满足不确定关系：

$$\sigma_A \sigma_B \geq \frac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|$$

### 12.4.3 例子

**相容的例子**：
- $\hat{H}$ 和 $\hat{p}$（自由粒子）：$[\hat{H}, \hat{p}] = 0$，能量和动量可以同时确定
- $\hat{L}^2$ 和 $\hat{L}_z$：$[\hat{L}^2, \hat{L}_z] = 0$，角动量平方和 $z$ 分量可以同时确定

**不相容的例子**：
- $\hat{x}$ 和 $\hat{p}_x$：$[\hat{x}, \hat{p}_x] = i\hbar \neq 0$
- $\hat{L}_x$ 和 $\hat{L}_y$：$[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z \neq 0$

---

## 12.5 完全对易集（CSCO）

### 12.5.1 定义

**完全对易集**（Complete Set of Commuting Observables, CSCO）是一组两两对易的厄米算符 $\{\hat{A}_1, \hat{A}_2, \ldots, \hat{A}_k\}$，满足：

1. 两两对易：$[\hat{A}_i, \hat{A}_j] = 0$（对所有 $i, j$）
2. 共同本征值组 $(a_1, a_2, \ldots, a_k)$ 唯一标记希尔伯特空间中的每个态

### 12.5.2 为什么需要CSCO

在量子力学中，一个态需要一组量子数来标记。CSCO 提供了这组量子数的物理来源。

例如：
- **一维谐振子**：CSCO = $\{\hat{H}\}$，一个量子数 $n$ 标记态 $|n\rangle$
- **氢原子**：CSCO = $\{\hat{H}, \hat{L}^2, \hat{L}_z, \hat{S}_z\}$，四个量子数 $(n, l, m_l, m_s)$ 标记态 $|n, l, m_l, m_s\rangle$
- **自旋1/2粒子**：CSCO = $\{\hat{S}_z\}$，一个量子数 $m_s = \pm 1/2$ 标记态

### 12.5.3 CSCO的选取

CSCO 的选取不是唯一的，但必须满足：
1. 算符两两对易
2. 共同本征值组唯一标记每个态（无简并）

例如，氢原子中也可以选 $\{\hat{H}, \hat{L}^2, \hat{L}_x, \hat{S}_x\}$ 作为 CSCO，但通常选 $z$ 分量更方便。

---

## 12.6 对易关系的应用

### 12.6.1 海森堡运动方程

算符 $\hat{A}$ 的期望值随时间的演化由 Ehrenfest 定理给出：

$$\frac{d\langle A\rangle}{dt} = \frac{i}{\hbar}\langle[\hat{H}, \hat{A}]\rangle + \left\langle\frac{\partial\hat{A}}{\partial t}\right\rangle$$

如果 $\hat{A}$ 不显含时间且与 $\hat{H}$ 对易，则 $\langle A\rangle$ 守恒。

### 12.6.2 守恒量

**定理**：如果 $[\hat{H}, \hat{A}] = 0$ 且 $\partial\hat{A}/\partial t = 0$，则 $\hat{A}$ 是守恒量。

**证明**：由 Ehrenfest 定理，$d\langle A\rangle/dt = 0$。更严格地，$\hat{A}$ 在薛定谔绘景中不随时间演化，在海森堡绘景中 $\hat{A}_H(t) = \hat{A}_H(0)$。

**例子**：
- 自由粒子：$[\hat{H}, \hat{p}] = 0$，动量守恒
- 中心力场：$[\hat{H}, \hat{L}^2] = 0$，$[\hat{H}, \hat{L}_z] = 0$，角动量守恒

### 12.6.3 对称性与守恒律

**诺特定理**（量子版本）：每条连续对称性对应一个守恒量。

- **空间平移对称性** → 动量守恒
- **时间平移对称性** → 能量守恒
- **旋转对称性** → 角动量守恒

生成元与守恒量的关系：

$$\hat{G} = \frac{\hat{Q}}{\hbar}$$

其中 $\hat{G}$ 是连续对称变换的生成元，$\hat{Q}$ 是对应的守恒量。

---

## 12.7 不确定关系的深入讨论

### 12.7.1 最小不确定态

不确定关系 $\sigma_A \sigma_B \geq \frac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|$ 的下限何时达到？

**条件**：当且仅当 $(\Delta\hat{A} + i\lambda\Delta\hat{B})|\psi\rangle = 0$（$\lambda$ 为实数）时，等号成立。

### 12.7.2 位置-动量的最小不确定态

对 $\hat{x}$ 和 $\hat{p}$，最小不确定态满足：

$$(\hat{x} - \langle x\rangle + i\lambda(\hat{p} - \langle p\rangle))|\psi\rangle = 0$$

在坐标表象中，这是微分方程：

$$\left(x - \langle x\rangle + \lambda\hbar\frac{d}{dx} - i\lambda\langle p\rangle\right)\psi(x) = 0$$

解为高斯波包：

$$\psi(x) = N \exp\left(-\frac{(x - \langle x\rangle)^2}{4\sigma_x^2} + \frac{i\langle p\rangle x}{\hbar}\right)$$

其中 $\sigma_x \sigma_p = \hbar/2$。

### 12.7.3 相干态

谐振子的**相干态**是位置和动量的最小不确定态，且 $\sigma_x$ 和 $\sigma_p$ 不随时间变化。相干态在量子光学和量子信息中有重要应用。

---

## 本章小结

1. **对易子**：$[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$，满足反对称性、线性、莱布尼茨法则、雅可比恒等式。

2. **正则对易关系**：$[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$，是量子力学的基本假设。

3. **对易与共同本征态**：$[\hat{A}, \hat{B}] = 0 \Rightarrow$ 有共同本征态完备集。

4. **相容观测量**：对易的力学量可以同时精确测量。

5. **CSCO**：完全对易集，共同本征值组唯一标记量子态。

6. **守恒量**：$[\hat{H}, \hat{A}] = 0 \Rightarrow \hat{A}$ 守恒。

7. **最小不确定态**：高斯波包达到不确定关系下限。

---

## 公式索引

| 编号 | 公式 | 含义 | 推导链接 |
|------|------|------|----------|
| [F171](#graph?f=F171) | $[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$ | 正则对易关系 | [查看推导](#graph?f=F171) |
| [F172](#graph?f=F172) | $[\hat{A}, \hat{B}] = 0 \Rightarrow$ 共同本征态 | 相容观测量 | [查看推导](#graph?f=F172) |
| [F173](#graph?f=F173) | $\sigma_A \sigma_B \geq \frac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|$ | 广义不确定关系 | [查看推导](#graph?f=F173) |

---

## 思考题

1. 验证对易子的莱布尼茨法则：$[\hat{A}, \hat{B}\hat{C}] = [\hat{A}, \hat{B}]\hat{C} + \hat{B}[\hat{A}, \hat{C}]$。

2. 为什么 $[\hat{x}, \hat{p}] = i\hbar$ 导致不确定关系？

3. 如果两个算符不对易，它们能否有某些共同本征态？举例说明。

4. 什么是CSCO？为什么氢原子需要四个算符构成CSCO？

5. 最小不确定态为什么是高斯波包？

---

**上一章**：[第11章 厄米算符与本征值问题](lecture-11-hermitian.md)

**下一章**：[第13章 时间演化与守恒量](lecture-13-time-evolution.md)
