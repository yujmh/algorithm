"""
直接插入排序

算法描述：
    每步将一个待排序元素，插入到前面已经排好序的一组元素的适当位置上，直到全部元素插入为止。

过程举例：
初始元素序列：    [8], 3, 2, 5, 9, 3, 6
第一趟排序：      [3, 8], 2, 5, 9, 3, 6
第二趟排序：      [2, 3, 8], 5, 9, 3, 6
第三趟排序：      [2, 3, 5, 8], 9, 3, 6
第四趟排序：      [2, 3, 5, 8, 9], 3, 6
第五趟排序：      [2, 3, 3, 5, 8, 9], 6
第六趟排序：      [2, 3, 3, 5, 6, 8, 9]

直接排序算法时稳定的算法，也是三种排序算法（冒泡、直接选择、直接插入）中最快的。
"""


def insertion(a):
    print(f'排序前：{a}')
    n = len(a)
    counter = 0
    for i in range(1, n):
        t = a[i]  # 待比较元素t
        j = i - 1
        while j >= 0 and a[j] > t:
            a[j + 1] = a[j]  # 每次比较，将大于t的元素后移一位
            j -= 1
        a[j + 1] = t  # 最终下标j的元素小于等于t
        counter += 1
        print(f'第{counter}趟排序：{a}')
    print(f'排序后：{a}')


insertion([8, 3, 2, 5, 9, 3, 6])
