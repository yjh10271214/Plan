"""
NumPy 数组中，每一个维度就是一个轴（axis）。
轴的编号从 0 开始，对应数组的第 0 维、第 1 维、第 2 维……
"""

import numpy as np
# transpose 后数组可能不连续
# 可以用 np.ascontiguousarray() 强制变成连续数组。
# img_contiguous = np.ascontiguousarray(img)

a = np.random.rand(2, 3, 4)

print(a.shape)
print(a.ndim)
print(a.size)

print(a.sum(axis=0).shape)
print(a.sum(axis=1).shape)
print(a.sum(axis=2).shape)

a = a.transpose(1, 0, 2)
print(a)


img_hwc = np.random.rand(4, 5, 3)   # 4高 5宽 3通道
print("CHW shape:", img_hwc.shape)

img_chw = img_hwc.transpose(2, 0, 1)
print("CHW shape:", img_chw.shape)

img_hwc_back = img_chw.transpose(1, 2, 0)
print("HWC back shape:", img_hwc_back.shape)

# 8. 检查数组是否连续
print("img_hwc contiguous?", img_hwc.flags['C_CONTIGUOUS'])
print("img_chw contiguous?", img_chw.flags['C_CONTIGUOUS'])
print("img_hwc_back contiguous?", img_hwc_back.flags['C_CONTIGUOUS'])

# 9. 使用 np.ascontiguousarray 把不连续变成连续
img_chw_cont = np.ascontiguousarray(img_chw)
print("img_chw_cont contiguous?", img_chw_cont.flags['C_CONTIGUOUS'])


#深度学习CHW通道在前内存连续的话每一个通道的数据就是连续的








