# Ehrenfest 定理与对易子

> 最后更新：2026-10-21
> 所属课程：《材料中的量子与统计》
> 来源：课后讲授（类比引入 → 公式阐述 → E1–E3 练手），承接笔记 07"内积守恒族"

---

## 一、类比引入

**画面**：电子是一团"概率云"，不是小点。云的重心就是期望值 $\langle x\rangle$。这团云在势能地形（如谐振子的"碗" $V=\frac12m\omega^2x^2$）上滑行。Ehrenfest 定理说：**云重心的运动规律 ≈ 经典牛顿力学**。

**数字锚点**：电子 $m_e=9.1\times10^{-31}\,\text{kg}$，原子尺度谐振子 $\omega\approx10^{15}\,\text{rad/s}$，经典小球振荡周期 $T=2\pi/\omega\approx6\times10^{-15}\,\text{s}$；量子云重心振荡周期**完全相同**。

**成立前提**：云足够窄（波包宽度 ≪ 势能变化尺度），或势能变化平缓；势能突变处失效。

---

## 二、定理与推导

$$\boxed{\ \frac{d\langle A\rangle}{dt}=\frac{i}{\hbar}\big\langle[\hat H,\hat A]\big\rangle+\left\langle\frac{\partial\hat A}{\partial t}\right\rangle\ }\qquad [\hat H,\hat A]\equiv\hat H\hat A-\hat A\hat H$$

**推导**（复用笔记 07 的四步法）：

1. 对 $t$ 求导，展开成**三项**：$\partial_t\psi^*$、$\partial_t\hat A$、$\partial_t\psi$
2. 薛定谔方程代入 $\partial_t\psi=\hat H\psi/(i\hbar)$、$\partial_t\psi^*=\hat H\psi^*/(-i\hbar)$
3. 厄米性合并 → 对易子

$$\frac{d\langle A\rangle}{dt}=\frac{1}{i\hbar}\left[\langle\hat A\hat H\rangle-\langle\hat H\hat A\rangle\right]+\left\langle\frac{\partial\hat A}{\partial t}\right\rangle=\frac{i}{\hbar}\big\langle[\hat H,\hat A]\big\rangle+\left\langle\frac{\partial\hat A}{\partial t}\right\rangle$$

**逐符号**：
- $\langle A\rangle=\int\psi^*\hat A\psi\,d^3x$：期望值；
- $[\hat H,\hat A]=\hat H\hat A-\hat A\hat H$：**对易子**，度量"先做 $\hat H$ 再做 $\hat A$"与反过来的差；量纲 = 能量 × $A$；
- $i/\hbar$：系数，凑出 $1/\text{时间}$ 量纲（$\hbar$ = 能量 × 时间）；
- $\langle\partial\hat A/\partial t\rangle$：$\hat A$ **显含时间**的部分（如含时外场）；薛定谔绘景中 $\hat x$、$\hat p$ 不显含 $t$ ⇒ 此项为 0（算符是固定模具，演化全在波函数上）。

---

## 三、特例与经典对应

| $\hat A$ | 用到的对易子 | 结果 |
|---|---|---|
| $\hat x$ | $[\hat H,\hat x]=-i\hbar\hat p/m$ | $d\langle x\rangle/dt=\langle p\rangle/m$ |
| $\hat p$ | $[\hat H,\hat p]=[\hat V,\hat p]=i\hbar\,dV/dx$ | $d\langle p\rangle/dt=-\langle dV/dx\rangle$ |

合并 → **量子版牛顿第二定律**：$m\dfrac{d^2\langle x\rangle}{dt^2}=-\left\langle\dfrac{dV}{dx}\right\rangle$。

**经典极限**：窄波包/势能缓变 ⇒ $\langle dV/dx\rangle\approx dV(\langle x\rangle)/dx$，严格回到 $m\ddot x=-V'(x)$；**势能突变处失效**。

**守恒量统一**：$\hat A$ 不显含 $t$ 且 $[\hat H,\hat A]=0$ ⇒ $d\langle A\rangle/dt=0$。例：能量（$[\hat H,\hat H]=0$）、自由粒子动量。

---

## 四、练手（E1–E3）与批改要点

**E1 能量守恒**：$[\hat H,\hat H]=0$、$\partial\hat H/\partial t=0$ ⇒ $d\langle H\rangle/dt=0$。✅

**E2 自由粒子**（$\hat H=\hat p^2/2m$）：
- $[\hat p^2,\hat x]=\hat p[\hat p,\hat x]+[\hat p,\hat x]\hat p=-2i\hbar\hat p$ ⇒ $[\hat H,\hat x]=-i\hbar\hat p/m$ ⇒ $d\langle x\rangle/dt=\langle p\rangle/m$
- $[\hat H,\hat p]=0$ ⇒ 动量守恒，$\langle x\rangle$ 匀速运动 ✅

**E3 谐振子**（$V=\frac12m\omega^2x^2$）：
- $[\hat H,\hat p]=[\hat V,\hat p]=\frac12m\omega^2[\hat x^2,\hat p]=\frac12m\omega^2(\hat x[\hat x,\hat p]+[\hat x,\hat p]\hat x)=i\hbar m\omega^2\hat x$
- $d\langle p\rangle/dt=(i/\hbar)\langle[\hat H,\hat p]\rangle=-m\omega^2\langle x\rangle$
- 合并 $d\langle x\rangle/dt=\langle p\rangle/m$ ⇒ $d^2\langle x\rangle/dt^2=-\omega^2\langle x\rangle$（经典谐振子方程）✅

---

## 五、易错点（本关踩过的坑）

| 坑 | 原因 | 正确做法 |
|---|---|---|
| 对易子展开**漏项** | 只写 $[\hat p,\hat x]\hat p$，漏 $\hat p[\hat p,\hat x]$ | $[AB,C]=A[B,C]+[A,C]B$ 两项都写；$[\hat p,\hat x]=-i\hbar$ 是 c-数，两项各 $=-i\hbar\hat p$，合起来 $-2i\hbar\hat p$（因子 2 藏在漏项里） |
| $[\hat H,\hat p]$ 结果乱写 | 把代入 $(i/\hbar)$ 的步骤提前合并 | 结果保留 $i\hbar$：$[\hat H,\hat p]=i\hbar m\omega^2\hat x$；负号由 $(i/\hbar)\times(i\hbar)=-1$ 产生 |
| **对象接错** | 把 $[\hat H,\hat p]$ 接进 $d\langle x\rangle/dt$ | $[\hat H,\hat p]$ 进 $d\langle p\rangle/dt$；$[\hat H,\hat x]$ 进 $d\langle x\rangle/dt$ |
| 记号丢三落四 | 笔误 | $d^2/dt^2$ 分母平方；期望值括号 $\langle\cdot\rangle$ 不丢；$\hat p$、$\hat x$ 不丢 |
| 以为 $\langle\partial\hat x/\partial t\rangle\neq0$ | 混淆"算符显含时间"与"期望值变化" | 薛定谔绘景：算符固定、波函数演化；$\partial\hat x/\partial t=0$ 但 $d\langle x\rangle/dt$ 可以非零（波函数在变） |

---

## 六、延伸 / 关联

- **[07-厄米性与内积守恒族证明](./07-厄米性与内积守恒族证明.md)**：四步法武器来源；
- **笔记 02**：$[\hat x,\hat p]=i\hbar\Rightarrow\Delta x\Delta p\ge\hbar/2$（测不准原理）——对易子的直接物理后果；
- **笔记 03**：谐振子 $E_n=(n+\frac12)\hbar\omega$；相干态（第 8 讲）；
- **下一站候选**：定态展开与完备性、一维势阱问题。
