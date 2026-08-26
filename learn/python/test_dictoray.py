d = {"name": "Tom", "age": 20}

# 常用方法
d["name"]           # 'Tom'，按键取值
d.get("name")       # 'Tom'，键不存在返回 None
d.get("xx", "默认值")  # 键不存在返回默认值
d.keys()            # dict_keys(['name', 'age'])
d.values()          # dict_values(['Tom', 20])
d.items()           # dict_items([('name','Tom'), ('age',20)])
d.update({"sex": "male"})  # 添加或更新
d.pop("age")        # 删除并返回值
d.clear()           # 清空

# 遍历
for k, v in d.items():
    print(k, v)