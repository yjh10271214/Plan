#!/bin/bash

#定义参数的数组，每组参数是"input output size save_every"
input_file="test.mp4"
output_dir="output_frames"
params=("320 5" "416 10" "512 10" "640 10" "800 20")

#创建/清空 CSV 文件，并写入表头
echo "size,save_every,total_time,avg_ms" > results.csv

#遍历
for p in "${params[@]}"; do
    size=$(echo $p | awk '{print $1}')
    save_every=$(echo $p | awk '{print $2}')

    echo "正在运行: size=${size}, save_every=${save_every}"
    output=$(python main.py --input "${input_file}" --output_dir "${output_dir}" \
        --size "${size}" --save_every "${save_every}" 2>&1)

    total_time=$(echo "$output" | grep "total take up times" | sed -E 's/.*total take up times: ([0-9.]+).*/\1/')
    avg_ms=$(echo "$output" | grep "average" | sed -E 's/.*average: ([0-9.]+).*/\1/')

    #将结果追加写入 CSV 文件
    echo "${size},${save_every},${total_time},${avg_ms}" >> results.csv
done

echo "experiment successfully, result saved to results.csv file"