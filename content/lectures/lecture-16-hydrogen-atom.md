
# 第16章 · 三维中心势与氢原子

> 从一维走向三维，最重要的特殊情况是**中心势** $V(r)$——势能只依赖于到原点的距离。氢原子是物理学中唯一能精确求解的原子模型，也是理解原子结构、元素周期表的起点。

---

## 16.1 球坐标分离变量

三维定态薛定谔方程

$$-\frac{\hbar^2}{2m}\nabla^2\psi(\mathbf{r})+V(r)\psi(\mathbf{r})=E\psi(\mathbf{r})$$

在球坐标 $(r,\theta,\phi)$ 下，拉普拉斯算符分裂为径向部分和角向部分：

$$\nabla^2=\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right)+\frac{1}{r^2}\Lambda^2$$

其中 $\Lambda^2$ 是**角动量平方算符**（与第14章球谐函数部分对应）：

$$\Lambda^2=\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right)+\frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}$$

因为 $V$ 只依赖 $r$，角向部分完全由 $\Lambda^2$ 决定，与 $V(r)$ 的具体形式无关。这提示我们做分离变量：

$$\psi(r,\theta,\phi)=R(r)\,Y_\ell^m(\theta,\phi)$$

代入方程，除以 $R\,Y$，径向和角向各自等于常数，得到两个独立方程。

---

## 16.2 角向方程与球谐函数

角向方程正是 $\Lambda^2$ 的本征值问题：

$$\Lambda^2 Y_\ell^m=-\ell(\ell+1)Y_\ell^m$$

本征函数 $Y_\ell^m(\theta,\phi)$ 就是**球谐函数**（Spherical Harmonics），其中：

- $\ell=0,1,2,\dots$ 是**角量子数**（轨道角动量大小）
- $m=-\ell,-\ell+1,\dots,\ell$ 是**磁量子数**（角动量 $z$ 分量）

球谐函数的物理意义：

| 量子数 | 决定什么 | 取值范围 |
|---|---|---|
| $\ell$ | 轨道角动量大小 $L=\sqrt{\ell(\ell+1)}\hbar$ | $0,1,2,\dots$ |
| $m$ | $L_z=m\hbar$（空间量子化） | $-\ell,\dots,+\ell$ |

前几个球谐函数：

$$Y_0^0=\frac{1}{\sqrt{4\pi}},\quad Y_1^0=\sqrt{\frac{3}{4\pi}}\cos\theta,\quad Y_1^{\pm1}=\mp\sqrt{\frac{3}{8\pi}}\sin\theta\,e^{\pm i\phi}$$

**关键性质**：球谐函数构成单位球面上平方可积函数的完备正交基。任意角向函数都可以展开为球谐函数的线性组合。

---

## 16.3 径向方程

分离变量后，径向函数 $R(r)$ 满足：

$$-\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dR}{dr}\right)+\left[V(r)+\frac{\ell(\ell+1)\hbar^2}{2mr^2}\right]R=ER$$

引入 $u(r)=rR(r)$，方程化简为**一维等效势**形式：

$$-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2}+V_{\text{eff}}(r)\,u=Eu$$

其中有效势

$$V_{\text{eff}}(r)=V(r)+\frac{\ell(\ell+1)\hbar^2}{2mr^2}$$

第二项是**离心势垒**：角动量越大，粒子越被"甩"向外侧，等效于在中心附近多了一道排斥势。

边界条件：$u(0)=0$（保证 $R$ 在原点不发散），$u(\infty)\to 0$（束缚态）。

---

## 16.4 氢原子精确解

氢原子中，电子在质子的库仑场中运动：

$$V(r)=-\frac{e^2}{4\pi\epsilon_0}\frac{1}{r}\equiv-\frac{ke^2}{r}$$

这是一个可以在数学上完全精确求解的问题（1926年薛定谔本人完成的）。

### 16.4.1 能级公式

$$E_n=-\frac{m_e(ke^2)^2}{2\hbar^2}\frac{1}{n^2}=-\frac{13.6\,\text{eV}}{n^2},\quad n=1,2,3,\dots$$

$n$ 是**主量子数**，决定能量。对给定 $n$，角量子数 $\ell$ 的取值范围是 $0,1,\dots,n-1$。

**简并度**：每个能级 $E_n$ 的简并度为

$$g_n=\sum_{\ell=0}^{n-1}(2\ell+1)=n^2$$

如果考虑自旋（$s=\pm 1/2$），简并度翻倍为 $2n^2$。

### 16.4.2 波函数

氢原子波函数的完整标记：

$$\psi_{n\ell m}(r,\theta,\phi)=R_{n\ell}(r)\,Y_\ell^m(\theta,\phi)$$

径向函数 $R_{n\ell}(r)$ 包含**关联拉盖尔多项式** $L_{n-\ell-1}^{2\ell+1}$：

$$R_{n\ell}(r)\propto e^{-r/na_0}\left(\frac{2r}{na_0}\right)^\ell L_{n-\ell-1}^{2\ell+1}\left(\frac{2r}{na_0}\right)$$

其中 $a_0=\frac{\hbar^2}{m_ek e^2}=0.529\,\text{Å}$ 是**玻尔半径**。

前几个径向波函数：

| $(n,\ell)$ | $R_{n\ell}(r)$ | 名称 |
|---|---|---|
| $(1,0)$ | $\frac{2}{a_0^{3/2}}e^{-r/a_0}$ | 1s |
| $(2,0)$ | $\frac{1}{\sqrt{2}a_0^{3/2}}(1-\frac{r}{2a_0})e^{-r/2a_0}$ | 2s |
| $(2,1)$ | $\frac{1}{\sqrt{24}a_0^{3/2}}\frac{r}{a_0}e^{-r/2a_0}$ | 2p |

### 16.4.3 概率分布

基态（1s）的径向概率密度：

$$P(r)=r^2|R_{10}(r)|^2=\frac{4r^2}{a_0^3}e^{-2r/a_0}$$

对 $P(r)$ 求极大值：$\frac{dP}{dr}=0\Rightarrow r=a_0$——恰好是玻尔轨道半径！

但这不是"轨道"，而是概率最大的地方。量子力学中电子没有确定轨迹，只有概率云。

---

## 16.5 物理光谱与选择定则

### 16.5.1 光谱线系

氢原子能级跃迁发出（或吸收）光子，能量为

$$h\nu=E_n-E_m=13.6\left(\frac{1}{m^2}-\frac{1}{n^2}\right)\,\text{eV}$$

不同 $m$ 值对应不同光谱线系：

| 终态 $m$ | 线系名 | 波段 |
|---|---|---|
| 1 | Lyman | 紫外 |
| 2 | Balmer | 可见光 |
| 3 | Paschen | 红外 |
| 4 | Brackett | 远红外 |

### 16.5.2 电偶极选择定则

并非所有跃迁都能发生。电偶极辐射的选择定则：

$$\Delta\ell=\pm 1,\quad \Delta m=0,\pm 1$$

物理原因：光子携带角动量 $\hbar$，跃迁前后轨道角动量必须守恒。$\Delta\ell=0$ 被禁止是因为光子是矢量粒子（自旋1），不能只改变磁量子数而不改变轨道大小。

---

## 16.6 类氢离子与约化质量

### 16.6.1 类氢离子

核电荷为 $Ze$ 的类氢离子（He⁺, Li²⁺, …），只需将 $e^2\to Ze^2$：

$$E_n=-\frac{Z^2\times 13.6\,\text{eV}}{n^2},\quad a=\frac{a_0}{Z}$$

核电荷越大，电子被拉得更近、束缚更深。

### 16.6.2 约化质量修正

严格来说，电子和质子围绕共同质心运动。将质量 $m_e$ 替换为**约化质量**：

$$\mu=\frac{m_e m_p}{m_e+m_p}\approx m_e\left(1-\frac{m_e}{m_p}\right)$$

这使得里德伯常数从 $R_\infty$ 变为 $R_H=R_\infty\times\mu/m_e$，修正约 $0.05\%$。对精密光谱（如氢-氘同位素位移）至关重要。

---

## 16.7 三维各向同性谐振子

除了库仑势，三维各向同性谐振子 $V(r)=\frac{1}{2}m\omega^2r^2$ 也是可精确求解的。

能级：

$$E_N=\left(N+\frac{3}{2}\right)\hbar\omega,\quad N=0,1,2,\dots$$

其中 $N=2n_r+\ell$，$n_r$ 是径向量子数（径向波函数的节点数）。

简并度：$g_N=\frac{(N+1)(N+2)}{2}$（不含自旋）。

**应用**：原子核的壳层模型（核子在核内近似感受到谐振子势）、量子点的电子态、三维晶格振动（声子）。

---

## 16.8 本章小结

| 概念 | 要点 |
|---|---|
| 球坐标分离变量 | $\psi=R(r)Y_\ell^m(\theta,\phi)$ |
| 球谐函数 | 角向本征函数，$\ell,m$ 标记 |
| 有效势 | $V_{\text{eff}}=V(r)+\frac{\ell(\ell+1)\hbar^2}{2mr^2}$ |
| 氢原子能级 | $E_n=-13.6/n^2$ eV |
| 量子数 | $n$（主）、$\ell$（角）、$m$（磁） |
| 选择定则 | $\Delta\ell=\pm 1$，$\Delta m=0,\pm 1$ |
| 约化质量 | $\mu=m_em_p/(m_e+m_p)$ |

---

> **下一步**：我们已经用"解微分方程"的方式（坐标表象）求出了氢原子。但谐振子有一种更优雅的**代数方法**——用升降算符，不碰微分方程就能得到全部能级。这就是第17章的内容。

