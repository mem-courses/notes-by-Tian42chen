# 随机变量数字特征

## 数学期望

### 离散型X分布律

$P(X=x_k)=p_k,\,k=1,2,\dots$，$$\begin{aligned}
E(X)=&\sum_{k=1}^{\infty}x_k p_k\\
    E\left[g(X)\right]=&\sum_{k=1}^{\infty}g(x_k)p_k
\end{aligned}$$

### 离散型(X,Y)联合分布律

$P(X=x_i,Y=y_j)=p_{ij},\,i,j=1,2,\dots$ , $$\begin{aligned}
E\left[ h(X,Y) \right]=\sum_{i=1}^{\infty}\sum_{j=1}^{\infty}h(x_i,y_j)p_{ij}
\end{aligned}$$

### 连续型X概率密度函数

$f(x)$ , $$\begin{aligned}
E(X)=&\int_{-\infty}^{+\infty}xf(x)\,\mathrm{d}x\\
    E(g(X))=&\int_{-\infty}^{+\infty}g(x)f(x)\,\mathrm{d}x
\end{aligned}$$

### 连续型(X,Y)联合密度函数

$f(x,y)$ $$\begin{aligned}
E\left(h(X,Y)\right)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}h(x,y)f(x,y)\,\mathrm{d}x\mathrm{d}y
\end{aligned}$$

### 性质

1.  $E(aX+bY+c)=aE(X)+bE(Y)+c$

2.  若 $X,Y$ 相互独立，则 $E(XY)=E(X)E(Y)$

## 方差

<span class="m-definition"></span> $$\begin{aligned}
Var(x)=E\left\{\left[X-E(x)\right]^2\right\}
\end{aligned}$$



1.  $Var(X)=E(X^2)-\left[E(X)\right]^2$  
    or $E(X^2)=Var(X)+[E(X)]^2$

2.  离散型 $$\begin{aligned}
    Var(x)=\sum_{i=1}^{\infty}\left[x_i-E(x)\right]^2p_i
    \end{aligned}$$

3.  连续型 $$\begin{aligned}
    Var(x)=\int_{-\infty}^{+\infty}\left[x-E(x)\right]^2f(x)\,\mathrm{d}x
    \end{aligned}$$

### 性质

1.  $a,c\in \mathbb{C},\，Var(aX+c)=a^2Var(X)$。

2.  $Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)$。
    若 $X,Y$ 相互独立，$Var(X+Y)=Var(X)+Var(Y)$。

3.  $Var(X)=0\Longleftrightarrow P(X=C)=1，C=E(X)$。

## 协方差与相关系数

### 协方差

<span class="m-definition"></span> $$\begin{aligned}
Cov(X,Y)=E\left\{ \left[X-E(X)\right]\left[Y-E(Y)\right] \right\}
\end{aligned}$$



$$\begin{aligned}
Cov(X,Y)&=E(XY)-E(X)E(Y)\\
    \text{or } E(XY)&=Cov(X,Y)+E(X)E(Y)
\end{aligned}$$

性质：

1.  $Cov(X,Y)=Cov(Y,X)$

2.  $Cov(X,X)=Var(X)$

3.  $Cov(aX,bY)=abCov(X,Y)$

4.  $Cov(X_1+X_2,Y)=Cov(X_1,Y)+Cov(X_2,Y)$

5.  $Cov(aX+bY,cX+dY)=acVar(X)+bdVar(Y)\\+(ad+bc)Cov(X,Y)$

6.  $Var(aX+bY+c)=a^2Var(X)+b^2Var(Y)\\+2abCov(X,Y)$

### 相关系数

<span class="m-definition"></span> $$\begin{aligned}
\rho_{XY}=&\frac{Cov(X,Y)}{\sqrt{Var(X)Var(Y)}}\\
        =&Cov\left(\frac{X-E(X)}{\sqrt{Var(X)}}\frac{Y-E(Y)}{\sqrt{Var(Y)}}\right)
\end{aligned}$$ 可看作标准化后的协方差



性质:

1.  $|\rho_{XY}|\le 1$。

2.  $|\rho_{XY}|=1\Longleftrightarrow \exists a,b，P(Y=a+bX)=1$  
    特别的，$\rho_{XY}=1，b>0$；$\rho_{XY}=-1，b<0$。

不相关：$\rho_{XY}=0$

1.  $X,Y$ 独立 $\Longrightarrow$ $X,Y$ 不相关。

2.  若 $(X,Y)$ 服从正太分布，
    则 $X,Y$ 独立 $\Longleftrightarrow$ $X,Y$ 不相关

## 正态分布性质

若 $(X,Y)\sim N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)$

1.  $aX+bY+c\sim N(a\mu_1+b\mu_2+c,a^2\sigma_1^2+b^2\sigma_2^2+2ab\rho\sigma_1\sigma_2)$

2.  $Cov(aX+bY,cX+dY)= ac\sigma_1^2+bd\sigma_2^2+(ad+bc)\rho\sigma_1\sigma_2$

3.  $aX+bY，cX+dY$ 相互独立 $\Longleftrightarrow$ $Cov(aX+bY，cX+dY)=0$

## 上 $\alpha$ 分位数

<span class="m-definition"></span> $X$ 连续随机变量，$\exists F(x)，f(x)$，$$\begin{aligned}
P\left\{X>x_{\alpha}\right\}=1-F(x_{\alpha})=\int_{x_{\alpha}}^{=\infty}f(x)\,\mathrm{d}x=\alpha
\end{aligned}$$ $x_{\alpha}$ 为 $X$ 上 $\alpha$ 分位数。


