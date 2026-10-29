
# 第26章 · 相对论量子力学与Dirac方程

> 薛定谔方程是非相对论的——时间和空间导数的阶数不同（时间一阶、空间二阶），不满足 Lorentz 对称性。要把量子力学与狭义相对论统一，需要新的方程。Klein-Gordon 方程是最简单的尝试，但有问题；Dirac 方程天才般地解决了这些问题，同时预言了反物质的存在。

---

## 26.1 相对论性能量-动量关系

### 26.1.1 经典关系

狭义相对论中，自由粒子的能量-动量关系：

$$E^2=p^2c^2+m^2c^4$$

非相对论极限（$p\ll mc$）：

$$E=mc^2+\frac{p^2}{2m}+\cdots$$

第一项是静止能量，第二项是经典动能。

### 26.1.2 量子化

按量子力学规则 $E\to i\hbar\partial_t$，$\mathbf{p}\to-i\hbar\nabla$，代入能量-动量关系：

$$-\hbar^2\frac{\partial^2\psi}{\partial t^2}=-\hbar^2c^2\nabla^2\psi+m^2c^4\psi$$

整理得 **Klein-Gordon 方程**：

$$\left(\frac{1}{c^2}\frac{\partial^2}{\partial t^2}-\nabla^2+\frac{m^2c^2}{\hbar^2}\right)\psi=0$$

或写成协变形式 $(\Box+\mu^2)\psi=0$，其中 $\Box=\partial_\mu\partial^\mu$，$\mu=mc/\hbar$。

---

## 26.2 Klein-Gordon方程的困难

### 26.2.1 负概率问题

Klein-Gordon 方程是时间二阶的，因此需要初始条件 $\psi(\mathbf{r},0)$ 和 $\partial_t\psi(\mathbf{r},0)$。

连续性方程可以从 KG 方程推导：

$$\frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf{j}=0$$

但概率密度：

$$\rho=\frac{i\hbar}{2mc^2}\left(\psi^*\frac{\partial\psi}{\partial t}-\psi\frac{\partial\psi^*}{\partial t}\right)$$

**$\rho$ 不一定是正数！** 因为 $\psi$ 和 $\partial_t\psi$ 可以独立指定，$\rho$ 可正可负。

### 26.2.2 负能量问题

平面波解 $E=\pm\sqrt{p^2c^2+m^2c^4}$，存在负能量态。经典力学中可以忽略（粒子不会自发跳到负能量），但量子力学中跃迁不可避免——正能态粒子会不断辐射光子跌入负能海，原子不稳定。

### 26.2.3 KG方程的正确诠释

尽管作为单粒子方程失败，KG 方程在**量子场论**中获得了正确的位置——$\psi$ 不再是波函数，而是**场算符**，$\rho$ 不再是概率密度而是**电荷密度**。负概率的困难通过二次量子化消除。

---

## 26.3 Dirac方程

### 26.3.1 Dirac的天才思路（1928）

Dirac 想要一个时间一阶、空间一阶的波动方程（像薛定谔方程那样），同时满足相对论协变。

把 $E^2=p^2c^2+m^2c^4$ "开方"：

$$E=c\boldsymbol{\alpha}\cdot\mathbf{p}+\beta mc^2$$

要求 $\alpha_i,\beta$ 满足：

$$\alpha_i\alpha_j+\alpha_j\alpha_i=2\delta_{ij},\quad \alpha_i\beta+\beta\alpha_i=0,\quad \beta^2=1$$

这些是**反对易关系**，不可能用普通数满足——$\alpha_i,\beta$ 必须是**矩阵**！最小维度是 $4\times 4$。

### 26.3.2 Dirac方程

$$i\hbar\frac{\partial\psi}{\partial t}=\left(-i\hbar c\boldsymbol{\alpha}\cdot\nabla+\beta mc^2\right)\psi$$

写成协变形式（引入 $\gamma^\mu$ 矩阵）：

$$(i\hbar\gamma^\mu\partial_\mu-mc)\psi=0$$

波函数 $\psi$ 是**四分量旋量**（Dirac旋量）：

$$\psi=\begin{pmatrix}\psi_1\\\psi_2\\\psi_3\\\psi_4\end{pmatrix}$$

### 26.3.3 概率密度

Dirac 方程的概率密度：

$$\rho=\psi^\dagger\psi=|\psi_1|^2+|\psi_2|^2+|\psi_3|^2+|\psi_4|^2\ge 0$$

**正定！** Klein-Gordon 的负概率问题被解决了。

---

## 26.4 反物质的预言

### 26.4.1 负能量解的困难

Dirac 方程仍然有负能量解（$E=\pm\sqrt{p^2c^2+m^2c^4}$）。怎么办？

### 26.4.2 Dirac海（1930）

Dirac 的原始解释：所有负能态都被电子填满了（"Dirac海"），泡利不相容原理阻止正能电子跌入负能态。

空穴 = 缺少一个负能电子 = 表现为一个**正电荷、正能量**的粒子。

### 26.4.3 正电子的发现

1932年，Carl Anderson 在宇宙线中发现了**正电子**（$e^+$）——质量与电子相同、电荷相反的粒子。Dirac 的理论被辉煌地证实。

现代观点（Feynman-Stueckelberg）：不需要"Dirac海"。负能量解理解为**反粒子正能量但反向时间传播的态**。粒子-反粒子对的产生和湮灭是量子场论的自然过程。

---

## 26.5 非相对论极限：Pauli方程

### 26.5.1 加电磁场

最小耦合：$\mathbf{p}\to\mathbf{p}-q\mathbf{A}$，$E\to E-q\phi$。Dirac 方程变为：

$$i\hbar\frac{\partial\psi}{\partial t}=\left[c\boldsymbol{\alpha}\cdot(\mathbf{p}-q\mathbf{A})+\beta mc^2+q\phi\right]\psi$$

### 26.5.2 非相对论展开

把四分量旋量分为"大分量" $\phi$（正能）和"小分量" $\chi$（负能），对 $v\ll c$ 展开。

到 $1/m$ 阶，大分量满足 **Pauli 方程**：

$$i\hbar\frac{\partial\phi}{\partial t}=\left[\frac{(\mathbf{p}-q\mathbf{A})^2}{2m}+q\phi-\frac{q\hbar}{2m}\boldsymbol{\sigma}\cdot\mathbf{B}\right]\phi$$

最后一项 $-\frac{q\hbar}{2m}\boldsymbol{\sigma}\cdot\mathbf{B}$ 是**自旋-磁场耦合**。

### 26.5.3 g=2 的奇迹

自旋磁矩：$\boldsymbol{\mu}=g\frac{q}{2m}\mathbf{S}$。

Dirac 方程预言 $g=2$（精确值！）。实验值 $g_e=2.00231930436256\cdots$

微小的偏差（$g-2\approx 0.00232$）来自**量子电动力学（QED）辐射修正**——虚光子的发射和吸收。QED 对 $g-2$ 的理论计算与实验符合到 $10^{-12}$，是物理学中最精确的预言。

---

## 26.6 氢原子精细结构

### 26.6.1 相对论修正

Dirac 方程对氢原子能级的精确解给出：

$$E_{nj}=mc^2\left[\left(1+\frac{\alpha^2}{(n-\delta_j)^2}\right)^{-1/2}-1\right]$$

其中 $\alpha\approx 1/137$ 是精细结构常数，$\delta_j=j+1/2-\sqrt{(j+1/2)^2-\alpha^2}$。

展开到 $\alpha^4$ 阶：

$$E_{nj}\approx-\frac{13.6\,\text{eV}}{n^2}\left[1+\frac{\alpha^2}{n^2}\left(\frac{n}{j+1/2}-\frac{3}{4}\right)\right]$$

### 26.6.2 三种贡献

精细结构来自三个效应的总和：

1. **相对论动能修正**：$p^2/2m\to\sqrt{p^2c^2+m^2c^4}-mc^2$ 的展开高阶项
2. **自旋-轨道耦合**：$\hat H_{SO}=\frac{1}{2m^2c^2}\frac{1}{r}\frac{dV}{dr}\mathbf{L}\cdot\mathbf{S}$
3. **Darwin项**：$\hat H_D=\frac{\hbar^2}{8m^2c^2}\nabla^2 V$（只影响 s 态）

Dirac 方程统一给出了这三项，不需要分别"加上去"。

### 26.6.3 兰姆位移

1947年，Lamb 和 Retherford 发现 $2s_{1/2}$ 和 $2p_{1/2}$ 能级不完全简并——差了约 1057 MHz。Dirac 方程预言它们应该严格简并。

**兰姆位移**的来源：量子电动力学（QED）的真空涨落——虚电子-正电子对和虚光子修正了库仑势。这是 QED 的关键实验验证之一。

---

## 26.7 从Dirac方程到量子场论

### 26.7.1 单粒子理论的局限

Dirac 方程仍然是单粒子理论，但相对论允许粒子数变化（$E>2mc^2$ 时可以产生粒子-反粒子对）。要自洽地描述相对论性量子现象，必须走向**量子场论**（QFT）。

### 26.7.2 二次量子化

把 Dirac 场 $\psi(\mathbf{x})$ 视为**场算符**（类似谐振子的 $\hat a,\hat a^\dagger$），展开为粒子消灭和反粒子产生算符：

$$\hat\psi(\mathbf{x})=\sum_s\int\frac{d^3p}{(2\pi)^3}\left[\hat b_{\mathbf{p},s}u_s(\mathbf{p})e^{i\mathbf{p}\cdot\mathbf{x}}+\hat d_{\mathbf{p},s}^\dagger v_s(\mathbf{p})e^{-i\mathbf{p}\cdot\mathbf{x}}\right]$$

- $\hat b_{\mathbf{p},s}$：消灭动量 $\mathbf{p}$、自旋 $s$ 的粒子
- $\hat d_{\mathbf{p},s}^\dagger$：产生动量 $\mathbf{p}$、自旋 $s$ 的反粒子

### 26.7.3 QED

量子电动力学（QED）= Dirac 场 + 电磁场的量子化 + 最小耦合。

基本过程：
- 电子发射/吸收光子（顶点 $e\bar\psi\gamma^\mu\psi A_\mu$）
- 电子-正电子湮灭为光子
- 光子产生电子-正电子对

QED 是可重整化的——所有无穷大可以被吸收到质量和电荷的重新定义中。微扰计算用 Feynman 图，精度极高。

---

## 26.8 本章小结

| 概念 | 要点 |
|---|---|
| Klein-Gordon方程 | 相对论性标量场方程，负概率困难 |
| Dirac方程 | 时间一阶，四分量旋量，$g=2$ |
| 反物质 | 负能解→正电子（1932 Anderson 发现） |
| Pauli方程 | Dirac 方程的非相对论极限，自然包含自旋 |
| 精细结构 | 相对论修正 + 自旋-轨道耦合 + Darwin项 |
| 兰姆位移 | QED 真空涨落修正 |
| 量子场论 | 场算符，粒子产生湮灭，QED |

---

> **下一步**：我们已经走到了量子力学的边界——从非相对论到相对论，从单粒子到场论。最后一章，我们回顾量子力学的概念基础，展望它与其他领域的交叉，以及那些仍未解答的问题。

