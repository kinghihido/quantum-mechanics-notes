# 第10章 表象理论

> **本章导读**：同一个量子态可以用不同的方式表示，就像同一个矢量可以用不同的坐标系描述一样。在量子力学中，这些不同的表示方式叫做**表象**（representation）。最常用的表象有坐标表象（波函数）、动量表象、能量表象等。不同表象之间的变换是幺正变换，保持内积不变。表象理论揭示了量子力学的深层数学结构，也是实际计算的重要工具。

---

## 10.1 表象的基本概念

### 10.1.1 什么是表象

在Dirac符号中，量子态用右矢 $|\psi\rangle$ 表示，这是一个抽象的矢量。要具体计算，需要选择一组基矢 $\{|n\rangle\}$，将 $|\psi\rangle$ 展开：

$$|\psi\rangle = \sum_n c_n |n\rangle$$

其中 $c_n = \langle n|\psi\rangle$ 是展开系数。

**表象**就是选择哪组基矢来展开态矢量。不同的选择对应不同的表象：

- **坐标表象**（位置表象）：基矢是位置本征态 $\{|x\rangle\}$，展开系数 $c(x) = \langle x|\psi\rangle = \psi(x)$ 就是波函数
- **动量表象**：基矢是动量本征态 $\{|p\rangle\}$，展开系数 $c(p) = \langle p|\psi\rangle = \phi(p)$
- **能量表象**：基矢是哈密顿量的本征态 $\{|n\rangle\}$，展开系数 $c_n = \langle n|\psi\rangle$

### 10.1.2 表象的物理意义

选择表象就像选择坐标系：物理内容不变，但数学形式不同。

- 坐标表象：波函数 $\psi(x)$ 是位置的函数，位置算符是乘法，动量算符是微分
- 动量表象：波函数 $\phi(p)$ 是动量的函数，动量算符是乘法，位置算符是微分
- 能量表象：波函数是列矢量 $(c_1, c_2, \ldots)^T$，算符是矩阵

哪个表象更方便，取决于具体问题。

---

## 10.2 坐标表象

### 10.2.1 位置本征态

位置算符 $\hat{x}$ 的本征方程为：

$$\hat{x}|x\rangle = x|x\rangle$$

位置本征态 $|x\rangle$ 满足正交归一性：

$$\langle x'|x\rangle = \delta(x' - x)$$

和完备性关系：

$$\int_{-\infty}^\infty |x\rangle\langle x| \, dx = \hat{I}$$

### 10.2.2 波函数

态矢量 $|\psi\rangle$ 在坐标表象中的表示是波函数：

$$\psi(x) = \langle x|\psi\rangle$$

内积为：

$$\langle\phi|\psi\rangle = \int_{-\infty}^\infty \phi^*(x)\psi(x) \, dx$$

归一化条件：

$$\int_{-\infty}^\infty |\psi(x)|^2 \, dx = 1$$

### 10.2.3 算符在坐标表象中的表示

**位置算符**：

$$\langle x|\hat{x}|\psi\rangle = x\psi(x)$$

位置算符就是乘以 $x$。

**动量算符**：

$$\langle x|\hat{p}|\psi\rangle = -i\hbar\frac{\partial}{\partial x} \psi(x)$$

动量算符是 $-i\hbar\partial/\partial x$。

**哈密顿算符**：

$$\langle = \left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)\right]\psi(x)$$

薛定谔方程在坐标表象中为：

$$i\hbar\frac{\partial\psi}{\partial t} = \left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)\right]\psi$$

---

## 10.3 动量表象

### 10.3.1 动量本征态

动量算符 $\hat{p}$ 的本征方程为：

$$\hat{p}|p\rangle = p|p\rangle$$

在坐标表象中，动量本征函数是平面波：

$$\langle x|p\rangle = \frac{1}{\sqrt{2\pi\hbar}} e^{ipx/\hbar}$$

动量本征态满足正交归一性：

$$\langle p'|p\rangle = \delta(p' - p)$$

和完备性关系：

$$\int_{-\infty}^\infty |p\rangle\langle p| \, dp = \hat{I}$$

### 10.3.2 动量空间波函数

态矢量 $|\psi\rangle$ 在动量表象中的表示是动量空间波函数：

$$\phi(p) = \langle p|\psi\rangle$$

与坐标表象波函数的关系（傅里叶变换）：

$$\phi(p) = \int_{-\infty}^\infty \langle p|x\rangle\langle x|\psi\rangle \, dx = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^\infty e^{-ipx/\hbar} \psi(x) \, dx$$

$$\psi(x) = \int_{-\infty}^\infty \langle x|p\rangle\langle p|\psi\rangle \, dp = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^\infty e^{ipx/\hbar} \phi(p) \, dp$$

### 10.3.3 算符在动量表象中的表示

**动量算符**：

$$\langle p|\hat{p}|\psi\rangle = p\phi(p)$$

动量算符就是乘以 $p$。

**位置算符**：

$$\langle x|\hat{x}|\psi\rangle = i\hbar\frac{\partial}{\partial p}\phi(p)$$

位置算符是 $i\hbar\partial/\partial p$。

注意：在动量表象中，位置和动量的角色互换了。

---

## 10.4 离散谱表象

### 10.4.1 能量表象

对于束缚态问题，哈密顿量 $\hat{H}$ 有离散的本征值谱：

$$\hat{H}|n\rangle = E_n|n\rangle$$

能量本征态 $\|n\rangle$ 构成离散的正交归一完备基：

$$\langle m|n\rangle = \delta_{mn}$$

$$\sum_n |n\rangle\langle n| = \hat{I}$$

### 10.4.2 态矢量的矩阵表示

态矢量 $|\psi\rangle$ 在能量表象中表示为列矢量：

$$|\psi\rangle = \sum_n c_n |n\rangle \quad \leftrightarrow \quad \begin{pmatrix} c_1 \\ c_2 \\ c_3 \\ \vdots \end{pmatrix}$$

其中 $c_n = \langle n|\psi\rangle$。

归一化条件：

$$\sum_n |c_n|^2 = 1$$

### 10.4.3 算符的矩阵表示

算符 $\hat{A}$ 在能量表象中表示为矩阵：

$$A_{mn} = \langle m|\hat{A}|n\rangle$$

矩阵元 $A_{mn}$ 构成矩阵：

$$\hat{A} \quad \leftrightarrow \quad \begin{pmatrix} A_{11} & A_{12} & A_{13} & \cdots \\ A_{21} & A_{22} & A_{23} & \cdots \\ A_{31} & A_{32} & A_{33} & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

### 10.4.4 本征值问题的矩阵形式

算符 $\hat{A}$ 的本征方程 $\hat{A}|a\rangle = a|a\rangle$ 在能量表象中为矩阵方程：

$$\sum_n A_{mn} c_n = a c_m$$

或写成矩阵形式：

$$\mathbf{A}\mathbf{c} = a\mathbf{c}$$

这是标准的矩阵本征值问题。本征值 $a$ 由久期方程决定：

$$\det(\mathbf{A} - a\mathbf{I}) = 0$$

---

## 10.5 表象变换

### 10.5.1 幺正变换

从一个表象 $\{|n\rangle\}$ 变换到另一个表象 $\{|m'\rangle\}$，通过幺正变换实现：

$$|m'\rangle = \sum_n U_{mn} |n\rangle$$

其中幺正矩阵 $U$ 满足：

$$U^\dagger U = U U^\dagger = I$$

即 $U^{-1} = U^\dagger$。

### 10.5.2 态矢量的变换

态矢量在两个表象中的分量关系：

$$c'_m = \langle m'|\psi\rangle = \sum_n \langle m'|n\rangle\langle n|\psi\rangle = \sum_n U_{mn}^* c_n$$

即 $\mathbf{c}' = U^\dagger \mathbf{c}$。

### 10.5.3 算符的变换

算符在两个表象中的矩阵元关系：

$$A'_{mn} = \langle m'|\hat{A}|n'\rangle = \sum_{j,k} U_{mj}^* A_{jk} U_{kn}$$

即 $\mathbf{A}' = U^\dagger \mathbf{A} U$。

### 10.5.4 内积不变性

幺正变换保持内积不变：

$$\langle\phi'|\psi'\rangle = \langle\phi|U^\dagger U|\psi\rangle = \langle\phi|\psi\rangle$$

这意味着概率、期望值等物理量不依赖于表象的选择。

---

## 10.6 线性谐振子的矩阵力学

### 10.6.1 能量表象中的矩阵元

线性谐振子的能量本征态为 $|n\rangle$，能量 $E_n = (n + 1/2)\hbar\omega$。

位置算符和动量算符的矩阵元为：

$$\langle m|\hat{x}|n\rangle = \sqrt{\frac{\hbar}{2m\omega}} \left(\sqrt{n}\delta_{m,n-1} + \sqrt{n+1}\delta_{m,n+1}\right)$$

$$\langle m|\hat{p}|n\rangle = i\sqrt{\frac{m\hbar\omega}{2}} \left(\sqrt{n}\delta_{m,n-1} - \sqrt{n+1}\delta_{m,n+1}\right)$$

### 10.6.2 矩阵形式

位置和动量算符在能量表象中是三三对角矩阵：

$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}} \begin{pmatrix} 0 & 1 & 0 & 0 & \cdots \\ 1 & 0 & \sqrt{2} & 0 & \cdots \\ 0 & \sqrt{2} & 0 & \sqrt{3} & \cdots \\ 0 & 0 & \sqrt{3} & 0 & \cdots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

$$\hat{p} = i\sqrt{\frac{m\hbar\omega}{2}} \begin{pmatrix} 0 & 1 & 0 & 0 & \cdots \\ -1 & 0 & \sqrt{2} & 0 & \cdots \\ 0 & -\sqrt{2} & 0 & \sqrt{3} & \cdots \\ 0 & 0 & -\sqrt{3} & 0 & \cdots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

### 10.6.3 对易关系

验证 $[\hat{x}, \hat{p}] = i\hbar$：

$$[\hat{x}, \hat{p}]_{mn} = \sum_k (x_{mk}p_{kn} - p_{mk}x_{kn}) = i\hbar\delta_{mn}$$

这正是正则对易关系。

---

## 10.7 表象理论的应用

### 10.7.1 选择表象的原则

1. **问题对称性**：选择与问题对称性匹配的表象
   - 位置相关问题（如势阱）→ 坐标表象
   - 动量相关问题（如散射）→ 动量表象
   - 能量相关问题（如光谱）→ 能量表象

2. **计算简便性**：选择使算符形式简单的表象
   - 坐标表象中 $\hat{x}$ 是乘法，$\hat{p}$ 是微分
   - 动量表象中 $\hat{p}$ 是乘法，$\hat{x}$ 是微分
   - 能量表象中 $\hat{H}$ 是对角矩阵

### 10.7.2 多表象方法

复杂问题可能需要同时使用多个表象：

1. 在坐标表象中建立薛定谔方程
2. 求解得到能量本征态
3. 变换到能量表象中处理时间演化
4. 计算观测量的期望值

### 10.7.3 数值计算

在数值计算中，通常将连续表象离散化：

1. 坐标空间网格化：$x_i = i\Delta x$
2. 波函数表示为列矢量：$\psi_i = \psi(x_i)$
3. 算符表示为矩阵
4. 薛定谔方程化为矩阵本征值问题

---

## 本章小结

1. **表象**：选择一组基矢展开态矢量，不同表象对应不同的数学表示。

2. **坐标表象**：波函数 $\psi(x) = \langle x|\psi\rangle$，位置算符是乘法，动量算符是微分。

3. **动量表象**：波函数 $\phi(p) = \langle p|\psi\rangle$，动量算符是乘法，位置算符是微分。

4. **能量表象**：态矢量是列矢量 $(c_1, c_2, \ldots)^T$，算符是矩阵。

5. **表象变换**：幺正变换，保持内积和物理量不变。

6. **应用**：根据问题对称性和计算简便性选择表象。

---

## 公式索引

| 编号 | 公式 | 含义 | 推导链接 |
|------|------|------|----------|
| [F166](#graph?f=F166) | $\psi(x) = \langle x|\psi\rangle$ | 坐标表象 | [查看推导](#graph?f=F166) |
| [F167](#graph?f=F167) | $\phi(p) = \langle p|\psi\rangle$ | 动量表象 | [查看推导](#graph?f=F167) |
| [F168](#graph?f=F168) | $\mathbf{A}' = U^\dagger \mathbf{A} U$ | 表象变换 | [查看推导](#graph?f=F168) |

---

## 思考题

1. 为什么坐标表象和动量表象通过傅里叶变换联系？

2. 在能量表象中，哈密顿量的矩阵是什么形式？

3. 幺正变换为什么保持物理量不变？

4. 如何选择合适表象来求解具体问题？

5. 数值计算中，如何离散化连续表象？

---

**上一章**：[第9章](https://kinghihido.github.io/quantum-mechanics-notes/content/lectures/lecture-09-dirac-notation.md)

**下一章**：[第11章](https://kinghihido.github.io/quantum-mechanics-notes/content/lectures/lecture-11-hermitian.md)
