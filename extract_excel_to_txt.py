import os
import glob
import pandas as pd

def excel_to_txt(input_folder, output_folder):
    """
    将指定目录下的所有Excel文件转换为TXT文本文件（使用制表符分隔）。
    如果Excel中有多个Sheet，会分别导出到不同的TXT文件中。
    """
    # 查找输入目录下所有的 '附件*.xlsx' 文件
    excel_files = glob.glob(os.path.join(input_folder, '附件*.xlsx'))
    
    if not excel_files:
        print(f"在 '{input_folder}' 目录下未找到任何 '附件*.xlsx' 文件。")
        return

    # 确保输出目录存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"已创建输出文件夹：{output_folder}")

    for file_path in excel_files:
        try:
            # 提取不带后缀的文件名
            base_name = os.path.basename(file_path)
            file_name = os.path.splitext(base_name)[0]
            
            # 读取所有Sheet的内容
            # sheet_name=None 表示以字典形式返回所有sheet (key为sheet名, value为dataframe)
            sheets_dict = pd.read_excel(file_path, sheet_name=None)
            
            if len(sheets_dict) == 1:
                # 如果只有一个Sheet，txt文件名就不带Sheet名了
                sheet_name = list(sheets_dict.keys())[0]
                df = sheets_dict[sheet_name]
                out_path = os.path.join(output_folder, f"{file_name}.txt")
                df.to_csv(out_path, sep='\t', index=False)
                print(f"成功导出: {out_path}")
            else:
                # 多个Sheet则在文件名后附加Sheet名称
                for sheet_name, df in sheets_dict.items():
                    # 避免Sheet名中包含路径分隔符等特殊字符
                    safe_sheet_name = str(sheet_name).replace('/', '_').replace('\\', '_')
                    out_path = os.path.join(output_folder, f"{file_name}_{safe_sheet_name}.txt")
                    df.to_csv(out_path, sep='\t', index=False)
                    print(f"成功导出: {out_path}")
                    
        except Exception as e:
            print(f"[-] 处理文件 '{file_path}' 时出错: {e}")
            print("请确保已安装所需依赖：pip install pandas openpyxl")

    print("\n所有附件数据已成功提取为TXT！")

if __name__ == '__main__':
    # 你的附件存放在 'A题' 目录下
    INPUT_FOLDER = 'A题'
    # 提取后的 TXT 将保存在 'A题_txt格式数据' 文件夹中
    OUTPUT_FOLDER = 'A题_txt格式数据'
    
    excel_to_txt(INPUT_FOLDER, OUTPUT_FOLDER)
