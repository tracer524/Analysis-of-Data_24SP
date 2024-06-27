import pandas as pd
import numpy as np
df = pd.read_csv('data2.csv')

columns_with_missing_values = df.columns[df.isnull().any()].tolist()

# Print the column names with missing values
print("Columns with missing values:")
print(columns_with_missing_values)

# Remove the rows with missing values
df = df.dropna()

print("Value distribution for 'tumor-size' before corrections:")
print(df['tumor-size'].value_counts())

print("\nValue distribution for 'inv-nodes' before corrections:")
print(df['inv-nodes'].value_counts())

# Define a correction mapping for date-like entries
correction_map_tumor_size = {
    '14-Oct' : '10-14',
    '9-May' : '5-9' 
}

correction_map_inv_nodes = {
    '5-Mar' : '3-5',
    '8-Jun' : '6-8',
    '11-Sep' : '9-11',
    '14-Dec' : '12-14'
}

# Apply corrections
df['tumor-size'] = df['tumor-size'].replace(correction_map_tumor_size)
df['inv-nodes'] = df['inv-nodes'].replace(correction_map_inv_nodes)

# Verify the corrections
print("\nCorrected value distribution for 'tumor-size':")
print(df['tumor-size'].value_counts())

print("\nCorrected value distribution for 'inv-nodes':")
print(df['inv-nodes'].value_counts())

# 加载Excel文件
variables_df = pd.read_excel('variables.xlsx')

ind2val = {}
current_index = 0

# 对每个变量的每个值进行遍历并分配索引
for i, row in variables_df.iterrows():
    variable_name = row['Variable Name']
    values = row['Description'].split(', ')
    for value in values:
        ind2val[current_index] = f"{variable_name}={value}"
        current_index += 1

# 创建从值到索引的逆映射字典
val2ind = {v: k for k, v in ind2val.items()}

# 替换数据集中的文本属性
for column in df.columns:
    if column in variables_df['Variable Name'].values:
        # 为每个列值构建一个映射函数
        df[column] = df[column].apply(lambda x: val2ind[f"{column}={x}"])

# 打印ind2val字典
for key in list(ind2val.keys()):
    print(key, ind2val[key])