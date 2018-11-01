# coding=utf-8

calc = lambda a: 1 if a <= 2 else (calc(a - 1) + calc(a - 2))


def cycling(times):
    r = [1, 1]
    while times > 2:
        times -= 1
        r.append(r[-1] + r[-2])
    return r


if __name__ == '__main__':
    print("递归法\n", [calc(i) for i in range(1, 20)])
    print("循环法\n", cycling(20))
