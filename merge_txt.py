import os
import glob

def merge_txt_files(input_folder, output_file):
    """
    将指定目录下的所有TXT文件合并成一个文件。
    在写入每个文件的数据之前，先写入该文件的文件名作为标识。
    """
    # 查找所有的 txt 文件
    txt_files = glob.glob(os.path.join(input_folder, '*.txt'))
    
    if not txt_files:
        print(f"在 '{input_folder}' 目录下未找到任何 TXT 文件。")
        return

    # 按文件名排个序，这样合并出来的文件顺序更清晰
    txt_files.sort()

    # 打开合并后的目标文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_path in txt_files:
            file_name = os.path.basename(file_path)
            
            # 写入文件名作为头部标识
            outfile.write(f"========== {file_name} ==========\n")
            
            try:
                # 读取原 TXT 文件内容并写入
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
            except Exception as e:
                print(f"[-] 读取文件 {file_name} 时出错: {e}")
                
            # 在每个文件内容结束后多加两个换行，方便区分
            outfile.write("\n\n")
            print(f"已合并: {file_name}")

    print(f"\n所有TXT文件已成功合并到: {output_file}")

if __name__ == '__main__':
    INPUT_FOLDER = 'A题_txt格式数据'
    OUTPUT_FILE = '所有附件合并数据.txt'
    
    merge_txt_files(INPUT_FOLDER, OUTPUT_FILE)
