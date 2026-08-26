lst = [1, 2, 3, 4, 5]

# 常用方法
lst.append(6)        # [1,2,3,4,5,6] 末尾添加
lst.insert(0, 0)     # [0,1,2,3,4,5,6] 在指定位置插入
lst.remove(3)        # 删除第一个值为 3 的元素
lst.pop()            # 删除并返回最后一个元素
lst.pop(0)           # 删除并返回第一个元素
lst.index(2)         # 返回 2 的下标
lst.count(1)         # 统计 1 出现次数
lst.sort()           # 原地排序
lst.reverse()        # 原地反转
len(lst)             # 长度

# 切片
lst[1:3]             # [2,3]
lst[::-1]            # 反转
lst[::2]             # 每隔一个取一个

# 列表推导式
[x**2 for x in range(10)]                    # [0,1,4,9,...]
[x for x in range(10) if x % 2 == 0]         # 偶数
[x if x > 0 else -x for x in [-1,2,-3]]      # [1,2,3]