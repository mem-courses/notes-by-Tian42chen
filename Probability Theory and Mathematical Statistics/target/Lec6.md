# 统计量与抽样分布

## 随机样本与统计量

### 总体

随机变量 $X$。

### 样本(简单随机样本)

$X_1,X_2,\dots,X_n$ 相互独立且与 $X$ 同分布。

### 样本均值 

$$\begin{aligned}
\bar{X}=\frac{1}{n}\sum_{i=1}^n X_i
\end{aligned}$$

### 样本方差

$$\begin{aligned}
S^2=&\frac{1}{n-1}\sum_{i=1}^n \left(X_i-\bar{X}\right)^2\\
    Var(S^2)=&\frac{2\sigma^4}{n-1}
\end{aligned}$$

### 样本k阶(原点)矩

$$\begin{aligned}
A_k=\frac{1}{n}\sum_{i=1}^n X_i^k\，(k=1,2,\dots)
\end{aligned}$$

### 样本k阶中心矩

$$\begin{aligned}
B_k=\frac{1}{n}\sum_{i=1}^n \left(X_i-\bar{X}\right)^k\，(k=1,2,\dots)
\end{aligned}$$

## 一些分布

###  $\chi^2$ 分布

<span class="m-definition"></span> 随机变量 $X_1,X_2,\dots,X_n$ 相互独立，$X_i\sim N(0,1)$ $$\begin{aligned}
\chi^2=\sum_{i=1}^2 X_i^2 \sim \chi^2(n)
\end{aligned}$$



性质：

1.  $X\sim \chi^2(n)$，则 $E(X)=n，\，Var(X)=2n$。

2.  $Y_i \sim \chi^2(n)$，$i=1,2$，$Y_1,Y_2$ 相互独立，
    则 $Y_1+Y_2\sim \chi^2(n_1+n_2)$。

###  $t$ 分布

<span class="m-definition"></span> $X,Y$ 相互独立，$X\sim N(0,1)$，$Y\sim \chi^2(n)$，$$\begin{aligned}
T=\frac{X}{\sqrt{\frac{Y}{n}}}\sim t(n)
\end{aligned}$$



性质：$t_{1-\alpha}(n)+t_{\alpha}(n)=0$

###  $F$ 分布

<span class="m-definition"></span> $X\sim \chi^2(n_1)$，$Y\sim \chi^2(n_2)$，$X,Y$ 相互独立，$$\begin{aligned}
F=\frac{\frac{X}{n_1}}{\frac{Y}{n_2}}\sim F(n_1,n_2)
\end{aligned}$$



性质：

1.  $F\sim F(n_1,n_2)$，则 $\frac{1}{F}\sim F(n_2,n_1)$。

2.  $F_{1-\alpha}(n_1,n_2)F_{\alpha}(n_2,n_1)=1$。

3.  $T\sim t(n)$，则 $T^2\sim F(1,n)$。

## 正态总体下的抽样分布

<span class="m-theorem"></span> $X_1,X_2,\dots,X_n$ 为自正太总体 $N(\mu,\sigma^2)$ 简单随机样本，$\bar{X}$ 为样本均值，$S^2$ 为样本方差，则

1.  $$\begin{aligned}
    \bar{X}\sim& N(\mu,\frac{\sigma^2}{n})\\
                \text{or }\frac{(\bar{X}-\mu)}{\frac{\sigma}{\sqrt{n}}}\sim& N(0,1)
    \end{aligned}$$

2.  $$\begin{aligned}
    \frac{(n-1)S^2}{\sigma^2}=\frac{\sum_{i=1}^n(X_i-\bar{X})^2}{\sigma^2}\sim \chi ^2(n-1)
    \end{aligned}$$

3.  $$\begin{aligned}
    \frac{(\bar{X}-\mu)}{\frac{S}{\sqrt{n}}}\sim t(n-1)
    \end{aligned}$$

$\bar{X}$ 与 $S^2$ 相互独立。



<span class="m-theorem"></span> $(X_1,\dots,X_{n_1})$，$(Y_1,\dots,Y_{n_2})$ 来自  
$N(\mu_1,\sigma_1^2)$，$N(\mu_2,\sigma_2^2)$，且相互独立，有 $\bar{X},\bar{Y}，S_1^2，S_2^2$，则

1.  $$\begin{aligned}
    \frac{\frac{S_1^2}{\sigma_1^2}}{\frac{S_2^2}{\sigma_2^2}}=\frac{\frac{S_1^2}{S_2^2}}{\frac{\sigma_1^2}{\sigma_2^2}}\sim F(n_1-1,n_2-1)
    \end{aligned}$$

2.  $$\begin{aligned}
    \frac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}}}\sim N(0,1)
    \end{aligned}$$

3.  当 $\sigma_1^2=\sigma_2^2=\sigma^2$，$$\begin{aligned}
    \frac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{S_w\cdot\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}\sim t(n_1+n_2-2)\\
                S_w^2=\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}{n_1+n_2-2}
    \end{aligned}$$ $E(S_w^2)=\sigma^2$，$Var(S_w^2)=\frac{\sigma^4}{n_1+n_2-2}$


