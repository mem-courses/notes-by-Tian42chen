# 多元随机变量及其分布

## 二元离散型随机变量

### 联合概率分布

<span class="m-definition"></span> 若二元随机变量 $(X,Y)$ 全部可能取到的不同值是有限对或可列无限对，则称 $(X,Y)$ 是离散型随机变量。



联合概率分布律：$$\begin{aligned}
(x_i,y_j),&\，i,j=1,2,\dots\\
    P(X=x_i,Y=y_j)=p_{ij},&\，i,j=1,2,\dots
\end{aligned}$$

性质:

1.  $p_{ij}\ge 0,\,i,j=1,2,\dots$

2.  $\sum_{i=1}^{\infty}\sum_{j=1}^{\infty}p_{ij}=1$

### 边际分布律

$$\begin{aligned}
P(Y=y_j)=&P(X<+\infty，Y=y_j)\\
    =&\sum_{i=1}^{\infty}p_{ij}\equiv p_{\bullet  j}\,j=1,2,\dots\\
    P(X=x_i)=&P(X=x_i，Y<+\infty)\\
    =&\sum_{j=1}^{\infty}p_{ij}\equiv p_{i\bullet }\,i=1,2,\dots
\end{aligned}$$

### 条件分布律

1.  对 $Y=y_j$，若 $P(Y=y_j)>0$ $$\begin{aligned}
    P(X=x_i|Y=y_j)=&\frac{P(X=x_i,Y=y_j)}{P(Y=y_j)}\\
            =&\frac{p_{ij}}{p_{\bullet j}}\，i=1,2,\dots
    \end{aligned}$$

2.  对 $X=x_i$，若 $P(X=x_i)>0$ $$\begin{aligned}
    P(Y=y_j|X=x_i)=&\frac{P(X=x_i,Y=y_j)}{P(X=x_i)}\\
            =&\frac{p_{ij}}{p_{i \bullet }}\，j=1,2,\dots
    \end{aligned}$$

## 随机变量(X,Y)的联合分布函数

$$\begin{aligned}
F(x,y)=&P\left\{(X\le x)\cup (Y\le y)\right\}\\
    \equiv&P(X\le x，Y\le y)
\end{aligned}$$

### 边际分布函数

$$\begin{aligned}
F_X(x)&=F(x,+\infty)=P(X\le x,Y<+\infty)\\
    F_Y(y)&=F(+\infty,y)=P(X<+\infty,Y\le y)
\end{aligned}$$

### 条件分布函数

$$\begin{aligned}
F_{X|Y}(x|y)&=P(X\le x|Y=y)=\frac{P(X\le x,Y=y)}{P(Y=y)}\\
    F_{Y|X}(y|x)&=P(Y\le y|X=x)=\frac{P(X=x,Y\le y)}{P(X=x)}
\end{aligned}$$

## 二元连续型随机变量

### 联合概率密度函数

<span class="m-definition"></span> $F(x,y)$，$\exists f(x,y)>0，\forall x,y$ , $$\begin{aligned}
F(x,y)=\int_{-\infty}^{y}\int_{-\infty}^{x}f(u,v)\,\mathrm{d}u\mathrm{d}v
\end{aligned}$$



性质:

1.  $f(x,y)\ge 0$

2.  $\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}f(x,y)\,\mathrm{d}x\mathrm{d}y=1$

3.  设 $G$ 是平面 $$\begin{aligned}
    P\left\{(X,Y)\in G\right\}=\underset{G}{\iint} f(x,y)\,\mathrm{d}x\mathrm{d}y
    \end{aligned}$$

4.  在 $(x,y)$ 连续 $f(x,y)$，$$\begin{aligned}
    \frac{\partial^2 F(x,y)}{\partial x\partial y}=f(x,y)
    \end{aligned}$$

### 边际概率密度函数

$$\begin{aligned}
f_X(x)=&\int_{-\infty}^{+\infty}f(x,y)\,\mathrm{d}y\\
    f_Y(y)=&\int_{-\infty}^{+\infty}f(x,y)\,\mathrm{d}x
\end{aligned}$$ $$\begin{aligned}
F_X(x)=&\int_{-\infty}^x f_X(u)\,\mathrm{d}u\\
    F_Y(y)=&\int_{-\infty}^y f_Y(v)\,\mathrm{d}v
\end{aligned}$$

### 条件概率密度函数

$$\begin{aligned}
\text{在  $ Y=y $ 下，}f_{X|Y}(x|y)=\frac{f(x,y)}{f_Y(y)}，\，f_Y(y)>0\\
    \text{在  $ X=x $ 下，}f_{Y|X}(y|x)=\frac{f(x,y)}{f_X(x)}，\，f_X(x)>0
\end{aligned}$$ $$\begin{aligned}
F_{X|Y}(x|y)=\int_{-\infty}^x \frac{f(u,y)}{f_Y(y)}\,\mathrm{d}u\\
    F_{Y|X}(y|x)=\int_{-\infty}^y \frac{f(x,v)}{f_X(x)}\,\mathrm{d}v
\end{aligned}$$ $$\begin{aligned}
P(Y\in D| X=x)=\underset{D}{\int}f_{Y|X}(y|x)\,\mathrm{d}y
\end{aligned}$$

## 二元随机变量常见分布及性质

### 二元均匀分布

$(X,Y)$ 在二维有界 $D$ 上，$$\begin{aligned}
f(x,y)=\left\{\begin{array}{lc}
        \frac{1}{D\text{面积}} & (x,y)\in D\\0 & otherwise
    \end{array} \right。
\end{aligned}$$

若 $D_1\subset D$，$$\begin{aligned}
P\left\{(X,Y)\in D_1\right\}=\frac{D_1\text{面积}}{D\text{面积}}
\end{aligned}$$

### 二元正态 $(X,Y)\sim N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho )$ 

性质:

1.  $$\begin{aligned}
    X\sim f_X(x)\sim N(\mu_1,\sigma_1^2)\\
            Y\sim f_Y(y)\sim N(\mu_2,\sigma_2^2)
    \end{aligned}$$

2.  $$\begin{aligned}
    \text{在 $ \{X=x\} $ 条件下，}& \\
            f_{Y|X}(y|x)\sim &N(\mu_2+\rho \frac{\sigma_1}{\sigma_2}(x-\mu_1),(1-\rho^2)\sigma_2^2)\\
            \text{在 $ \{Y=y\} $ 条件下，}& \\
            f_{X|Y}(x|y)\sim &N(\mu_1+\rho \frac{\sigma_2}{\sigma_1}(x-\mu_2),(1-\rho^2)\sigma_1^2)
    \end{aligned}$$

3.  $X$ 与 $Y$ 相互独立 $\Longleftrightarrow$ $\rho=0$

4.  若 $\rho=0$，$aX+bY+c\sim N(a\mu_1+n\mu_2+c,a^2\sigma_1^2+b^2\sigma_2^2)$

## 事件独立性与随机变量独立性

<span class="m-definition"></span> $\forall x,y \in R$，$$P(X\le x,Y\le y)=P(X\le x)P(y\le y)$$ or $$F(x,y)=F_X(x)F_Y(y)$$



$A$ 发生与否都不会改变 $B$ 发生的概率。

$A,B$ 相互独立 $\Longleftrightarrow$ $\bar{A},B$ 相互独立 $\Longleftrightarrow$ $A,\bar{B}$ 相互独立 $\Longleftrightarrow$ $\bar{A},\bar{B}$ 相互独立。

1.  离散型独立 $\Longleftrightarrow$ $$\begin{aligned}
    \forall i,j,\，P(X=x_i,Y=y_j)=P(X=x_i)P(Y=y_j)
    \end{aligned}$$

2.  连续型独立 $\Longleftrightarrow$ $$\begin{aligned}
    f(x,y)=f_X(x)f_Y(y)
    \end{aligned}$$ 除去0面积后处处成立。

## 二元随机变量函数的分布

### 离散型

$(X,Y)$，有 $P(X=x_i,Y=y_i)=p_{ij}$。

1.  若 $U=u(x,y)，V=v(x,y)$，先定 $u_i,v_j$，找 $(U=u_i,V=V_j)=\left\{(X,Y)\in D\right\}$。

2.  若 $Z=z(x,y)$，先定 $z_i$，找 $(Z=z_i)=\left\{(X,Y)\in D\right\}$。

### 连续型

分布函数 $$\begin{aligned}
F_Z(z)=P(g(X,Y)\le z)=\underset{g(x,y)\le z}{\iint} f(x,y)\，\mathrm{d}x\mathrm{d}y
\end{aligned}$$

1.  $Z=X+Y$ $$\begin{aligned}
    f_Z(z)=&\int_{-\infty}^{\infty}f(z-y,y)\,\mathrm{d}y\\
            =&\int_{-\infty}^{\infty}f(x,z-x)\,\mathrm{d}x
    \end{aligned}$$

    若 $X,Y$ 独立, $$\begin{aligned}
    f_Z(z)=&\int_{-\infty}^{\infty}f_X(x)f_Y(z-x)\,\mathrm{d}x\\
            =&\int_{-\infty}^{\infty}f_X(z-y)f_Y(y)\,\mathrm{d}y
    \end{aligned}$$

2.  $M=\max\left\{X,Y\right\}$，$N=\min\left\{X,Y\right\}$，$X,Y$ 独立 $$\begin{aligned}
    F_M(z)=&P(X\le z,Y\le z)=F_X(z)F_Y(z)\\
            F_N(z)=&1-P(X>z,Y>z)\\=&1-(1-F_X(z))(1-F_Y(z))
    \end{aligned}$$
