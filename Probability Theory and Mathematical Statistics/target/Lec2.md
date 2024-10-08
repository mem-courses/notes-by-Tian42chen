# 随机变量及分布函数

## 随机变量

<span class="m-definition"></span> 设随机试验的样本空间 $S=\{e\}$，若 $X=X(e)$ 为定义在样本空间 $S$ 上的实值单值函数，则称 $X=X(e)$ 为随机变量。



## 分布函数

<span class="m-definition"></span> 随机变量 $X$ 的分布函数：$$\forall x \in R，\，F(x)=P(X\le x)$$



性质：

1.  $0\le F(x) \le 1$

2.  $F(x)$ 单调不减，且 $F(-\infty )=0，F(+\infty)=1$

3.  $F(x)$ 右连续，即 $F(x+0)=F(x)$

4.  $F(x)-F(x-0)=P(X=x)$

## 离散型随机变量

<span class="m-definition"></span> 取值至多可数的随机变量为 **离散型的随机变量**。$$\begin{aligned}
\text{概率分布律性质：}& p\ge 0,\,\sum_{i=1}^{\infty}p_i=1\\
        \text{分布函数：}& F(x)=\sum_{x_k\le x} p_k
\end{aligned}$$



### 0-1分布 $X\sim B(1,p)$ 

|  X  |   0   |  1  |
|:---:|:-----:|:---:|
|  P  | $1-p$ | $p$ |

$$\begin{aligned}
F(x)=P\left\{X\le x\right\}=\left\{ \begin{array}{lc}
        0 &x<0 \\ 1-p & 0\le x <1 \\ 1 & x\ge 1
    \end{array} \right。\\
\end{aligned}$$ $$\begin{aligned}
E(X)=p,\，Var(X)=p(1-p)
\end{aligned}$$

### n重贝努里试验与二项分布 $X\sim B(n,p)$ 

进行 $n$ 次独立重复观测，每次 $A$ 或 $\bar{A}$ 发生，$P(A)=p$，$X$ 表示 $A$ 发生的次数。

$$\begin{aligned}
P(X=k)=C_n^k p^k (1-p)^{n-k},\，k=0,1,\dots,n
\end{aligned}$$ $$\begin{aligned}
E(x)=np,\，Var(X)=np(1-p)
\end{aligned}$$

### 泊松分布 $X\sim P(\lambda)$ 

$$\begin{aligned}
P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}，\，k=0,1,\dots
\end{aligned}$$ $$\begin{aligned}
E(X)=Var(X)=\lambda
\end{aligned}$$

泊松定理:

<span class="m-theorem"></span> 当 $n>10，p<0.1$ 时，$$\begin{aligned}
C_n^k p^k(1-p)^{n-k} \approx \frac{e^{-\lambda}\lambda^k}{k!}，\，\lambda=np
\end{aligned}$$



## 连续型随机变量

<span class="m-definition"></span> 对于随机变量 $X$ 的分布函数 $F(x)$，若对 $\forall x \in R$，$\exists f(x)\ge 0$，$$\begin{aligned}
F(x)=\int_{-\infty}^{x}f(t)\,\mathrm{d}t
\end{aligned}$$ 则称 $X$ 为 **连续型随机变量**，其中 $f(x)$ 称为 $X$ 的 **概率密度函数**，简称 **密度函数**。



性质:

1.  $f(x)\ge 0$

2.  $\int_{-\infty}^{\infty}f(x)\,\mathrm{d}x=1$

3.  $P(a\le X\le b)=P(a<X<b)=F(b)-F(a)=\int_{b}^{a}f(x)\,\mathrm{d}x$

### 均匀分布 $X\sim U(a,b)$ 

$$\begin{aligned}
f(x)=&\left\{\begin{array}{lc}
        \frac{1}{b-a} & x\in(a,b)\\0 & otherwise
    \end{array} \right.\\
    F(x)=&\left\{\begin{array}{lc}
        0 & x<a\\ \frac{x-a}{b-a} & a\le x<b \\ 1 & x\ge b
    \end{array} \right。
\end{aligned}$$ $$\begin{aligned}
E(X)=\frac{a+b}{2}，\，Var(X)=\frac{(b-a)^2}{12}
\end{aligned}$$ $$\begin{aligned}
a<c<d<b，\，P(c\le X \le d)=\frac{d-c}{b-a}
\end{aligned}$$

### 正态分布 $X\sim N(\mu,\sigma^2)$ 

$$\begin{aligned}
f(x)=\frac{1}{\sqrt{2\pi} \sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}，\，-\infty<x<\infty
\end{aligned}$$ $$\begin{aligned}
E(X)=\mu,\,Var(X)=\sigma^2
\end{aligned}$$

标准正态分布 $N(0,1)$ : $$\begin{aligned}
\psi(x)=&\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}\\
    \Phi(x)=&\int_{-\infty}^x \frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\,\mathrm{d}t
\end{aligned}$$

性质：

1.  $\Phi(-x)+\Phi(x)=1,\,\Phi(0)=\frac{1}{2}$

2.  $\Phi(z_{\alpha})=1-\alpha，\，z_{1-\alpha}=-z_{\alpha}$

3.  当 $X\sim N(\mu,\sigma^2)$ 时：令 $t=\frac{x-\mu}{\sigma} \sim N(0,1)$，$$\begin{aligned}
    P(x\le b)=\Phi(\frac{b-\mu}{\sigma})
    \end{aligned}$$

4.  $aX+b \sim N(a\mu+b，a^2\sigma^2)$

### 指数分布 $X\sim Exp(\lambda)$ 

$$\begin{aligned}
f(x)=&\left\{ \begin{array}{lc}
        \lambda e^{-\lambda x} & x>0 \\ 0 & x\le 0
    \end{array} \right.\\
    F(x)=&\left\{\begin{array}{lc}
        1-e^{-\lambda x} & x>0 \\ 0 & x\le 0
    \end{array} \right。
\end{aligned}$$ $$\begin{aligned}
E(X)=\frac{1}{\lambda},\，Var(X)=\frac{1}{\lambda^2}
\end{aligned}$$

无记忆性：$$\begin{aligned}
s>0,t>0,\，P(X>s+t|X>s)=P(X>t)=e^{-\lambda t}
\end{aligned}$$

## 随机变量函数的分布

已知 $X$ 的概率分布，$Y=g(X)$，求 $Y$ 的概率分布。

1.  若Y为离散型随机变量，则先写出 $Y$ 的可能取值：$y_1,y_2,\dots,y_j,\dots$，再找出 $(Y=y_i)$ 的等价事件 $(X\in D_j)$，得 $P(Y=y_i)=P(X\in D_j)$。

2.  若Y为连续型随机变量，则先写出 $Y$ 的概率分布函数：$F_Y(y)=P(Y\le y)$，找出 $(Y\le y)$ 的等价事件 $(X\in D_y)$，得 $F_Y(y)=P(X\in D_y)$；再求出 $Y$ 的概率密度函数 $f_Y(y)$。

<span class="m-definition"></span> 设 $X\sim f_X(x)$，$-\infty < x < \infty$，$y=g(x)$ 是严增(减)可微函数，即 $g'(x)>0$ (或 $g'(x)<0$ )。$Y=g(X)$，则 $Y$ 具有概率密度函数为 $$\begin{aligned}
f_Y(y)=\left\{\begin{array}{lc}
            f_X\left(h(y)\right)\cdot \left| h'(y) \right| & \alpha<y<\beta\\ 0 & otherwise
        \end{array} \right。
\end{aligned}$$ 这里 $(\alpha,\beta)$ 是 $Y$ 的取值范围，$h$ 是 $g$ 的反函数，$h(y)=x\Longleftrightarrow y=g(x)$。


