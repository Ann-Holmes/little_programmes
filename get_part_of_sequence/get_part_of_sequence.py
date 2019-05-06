#  输入读取文件和输出文件名称(绝对路径)
input_name = "expriment.fasta"
output_name = "expriment_front.fasta"
seq_dict = {}

# 读入文件到字典
with open(input_name) as fn:
    for line in fn:
        if line[0] == '>':
            key = line.strip()
            seq_dict[key] = []
        else:
            seq_dict[key].append(line.strip())
    #  去掉每行末尾的格式字符
    seq_dict_string = {key: ''.join(valueL) for key, valueL in seq_dict.items()}
    #  设置头尾
    seq_begin = 0
    seq_end = 80
    #  切割序列
    seq_dict_part_front = {key: value[:80] for key, value in seq_dict_string .items()}
    '''
    #  测试输出
    for key, value in seq_dict_string.items():
        print(key, '\n', value)
    for key, value in seq_dict_part_front.items():
        print(key, '\n', value)
    '''

    #  写入文件
    with open(output_name, 'w') as ef:
        for key, value in seq_dict_part_front.items():
            ef.writelines(key + '\n' + value + '\n')


