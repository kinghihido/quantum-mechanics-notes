
**上一章**：[第19章](https://kinghihido.github.io/quantum-mechanics-notes/content/lectures/lecture-19-scattering.md)
# 第20章 · 定态微扰论

> 量子力学中能精确求解的问题屈指可数（谐振子、氢原子、无限深势阱……）。真实的物理系统几乎总是需要近似方法。**微扰论**的核心思想：如果哈密顿量 $\hat H=\hat H_0+\hat H'$，其中 $\hat H_0$ 可精确求解、$\hat H'$ 很小，那么可以从 $\hat H_0$ 的已知解出发，逐阶修正得到 $\hat H$ 的近似解。

---

## 20.1 非简并微扰论

### 20.1.1 设定

已知 $\hat H_0|n^{(0)}\rangle=E_n^{(0)}|n^{(0)}\rangle$ 的完整解。求 $\hat H=\hat H_0+\lambda\hat H'$ 的本征值和本征态（$\lambda$ 是小参数，最后令 $\lambda=1$）。

把待求量展开为 $\lambda$ 的幂级数：

$$E_n=E_n^{(0)}+\lambda E_n^{(1)}+\lambda^2 E_n^{(2)}+\cdots$$
$$|n\rangle=|n^{(0)}\rangle+\lambda|n^{(1)}\rangle+\lambda^2|n^{(2)}\rangle+\cdots$$

### 20.1.2 一阶修正

**能量一阶修正**：

$$E_n^{(1)}=\langle n^{(0)}|\hat H'|n^{(0)}\rangle$$

物理意义：能量的一阶修正就是微扰在未微扰态上的**期望值**。

**态的一阶修正**：

$$|n^{(1)}\rangle=\sum_{m\neq n}\frac{\langle m^{(0)}|\hat H'|n^{(0)}\rangle}{E_n^{(0)}-E_m^{(0)}}|m^{(0)}\rangle$$

微扰把其他态 $|m^{(0)}\rangle$ "混"进来了，混合系数与矩阵元 $\langle m|\hat H'|n\rangle$ 成正比，与能级差 $E_n-E_m$ 成反比。

### 20.1.3 二阶修正

**能量二阶修正**：

$$E_n^{(2)}=\sum_{m\neq n}\frac{|\langle m^{(0)}|\hat H'|n^{(0)}\rangle|^2}{E_n^{(0)}-E_m^{(0)}}$$

**重要性质**：基态能量的二阶修正**总是负的**（因为分母 $E_0-E_m<0$）。这意味着微扰总是降低基态能量——变分法的直觉与此一致。

### 20.1.4 适用条件

微扰论有效的条件：

$$\left|\frac{\langle m^{(0)}|\hat H'|n^{(0)}\rangle}{E_n^{(0)}-E_m^{(0)}}\right|\ll 1\quad\text{对所有 }m\neq n$$

微扰矩阵元远小于能级间距。如果能级简并或近简并，分母趋于零，微扰论失效——需要用**简并微扰论**。

---

## 20.2 简并微扰论

### 20.2.1 问题

设 $\hat H_0$ 的能级 $E_D^{(0)}$ 有 $g$ 重简并，简并子空间由 $\{|D,1\rangle,|D,2\rangle,\dots,|D,g\rangle\}$ 张成。

在简并子空间内，分母 $E_D^{(0)}-E_D^{(0)}=0$，一阶修正公式发散。

### 20.2.2 解法：在简并子空间内对角化

构造微扰在简并子空间内的 $g\times g$ 矩阵：

$$W_{ij}=\langle D,i|\hat H'|D,j\rangle$$

解本征值方程：

$$\det(W-\varepsilon^{(1)}I)=0$$

得到 $g$ 个一阶能量修正 $\varepsilon_1^{(1)},\varepsilon_2^{(1)},\dots,\varepsilon_g^{(1)}$。

**物理意义**：微扰**解除简并**（或部分解除），原来能量相同的 $g$ 个态分裂为 $g$ 个能级，间距为 $\sim\lambda\varepsilon^{(1)}$。

### 20.2.3 正确的零级波函数

对角化 $W$ 矩阵的本征矢，给出了**正确的零级波函数**——它们是简并子空间中"被微扰选中"的特定线性组合。

---

## 20.3 经典应用：Stark效应

### 20.3.1 氢原子的一阶Stark效应

氢原子 $n=2$ 能级有4重简并（不考虑自旋）：$|2s\rangle,|2p_0\rangle,|2p_{+1}\rangle,|2p_{-1}\rangle$。

加外电场 $\mathbf{E}=E\hat z$，微扰 $\hat H'=-eEz=-eEr\cos\theta$。

在简并子空间内计算 $W$ 矩阵，非零矩阵元只有：

$$\langle 2s|\hat H'|2p_0\rangle=-3ea_0E$$

对角化 $2\times 2$ 子矩阵，得到能量修正：

$$\Delta E=\pm 3ea_0E,\quad 0,\quad 0$$

$n=2$ 能级分裂为3条：一条上移 $3ea_0E$，一条下移 $3ea_0E$，两条不动。

**线性Stark效应**是氢原子特有的（因为库仑势的 $l$ 简并），一般原子只有**二次Stark效应**（$\Delta E\propto E^2$）。

### 20.3.2 二次Stark效应

对非简并能级（如基态），一阶修正 $\langle 0|\hat H'|0\rangle$ 可能为零（由对称性），此时主导的是二阶修正：

$$\Delta E_0^{(2)}=\sum_{n\neq 0}\frac{|\langle n|\hat H'|0\rangle|^2}{E_0-E_n}<0$$

基态能量总是被电场降低。定义**极化率** $\alpha$：$\Delta E=-\frac{1}{2}\alpha E^2$。

---

## 20.4 经典应用：Zeeman效应

### 20.4.1 正常Zeeman效应

外磁场 $\mathbf{B}=B\hat z$，微扰（忽略自旋）：

$$\hat H'=-\frac{eB}{2m_e}\hat L_z=\omega_L\hat L_z$$

其中 $\omega_L=eB/2m_e$ 是 Larmor 频率。

对非简并微扰（或简并但 $\hat L_z$ 已对角的情况），一阶修正：

$$\Delta E=\omega_L m\hbar=m\hbar\omega_L$$

原来 $2\ell+1$ 重简并的能级分裂为等间距的 $2\ell+1$ 条，间距 $\hbar\omega_L$。

跃迁选择定则 $\Delta m=0,\pm 1$ 给出三条谱线——这就是"正常"Zeeman三重线。

### 20.4.2 反常Zeeman效应

考虑自旋后，微扰：

$$\hat H'=\frac{eB}{2m_e}(\hat L_z+2\hat S_z)$$

总角动量 $\mathbf{J}=\mathbf{L}+\mathbf{S}$，在hat H' 在 $|j,m_j\rangle$ 基下不完全对角。需要用 Landé $g$ 因子：

$$\Delta E=g_J m_J\mu_B B$$

$$g_J=1+\frac{j(j+1)+s(s+1)-\ell(\ell+1)}{2j(j+1)}$$

不同 $j$ 的能级以不同速率分裂——谱线比正常Zeeman效应复杂得多，故称"反常"。

---

## 20.5 微扰论在量子化学中的应用

### 20.5.1 分子轨道理论

分子中的电子近似在核和其他电子的平均场中运动。零级哈密顿量是单电子哈密顿量之和，微扰是电子-电子相互作用的涨落部分。

**Møller-Plesset 微扰论**（MP2, MP4, …）：以 Hartree-Fock 解为零级，逐阶修正电子关联能。这是量子化学计算的标准方法之一。

### 20.5.2 微扰论的局限

- 当微扰与能级间距相当时失效
- 级数可能不收敛（Dyson 1952 证明 QED 的微扰级数渐近而非收敛）
- 强关联系统需要非微扰方法（变分法、数值对角化、密度矩阵重整化群等）

---

## 20.6 本章小结

| 概念 | 要点 |
|---|---|
| 非简并微扰 | $E_n^{(1)}=\langle n|\hat H'|n\rangle$，态修正混合其他能级 |
| 二阶能量 | $E_n^{(2)}=\sum_{m\neq n}\frac{|H'_{mn}|^2}{E_n-E_m}$，基态总是降低 |
| 简并微扰 | 在简并子空间对角化 $W$ 矩阵 |
| Stark效应 | 电场导致能级分裂（氢原子线性，一般原子二次） |
| Zeeman效应 | 磁场导致能级分裂（正常/反常，Landé g因子） |
| 适用条件 | 微扰矩阵元 $\ll$ 能级间距 |

---

> **下一步**：定态微扰论处理的是与时间无关的微扰。如果微扰随时间变化——比如原子受到光波的交变电场作用——系统会在不同能级之间跃迁。这就是**含时微扰论**和**Fermi黄金定则**，第21章的主题。

**下一章**：[第21章](https://kinghihido.github.io/quantum-mechanics-notes/content/lectures/lecture-21-perturbation-time.md)
