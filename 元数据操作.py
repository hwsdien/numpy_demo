import time
import numpy as np


def main():
    np.random.seed(int(time.time()))
    a = np.random.randint(1, 50, (3, 4))
    print(a)
    # Output:
    # [[44 36 41 47]
    #  [21  5 35 45]
    #  [15 30 14 25]]

    # 数组的形状，表示每个维度的大小
    print(a.shape)
    # Output:
    # (3, 4)

    # 数组元素的类型
    print(a.dtype)
    # Output:
    # int64

    # 数组中元素的数据类型名称，返回的是字符串
    print(a.dtype.name)
    # Output:
    # int64
    print(type(a.dtype.name))
    # Output:
    # <class 'str'>

    # 转换成指定的数据类型，会创新一个新的数组
    print(a.astype(np.float64))
    # Output:
    # [[44. 36. 41. 47.]
    #  [21.  5. 35. 45.]
    #  [15. 30. 14. 25.]]

    # 数组的字节序（小端或大端）
    # =：与系统本地字节序相同（native byte order）
    # <：小端字节序（little-endian），低字节在前
    # >：大端字节序（big-endian），高字节在前
    # |：不适用字节序的类型，例如 np.str_ 或 np.bool_
    print(a.dtype.byteorder)
    # Output:
    # =

    # 数组的维数
    print(a.ndim)
    # Output:
    # 2

    # 数组中元素的总个数
    print(a.size)
    # Output:
    # 12

    # 数组中每个元素占用的字节数
    print(a.itemsize)
    # Output:
    # 8

    # 整个数组占用的字节数
    print(a.nbytes)
    # Output:
    # 96

    # 沿每个维度步进的字节数，用于解释数组在内存中的布局
    print(a.strides)
    # Output:
    # (32, 8)
    # 说明: 每行 32 字节（4*8），每列 8 字节

    # 数组的内存布局信息，例如是否是连续的
    print(a.flags)
    # Output:
    #   C_CONTIGUOUS : True
    #   F_CONTIGUOUS : False
    #   OWNDATA : True
    #   WRITEABLE : True
    #   ALIGNED : True
    #   WRITEBACKIFCOPY : False

    # 数组的内存布局, 是否是行优先（C-style）存储
    print(a.flags.c_contiguous)
    # Output:
    # True

    # 数组的内存布局, 是否是列优先（Fortran-style）存储
    print(a.flags.f_contiguous)
    # Output:
    # False

    # 判断数组是否拥有自身的数据或引用了其他数组的数据
    print(a.flags.owndata)
    # Output:
    # True

    # 如果数组是由另一个数组派生的，则可以通过 a.base 查看其基对象
    print(a.base)
    # Output:
    # None

    # 返回数组的第一个维度的大小
    print(len(a))
    # Output:
    # 3


if __name__ == '__main__':
    main()
