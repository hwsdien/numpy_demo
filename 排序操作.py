import time
import numpy as np


def main():
    np.random.seed(int(time.time()))
    a = np.random.randint(1, 50, (5, 4))
    print(a)
    # Output:
    # [[ 2 20 44 35]
    #  [49 24 48 28]
    #  [25 29 15 33]
    #  [13 11 47 42]
    #  [24 33  6 37]]

    b = np.copy(a)

    # 调用 a.sort() 会对数组 a 进行排序，并且这个排序是原地进行的，即直接修改 a 数组，而不返回一个新的数组
    # 默认 axis=-1, 即对最后一个维度进行排序，二维数组的话，即对列进行按行排序，默认为升序
    a.sort()
    print(a)
    # Output:
    # [[ 2 20 35 44]
    #  [24 28 48 49]
    #  [15 25 29 33]
    #  [11 13 42 47]
    #  [ 6 24 33 37]]

    # 修改成对第1个维度进行排序，即对行进行按列排序，默认为升序
    a = b.copy()
    a.sort(axis=0)
    print(a)
    # Output:
    # [[ 2 11  6 28]
    #  [13 20 15 33]
    #  [24 24 44 35]
    #  [25 29 47 37]
    #  [49 33 48 42]]

    # 得到降序排序的数组
    a = b.copy()
    a.sort()
    print(a)
    # Output:
    # [[ 2 20 35 44]
    #  [24 28 48 49]
    #  [15 25 29 33]
    #  [11 13 42 47]
    #  [ 6 24 33 37]]

    a = a[:, ::-1]
    print(a)
    # Output:
    # [[44 35 20  2]
    #  [49 48 28 24]
    #  [33 29 25 15]
    #  [47 42 13 11]
    #  [37 33 24  6]]

    my_data_type = [('name', 'U10'), ('age', 'i4')]
    data = np.array([('Alice', 25), ('Bob', 30), ('Charlie', 20)], dtype=my_data_type)

    # 按 'age' 字段进行排序
    data.sort(order='age')  # 默认是升序排序
    print(data)
    # Output:
    # [('Charlie', 20) ('Alice', 25) ('Bob', 30)]

    # 得到降序排序数据
    data = data[::-1]
    print(data)
    # Output:
    # [('Bob', 30) ('Alice', 25) ('Charlie', 20)]


if __name__ == '__main__':
    main()
