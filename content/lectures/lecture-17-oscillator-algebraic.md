
**上一章**：[第16章](https://kinghihido.github.io/quantum-mechanics-notes/content/lectures/lecture-16-hydrogen-atom.md)
# 第17章 · 谐振子代数解法与相干态

> 第8章我们用解微分方程的方法得到了谐振子的能级和波函数（厄米多项式）。本章介绍一种更深刻、更代数的方法——**升降算符法**（Dirac, 1930），以及由此引出的**相干态**。这套方法直接通向量子场论的粒子产生与湮灭。

---

## 17.1 升降算符的构造

一维谐振子哈密顿量：

$$\hat H=\frac{\hat p^2}{2m}+\frac{1}{2}m\omega^2\hat x^2$$

定义**湮灭算符**（ lowering / annihilation）和**产生算符**（raising / creation）：

$$\hat a=\sqrt{\frac{m\omega}{2\hbar}}\left(\hat x+\frac{i\hat p}{m\omega}\right),\quad \hat a^\dagger=\sqrt{\frac{m\omega}{2\hbar}}\left(\hat x-\frac{i\hat p}{m\omega}\right)$$

反过来：

$$\hat x=\sqrt{\frac{\hbar}{2m\omega}}(\hat a+\hat a^\dagger),\quad \hat p=-i\sqrt{\frac{m\omega\hbar}{2}}(\hat a-\hat a^\dagger)$$

### 17.1.1 基本对易关系

由 $[\hat x,\hat p]=i\hbar$，可推出：

$$[\hat a,\hat a^\dagger]=1$$

这是整个代数方法的基石。注意 $\hat a$ 和 $\hat a^\dagger$ 都不是厄米算符（不对应可观测量），但它们的关系极其简洁。

### 17.1.2 哈密顿量的重写

把 $\hat x,\hat p$ 用 $\hat a,\hat a^\dagger$ 代入 $\hat H$，展开整理：

$$\hat H=\hbar\omega\left(\hat a^\dagger\hat a+\frac{1}{2}\right)=\hbar\omega\left(\hat N+\frac{1}{2}\right)$$

其中 $\hat N=\hat a^\dagger\hat a$ 是**粒子数算符**。

---

## 17.2 能级的代数推导

### 17.2.1 粒子数算符的本征值

设 $|n\rangle$ 是 $\hat N$ 的本征态：$\hat N|n\rangle=n|n\rangle$。

利用对易关系可以证明：

$$[\hat N,\hat a]=-\hat a,\quad [\hat N,\hat a^\dagger]=\hat a^\dagger$$

因此：

$$\hat N(\hat a|n\rangle)=(\hat a\hat N-\hat a)|n\rangle=(n-1)(\hat a|n\rangle)$$
$$\hat N(\hat a^\dagger|n\rangle)=(n+1)(\hat a^\dagger|n\rangle)$$

**结论**：$\hat a$ 把本征值降 1（湮灭一个量子），$\hat a^\dagger$ 把本征值升 1（产生一个量子）。

### 17.2.2 能级谱的推导

1. 因为 $\hat N=\hat a^\dagger\hat a$，对任意态 $|\psi\rangle$：$\langle\psi|\hat N|\psi\rangle=\|\hat a|\psi\rangle\|^2\ge 0$，所以 $n\ge 0$。

2. 反复用 $\hat a$ 降低 $n$，必须有一个下限——否则会出现负本征值，矛盾。

3. 设最低态为 $|0\rangle$，满足 $\hat a|0\rangle=0$（湮灭算符作用在基态上得零矢量）。

4. 由此 $\hat N|0\rangle=0$，即最低本征值为 $0$。

5. 反复用 $\hat a^\dagger$ 升高，得到 $n=0,1,2,\dots$

因此能量：

$$E_n=\hbar\omega\left(n+\frac{1}{2}\right),\quad n=0,1,2,\dots$$

**零点能** $E_0=\frac{1}{2}\hbar\omega$ 自然出现——基态不能静止，因为 $\hat a|0\rangle=0$ 意味着 $\hat x$ 和 $\hat p$ 的涨落之积恰好达到不确定关系的下限。

### 17.2.3 归一化

$$\hat a|n\rangle=\sqrt{n}|n-1\rangle,\quad \hat a^\dagger|n\rangle=\sqrt{n+1}|n+1\rangle$$

任意激发态可以从基态构造：

$$|n\rangle=\frac{(\hat a^\dagger)^n}{\sqrt{n!}}|0\rangle$$

---

## 17.3 矩阵元与选择定则

在粒子数表象中，算符的矩阵元非常容易计算。

### 17.3.1 位置和动量的矩阵元

$$\langle m|\hat x|n\rangle=\sqrt{\frac{\hbar}{2m\omega}}\left(\sqrt{n}\,\delta_{m,n-1}+\sqrt{n+1}\,\delta_{m,n+1}\right)$$

$$\langle m|\hat p|n\rangle=-i\sqrt{\frac{m\omega\hbar}{2}}\left(\sqrt{n}\,\delta_{m,n-1}-\sqrt{n+1}\,\delta_{m,n+1}\right)$$

**选择定则**：$\hat x$ 和 $\hat p$ 只连接相邻能级（$\Delta n=\pm 1$）。这解释了为什么谐振子的光谱只有一条频率 $\omega$。

### 17.3.2 动能和势能的期望值

对任意本征态 $|n\rangle$：

$$\langle n|\hat T|n\rangle=\langle n|\hat V|n\rangle=\frac{E_n}{2}=\frac{1}{2}\hbar\omega\left(n+\frac{1}{2}\right)$$

这是**位力定理**（Virial Theorem）对谐振子的特殊形式：动能和势能平均各占一半。

---

## 17.4 相干态

### 17.4.1 定义

**相干态** $|\alpha\rangle$ 是湮灭算符的本征态：

$$\hat a|\alpha\rangle=\alpha|\alpha\rangle$$

其中 $\alpha$ 是任意复数。注意 $\hat a$ 不是厄米算符，所以 $\alpha$ 可以是复数（本征值不必是实数）。

### 17.4.2 在粒子数基下展开

$$|\alpha\rangle=e^{-|\alpha|^2/2}\sum_{n=0}^\infty\frac{\alpha^n}{\sqrt{n!}}|n\rangle$$

这是一个归一化态（$\langle\alpha|\alpha\rangle=1$），但不同 $\alpha$ 的相干态**不正交**：

$$|\langle\beta|\alpha\rangle|^2=e^{-|\alpha-\beta|^2}$$

当 $|\alpha-\beta|\gg 1$ 时近似正交，但严格来说它们构成**过完备基**。

### 17.4.3 物理性质

相干态是"最接近经典"的量子态：

1. **最小不确定波包**：$\Delta x\Delta p=\hbar/2$，且 $\Delta x=\Delta p$（等分配）。

2. **期望值做经典运动**：
$$\langle\alpha|\hat x(t)|\alpha\rangle=x_0\cos(\omega t-\phi)$$
其中 $\alpha=|\alpha|e^{i\phi}$，$x_0=\sqrt{2\hbar/m\omega}\,|\alpha|$。波包的中心完全按照经典谐振子轨迹运动！

3. **波包不扩散**：与一般量子波包不同，谐振子相干态的宽度始终不变。

4. **光子数分布**：$P(n)=|\langle n|\alpha\rangle|^2=e^{-\bar n}\frac{\bar n^n}{n!}$，是泊松分布，$\bar n=|\alpha|^2$。

### 17.4.4 产生方式

相干态可以通过**位移算符**从真空态产生：

$$|\alpha\rangle=\hat D(\alpha)|0\rangle,\quad \hat D(\alpha)=e^{\alpha\hat a^\dagger-\alpha^*\hat a}$$

物理上，经典电流驱动电磁场真空态，产生的就是相干态——这就是激光的量子理论。

---

## 17.5 多体谐振子与声子

### 17.5.1 N个独立谐振子

$N$ 个独立谐振子的总哈密顿量：

$$\hat H=\sum_{k=1}^N\hbar\omega_k\left(\hat a_k^\dagger\hat a_k+\frac{1}{2}\right)$$

本征态用**占有数**标记：$|n_1,n_2,\dots,n_N\rangle$，总能量

$$E=\sum_k\hbar\omega_k\left(n_k+\frac{1}{2}\right)$$

### 17.5.2 从粒子到声子

在固体物理中，$N$ 个耦合的原子振动可以通过正则变换解耦为 $N$ 个独立的**简正模**，每个简正模就是一个量子谐振子。能量量子 $\hbar\omega_k$ 被称为**声子**（phonon）。

声子不是"真实的粒子"，而是集体激发的量子。但它的数学描述与光子完全相同——都是谐振子的激发态。

### 17.5.3 热容的 Einstein 与 Debye 模型

- **Einstein 模型**（1907）：假设所有原子独立同频振动，$C_V$ 在高温趋于 Dulong-Petit 定律 $3Nk_B$，低温指数衰减。
- **Debye 模型**（1912）：考虑连续频谱 $\omega\in[0,\omega_D]$，低温 $C_V\propto T^3$，与实验完美吻合。

---

## 17.6 代数方法的力量

升降算符方法的价值远超谐振子本身：

1. **量子场论**：场的每个模式就是一个谐振子，$\hat a_k$ 湮灭动量为 $k$ 的粒子，$\hat a_k^\dagger$ 产生它。真空 $|0\rangle$ 是没有粒子的态。

2. **角动量**：第14章的 $J_\pm=J_x\pm iJ_y$ 本质上就是升降算符，代数结构与谐振子同构。

3. **氢原子**：存在隐藏的 $SO(4)$ 对称性，也可以用升降算符处理（Pauli, 1926），得到能级简并。

4. **超对称量子力学**：用算符对 $\hat A,\hat A^\dagger$ 把不同势的薛定谔方程联系起来。

**核心思想**：量子力学中许多问题的"可解性"来自隐藏的代数结构。找到正确的算符和对易关系，比硬解微分方程更深刻。

---

## 17.7 本章小结

| 概念 | 要点 |
|---|---|
| 升降算符 | $\hat a,\hat a^\dagger$，$[\hat a,\hat a^\dagger]=1$ |
| 粒子数算符 | $\hat N=\hat a^\dagger\hat a$，本征值 $n=0,1,2,\dots$ |
| 能级 | $E_n=\hbar\omega(n+1/2)$ |
| 零点能 | $E_0=\hbar\omega/2$（不确定关系的直接后果） |
| 相干态 | $\hat a|\alpha\rangle=\alpha|\alpha\rangle$，最小不确定波包 |
| 位移算符 | $|\alpha\rangle=\hat D(\alpha)|0\rangle$ |
| 多体推广 | 声子、量子场论的粒子产生湮灭 |

---

> **下一步**：到目前为止，我们讨论的都是单个粒子。但当有两个或更多全同粒子时，量子力学出现了一个全新的现象——**交换对称性**，它决定了元素周期表的结构、金属的导电性、甚至白矮星为什么不会坍缩。这就是第18章的主题。

**下一章**：[第18章](https://kinghihido.github.io/quantum-mechanics-notes/content/lectures/lecture-18-identical-particles.md)
