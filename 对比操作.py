import time
import numpy as np


def main():
    np.random.seed(int(time.time()))
    a = np.random.randint(1, 50, (7, 5))
    print(a)
    # Output:
    # [[11 43 39  7 22]
    #  [17  4 14 45 27]
    #  [13 43 36 28 27]
    #  [ 2  6 45 43 34]
    #  [32 30 11 22 34]
    #  [12  2 32 21 35]
    #  [46 13 33 37 25]]

    b = np.array([(1, 2, 3), (4, 5, 6)])
    c = np.array([(1, 2, 3), (4, 5, 6)])
    d = np.array([(1, 2, 3), (6, 6, 6)])

    # 逐元素地对比数组 b 和 c 中的对应元素, 成立返回 True，否则返回 False
    result = b == c
    print(result)
    # Output:
    # [[ True  True  True]
    #  [ True  True  True]]

    # 逐元素地对比数组 b 和 c 中的对应元素, 成立返回 True，否则返回 False
    result = b != c
    print(result)
    # Output:
    # [[False False False]
    #  [False False False]]

    # 逐元素地对比数组 a 的元素, 成立返回 True，否则返回 False
    result = a < 25
    print(result)
    # Output:
    # [[ True False False  True  True]
    #  [ True  True  True False False]
    #  [ True False False False False]
    #  [ True  True False False False]
    #  [False False  True  True False]
    #  [ True  True False  True False]
    #  [False  True False False False]]

    # 逐元素地比较两个数组 b 和 c 是否相等，相等返回 True，不相等返回 False
    result = np.equal(b, c)
    print(result)
    # Output:
    # [[ True  True  True]
    #  [ True  True  True]]

    # 逐元素地比较两个数组 b 和 c 是否相等，相等返回 True，不相等返回 False
    result = np.equal(c, d)
    print(result)
    # Output:
    # [[ True  True  True]
    #  [False False  True]]


if __name__ == '__main__':
    main()
