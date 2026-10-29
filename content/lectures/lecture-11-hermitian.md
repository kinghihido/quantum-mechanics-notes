# 第11章 厄米算符与本征值问题

> **本章导读**：在量子力学中，每个可观测的力学量都对应一个厄米算符。厄米算符有三个关键性质：本征值是实数（测量结果必须是实数）、本征态正交（不同结果互斥）、本征态完备（任何态都可以展开）。这些性质不是巧合，而是量子力学公设的必然结果。本章详细讨论厄米算符的数学性质和物理意义。

---

## 11.1 算符的数学基础

### 11.1.1 线性算符

算符 $\hat{A}$ 是**线性**的，如果它满足：

$$\hat{A}(a|\psi_1\rangle + b|\psi_2\rangle) = a\hat{A}|\psi_1\rangle + b\hat{A}|\psi_2\rangle$$

量子力学中的所有算符都是线性的，这与态叠加原理一致。

### 11.1.2 算符的加法与乘法

**加法**：$(\hat{A} + \hat{B})|\psi\rangle = \hat{A}|\psi\rangle + \hat{B}|\psi\rangle$

**乘法**（复合）：$(\hat{A}\hat{B})|\psi\rangle = \hat{A}(\hat{B}|\psi\rangle)$

注意：算符乘法一般**不交换**，即 $\hat{A}\hat{B} \neq \hat{B}\hat{A$。

**对易子**：

$$[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$$

如果 $[\hat{A}, \hat{B}] = 0$，称 $\hat{A}$ 和 $\hat{B}$ **对易**。

### 11.1.3 算符的共轭转置

算符 $\hat{A}$ 的**共轭转置**（厄米共轭）$\hat{A}^\dagger$ 定义为：

$$\langle\phi|\hat{A}^\dagger|\psi\rangle = \langle\psi|\hat{A}|\phi\rangle^*$$

对任意 $|\psi\rangle, |\phi\rangle$ 成立。

**性质**：
- $(\hat{A}^\dagger)^\dagger = \hat{A}$
- $(\hat{A}\hat{B})^\dagger = \hat{B}^\dagger \hat{A}^\dagger$（注意顺序反转）
- $(a\hat{A})^\dagger = a^* \hat{A}^\dagger$

---

## 11.2 厄米算符

### 11.2.1 定义

算符 $\hat{A}$ 是**厄米算符**（自伴算符），如果：

$$\hat{A}^\dagger = \hat{A}$$

等价地：

$$\langle\phi|\hat{A}|\psi\rangle = \langle\psi|\hat{A}|\phi\rangle^*$$

或：

$$\langle\psi|\hat{A}|\psi\rangle \in \mathbb{R} \quad \text{（对任意 } |\psi\rangle \text{）}$$

### 11.2.2 为什么可观测量必须是厄米算符

**物理要求**：测量结果必须是实数。

如果 $\hat{A}$ 代表可观测量，其本征值 $a$ 是可能的测量结果。由本征方程 $\hat{A}|a\rangle = a|a\rangle$：

$$\langle a|\hat{A}|a\rangle = a\langle a|a\rangle$$

由于 $\hat{A}$ 厄米，$\langle a|\hat{A}|a\rangle$ 是实数，$\langle a|a\rangle > 0$，所以 $a$ 必须是实数。

**结论**：只有厄米算符才能保证本征值是实数，因此可观测量必须用厄米算符表示。

### 11.2.3 常见厄米算符

**位置算符** $\hat{x}$：

$$\langle\phi|\hat{x}|\psi\rangle = \int \phi^*(x) x \psi(x) dx = \int (x\phi(x))^* \psi(x) dx = \langle\psi|\hat{x}|\phi\rangle^*$$

**动量算符** $\hat{p} = -i\hbar\partial/\partial x$：

$$\langle\phi|\hat{p}|\psi\rangle = \int \phi^*(x) (-i\hbar\psi'(x)) dx$$

分部积分（边界项为零）：

$$= i\hbar \int (\phi^*(x))' \psi(x) dx = \int (-i\hbar\phi'(x))^* \psi(x) dx = \langle\psi|\hat{p}|\phi\rangle^*$$

**哈密顿算符** $\hat{H} = \hat{p}^2/(2m) + V(\hat{x})$：

由于 $\hat{p}$ 和 $\hat{x}$ 都是厄米的，且 $V(x)$ 是实函数，$\hat{H}$ 也是厄米的。

---

## 11.3 厄米算符的性质

### 11.3.1 本征值是实数

**定理**：厄米算符的本征值都是实数。

**证明**：设 $\hat{A}|a\rangle = a|a\rangle$，则：

$$\langle a|\hat{A}|a\rangle = a\langle a|a\rangle$$

由于 $\hat{A}$ 厄米，$\langle a|\hat{A}|a\rangle$ 是实数。又 $\langle a|a\rangle > 0$ 是实数，所以 $a$ 必须是实数。$\blacksquare$

### 11.3.2 不同本征值的本征态正交

**定理**：厄米算符对应不同本征值的本征态正交。

**证明**：设 $\hat{A}|a_1\rangle = a_1|a_1\rangle$，$\hat{A}|a_2\rangle = a_2|a_2\rangle$，且 $a_1 \neq a_2$。

$$\langle a_2|\hat{A}|a_1\rangle = a_1\langle a_2|a_1\rangle$$

另一方面，由于 $\hat{A}$ 厄米：

$$\langle a_2|\hat{A}|a_1\rangle = \langle a_1|\hat{A}|a_2\rangle^* = (a_2\langle a_1|a_2\rangle)^* = a_2\langle a_2|a_1\rangle$$

（$a_2$ 是实数）

两式相减：

$$(a_1 - a_2)\langle a_2|a_1\rangle = 0$$

由于 $a_1 \neq a_2$，必须 $\langle a_2|a_1\rangle = 0$。$\blacksquare$

### 11.3.3 本征态构成完备正交基

**定理**（谱定理）：厄米算符的本征态构成希尔伯特空间的完备正交基。

这意味着任意态 $|\psi\rangle$ 可以按本征态展开：

$$|\psi\rangle = \sum_n c_n |a_n\rangle$$

其中 $c_n = \langle a_n|\psi\rangle$。

**物理意义**：任何量子态都可以表示为"测量结果为 $a_n$"的态的叠加。

---

## 11.4 简并

### 11.4.1 简并的定义

如果厄米算符 $\hat{A}$ 有多个线性无关的本征态对应同一个本征值 $a$，称该本征值是**简并**的。

例如，氢原子的能级 $E_n$ 有 $n^2$ 重简并（不考虑自旋）。

### 11.4.2 简并子空间

本征值 $a$ 对应的所有本征态构成一个**简并子空间**。在这个子空间中，任何线性组合仍然是 $\hat{A}$ 的本征态，本征值都是 $a$。

### 11.4.3 解除简并

如果有另一个算符 $\hat{B}$ 与 $\hat{A}$ 对易（$[\hat{A}, \hat{B}] = 0$），则可以在简并子空间中选择 $\hat{B}$ 的本征态作为基。这样，$\hat{A}$ 和 $\hat{B}$ 的**共同本征态**可以唯一标记（本征值组 $(a, b)$）。

例如，氢原子中 $\hat{H}$、$\hat{L}^2$、$\hat{L}_z$ 两两对易，共同本征态 $|n, l, m\rangle$ 由三个量子数唯一标记。

---

## 11.5 投影算符与谱分解

### 11.5.1 投影算符

投影到本征态 $|a_n\rangle$ 的**投影算符**定义为：

$$\hat{P}_n = |a_n\rangle\langle a_n|$$

**性质**：
- **幂等性**：$\hat{P}_n^2 = \hat{P}_n$
- **厄米性**：$\hat{P}_n^\dagger = \hat{P}_n$
- **正交性**：$\hat{P}_m \hat{P}_n = \delta_{mn} \hat{P}_n$

### 11.5.2 谱分解

厄米算符可以用其本征值和本征投影算符表示：

$$\hat{A} = \sum_n a_n \hat{P}_n = \sum_n a_n |a_n\rangle\langle a_n|$$

这就是**谱分解**（spectral decomposition）。

**验证**：作用在本征态 $|a_m\rangle$ 上：

$$\hat{A}|a_m\rangle = \sum_n a_n |a_n\rangle\langle a_n|a_m\rangle = \sum_n a_n |a_n\rangle \delta_{nm} = a_m |a_m\rangle$$

正确。

### 11.5.3 函数算符

利用谱分解，可以定义算符的函数：

$$f(\hat{A}) = \sum_n f(a_n) |a_n\rangle\langle a_n|$$

例如：
- $e^{i\hat{A}} = \sum_n e^{ia_n} |a_n\rangle\langle a_n|$
- $\hat{A}^2 = \sum_n a_n^2 |a_n\rangle\langle a_n|$

---

## 11.6 对易算符的共同本征态

### 11.6.1 定理

**定理**：如果两个厄米算符 $\hat{A}$ 和 $\hat{B}$ 对易（$[\hat{A}, \hat{B}] = 0$），则它们有共同的本征态完备集。

**证明思路**：
1. 设 $\hat{A}|a\rangle = a|a\rangle$
2. 由 $[\hat{A}, \hat{B}] = 0$，得 $\hat{A}(\hat{B}|a\rangle) = \hat{B}(\hat{A}|a\rangle) = a(\hat{B}|a\rangle)$
3. 所以 $\hat{B}|a\rangle$ 也是 $\hat{A}$ 的本征态，本征值仍为 $a$
4. 如果 $a$ 非简并，$\hat{B}|a\rangle \propto |a\rangle$，即 $|a\rangle$ 也是 $\hat{B}$ 的本征态
5. 如果 $a$ 简并，可以在简并子空间中对角化 $\hat{B}$，得到共同本征态

### 11.6.2 物理意义

如果两个算符对易，它们代表的力学量可以**同时精确测量**。

例如：
- $[\hat{x}, \hat{p}_x] = i\hbar \neq 0$：位置和动量不能同时精确确定
- $[\hat{L}^2, \hat{L}_z] = 0$：角动量平方和 $z$ 分量可以同时精确确定

### 11.6.3 完全对易集（CSCO）

**完全对易集**（Complete Set of Commuting Observables, CSCO）是一组两两对易的算符，它们的共同本征值组可以**唯一标记**希尔伯特空间中的每个态。

例如，氢原子的 CSCO 是 $\{\hat{H}, \hat{L}^2, \hat{L}_z, \hat{S}_z\}$，共同本征态 $|n, l, m_l, m_s\rangle$ 唯一标记每个态。

---

## 11.7 不确定关系的算符表述

### 11.7.1 广义不确定关系

对于任意两个厄米算符 $\hat{A}$ 和 $\hat{B}$，定义 $\Delta\hat{A} = \hat{A} - \langle A\rangle$，$\Delta\hat{B} = \hat{B} - \langle B\rangle$。

**罗伯逊不确定关系**：

$$\sigma_A^2 \sigma_B^2 \geq \frac{1}{4}|\langle[\hat{A}, \hat{B}]\rangle|^2$$

或：

$$\sigma_A \sigma_B \geq \frac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|$$

### 11.7.2 推导

利用柯西-施瓦茨不等式：

$$\sigma_A^2 \sigma_B^2 = \langle(\Delta A)^2\rangle \langle(\Delta B)^2\rangle \geq |\langle\Delta A \Delta B\rangle|^2$$

将 $\Delta A \Delta B$ 分解为对易子和反对易子：

$$\Delta A \Delta B = \frac{1}{2}[\Delta A, \Delta B] + \frac{1}{2}\{\Delta A, \Delta B\}$$

其中 $[\Delta A, \Delta B] = [\hat{A}, \hat{B}]$，$\{\Delta A, \Delta B\}$ 是厄米的。

由于 $[\hat{A}, \hat{B}]$ 是反厄米的（$(i[\hat{A}, \hat{B}])^\dagger = i[\hat{A}, \hat{B}]$），其期望值是纯虚数；而 $\{\Delta A, \Delta B\}$ 是厄米的，其期望值是实数。

所以：

$$|\langle\Delta A \Delta B\rangle|^2 = \frac{1}{4}|\langle[\hat{A}, \hat{B}]\rangle|^2 + \frac{1}{4}|\langle\{\Delta A, \Delta B\}\rangle|^2 \geq \frac{1}{4}|\langle[\hat{A}, \hat{B}]\rangle|^2$$

因此 $\sigma_A \sigma_B \geq \frac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|$。$\blacksquare$

### 11.7.3 位置-动量不确定关系

取 $\hat{A} = \hat{x}$，$\hat{B} = \hat{p}_x$，$[\hat{x}, \hat{p}_x] = i\hbar$：

$$\sigma_x \sigma_p \geq \frac{1}{2}|i\hbar| = \frac{\hbar}{2}$$

这正是海森堡不确定关系。

### 11.7.4 能量-时间不确定关系

能量-时间不确定关系的形式为：

$$\Delta E \Delta t \geq \frac{\hbar}{2}$$

但要注意：时间 $t$ 在量子力学中不是算符，而是参数。这个关系的严格推导需要用到 Ehrenfest 定理，我们将在第14章讨论。

---

## 本章小结

1. **厄米算符**：$\hat{A}^\dagger = \hat{A}$，本征值是实数，本征态正交完备。

2. **可观测量**：必须用厄米算符表示，保证测量结果是实数。

3. **谱分解**：$\hat{A} = \sum_n a_n |a_n\rangle\langle a_n|$，是算符的"对角化"。

4. **对易算符**：有共同本征态，对应的力学量可以同时精确测量。

5. **CSCO**：完全对易集，共同本征值组唯一标记量子态。

6. **不确定关系**：$\sigma_A \sigma_B \geq \frac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|$，对易子越大，同时测量越模糊。

---

## 公式索引

| 编号 | 公式 | 含义 | 推导链接 |
|------|------|------|----------|
| [F170](#graph?f=F170) | $\hat{A} = \sum_n a_n |a_n\rangle\langle a_n|$ | 谱分解 | [查看推导](#graph?f=F170) |
| [F171](#graph?f=F171) | $[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$ | 正则对易关系 | [查看推导](#graph?f=F171) |
| [F172](#graph?f=F172) | $[\hat{A}, \hat{B}] = 0 \Rightarrow$ 共同本征态 | 相容观测量 | [查看推导](#graph?f=F172) |
| [F173](#graph?f=F173) | $\sigma_A \sigma_B \geq \frac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|$ | 广义不确定关系 | [查看推导](#graph?f=F173) |

---

## 思考题

1. 为什么厄米算符的本征值必须是实数？如果算符不是厄米的，本征值会怎样？

2. 验证动量算符 $\hat{p} = -i\hbar\partial/\partial x$ 是厄米的。

3. 如果两个算符不对易，它们能否有共同本征态？举例说明。

4. 什么是CSCO？为什么需要CSCO来标记量子态？

5. 从广义不确定关系推导位置-动量不确定关系。

---


