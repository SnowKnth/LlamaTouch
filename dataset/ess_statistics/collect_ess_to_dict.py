import os
import json

def collect_ess_files(root_dir, output_file):
    ess_dict = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.ess'):
                # 构建唯一索引key：用相对路径+文件名（不含root_dir前缀）
                rel_path = os.path.relpath(os.path.join(dirpath, filename), root_dir)
                key = rel_path.replace(os.sep, '/')  # 用/分隔，便于跨平台
                # 读取ess内容
                with open(os.path.join(dirpath, filename), 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                ess_dict[key] = content
    # 输出到文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(ess_dict, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    # 修改为你的实际路径
    root = '../llamatouch_dataset_0521'
    output = 'all_ess_content.json'
    collect_ess_files(root, output)
    print(f'All .ess content collected to {output}')
