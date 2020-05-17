# 加步探索法
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
        print(h, t, phi_)
        return t - h, t
    else:
        h = -h
        while phi_ < phi:
            print(h, t, phi_)
            h = a * h
            t += h
            phi = phi_
            phi_ = func(t)
        print(h, t, phi_)
        return t, t - h


# 对分法
def method2(func, d_func, a, b, epsilon):
    if d_func(a) < 0 < d_func(b):
        while abs(a - b) > epsilon:
            c = (a + b) / 2
            dfc = d_func(c)
            print(a, b, c, dfc)
            if dfc < 0:
                a = c
            elif dfc == 0:
                return c, func(c)
            else:
                b = c
        print(abs(a - b))
        c = (a + b) / 2
        return c, func(c)
    else:
        return None


# 牛顿法
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


# 黄金分割法
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


print("第一题:", method1(lambda _t: _t ** 3 - 2 * _t + 1, 0, 1, 2))
print("第二题:", method2(lambda _t: _t * (_t - 3), lambda _t: 2 * _t - 3, -3, 5, 0.1))
print("第三题:", method3(lambda _t: _t ** 3 - 2 * _t + 1, lambda _t: 3 * _t ** 2 - 2,
                      lambda _t: 6 * _t, 1, 3, 0.1))
print("第四题:", method4(lambda _t: _t * (_t + 2), -3, 5, 0.001))
print("第五题:", method5(lambda _t: 8 * _t ** 3 - 2 * _t ** 2 - 7 * _t + 3, 0, 2, 0.001))
