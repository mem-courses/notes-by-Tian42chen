# 大数定律和中心极限定理

## 依概率收敛

<span class="m-definition"></span> $Y_1,\dots,Y_n$，$\exists c\in R，\forall \epsilon>0$ , $$\lim_{n\rightarrow +\infty}P\left\{\left| Y_n-c \right|\ge \epsilon \right\}=0$$ 称 $\left\{Y_n,n\ge 1\right\}$ 依概率收敛于 $c$，记 $Y_n \overset{P}{\longrightarrow}c，(n\rightarrow +\infty)$。



性质：若 $X_n \overset{P}{\longrightarrow}a，Y_n \overset{P}{\longrightarrow}b$，$g\in \mathbb{C}(a,b)$ , $$\begin{aligned}
g(X_n,Y_n) \overset{P}{\longrightarrow} g(a,b)
\end{aligned}$$

## 不等式

### 马尔可夫不等式

<span class="m-theorem"></span> 对随机变量 $Y$，$\exists k$ 阶矩 $(k\ge 1)$，$\forall \epsilon >0$ $$\begin{aligned}
P\left\{|Y|\ge \epsilon\right\}\le& \frac{E\left(|Y|^k\right)}{\epsilon^k}\\
        \text{or }P\left\{|Y|<\epsilon\right\}\ge & 1-\frac{E\left(|Y|^k\right)}{\epsilon^k}
\end{aligned}$$



### 切比雪夫不等式

<span class="m-theorem"></span> 对随机变量 $X$，$\exists Var(x)$，$\forall \epsilon >0$ $$\begin{aligned}
P\left\{|X-E(X)|\ge \epsilon\right\}\le& \frac{Var(x)}{\epsilon^2}\\
        P\left\{|X-E(X)|< \epsilon\right\}\ge& 1-\frac{Var(x)}{\epsilon^2}
\end{aligned}$$



## 大数定律

### 弱大数定律

<span class="m-theorem"></span> 随机变量序列 $Y_1,\dots,Y_n,\dots$，若 $\exists \left\{c_n，n\ge 1\right\}$，则当 $n\rightarrow +\infty$，$$\begin{aligned}
\frac{1}{n}\sum_{i=1}^n Y_i-c_n\overset{P}{\longrightarrow}0
\end{aligned}$$ 即 $\forall \epsilon>0$，$$\begin{aligned}
\lim_{n\rightarrow \infty}P\left\{ \left| \frac{1}{n}\sum_{i=1}^n Y_i-c_n \right|\ge \epsilon \right\}=0
\end{aligned}$$ 特别地，当 $c_n\equiv c，n=1,2,\dots$，$n\rightarrow +\infty$，$$\begin{aligned}
\frac{1}{n}\sum_{i=1}^n Y_i\overset{P}{\longrightarrow}c
\end{aligned}$$



### 切比雪夫大数定律

<span class="m-theorem"></span> $X_1,X_2,\dots,X_n$ 相互独立，且 $\exists E(X_i)=\mu$，
$Var(X_i)=\sigma^2$，则 $n\rightarrow +\infty$，$$\begin{aligned}
\frac{1}{n}\sum_{i=1}^n X_i \overset{P}{\longrightarrow} \mu
\end{aligned}$$



### 辛钦大数定律

<span class="m-theorem"></span> $X_1,\dots，X_n$ 独立同分布，且 $\exists E(X_i)=\mu$，则当 $n\rightarrow +\infty$，$$\begin{aligned}
\frac{1}{n}\sum_{i=1}^n X_i \overset{P}{\longrightarrow} \mu
\end{aligned}$$ 若 $h(x)\in \mathbb{C}，\，\exists E(h(X_1))=a$，则当 $n\rightarrow +\infty$，$$\begin{aligned}
\frac{1}{n}\sum_{i=1}^n h(x_i) \overset{P}{\longrightarrow} a
\end{aligned}$$



### 贝努里大数定律

<span class="m-theorem"></span> $n_A$ 为 $n$ 重贝努里实验中 $A$ 发生次数，$P(A)=p$，则当 $n\rightarrow +\infty$，$$\begin{aligned}
\frac{n_A}{n}\overset{P}{\longrightarrow}p
\end{aligned}$$



## 中心极限定律

### 林德贝格-列维中心极限定理 (独立同分布)

<span class="m-theorem"></span> $X_1,X_2,\dots,X_n$ 独立同分布，$E(X_i)=\mu$ ,  
$Var(X_i)=\sigma^2$，当 $n$ 足够大时 $(n>50)$，$$\begin{aligned}
\sum_{i=1}^n X_i \sim& N(n\mu,n\sigma^2)\\
        \frac{1}{n}\sum_{i=1}^n X_i \sim& N(\mu,\frac{\sigma^2}{n})
\end{aligned}$$



### 棣莫弗—拉普拉斯中心极限定理 (二项分布)

<span class="m-theorem"></span> $n_A$ 为 $n$ 重贝努里实验中 $A$ 发生次数，$P(A)=p$，当 $n$ 足够大时，$$\begin{aligned}
B(n,p)\sim N\left(np,np(1-p)\right)
\end{aligned}$$


