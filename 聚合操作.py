import time
import numpy as np


def main():
    np.random.seed(int(time.time()))
    a = np.random.randint(1, 20, (3, 3))
    print(a)
    # Output:
    # [[11 14  4]
    #  [11 15 14]
    #  [10  9 15]]

    # 计算所有元素的总和
    data = a.sum()
    print(data)
    # Output:
    # 103

    # 计算所有元素中的最大值
    data = a.max()
    print(data)
    # Output:
    # 15

    # 计算所有元素中的最小值
    data = a.min()
    print(data)
    # Output:
    # 4

    # 计算数组 a 的 累积和（cumulative sum）的函数
    # 它会返回一个数组，其中的每个元素是原数组从第一个元素到当前位置元素的累计和。
    data = a.cumsum()
    print(data)
    # Output:
    # [ 11  25  29  40  55  69  79  88 103]

    # 计算数组的均值（平均值）
    data = a.mean()
    print(data)
    # Output:
    # 11.444444444444445

    # 计算数组的中位数
    data = np.median(a)
    print(data)
    # Output:
    # 11.0

    # 计算数组 a 的皮尔逊相关系数矩阵，即每对变量之间的线性相关性
    data = np.corrcoef(a)
    print(data)
    # Output:
    # [[ 1.          0.01560216 -0.99015159]
    #  [ 0.01560216  1.          0.12453387]
    #  [-0.99015159  0.12453387  1.        ]]

    # 计算数组的方差
    data = np.var(a)
    print(data)
    # Output:
    # 11.358024691358025

    # 计算数组的标准差
    data = np.std(a)
    print(data)
    # Output:
    # 3.3701668640229117


if __name__ == '__main__':
    main()
