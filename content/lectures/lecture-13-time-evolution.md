# 第13章 时间演化与守恒量

> **本章导读**：量子态如何随时间演化？薛定谔方程给出了答案：$i\hbar\partial|\psi\rangle/\partial t = \hat{H}|\psi\rangle$。如果哈密顿量不显含时间，时间演化由幺正算符 $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ 描述。与哈密顿量对易的力学量是守恒量，其期望值不随时间变化。本章系统讨论时间演化的数学结构和守恒量的物理意义。

---

## 13.1 时间演化算符

### 13.1.1 薛定谔方程的算符形式

含时薛定谔方程：

$$i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle$$

如果 $\hat{H}$ 不显含时间，方程的解为：

$$|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$$

其中**时间演化算符**为：

$$\hat{U}(t) = e^{-i\hat{H}t/\hbar}$$

### 13.1.2 时间演化算符的性质

**正性**：

$$\hat{U}^\dagger(t) = e^{i\hat{H}t/\hbar} = \hat{U}^{-1}(t)$$

$$\hat{U}^\dagger(t)\hat{U}(t) = \hat{I}$$

幺正性保证概率守恒：$\langle\psi(t)|\psi(t)\rangle = \langle\psi(0)|\hat{U}^\dagger\hat{U}|\psi(0)\rangle = \langle\psi(0)|\psi(0)\rangle$。

**群性质**：

$$\hat{U}(t_1)\hat{U}(t_2) = \hat{U}(t_1 + t_2)$$

$$\hat{U}(0) = \hat{I}$$

**微分方程**：

$$i\hbar\frac{d\hat{U}}{dt} = \hat{H}\hat{U}$$

### 13.1.3 指数算符的定义

算符指数 $e^{\hat{A}}$ 通过泰勒级数定义：

$$e^{\hat{A}} = \sum_{n=0}^\infty \frac{\hat{A}^n}{n!} = \hat{I} + \hat{A} + \frac{\hat{A}^2}{2!} + \cdots$$

对于 $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$，如果 $\hat{H}$ 有本征分解 $\hat{H} = \sum_n E_n|n\rangle\langle n|$，则：

$$\hat{U}(t) = \sum_n e^{-iE_n t/\hbar}|n\rangle\langle n|$$

---

## 13.2 定态与能量本征态

### 13.2.1 定态的定义

如果初始态是能量本征态 $|\psi(0)\rangle = |n\rangle$（$\hat{H}|n\rangle = E_n|n\rangle$），则：

$$|\psi(t)\rangle = \hat{U}(t)|n\rangle = e^{-iE_n t/\hbar}|n\rangle$$

这样的态叫做**定态**（stationary state）。

### 13.2.2 定态的性质

**概率密度不随时间变化**：

$$|\psi(t)\rangle = e^{-iE_n t/\hbar}|n\rangle$$

$$|\langle\vec{r}|\psi(t)\rangle|^2 = |e^{-iE_n t/\hbar}\phi_n(\vec{r})|^2 = |\phi_n(\vec{r})|^2$$

时间因子 $e^{-iE_n t/\hbar}$ 的模为 1，对概率密度没有贡献。

**期望值不随时间变化**：

对于任何不显含时间的算符 $\hat{A}$：

$$\langle A\rangle_t = \langle\psi(t)|\hat{A}|\psi(t)\rangle = \langle n|\hat{A}|n\rangle$$

与时间无关。

### 13.2.3 一般态的时间演化

如果初始态不是能量本征态，可以按能量本征态展开：

$$|\psi(0)\rangle = \sum_n c_n|n\rangle$$

则：

$$|\psi(t)\rangle = \sum_n c_n e^{-iE_n t/\hbar}|n\rangle$$

概率幅 $c_n(t) = c_n e^{-iE_n t/\hbar}$，概率 $|c_n(t)|^2 = |c_n|^2$ 不随时间变化。

**物理意义**：能量测量结果的概率分布不随时间变化（能量守恒）。

---

## 13.3 海森堡绘景

### 13.3.1 薛定谔绘景 vs 海森堡绘景

**薛定谔绘景**：态矢量随时间演化，算符不随时间变化（除非显含时间）。

$$|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$$

$$\hat{A}_S = \hat{A}$$

**海森堡绘景**：态矢量不随时间变化，算符随时间演化。

$$|\psi_H\rangle = |\psi(0)\rangle$$

$$\hat{A}_H(t) = \hat{U}^\dagger(t)\hat{A}_S\hat{U}(t) = e^{i\hat{H}t/\hbar}\hat{A}e^{-i\hat{H}t/\hbar}$$

### 13.3.2 两种绘景的等价性

期望值在两种绘景中相同：

$$\langle A\rangle_t = \langle\psi(t)|\hat{A}_S|\psi(t)\rangle = \langle\psi_H|\hat{A}_H(t)|\psi_H\rangle$$

物理预言与绘景选择无关。

### 13.3.3 海森堡运动方程

海森堡绘景中算符的时间演化满足：

$$\frac{d\hat{A}_H}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{A}_H] + \left(\frac{\partial\hat{A}}{\partial t}\right)_H$$

如果 $\hat{A}$ 不显含时间：

$$\frac{d\hat{A}_H}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{A}_H]$$

这与经典力学中的哈密顿方程形式类似：

$$\frac{dA}{dt} = \{A, H\} \quad \leftrightarrow \quad \frac{d\hat{A}_H}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{A}_H]$$

其中 $\{,\}$ 是泊松括号。

---

## 13.4 守恒量

### 13.4.1 守恒量的定义

力学量 $\hat{A}$ 是**守恒量**，如果：

1. $\hat{A}$ 不显含时间：$\partial\hat{A}/\partial t = 0$
2. $\hat{A}$ 与哈密顿量对易：$[\hat{H}, \hat{A}] = 0$

### 13.4.2 守恒量的性质

**期望值守恒**：

由 Ehrenfest 定理：

$$\frac{d\langle A\rangle}{dt} = \frac{i}{\hbar}\langle[\hat{H}, \hat{A}]\rangle + \left\langle\frac{\partial\hat{A}}{\partial t}\right\rangle = 0$$

**概率分布守恒**：

测量 $A$ 得到 $a_n$ 的概率 $P(a_n) = |c_n|^2$ 不随时间变化。

**共同本征态**：

由于 $[\hat{H}, \hat{A}] = 0$，$\hat{H}$ 和 $\hat{A}$ 有共同本征态。可以在能量本征态中同时确定 $A$ 的值。

### 13.4.3 守恒量的例子

**动量守恒**（自由粒子）：

$$\hat{H} = \frac{\hat{p}^2}{2m}, \quad [\hat{H}, \hat{p}] = 0$$

**角动量守恒**（中心力场）：

$$\hat{H} = \frac{\hat{p}^2}{2m} + V(r), \quad [\hat{H}, \hat{L}^2] = 0, \quad [\hat{H}, \hat{L}_z] = 0$$

**宇称守恒**（对称势）：

$$V(-x) = V(x) \Rightarrow [\hat{H}, \hat{P}] = 0$$

其中 $\hat{P}$ 是宇称算符。

---

## 13.5 Ehrenfest 定理

### 13.5.1 定理内容

**Ehrenfest 定理**：力学量期望值的时间演化为

$$\frac{d\langle A\rangle}{dt} = \frac{i}{\hbar}\langle[\hat{H}, \hat{A}]\rangle + \left\langle\frac{\partial\hat{A}}{\partial t}\right\rangle$$

### 13.5.2 推导

$$\frac{d\langle A\rangle}{dt} = \frac{d}{dt}\langle\psi|\hat{A}|\psi\rangle$$

$$= \left(\frac{\partial\langle\psi|}{\partial t}\right)\hat{A}|\psi\rangle + \langle\psi|\frac{\partial\hat{A}}{\partial t}|\psi\rangle + \langle\psi|\hat{A}\left(\frac{\partial|\psi\rangle}{\partial t}\right)$$

由薛定谔方程 $i\hbar\partial|\psi\rangle/\partial t = \hat{H}|\psi\rangle$ 及其共轭 $-i\hbar\partial\langle\psi|/\partial t = \langle\psi|\hat{H}$：

$$= \frac{1}{-i\hbar}\langle\psi|\hat{H}\hat{A}|\psi\rangle + \left\langle\frac{\partial\hat{A}}{\partial t}\right\rangle + \frac{1}{i\hbar}\langle\psi|\hat{A}\hat{H}|\psi\rangle$$

$$= \frac{i}{\hbar}\langle\psi|(\hat{H}\hat{A} - \hat{A}\hat{H})|\psi\rangle + \left\langle\frac{\partial\hat{A}}{\partial t}\right\rangle$$

$$= \frac{i}{\hbar}\langle[\hat{H}, \hat{A}]\rangle + \left\langle\frac{\partial\hat{A}}{\partial t}\right\rangle$$

$\blacksquare$

### 13.5.3 经典极限

取 $\hat{A} = \hat{x}$：

$$\frac{d\langle x\rangle}{dt} = \frac{i}{\hbar}\langle[\hat{H}, \hat{x}]\rangle = \frac{i}{\hbar}\left\langle\left[\frac{\hat{p}^2}{2m}, \hat{x}\right]\right\rangle = \frac{\langle p\rangle}{m}$$

取 $\hat{A} = \hat{p}$：

$$\frac{d\langle p\rangle}{dt} = \frac{i}{\hbar}\langle[\hat{H}, \hat{p}]\rangle = \frac{i}{\hbar}\langle[V(\hat{x}), \hat{p}]\rangle = -\left\langle\frac{dV}{dx}\right\rangle = \langle F\rangle$$

这正是牛顿第二定律的量子版本：

$$m\frac{d^2\langle x\rangle}{dt^2} = \langle F\rangle$$

在经典极限（波包窄，$\langle F(x)\rangle \approx F(\langle x\rangle)$），还原为经典力学。

---

## 13.6 对称性与守恒律

### 13.6.1 诺特定理

**诺特定理**（量子版本）：每条连续对称性对应一个守恒量。

### 13.6.2 空间平移与动量守恒

如果系统具有空间平移对称性（$V(x + a) = V(x)$），则动量守恒。

**生成元**：平移算符 $\hat{T}(a) = e^{-i\hat{p}a/\hbar}$，生成元是 $\hat{p}/\hbar$。

### 13.6.3 时间平移与能量守恒

如果系统具有时间平移对称性（$\hat{H}$ 不显含时间），则能量守恒。

**生成元**：时间演化算符 $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$，生成元是 $\hat{H}/\hbar$。

### 13.6.4 旋转对称与角动量守恒

如果系统具有旋转对称性（中心力场 $V(r)$），则角动量守恒。

**生成元**：旋转算符 $\hat{R}(\theta) = e^{-i\hat{L}\theta/\hbar}$，生成元是 $\hat{L}/\hbar$。

### 13.6.5 宇称与分立对称性

**宇称算符** $\hat{P}$：$\hat{P}\psi(x) = \psi(-x)$

宇称是**分立对称性**（不是连续对称性），不直接对应诺特定理。

如果 $V(-x) = V(x)$，则 $[\hat{H}, \hat{P}] = 0$，宇称守恒。

能量本征态可以有确定的宇称（偶函数或奇函数）。

---

## 13.7 简并与对称性

### 13.7.1 对称性导致简并

如果哈密顿量具有某种对称性，能级可能出现简并。

**例子**：
- **三维各向同性谐振子**：旋转对称性 → 能级简并
- **氢原子**：SO(4)对称性 → $n^2$ 重简并
- **周期晶格**：平移对称性 → 能带结构

### 13.7.2 对称性破缺与简并解除

如果对称性被破坏，简并可能解除。

**例子**：
- **Zeeman效应**：外加磁场破坏旋转对称性 → 能级分裂
- **Stark效应**：外加电场破坏宇称对称性 → 能级分裂
- **晶体场**：晶格势破坏球对称性 → 轨道简并解除

---

## 本章小结

1. **时间演化算符**：$\hat{U}(t) = e^{-i\hat{H}t/\hbar}$，幺正、满足群性质。

2. **定态**：能量本征态，概率密度和期望值不随时间变化。

3. **海森堡绘景**：算符演化，态不变；与薛定谔绘景等价。

4. **守恒量**：$[\hat{H}, \hat{A}] = 0$ 且 $\partial\hat{A}/\partial t = 0$，期望值和概率分布守恒。

5. **Ehrenfest定理**：量子期望值的运动方程，经典极限还原为牛顿定律。

6. **对称性与守恒律**：空间平移→动量守恒，时间平移→能量守恒，旋转→角动量守恒。

7. **简并与对称性**：对称性导致简并，对称性破缺解除简并。

---

## 公式索引

| 编号 | 公式 | 含义 | 推导链接 |
|------|------|------|----------|
| [F174](#graph?f=F174) | $d\langle A\rangle/dt = (i/\hbar)\langle[\hat{H}, \hat{A}]\rangle + \langle\partial\hat{A}/\partial t\rangle$ | Ehrenfest定理 | [查看推导](#graph?f=F174) |
| [F175](#graph?f=F175) | $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ | 时间演化算符 | [查看推导](#graph?f=F175) |
| [F176](#graph?f=F176) | $[\hat{H}, \hat{A}] = 0 \Rightarrow \langle A\rangle$ 恒定 | 守恒量判据 | [查看推导](#graph?f=F176) |
| [F177](#graph?f=F177) | 对称性→守恒律 | 诺特定理 | [查看推导](#graph?f=F177) |
| [F178](#graph?f=F178) | 薛定谔绘景海森堡绘景 | 绘景变换 | [查看推导](#graph?f=F178) |
| [F179](#graph?f=F179) | $\hat{P}\psi(x) = \psi(-x)$ | 宇称算符 | [查看推导](#graph?f=F179) |
| [F180](#graph?f=F180) | $\hat{T}(a) = e^{-i\hat{p}a/\hbar}$ | 平移生成元 | [查看推导](#graph?f=F180) |

---

## 思考题

1. 为什么时间演化算符必须是幺正的？如果不是幺正的，会有什么问题？

2. 定态的概率密度为什么不随时间变化？

3. 薛定谔绘景和海森堡绘景有什么物理区别？为什么两种绘景给出相同的预言？

4. 守恒量的概率分布为什么守恒？

5. 从Ehrenfest定理推导经典极限下的牛顿第二定律。

---


