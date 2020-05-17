import numpy as np


# 最速下降法
def method1(a, b, x, epsilon):
    df = a@x
    dx = df.T @ df / (df.T @ a @ df) * df
    while np.linalg.norm(dx) > epsilon:
        print(x, df)
        x = x - dx
        df = a@x
        dx = df.T@df/(df.T@a@df)*df
    return x, x.T@a@x/2+b


# 牛顿法
def method2(a, w, b, x, epsilon):
    ai = np.linalg.inv(a)
    print(ai)
    aiw = -ai@w
    df = a@x + w
    while np.linalg.norm(df) > epsilon:
        df = a@x + w
        print(x, df)
        p = aiw-x
        x = x + p
    return x, x.T@a@x/2+w.T@x+b


# 修正牛顿法
def method3(a, w, b, x, epsilon):
    ai = np.linalg.inv(a)
    print(ai)
    aiw = -ai@w
    while True:
        df = a@x + w
        print(x, df)
        if np.linalg.norm(df) < epsilon:
            break
        p = aiw-x
        dx = (-w.T@p) / (x.T@a@x+2*w.T@x+w.T@ai@w) * p
        x = x + dx
    return x, x.T@a@x/2+w.T@x+b


# 共轭梯度法
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


# 抛物线插值法
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


# print("第1题:", method1(np.array([[2, 0], [0, 50]]), 0, np.array([[2], [2]]), 0.01))
# print("第2题:", method2(np.array([[2, -1], [-1, 2]]), np.array([[-10], [-4]]),
#                       60, np.array([[0], [0]]), 0.01))
# print("第3题:", method3(np.array([[8, 0], [0, 4]]), np.array([[9], [-3]]),
#                       16, np.array([[0], [0]]), 0.01))
print("第4题:", method4(np.array([[2, 0], [0, 8]]), np.array([[0], [0]]),
                      0, np.array([[1], [1]]), 0.01))
# print("第四题:", method4(lambda _t: _t * (_t + 2), -3, 5, 0.001))
# print("第五题:", method5(lambda _t: 8 * _t ** 3 - 2 * _t ** 2 - 7 * _t + 3, 0, 2, 0.001))
