import numpy as np


# 最速下降法
def method1(a, b, x, epsilon):
    df = a @ x
    dx = df.T @ df / (df.T @ a @ df) * df
    while np.linalg.norm(dx) > epsilon:
        print(x, df)
        x = x - dx
        df = a @ x
        dx = df.T @ df / (df.T @ a @ df) * df
    return x, x.T @ a @ x / 2 + b


# 牛顿法
def method2(a, w, b, x, epsilon):
    ai = np.linalg.inv(a)
    print(ai)
    aiw = -ai @ w
    df = a @ x + w
    while np.linalg.norm(df) > epsilon:
        df = a @ x + w
        print(x, df)
        p = aiw - x
        x = x + p
    return x, x.T @ a @ x / 2 + w.T @ x + b


# 修正牛顿法
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
        dx = (-(x.T @ a + w.T) @ p) / (p.T @ a @ p) * p
        x = x + dx
    return x, x.T @ a @ x / 2 + w.T @ x + b


# 共轭梯度法
def method4(a, w, b, x, epsilon):
    while True:
        df = a @ x + w
        print(r"$X_k=\left(\array{"
              f"{x[0][0]:.4f}"r"\\"f"{x[1][0]:.4f}"
              r"}\right),g_k=\left(\array{"
              f"{df[0][0]:.4f}"r"\\"f"{df[1][0]:.4f}"
              r"}\right)$""\n")
        if np.linalg.norm(df) < epsilon:
            break
        p = -df
        a2 = a @ a
        a3 = a2 @ a
        t = (x.T @ a2 @ x) / (x.T @ a3 @ x)
        x = x + t * p
    return x, x.T @ a @ x / 2 + w.T @ x + b


# DFP
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
        p = -h @ df
        t = (-(x.T @ a + w.T) @ p) / (p.T @ a @ p)
        s = t * p
        x = x + s
        k += 1
        y = a @ s
        h += s @ s.T / (s.T @ y) - h @ y @ y.T @ h / (y.T @ h @ y)

    return x, x.T @ a @ x / 2 + w.T @ x + b


# 坐标轮换法
def method6(a, w, b, x, epsilon):
    k = 0
    while True:
        f = x.T @ a @ x / 2 + w.T @ x + b
        print(r"1. $X_"f"{k}"r"=\left(\array{"
              f"{x[0][0]:.4f}"r"\\"f"{x[1][0]:.4f}"
              r"}\right),f(X_"f"{k}"f")={f[0][0]:.4f}$")
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


# 单纯形法
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


# print("第1题:", method1(np.array([[2, 0], [0, 50]]), 0, np.array([[2], [2]]), 0.01))
# print("第2题:", method2(np.array([[2, -1], [-1, 2]]), np.array([[-10], [-4]]),
#                       60, np.array([[0], [0]]), 0.01))
# print("第3题:", method3(np.array([[8, 0], [0, 4]]), np.array([[9], [-3]]),
#                       16, np.array([[0], [0]]), 0.01))
# print("第4题:", method4(np.array([[2, 0], [0, 8]]), np.array([[0], [0]]),
#                       0, np.array([[1], [1]]), 0.01))

# 第6题
# x, f = method5(np.array([[8, 0], [0, 4]]), np.array([[-40], [-4]]),
#                         102, np.array([[8], [9]]), 0.01)
# print("\n得到最小值："r"$f(\left(\array{"f"{x[0][0]:.4f}"
#       r"\\"f"{x[1][0]:.4f}"r"}\right))="f"{f[0][0]:.4f}"r"$")

# 第7题
# x, f = method6(np.array([[2, -1], [-1, 2]]), np.array([[-10], [-4]]),
#                102, np.array([[8], [9]]), 0.01)
# print("\n得到最小值："r"$f(\left(\array{"f"{x[0][0]:.4f}"
#       r"\\"f"{x[1][0]:.4f}"r"}\right))="f"{f[0][0]:.4f}"r"$")

# 第8题
x, f = method7(np.array([[2, 0], [0, 4]]), np.array([[-4], [-8]]),
               5, np.array([[[0], [0]], [[0.965], [0.259]], [[0.259], [0.965]]]), 0.1, 1.1, 0.4)
print("\n得到最小值："r"$f(\left(\array{"f"{x[0][0]:.4f}"
      r"\\"f"{x[1][0]:.4f}"r"}\right))="f"{f[0][0]:.4f}"r"$")
