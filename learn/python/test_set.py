s = {1, 2, 3, 3, 4}
print(s)            # {1,2,3,4} 自动去重

# 常用方法
s.add(5)            # 添加
s.remove(2)         # 删除，不存在报错
s.discard(2)        # 删除，不存在不报错
s.union({5,6})      # 并集
s.intersection({3,4,5})  # 交集
s.difference({1})   # 差集

# 去重
lst = [1,2,2,3]
list(set(lst))       # [1,2,3]，但顺序可能变
list(dict.fromkeys(lst))  # [1,2,3]，保持原顺序