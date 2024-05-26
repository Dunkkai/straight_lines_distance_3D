def tr(a):
    a1 = a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
    a2 = -1 * a[0][1] * (a[1][0] * a[2][2] - a[2][0] * a[1][2])
    a3 = a[0][2] * (a[1][0] * a[2][1] - a[2][0] * a[1][1])

    return a1, a2, a3


a = list(map(float,input("Введите координаты точки А в формате 'x y z' ").replace(',','.').split()))
b = list(map(float,input("Введите координаты точки B в формате 'x y z' ").replace(',','.').split()))
c = list(map(float,input("Введите координаты точки C в формате 'x y z' ").replace(',','.').split()))
d = list(map(float,input("Введите координаты точки D в формате 'x y z' ").replace(',','.').split()))
ed = [1, 1, 1]



v_ab = [bi - ai for ai, bi in zip(a, b)]
v_cd = [di - ci for ci, di in zip(c, d)]
v_ad = [di - ai for ai, di in zip(a, d)]

if v_ab == v_cd:
    v_ca = [ai - ci for ci, ai in zip(c, a)]
    Sacd2 = [ed,
             v_ab,
             v_ca]
    Sacd_2 = sum([x ** 2 for x in tr(Sacd2)]) ** 0.5
    h = (sum([x ** 2 for x in v_ab]) ** 0.5)
    ans = Sacd_2 / h
    if ans == 0:
        print(f'Прямая AB совпадает с прямой CD, расстояние между ними:\n{ans}')
    else:
        print(f'Прямая AB параллельна прямой CD, расстояние между ними:\n{ans}')
else:
    V_par = [v_ab,
             v_cd,
             v_ad]
    V_par = abs(sum(tr(V_par)))

    S_osn = [ed,
             v_ab,
             v_cd]

    S_osn = sum([x ** 2 for x in tr(S_osn)]) ** 0.5

    if V_par == 0:
        print(f'Прямые AB и CD пересекаются, значит расстояние между ними равно:\n{V_par / S_osn}')
    else:
        print(f'Расстояние от прямой AB до прямой CD: \n{V_par / S_osn}')
