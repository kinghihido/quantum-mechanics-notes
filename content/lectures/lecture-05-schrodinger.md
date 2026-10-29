# 第5章 薛定谔方程

> **本章导读**：有了波函数和概率诠释，下一个问题是：波函数如何随时间演化？在经典力学中，牛顿第二定律 $F = ma$ 决定粒子的运动；在量子力学中，薛定谔方程决定波函数的演化。这是量子力学最核心的方程，地位相当于经典力学中的牛顿第二定律。

---

## 5.1 薛定谔方程的建立

### 5.1.1 从经典波到量子力学方程

薛定谔方程不是从某个更基本的原理"推导"出来的，而是薛定谔在1926年"构造"出来的。它的正确性由实验验证。

薛定谔的构造思路如下：

**第一步：从自由粒子的平面波出发**

自由粒子（$V = 0$）的德布罗意波是平面波：

$$\psi(x, t) = A e^{i(kx - \omega t)}$$

其中 $k = 2\pi/\lambda$ 是波数，$\omega = 2\pi\nu$ 是角频率。

由德布罗意关系：

$$p = \hbar k, \quad E = \hbar \omega$$

**第二步：找出平面波满足的微分方程**

对平面波求时间和空间导数：

$$\frac{\partial \psi}{\partial t} = -i\omega \psi = -\frac{iE}{\hbar} \psi$$

$$\frac{\partial^2 \psi}{\partial x^2} = -k^2 \psi = -\frac{p^2}{\hbar^2} \psi$$

由经典能量关系 $E = p^2/(2m)$（自由粒子动能），代入：

$$i\hbar \frac{\partial \psi}{\partial t} = E \psi = \frac{p^2}{2m} \psi = -\frac{\hbar^2}{2m} \frac{\partial^2 \psi}{\partial x^2}$$

所以自由粒子的薛定谔方程为：

$$i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \psi}{\partial x^2}$$

**第三步：加入势能**

如果粒子在势场 $V(x)$ 中运动，总能量为 $E = p^2/(2m) + V$。将 $V$ 作为算符（乘法算符）加入方程：

$$i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \psi}{\partial x^2} + V(x)\psi$$

这就是一维含时薛定谔方程。

### 5.1.2 三维含时薛定谔方程

推广到三维：

$$i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2 \psi + V(\vec{r})\psi$$

其中 $\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$ 是拉普拉斯算符。

引入**哈密顿算符**：

$$\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\vec{r}) = \frac{\hat{p}^2}{2m} + V(\vec{r})$$

薛定谔方程可以简洁地写为：

$$i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi$$

### 5.1.3 薛定谔方程的性质

**线性性**：薛定谔方程是线性的。如果 $\psi_1$ 和 $\psi_2$ 是方程的解，那么它们的线性组合 $c_1\psi_1 + c_2\psi_2$ 也是解。这保证了态叠加原理成立。

**一阶时间导数**：方程对时间是一阶的。这意味着只要给定初始时刻的波函数 $\psi(\vec{r}, 0)$，就可以唯一确定未来任意时刻的波函数。这与经典力学中给定初始位置和速度就可以确定未来运动类似。

**幺正性**：薛定谔方程保证概率守恒。如果初始时刻波函数归一化（$\int |\psi|^2 d^3r = 1$），那么任意时刻都保持归一化。

---

## 5.2 定态薛定谔方程

### 5.2.1 分离变量法

如果势能 $V(\vec{r})$ 不显含时间，可以用分离变量法求解：

设 $\psi(\vec{r}, t) = \phi(\vec{r}) f(t)$，代入薛定谔方程：

$$i\hbar \phi(\vec{r}) f'(t) = f(t) \hat{H}\phi(\vec{r})$$

两边除以 $\phi(\vec{r}) f(t)$：

$$i\hbar \frac{f'(t)}{f(t)} = \frac{\hat{H}\phi(\vec{r})}{\phi(\vec{r})}$$

左边只依赖 $t$，右边只依赖 $\vec{r}$。要使等式对所有 $t$ 和 $\vec{r}$ 成立，两边必须等于同一个常数 $E$：

$$i\hbar \frac{f'(t)}{f(t)} = E \quad \Rightarrow \quad f(t) = e^{-iEt/\hbar}$$

$$\hat{H}\phi(\vec{r}) = E\phi(\vec{r})$$

后者是**定态薛定谔方程**（能量本征方程）：

$$\left[-\frac{\hbar^2}{2m}\nabla^2 + V(\vec{r})\right]\phi(\vec{r}) = E\phi(\vec{r})$$

### 5.2.2 定态的性质

定态 $\psi(\vec{r}, t) = \phi(\vec{r}) e^{-iEt/\hbar}$ 有以下重要性质：

**概率密度不随时间变化**：

$$|\psi(\vec{r}, t)|^2 = |\phi(\vec{r})|^2 |e^{-iEt/\hbar}|^2 = |\phi(\vec{r})|^2$$

时间因子 $e^{-iEt/\hbar}$ 的模为 1，对概率密度没有贡献。

**期望值不随时间变化**：

对于任何不显含时间的算符 $\hat{A}$：

$$\langle A \rangle = \int \psi^* \hat{A} \psi \, d^3r = \int \phi^* \hat{A} \phi \, d^3r$$

与时间无关。

这就是为什么叫"定态"（stationary state）：所有可观测量的概率分布都不随时间变化。

### 5.2.3 能量本征值

定态薛定谔方程是一个本征值问题：

$$\hat{H}\phi = E\phi$$

$E$ 是哈密顿算符 $\hat{H}$ 的本征值，$\phi$ 是对应的本征函数。

物理上，$E$ 是粒子在定态中的总能量。本征值问题决定了能量的可能取值：
- 束缚态：能量取离散值（量子化）
- 散射态：能量取连续值

### 5.2.4 一般解

如果定态薛定谔方程有一组解 $\{\phi_n, E_n\}$，那么含时薛定谔方程的一般解为：

$$\psi(\vec{r}, t) = \sum_n c_n \phi_n(\vec{r}) e^{-iE_n t/\hbar}$$

其中系数 $c_n$ 由初始条件 $\psi(\vec{r}, 0)$ 决定：

$$c_n = \int \phi_n^*(\vec{r}) \psi(\vec{r}, 0) \, d^3r$$

$|c_n|^2$ 表示测量能量时得到 $E_n$ 的概率。

---

## 5.3 概率守恒与连续性方程

### 5.3.1 概率密度的时间演化

定义概率密度 $\rho = |\psi|^2 = \psi^* \psi$。

对时间求导：

$$\frac{\partial \rho}{\partial t} = \frac{\partial \psi^*}{\partial t} \psi + \psi^* \frac{\partial \psi}{\partial t}$$

由薛定谔方程及其复共轭：

$$\frac{\partial \psi}{\partial t} = \frac{1}{i\hbar}\left(-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi\right)$$

$$\frac{\partial \psi^*}{\partial t} = -\frac{1}{i\hbar}\left(-\frac{\hbar^2}{2m}\nabla^2\psi^* + V\psi^*\right)$$

代入得：

$$\frac{\partial \rho}{\partial t} = \frac{1}{i\hbar}\left[-\frac{\hbar^2}{2m}(\nabla^2\psi^*)\psi + \frac{\hbar^2}{2m}\psi^*(\nabla^2\psi)\right]$$

$$= -\frac{\hbar}{2mi}\nabla \cdot (\psi^* \nabla\psi - \psi\nabla\psi^*)$$

### 5.3.2 概率流密度

定义**概率流密度**：

$$\vec{j} = \frac{\hbar}{2mi}(\psi^* \nabla\psi - \psi\nabla\psi^*) = \text{Re}\left(\psi^* \frac{\hat{p}}{m} \psi\right)$$

则概率密度的时间演化满足**连续性方程**：

$$\frac{\partial \rho}{\partial t} + \nabla \cdot \vec{j} = 0$$

这与流体力学中的连续性方程形式完全相同，表示概率的"流动"是守恒的。

### 5.3.3 概率守恒

对全空间积分：

$$\frac{d}{dt}\int \rho \, d^3r = -\int \nabla \cdot \vec{j} \, d^3r = -\oint \vec{j} \cdot d\vec{S}$$

如果波函数在无穷远处趋于零（束缚态），则面积分为零：

$$\frac{d}{dt}\int |\psi|^2 \, d^3r = 0$$

总概率不随时间变化。如果初始时刻归一化，则永远归一化。

### 5.3.4 物理意义

连续性方程的物理意义是：

- $\rho = |\psi|^2$ 是概率密度（单位体积内的概率）
- $\vec{j}$ 是概率流密度（单位时间通过单位面积的概率）
- $\partial\rho/\partial t + \nabla\cdot\vec{j} = 0$ 表示概率的局部守恒：某处概率的增加等于从周围流入的概率

这与电荷守恒（$\partial\rho_e/\partial t + \nabla\cdot\vec{J} = 0$）完全类似。

---

## 5.4 薛定谔方程的启发式构造

### 5.4.1 为什么说薛定谔方程是"构造"的？

严格来说，薛定谔方程不是从更基本的原理"推导"出来的。它的建立过程是：

1. 从德布罗意关系和经典能量关系出发
2. 通过类比和启发式论证，猜出方程的形式
3. 用实验验证方程的正确性

这与牛顿第二定律 $F = ma$ 的建立类似：牛顿不是从更基本的原理推导出 $F = ma$，而是通过观察和归纳，提出这个假设，然后用实验验证。

### 5.4.2 构造过程中的"公设化"

薛定谔方程的构造中有两处关键的"公设化"（无法从更基本的原理推导，只能由实验验证）：

**公设一：线性叠加**

薛定谔方程是线性的，这意味着态叠加原理成立。为什么自然界必须是线性的？这是一个基本假设，无法从更深的原理推导。

**公设二：时间一阶**

薛定谔方程对时间是一阶导数。为什么不是二阶（如经典波动方程）？因为一阶时间导数保证了概率守恒（幺正演化）。如果方程对时间是二阶的，概率可能不守恒。

### 5.4.3 从行波到薛定谔方程

另一种理解薛定谔方程的方式是从行波假设出发：

1. **假设**：自由粒子的波函数是行波 $\psi = Ae^{i(kx-\omega t)}$
2. **德布罗意关系**：$p = \hbar k$, $E = \hbar\omega$
3. **经典能量关系**：$E = p^2/(2m)$（自由粒子）
4. **算符替换**：$E \to i\hbar\partial/\partial t$, $p \to -i\hbar\partial/\partial x$
5. **得到方程**：$i\hbar\partial\psi/\partial t = -(\hbar^2/2m)\partial^2\psi/\partial x^2$
6. **加入势能**：$E = p^2/(2m) + V \to i\hbar\partial\psi/\partial t = [-(\hbar^2/2m)\nabla^2 + V]\psi$

这个过程不是严格的"推导"，而是启发式的"构造"。每一步都有物理动机，但最终的正确性由实验决定。

---

## 5.5 薛定谔方程的应用范围

### 5.5.1 非相对论量子力学

薛定谔方程是非相对论的。它基于经典能量关系 $E = p^2/(2m) + V$，这在 $v \ll c$ 时成立。

当粒子速度接近光速时，需要用相对论性能量-动量关系：

$$E^2 = (pc)^2 + (m_0 c^2)^2$$

对应的波动方程是**克莱因-戈登方程**（自旋为 0 的粒子）或**狄拉克方程**（自旋为 1/2 的粒子）。

### 5.5.2 单粒子问题

薛定谔方程描述的是单粒子问题。对于多粒子体系，波函数定义在 $3N$ 维空间（$N$ 是粒子数），方程变为：

$$i\hbar\frac{\partial\psi}{\partial t} = \left[-\sum_{i=1}^N \frac{\hbar^2}{2m_i}\nabla_i^2 + V(\vec{r}_1, \ldots, \vec{r}_N)\right]\psi$$

多粒子薛定谔方程的求解极其困难，是量子多体物理的核心问题。

### 5.5.3 量子力学的基本方程

尽管有这些限制，薛定谔方程仍然是量子力学最基本的方程。它在原子物理、分子物理、凝聚态物理、量子化学等领域有广泛应用。

---

## 本章小结

1. **含时薛定谔方程**：$i\hbar\partial\psi/\partial t = \hat{H}\psi$，决定波函数的时间演化。

2. **定态薛定谔方程**：$\hat{H}\phi = E\phi$，能量本征值问题。

3. **定态性质**：概率密度和期望值不随时间变化。

4. **概率守恒**：$\partial\rho/\partial t + \nabla\cdot\vec{j} = 0$，连续性方程。

5. **启发式构造**：从行波假设和德布罗意关系出发，通过类比得到方程。

6. **适用范围**：非相对论、单粒子（或多粒子）问题。

---

## 公式索引

| 编号 | 公式 | 含义 | 推导链接 |
|------|------|------|----------|
| [F121](#graph?f=F121) | $i\hbar\partial\psi/\partial t = \hat{H}\psi$ | 含时薛定谔方程 | [查看推导](#graph?f=F121) |
| [F122](#graph?f=F122) | $\hat{H} = \hat{p}^2/(2m) + V$ | 哈密顿算符 | [查看推导](#graph?f=F122) |
| [F123](#graph?f=F123) | $\vec{j} = \frac{\hbar}{2mi}(\psi^*\nabla\psi - \psi\nabla\psi^*)$ | 概率流密度 | [查看推导](#graph?f=F123) |
| [F124](#graph?f=F124) | $\partial\rho/\partial t + \nabla\cdot\vec{j} = 0$ | 连续性方程 | [查看推导](#graph?f=F124) |
| [F125](#graph?f=F125) | $\psi(\vec{r},t) = \phi(\vec{r})e^{-iEt/\hbar}$ | 分离变量 | [查看推导](#graph?f=F125) |
| [F126](#graph?f=F126) | $\hat{H}\phi = E\phi$ | 定态薛定谔方程 | [查看推导](#graph?f=F126) |

---

## 思考题

1. 为什么薛定谔方程对时间是一阶导数？如果是二阶导数，会有什么问题？

2. 定态的物理意义是什么？为什么概率密度不随时间变化？

3. 概率流密度 $\vec{j}$ 的物理意义是什么？它与电流密度有什么关系？

4. 如何从薛定谔方程推导出不确定关系？

5. 薛定谔方程是"推导"出来的还是"构造"出来的？这与牛顿第二定律的建立有什么相似之处？

---


