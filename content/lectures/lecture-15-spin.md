# 第15章 自旋与Zeeman效应

> **本章导读**：自旋是量子力学特有的内禀角动量，没有经典对应。电子的自旋为1/2，只有两个可能的取向（"上"和"下"）。自旋的发现源于Stern-Gerlach实验和原子光谱的精细结构。自旋在磁场中会产生Zeeman分裂，这是理解原子光谱、磁共振、自旋电子学的基础。

---

## 15.1 Stern-Gerlach实验

### 15.1.1 实验装置

1922年，Stern和Gerlach做了以下实验：

1. 银原子束从炉中射出
2. 通过非均匀磁场
3. 在后面的屏幕上记录原子沉积的位置

### 15.1.2 经典预言

银原子有磁矩 $\vec{\mu}$。在非均匀磁场 $\vec{B}$ 中，受力为：

$$\vec{F} = \nabla(\vec{\mu} \cdot \vec{B})$$

如果磁矩取向是连续的（经典预言），屏幕上应该看到连续的沉积带。

### 15.1.3 实验结果

屏幕上出现了**两条分离的沉积线**，对应磁矩的两个离散取向。

这表明：
1. 角动量是量子化的
2. 银原子（基态 $l = 0$）有"内禀"角动量，不是轨道角动量

这个内禀角动量就是**自旋**。

---

## 15.2 自旋的基本性质

### 15.2.1 自旋量子数

电子的自旋量子数 $s = 1/2$。

自旋z分量 $S_z$ 的本征值为 $m_s\hbar$，其中 $m_s = \pm 1/2$。

**自旋态**：
- $|s, m_s\rangle = |1/2, +1/2\rangle \equiv |\uparrow\rangle$（自旋向上）
- $|s, m_s\rangle = |1/2, -1/2\rangle \equiv |\downarrow\rangle$（自旋向下）

### 15.2.2 自旋算符

自旋算符 $\hat{\vec{S}} = (\hat{S}_x, \hat{S}_y, \hat{S}_z)$ 满足角动量对易关系：

$$[\hat{S}_i, \hat{S}_j] = i\hbar\epsilon_{ijk}\hat{S}_k$$

$$\hat{S}^2|s, m_s\rangle = s(s+1)\hbar^2|s, m_s\rangle = \frac{3}{4}\hbar^2|s, m_s\rangle$$

$$\hat{S}_z|s, m_s\rangle = m_s\hbar|s, m_s\rangle = \pm\frac{\hbar}{2}|s, m_s\rangle$$

### 15.2.3 泡利矩阵

在 $|\uparrow\rangle, |\downarrow\rangle$ 基中，自旋算符表示为：

$$\hat{S}_x = \frac{\hbar}{2}\sigma_x = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

$$\hat{S}_y = \frac{\hbar}{2}\sigma_y = \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$$

$$\hat{S}_z = \frac{\hbar}{2}\sigma_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

其中 $\sigma_x, \sigma_y, \sigma_z$ 是**泡利矩阵**。

### 15.2.4 泡利矩阵的性质

**厄米性**：$\sigma_i^\dagger = \sigma_i$

**正性**：$\sigma_i^2 = I$

**对易关系**：

$$[\sigma_x, \sigma_y] = 2i\sigma_z$$

$$[\sigma_y, \sigma_z] = 2i\sigma_x$$

$$[\sigma_z, \sigma_x] = 2i\sigma_y$$

**反对易关系**：

$$\{\sigma_i, \sigma_j\} = 2\delta_{ij}I$$

**乘积公式**：

$$(\vec{a} \cdot \vec{\sigma})(\vec{b} \cdot \vec{\sigma}) = \vec{a} \cdot \vec{b} I + i(\vec{a} \times \vec{b}) \cdot \vec{\sigma}$$

---

## 15.3 自旋态的表示

### 15.3.1 自旋向上和向下

$$|\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

### 15.3.2 任意方向的自旋态

沿 $\hat{n} = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$ 方向自旋向上的态：

$$|\uparrow_{\hat{n}}\rangle = \cos\frac{\theta}{2}|\uparrow\rangle + e^{i\phi}\sin\frac{\theta}{2}|\downarrow\rangle = \begin{pmatrix} \cos(\theta/2) \\ e^{i\phi}\sin(\theta/2) \end{pmatrix}$$

### 15.3.3 自旋的测量

测量 $\hat{S}_z$：
- 得到 $+\hbar/2$ 的概率：$|\langle\uparrow|\psi\rangle|^2$
- 得到 $-\hbar/2$ 的概率：$|\langle\downarrow|\psi\rangle|^2$

测量 $\hat{S}_x$：

本征态 $|\pm_x\rangle = \frac{1}{\sqrt{2}}(|\uparrow\rangle \pm |\downarrow\rangle)$

---

## 15.4 自旋的磁矩

### 15.4.1 自旋磁矩

电子的自旋磁矩为：

$$\vec{\mu}_s = -g_s\frac{e}{2m_e}\vec{S}$$

其中 $g_s \approx 2$ 是电子的g因子（狄拉克理论预言 $g_s = 2$，QED修正给出 $g_s = 2.002319...$）。

### 15.4.2 轨道磁矩

轨道角动量对应的磁矩：

$$\vec{\mu}_L = -\frac{e}{2m_e}\vec{L}$$

注意：自旋磁矩的g因子是2，轨道磁矩的g因子是1。

### 15.4.3 总磁矩

原子的总磁矩：

$$\vec{\mu} = \vec{\mu}_L + \vec{\mu}_s = -\frac{e}{2m_e}(\vec{L} + g_s\vec{S})$$

---

## 15.5 Zeeman效应

### 15.5.1 正常Zeeman效应

**条件**：弱磁场，自旋-轨道耦合可忽略（或 $S = 0$）。

**哈密顿量**：

$$\hat{H}_Z = -\vec{\mu}_L \cdot \vec{B} = \frac{e}{2m_e}\hat{L}_z B$$

（取 $\vec{B} = B\hat{z}$）

**能级分裂**：

$$\Delta E = \frac{e\hbar}{2m_e}m_l B = \mu_B m_l B$$

其中 $\mu_B = e\hbar/(2m_e) = 5.788 \times 10^{-5}$ eV/T 是**玻尔磁子**。

**选择定则**：$\Delta m_l = 0, \pm 1$

### 15.5.2 反常Zeeman效应

**条件**：弱磁场，自旋-轨道耦合不可忽略。

**总角动量**：$\vec{J} = \vec{L} + \vec{S}$

**朗德g因子**：

$$g_J = 1 + \frac{J(J+1) + S(S+1) - L(L+1)}{2J(J+1)}$$

**能级分裂**：

$$\Delta E = g_J\mu_B m_J B$$

### 15.5.3 强磁场：Paschen-Back效应

**条件**：强磁场，自旋-轨道耦合可忽略。

**哈密顿量**：

$$\hat{H} = \hat{H}_0 + \frac{eB}{2m_e}(\hat{L}_z + 2\hat{S}_z)$$

**能级分裂**：

$$\Delta E = \mu_B(m_l + 2m_s)B$$

此时 $m_l$ 和 $m_s$ 是好量子数，$j$ 和 $m_j$ 不是。

---

## 15.6 自旋-轨道耦合

### 15.6.1 物理起源

在电子的静止参考系中，原子核绕电子运动，产生磁场 $\vec{B}$。电子自旋磁矩与该磁场相互作用：

$$\hat{H}_{SO} = -\vec{\mu}_s \cdot \vec{B} \propto \vec{L} \cdot \vec{S}$$

### 15.6.2 自旋-轨道哈密顿量

$$\hat{H}_{SO} = \xi(r)\vec{L} \cdot \vec{S}$$

其中 $\xi(r) = \frac{1}{2m_e^2 c^2}\frac{1}{r}\frac{dV}{dr}$（托马斯进动因子 $1/2$ 已包含）。

### 15.6.3 能级修正

利用 $\vec{J} = \vec{L} + \vec{S}$，得 $\vec{L} \cdot \vec{S} = \frac{1}{2}(\hat{J}^2 - \hat{L}^2 - \hat{S}^2)$。

一级微扰修正：

$$\Delta E_{SO} = \frac{\hbar^2}{2}[j(j+1) - l(l+1) - s(s+1)]\langle\xi(r)\rangle$$

对于氢原子，这导致能级的**精细结构**分裂。

---

## 15.7 自旋的应用

### 15.7.1 核磁共振（NMR）

原子核有自旋和磁矩。在外磁场中，自旋能级分裂（Zeeman效应）。施加射频场，当频率匹配能级间距时，发生共振吸收。

**应用**：
- 医学成像（MRI）
- 分子结构分析
- 材料科学

### 15.7.2 自旋电子学

利用电子自旋（而非电荷）存储和处理信息。

**应用**：
- 硬盘读头（巨磁阻效应）
- 磁性随机存储器（MRAM）
- 量子计算（自旋量子比特）

### 15.7.3 量子计算中的自旋量子比特

自旋1/2系统是最自然的量子比特：

$$|0\rangle \equiv |\uparrow\rangle, \quad |1\rangle \equiv |\downarrow\rangle$$

任意量子态：$|\psi\rangle = \alpha|\uparrow\rangle + \beta|\downarrow\rangle$，$|\alpha|^2 + |\beta|^2 = 1$。

---

## 本章小结

1. **Stern-Gerlach实验**：证实了角动量的量子化和自旋的存在。

2. **自旋量子数**：电子 $s = 1/2$，$m_s = \pm 1/2$。

3. **泡利矩阵**：自旋算符的矩阵表示，满足特殊的对易和反对易关系。

4. **自旋磁矩**：$\vec{\mu}_s = -g_s(e/2m_e)\vec{S}$，$g_s \approx 2$。

5. **Zeeman效应**：磁场导致能级分裂，正常Zeeman（$S=0$）、反常Zeeman（$LS$耦合）、Paschen-Back（强场）。

6. **自旋-轨道耦合**：$\hat{H}_{SO} \propto \vec{L} \cdot \vec{S}$，导致精细结构。

7. **应用**：NMR/MRI、自旋电子学、量子计算。

---

## 公式索引

| 编号 | 公式 | 含义 | 推导链接 |
|------|------|------|----------|
| [F184](#graph?f=F184) | $\hat{S}_i = (\hbar/2)\sigma_i$ | 自旋算符 | [查看推导](#graph?f=F184) |
| [F185](#graph?f=F185) | $\vec{\mu}_s = -g_s(e/2m_e)\vec{S}$ | 自旋磁矩 | [查看推导](#graph?f=F185) |
| [F186](#graph?f=F186) | $\Delta E = g_J\mu_B m_J B$ | Zeeman分裂 | [查看推导](#graph?f=F186) |

---

## 思考题

1. Stern-Gerlach实验为什么不能用经典理论解释？

2. 泡利矩阵为什么满足 $\sigma_i^2 = I$？物理意义是什么？

3. 正常Zeeman效应和反常Zeeman效应的区别是什么？

4. 自旋-轨道耦合的物理起源是什么？为什么有托马斯进动因子？

5. 自旋量子比特如何实现量子门操作？

---

**上一章**：[第14章 角动量代数](lecture-14-angular-momentum.md)

**下一章**：[第16章 谐振子代数解法与相干态](lecture-16-oscillator-algebra.md)
