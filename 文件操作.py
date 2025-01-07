import time
import numpy as np


def main():
    np.random.seed(int(time.time()))
    a = np.random.randint(1, 50, (3, 3))
    print(a)
    # Output:
    # [[23 35 19]
    #  [18 28  3]
    #  [10  5  6]]
    b = np.random.randint(1, 50, (3, 3))
    print(b)
    # Output:
    # [[35 29 36]
    #  [ 6  6  1]
    #  [14 39 43]]

    # 将单个数组保存到一个 .npy 文件中
    # .npy 文件是 NumPy 的二进制格式文件，用于存储数组及其元数据（如形状、数据类型等）
    np.save('my_array', a)

    # 加载保存的 .npy 文件
    c = np.load('my_array.npy')
    print(c)
    # Output:
    # [[23 35 19]
    #  [18 28  3]
    #  [10  5  6]]

    # 将多个数组保存到一个 .npz 文件中
    # .npz 文件是一个压缩格式，包含多个数组
    np.savez('my_array.npz', key1=a, key2=b)

    # 加载保存的 .npz 文件，它返回一个 NpzFile 对象，类似字典，可以按键访问其中的数组
    d = np.load('my_array.npz')
    print(d['key2'])
    # Output:
    # [[35 29 36]
    #  [ 6  6  1]
    #  [14 39 43]]

    # 将数组保存到文本文件中，可以指定分隔符、格式、是否包含头部信息等参数
    np.savetxt('data.txt', a, delimiter=",")

    # 从文本文件加载数据
    e = np.genfromtxt('data.txt', delimiter=",")
    print(e)
    # Output:
    # [[23. 35. 19.]
    #  [18. 28.  3.]
    #  [10.  5.  6.]]

    # 从文本文件中加载数据
    # 与 np.genfromtxt 类似, 但它假设文件中的数据是规则的（即没有缺失值）
    f = np.loadtxt('data.txt', delimiter=",")
    print(f)
    # Output:
    # [[23. 35. 19.]
    #  [18. 28.  3.]
    #  [10.  5.  6.]]

    # 将 NumPy 数组 a 写入名为 my_data.bin 的二进制文件
    # 与 np.save 的区别：np.tofile 不包含额外的元数据，如数组的形状
    a.tofile('my_data.bin')

    # 从 my_data.bin 文件中读取数据，并按整数类型返回一个新的 NumPy 一维数组
    g = np.fromfile('my_data.bin', dtype=np.int64)
    print(g)
    # Output:
    # [23 35 19 18 28  3 10  5  6]
    print(np.reshape(g, a.shape))
    # Output:
    # [[23 35 19]
    #  [18 28  3]
    #  [10  5  6]]


if __name__ == '__main__':
    main()
