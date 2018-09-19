"""
冒泡排序--改进版

target: 对于某些有序的序列，下一次遍历时就不用再比较了。
        最理想的是整个序列本就有序，如此，k=0，只遍历一遍就完成了。

初始元素序列：    8, 3, 2, 5, 9, 3, 6
第一趟排序：      3, 2, 5, 8, 3, 6,[9]
第二趟排序：      2, 3, 5, 3, 6,[8, 9]
第三趟排序：      2, 3, 3, 5,[6, 8, 9]
第四趟排序：      2, 3, 3,[5, 6, 8, 9]
第五趟排序：      2, 3,[3, 5, 6, 8, 9]
第六趟排序：      2,[3, 3, 5, 6, 8, 9]
"""


def bubble(a):
    print(f'排序前：{a}')
    n = len(a)
    i = n - 1
    counter = 0
    while i > 0:
        k = j = 0
        while j < i:
            if a[j] > a[j + 1]:
                t = a[j]
                a[j] = a[j + 1]
                a[j + 1] = t
                k = j  # 如有交换发生，记录最小元素的下标
            j = j + 1
        i = k
        counter = counter + 1
        print(f'第{counter}趟排序结果：{a}')
    print(f'排序后：{a}')


bubble([8, 3, 2, 5, 9, 3, 6])
