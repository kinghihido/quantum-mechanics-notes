# 第9章 态矢量与Dirac符号

> **本章导读**：到目前为止，我们用波函数 $\psi(\vec{r}, t)$ 描述量子态。波函数是位置和时间的函数，定义在三维空间中。但量子力学有一个更抽象、更强大的表述方式：Dirac 符号。在这个框架中，量子态被看作希尔伯特空间中的矢量，力学量是作用在矢量上的算符。这种表述不仅更简洁，而且揭示了量子力学的深层数学结构。

---

## 9.1 希尔伯特空间

### 9.1.1 从波函数到态矢量

波函数 $\psi(\vec{r}, t)$ 是坐标的复函数。但我们可以从更抽象的角度看待它：波函数是某个抽象空间中的"矢量"。

**类比**：在三维空间中，一个矢量 $\vec{v}$ 可以用分量表示：$\vec{v} = (v_x, v_y, v_z)$。分量依赖于坐标系的选择，但矢量本身是客观存在的。

类似地，波函数 $\psi(\vec{r})$ 可以看作某个抽象空间中的"矢量"在"坐标基"下的分量。这个抽象空间叫做**希尔伯特空间**（Hilbert space）。

### 9.1.2 希尔伯特空间的定义

希尔伯特空间 $\mathcal{H}$ 是一个满足以下条件的向量空间：

1. **线性空间**：可以相加、数乘
2. **内积**：任意两个矢量 $|\psi\rangle, |\phi\rangle$ 有内积 $\langle\phi|\psi\rangle$，满足：
   - 共轭对称：$\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*$
   - 线性：$\langle\phi|(a|\psi_1\rangle + b|\psi_2\rangle) = a\langle\phi|\psi_1\rangle + b\langle\phi|\psi_2\rangle$
   - 正定性：$\langle\psi|\psi\rangle \geq 0$，等号当且仅当 $|\psi\rangle = 0$
3. **完备性**：柯西序列收敛（数学技术要求，物理上保证极限存在）

### 9.1.3 波函数空间是希尔伯特空间

平方可积的波函数构成希尔伯特空间 $L^2(\mathbb{R}^3)$。内积定义为：

$$\langle\phi|\psi\rangle = \int \phi^*(\vec{r}) \psi(\vec{r}) \, d^3r$$

归一化条件 $\langle\psi|\psi\rangle = 1$ 保证总概率为 1。

两个波函数正交 $\langle\phi|\psi\rangle = 0$ 意味着它们代表互斥的状态。

---

## 9.2 Dirac 符号

### 9.2.1 右矢与左矢

Dirac 引入了一套优雅的符号：

- **右矢**（ket）$|\psi\rangle$：表示希尔伯特空间中的一个矢量（量子态）
- **左矢**（bra）$\langle\psi|$：表示对偶空间中的一个线性泛函

左矢 $\langle\psi|$ 右矢 $|\phi\rangle$ 上，给出内积 $\langle\psi|\phi\rangle$（一个复数）。

### 9.2.2 内积的性质

$$\langle\psi|\phi\rangle = \langle\phi|\psi\rangle^*$$

$$\langle\psi|(a|\phi_1\rangle + b|\phi_2\rangle) = a\langle\psi|\phi_1\rangle + b\langle\psi|\phi_2\rangle$$

$$(a|\psi\rangle)^\dagger = a^* \langle\psi|$$

### 9.2.3 波函数在Dirac符号中的表示

坐标表象中的波函数 $\psi(\vec{r})$ 可以写为：

$$\psi(\vec{r}) = \langle\vec{r}|\psi\rangle$$

其中 $|\vec{r}\rangle$ 是"位置本征态"（严格来说不属于希尔伯特空间，但作为理想化很有用）。

内积 $\langle\phi|\psi\rangle$ 在坐标表象中为：

$$\langle\phi|\psi\rangle = \int \phi^*(\vec{r}) \psi(\vec{r}) \, d^3r = \int \langle\phi|\vec{r}\rangle\langle\vec{r}|\psi\rangle \, d^3r$$

---

## 9.3 算符

### 9.3.1 算符的定义

算符 $\hat{A}$ 是将一个矢量映射到另一个矢量的线性变换：

$$\hat{A}: |\psi\rangle \mapsto |\phi\rangle = \hat{A}|\psi\rangle$$

### 9.3.2 厄米算符

**厄米算符**（自伴算符）满足：

$$\langle\phi|\hat{A}|\psi\rangle = \langle\psi|\hat{A}|\phi\rangle^* \quad \text{或等价地} \quad \hat{A}^\dagger = \hat{A}$$

在坐标表象中，厄米条件为：

$$\int \phi^* (\hat{A}\psi) \, d^3r = \int (\hat{A}\phi)^* \psi \, d^3r$$

**物理意义**：厄米算符的本征值是实数，本征态构成完备正交基。可观测量（位置、动量、能量等）用厄米算符表示。

### 9.3.3 常见算符

**位置算符**：

$$\hat{x} \psi(x) = x \psi(x)$$

**动量算符**：

$$\hat{p}_x \psi(x) = -i\hbar \frac{\partial}{\partial x} \psi(x)$$

**哈密顿算符**：

$$\hat{H} = \frac{\hat{p}^2}{2m} + V(\hat{x}) = -\frac{\hbar^2}{2m}\nabla^2 + V(\vec{r})$$

---

## 9.4 本征值与本征态

### 9.4.1 本征方程

算符 $\hat{A}$ 的本征方程为：

$$\hat{A}|a\rangle = a|a\rangle$$

$a$ 是本征值，$|a\rangle$ 是本征态。

### 9.4.2 厄米算符的性质

**定理1**：厄米算符的本征值是实数。

**证明**：$\langle a|\hat{A}|a\rangle = a\langle a|a\rangle$。由于 $\hat{A}$ 厄米，$\langle a|\hat{A}|a\rangle$ 是实数，$\langle a|a\rangle > 0$，所以 $a$ 是实数。

**定理2**：厄米算符对应不同本征值的本征态正交。

**证明**：$\hat{A}|a_1\rangle = a_1|a_1\rangle$，$\hat{A}|a_2\rangle = a_2|a_2\rangle$。

$$\langle a_2|\hat{A}|a_1\rangle = a_1\langle a_2|a_1\rangle$$

$$\langle a_2|\hat{A}|a_1\rangle = \langle a_1|\hat{A}|a_2\rangle^* = (a_2\langle a_1|a_2\rangle)^* = a_2\langle a_2|a_1\rangle$$

所以 $(a_1 - a_2)\langle a_2|a_1\rangle = 0$。由于 $a_1 \neq a_2$，必须 $\langle a_2|a_1\rangle = 0$。

**定理3**：厄米算符的本征态构成完备正交基。

这意味着任意态可以按本征态展开：

$$|\psi\rangle = \sum_n c_n |a_n\rangle$$

其中 $c_n = \langle a_n|\psi\rangle$。

### 9.4.3 谱分解

厄米算符可以用其本征值和本征投影算符表示：

$$\hat{A} = \sum_n a_n |a_n\rangle\langle a_n| = \sum_n a_n \hat{P}_n$$

其中 $\hat{P}_n = |a_n\rangle\langle a_n|$ 是投影到本征态 $|a_n\rangle$ 的投影算符。

---

## 9.5 测量公设

### 9.5.1 测量的概率

如果系统处于态 $|\psi\rangle$，测量力学量 $A$（对应算符 $\hat{A}$），得到本征值 $a_n$ 的概率为：

$$P(a_n) = |\langle a_n|\psi\rangle|^2 = |c_n|^2$$

### 9.5.2 测量后的状态

测量得到 $a_n$ 后，系统"坍缩"到对应的本征态 $|a_n\rangle$。

这就是**波函数坍缩**（或状态坍缩），是量子力学测量问题的核心。

### 9.5.3 期望值

测量 $A$ 的期望值（大量相同状态测量的平均）为：

$$\langle A \rangle = \sum_n a_n P(a_n) = \sum_n a_n |c_n|^2 = \langle\psi|\hat{A}|\psi\rangle$$

### 9.5.4 不确定度

$$\sigma_A^2 = \langle A^2 \rangle - \langle A \rangle^2 = \langle\psi|(\hat{A} - \langle A\rangle)^2|\psi\rangle$$

---

## 9.6 完备性关系

### 9.6.1 封闭性

本征态构成完备基，满足**封闭性关系**（completeness relation）：

$$\sum_n |a_n\rangle\langle a_n| = \hat{I}$$

其中 $\hat{I}$ 是单位算符。

### 9.6.2 应用

封闭性关系非常有用。例如，任意态可以展开为：

$$|\psi\rangle = \hat{I}|\psi\rangle = \sum_n |a_n\rangle\langle a_n|\psi\rangle = \sum_n c_n |a_n\rangle$$

内积可以计算为：

$$\langle\phi|\psi\rangle = \langle\phi|\hat{I}|\psi\rangle = \sum_n \langle\phi|a_n\rangle\langle a_n|\psi\rangle = \sum_n c_n^* d_n$$

其中 $c_n = \langle a_n|\psi\rangle$，$d_n = \langle a_n|\phi\rangle$。

---

## 9.7 表象变换

### 9.7.1 坐标表象与动量表象

同一个量子态可以在不同的表象中表示：

**坐标表象**：$\psi(x) = \langle x|\psi\rangle$

**动量表象**：$\phi(p) = \langle p|\psi\rangle$

两者通过傅里叶变换联系：

$$\phi(p) = \frac{1}{\sqrt{2\pi\hbar}} \int \psi(x) e^{-ipx/\hbar} dx$$

$$\psi(x) = \frac{1}{\sqrt{2\pi\hbar}} \int \phi(p) e^{ipx/\hbar} dp$$

### 9.7.2 能量表象

在能量本征态 $\{|n\rangle\}$ 构成的基中，态矢量表示为列矢量：

$$|\psi\rangle = \begin{pmatrix} c_1 \\ c_2 \\ c_3 \\ \vdots \end{pmatrix}$$

其中 $c_n = \langle n|\psi\rangle$。

算符表示为矩阵：

$$\hat{A} = \begin{pmatrix} A_{11} & A_{12} & \cdots \\ A_{21} & A_{22} & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}$$

其中 $A_{mn} = \langle m|\hat{A}|n\rangle$。

---

## 本章小结

1. **希尔伯特空间**：量子态所在的抽象空间，具有内积结构。

2. **Dirac符号**：$|\psi\rangle$ 表示右矢（态矢量），$\langle\psi|$ 表示左矢（对偶矢量）。

3. **厄米算符**：本征值为实数，本征态构成完备正交基，代表可观测量。

4. **测量公设**：测量力学量 $A$ 得到 $a_n$ 的概率为 $|\langle a_n|\psi\rangle|^2$，测量后态坍缩到 $|a_n\rangle$。

5. **完备性关系**：$\sum_n |a_n\rangle\langle a_n| = \hat{I}$，是表象变换的基础。

6. **表象变换**：同一态在不同基下有不同的表示，通过幺正变换联系。

---

## 公式索引

| 编号 | 公式 | 含义 | 推导链接 |
|------|------|------|----------|
| [F161](#graph?f=F161) | $\langle\phi|\psi\rangle = \int \phi^*\psi \, d^3r$ | 内积 | [查看推导](#graph?f=F161) |
| [F162](#graph?f=F162) | $|\psi\rangle = \sum_n c_n|a_n\rangle$ | 态展开 | [查看推导](#graph?f=F162) |
| [F163](#graph?f=F163) | $A_{mn} = \langle m|\hat{A}|n\rangle$ | 算符矩阵元 | [查看推导](#graph?f=F163) |
| [F164](#graph?f=F164) | $P(a_n) = |\langle a_n|\psi\rangle|^2$ | 测量概率 | [查看推导](#graph?f=F164) |
| [F165](#graph?f=F165) | $\rho = \sum_i p_i|\psi_i\rangle\langle\psi_i|$ | 密度矩阵 | [查看推导](#graph?f=F165) |

---

## 思考题

1. 为什么希尔伯特空间需要完备性？物理上意味着什么？

2. Dirac符号相比波函数表示有什么优势？

3. 为什么可观测量必须用厄米算符表示？

4. 测量公设中的"坍缩"是如何发生的？这是一个物理过程还是认识论更新？

5. 坐标表象和动量表象之间的傅里叶变换如何从Dirac符号推导出来？

---

**上一章**：[第8章 量子谐振子](lecture-08-harmonic-oscillator.md)

**下一章**：[第10章 表象理论](lecture-10-representation.md)
