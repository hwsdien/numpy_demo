import time
import numpy as np


def main():
    np.random.seed(int(time.time()))
    a = np.random.randint(1, 50, (3, 3))
    print(a)
    # Output:
    # [[10 17  1]
    #  [31 11  3]
    #  [33 32 12]]

    # 创建数组视图，视图和原数据共享相同的内存数据
    b = a.view()
    print(b)
    # Output:
    # [[10 17  1]
    #  [31 11  3]
    #  [33 32 12]]
    b[0, 0] = 100
    print(a)
    # Output:
    # [[100  17   1]
    #  [ 31  11   3]
    #  [ 33  32  12]]

    # 创建数组副本，独立的新数组，修改不影响原数组
    c = np.copy(a)
    print(c)
    # Output:
    # [[100  17   1]
    #  [ 31  11   3]
    #  [ 33  32  12]]
    c[1, 0] = 200
    print(c)
    # Output:
    # [[100  17   1]
    #  [200  11   3]
    #  [ 33  32  12]]
    print(a)
    # Output:
    # [[100  17   1]
    #  [ 31  11   3]
    #  [ 33  32  12]]

    # 是 np.copy(a) 的简写形式，创建数组副本，属于深拷贝
    d = a.copy()
    d[2, 0] = 300
    print(a)
    # Output:
    # [[100  17   1]
    #  [ 31  11   3]
    #  [ 33  32  12]]

    # np.copyto() 函数用于将一个数组的内容复制到另一个数组
    e = np.zeros(shape=a.shape)
    print(e)
    # Output:
    # [[0. 0. 0.]
    #  [0. 0. 0.]
    #  [0. 0. 0.]]
    np.copyto(e, a)
    print(e)
    # Output:
    # [[100.  17.   1.]
    #  [ 31.  11.   3.]
    #  [ 33.  32.  12.]]


if __name__ == '__main__':
    main()
