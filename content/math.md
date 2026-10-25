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

<details class="sup"><summary>补充</summary>

**内积要共轭转置，不是转置**：狄拉克记号里，$\langle U\psi|$ 是 $|U\psi\rangle$ 的**共轭转置**（先转置、再逐项取共轭，合称 $\dagger$），不是普通转置。你的推导写 $\langle U\psi|U\varphi\rangle=(U\psi)^*(U\varphi)$，这里的 $^*$ 必须理解为 $\dagger$：$(U\psi)^\dagger=\psi^\dagger U^\dagger$。于是

$$\langle U\psi|U\varphi\rangle=\psi^\dagger U^\dagger U\varphi=\psi^\dagger\varphi=\langle\psi|\varphi\rangle.$$

**为什么必须是共轭转置**：内积要求 $\langle\psi|\psi\rangle\ge0$。若只做转置不做共轭，$\langle\psi|\psi\rangle$ 是"转置后乘自己"，可能为负甚至复数，就配不上"概率"的含义。共轭转置保证对角元素 $\psi^\dagger\psi=\sum_i|\psi_i|^2\ge0$。

**记号规则一句话**：$\langle A\psi|= \langle\psi|A^\dagger$——算符从 ket 侧移到 bra 侧要换成共轭转置。幺正算符的定义 $U^\dagger U=1$ 正是保证"换基后一切内积不变"，所以两个表象是同一物理的不同写法。

</details>

### M08 · 矩阵迹
$$\operatorname{Tr}A=\sum_i A_{ii},\qquad \operatorname{Tr}(AB)=\operatorname{Tr}(BA)$$
用：不随基变化（$\operatorname{Tr}(UAU^\dagger)=\operatorname{Tr}A$）；密度矩阵 $\operatorname{Tr}\rho=1$。

<details class="sup"><summary>补充</summary>

**迹 = 主对角线求和**：$\operatorname{Tr}A=\sum_iA_{ii}$。它最神奇的性质是循环性：$\operatorname{Tr}(AB)=\operatorname{Tr}(BA)$——乘积的迹与你乘的顺序无关（再多几个也一样：$\operatorname{Tr}(ABC)=\operatorname{Tr}(BCA)=\operatorname{Tr}(CAB)$）。

**为什么成立（求和指标重排）**：
$$\operatorname{Tr}(AB)=\sum_i(AB)_{ii}=\sum_i\sum_j A_{ij}B_{ji}=\sum_j\sum_i B_{ji}A_{ij}=\sum_j(BA)_{jj}=\operatorname{Tr}(BA).$$
把 $\sum_i\sum_j$ 交换顺序，就完成了"重排后完全相同"——你在笔记里写的就是这一步。

**密度矩阵是什么**：体系处于混合态（不是确定的一个态，而是以概率 $p_i$ 处于各态 $|\psi_i\rangle$）时，用一个算符统一描述：
$$\rho=\sum_i p_i\,|\psi_i\rangle\langle\psi_i|,\qquad 0\le p_i\le1,\ \sum_i p_i=1.$$
它把"概率"和"态"打包在一起。**为什么 $\operatorname{Tr}\rho=1$**：$\operatorname{Tr}(|\psi_i\rangle\langle\psi_i|)=\langle\psi_i|\psi_i\rangle=1$（迹中内外积可交换循环），所以 $\operatorname{Tr}\rho=\sum_ip_i\cdot1=1$——这就是"总概率归一"在算符语言里的样子。纯态（$p_i=1$ 只有一个）对应 $\rho^2=\rho$。

</details>

### M09 · 投影算符与谱分解
$$\hat P_a=|a\rangle\langle a|,\qquad \hat A=\sum_a a\,|a\rangle\langle a|,\qquad \sum_a|a\rangle\langle a|=1$$
用：测量坍缩 $\rho\to\hat P_a\rho\hat P_a/\operatorname{Tr}(\hat P_a\rho)$；算符展开。

<details class="sup"><summary>补充</summary>

**投影算符就是"只保留某个方向的分量"**：$\hat P_a=|a\rangle\langle a|$ 作用在任意态 $|\psi\rangle$ 上，得 $\hat P_a|\psi\rangle=|a\rangle\langle a|\psi\rangle=\langle a|\psi\rangle\,|a\rangle$——把态"拍"到基矢 $|a\rangle$ 上，系数就是投影 $\langle a|\psi\rangle$。

**"内积是数，所以可以提前"——对的**：$\langle a|\psi\rangle$ 是一个复数（不是态），乘在 $|a\rangle$ 左边或右边都一样，所以 $|a\rangle\langle a|\psi\rangle\equiv\langle a|\psi\rangle\,|a\rangle$。这就是"外积作用在态上 = 投影系数 × 基矢"。

**谱分解**：$\hat A=\sum_a a\,|a\rangle\langle a|$ 意思是"测 $A$ 的结果是各本征值 $a$ 乘以投影"，$\sum_a|a\rangle\langle a|=1$ 表示完备基把空间铺满（任意态都能展开）。

**记号澄清（你问的 α 冲突）**：$|a\rangle$ 里的 $a$ 是**标签/量子数**（用来指认是哪一个本征态，就像给抽屉贴编号），外面的 $a$ 是**本征值**（那个抽屉里装的数值）。它们恰好同名，所以容易混。标准记号喜欢用 $|a\rangle$ 配本征值 $a$：$a$ 是数字，$|a\rangle$ 是态。你用 $\alpha$ 同时标两处时，最好区分成 $|\alpha\rangle$（态）与本征值 $\lambda_\alpha$ 或 $a_\alpha$（数）。

**与测量联系**：测量后态坍缩为 $\hat P_a\rho\hat P_a/\operatorname{Tr}(\hat P_a\rho)$——即"只剩 $|a\rangle$ 分量，再归一化"。

</details>

### M10 · 张量积（多粒子）
$$|\psi\rangle=|\psi_1\rangle\otimes|\psi_2\rangle,\qquad \mathcal H=\mathcal H_1\otimes\mathcal H_2,\quad \dim=\dim_1\dim_2$$
用：多粒子态、纠缠态（不可分解成张量积的态）。

<details class="sup"><summary>补充</summary>

**三个符号逐个说**：
- $\otimes$（张量积）：把两个独立体系的态"拼在一起"的运算。粒子 1 在态 $|\psi_1\rangle$、粒子 2 在态 $|\psi_2\rangle$，整体就是 $|\psi_1\rangle\otimes|\psi_2\rangle$（常省略写 $|\psi_1\rangle|\psi_2\rangle$）。
- $\mathcal H$（希尔伯特空间）：所有可能态的集合，量子力学的"态空间"——每个态是空间里一个矢量。单个粒子有 $\mathcal H_1$，两个粒子整体有 $\mathcal H$。
- $\dim$（维度）：空间里线性无关基矢的个数。

**维度为什么相乘**：粒子 1 有 $\dim_1$ 个独立基矢 $|e_i\rangle$，粒子 2 有 $\dim_2$ 个 $|f_j\rangle$。整体的基矢是全部组合 $|e_i\rangle\otimes|f_j\rangle$，共 $\dim_1\times\dim_2$ 个。例：两个自旋 $\tfrac12$ 粒子（各自 $\dim=2$），整体 $\dim=4$，基矢是 $|\uparrow\uparrow\rangle,|\uparrow\downarrow\rangle,|\downarrow\uparrow\rangle,|\downarrow\downarrow\rangle$。

**为什么纠缠态特殊**：有些整体态能写成"粒子 1 态 × 粒子 2 态"（可分解），有些不能——比如 $\tfrac1{\sqrt2}(|\uparrow\downarrow\rangle+|\downarrow\uparrow\rangle)$ 拆不成任何单个粒子态的乘积，这叫纠缠态，量子信息学的资源。

</details>

### M11 · 行列式与特征多项式
$$\det(\hat A-\lambda I)=0$$
用：求本征值；多电子波函数（Slater 行列式，交换反对称）。

<details class="sup"><summary>补充</summary>

**它是怎么来的（你猜对了，正是 $A\alpha=\lambda\alpha$ 的求解片段）**：本征方程 $\hat A|\alpha\rangle=\lambda|\alpha\rangle$ 移项得 $(\hat A-\lambda I)|\alpha\rangle=0$。这是一个齐次线性方程组。**有非零解的充要条件是系数矩阵不可逆，即行列式为零**：

$$\det(\hat A-\lambda I)=0.$$

**几何直觉**：$(\hat A-\lambda I)$ 把某个方向"压扁"成零（那个方向就是本征矢 $\alpha$）——一个把矢量压扁的变换，体积缩放因子（行列式）必为 0。

**实操**：$\det(\hat A-\lambda I)=0$ 展开后是关于 $\lambda$ 的 $n$ 次多项式（$n\times n$ 矩阵），$n$ 个根就是 $n$ 个本征值；每个根代回 $(\hat A-\lambda I)\alpha=0$ 解出对应本征矢。例：$\hat A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$，$\det=\lambda^2-4\lambda+3=0\Rightarrow\lambda=1,3$。

</details>

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

**分部积分路径（你推的那条也对）**：令 $u=x,\ dv=xe^{-\alpha x^2}dx$，则 $v=-\frac1{2\alpha}e^{-\alpha x^2}$：
$$\int x^2e^{-\alpha x^2}dx=\Big[-\frac{x}{2\alpha}e^{-\alpha x^2}\Big]_{-\infty}^{+\infty}+\frac1{2\alpha}\int_{-\infty}^{+\infty}e^{-\alpha x^2}dx=0+\frac{\sqrt\pi}{2\alpha^{3/2}}.$$
两种路径殊途同归；换元与分部都可行。

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

<details class="sup"><summary>补充</summary>

**$\nabla$ 是什么**：读作"nabla"，是一个"把导数打包的符号"：$\nabla=\big(\frac{\partial}{\partial x},\frac{\partial}{\partial y},\frac{\partial}{\partial z}\big)$。它有三种用法：
- 作用在标量 $f$ 上得梯度 $\nabla f$（指向 $f$ 上升最快方向的矢量）；
- 与矢量 $\vec F$ 点乘得散度 $\nabla\cdot\vec F=\frac{\partial F_x}{\partial x}+\frac{\partial F_y}{\partial y}+\frac{\partial F_z}{\partial z}$（衡量"源往外冒的速率"）；
- 与 $\vec F$ 叉乘得旋度（衡量涡旋）。

**散度定理 = 高斯公式，就是同一个东西**：左边把 $\nabla\cdot\vec F$ 在整个体积内加起来，右边是穿过边界曲面的通量。一句话：**体内"冒出来的总量"等于"从边界流出去的总量"**——净流量守恒。

**为什么成立（推导思路，切小方块再求和）**：把体积切成许多小立方体。对第 $i$ 个小立方体，$\nabla\cdot\vec F\,\Delta V$ 恰等于从它六个面流出的通量（泰勒展开一阶项即得，误差 $O(\Delta x^2)$）。把所有小立方体加起来：相邻面的通量互相抵消（一个面流出 = 邻面流入），只剩最外层边界的通量。令切分无限细，求和变积分，即得 $\int_V\nabla\cdot\vec F\,dV=\oint_S\vec F\cdot d\vec S$。

**三维分部积分**：把 $\nabla\cdot(f\nabla g)=\nabla f\cdot\nabla g+f\nabla^2g$（乘法法则）两边积分，左边用散度定理变成边界项；波函数在无穷远为零故边界项消失，得 $\int\nabla f\cdot\nabla g\,dV=-\int f\nabla^2g\,dV$——这是概率流、动能算符推导的关键一步。

</details>

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

**三个字母 p、q、ρ 逐个说（你问的）**：
- $p(x)$：一阶导数前面的系数，决定"弹性/刚度"分布。对最朴素的方程 $y''=\lambda y$（无限深阱内），$p(x)\equiv1$。
- $q(x)$：零阶项系数，相当于"势"或"基底刚度"。无限深阱 $q\equiv0$；若写成 $y''+k^2y=0$ 形式，把 $k^2$ 挪到右边就是 $\lambda$。
- $\rho(x)$：**权重函数**，正交积分时乘在中间：$\int y_n y_m\rho\,dx=\delta_{nm}$。它告诉"正交该按什么测度积分"。均匀问题 $\rho=1$；球谐函数按 $d\Omega=\sin\theta\,d\theta\,d\varphi$ 积分，权重 $\sin\theta$ 就藏在 $\rho$ 里。

**对照例子**（帮你对号入座）：

| 问题 | p | q | ρ |
|---|---|---|---|
| 无限深阱 $\psi''=-k^2\psi$ | 1 | 0 | 1 |
| 谐振子（无量纲）$\psi''=(\xi^2-\epsilon)\psi$ | 1 | $-\xi^2$ | 1 |
| 球谐角向（勒让德） | $1-x^2$ | 0 | 1 |
| 球谐（连带勒让德/按 dΩ） | $1-x^2$ | $-\frac{m^2}{1-x^2}$ | 1 |

**正交的意思**：$\int y_n(x)y_m(x)\rho(x)dx=0\ (n\neq m)$。这是"能量不同 ⇒ 态互相垂直"，谱分解、展开法（M29）全都建立在这上面。

</details>

### M26 · 边界值问题 → 离散谱
二阶线性方程 + 两端齐次边界条件 ⇒ 只有分立 $\lambda_n$ 有非零解。
用：能量量子化的数学本质。

<details class="sup"><summary>补充</summary>

**为什么"一笔带过"不行，这里补上推理链**：

**第一步：方程有多少自由度**。二阶线性常微分方程有两个线性无关解 $y_1,y_2$（比如 $\sin kx,\cos kx$），通解 $y=Ay_1+By_2$——$A,B$ 两个待定常数。

**第二步：两端边界各扣掉一个自由度**。左端齐次边界（如 $y(0)=0$）给出 $A,B$ 的一个线性关系，右端齐次边界（如 $y(L)=0$）再给一个。两个方程约束两个未知数，看似有唯一解——但注意解 $y\equiv0$ 永远满足，真正的问题是"除零解外还有没有非零解"。

**第三步：只有特殊 λ 才留得下非零解**。$y_1,y_2$ 的形状由方程里的 $\lambda$ 决定。要求 $y$ 同时穿过两端边界（$y(0)=y(L)=0$），等于要求 $y_1,y_2$ 的某种组合在两端恰好成比例——这只对离散的 $\lambda_n$ 成立。

**具体看无限深阱**：阱内 $\psi''=-k^2\psi$，$k^2=2mE/\hbar^2$。$\psi(0)=0$ 干掉 $\cos$ 项，剩 $\psi=A\sin kx$；$\psi(L)=0$ 要求 $\sin kL=0\Rightarrow kL=n\pi$。于是 $k$ 被钉死成 $k_n=n\pi/L$，能量只能取 $E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}$——**连续变化的 $E$ 被边界条件筛成一份一份的**，这就是"量子化"的数学本质。不满足 $kL=n\pi$ 的 $E$ 对应的解在右端非零，不是物理允许的束缚态。

</details>

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

<details class="sup"><summary>补充</summary>

**它从傅里叶级数"极限"而来（你说得对，先补怎么变换法）**：

周期 $L$ 的函数可展成级数 $f(x)=\sum_n c_n e^{2\pi inx/L}$，其中 $c_n=\frac1L\int_0^L f(x)e^{-2\pi inx/L}dx$——频率只能取 $k_n=2\pi n/L$ 这一排分立值。

把周期拉长 $L\to\infty$：频率间隔 $\Delta k=2\pi/L\to0$，分立频率 $k_n$ 糊成连续变量 $k$；求和 $\sum_n(\cdots)$ 按 $\Delta k$ 换成积分 $\int(\cdots)\frac{dk}{2\pi/L}$；系数 $c_n$ 乘上 $L$ 变成 $\tilde f(k)$。极限结果就是变换对：

$$\tilde f(k)=\int_{-\infty}^{+\infty}f(x)e^{-ikx}dx,\qquad f(x)=\frac1{2\pi}\int_{-\infty}^{+\infty}\tilde f(k)e^{ikx}dk.$$

**怎么理解"变换-逆变换互相恢复"**：$\tilde f(k)$ 量度 $f$ 里"频率为 $k$ 的成分有多少"（类比：调色板里每种颜色的量）。逆变换把所有频率成分 $e^{ikx}$ 按权重 $\tilde f(k)$ 叠加回去，还原出 $f(x)$——正变换是"拆开"，逆变换是"拼回"。

**量子力学落点**：位置波函数 $\psi(x)$ 与动量波函数 $\tilde\psi(p)$ 正是傅里叶共轭对（$k=p/\hbar$）。"位置确定的态"含所有动量成分（$\delta$ 函数变换成常数），"动量确定的态"位置完全弥散——测不准关系的根源。

</details>

### M32 · 狄拉克 δ 函数
$$\delta(x-x_0)=0\,(x\neq x_0),\qquad \int f(x)\delta(x-x_0)dx=f(x_0)$$
用：位置本征态 $\langle x|x'\rangle=\delta(x-x')$；连续谱正交归一。

<details class="sup"><summary>补充</summary>

**δ 函数不是普通函数**：它只在 $x=x_0$ 处"无限高、无限窄、面积恰为 1"。直观图像：一串归一化的窄高斯峰，宽度 $\varepsilon\to0$、高度 $\sim1/\varepsilon$，极限就是 $\delta(x-x_0)$。

**"一点处有值，积分怎么积出来"——你的困惑核心**：积分不是真的只取那一个点，而是取"窄峰 × f(x) 的乘积再求和"。看窄高斯近似：

$$\int f(x)\,\delta_\varepsilon(x-x_0)\,dx=\int f(x)\cdot\frac{1}{\sqrt{2\pi}\varepsilon}e^{-(x-x_0)^2/2\varepsilon^2}dx.$$

峰宽 $\varepsilon$ 极小，$f(x)$ 在峰内几乎不变，可提出 $f(x_0)$：上式 $\approx f(x_0)\int\delta_\varepsilon(x-x_0)\,dx=f(x_0)\cdot1$。$\varepsilon\to0$ 的极限就是 $\int f(x)\delta(x-x_0)dx=f(x_0)$。**它不是"只取一点的函数值"，而是"宽度趋于零的归一化峰扫过 f 时，只留下 f 在峰心处的值"**——抽样性质由此而来。

**在量子力学里的角色**：位置本征态 $\langle x|x'\rangle=\delta(x-x')$；它是"位置钉死在一点"的理想极限，代价是动量完全弥散（见 M31 傅里叶共轭、F115 测不准）。

</details>

### M33 · 卷积定理
$$(f*g)(x)=\int f(x-x')g(x')dx',\qquad \mathcal F\{f*g\}=\tilde f(k)\tilde g(k)$$
用：测量仪器响应、动量传递。

<details class="sup"><summary>补充</summary>

**"*" 是卷积符号，不是乘法**：$(f*g)(x)$ 读作"f 卷积 g 在 x 处的值"，是两个函数"互相重叠的加权和"，与普通乘积完全是两回事。公式里 $f(x-x')g(x')$ 对 $x'$ 积分——**把 f 反转后平移 x，与 g 逐点相乘再求和（滑动的重叠面积）**。

**直观三步（画面感）**：
1. 把 $f$ 沿横轴反转（$f(x-x')$ 里负号的作用）；
2. 把反转后的 $f$ 平移 $x$；
3. 与 $g$ 逐点相乘、求和 = 重叠面积。

$x$ 从 $-\infty$ 滑到 $+\infty$，得到一条新曲线 $(f*g)(x)$。例：两个矩形脉冲卷积 = 梯形；高斯卷积高斯仍是高斯（宽度平方相加）。

**为什么物理里到处都是它**：任何"仪器响应"都是真实信号被仪器模糊化的过程——输出 = 输入 × 仪器响应函数的卷积。量子力学里，动量不确定度、测量分辨率都长这样。

**卷积定理为什么有用**：傅里叶变换把卷积变成普通乘法 $\mathcal F\{f*g\}=\tilde f\,\tilde g$——时域里做"重叠积分"太麻烦，换到频域只需乘一乘，再变回来。这是信号处理、衍射理论的看家本领。

</details>

### M34 · 高斯波包与展宽
高斯波包 $\sigma_x\sigma_p=\hbar/2$ 取最小不确定；自由传播中 $\sigma_x(t)=\sigma_x(0)\sqrt{1+(\hbar t/2m\sigma_x^2)^2}$ 展宽。
用：测不准关系的最小态；相干态不展宽的对比对象。

<details class="sup"><summary>补充</summary>

**它是什么（画面）**：一个"高斯信封 × 载波"的波包——位置概率是高斯分布（**这就是 M48 高斯分布，两处合并理解**：M48 给概率形状，M34 给它加上相位/动量），叠加不同动量成分的平面波 $e^{ikx}$ 而成（M31 傅里叶变换视角）。$\sigma_x$ 越小，动量分布 $\sigma_p$ 越大，乘积恒为 $\hbar/2$——**它是测不准关系取等号的最小不确定态**。

**为什么恰好最小不确定**：高斯是"同时最集中的函数"——数学上唯一使 Heisenberg 不等式取等号的波函数形状。数字例：$\sigma_x=1\,\text{nm}$ 的电子波包，$\sigma_p=\hbar/2\sigma_x\approx5.3\times10^{-26}\,\text{kg·m/s}$，对应动量弥散 $\Delta v=\sigma_p/m_e\approx58\,\text{m/s}$。

**自由传播为什么展宽**：不同动量成分速度不同（$v=\hbar k/m$），快的跑前面、慢的落后面，波包被"拉长"。公式
$$\sigma_x(t)=\sigma_x(0)\sqrt{1+\Big(\frac{\hbar t}{2m\sigma_x^2}\Big)^2}$$
括号里是"展宽时间尺度"：**质量越小、初包越窄，展得越快**。数字例：$\sigma_x(0)=0.1\,\text{nm}$ 的电子，$\frac{\hbar}{2m\sigma_x^2}\approx\frac{1.05\times10^{-34}}{2\times9.1\times10^{-31}\times10^{-20}}\approx5.8\times10^{15}\,\text{s}^{-1}$，即约 $2\times10^{-16}\,\text{s}$ 后宽度翻倍——微观粒子波包极速弥散。

**与相干态的对比**：谐振子中高斯相干态在势阱里来回振荡却不展宽（能级等间距，各成分相位同步，见图谱 F186）——材料物理里激光、声子相干态都靠它。

</details>

### M35 · 帕塞瓦尔定理
$$\int_{-\infty}^{+\infty}|f(x)|^2dx=\frac1{2\pi}\int_{-\infty}^{+\infty}|\tilde f(k)|^2dk$$
用：归一化在位置/动量空间的等价性；$|\tilde\psi(k)|^2$ 为动量概率密度。

<details class="sup"><summary>补充</summary>

**一句话**：能量（概率）守恒——函数 $f$ 的"总量"在位置空间和频率空间里一样多。$|f(x)|^2$ 沿 $x$ 积分，等于 $|\tilde f(k)|^2$ 沿 $k$ 积分（差一个 $1/2\pi$ 的约定因子）。

**怎么推出来（利用 δ 函数的抽样性质）**：把 $f(x)$ 用逆变换展开代入左边：

$$\int|f(x)|^2dx=\int f^*(x)f(x)\,dx=\frac1{2\pi}\int\!\!\!\int \tilde f^*(k')\tilde f(k)\Big[\frac1{2\pi}\int e^{i(k-k')x}dx\Big]dk\,dk'.$$

中括号里的 $\frac1{2\pi}\int e^{i(k-k')x}dx=\delta(k-k')$（M32 连续谱正交归一），δ 函数把 $k'$ 钉死成 $k$，二重积分塌缩成单重：

$$\int|f(x)|^2dx=\frac1{2\pi}\int|\tilde f(k)|^2dk.$$

**量子力学落点**：波函数归一化 $\int|\psi(x)|^2dx=1$ 等价于 $\frac1{2\pi}\int|\tilde\psi(k)|^2dk=1$，即 $|\tilde\psi(k)|^2/(2\pi)$ 是动量概率密度（$k=p/\hbar$ 换成 $p$ 后无 $2\pi$ 因子）。位置归一好了，动量自动归一——一体两面。

</details>

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
> 与 M34 高斯波包**合并理解**：M48 给出概率密度的形状（均值 $\mu$、标准差 $\sigma$，$\mu\pm\sigma$ 区间约 68% 概率），M34 给它加上动量/相位结构构成波包。谐振子基态 $\psi_0\propto e^{-x^2/2x_0^2}$ 正是高斯（$\mu=0,\ \sigma=x_0/\sqrt2$）；相干态的光子数分布则是泊松（M49）。

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

**具体例子（谐振子，数字走一遍）**：方程 $\psi''=-\frac{2m}{\hbar^2}(E-\tfrac12m\omega^2x^2)\psi$，无量纲化后 $\psi''=(\xi^2-\epsilon)\psi$，$\epsilon=2E/\hbar\omega$。真本征值是 $\epsilon=1,3,5,\dots$（即 $E_n=(n+\tfrac12)\hbar\omega$）。
- 试探 $\epsilon=0.8$（偏低）：从 $\xi=-5$ 取衰减解向右积分，弯曲不足，到 $\xi=+5$ 时 $\psi\to+\infty$（发散到正）；
- 试探 $\epsilon=1.2$（偏高）：弯曲过度，多穿一次轴，到 $\xi=+5$ 时 $\psi\to-\infty$；
- 二分法在 0.8 与 1.2 之间反复扫：$\epsilon=1.0$ 附近右端发散的符号恰好翻转，翻号点就是本征值——**"本征值处解翻号"就是这个意思**，配合节点定理（每穿一次轴多一个节点）核对能级序号。

**配合节点定理**（图谱 F157）：每穿一次轴就多一个节点，可用它核对扫描到的 $E$ 对应第几个能级。

</details>

### M56 · 谱方法
未知函数按完备正交基展开（傅里叶/切比雪夫），微分变成对角运算，指数收敛。
用：高精度求解周期势、波动方程。
