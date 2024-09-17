# 概率论基本概念

## 事件的关系与运算

### 随机试验

对随机现象的观察、记录、实验统称为 **随机试验**。它具有以下特性：

1.  可以在相同条件下重复进行；

2.  事先知道可能出现的结果 $(\ge 2)$；

3.  进行试验前并不知道哪个试验结果会发生。

### 样本空间

<span class="m-definition"></span> 随机试验E的所有结果构成的集合称为 $E$ 的 **样本空间**，记为 $S=\{e\}$，称 $S$ 中的元素 $e$ 为 **样本点**，一个元素的单点集称为 **基本事件**。



### 随机事件

一般我们称 $S$ 的子集 $A$ 为 $E$ 的 **随机事件 $A$**，简称 **事件 $A$** .当且仅当 $A$ 所包含的一个样本点发生称 **事件 $A$ 发生**。

### 运算与关系

和、差、积、逆、包含、不相容

## 概率定义与性质

### 频率

<span class="m-definition"></span> $f_n(A)=\frac{n_A}{n}$，在 $n$ 次中 $A$ 发生 $n_A$ 次。



性质：

1.  $0\le f_n(A) \le 1$

2.  $f_n(S)=1$

3.  若 $A_1,A_2,\dots,A_k$ 两两不相容，则 $$\begin{aligned}
    f_n\left(\bigcup_{i=1}^k A_i\right)=\sum_{i=1}^k f_n(A_i)
    \end{aligned}$$

### 概率

<span class="m-definition"></span> 对样本空间 $S$ 中任一事件 $A$，定义一个实数 $P(A)$，满足以下三条公理：

1.  非负性：$P(A)\ge 0$

2.  规范性：$P(S)=1$

3.  可列可加性：若 $A_1,A_2,\dots,A_k,\dots$ 两两不相容，则 $$\begin{aligned}
    P\left(\bigcup_{i=1}^{\infty}A_i\right)=\sum_{i=1}^{\infty}P(A_i)
    \end{aligned}$$

称 $P(A)$ 为事件 $A$ 的 **概率**。



性质：

1.  $P(\phi)=0$

2.  $A_1,A_2,\dots,A_n$，$A_i A_j=\phi，i\ne j$ $$\begin{aligned}
    P\left(\bigcup_{i=1}^{n}A_i\right)=\sum_{i=1}^{n}P(A_i)
    \end{aligned}$$

3.  $P(A)=1-P(\bar{A})$

4.  $P(B-A)=P(B)-P(AB)=P(B\bar{A})$

5.  $P(A\cup B)=P(A)+P(B)-P(AB)$ $$\begin{aligned}
    P\left(\bigcup_{i=1}^n A_i\right)=&\sum_{i=1}^n P(A_i)-\sum_{1\le i<j\le n}P(A_i A_j)\\
            &+\sum_{1\le i<j<k\le n}P(A_i A_j A_k)+\cdots\\
            &+(-1)^{n-1}P(A_1 A_2 \cdots A_n)
    \end{aligned}$$

6.  $P(AB)=P(A)P(B|A)$ 若 $P(A)>0$ $$\begin{aligned}
    P(A_1\cdots A_n)=P(A_1)P(A_2|A_1)\cdots P(A_n|A_1\cdots A_{n-1})
    \end{aligned}$$

## 等可能概型

<span class="m-definition"></span> 若试验 $E$ 满足:

1.  S中样本点有限(有限性)

2.  出现每一样本点的概率相等(等可能性)

称这种试验为等可能概型(或古典概型)。$$P(A)=\frac{A \text{所包含的样本点数}}{S \text{中的样本点数}}$$



## 条件概率

<span class="m-definition"></span> $$P(B|A)=\frac{P(AB)}{P(A)}，\，P(A)>0$$



### 全概率公式与Bayes公式

<span class="m-definition"></span> 称 $B_1,B_2,\dots,B_n$ 为 $S$ 的一个划分，若

1.  不漏 $B_1 \cup B_2 \cup \cdots \cup B_n =S$

2.  不重 $B_i B_j=\phi，\，i\ne j$



<span class="m-theorem"></span> 设 $B_1,B_2,\dots,B_n$ 为样本空间 $S$ 的一个划分，$P(B_i)>0，\，i=1,2,\dots,n$，则称 $$P(A)=\sum_{j=1}^n P(B_j)\cdot P(A|B_j)$$ 为 **全概率公式**。



<span class="m-theorem"></span> 接全概率公式的条件，且 $P(A)>0$ ,则 $$P(B_i|A)=\frac{P(B_i)P(A|B_i)}{\sum_{j=1}^n P(B_j)\cdot P(A|B_j)}$$ 称为 **Bayes公式**。



## 事件独立性与独立试验

<span class="m-definition"></span> 设 $A，B$ 为两随机事件，如果 $P(AB)=P(A)P(B)$，则称 **$A$ 与 $B$ 相互独立**。若 $P(A)\ne 0，P(B)\ne 0$，则 $$\begin{aligned}
P(AB)=P(A)P(B)&\Longleftrightarrow P(A|B)=P(A)\\
        &\Longleftrightarrow P(B|A)=P(B)
\end{aligned}$$



<span class="m-definition"></span> 设 $A_1,A_2,\dots,A_n$ 为 $n$ 个随机时间，若对 $2\le k \le n$，均有 $$\begin{aligned}
P(A_{i_1}A_{i_2}\cdots A_{i_n})=\prod_{j=1}^k P(A_{i_j})
\end{aligned}$$ 则称 $A_1,A_2,\dots,A_n$ 相互独立。


