import time
import numpy as np


def main():
    np.random.seed(int(time.time()))
    # 有符号整数
    # np.int8：8 位整数，取值范围：-128 到 127
    a = np.random.randint(-128, 127, (2, 3), dtype=np.int8)
    print(a.dtype)
    # Output:
    # int8

    # 16 位整数，取值范围：-32,768 到 32,767
    a = np.random.randint(-32768, 32767, (2, 3), dtype=np.int16)
    print(a.dtype)
    # Output:
    # int16

    # 32 位整数，取值范围：-2,147,483,648 到 2,147,483,647
    a = np.random.randint(-2147483648, -2147483647, (2, 3), dtype=np.int32)
    print(a.dtype)
    # Output:
    # int32

    # 64 位整数，取值范围：-9,223,372,036,854,775,808 到 9,223,372,036,854,775,807
    a = np.random.randint(-9223372036854775808, -9223372036854775807, (2, 3), dtype=np.int64)
    print(a.dtype)
    # Output:
    # int64

    # 无符号整数
    # 8 位无符号整数，取值范围：0 到 255
    a = np.random.randint(0, 255, (3, 4), dtype=np.uint8)
    print(a.dtype)
    # Output:
    # uint8

    # 16 位无符号整数，取值范围：0 到 65,535
    a = np.random.randint(0, 65535, (3, 4), dtype=np.uint16)
    print(a.dtype)
    # Output:
    # uint16

    # 32 位无符号整数，取值范围：0 到 4294967295
    a = np.random.randint(0, 4294967295, (3, 4), dtype=np.uint32)
    print(a.dtype)
    # Output:
    # uint32

    # 64 位无符号整数，取值范围：0 到 18446744073709551615
    a = np.random.randint(0, 18446744073709551615, (3, 4), dtype=np.uint64)
    print(a.dtype)
    # Output:
    # uint64

    # 浮点数类型
    # 16 位半精度浮点数
    a = np.random.uniform(1, 10, (2, 3))
    a = a.astype(np.float16)
    print(a.dtype)
    # Output:
    # float16

    # 32 位单精度浮点数
    a = a.astype(np.float32)
    print(a.dtype)
    # Output:
    # float32

    # 64 位双精度浮点数（默认浮点类型）
    a = a.astype(np.float64)
    print(a.dtype)
    # Output:
    # float64

    # 复数类型
    # 表示每个复数包含 32 位的实部和 32 位的虚部
    a = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype=np.complex64)
    print(a.dtype)
    # Output:
    # complex64

    # 每个复数包含 64 位的实部和 64 位的虚部
    a = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype=np.complex128)
    print(a.dtype)
    # Output:
    # complex128

    # 字符串类型
    # np.str_ 是 NumPy 中的字符串类型，通常用来表示 Unicode 字符串，它等价于 Python 中的 str 类型
    a = np.array(['Hello', 'Hwsdien'], dtype=np.str_)
    print(a.dtype)
    # Output:
    # <U7
    # 说明: <U7 表示每个字符串最多可以有 7 个字符

    a = np.array([b'Hello', b'Hwsdien'], dtype=np.bytes_)
    print(a.dtype)
    # Output:
    # |S7
    # 说明: |S7 表示每个字符串最多可以有 7 个字节

    # 日期时间类型
    # np.datetime64 用于表示日期和时间，支持各种时间单位（如年、月、日、小时、分钟、秒等）。它能够精确表示时间戳，并且与 Python 的标准库 datetime 兼容
    a = np.datetime64('2025-01-04T00:30:37')
    print(a)
    # Output:
    # 2025-01-04T00:30:37
    print(a.dtype)
    # Output:
    # datetime64[s]

    # np.timedelta64 用于表示时间间隔（时间差），它是 np.datetime64 的补充，可以表示任意单位的时间差（如秒、分钟、小时、天、月、年等）
    # 3个小时
    time_diff_hours = np.timedelta64(3, 'h')
    # 5天
    time_diff = np.timedelta64(5, 'D')
    a = a + time_diff_hours
    print(a)
    # Output:
    # 2025-01-04T03:30:37

    # 布尔类型
    a = np.array([True, False, True, False], dtype=np.bool_)
    print(a.dtype)
    # Output:
    # bool

    # 复合数据类型
    # 结构化数组：可以通过为数组的每个元素定义多个字段（每个字段有一个特定的数据类型）来存储不同类型的数据
    # 先定义一个数据类型
    my_data_type = np.dtype([('name', 'U10'), ('age', 'i4'), ('height', 'f4')])
    # 使用定义的数据类型
    a = np.array([('Alice', 25, 5.5), ('Bob', 30, 5.8), ('Charlie', 35, 5.9)], dtype=my_data_type)
    print(a)
    # Output:
    # [('Alice', 25, 5.5) ('Bob', 30, 5.8) ('Charlie', 35, 5.9)]
    print(a.dtype)
    # Output:
    # [('name', '<U10'), ('age', '<i4'), ('height', '<f4')]

    # 记录数组：是结构化数组的一种扩展，与结构化数组不同，记录数组允许使用字段名访问数组的字段
    a = np.recarray(3, dtype=my_data_type)
    a.name = ['Alice', 'Bob', 'Charlie']
    a.age = [25, 30, 35]
    a.height = [5.5, 5.8, 5.9]
    print(a.name)
    # Output:
    # ['Alice' 'Bob' 'Charlie']
    print(a.dtype)
    # Output:
    # (numpy.record, [('name', '<U10'), ('age', '<i4'), ('height', '<f4')])

    # 对象类型
    # object 是用于表示 Python 对象类型的 NumPy 数据类型。
    a = np.array([{'name': 'Alice'}, [1, 2, 3], 'hello'], dtype=object)
    print(a.dtype)
    # Output:
    # object

    # 特殊类型
    # np.void 是用于表示不确定的类型，或者是用于存储原始数据类型的“无类型”占位符。
    a = np.array([np.void(b'hello'), np.void(b'world')])
    print(a.dtype)
    # Output:
    # |V5

    # 常用的 NumPy 数据类型及其表示规则
    # 符号	描述	示例
    # 'b'	布尔类型（bool）	'b1'（1 字节）
    # 'i'	有符号整数（signed integer）	'i1'（1 字节）、'i2'（2 字节）、'i4'（4 字节）、'i8'（8 字节）
    # 'u'	无符号整数（unsigned integer）	'u1'（1 字节）、'u2'（2 字节）、'u4'（4 字节）、'u8'（8 字节）
    # 'f'	浮点数（float）	'f4'（4 字节，单精度）、'f8'（8 字节，双精度）
    # 'c'	复数数值（complex number）	'c8'（8 字节复数）
    # 'S'	字节字符串（byte string）	'S10'（最大长度为 10 的字节字符串）
    # 'U'	Unicode 字符串	'U10'（最大长度为 10 的 Unicode 字符串）
    # 'M'	时间（datetime）	'M8[D]'（日期格式）
    # 'm'	时间差（timedelta）	'm8[D]'（日期差）
    # 'O'	Python 对象（object）	'O'（Python 对象类型）


if __name__ == '__main__':
    main()