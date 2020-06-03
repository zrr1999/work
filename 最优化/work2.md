# 詹荣瑞 18170100045 最优化作业

算法全部采用Python3.7实现，仅使用了Numpy库用来进行向量运算。

## 第1题

$$
\min_{t \ge0} f(X)=x_1^2+25x_2^2=X^T\left(\array{1&0\\0&25}\right)X
$$
梯度
$$
g_k=\nabla f(X_k)=\left(\array{2&0\\0&50}\right)X_k
$$
记
$$
A=\left(\array{2&0\\0&50}\right)
$$
则最速下降法迭代公式
$$
X_{k+1}=X_k-\frac{g_k^Tg_k}{g_k^TAg_k}g_k
$$


最速下降法：选取$X_0=[2, 2]^T,\epsilon=0.01$，迭代如下

1. $X_k=\left(\array{2\\2}\right),g_k=\left(\array{4\\100}\right)$
2. $X_k=\left(\array{1.920\\-0.003}\right),g_k=\left(\array{3.839\\-0.153}\right)$
3. $X_k=\left(\array{0.071\\0.071}\right),g_k=\left(\array{0.142\\3.544}\right)$
4. $X_k=\left(\array{0.058\\0.0001}\right),g_k=\left(\array{0.136\\-0.005}\right)$

得到最小值：$f(\left(\array{0.0025\\0.0025}\right))=0.000164$
实现代码：

```python
def method1(a, b, x, epsilon):
    df = a@x
    dx = df.T @ df / (df.T @ a @ df) * df
    while np.linalg.norm(dx) > epsilon:
        print(x, df)
        x = x - dx
        df = a@x
        dx = df.T@df/(df.T@a@df)*df
    return x, x.T@a@x/2+b
print("第1题:", method1(np.array([[2, 0], [0, 50]]), 0, np.array([[2], [2]]), 0.01))
```

## 第2题
$$
\min_{t \ge0} f(X)=-10x_1-4x_2+x_1^2+x_2^2-x_1x_2+60=X^T\left(\array{1&-0.5\\-0.5&1}\right)X+\left(\array{-10\\-4}\right)^TX+60
$$
梯度
$$
g_k=\nabla f(X_k)=\left(\array{2&-1\\-1&2}\right)X_k+\left(\array{-10\\-4}\right)
$$
Hesse矩阵
$$
G_k=\nabla^2 f(X_k)=\left(\array{2&-1\\-1&2}\right)
$$
记
$$
A=\left(\array{2&-1\\-1&2}\right),\omega=\left(\array{-10\\-4}\right),b=60
$$
牛顿法：选取$X_0=[0, 0]^T,\epsilon=0.01$，迭代如下

1. $X_k=\left(\array{0\\0}\right),g_k=\left(\array{-10\\-4}\right)$
2. $X_k=\left(\array{8\\6}\right),g_k=\left(\array{-1.776\times 10^{-15}\\8.8818\times 10^{-16}}\right)$

得到最小值：$f(\left(\array{8\\6}\right))=8$
实现代码：

```python
def method2(a, w, b, x, epsilon):
    ai = np.linalg.inv(a)
    print(ai)
    aiw = -ai@w
    df = a@x + w
    while np.linalg.norm(df) > epsilon:
        df = a@x + w
        print(x, df)
        p = aiw-x
        dx = (-w.T@p) / (x.T@a@x+2*w.T@x+w.T@ai@w) * p
        x = x + dx
    return x, x.T@a@x/2+w.T@x+b
print("第2题:", method2(np.array([[2, -1], [-1, 2]]), np.array([[-10], [-4]]),
                       60, np.array([[0], [0]]), 0.01))
```
## 第3题
$$
\begin{align}
\min_{t \ge0} f(X)&=4(x_1+1)^2+2(x_2-1)^2+x_1+x_2+10\\
&=4(x_1^2+2x_1+1)+2(x_2^2-2x_2+1)+x_1+x_2+10\\
&=4x_1^2+2x_2^2+9x_1-3x_2+16\\
&=X^T\left(\array{4&0\\0&2}\right)X+\left(\array{9\\-3}\right)^TX+16\\
\end{align}
$$
梯度
$$
g_k=\nabla f(X_k)=\left(\array{8&0\\0&4}\right)X_k+\left(\array{9\\-3}\right)
$$
Hesse矩阵
$$
G_k=\nabla^2 f(X_k)=\left(\array{8&0\\0&4}\right)
$$
记
$$
A=\left(\array{8&0\\0&4}\right),\omega=\left(\array{9\\-3}\right),b=16
$$
搜索方向
$$
P_k=-G_k^{-1}g_k=-A^{-1}(AX_k+\omega)=-X_k-A^{-1}\omega
$$
寻找最优步长，设步长$t_k$，则
$$
\begin{align}
f(X_k+t_kP_k)
&=f(X_k)+\frac1 2t_k^2P_k^TAP_k+t_kP_k^TAX+t_k\omega^TP_k\\
&=f(X_k)+\frac1 2t_k^2P_k^TAP_k+t_k(X^TA+\omega^T)P_k\\
\end{align}
$$
对$t_k$求导
$$
\begin{align}
\frac {\partial f(X_k+t_kP_k)}{\partial t_k}
&=t_kP_k^TAP_k+(X^TA+\omega^T)P_k\\
\end{align}
$$
令 $\frac {\partial f(X_k+t_kP_k)}{\partial t_k}=0$ 得 $t_k=-\frac{(X^TA+\omega^T)P_k}{P_k^TAP_k}$

修正牛顿法：选取$X_0=[0, 0]^T,\epsilon=0.01$，迭代如下

1. $X_k=\left(\array{0.0000\\0.0000}\right),g_k=\left(\array{9.0000\\-3.0000}\right)$

2. $X_k=\left(\array{-1.1250\\0.7500}\right),g_k=\left(\array{0.0000\\0.0000}\right)$

得到最小值：$f(\left(\array{-1.125\\0.75}\right))=9.8125$
实现代码：

```python
def method3(a, w, b, x, epsilon):
    ai = np.linalg.inv(a)
    aiw = -ai @ w
    while True:
        df = a @ x + w
        print(r"$X_k=\left(\array{"
              f"{x[0][0]:.4f}"r"\\"f"{x[1][0]:.4f}"
              r"}\right),g_k=\left(\array{"
              f"{df[0][0]:.4f}"r"\\"f"{df[1][0]:.4f}"
              r"}\right)$""\n")
        if np.linalg.norm(df) < epsilon:
            break
        p = aiw - x
        dx = (-(x.T@a+w.T) @ p) / (p.T @ a @ p) * p
        x = x + dx
    return x, x.T @ a @ x / 2 + w.T @ x + b
print("第3题:", method3(np.array([[8, 0], [0, 4]]), np.array([[9], [-3]]),
                      16, np.array([[0], [0]]), 0.01))
```

## 第4题

$$
\begin{align}
\min_{t \ge0} f(X)&=x_1^2+4x_2^2\\
&=X^T\left(\array{1&0\\0&4}\right)X\\
\end{align}
$$

梯度
$$
g_k=\nabla f(X_k)=\left(\array{2&0\\0&8}\right)X_k
$$
记
$$
A=\left(\array{2&0\\0&8}\right)
$$
搜索方向
$$
P_k=-g_k=-AX_k
$$
寻找最优步长，设步长$t_k$，则
$$
\begin{align}
f(X_k+t_kP_k)
&=\frac 1 2(X_k-t_kAX)^TA(X-t_kAX_k)\\
&=\frac 1 2 X_k^T(1-t_kA)^TA(1-t_kA)X_k\\
&=\frac 1 2 X_k^T(1-t_kA)(A-t_kA^2)X_k\\
&=\frac 1 2 X_k^T(A-2t_kA^2+t_k^2A^3)X_k\\
\end{align}
$$
对$t_k$求导
$$
\begin{align}
\frac {\partial f(X_k+t_kP_k)}{\partial t_k}
&= -X_k^TA^2X_k+t_kX_k^TA^3X_k\\
\end{align}
$$
令 $\frac {\partial f(X_k+t_kP_k)}{\partial t_k}=0$ 得 $t_k=\frac{X^TA^2X}{X^TA^3X}$

共轭梯度法：选取$X_0=[1, 1]^T,\epsilon=0.01$，迭代如下

1. $X_k=\left(\array{1.0000\\1.0000}\right),g_k=\left(\array{2.0000\\8.0000}\right)$

1. $X_k=\left(\array{0.7385\\-0.0462}\right),g_k=\left(\array{1.4769\\-0.3692}\right)$

1. $X_k=\left(\array{0.1108\\0.1108}\right),g_k=\left(\array{0.2215\\0.8862}\right)$

1. $X_k=\left(\array{0.0818\\-0.0051}\right),g_k=\left(\array{0.1636\\-0.0409}\right)$

1. $X_k=\left(\array{0.0123\\0.0123}\right),g_k=\left(\array{0.0245\\0.0982}\right)$

1. $X_k=\left(\array{0.0091\\-0.0006}\right),g_k=\left(\array{0.0181\\-0.0045}\right)$

1. $X_k=\left(\array{0.0014\\0.0014}\right),g_k=\left(\array{0.0027\\0.0109}\right)$

1. $X_k=\left(\array{0.0010\\-0.0001}\right),g_k=\left(\array{0.0020\\-0.0005}\right)$

得到最小值：$f(\left(\array{0.001\\0.00001}\right))=1.02\times 10^{-6}$
实现代码：

```python
def method4(a, w, b, x, epsilon):
    while True:
        df = a@x + w
        print(r"$X_k=\left(\array{"
              f"{x[0][0]:.4f}"r"\\"f"{x[1][0]:.4f}"
              r"}\right),g_k=\left(\array{"
              f"{df[0][0]:.4f}"r"\\"f"{df[1][0]:.4f}"
              r"}\right)$""\n")
        if np.linalg.norm(df) < epsilon:
            break
        p = -df
        a2 = a@a
        a3 = a2@a
        t = (x.T@a2@x)/(x.T@a3@x)
        x = x + t*p
    return x, x.T@a@x/2+w.T@x+b
print("第4题:", method4(np.array([[2, 0], [0, 8]]), np.array([[0], [0]]),
                      0, np.array([[1], [1]]), 0.01))
```

## 第6题

$$
\begin{align}
\min_{t \ge0} f(X)&=4(x_1-5)^2+2(x_2-1)^2\\
&=4(x_1^2-10x_1+25)+2(x_2^2-2x_2+1)\\
&=4x_1^2+2x_2^2-40x_1-4x_2+102\\
&=X^T\left(\array{4&0\\0&2}\right)X+\left(\array{-40\\-4}\right)^TX+102\\
\end{align}
$$

梯度
$$
g_k=\nabla f(X_k)=\left(\array{8&0\\0&4}\right)X_k+\left(\array{-40\\-4}\right)
$$
记
$$
A=\left(\array{8&0\\0&4}\right),\omega=\left(\array{-40\\-4}\right),b=102
$$
搜索方向
$$
P_k=-H_kg_k
$$
寻找最优步长，设步长$t_k$，与第三题结果相同
$$
t_k=-\frac{(X^TA+\omega^T)P_k}{P_k^TAP_k}
$$
DFP：选取$X_0=[8, 9]^T,\epsilon=0.01$，迭代如下

1. $X_0=\left(\array{8.0000\\9.0000}\right),g_0=\left(\array{24.0000\\32.0000}\right)$
1. $X_1=\left(\array{3.5882\\3.1176}\right),g_1=\left(\array{-11.2941\\8.4706}\right)$
1. $X_2=\left(\array{5.0000\\1.0000}\right),g_2=\left(\array{0.0000\\-0.0000}\right)$

得到最小值：$f(\left(\array{5.000\\1.000}\right))=0.0$

实现代码：

```python
def method5(a, w, b, x, epsilon):
    k = 0
    h = np.eye(a.shape[0])
    while True:
        df = a @ x + w
        print(r"1. $X_"f"{k}"r"=\left(\array{"
              f"{x[0][0]:.4f}"r"\\"f"{x[1][0]:.4f}"
              r"}\right),g_"f"{k}"r"=\left(\array{"
              f"{df[0][0]:.4f}"r"\\"f"{df[1][0]:.4f}"
              r"}\right)$")
        if np.linalg.norm(df) < epsilon:
            break
        p = -h@df
        t = (-(x.T@a+w.T) @ p) / (p.T @ a @ p)
        s = t * p
        x = x + s
        k += 1
        y = a @ s
        h += s@s.T/(s.T@y) - h@y@y.T@h/(y.T@h@y)
    return x, x.T @ a @ x / 2 + w.T @ x + b
x, f = method5(np.array([[8, 0], [0, 4]]), np.array([[-40], [-4]]),
                        102, np.array([[8], [9]]), 0.01)
print("\n得到最小值："r"$f(\left(\array{"f"{x[0][0]:.4f}"
      r"\\"f"{x[1][0]:.4f}"r"}\right))="f"{f[0][0]:.4f}"r"$")
```

## 第7题

$$
\begin{align}
\min_{t \ge0} f(X)&=x_1^2+x_2^2-x_1x_2-10x_1-4x_2+60\\
&=X^T\left(\array{1&-0.5\\-0.5&1}\right)X+\left(\array{-10\\-4}\right)^TX+60\\
\end{align}
$$

记
$$
A=\left(\array{2&-1\\-1&2}\right),\omega=\left(\array{-10\\-4}\right),b=60
$$
搜索方向
$$
P_k^{(i)}=e_i(i=0,1,2......)
$$
寻找最优步长，设步长$t_k$，与第三题结果相同
$$
t_k=-\frac{(X^TA+\omega^T)P_k}{P_k^TAP_k}
$$
坐标轮换法：选取$X_0=[0, 0]^T,\epsilon=0.01$，迭代如下
1. $X_0=\left(\array{8.0000\\9.0000}\right),f(X_0)=59.0000$
1. $X_1=\left(\array{9.5000\\6.7500}\right),f(X_1)=51.6875$
1. $X_2=\left(\array{8.3750\\6.1875}\right),f(X_2)=50.1055$
1. $X_3=\left(\array{8.0938\\6.0469}\right),f(X_3)=50.0066$
1. $X_4=\left(\array{8.0234\\6.0117}\right),f(X_4)=50.0004$

得到最小值：$f(\left(\array{8.0059\\6.0029}\right))=50.0000$

实现代码：

```python
def method6(a, w, b, x, epsilon):
    k = 0
    while True:
        f = x.T @ a @ x / 2 + w.T @ x + b
        print(r"1. $X_"f"{k}"r"=\left(\array{"
              f"{x[0][0]:.4f}"r"\\"f"{x[1][0]:.4f}"
              r"}\right),f(X_"f"{k}"f")={f[0][0]:.4f})$")
        ps = np.array([[[1], [0]], [[0], [1]]])
        s = 0
        for p in ps:
            t = (-(x.T @ a + w.T) @ p) / (p.T @ a @ p)
            s = t * p
            x = x + s
        if np.linalg.norm(s) < epsilon:
            break
        k += 1
    return x, x.T @ a @ x / 2 + w.T @ x + b
x, f = method6(np.array([[2, -1], [-1, 2]]), np.array([[-10], [-4]]),
               102, np.array([[8], [9]]), 0.01)
print("\n得到最小值："r"$f(\left(\array{"f"{x[0][0]:.4f}"
      r"\\"f"{x[1][0]:.4f}"r"}\right))="f"{f[0][0]:.4f}"r"$")
```

## 第8题

$$
\begin{align}
\min_{t \ge0} f(X)&=x_1^2+2x_2^2-4x_1-8x_2+5\\
&=X^T\left(\array{1&0\\0&2}\right)X+\left(\array{-4\\-8}\right)^TX+5\\
\end{align}
$$

记
$$
A=\left(\array{2&0\\0&4}\right),\omega=\left(\array{-4\\-8}\right),b=5
$$
**题目给的 $\epsilon$ 有点大，结果离最优值有点远**

单纯形法：选取$X_0=[0, 0]^T,X_1=[0.965,0.259]^T,X_2=[0.259, 0.965]^T,\epsilon=0.1$，迭代如下

1. $X_H=\left(\array{1.2852\\1.2852}\right),f(X_H)=-5.4672$
1. $X_H=\left(\array{1.9912\\0.5792}\right),f(X_H)=-2.9626$
1. $X_H=\left(\array{2.3787\\1.6727}\right),f(X_H)=-6.6423$
1. $X_H=\left(\array{3.0847\\0.9667}\right),f(X_H)=-3.6880$
1. $X_H=\left(\array{3.4722\\2.0602}\right),f(X_H)=-4.8253$
1. $X_H=\left(\array{2.7662\\2.7662}\right),f(X_H)=-5.2386$
1. $X_H=\left(\array{1.6727\\2.3787}\right),f(X_H)=-6.6060$
1. $X_H=\left(\array{1.7295\\1.7295}\right),f(X_H)=-6.7805$

得到最小值：$f(\left(\array{2.3787\\1.6727}\right))=-6.6423$

实现代码：

```python
def method7(a, w, b, xs, epsilon, alpha, beta):
    def func(x):
        return x.T @ a @ x / 2 + w.T @ x + b

    k = 0
    xh, xg, xl = (x for x in xs)
    fh, fg, fl = (func(x) for x in xs)

    while True:
        if fl > fg:
            fg, fl = fl, fg
            xg, xl = xl, xg
        if fh < fg:
            if fh < fl:
                fh, fl = fl, fh
                xh, xl = xl, xh
            else:
                fg, fh = fh, fg
                xg, xh = xh, xg
        x1 = (xg + xl) / 2
        x2 = 2 * x1 - xh
        f2 = func(x2)
        if f2 < fl:
            x3 = x1 + alpha * (x2 - x1)
            if func(x3) < f2:
                xh = x3
            else:
                xh = x2
        elif fl <= f2 < fg:
            xh = x2
        elif fg <= f2 < fh:
            x4 = x1 + beta * (x2 - x1)
            xh = x4
        else:
            x5 = x1 + beta * (xh - x1)
            if func(x5) >= fh:
                xs = (xs + xl) / 2
            else:
                xh = x5
        fh = func(xh)
        print(r"1. $X_H=\left(\array{"
              f"{xh[0][0]:.4f}"r"\\"f"{xh[1][0]:.4f}"
              r"}\right),f(X_H)="f"{fh[0][0]:.4f}$")
        if (fh - fl)**2+(fg - fl)**2 <= epsilon:
            break
        k += 1
    return xl, fl
x, f = method7(np.array([[2, 0], [0, 4]]), np.array([[-4], [-8]]),
               5, np.array([[[0], [0]], [[0.965], [0.259]], [[0.259], [0.965]]]), 0.1, 1.1, 0.4)
print("\n得到最小值："r"$f(\left(\array{"f"{x[0][0]:.4f}"
      r"\\"f"{x[1][0]:.4f}"r"}\right))="f"{f[0][0]:.4f}"r"$")
```



