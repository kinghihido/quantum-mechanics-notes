# 数学前备库 · M01–M56

> 全局工具层：保证任何公式推导看得懂。数学部分只列公式与用途，不写叙述。
> 每条 = 定义要点 + 核心公式 + 用在哪一句。学习路径：先过本库 → 读概论 → 深入模块 → 卡住查公式图谱。

## A · 线性代数（M01–M11）

### M01 · 向量空间与基
线性无关组张成向量空间；基 = 最大线性无关组；维度 = 基的个数。
$$\vec v=\sum_i c_i\vec e_i,\qquad \dim V=n$$
用：态矢空间、任意态按基展开。

### M02 · 内积与正交
内积给出"夹角/投影"，正交 = 内积为零。
$$\langle\varphi|\psi\rangle,\qquad \langle e_i|e_j\rangle=\delta_{ij}$$
用：正交归一基、投影系数 $c_i=\langle e_i|\psi\rangle$。

### M03 · 线性算符与矩阵表示
算符 $\hat A$ 作用在态上，选基后成矩阵。
$$\hat A|e_j\rangle=\sum_i A_{ij}|e_i\rangle,\qquad A_{ij}=\langle e_i|\hat A|e_j\rangle$$
用：可观测量=厄米算符；矩阵元计算。

<details class="sup"><summary>补充</summary>

**算符 = "对态做的操作"**：$\hat A$ 作用在 $|\psi\rangle$ 上得到新态 $\hat A|\psi\rangle$。选好基后，这个操作完全由矩阵 $A_{ij}$ 描述：矩阵元 $A_{ij}=\langle e_i|\hat A|e_j\rangle$ 的意思是"把基矢 $|e_j\rangle$ 送进算符，再看结果在 $|e_i\rangle$ 方向有多少分量"。

**为什么要矩阵**：因为算符是线性的，知道它对每个基矢做了什么，就知道它对所有态做了什么——矩阵就是这份完整说明书。

**量子力学用法**：可观测量（位置、动量、能量）都对应一个厄米算符；算 $A$ 的平均值就是 $\langle\psi|\hat A|\psi\rangle$，把矩阵和态矢量"夹"起来。

</details>

### M04 · 本征方程
$$\hat A|a\rangle=a|a\rangle$$
用：测量结果=本征值；定态方程即能量本征方程。

### M05 · 厄米矩阵：实谱 + 正交完备
$$\hat A^\dagger=\hat A\;\Rightarrow\;a\in\mathbb R,\quad \langle a|a'\rangle=\delta_{aa'}$$
用：可观测量的本征值必为实数、本征态正交完备。

### M06 · 对易子与相容可观测量
$$[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$$
对易 ⇒ 存在共同本征态（可同时确定）；不对易 ⇒ 不确定关系。
用：位置-动量 $[\hat x,\hat p]=i\hbar$；角动量分量。

<details class="sup"><summary>补充</summary>

**对易子衡量"测量顺序是否可交换"**：$[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$。若等于零，先测 $A$ 再测 $B$ 与先测 $B$ 再测 $A$ 结果一致，两个量可以同时确定；若不为零，测一个会扰动另一个。

**类比**：戴帽子再系围巾 ↔ 先系围巾再戴帽子——结果一样（对易）；先穿袜子再穿鞋 ↔ 先穿鞋再穿袜子——完全两样（不对易）。

**最著名的实例**：$[\hat x,\hat p]=i\hbar\neq0$，所以位置与动量不能同时测准，$\Delta x\,\Delta p\ge\hbar/2$（见图谱 F115）。

</details>

### M07 · 幺正变换（换基）
$$\hat U^\dagger\hat U=1\;\Rightarrow\;\langle U\psi|U\varphi\rangle=\langle\psi|\varphi\rangle$$
用：表象变换；时间演化算符 $e^{-i\hat Ht/\hbar}$ 是幺正的。

### M08 · 矩阵迹
$$\operatorname{Tr}A=\sum_i A_{ii},\qquad \operatorname{Tr}(AB)=\operatorname{Tr}(BA)$$
用：不随基变化（$\operatorname{Tr}(UAU^\dagger)=\operatorname{Tr}A$）；密度矩阵 $\operatorname{Tr}\rho=1$。

### M09 · 投影算符与谱分解
$$\hat P_a=|a\rangle\langle a|,\qquad \hat A=\sum_a a\,|a\rangle\langle a|,\qquad \sum_a|a\rangle\langle a|=1$$
用：测量坍缩 $\rho\to\hat P_a\rho\hat P_a/\operatorname{Tr}(\hat P_a\rho)$；算符展开。

<details class="sup"><summary>补充</summary>

**投影算符就是"只保留某个方向的分量"**：$\hat P_a=|a\rangle\langle a|$ 作用在任意态 $|\psi\rangle$ 上，得 $\hat P_a|\psi\rangle=|a\rangle\langle a|\psi\rangle=\langle a|\psi\rangle\,|a\rangle$——把态"拍"到基矢 $|a\rangle$ 上，系数就是投影 $\langle a|\psi\rangle$。

**谱分解**：$\hat A=\sum_a a\,|a\rangle\langle a|$ 意思是"测 $A$ 的结果是各本征值 $a$ 乘以投影"，$\sum_a|a\rangle\langle a|=1$ 表示完备基把空间铺满（任意态都能展开）。

**与测量联系**：测量后态坍缩为 $\hat P_a\rho\hat P_a/\operatorname{Tr}(\hat P_a\rho)$——即"只剩 $|a\rangle$ 分量，再归一化"。

</details>

### M10 · 张量积（多粒子）
$$|\psi\rangle=|\psi_1\rangle\otimes|\psi_2\rangle,\qquad \mathcal H=\mathcal H_1\otimes\mathcal H_2,\quad \dim=\dim_1\dim_2$$
用：多粒子态、纠缠态（不可分解成张量积的态）。

### M11 · 行列式与特征多项式
$$\det(\hat A-\lambda I)=0$$
用：求本征值；多电子波函数（Slater 行列式，交换反对称）。

## B · 微积分（M12–M20）

### M12 · 偏导与链式法则
$$\frac{d}{dt}f(x_1(t),\dots)=\sum_i\frac{\partial f}{\partial x_i}\frac{dx_i}{dt}$$
用：波包运动、算符期望值随时间变化（Ehrenfest）。

### M13 · 分部积分
$$\int_a^b u\,dv=uv\Big|_a^b-\int_a^b v\,du$$
端点消失（$uv|_a^b=0$）时：$\int\psi^*\psi''dx=-\int|\psi'|^2dx$。
用：动能期望、$\langle x^2\rangle$、动量算符的厄米性证明。

<details class="sup"><summary>补充</summary>

**一句话记法**：$\int u\,dv=uv-\int v\,du$——把难积的 $\int u\,dv$ 换成易积的 $\int v\,du$，代价是边界项 $uv|_a^b$。

**什么时候用**：被积函数是两类函数的乘积，其中一类好求导、另一类好积分。量子力学里最常把 $u=\psi^*$（好求导）与 $dv=\psi''dx$（两次积分回到 $\psi$）配对。

**端点消失**：束缚态波函数在无穷远为零，边界项 $uv|_{-\infty}^{+\infty}=0$，于是 $\int\psi^*\psi''dx=-\int|\psi'|^2dx$——把二阶导数"转移"到一阶，动能期望 $\langle T\rangle=\frac{\hbar^2}{2m}\int|\psi'|^2dx$ 就出来了。

</details>

### M14 · 换元积分
$$\int f(g(x))g'(x)\,dx=\int f(u)\,du,\qquad u=g(x)$$
用：化简积分、径向积分 $r^2dr$。

### M15 · 泰勒展开
$$f(x)=\sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(x-a)^n,\qquad V(x)\approx V(x_0)+\tfrac12 V''(x_0)(x-x_0)^2$$
用：势能极小点附近 ≈ 谐振子；波包传播。

### M16 · 欧拉公式与复数
$$e^{i\theta}=\cos\theta+i\sin\theta,\qquad z=|z|e^{i\arg z}$$
用：振荡因子 $e^{-iEt/\hbar}$、$e^{ikx}$；平面波。

### M17 · 高斯积分
$$\int_{-\infty}^{+\infty}e^{-\alpha x^2}dx=\sqrt{\frac{\pi}{\alpha}},\qquad \int_{-\infty}^{+\infty}x^2e^{-\alpha x^2}dx=\frac{\sqrt\pi}{2\alpha^{3/2}}$$
用：高斯波包归一化、谐振子 $\langle x^2\rangle$、动量和位置积分。

<details class="sup"><summary>补充</summary>

**关键结论只有一个**：$e^{-\alpha x^2}$ 从 $-\infty$ 积到 $+\infty$ 等于 $\sqrt{\pi/\alpha}$。

**怎么理解它**：$e^{-\alpha x^2}$ 是一顶钟形帽，$\alpha$ 越大帽子越瘦越高；帽子的总面积恰为 $\sqrt{\pi/\alpha}$。验证数字：$\alpha=1$ 时 $\int_{-\infty}^{+\infty}e^{-x^2}dx=\sqrt\pi\approx1.772$。

**怎么推导（凑平方技巧）**：记 $I=\int_{-\infty}^{+\infty}e^{-\alpha x^2}dx$，则 $I^2=\iint e^{-\alpha(x^2+y^2)}dx\,dy$。换极坐标 $x^2+y^2=r^2,\ dx\,dy=r\,dr\,d\theta$，得 $I^2=2\pi\int_0^\infty e^{-\alpha r^2}r\,dr=2\pi\cdot\frac1{2\alpha}=\frac{\pi}{\alpha}$，故 $I=\sqrt{\pi/\alpha}$。

**第二个积分**：把 $x^2e^{-\alpha x^2}$ 看成对参数求导 $-e^{-\alpha x^2}$ 的导数：$\int x^2e^{-\alpha x^2}dx=-\frac{d}{d\alpha}\sqrt{\pi/\alpha}=\frac{\sqrt\pi}{2\alpha^{3/2}}$。

</details>

### M18 · 反常积分与平方可积
$$\int_{-\infty}^{+\infty}|f(x)|^2dx<\infty$$
用：波函数归一化条件；排除指数增长解。

### M19 · 极值与二阶判据
$f'(x_0)=0$；$f''(x_0)>0$ 极小、$<0$ 极大。
用：变分法最小化能量泛函 $E[\psi]$。

### M20 · 散度定理（三维分部积分）
$$\int_V\nabla\cdot\vec F\,dV=\oint_S\vec F\cdot d\vec S,\qquad \int\nabla f\cdot\nabla g\,dV=-\int f\nabla^2 g\,dV\ (\text{边界项为}0)$$
用：概率守恒推导 $\nabla\cdot\vec j$ 项、动能算符三维形式。

## C · 常微分方程（M21–M26）

### M21 · 一阶 ODE 与分离变量
$$\frac{dy}{dx}=g(x)h(y)\;\Rightarrow\;\int\frac{dy}{h(y)}=\int g(x)dx$$
用：时间演化分离、速率方程。

### M22 · 二阶常系数 ODE
$$y''+k^2y=0\Rightarrow y=A\sin kx+B\cos kx\ (\text{振荡});\qquad y''-\kappa^2y=0\Rightarrow y=Ce^{\kappa x}+De^{-\kappa x}\ (\text{指数})$$
用：允许区振荡/禁区指数——束缚态求解的核心判据。

### M23 · Wronskian 与线性独立
$$W[y_1,y_2]=y_1y_2'-y_2y_1'$$
$W\not\equiv0$ ⇔ 两解线性无关；$W'=0$（对 $y''+fy=0$ 型）⇒ $W\equiv$ 常数。
用：一维束缚态非简并证明。

<details class="sup"><summary>补充</summary>

**Wronskian 是什么**：$W=\psi_1\psi_2'-\psi_2\psi_1'$ 是"两个解有多独立"的判据——若两个波函数成比例（比如 $\psi_2=c\psi_1$），代入得 $W=\psi_1(c\psi_1')-(c\psi_1)\psi_1'=0$；不成比例则 $W\neq0$。

**求导为什么只剩两项**：对 $W$ 求导，每个因子各导一次再相加：$W'=\psi_1'\psi_2'+\psi_1\psi_2''-\psi_2'\psi_1'-\psi_2\psi_1''$。其中 $\psi_1'\psi_2'$ 与 $\psi_2'\psi_1'$ 是同一项，一正一负抵消——所以只剩 $\psi_1\psi_2''-\psi_2\psi_1''$，共两项而非四项。

**它为什么是常数**：把方程改写为 $\psi''=-\frac{2m}{\hbar^2}(E-V)\psi$ 代入，得 $W'=-\frac{2m}{\hbar^2}(E-V)(\psi_1\psi_2-\psi_2\psi_1)=0$。处处导数为零 ⇒ $W$ 恒为常数。

</details>

### M24 · 级数解法（Frobenius）
$$y=\sum_{n=0}^\infty a_nx^n\ (\text{或含 }x^s)\ \text{代入方程逐项定系数}$$
用：谐振子（Hermite）、氢原子（Laguerre）、Bessel 方程的幂级数解。

### M25 · Sturm–Liouville 理论
$$-\frac{d}{dx}\left[p(x)\frac{dy}{dx}\right]+q(x)y=\lambda\rho(x)y$$
本征函数关于权重 $\rho$ 正交且完备。
用：本征函数正交完备性的统一证明（无限深阱、谐振子、球谐函数）。

<details class="sup"><summary>补充</summary>

**它回答"为什么本征函数天然正交完备"**：很多束缚态方程都能写成 $-\frac{d}{dx}[p(x)\frac{dy}{dx}]+q(x)y=\lambda\rho(x)y$ 的标准形式（无限深阱、谐振子、球谐函数都行）。这类方程有一个共同定理：不同本征值对应的本征函数关于权重 $\rho$ 正交，且本征函数族完备。

**正交的意思**：$\int y_n(x)y_m(x)\rho(x)dx=0\ (n\neq m)$。这是"能量不同 ⇒ 态互相垂直"，谱分解、展开法（M29）全都建立在这上面。

**权重 $\rho$ 为什么重要**：不是所有正交都按普通积分算——球谐函数按 $d\Omega=\sin\theta\,d\theta\,d\varphi$ 积分，权重 $\sin\theta$ 就藏在 $\rho$ 里。

</details>

### M26 · 边界值问题 → 离散谱
二阶线性方程 + 两端齐次边界条件 ⇒ 只有分立 $\lambda_n$ 有非零解。
用：能量量子化的数学本质。

## D · 偏微分方程（M27–M29）

### M27 · 分离变量法
$V$ 可分离时 $\psi=X(x)Y(y)Z(z)$，$\hat H\psi=E\psi$ 拆成三个单变量方程，$E=E_x+E_y+E_z$。
用：三维势箱。

### M28 · 三大线性方程类比
扩散：$\partial_t u=\alpha\partial_x^2u$（实系数、耗散）；波动：$\partial_t^2u=c^2\partial_x^2u$；薛定谔：$i\hbar\partial_t\psi=-\frac{\hbar^2}{2m}\partial_x^2\psi$（一阶时间、振荡）。
用：理解薛定谔方程"像什么"——它既有传播性又有振荡性。

### M29 · 本征函数展开
$$f(x)=\sum_n c_n\varphi_n(x),\qquad c_n=\langle\varphi_n|f\rangle=\int\varphi_n^*f\,dx$$
用：任意初态按定态展开、态随时间演化。

## E · 傅里叶与积分变换（M30–M35）

### M30 · 傅里叶级数
$$f(x)=\sum_{n}c_ne^{2\pi inx/L},\qquad c_n=\frac1L\int_0^L f(x)e^{-2\pi inx/L}dx$$
用：周期势、无限深阱完备性、晶体中平面波基。

### M31 · 傅里叶变换与逆变换
$$\tilde f(k)=\int_{-\infty}^{+\infty}f(x)e^{-ikx}dx,\qquad f(x)=\frac1{2\pi}\int\tilde f(k)e^{ikx}dk$$
用：动量空间波函数 $\tilde\psi(k)$；位置-动量是傅里叶共轭对。

### M32 · 狄拉克 δ 函数
$$\delta(x-x_0)=0\,(x\neq x_0),\qquad \int f(x)\delta(x-x_0)dx=f(x_0)$$
用：位置本征态 $\langle x|x'\rangle=\delta(x-x')$；连续谱正交归一。

<details class="sup"><summary>补充</summary>

**δ 函数不是普通函数**：它只在 $x=x_0$ 处"无限高、无限窄、面积恰为 1"。直观图像：一串归一化的窄高斯峰，宽度 $\varepsilon\to0$、高度 $\sim1/\varepsilon$，极限就是 $\delta(x-x_0)$。

**抽样性质是它的全部意义**：$\int f(x)\delta(x-x_0)dx=f(x_0)$——把函数 $f$ 在 $x_0$ 处"抽"出来。所以 $\delta$ 只活在积分号下才有意义。

**在量子力学里的角色**：位置本征态 $\langle x|x'\rangle=\delta(x-x')$；它是"位置钉死在一点"的理想极限，代价是动量完全弥散（见 M31 傅里叶共轭、F115 测不准）。

</details>

### M33 · 卷积定理
$$(f*g)(x)=\int f(x-x')g(x')dx',\qquad \mathcal F\{f*g\}=\tilde f(k)\tilde g(k)$$
用：测量仪器响应、动量传递。

### M34 · 高斯波包与展宽
高斯波包 $\sigma_x\sigma_p=\hbar/2$ 取最小不确定；自由传播中 $\sigma_x(t)=\sigma_x(0)\sqrt{1+(\hbar t/2m\sigma_x^2)^2}$ 展宽。
用：测不准关系的最小态；相干态不展宽的对比对象。

### M35 · 帕塞瓦尔定理
$$\int_{-\infty}^{+\infty}|f(x)|^2dx=\frac1{2\pi}\int_{-\infty}^{+\infty}|\tilde f(k)|^2dk$$
用：归一化在位置/动量空间的等价性；$|\tilde\psi(k)|^2$ 为动量概率密度。

## F · 复变（M36–M38）

### M36 · 复平面与解析函数
$z=x+iy$；$f$ 可导 ⇔ Cauchy–Riemann 条件 $\partial_xu=\partial_yv,\ \partial_xv=-\partial_yu$。
用：时间演化因子 $e^{-iEt/\hbar}$ 的模长恒为 1（幺正、概率守恒）。

### M37 · 留数定理
$$\oint f(z)dz=2\pi i\sum\text{Res}\,f(\text{奇点})$$
用：实轴上困难积分、格林函数、传播子。

### M38 · 行波解与相位
$$\psi(x,t)=Ae^{i(kx-\omega t)},\qquad \lambda=2\pi/k,\ \nu=\omega/2\pi$$
用：平面波、动量-波长关系 $p=\hbar k$、德布罗意波。

## G · 特殊函数（M39–M45）

### M39 · 伽马函数
$$\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}dt,\qquad \Gamma(n+1)=n!,\ \Gamma(1/2)=\sqrt\pi$$
用：径向积分的阶乘推广、$d$ 维态密度。

### M40 · 贝塞尔函数
$$x^2y''+xy'+(x^2-n^2)y=0\Rightarrow y=J_n(x)$$
用：圆柱对称问题（波导、二维圆域振动）。

### M41 · 勒让德多项式
$$\int_{-1}^{1}P_l(x)P_{l'}(x)dx=\frac2{2l+1}\delta_{ll'},\qquad P_l(1)=1$$
用：轴对称角向方程、多极展开。

### M42 · 球谐函数
$$Y_{lm}(\theta,\varphi),\qquad \int Y_{lm}^*Y_{l'm'}d\Omega=\delta_{ll'}\delta_{mm'}$$
用：三维角向本征函数、$\hat L^2$ 与 $\hat L_z$ 共同本征态、氢原子角向。

### M43 · 埃尔米特多项式
$$H_{n+1}=2\xi H_n-2nH_{n-1},\qquad H_n''-2\xi H_n'+2nH_n=0,\qquad \int H_nH_me^{-\xi^2}d\xi\propto\delta_{nm}$$
用：谐振子本征函数 $H_n(\xi)e^{-\xi^2/2}$。

### M44 · 拉盖尔多项式
$$xL_n''+(1-x)L_n'+nL_n=0$$
用：氢原子径向波函数、库仑场束缚态。

### M45 · 正交多项式统一性质
Rodrigues 公式、递推关系、完备性、与权重函数的正交性（Gegenbauer/超几何统一）。
用：一切"级数解被截断成多项式"的束缚态问题（量子化条件来源）。

## H · 概率与统计（M46–M51）

### M46 · 概率密度与归一化
$$\rho(x)\ge0,\qquad\int\rho(x)dx=1$$
用：$|\psi|^2$ 作为概率密度；归一化。

### M47 · 期望 / 方差 / 标准差
$$\langle x\rangle=\int x\rho(x)dx,\qquad \sigma^2=\langle x^2\rangle-\langle x\rangle^2,\ \sigma=\sqrt{\sigma^2}$$
用：位置/动量测量的统计描述、不确定度。

### M48 · 高斯分布
$$\rho(x)=\frac1{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2/2\sigma^2}$$
用：谐振子基态、相干态、测量误差、中心极限的产物。

### M49 · 泊松分布
$$P(n)=\frac{\lambda^n}{n!}e^{-\lambda},\qquad \langle n\rangle=\lambda,\ \sigma=\sqrt\lambda$$
用：相干态的光子数统计、放射性衰变、计数实验。

### M50 · 协方差与相关性
$$\operatorname{Cov}(x,y)=\langle xy\rangle-\langle x\rangle\langle y\rangle$$
用：两个可观测量是否相关；不确定关系的另一种表述 $\sigma_x\sigma_y\ge|\operatorname{Cov}|/2$。

### M51 · 中心极限定理
大量独立同分布变量之和 → 高斯分布（均值为总均值、方差为方差之和）。
用：统计物理中宏观量涨落小；测量误差高斯化。

## I · 数值方法（M52–M56）

### M52 · 欧拉法 / 龙格–库塔
$$y_{n+1}=y_n+hf(x_n,y_n)\ (\text{欧拉});\quad \text{RK4 每步 4 次斜率评估，误差}\ O(h^4)$$
用：打靶法的积分器、任意势阱求波函数。

### M53 · 有限差分
$$\psi''(x_j)\approx\frac{\psi_{j+1}-2\psi_j+\psi_{j-1}}{\Delta^2}$$
用：把薛定谔方程离散成三对角矩阵求本征值（$O(\Delta^2)$ 误差）。

### M54 · 矩阵本征值数值解
幂法（最大本征值）、QR 算法（全部本征值）、Lanczos（稀疏大矩阵）。
用：任何势阱的本征能谱数值计算。

### M55 · 打靶法
从一端积分试探解，扫参数 $E$ 使另一端满足边界条件；本征值处解"翻号"。
用：束缚态本征值扫描（配合节点定理核对）。

<details class="sup"><summary>补充</summary>

**这是数值流程，不是公式**：给定试探能量 $E$，方程 $\psi''=-\frac{2m}{\hbar^2}(E-V)\psi$ 就能从一端一步步积分出 $\psi$（用欧拉法或 RK4，见 M52）。

**打靶的思路**：束缚态要求 $\psi(\pm\infty)\to0$。对试探 $E$：从左边取衰减解出发向右积分——$E$ 偏低时弯曲不够，到右端变成 $+\infty$；$E$ 偏高时弯曲过度，多穿一次轴后变成 $-\infty$；只有 $E$ 恰为本征值时右端恰好衰减到零。像调整炮口角度让炮弹正中靶心，扫参数 $E$ 找到满足边界条件的值。

**配合节点定理**（图谱 F157）：每穿一次轴就多一个节点，可用它核对扫描到的 $E$ 对应第几个能级。

</details>

### M56 · 谱方法
未知函数按完备正交基展开（傅里叶/切比雪夫），微分变成对角运算，指数收敛。
用：高精度求解周期势、波动方程。
