# 第19章 · 散射理论与Born近似

> 高能物理实验的核心手段：用一束粒子轰击靶，看散射后的角分布，反推相互作用势。从卢瑟福发现原子核到LHC发现Higgs玻色子，散射理论是量子力学最重要的应用之一。

---

## 19.1 散射实验的基本图像

### 19.1.1 经典散射

经典力学中，粒子射向靶心，偏转角度 $\theta$ 由碰撞参数 $b$（入射轨迹到靶心的垂直距离）和相互作用势 $V(r)$ 共同决定。

**微分散射截面** $\frac{d\sigma}{d\Omega}$：单位立体角内散射的粒子数与入射流密度之比。物理上就是"靶子把粒子散射到某个方向的概率有多大"。

### 19.1.2 量子散射

量子力学中，入射粒子是平面波 $e^{ikz}$，遇到势 $V(r)$ 后变成**球面出射波**叠加在平面波上：

$$\psi(\mathbf{r})\xrightarrow{r\to\infty}e^{ikz}+f(\theta,\phi)\frac{e^{ikr}}{r}$$

$f(\theta,\phi)$ 是**散射振幅**，包含势的全部信息。微分散射截面：

$$\frac{d\sigma}{d\Omega}=|f(\theta,\phi)|^2$$

---

## 19.2 分波法（Partial Wave Analysis）

### 19.2.1 中心势的简化

如果势是球对称的 $V(r)$，散射振幅只依赖 $\theta$（不依赖 $\phi$）。入射平面波可以展开为各角动量分波的叠加：

$$e^{ikz}=\sum_{\ell=0}^\infty i^\ell(2\ell+1)j_\ell(kr)P_\ell(\cos\theta)$$

其中 $j_\ell$ 是球贝塞尔函数，$P_\ell$ 是勒让德多项式。

### 19.2.2 相移

每个分波 $\ell$ 在势的作用下获得一个**相移** $\delta_\ell$——径向波函数在大 $r$ 处的渐近相位相对于自由波的偏移。

散射振幅：

$$f(\theta)=\frac{1}{k}\sum_{\ell=0}^\infty(2\ell+1)e^{i\delta_\ell}\sin\delta_\ell\,P_\ell(\cos\theta)$$

总截面：

$$\sigma_{\text{tot}}=\frac{4\pi}{k^2}\sum_{\ell=0}^\infty(2\ell+1)\sin^2\delta_\ell$$

### 19.2.3 低能散射

当 $ka\ll 1$（$a$ 是势的范围，$k$ 是波数），只有 $\ell=0$（s波）贡献显著：

$$f\approx\frac{1}{k}e^{i\delta_0}\sin\delta_0,\quad \sigma\approx\frac{4\pi}{k^2}\sin^2\delta_0$$

定义**散射长度** $a_s=-\lim_{k\to 0}\frac{\tan\delta_0}{k}$，低能截面 $\sigma\approx 4\pi a_s^2$。

---

## 19.3 Born近似

### 19.3.1 适用条件

当势很弱（$V\ll E$）或能量很高时，散射波近似为平面波，可以用**微扰法**求解。这就是 Born 近似。

### 19.3.2 第一Born近似

散射振幅的一阶近似：

$$f(\theta,\phi)=-\frac{m}{2\pi\hbar^2}\int e^{-i\mathbf{q}\cdot\mathbf{r}}V(\mathbf{r})\,d^3r$$

其中 $\mathbf{q}=\mathbf{k}_f-\mathbf{k}_i$ 是**动量转移**，$|\mathbf{q}|=2k\sin(\theta/2)$。

**物理意义**：散射振幅是势的**傅里叶变换**（在动量转移 $\mathbf{q}$ 处取值）。

### 19.3.3 几个例子

**例1：Yukawa势** $V(r)=V_0\frac{e^{-\mu r}}{r}$

$$f(\theta)=-\frac{2mV_0}{\hbar^2(q^2+\mu^2)}$$

令 $\mu\to 0$、$V_0=\frac{Z_1 Z_2 e^2}{4\pi\epsilon_0}$，得到**库仑散射**的Born近似：

$$\frac{d\sigma}{d\Omega}=\left(\frac{Z_1 Z_2 e^2}{16\pi\epsilon_0 E}\right)^2\frac{1}{\sin^4(\theta/2)}$$

这正是卢瑟福散射公式！量子力学与经典力学在此巧合一致。

**例2：高斯势** $V(r)=V_0 e^{-r^2/a^2}$

$$f(\theta)=-\frac{mV_0 a^3}{2\sqrt{\pi}\hbar^2}e^{-q^2a^2/4}$$

前向散射（$q=0,\theta=0$）最强，随角度增大指数衰减。

---

## 19.4 光学定理

散射振幅的前向值（$\theta=0$）与总截面有一个深刻关系：

$$\sigma_{\text{tot}}=\frac{4\pi}{k}\text{Im}\,f(0)$$

**光学定理**：前向散射的虚部正比于总截面。

物理原因：前向散射波与入射平面波干涉，使入射束减弱——减弱的部分就是被散射到其他方向的粒子。这是概率守恒的直接结果。

---

## 19.5 共振散射

### 19.5.1 Breit-Wigner公式

当入射能量接近势的某个准束缚态能量时，某个分波的相移快速通过 $\pi/2$，截面出现尖锐的峰：

$$\sigma_\ell=\frac{4\pi}{k^2}(2\ell+1)\frac{(\Gamma/2)^2}{(E-E_R)^2+(\Gamma/2)^2}$$

$E_R$ 是共振能量，$\Gamma$ 是共振宽度。

### 19.5.2 寿命与宽度的关系

共振态的平均寿命：

$$\tau=\frac{\hbar}{\Gamma}$$

这是能量-时间不确定关系 $\Delta E\cdot\Delta t\sim\hbar$ 的直接体现：寿命越短的态，能量越不确定，共振峰越宽。

### 19.5.3 核物理中的共振

中子被重核散射时，在特定能量出现大量尖锐共振峰——每个峰对应复合核的一个准束缚态。Bohr 的复合核模型（1936）由此建立。

---

## 19.6 Lippmann-Schwinger方程

### 19.6.1 积分方程形式

散射问题可以严格地写成积分方程：

$$|\psi^{(+)}\rangle=|\phi\rangle+\frac{1}{E-\hat H_0+i\epsilon}\hat V|\psi^{(+)}\rangle$$

其中 $|\phi\rangle$ 是入射平面波态，$\hat H_0$ 是自由哈密顿量，$\hat V$ 是散射势，$\epsilon\to 0^+$ 保证出射波边界条件。

### 19.6.2 Born级数

迭代求解 Lippmann-Schwinger 方程，得到 Born 级数：

$$f=f^{(1)}+f^{(2)}+f^{(3)}+\cdots$$

第一Born近似 $f^{(1)}$ 就是上一节的公式。高阶项对应多次散射修正。

---

## 19.7 散射理论的应用

### 19.7.1 电子-原子散射

用电子束探测原子结构。Rutherford 用 $\alpha$ 粒子散射发现原子核；现代用高能电子散射探测核内电荷分布和核子结构（Hofstadter 实验，1961年诺贝尔奖）。

### 19.7.2 中子散射

中子不带电，与原子核通过短程核力相互作用。中子散射是研究晶体磁结构（中子有磁矩）和轻元素位置（X射线对轻元素不敏感）的有力工具。

### 19.7.3 量子化学中的散射

低能电子-分子散射涉及分子轨道的对称性、临时负离子态（共振）、以及化学反应的量子隧穿。

---

## 19.8 本章小结

| 概念 | 要点 |
|---|---|
| 散射振幅 | $f(\theta,\phi)$，截面 $d\sigma/d\Omega=|f|^2$ |
| 分波法 | 按角动量展开，相移 $\delta_\ell$ |
| Born近似 | 弱势/高能近似，$f\propto\tilde V(\mathbf{q})$ |
| 光学定理 | $\sigma_{\text{tot}}=\frac{4\pi}{k}\text{Im}\,f(0)$ |
| 共振散射 | Breit-Wigner公式，$\tau=\hbar/\Gamma$ |
| Lippmann-Schwinger | 散射的严格积分方程 |

---

> **下一步**：散射理论处理的是连续谱问题。现在回到束缚态——如果哈密顿量不能精确求解，但接近一个可解的哈密顿量，如何近似求能级和波函数？这就是**定态微扰论**，第20章的主题。
