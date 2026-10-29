# 第14章 角动量代数

> **本章导读**：角动量是量子力学中最重要的力学量之一。与经典力学不同，量子角动量是量子化的，且三个分量不能同时确定。角动量代数完全由对易关系 $[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k$ 决定，由此可以推导出角动量的本征值谱、升降算符、矩阵表示等。这套代数方法不仅适用于轨道角动量，也适用于自旋角动量。

---

## 14.1 轨道角动量

### 14.1.1 定义

经典角动量 $\vec{L} = \vec{r} \times \vec{p}$。量子化后：

$$\hat{\vec{L}} = \hat{\vec{r}} \times \hat{\vec{p}}$$

分量形式：

$$\hat{L}_x = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y$$

$$\hat{L}_y = \hat{z}\hat{p}_x - \hat{x}\hat{p}_z$$

$$\hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x$$

### 14.1.2 角动量对易关系

**定理**：角动量分量满足对易关系

$$[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$$

$$[\hat{L}_y, \hat{L}_z] = i\hbar\hat{L}_x$$

$$[\hat{L}_z, \hat{L}_x] = i\hbar\hat{L}_y$$

或紧凑地：

$$[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k$$

其中 $\epsilon_{ijk}$ 是列维-奇维塔符号。

**证明**（以 $[\hat{L}_x, \hat{L}_y]$ 为例）：

$$[\hat{L}_x, \hat{L}_y] = [\hat{y}\hat{p}_z - \hat{z}\hat{p}_y, \hat{z}\hat{p}_x - \hat{x}\hat{p}_z]$$

展开（利用 $[\hat{A}, \hat{B}\hat{C}] = [\hat{A}, \hat{B}]\hat{C} + \hat{B}[\hat{A}, \hat{C}]$）：

$$= [\hat{y}\hat{p}_z, \hat{z}\hat{p}_x] - [\hat{y}\hat{p}_z, \hat{x}\hat{p}_z] - [\hat{z}\hat{p}_y, \hat{z}\hat{p}_x] + [\hat{z}\hat{p}_y, \hat{x}\hat{p}_z]$$

利用 $[\hat{y}, \hat{p}_y] = i\hbar$，其他对易子为零：

$$= \hat{y}[\hat{p}_z, \hat{z}]\hat{p}_x + \hat{z}[\hat{z}, \hat{p}_z]\hat{p}_y$$

$$= \hat{y}(-i\hbar)\hat{p}_x + \hat{z}(i\hbar)\hat{p}_y$$

$$= i\hbar(\hat{z}\hat{p}_y - \hat{y}\hat{p}_x) = i\hbar\hat{L}_z$$

$\blacksquare$

### 14.1.3 角动量平方

定义角动量平方：

$$\hat{L}^2 = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2$$

**重要性质**：$\hat{L}^2$ 与每个分量对易：

$$[\hat{L}^2, \hat{L}_i] = 0 \quad (i = x, y, z)$$

**证明**（以 $[\hat{L}^2, \hat{L}_z]$ 为例）：

$$[\hat{L}^2, \hat{L}_z] = [\hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2, \hat{L}_z]$$

$$= [\hat{L}_x^2, \hat{L}_z] + [\hat{L}_y^2, \hat{L}_z]$$

$$= \hat{L}_x[\hat{L}_x, \hat{L}_z] + [\hat{L}_x, \hat{L}_z]\hat{L}_x + \hat{L}_y[\hat{L}_y, \hat{L}_z] + [\hat{L}_y, \hat{L}_z]\hat{L}_y$$

$$= \hat{L}_x(-i\hbar\hat{L}_y) + (-i\hbar\hat{L}_y)\hat{L}_x + \hat{L}_y(i\hbar\hat{L}_x) + (i\hbar\hat{L}_x)\hat{L}_y$$

$$= -i\hbar(\hat{L}_x\hat{L}_y + \hat{L}_y\hat{L}_x) + i\hbar(\hat{L}_y\hat{L}_x + \hat{L}_x\hat{L}_y) = 0$$

$\blacksquare$

---

## 14.2 角动量的本征值问题

### 14.2.1 共同本征态

由于 $[\hat{L}^2, \hat{L}_z] = 0$，$\hat{L}^2$ 和 $\hat{L}_z$ 有共同本征态。设：

$$\hat{L}^2|l, m\rangle = \lambda\hbar^2|l, m\rangle$$

$$\hat{L}_z|l, m\rangle = m\hbar|l, m\rangle$$

其中 $\lambda$ 和 $m$ 是无量纲的量子数。

### 14.2.2 升降算符

定义**升降算符**（ladder operators）：

$$\hat{L}_+ = \hat{L}_x + i\hat{L}_y$$

$$\hat{L}_- = \hat{L}_x - i\hat{L}_y$$

**对易关系**：

$$[\hat{L}_z, \hat{L}_\pm] = \pm\hbar\hat{L}_\pm$$

$$[\hat{L}_+, \hat{L}_-] = 2\hbar\hat{L}_z$$

### 14.2.3 升降算符的作用

**定理**：$\hat{L}_\pm|l, m\rangle$ 是 $\hat{L}^2$ 和 $\hat{L}_z$ 的共同本征态，本征值分别为 $\lambda\hbar^2$ 和 $(m \pm 1)\hbar$。

**证明**：

$$\hat{L}_z(\hat{L}_\pm|l, m\rangle) = (\hat{L}_\pm\hat{L}_z \pm \hbar\hat{L}_\pm)|l, m\rangle = (m\hbar \pm \hbar)(\hat{L}_\pm|l, m\rangle)$$

$$\hat{L}^2(\hat{L}_\pm|l, m\rangle) = \hat{L}_\pm(\hat{L}^2|l, m\rangle) = \lambda\hbar^2(\hat{L}_\pm|l, m\rangle)$$

$\blacksquare$

所以 $\hat{L}_+$ 将 $m$ 增加 1，$\hat{L}_-$ 将 $m$ 减少 1。

### 14.2.4 量子数的取值范围

由于 $\hat{L}^2 - \hat{L}_z^2 = \hat{L}_x^2 + \hat{L}_y^2$ 是半正定的：

$$\langle l, m|\hat{L}^2 - \hat{L}_z^2|l, m\rangle \geq 0$$

$$\lambda\hbar^2 - m^2\hbar^2 \geq 0 \Rightarrow \lambda \geq m^2$$

所以 $m$ 有上下界。设 $m_{\max} = l$，$m_{\min} = -l$。

由 $\hat{L}_+|l, l\rangle = 0$ 和 $\hat{L}_-|l, -l\rangle = 0$，可以推导出：

$$\lambda = l(l+1)$$

其中 $l = 0, 1/2, 1, 3/2, 2, \ldots$（非负整数或半整数）。

对于给定的 $l$，$m = -l, -l+1, \ldots, l-1, l$（共 $2l+1$ 个值）。

### 14.2.5 角动量本征值

**角动量平方**：

$$\hat{L}^2|l, m\rangle = l(l+1)\hbar^2|l, m\rangle$$

**角动量z分量**：

$$\hat{L}_z|l, m\rangle = m\hbar|l, m\rangle$$

其中 $l = 0, 1/2, 1, 3/2, 2, \ldots$，$m = -l, -l+1, \ldots, l$。

### 14.2.6 升降算符的矩阵元

$$\hat{L}_\pm|l, m\rangle = \hbar\sqrt{l(l+1) - m(m \pm 1)}|l, m \pm 1\rangle$$

$$= \hbar\sqrt{(l \mp m)(l \pm m + 1)}|l, m \pm 1\rangle$$

---

## 14.3 轨道角动量的球坐标表示

### 14.3.1 球坐标中的角动量算符

在球坐标 $(r, \theta, \phi)$ 中：

$$\hat{L}_z = -i\hbar\frac{\partial}{\partial\phi}$$

$$\hat{L}^2 = -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right]$$

### 14.3.2 球谐函数

$\hat{L}^2$ 和 $\hat{L}_z$ 的共同本征函数是**球谐函数** $Y_l^m(\theta, \phi)$：

$$\hat{L}^2 Y_l^m = l(l+1)\hbar^2 Y_l^m$$

$$\hat{L}_z Y_l^m = m\hbar Y_l^m$$

球谐函数的形式：

$$Y_l^m(\theta, \phi) = N_{lm} P_l^{|m|}(\cos\theta) e^{im\phi}$$

其中 $P_l^m$ 是连带勒让德多项式，$N_{lm}$ 是归一化常数。

### 14.3.3 球谐函数的性质

**正交归一性**：

$$\int_0^{2\pi}\int_0^\pi Y_{l'}^{m'*}(\theta, \phi) Y_l^m(\theta, \phi) \sin\theta \, d\theta \, d\phi = \delta_{ll'}\delta_{mm'}$$

**完备性**：

$$\sum_{l=0}^\infty \sum_{m=-l}^l Y_l^{m*}(\theta', \phi') Y_l^m(\theta, \phi) = \delta(\cos\theta - \cos\theta')\delta(\phi - \phi')$$

### 14.3.4 前几个球谐函数

$$Y_0^0 = \frac{1}{\sqrt{4\pi}}$$

$$Y_1^0 = \sqrt{\frac{3}{4\pi}}\cos\theta$$

$$Y_1^{\pm 1} = \mp\sqrt{\frac{3}{8\pi}}\sin\theta e^{\pm i\phi}$$

$$Y_2^0 = \sqrt{\frac{5}{16\pi}}(3\cos^2\theta - 1)$$

---

## 14.4 角动量的矩阵表示

### 14.4.1 $l = 1/2$（自旋1/2）

$l = 1/2$ 时，$m = \pm 1/2$，态空间是二维的。

$$\hat{L}_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \frac{\hbar}{2}\sigma_z$$

$$\hat{L}_x = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \frac{\hbar}{2}\sigma_x$$

$$\hat{L}_y = \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \frac{\hbar}{2}\sigma_y$$

其中 $\sigma_x, \sigma_y, \sigma_z$ 是**泡利矩阵**。

### 14.4.2 $l = 1$

$l = 1$ 时，$m = -1, 0, 1$，态空间是三维的。

$$\hat{L}_z = \hbar\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix}$$

$$\hat{L}_x = \frac{\hbar}{\sqrt{2}}\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$$

$$\hat{L}_y = \frac{\hbar}{\sqrt{2}}\begin{pmatrix} 0 & -i & 0 \\ i & 0 & -i \\ 0 & i & 0 \end{pmatrix}$$

### 14.4.3 一般 $l$ 的矩阵元

在 $|l, m\rangle$ 基中：

$$\langle l, m'|\hat{L}_z|l, m\rangle = m\hbar\delta_{m'm}$$

$$\langle l, m'|\hat{L}_\pm|l, m\rangle = \hbar\sqrt{(l \mp m)(l \pm m + 1)}\delta_{m', m \pm 1}$$

$$\hat{L}_x = \frac{1}{2}(\hat{L}_+ + \hat{L}_-), \quad \hat{L}_y = \frac{1}{2i}(\hat{L}_+ - \hat{L}_-)$$

---

## 14.5 角动量的耦合

### 14.5.1 两个角动量的耦合

考虑两个角动量 $\hat{\vec{J}}_1$ 和 $\hat{\vec{J}}_2$（可以是轨道角动量或自旋），总角动量为：

$$\hat{\vec{J}} = \hat{\vec{J}}_1 + \hat{\vec{J}}_2$$

### 14.5.2 非耦合基与耦合基

**非耦合基**：$|j_1, m_1\rangle \otimes |j_2, m_2\rangle = |j_1, m_1; j_2, m_2\rangle$

**耦合基**：$|j, m\rangle$，其中 $\hat{J}^2|j, m\rangle = j(j+1)\hbar^2|j, m\rangle$，$\hat{J}_z|j, m\rangle = m\hbar|j, m\rangle$

### 14.5.3 克莱布希-高登系数

两种基通过**克莱布希-高登系数**（Clebsch-Gordan coefficients）联系：

$$|j, m\rangle = \sum_{m_1, m_2} \langle j_1, m_1; j_2, m_2|j, m\rangle |j_1, m_1; j_2, m_2\rangle$$

其中 $m = m_1 + m_2$，$j$ 的取值范围为 $|j_1 - j_2| \leq j \leq j_1 + j_2$。

### 14.5.4 例子：两个自旋1/2的耦合

$j_1 = j_2 = 1/2$，则 $j = 0$ 或 $j = 1$。

**三重态**（$j = 1$）：

$$|1, 1\rangle = |\uparrow\uparrow\rangle$$

$$|1, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)$$

$$|1, -1\rangle = |\downarrow\downarrow\rangle$$

**单态**（$j = 0$）：

$$|0, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$$

---

## 本章小结

1. **角动量对易关系**：$[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k$，$[\hat{L}^2, \hat{L}_i] = 0$。

2. **本征值**：$\hat{L}^2$ 的本征值为 $l(l+1)\hbar^2$，$\hat{L}_z$ 的本征值为 $m\hbar$。

3. **量子数**：$l = 0, 1/2, 1, 3/2, \ldots$，$m = -l, -l+1, \ldots, l$。

4. **升降算符**：$\hat{L}_\pm|l, m\rangle = \hbar\sqrt{(l \mp m)(l \pm m + 1)}|l, m \pm 1\rangle$。

5. **球谐函数**：$\hat{L}^2$ 和 $\hat{L}_z$ 的共同本征函数，构成球面上的完备正交基。

6. **角动量耦合**：两个角动量耦合，总角动量量子数 $j$ 的范围为 $|j_1 - j_2| \leq j \leq j_1 + j_2$。

---

## 公式索引

| 编号 | 公式 | 含义 | 推导链接 |
|------|------|------|----------|
| [F181](#graph?f=F181) | $[\hat{L}_i, \hat{L}_j] = i\hbar\epsilon_{ijk}\hat{L}_k$ | 角动量对易关系 | [查看推导](#graph?f=F181) |
| [F182](#graph?f=F182) | $\hat{L}^2|l,m\rangle = l(l+1)\hbar^2|l,m\rangle$ | 角动量平方本征值 | [查看推导](#graph?f=F182) |
| [F183](#graph?f=F183) | $\hat{L}_z|l,m\rangle = m\hbar|l,m\rangle$ | 角动量z分量本征值 | [查看推导](#graph?f=F183) |

---

## 思考题

1. 验证角动量对易关系 $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$。

2. 为什么 $l$ 可以是半整数？轨道角动量的 $l$ 为什么只能是整数？

3. 升降算符 $\hat{L}_+$ 和 $\hat{L}_-$ 的物理意义是什么？

4. 球谐函数 $Y_l^m(\theta, \phi)$ 的节点结构如何？

5. 两个自旋1/2粒子耦合，三重态和单态的对称性如何？

---


