import random


def merge_sort(seq):
    '''归并排序'''
    if len(seq) <= 1:  # 递归出口
        return seq

    # 中间位置
    mid = len(seq) // 2

    # 递归拆分成左右两个部分
    left_half = merge_sort(seq[:mid])
    right_half = merge_sort(seq[mid:])

    # 再将排好序的合并回去
    new_sort_list = merge_sort_list(left_half, right_half)
    return new_sort_list


def merge_sort_list(sort_a, sort_b):
    '''
        合并两个有序列表
    :param sort_a: 有序列表a
    :param sort_b: 有序列表b
    '''
    a = b = 0
    length_a, length_b = len(sort_a), len(sort_b)
    new_sort_list = []

    while a < length_a and b < length_b:
        if sort_a[a] < sort_b[b]:
            new_sort_list.append(sort_a[a])
            a += 1
        else:
            new_sort_list.append(sort_b[b])
            b += 1

    # 把多余的列表元素追加到new_sort_list
    while a < length_a:
        new_sort_list.append(sort_a[a])
        a += 1

    while b < length_b:
        new_sort_list.append(sort_b[b])
        b += 1

    return new_sort_list


def test_merge_sort():
    seq = list(range(1, 10))
    random.shuffle(seq)
    assert merge_sort(seq) == sorted(seq)
    # assert 0