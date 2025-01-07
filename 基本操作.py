import time
import numpy as np


def main():
    np.random.seed(int(time.time()))
    a = np.random.randint(1, 20, (3, 4))
    print(a)
    # Output:
    # [[17 11  6  1]
    #  [13 12  6  4]
    #  [10  7 13 14]]

    # 对数组 a 进行转置操作
    data = a.T
    print(data)
    # Output:
    # [[17 13 10]
    #  [11 12  7]
    #  [ 6  6 13]
    #  [ 1  4 14]]

    # 同 a.T
    data = np.transpose(a)
    print(data)
    # Output:
    # [[17 13 10]
    #  [11 12  7]
    #  [ 6  6 13]
    #  [ 1  4 14]]

    # 将数组 a 展平为一维数组
    data = a.flatten()
    print(data)
    # Output:
    # [17 11  6  1 13 12  6  4 10  7 13 14]

    # 将数组 a 展平为一维数组, 比 flatten 效率高
    data = a.ravel()
    print(data)
    # Output:
    # [17 11  6  1 13 12  6  4 10  7 13 14]

    # 改变数组的形状
    # -1：自动计算对应的维度大小，使新数组的总元素数保持一致
    # 新形状必须保证元素总数与原数组一致，否则会抛出错误
    data = a.reshape(2, -1)
    print(data)
    # Output:
    # [[17 11  6  1 13 12]
    #  [ 6  4 10  7 13 14]]

    # 直接修改数组的形状，不会返回新数组，而是在原地修改数组的形状
    a.resize(1, 12)
    print(a)
    # Output:
    # [[17 11  6  1 13 12  6  4 10  7 13 14]]

    a = np.random.randint(1, 50, (3, 3))
    print(a)
    # Output:
    # [[ 8 12 13]
    #  [11 39 42]
    #  [44 48 21]]
    b = np.ones((3, 3))
    # 将数组 b 的元素添加到数组 a 的末尾的函数
    data = np.append(a, b)
    print(data)
    # Output:
    # [ 8. 12. 13. 11. 39. 42. 44. 48. 21.  1.  1.  1.  1.  1.  1.  1.  1.  1.]

    # 合并多个数组, 比 np.append 更高效
    # 但要求输入数组形状完全匹配（不会自动展平）
    data = np.concatenate((a, b), axis=0)
    print(data)
    # Output:
    # [[ 8. 12. 13.]
    #  [11. 39. 42.]
    #  [44. 48. 21.]
    #  [ 1.  1.  1.]
    #  [ 1.  1.  1.]
    #  [ 1.  1.  1.]]

    # 向数组的指定位置插入值
    data = np.insert(a, 2, [100, 111, 222], axis=0)
    print(data)
    # Output:
    # [[  8  12  13]
    #  [ 11  39  42]
    #  [100 111 222]
    #  [ 44  48  21]]

    # 删除数组中指定索引位置的元素
    data = np.delete(a, [1, 3])
    print(data)
    # Output:
    # [ 8 13 39 42 44 48 21]

    # 垂直堆叠数组, 将数组沿着垂直方向（行方向）进行拼接
    data = np.r_[a, b]
    print(data)
    # Output:
    # [[ 8. 12. 13.]
    #  [11. 39. 42.]
    #  [44. 48. 21.]
    #  [ 1.  1.  1.]
    #  [ 1.  1.  1.]
    #  [ 1.  1.  1.]]

    # 同 np.r_[a, b]
    data = np.vstack((a, b))
    print(data)
    # Output:
    # [[ 8. 12. 13.]
    #  [11. 39. 42.]
    #  [44. 48. 21.]
    #  [ 1.  1.  1.]
    #  [ 1.  1.  1.]
    #  [ 1.  1.  1.]]

    # 水平堆叠数组, 将数组沿着水平方向（列方向）进行拼接
    data = np.hstack((a, b))
    print(data)
    # Output:
    # [[ 8. 12. 13.  1.  1.  1.]
    #  [11. 39. 42.  1.  1.  1.]
    #  [44. 48. 21.  1.  1.  1.]]

    # 将多个数组按列进行堆叠
    data = np.c_[a, b]
    print(data)
    # Output:
    # [[ 8. 12. 13.  1.  1.  1.]
    #  [11. 39. 42.  1.  1.  1.]
    #  [44. 48. 21.  1.  1.  1.]]

    # 同 np.c_[a, b]
    data = np.column_stack((a, b))
    print(data)
    # Output:
    # [[ 8. 12. 13.  1.  1.  1.]
    #  [11. 39. 42.  1.  1.  1.]
    #  [44. 48. 21.  1.  1.  1.]]

    # 将数组沿水平方向（列方向）分割成多个子数组
    data = np.hsplit(a, 3)
    print(data)
    # Output:
    # [array([[ 8],
    #        [11],
    #        [44]]), array([[12],
    #        [39],
    #        [48]]), array([[13],
    #        [42],
    #        [21]])]

    # 将数组沿垂直方向（行方向）分割成多个子数组
    data = np.vsplit(a, 3)
    print(data)
    # Output:
    # [array([[ 8, 12, 13]]), array([[11, 39, 42]]), array([[44, 48, 21]])]


if __name__ == '__main__':
    main()
