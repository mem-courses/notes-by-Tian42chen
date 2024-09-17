# 参数估计

## 矩估计

总体 $X$ 有m个未知参数 $\theta_1,\dots,\theta_m$，
$\exists m$ 阶矩 $\mu_1,\dots,\mu_m$

1.  计算 $\mu_k=E(X^k)=g_k(\theta_1,\dots,\theta_m),\,k=1,\dots,m$。

2.  求反函数，得 $\theta_k=h_k(\mu_1,\dots,\mu_m),\,k=1,\dots,m$。

3.  以样本各阶矩 $A_1,\dots,A_m$ 代替  
    总体各阶矩 $\theta_1,\dots,\theta_m$，得各参数的矩估计 $$\begin{aligned}
    \hat{\theta}=h_k(A_1,\dots,A_m),\,k=1,\dots,m
    \end{aligned}$$

## 极大似然估计

设总体 $X$ 的分布律为 $p(x;\theta)$ (或密度函数 $f(x;\theta)$ )，$\theta\in \Theta$。从总体 $X$ 中取得样本 $X_1,\dots,X_n$，其观察值为 $x_1,\dots,x_n$。似然函数 $L(\theta)=\prod_{i=1}^n p(x_i;\theta)$ (或 $L(\theta)=\prod_{i=1}^n f(x_i;\theta)$ )。$$\begin{aligned}
\text{极大似然原理 }L\left(\hat{\theta}(x_1,\dots,x_n)\right)=\max_{\theta\in \Theta}L(\theta)
\end{aligned}$$ $\hat{\theta}(x_1,\dots,x_n)$ 称为 $\theta$ 的极大似然估计值，相应统计量 $\hat{\theta}(X_1,\dots,X_n)$ 称为 $\theta$ 的极大似然估计量(MLE)。

求解:

1.  令 $\ln L(\theta)=l(\theta)$，称为对数似然函数，再令 $$\begin{aligned}
    \left.\frac{\partial l(\theta)}{\partial \theta_i}\right|_{\hat{\theta}_i，1\le i \le k}=0
    \end{aligned}$$ 解得 $\hat{\theta}_i$，$i=1,2,\dots,k$。

2.  若 $L(\theta)$ 关于某个 $\theta_i$ 单调增(减), $$\begin{aligned}
    \theta_i \le (\ge) \hat{\theta}_i(x_1,\dots,x_n)
    \end{aligned}$$ 此时 $\hat{\theta}(x_1,\dots,x_n)$ 为 $\theta$ 的极大似然估计值，相应统计量 $\hat{\theta}(X_1,\dots,X_n)$ 为 $\theta$ 的极大似然估计量。

3.  若 $\hat{\theta}(X_1,\dots,X_n)$ 为 $\theta$ 的极大似然估计量，则 $g(\theta)$ 的极大似然估计量为 $g\left(\hat{\theta}(X_1,\dots,X_n)\right)$。

## 估计量评选准则

### 无偏性准则

<span class="m-definition"></span> 若参数 $\theta$ 的估计量 $\hat{\theta}=\hat{\theta}(X_1,\dots,X_n)$ 满足 $$\begin{aligned}
E(\hat{\theta})=\theta
\end{aligned}$$ 则称 $\hat{\theta}$ 是 $\theta$ 的无偏估计量。



### 有效性准则

<span class="m-definition"></span> $\hat{\theta}_1，\hat{\theta}_2$ 是 $\theta$ 的两个无偏估计量，如果 $\forall \theta\in \Theta$ , $$\begin{aligned}
Var(\hat{\theta}_1)\le Var(\hat{\theta}_2)
\end{aligned}$$ 且不等号至少对某一 $\theta$ 成立，则称 $\hat{\theta}_1$ 比 $\hat{\theta}_2$ 有效。



### 均方误差准则

<span class="m-definition"></span> $Mse(\hat{\theta})=E\left(\hat{\theta}-\theta\right)^2$ 称为 $\hat{\theta}$ 关于 $\theta$ 的均方误差。$\hat{\theta}_1，\hat{\theta}_2$ 是 $\theta$ 的两个估计量，如果 $\forall \theta\in \Theta$ , $$\begin{aligned}
Mse(\hat{\theta}_1)\le Mse(\hat{\theta}_2)
\end{aligned}$$ 且不等号至少对某一 $\theta$ 成立，则称 $\hat{\theta}_1$ 优于 $\hat{\theta}_2$。



### 相合性准则

<span class="m-definition"></span> 设 $\hat{\theta}_n=\hat{\theta}(X_1,\dots,X_n)$ 为参数 $\theta$ 的估计量，若 $\forall \theta\in\Theta$，当 $n\rightarrow +\infty$，$$\begin{aligned}
\hat{\theta}_n\overset{P}{\longrightarrow}\theta
\end{aligned}$$ 即 $\forall \epsilon>0$ , $$\begin{aligned}
\lim_{n\rightarrow +\infty}P\left\{\left|\hat{\theta}_n-\theta\right|\ge \epsilon \right\}=0
\end{aligned}$$ 则称 $\hat{\theta}_n$ 为 $\theta$ 的 **相合估计量** 或 **一致估计量**。



## 置信区间

<span class="m-definition"></span> 设总体 $X$ 的分布函数 $F(x;\theta)$，$\theta$ 未知.对给定值 $\alpha(0<\alpha<1)$，有两个统计量 $\theta_L=\theta_L(X_1,\dots,X_n)$ , $\theta_U=\theta_U(X_1,\dots,X_n)$，使得 $$\begin{aligned}
P\left\{ \theta_L(X_1,\dots,X_n)<\theta<\theta_U(X_1,\dots,X_n) \right\}\ge 1-\alpha
\end{aligned}$$ 称 $\left(\theta_L,\theta_U\right)$ 是 $\theta$ 的 **置信水平** 为 $1-\alpha$ 的 **双侧置信区间**；$\theta_L,\theta_U$ 分别为 **双侧置信下限** 和 **双侧置信上限**。

若 $$\begin{aligned}
P\left\{ \theta_L(X_1,\dots,X_n)<\theta \right\}\ge 1-\alpha
\end{aligned}$$ 则称 $\theta_L$ 是 $\theta$ 的置信水平为 $1-\alpha$ 的 **单侧置信下限**。

若 $$\begin{aligned}
P\left\{ \theta<\theta_U(X_1,\dots,X_n) \right\}\ge 1-\alpha
\end{aligned}$$ 则称 $\theta_U$ 是 $\theta$ 的置信水平为 $1-\alpha$ 的 **单侧置信上限**。



## 正态总体均值，方差的置信区间与单侧置信限

<div class="table*">

|  | 待估参数 | 其他参数 | 枢轴量及分布 | 置信区间 | 单侧置信限 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 一个正态总体 | $\mu$ | $\sigma^2$ 已知 |  |  |  |
|  | $\mu$ | $\sigma^2$ 未知 |  |  |  |
|  | $\sigma^2$ | $\mu$ 未知 |  |  |  |
| 两个正态总体 | $\mu_1-\mu_2$ | $\sigma_1^2,\sigma_2^2$ 已知 |  |  |  |
|  | $\mu_1-\mu_2$ | $\sigma_1^2=\sigma_2^2$ 未知 |  |  |  |
|  | $\frac{\sigma_1^2}{\sigma_2^2}$ | $\mu_1,\mu_2$ 未知 |  |  |  |



注意区分是成对数据还是两正态总体数据
