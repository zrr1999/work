# 詹荣瑞 18170100045 最优化作业



## 第一题

$$
\min_{t \ge0} \phi(t)=t^3-2t+1
$$
加步探索法：选取$t_0=0,h_0=1,\alpha=2$，计算$\phi(0)=2$，迭代如下
1. $t=1,h=1,\phi(1)=0<2$
2. $t=2,h=3,\phi(2)=22>2$

得到区间：$(1,3)$
实现代码：
```python
def method1(func, t, h, a):
    phi = func(t)
    t += h
    phi_ = func(t)
    if phi_ < phi:
        while phi_ < phi:
            print(h, t, phi_)
            h = a * h
            t += h
            phi = phi_
            phi_ = func(t)
        return t - h, t
    else:
        h = -h
        while phi_ < phi:
            print(h, t, phi_)
            h = a * h
            t += h
            phi = phi_
            phi_ = func(t)
        return t, t - h
```

## 第二题
$$
\min \phi(t)=t(t-3)
$$
导数
$$
\phi'(t)=2t-3
$$
对分法：初始区域$[a, b]=[-3, 5]$，精度$\epsilon=0.1$，计算$\phi'(-3)=-9<0<\phi'(5)=7$满足条件，迭代如下
1. $c=1,\phi'(1)=-1<2$
1. $c=3,\phi'(3)=3>2$
1. $c=2,\phi'(2)=1<2$
1. $c=1.5,\phi'(1.5)=0,\phi(1.5)=-2.25$

得到最小值：$\phi(1.5)=-2.25$
实现代码：
```python
def method2(func, d_func, a, b, epsilon):
    if d_func(a) < 0 < d_func(b):
        while abs(a - b) > epsilon:
            c = (a + b) / 2
            dfc = d_func(c)
            print(c, dfc)
            if dfc < 0:
                a = c
            elif dfc == 0:
                return c, func(c)
            else:
                b = c
        c = (a + b) / 2
        return c, func(c)
    else:
        return None
```

## 第三题
$$
\min \phi(t)=t^3-2t+1
$$
导数
$$
\phi'(t)=3t^2-2
$$
对分法：初始区域$[a, b]=[1, 3]$，精度$\epsilon=0.1$，计算$\phi'(1)=1>0,\phi'(3)=25>0$不满足条件。
实现代码：
```python
def method3(func, d_func, dd_func, a, b, epsilon):
    if d_func(a) < 0 < d_func(b):
        t = (a + b) / 2
        t_ = t - d_func(t) / dd_func(t)
        while abs(t - t_) > epsilon:
            t = t_
            t_ = t - d_func(t) / dd_func(t)
            dfc = d_func(t)
            print(t, dfc)
        return t, func(t)
    else:
        return None
```

## 第四题
$$
\min \phi(t)=t(t+2)
$$
对分法：初始区域$[a, b]=[-3, 5]$，精度$\epsilon=0.001$，迭代如下
$t_1 , t_2 , \phi_1 , \phi_2$
1.9440 0.0560 7.6671 0.1151
0.0560 -1.1114 0.1151 -0.9876
-1.1114 -1.8326 -0.9876 -0.3068
-0.6652 -1.1114 -0.8879 -0.9876
-1.1114 -1.3867 -0.9876 -0.8505
-0.9405 -1.1114 -0.9965 -0.9876
-0.8361 -0.9405 -0.9731 -0.9965
-0.9405 -1.0062 -0.9965 -1.0000
-1.0062 -1.0461 -1.0000 -0.9979
-0.9804 -1.0062 -0.9996 -1.0000
-1.0062 -1.0210 -1.0000 -0.9996
-0.9951 -1.0062 -1.0000 -1.0000
-0.9915 -0.9951 -0.9999 -1.0000
-0.9951 -1.0006 -1.0000 -1.0000
-1.0006 -1.0020 -1.0000 -1.0000
-0.9965 -1.0006 -1.0000 -1.0000
-1.0006 -0.9999 -1.0000 -1.0000

得到最小值：$\phi(-1.0002455325355535)=-0.999999939713774$
实现代码：
```python
def method4(func, a, b, epsilon, beta=0.382):
    t2 = a + beta * (b - a)
    t1 = a + b - t2
    phi1 = func(t1)
    phi2 = func(t2)
    while abs(t1 - t2) > epsilon:
        print("%.4f %.4f %.4f %.4f" % (t1, t2, phi1, phi2))
        if phi1 < phi2:
            a = t2
            t2 = t1
            phi2 = phi1
            t1 = a + b - t2
            phi1 = func(t1)
        else:
            b = t1
            t1 = t2
            phi1 = phi2
            t2 = a + beta * (b - a)
            phi2 = func(t2)
    t = (t1 + t2) / 2
    print("%.4f %.4f %.4f %.4f" % (t1, t2, phi1, phi2))
    return t, func(t)
```


## 第五题
$$
\min \phi(t)=8t^3-2t^2-7t+3
$$
导数
$$
\phi'(t)=2t-3
$$
对分法：初始区域$[a, b]=[0, 2]$，精度$\epsilon=0.001$，迭代如下
$t_1 ,t_0,t, t_2 $
0.0000 1.0000 0.5227 2.0000
1.0000 0.5227 0.6788 2.0000
1.0000 0.6788 0.6229 0.5227
0.6788 0.6229 0.6282 0.5227
0.6788 0.6282 0.6297 0.6229
0.6788 0.6297 0.6298 0.6282

得到最小值：$\phi(0.6297624685839073)=-0.2034245900373466$
实现代码：
```python
def method5(func, t1, t2, epsilon, beta=0.382):
    t0 = 1

    def _f(_a, _b, _c):
        return (_a ** 2 - _b ** 2) * func(_c)

    def _fi(_a, _b, _c):
        return (_a - _b) * func(_c)

    t = (_f(t0, t2, t1) + _f(t2, t1, t0) + _f(t1, t0, t2)) / 2
    t /= (_fi(t2, t1, t0) + _fi(t0, t2, t1) + _fi(t1, t0, t2))
    while abs(t - t0) > epsilon:
        print("%.4f %.4f %.4f %.4f" % (t1, t0, t, t2))
        phi, phi0 = func(t), func(t0)
        if t > t0:
            if phi < phi0:
                t2 = t0
                t0 = t
            else:
                t1 = t
        else:
            if phi < phi0:
                t1 = t0
                t0 = t
            else:
                t2 = t

        t = (_f(t0, t2, t1) + _f(t2, t1, t0) + _f(t1, t0, t2)) / 2
        t /= (_fi(t2, t1, t0) + _fi(t0, t2, t1) + _fi(t1, t0, t2))
    print("%.4f %.4f %.4f %.4f" % (t1, t0, t, t2))
    return t, func(t)
```

