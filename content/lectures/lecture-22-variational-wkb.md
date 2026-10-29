
# 第22章 · 变分法与近似方法

> 变分法是量子力学中最强大的近似工具之一。它不需要"可解的零级问题"，只需要一个合理的**试探波函数**（含可调参数），通过最小化能量期望值来逼近真实基态。从氦原子到分子，从核物理到凝聚态，变分法无处不在。

---

## 22.1 变分原理

### 22.1.1 核心定理

**变分定理**：对任意归一化试探波函数 $|\psi_{\text{trial}}\rangle$，

$$\langle\psi_{\text{trial}}|\hat H|\psi_{\text{trial}}\rangle\ge E_0$$

其中 $E_0$ 是真实基态能量。

**证明**：把试探态按精确本征态展开 $|\psi_{\text{trial}}\rangle=\sum_n c_n|n\rangle$，则

$$\langle\hat H\rangle=\sum_n|c_n|^2 E_n\ge E_0\sum_n|c_n|^2=E_0$$

等号成立当且仅当 $|\psi_{\text{trial}}\rangle=|0\rangle$（即试探态恰好是基态）。

### 22.1.2 使用方法

1. 选择含参数 $\alpha_1,\alpha_2,\dots$ 的试探波函数 $\psi(\mathbf{r};\alpha_1,\alpha_2,\dots)$。
2. 计算能量期望值 $E(\alpha_1,\alpha_2,\dots)=\langle\psi|\hat H|\psi\rangle/\langle\psi|\psi\rangle$。
3. 对参数求极小：$\frac{\partial E}{\partial\alpha_i}=0$。
4. 极小值 $E_{\min}$ 是基态能量的**上界**。

参数越多、试探波函数越灵活，结果越接近真实值。

---

## 22.2 经典应用：氦原子

### 22.2.1 问题

氦原子有两个电子，哈密顿量：

$$\hat H=-\frac{\hbar^2}{2m}(\nabla_1^2+\nabla_2^2)-\frac{2e^2}{4\pi\epsilon_0}\left(\frac{1}{r_1}+\frac{1}{r_2}\right)+\frac{e^2}{4\pi\epsilon_0}\frac{1}{|\mathbf{r}_1-\mathbf{r}_2|}$$

最后一项是电子-电子排斥，使问题不可分离变量，无法精确求解。

### 22.2.2 简单变分

试探波函数：两个电子各自在类氢基态，但用**有效核电荷** $Z_{\text{eff}}$ 代替真实核电荷 $Z=2$：

$$\psi(\mathbf{r}_1,\mathbf{r}_2)=\frac{Z_{\text{eff}}^3}{\pi a_0^3}e^{-Z_{\text{eff}}(r_1+r_2)/a_0}$$

$Z_{\text{eff}}$ 是变分参数——物理意义是"每个电子看到核电荷被另一个电子屏蔽了一部分"。

计算能量期望值：

$$E(Z_{\text{eff}})=\left[-2Z_{\text{eff}}^2+4Z_{\text{eff}}(Z-Z_{\text{eff}})+\frac{5}{4}Z_{\text{eff}}\right]\times 13.6\,\text{eV}$$

（具体系数来自各项积分，此处省略计算细节）

对 $Z_{\text{eff}}$ 求极小：$Z_{\text{eff}}=Z-\frac{5}{16}=2-\frac{5}{16}=\frac{27}{16}\approx 1.69$

代入得 $E_{\min}\approx-77.5\,\text{eV}$。

实验值：$-79.0\,\text{eV}$。误差约 $2\%$——对一个两电子系统来说已经相当不错。

### 22.2.3 物理诠释

$Z_{\text{eff}}=1.69<2$ 说明每个电子感受到的核电荷确实被另一个电子"屏蔽"了约 $0.31$ 个单位。这就是**屏蔽效应**的定量描述。

更精确的变分波函数可以加入电子-电子距离 $|\mathbf{r}_1-\mathbf{r}_2|$ 的依赖（Hylleraas 波函数），精度可达 $10^{-6}$ eV 量级——与实验完美吻合。

---

## 22.3 线性变分法（Ritz法）

### 22.3.1 方法

当试探波函数是多个基函数的线性组合：

$$|\psi\rangle=\sum_{i=1}^N c_i|\phi_i\rangle$$

变分原理给出广义本征值问题：

$$\mathbf{H}\mathbf{c}=E\mathbf{S}\mathbf{c}$$

其中 $H_{ij}=\langle\phi_i|\hat H|\phi_j\rangle$，$S_{ij}=\langle\phi_i|\phi_j\rangle$。

解这个矩阵方程，得到 $N$ 个本征值 $E_1\le E_2\le\dots\le E_N$ 和对应的本征矢。

### 22.3.2 性质

- $E_1$ 是基态能量的上界（变分原理）
- $E_2$ 是第一激发态能量的上界（前提是 $|\phi_i\rangle$ 与基态正交，或通过对称性分离）
- 基函数越多（$N$ 越大），结果越精确
- 当 $N\to\infty$ 且基函数完备时，得到精确解

### 22.3.3 应用

**量子化学计算**的核心方法：
- 用原子轨道的线性组合（LCAO）作为基函数
- 解 Roothaan 方程（线性变分的分子轨道版本）
- 程序包：Gaussian, ORCA, VASP 等

---

## 22.4 WKB近似

### 22.4.1 思想

WKB（Wentzel-Kramers-Brillouin）近似适用于**势能缓慢变化**的情况——波长的空间变化远小于波长本身。

在一维问题中，设 $\psi(x)=A(x)e^{iS(x)/\hbar}$，代入薛定谔方程，按 $\hbar$ 的幂次展开。

### 22.4.2 WKB波函数

**经典允许区**（$E>V(x)$）：

$$\psi(x)\approx\frac{C}{\sqrt{p(x)}}\exp\left(\pm\frac{i}{\hbar}\int p(x)dx\right),\quad p(x)=\sqrt{2m(E-V(x))}$$

**经典禁区**（$E<V(x)$）：

$$\psi(x)\approx\frac{C}{\sqrt{\kappa(x)}}\exp\left(\pm\frac{1}{\hbar}\int\kappa(x)dx\right),\quad \kappa(x)=\sqrt{2m(V(x)-E)}$$

物理图像：振幅随局部动量调整（动量大→速度快→概率密度小→振幅小），相位是经典作用量的积分。

### 22.4.3 Bohr-Sommerfeld量子化条件

对束缚态，WKB给出能级的近似公式：

$$\int_{x_1}^{x_2}p(x)dx=\left(n+\frac{1}{2}\right)\pi\hbar,\quad n=0,1,2,\dots$$

其中 $x_1,x_2$ 是两个经典转折点（$E=V(x)$ 处）。

$+1/2$ 来自转折点处的连接条件（Airy函数匹配）。对谐振子，WKB给出**精确**能级（因为势能是二次的，WKB近似恰好精确）。

### 22.4.4 隧穿概率

粒子穿过势垒的 WKB 隧穿概率：

$$T\approx\exp\left(-\frac{2}{\hbar}\int_{x_1}^{x_2}\kappa(x)dx\right)$$

这是 $\alpha$ 衰变理论（Gamow, 1928）和隧道二极管、扫描隧道显微镜（STM）的理论基础。

---

## 22.5 数值方法简介

### 22.5.1 矩阵对角化

把空间离散为 $N$ 个格点，微分算符用差分近似，哈密顿量变成 $N\times N$ 矩阵。用数值线性代数（LAPACK, ARPACK）对角化，得到本征值和本征矢。

对一维问题，$N\sim 1000$ 就足够精确。对高维问题，$N$ 指数增长（"维数灾难"），需要更聪明的方法。

### 22.5.2 密度矩阵重整化群（DMRG）

对一维强关联系统（如 Hubbard 模型、自旋链），DMRG 通过截断希尔伯特空间到"最重要的"态，可以处理 $N\sim 10^4$ 的格点，精度极高。

### 22.5.3 量子蒙特卡罗

用随机采样计算高维积分，可以处理多体费米子系统的基态和有限温度性质。符号问题（sign problem）是主要困难。

### 22.5.4 密度泛函理论（DFT）

虽然严格来说不是"变分法"的标准形式，但 DFT 的核心——Hohenberg-Kohn 变分原理——与变分法一脉相承：

$$E_0=\min_{n(\mathbf{r})}\left\{T_s[n]+E_H[n]+E_{xc}[n]+\int v_{\text{ext}}(\mathbf{r})n(\mathbf{r})d\mathbf{r}\right\}$$

对电子密度 $n(\mathbf{r})$ 变分，而非对多体波函数。这使得 DFT 可以处理数百个原子的系统，成为材料科学和化学的标准工具。

---

## 22.6 本章小结

| 方法 | 核心思想 | 适用场景 |
|---|---|---|
| 变分法 | $\langle\hat H\rangle\ge E_0$，最小化能量 | 基态能量上界 |
| 线性变分（Ritz） | 基函数展开，解广义本征值方程 | 量子化学、分子轨道 |
| WKB | 缓变势近似，经典作用量积分 | 高量子数、隧穿 |
| Bohr-Sommerfeld | $\oint p\,dx=(n+1/2)\pi\hbar$ | 半经典量子化 |
| 数值对角化 | 空间离散化，矩阵对角化 | 一维/小系统 |
| DMRG | 截断希尔伯特空间 | 一维强关联 |
| QMC | 随机采样 | 多体系统 |
| DFT | 对电子密度变分 | 材料/化学 |

---

> **下一步**：我们已经讨论了束缚态问题（势阱、谐振子、氢原子）和散射问题（分波法、Born近似）。现在回到固体物理——晶体中的电子在**周期势**中运动，会出现什么新现象？能带、带隙、导体/绝缘体/半导体——第23章。

