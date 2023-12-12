import csv
import os

def generate_interface(csv_file):
    interface_name = os.path.splitext(os.path.basename(csv_file))[0]  # 获取 CSV 文件的名称（不包含扩展名）
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # 获取第一行数据
        variable_names = next(reader)  # 获取第二行数据
        variable_types = next(reader)  # 获取第三行数据

        interface_string = f"/**{interface_name} */\ninterface {interface_name} " + "{\n"
        for i in range(len(header)):
            if header[i]:  # 只处理非空单元格
                variable_type = "string"  # 默认为字符串类型
                if variable_types[i].isdigit():  # 如果第三行单元格内容为数字，则为数字类型
                    variable_type = "number"

                interface_string += f"    // {header[i]}\n"
                interface_string += f"    {variable_names[i]}: {variable_type},\n"

        interface_string += "}"

        return interface_string

# 用法示例
csv_files = input("请输入CSV文件路径（多个文件请用空格分隔）：").split()  # 用户输入CSV文件路径列表

for csv_file in csv_files:
    csv_file = csv_file.strip()  # 去除路径中的空白字符
    interface = generate_interface(csv_file)
    print(interface)
    print("\n")

input("按任意键退出...")
