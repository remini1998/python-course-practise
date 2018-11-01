from enum import Enum


class StandardType(Enum):
    INNER = 1
    FOREIGN = 2


def bmi_calc(height: float, weight: float, standard: StandardType):
    bmi = weight / pow(height / 100, 2)
    standard = [18.5, 24, 28] if standard is StandardType.INNER else [18.5, 25, 30]
    if bmi < standard[0]:
        return bmi, "偏瘦"
    elif bmi < standard[1]:
        return bmi, "正常"
    elif bmi < standard[2]:
        return bmi, "偏胖"
    else:
        return bmi, "肥胖"


if __name__ == '__main__':
    w = float(input("请输入体重(kg):"))
    h = float(input("请输身高(cm):"))
    s = int(input("请选择标准，1为国内，2位国际:"))
    print("您的BMI指数为%.2f，经鉴定为%s" % bmi_calc(h, w, s))
