import time
import numpy as np


def main():
    np.random.seed(int(time.time()))
    a = np.random.randint(1, 20, (2, 2))
    print(a)
    # Output:
    # [[19  6]
    #  [19 18]]
    b = np.random.randint(1, 20, (2, 2))
    print(b)
    # Output:
    # [[19 18]
    #  [17  2]]

    # 逐元素相减
    data = a - b
    print(data)
    # Output:
    # [[  0 -12]
    #  [  2  16]]

    # 同 a - b
    data = np.subtract(a, b)
    print(data)
    # Output:
    # [[  0 -12]
    #  [  2  16]]

    # 逐元素相加
    data = a + b
    print(data)
    # Output:
    # [[38 24]
    #  [36 20]]

    # 同 a + b
    data = np.add(a, b)
    print(data)
    # Output:
    # [[38 24]
    #  [36 20]]

    # 逐元素相除
    data = a / b
    print(data)
    # Output:
    # [[1.         0.33333333]
    #  [1.11764706 9.        ]]

    # 同 a / b
    data = np.divide(a, b)
    print(data)
    # Output:
    # [[1.         0.33333333]
    #  [1.11764706 9.        ]]

    # 逐元素相乘
    data = a * b
    print(data)
    # Output:
    # [[361 108]
    #  [323  36]]

    # 同 a * b
    data = np.multiply(a, b)
    print(data)
    # Output:
    # [[361 108]
    #  [323  36]]

    # 计算两个数组的点积, 一维数组计算向量的点积，二维数组执行线性代数的矩阵乘法
    data = a @ b
    print(data)
    # Output:
    # [[463 354]
    #  [667 378]]

    # 同 a @ b
    data = a.dot(b)
    print(data)
    # Output:
    # [[463 354]
    #  [667 378]]

    # 计算数组 a 中每个元素的 指数（e 的幂次方）
    data = np.exp(a)
    print(data.astype(np.int64))
    # Output:
    # [[178482300       403]
    #  [178482300  65659969]]

    # 计算数组 a 中每个元素的 2 的幂（即 2^x）
    data = np.exp2(a)
    print(data.astype(np.int64))
    # Output:
    # [[524288     64]
    #  [524288 262144]]

    # 计算数组 a 中每个元素的平方根
    data = np.sqrt(a)
    print(data)
    # Output:
    # [[4.35889894 2.44948974]
    #  [4.35889894 4.24264069]]

    # 计算每个元素的正弦值
    data = np.sin(a)
    print(data)
    # Output:
    # [[ 0.14987721 -0.2794155 ]
    #  [ 0.14987721 -0.75098725]]

    # 计算每个元素的余弦值
    data = np.cos(a)
    print(data)
    # Output:
    # [[0.98870462 0.96017029]
    #  [0.98870462 0.66031671]]

    # 计算每个元素的自然对数
    data = np.log(a)
    print(data)
    # Output:
    # [[2.94443898 1.79175947]
    #  [2.94443898 2.89037176]]

    # 计算每个元素的平方
    data = np.power(a, 2)
    print(data)
    # Output:
    # [[361  36]
    #  [361 324]]


if __name__ == '__main__':
    main()
